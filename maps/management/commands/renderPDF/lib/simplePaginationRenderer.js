var page = require('webpage').create(),
    system = require('system'),
    address, output;


if (system.args.length < 2 || system.args.length > 4) {
    console.log('Usage: renderPDF URL [OUTPUTFILE] [CONFIGFILE]');
    phantom.exit(1);
} else {
    address = system.args[1];
    if (system.args.length===2) {
	output = 'out.pdf';
    } else {
    	output = system.args[2];
    }
    page.viewportSize = {
        width: 600,
        height: 600
    };

    if (system.args.length===4) {
	phantom.injectJs('../'+system.args[3]);
    }
    phantom.injectJs('./simplePagination.js');	
    page.paperSize = {
	width: pagination.config('pageWidth') + pagination.config('lengthUnit'),
	height: pagination.config('pageHeight') + pagination.config('lengthUnit'),
	margin: '0px'
    }

    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
            phantom.exit();
        } else {
            page.onCallback = function (data) {
                page.render(output);
                phantom.exit();
            };
	
            page.injectJs('simplePagination.js');
	    if (typeof paginationConfig != 'undefined') {
		page.injectJs('../'+system.args[3]);
	    }
		
                page.evaluate(function () {
		    var extraStyle = document.createElement('style');
		    extraStyle.innerHTML= '.pagination-page{ border:solid 1px #fff;}';
		    document.head.appendChild(extraStyle);
//                    document.addEventListener('layoutFlowFinished', function () {
//setTimeOut( function() {
                        window.callPhantom({
                            action: 'done',
                        });
//}, 1000);
//                    }, false);


                    pagination.initiate();
		});
		if (pagination.config('divideContents')) {
		    page.evaluate(function () {
                        pagination.applyBookLayout();
                    });
		} else {
		    page.evaluate(function () {
                        pagination.applyBookLayoutWithoutDivision();
                    });
		}

        }

    });
}
