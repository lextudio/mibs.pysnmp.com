# SNMP MIB module (GWIAMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWIAMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:23 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_Gateways_ObjectIdentity = ObjectIdentity
gateways = _Gateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Gwia_ObjectIdentity = ObjectIdentity
gwia = _Gwia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 70)
)
_GwiaInfo_ObjectIdentity = ObjectIdentity
gwiaInfo = _GwiaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1)
)


class _GwiaGatewayName_Type(DisplayString):
    """Custom type gwiaGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwiaGatewayName_Type.__name__ = "DisplayString"
_GwiaGatewayName_Object = MibScalar
gwiaGatewayName = _GwiaGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 1),
    _GwiaGatewayName_Type()
)
gwiaGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaGatewayName.setStatus("mandatory")
_GwiaTimeUp_Type = TimeTicks
_GwiaTimeUp_Object = MibScalar
gwiaTimeUp = _GwiaTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 2),
    _GwiaTimeUp_Type()
)
gwiaTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaTimeUp.setStatus("mandatory")


class _GwiaLinkGroupWise_Type(DisplayString):
    """Custom type gwiaLinkGroupWise based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwiaLinkGroupWise_Type.__name__ = "DisplayString"
_GwiaLinkGroupWise_Object = MibScalar
gwiaLinkGroupWise = _GwiaLinkGroupWise_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 3),
    _GwiaLinkGroupWise_Type()
)
gwiaLinkGroupWise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLinkGroupWise.setStatus("mandatory")


class _GwiaLinkFrgn_Type(DisplayString):
    """Custom type gwiaLinkFrgn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwiaLinkFrgn_Type.__name__ = "DisplayString"
_GwiaLinkFrgn_Object = MibScalar
gwiaLinkFrgn = _GwiaLinkFrgn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 4),
    _GwiaLinkFrgn_Type()
)
gwiaLinkFrgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLinkFrgn.setStatus("mandatory")
_GwiaStatBytesOut_Type = Counter32
_GwiaStatBytesOut_Object = MibScalar
gwiaStatBytesOut = _GwiaStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 5),
    _GwiaStatBytesOut_Type()
)
gwiaStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatBytesOut.setStatus("mandatory")
_GwiaStatBytesIn_Type = Counter32
_GwiaStatBytesIn_Object = MibScalar
gwiaStatBytesIn = _GwiaStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 6),
    _GwiaStatBytesIn_Type()
)
gwiaStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatBytesIn.setStatus("mandatory")
_GwiaStatMsgsOut_Type = Counter32
_GwiaStatMsgsOut_Object = MibScalar
gwiaStatMsgsOut = _GwiaStatMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 7),
    _GwiaStatMsgsOut_Type()
)
gwiaStatMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatMsgsOut.setStatus("mandatory")
_GwiaStatMsgsIn_Type = Counter32
_GwiaStatMsgsIn_Object = MibScalar
gwiaStatMsgsIn = _GwiaStatMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 8),
    _GwiaStatMsgsIn_Type()
)
gwiaStatMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatMsgsIn.setStatus("mandatory")
_GwiaStatStatusesOut_Type = Counter32
_GwiaStatStatusesOut_Object = MibScalar
gwiaStatStatusesOut = _GwiaStatStatusesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 9),
    _GwiaStatStatusesOut_Type()
)
gwiaStatStatusesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatStatusesOut.setStatus("mandatory")
_GwiaStatStatusesIn_Type = Counter32
_GwiaStatStatusesIn_Object = MibScalar
gwiaStatStatusesIn = _GwiaStatStatusesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 10),
    _GwiaStatStatusesIn_Type()
)
gwiaStatStatusesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatStatusesIn.setStatus("mandatory")
_GwiaStatErrorsOut_Type = Counter32
_GwiaStatErrorsOut_Object = MibScalar
gwiaStatErrorsOut = _GwiaStatErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 11),
    _GwiaStatErrorsOut_Type()
)
gwiaStatErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatErrorsOut.setStatus("mandatory")
_GwiaStatErrorsIn_Type = Counter32
_GwiaStatErrorsIn_Object = MibScalar
gwiaStatErrorsIn = _GwiaStatErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 12),
    _GwiaStatErrorsIn_Type()
)
gwiaStatErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatErrorsIn.setStatus("mandatory")
_GwiaStatTimeReset_Type = TimeTicks
_GwiaStatTimeReset_Object = MibScalar
gwiaStatTimeReset = _GwiaStatTimeReset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 13),
    _GwiaStatTimeReset_Type()
)
gwiaStatTimeReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatTimeReset.setStatus("mandatory")
_GwiaQueueWpcsout_Type = Counter32
_GwiaQueueWpcsout_Object = MibScalar
gwiaQueueWpcsout = _GwiaQueueWpcsout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 14),
    _GwiaQueueWpcsout_Type()
)
gwiaQueueWpcsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaQueueWpcsout.setStatus("mandatory")
_GwiaQueueWpcsin_Type = Counter32
_GwiaQueueWpcsin_Object = MibScalar
gwiaQueueWpcsin = _GwiaQueueWpcsin_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 15),
    _GwiaQueueWpcsin_Type()
)
gwiaQueueWpcsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaQueueWpcsin.setStatus("mandatory")
_GwiaQueueGwhold_Type = Counter32
_GwiaQueueGwhold_Object = MibScalar
gwiaQueueGwhold = _GwiaQueueGwhold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 16),
    _GwiaQueueGwhold_Type()
)
gwiaQueueGwhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaQueueGwhold.setStatus("mandatory")
_GwiaQueueGwprob_Type = Counter32
_GwiaQueueGwprob_Object = MibScalar
gwiaQueueGwprob = _GwiaQueueGwprob_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 17),
    _GwiaQueueGwprob_Type()
)
gwiaQueueGwprob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaQueueGwprob.setStatus("mandatory")
_GwiaStatInterval_Type = TimeTicks
_GwiaStatInterval_Object = MibScalar
gwiaStatInterval = _GwiaStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 18),
    _GwiaStatInterval_Type()
)
gwiaStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatInterval.setStatus("mandatory")
_GwiaStatIntervalMsgsOut_Type = Counter32
_GwiaStatIntervalMsgsOut_Object = MibScalar
gwiaStatIntervalMsgsOut = _GwiaStatIntervalMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 19),
    _GwiaStatIntervalMsgsOut_Type()
)
gwiaStatIntervalMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalMsgsOut.setStatus("mandatory")
_GwiaStatIntervalMsgsIn_Type = Counter32
_GwiaStatIntervalMsgsIn_Object = MibScalar
gwiaStatIntervalMsgsIn = _GwiaStatIntervalMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 20),
    _GwiaStatIntervalMsgsIn_Type()
)
gwiaStatIntervalMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalMsgsIn.setStatus("mandatory")
_GwiaStatIntervalStatusesOut_Type = Counter32
_GwiaStatIntervalStatusesOut_Object = MibScalar
gwiaStatIntervalStatusesOut = _GwiaStatIntervalStatusesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 21),
    _GwiaStatIntervalStatusesOut_Type()
)
gwiaStatIntervalStatusesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalStatusesOut.setStatus("mandatory")
_GwiaStatIntervalStatusesIn_Type = Counter32
_GwiaStatIntervalStatusesIn_Object = MibScalar
gwiaStatIntervalStatusesIn = _GwiaStatIntervalStatusesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 22),
    _GwiaStatIntervalStatusesIn_Type()
)
gwiaStatIntervalStatusesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalStatusesIn.setStatus("mandatory")
_GwiaStatIntervalErrorsOut_Type = Counter32
_GwiaStatIntervalErrorsOut_Object = MibScalar
gwiaStatIntervalErrorsOut = _GwiaStatIntervalErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 23),
    _GwiaStatIntervalErrorsOut_Type()
)
gwiaStatIntervalErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalErrorsOut.setStatus("mandatory")
_GwiaStatIntervalErrorsIn_Type = Counter32
_GwiaStatIntervalErrorsIn_Object = MibScalar
gwiaStatIntervalErrorsIn = _GwiaStatIntervalErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 24),
    _GwiaStatIntervalErrorsIn_Type()
)
gwiaStatIntervalErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaStatIntervalErrorsIn.setStatus("mandatory")
_GwiaQThresholdCheckInterval_Type = Counter32
_GwiaQThresholdCheckInterval_Object = MibScalar
gwiaQThresholdCheckInterval = _GwiaQThresholdCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 25),
    _GwiaQThresholdCheckInterval_Type()
)
gwiaQThresholdCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaQThresholdCheckInterval.setStatus("mandatory")
_GwiaQThresholdWpcsout_Type = Counter32
_GwiaQThresholdWpcsout_Object = MibScalar
gwiaQThresholdWpcsout = _GwiaQThresholdWpcsout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 26),
    _GwiaQThresholdWpcsout_Type()
)
gwiaQThresholdWpcsout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaQThresholdWpcsout.setStatus("mandatory")
_GwiaQThresholdWpcsin_Type = Counter32
_GwiaQThresholdWpcsin_Object = MibScalar
gwiaQThresholdWpcsin = _GwiaQThresholdWpcsin_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 27),
    _GwiaQThresholdWpcsin_Type()
)
gwiaQThresholdWpcsin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaQThresholdWpcsin.setStatus("mandatory")
_GwiaQThresholdGwhold_Type = Counter32
_GwiaQThresholdGwhold_Object = MibScalar
gwiaQThresholdGwhold = _GwiaQThresholdGwhold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 28),
    _GwiaQThresholdGwhold_Type()
)
gwiaQThresholdGwhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaQThresholdGwhold.setStatus("mandatory")
_GwiaQThresholdGwprob_Type = Counter32
_GwiaQThresholdGwprob_Object = MibScalar
gwiaQThresholdGwprob = _GwiaQThresholdGwprob_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 29),
    _GwiaQThresholdGwprob_Type()
)
gwiaQThresholdGwprob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaQThresholdGwprob.setStatus("mandatory")
_GwiaThresholdMsgSizeIn_Type = Counter32
_GwiaThresholdMsgSizeIn_Object = MibScalar
gwiaThresholdMsgSizeIn = _GwiaThresholdMsgSizeIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 30),
    _GwiaThresholdMsgSizeIn_Type()
)
gwiaThresholdMsgSizeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaThresholdMsgSizeIn.setStatus("mandatory")
_GwiaThresholdMsgSizeOut_Type = Counter32
_GwiaThresholdMsgSizeOut_Object = MibScalar
gwiaThresholdMsgSizeOut = _GwiaThresholdMsgSizeOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 31),
    _GwiaThresholdMsgSizeOut_Type()
)
gwiaThresholdMsgSizeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiaThresholdMsgSizeOut.setStatus("mandatory")


class _GwiaActionResetStats_Type(Integer32):
    """Custom type gwiaActionResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_GwiaActionResetStats_Type.__name__ = "Integer32"
_GwiaActionResetStats_Object = MibScalar
gwiaActionResetStats = _GwiaActionResetStats_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 32),
    _GwiaActionResetStats_Type()
)
gwiaActionResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gwiaActionResetStats.setStatus("mandatory")


class _GwiaActionRestartGateway_Type(Integer32):
    """Custom type gwiaActionRestartGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_GwiaActionRestartGateway_Type.__name__ = "Integer32"
_GwiaActionRestartGateway_Object = MibScalar
gwiaActionRestartGateway = _GwiaActionRestartGateway_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 33),
    _GwiaActionRestartGateway_Type()
)
gwiaActionRestartGateway.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gwiaActionRestartGateway.setStatus("mandatory")
_GwiaHTTPPort_Type = Integer32
_GwiaHTTPPort_Object = MibScalar
gwiaHTTPPort = _GwiaHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 34),
    _GwiaHTTPPort_Type()
)
gwiaHTTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaHTTPPort.setStatus("mandatory")
_GwiasmtpdThreadsAvailSend_Type = Counter32
_GwiasmtpdThreadsAvailSend_Object = MibScalar
gwiasmtpdThreadsAvailSend = _GwiasmtpdThreadsAvailSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 48),
    _GwiasmtpdThreadsAvailSend_Type()
)
gwiasmtpdThreadsAvailSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdThreadsAvailSend.setStatus("mandatory")
_GwiasmtpdThreadsAvailReceive_Type = Counter32
_GwiasmtpdThreadsAvailReceive_Object = MibScalar
gwiasmtpdThreadsAvailReceive = _GwiasmtpdThreadsAvailReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 49),
    _GwiasmtpdThreadsAvailReceive_Type()
)
gwiasmtpdThreadsAvailReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdThreadsAvailReceive.setStatus("mandatory")
_GwiasmtpdThreadsActiveSend_Type = Counter32
_GwiasmtpdThreadsActiveSend_Object = MibScalar
gwiasmtpdThreadsActiveSend = _GwiasmtpdThreadsActiveSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 50),
    _GwiasmtpdThreadsActiveSend_Type()
)
gwiasmtpdThreadsActiveSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdThreadsActiveSend.setStatus("mandatory")
_GwiasmtpdThreadsActiveReceive_Type = Counter32
_GwiasmtpdThreadsActiveReceive_Object = MibScalar
gwiasmtpdThreadsActiveReceive = _GwiasmtpdThreadsActiveReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 51),
    _GwiasmtpdThreadsActiveReceive_Type()
)
gwiasmtpdThreadsActiveReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdThreadsActiveReceive.setStatus("mandatory")
_GwiasmtpdErrorsMXLookup_Type = Counter32
_GwiasmtpdErrorsMXLookup_Object = MibScalar
gwiasmtpdErrorsMXLookup = _GwiasmtpdErrorsMXLookup_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 52),
    _GwiasmtpdErrorsMXLookup_Type()
)
gwiasmtpdErrorsMXLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdErrorsMXLookup.setStatus("mandatory")
_GwiasmtpdErrorsHostsUnknown_Type = Counter32
_GwiasmtpdErrorsHostsUnknown_Object = MibScalar
gwiasmtpdErrorsHostsUnknown = _GwiasmtpdErrorsHostsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 53),
    _GwiasmtpdErrorsHostsUnknown_Type()
)
gwiasmtpdErrorsHostsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdErrorsHostsUnknown.setStatus("mandatory")
_GwiasmtpdErrorsHostsDown_Type = Counter32
_GwiasmtpdErrorsHostsDown_Object = MibScalar
gwiasmtpdErrorsHostsDown = _GwiasmtpdErrorsHostsDown_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 54),
    _GwiasmtpdErrorsHostsDown_Type()
)
gwiasmtpdErrorsHostsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdErrorsHostsDown.setStatus("mandatory")
_GwiasmtpdErrorsTCPRead_Type = Counter32
_GwiasmtpdErrorsTCPRead_Object = MibScalar
gwiasmtpdErrorsTCPRead = _GwiasmtpdErrorsTCPRead_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 55),
    _GwiasmtpdErrorsTCPRead_Type()
)
gwiasmtpdErrorsTCPRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdErrorsTCPRead.setStatus("mandatory")
_GwiasmtpdErrorsTCPWrite_Type = Counter32
_GwiasmtpdErrorsTCPWrite_Object = MibScalar
gwiasmtpdErrorsTCPWrite = _GwiasmtpdErrorsTCPWrite_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 56),
    _GwiasmtpdErrorsTCPWrite_Type()
)
gwiasmtpdErrorsTCPWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdErrorsTCPWrite.setStatus("mandatory")
_GwiasmtpdMessagesIn_Type = Counter32
_GwiasmtpdMessagesIn_Object = MibScalar
gwiasmtpdMessagesIn = _GwiasmtpdMessagesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 57),
    _GwiasmtpdMessagesIn_Type()
)
gwiasmtpdMessagesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdMessagesIn.setStatus("mandatory")
_GwiasmtpdMessagesOut_Type = Counter32
_GwiasmtpdMessagesOut_Object = MibScalar
gwiasmtpdMessagesOut = _GwiasmtpdMessagesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 58),
    _GwiasmtpdMessagesOut_Type()
)
gwiasmtpdMessagesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpdMessagesOut.setStatus("mandatory")
_GwiasmtpQThresholdSend_Type = Counter32
_GwiasmtpQThresholdSend_Object = MibScalar
gwiasmtpQThresholdSend = _GwiasmtpQThresholdSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 59),
    _GwiasmtpQThresholdSend_Type()
)
gwiasmtpQThresholdSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiasmtpQThresholdSend.setStatus("mandatory")
_GwiasmtpQThresholdReceive_Type = Counter32
_GwiasmtpQThresholdReceive_Object = MibScalar
gwiasmtpQThresholdReceive = _GwiasmtpQThresholdReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 60),
    _GwiasmtpQThresholdReceive_Type()
)
gwiasmtpQThresholdReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiasmtpQThresholdReceive.setStatus("mandatory")
_GwiasmtpQThresholdDefer_Type = Counter32
_GwiasmtpQThresholdDefer_Object = MibScalar
gwiasmtpQThresholdDefer = _GwiasmtpQThresholdDefer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 61),
    _GwiasmtpQThresholdDefer_Type()
)
gwiasmtpQThresholdDefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwiasmtpQThresholdDefer.setStatus("mandatory")
_GwiasmtpQueueSend_Type = Counter32
_GwiasmtpQueueSend_Object = MibScalar
gwiasmtpQueueSend = _GwiasmtpQueueSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 62),
    _GwiasmtpQueueSend_Type()
)
gwiasmtpQueueSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpQueueSend.setStatus("mandatory")
_GwiasmtpQueueReceive_Type = Counter32
_GwiasmtpQueueReceive_Object = MibScalar
gwiasmtpQueueReceive = _GwiasmtpQueueReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 63),
    _GwiasmtpQueueReceive_Type()
)
gwiasmtpQueueReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpQueueReceive.setStatus("mandatory")
_GwiasmtpQueueDefer_Type = Counter32
_GwiasmtpQueueDefer_Object = MibScalar
gwiasmtpQueueDefer = _GwiasmtpQueueDefer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 64),
    _GwiasmtpQueueDefer_Type()
)
gwiasmtpQueueDefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiasmtpQueueDefer.setStatus("mandatory")
_Gwiapop3SessionsAvail_Type = Counter32
_Gwiapop3SessionsAvail_Object = MibScalar
gwiapop3SessionsAvail = _Gwiapop3SessionsAvail_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 65),
    _Gwiapop3SessionsAvail_Type()
)
gwiapop3SessionsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3SessionsAvail.setStatus("mandatory")
_Gwiapop3SessionsActive_Type = Counter32
_Gwiapop3SessionsActive_Object = MibScalar
gwiapop3SessionsActive = _Gwiapop3SessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 66),
    _Gwiapop3SessionsActive_Type()
)
gwiapop3SessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3SessionsActive.setStatus("mandatory")
_Gwiapop3SessionsTotal_Type = Counter32
_Gwiapop3SessionsTotal_Object = MibScalar
gwiapop3SessionsTotal = _Gwiapop3SessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 67),
    _Gwiapop3SessionsTotal_Type()
)
gwiapop3SessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3SessionsTotal.setStatus("mandatory")
_Gwiapop3MessagesSent_Type = Counter32
_Gwiapop3MessagesSent_Object = MibScalar
gwiapop3MessagesSent = _Gwiapop3MessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 68),
    _Gwiapop3MessagesSent_Type()
)
gwiapop3MessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3MessagesSent.setStatus("mandatory")
_Gwiapop3StoreLoginErrs_Type = Counter32
_Gwiapop3StoreLoginErrs_Object = MibScalar
gwiapop3StoreLoginErrs = _Gwiapop3StoreLoginErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 69),
    _Gwiapop3StoreLoginErrs_Type()
)
gwiapop3StoreLoginErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3StoreLoginErrs.setStatus("mandatory")
_Gwiapop3StoreRetrievalErrs_Type = Counter32
_Gwiapop3StoreRetrievalErrs_Object = MibScalar
gwiapop3StoreRetrievalErrs = _Gwiapop3StoreRetrievalErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 70),
    _Gwiapop3StoreRetrievalErrs_Type()
)
gwiapop3StoreRetrievalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3StoreRetrievalErrs.setStatus("mandatory")
_Gwiapop3ConversionErrs_Type = Counter32
_Gwiapop3ConversionErrs_Object = MibScalar
gwiapop3ConversionErrs = _Gwiapop3ConversionErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 71),
    _Gwiapop3ConversionErrs_Type()
)
gwiapop3ConversionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3ConversionErrs.setStatus("mandatory")
_Gwiapop3UnknownUsers_Type = Counter32
_Gwiapop3UnknownUsers_Object = MibScalar
gwiapop3UnknownUsers = _Gwiapop3UnknownUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 72),
    _Gwiapop3UnknownUsers_Type()
)
gwiapop3UnknownUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3UnknownUsers.setStatus("mandatory")
_Gwiapop3BadPassword_Type = Counter32
_Gwiapop3BadPassword_Object = MibScalar
gwiapop3BadPassword = _Gwiapop3BadPassword_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 73),
    _Gwiapop3BadPassword_Type()
)
gwiapop3BadPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3BadPassword.setStatus("mandatory")
_Gwiapop3AccessDenied_Type = Counter32
_Gwiapop3AccessDenied_Object = MibScalar
gwiapop3AccessDenied = _Gwiapop3AccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 74),
    _Gwiapop3AccessDenied_Type()
)
gwiapop3AccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3AccessDenied.setStatus("mandatory")
_Gwiapop3ErrorsTCPRead_Type = Counter32
_Gwiapop3ErrorsTCPRead_Object = MibScalar
gwiapop3ErrorsTCPRead = _Gwiapop3ErrorsTCPRead_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 75),
    _Gwiapop3ErrorsTCPRead_Type()
)
gwiapop3ErrorsTCPRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3ErrorsTCPRead.setStatus("mandatory")
_Gwiapop3ErrorsTCPWrite_Type = Counter32
_Gwiapop3ErrorsTCPWrite_Object = MibScalar
gwiapop3ErrorsTCPWrite = _Gwiapop3ErrorsTCPWrite_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 76),
    _Gwiapop3ErrorsTCPWrite_Type()
)
gwiapop3ErrorsTCPWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiapop3ErrorsTCPWrite.setStatus("mandatory")
_GwiaLdapPublic_Type = Counter32
_GwiaLdapPublic_Object = MibScalar
gwiaLdapPublic = _GwiaLdapPublic_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 77),
    _GwiaLdapPublic_Type()
)
gwiaLdapPublic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapPublic.setStatus("mandatory")
_GwiaLdapAuth_Type = Counter32
_GwiaLdapAuth_Object = MibScalar
gwiaLdapAuth = _GwiaLdapAuth_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 78),
    _GwiaLdapAuth_Type()
)
gwiaLdapAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapAuth.setStatus("mandatory")
_GwiaLdapThreadsFree_Type = Counter32
_GwiaLdapThreadsFree_Object = MibScalar
gwiaLdapThreadsFree = _GwiaLdapThreadsFree_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 79),
    _GwiaLdapThreadsFree_Type()
)
gwiaLdapThreadsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapThreadsFree.setStatus("mandatory")
_GwiaLdapSearchReq_Type = Counter32
_GwiaLdapSearchReq_Object = MibScalar
gwiaLdapSearchReq = _GwiaLdapSearchReq_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 80),
    _GwiaLdapSearchReq_Type()
)
gwiaLdapSearchReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapSearchReq.setStatus("mandatory")
_GwiaLdapReturnedItems_Type = Counter32
_GwiaLdapReturnedItems_Object = MibScalar
gwiaLdapReturnedItems = _GwiaLdapReturnedItems_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 81),
    _GwiaLdapReturnedItems_Type()
)
gwiaLdapReturnedItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapReturnedItems.setStatus("mandatory")
_GwiaLdapActive_Type = Counter32
_GwiaLdapActive_Object = MibScalar
gwiaLdapActive = _GwiaLdapActive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 82),
    _GwiaLdapActive_Type()
)
gwiaLdapActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaLdapActive.setStatus("mandatory")
_Gwiaimap4SessionsAvail_Type = Counter32
_Gwiaimap4SessionsAvail_Object = MibScalar
gwiaimap4SessionsAvail = _Gwiaimap4SessionsAvail_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 83),
    _Gwiaimap4SessionsAvail_Type()
)
gwiaimap4SessionsAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4SessionsAvail.setStatus("mandatory")
_Gwiaimap4SessionsActive_Type = Counter32
_Gwiaimap4SessionsActive_Object = MibScalar
gwiaimap4SessionsActive = _Gwiaimap4SessionsActive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 84),
    _Gwiaimap4SessionsActive_Type()
)
gwiaimap4SessionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4SessionsActive.setStatus("mandatory")
_Gwiaimap4SessionsTotal_Type = Counter32
_Gwiaimap4SessionsTotal_Object = MibScalar
gwiaimap4SessionsTotal = _Gwiaimap4SessionsTotal_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 85),
    _Gwiaimap4SessionsTotal_Type()
)
gwiaimap4SessionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4SessionsTotal.setStatus("mandatory")
_Gwiaimap4MessagesSent_Type = Counter32
_Gwiaimap4MessagesSent_Object = MibScalar
gwiaimap4MessagesSent = _Gwiaimap4MessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 86),
    _Gwiaimap4MessagesSent_Type()
)
gwiaimap4MessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4MessagesSent.setStatus("mandatory")
_Gwiaimap4StoreLoginErrs_Type = Counter32
_Gwiaimap4StoreLoginErrs_Object = MibScalar
gwiaimap4StoreLoginErrs = _Gwiaimap4StoreLoginErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 87),
    _Gwiaimap4StoreLoginErrs_Type()
)
gwiaimap4StoreLoginErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4StoreLoginErrs.setStatus("mandatory")
_Gwiaimap4StoreRetrievalErrs_Type = Counter32
_Gwiaimap4StoreRetrievalErrs_Object = MibScalar
gwiaimap4StoreRetrievalErrs = _Gwiaimap4StoreRetrievalErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 88),
    _Gwiaimap4StoreRetrievalErrs_Type()
)
gwiaimap4StoreRetrievalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4StoreRetrievalErrs.setStatus("mandatory")
_Gwiaimap4ConversionErrs_Type = Counter32
_Gwiaimap4ConversionErrs_Object = MibScalar
gwiaimap4ConversionErrs = _Gwiaimap4ConversionErrs_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 89),
    _Gwiaimap4ConversionErrs_Type()
)
gwiaimap4ConversionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4ConversionErrs.setStatus("mandatory")
_Gwiaimap4UnknownUsers_Type = Counter32
_Gwiaimap4UnknownUsers_Object = MibScalar
gwiaimap4UnknownUsers = _Gwiaimap4UnknownUsers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 90),
    _Gwiaimap4UnknownUsers_Type()
)
gwiaimap4UnknownUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4UnknownUsers.setStatus("mandatory")
_Gwiaimap4BadPassword_Type = Counter32
_Gwiaimap4BadPassword_Object = MibScalar
gwiaimap4BadPassword = _Gwiaimap4BadPassword_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 91),
    _Gwiaimap4BadPassword_Type()
)
gwiaimap4BadPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4BadPassword.setStatus("mandatory")
_Gwiaimap4AccessDenied_Type = Counter32
_Gwiaimap4AccessDenied_Object = MibScalar
gwiaimap4AccessDenied = _Gwiaimap4AccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 92),
    _Gwiaimap4AccessDenied_Type()
)
gwiaimap4AccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4AccessDenied.setStatus("mandatory")
_Gwiaimap4ErrorsTCPRead_Type = Counter32
_Gwiaimap4ErrorsTCPRead_Object = MibScalar
gwiaimap4ErrorsTCPRead = _Gwiaimap4ErrorsTCPRead_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 93),
    _Gwiaimap4ErrorsTCPRead_Type()
)
gwiaimap4ErrorsTCPRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4ErrorsTCPRead.setStatus("mandatory")
_Gwiaimap4ErrorsTCPWrite_Type = Counter32
_Gwiaimap4ErrorsTCPWrite_Object = MibScalar
gwiaimap4ErrorsTCPWrite = _Gwiaimap4ErrorsTCPWrite_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 1, 94),
    _Gwiaimap4ErrorsTCPWrite_Type()
)
gwiaimap4ErrorsTCPWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwiaimap4ErrorsTCPWrite.setStatus("mandatory")
_GwiaTrapInfo_ObjectIdentity = ObjectIdentity
gwiaTrapInfo = _GwiaTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 2)
)
_GwiaTrapTime_Type = Integer32
_GwiaTrapTime_Object = MibScalar
gwiaTrapTime = _GwiaTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 2, 1),
    _GwiaTrapTime_Type()
)
gwiaTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwiaTrapTime.setStatus("mandatory")


class _GwiaTrapDomainName_Type(DisplayString):
    """Custom type gwiaTrapDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwiaTrapDomainName_Type.__name__ = "DisplayString"
_GwiaTrapDomainName_Object = MibScalar
gwiaTrapDomainName = _GwiaTrapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 2, 2),
    _GwiaTrapDomainName_Type()
)
gwiaTrapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwiaTrapDomainName.setStatus("mandatory")
_GwiaTraps_ObjectIdentity = ObjectIdentity
gwiaTraps = _GwiaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3)
)

# Managed Objects groups


# Notification objects

gwiaStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 1)
)
gwiaStartTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaStartTrap.setStatus(
        ""
    )

gwiaStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 2)
)
gwiaStopTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaStopTrap.setStatus(
        ""
    )

gwiaRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 3)
)
gwiaRestartTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaRestartTrap.setStatus(
        ""
    )

gwiaGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 4)
)
gwiaGroupWiseLinkTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaGroupWiseLinkTrap.setStatus(
        ""
    )

gwiaMovedToProbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 6)
)
gwiaMovedToProbTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaMovedToProbTrap.setStatus(
        ""
    )

gwiaWpcsoutThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 7)
)
gwiaWpcsoutThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaWpcsoutThreshTrap.setStatus(
        ""
    )

gwiaWpcsinThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 8)
)
gwiaWpcsinThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaWpcsinThreshTrap.setStatus(
        ""
    )

gwiaGwholdThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 9)
)
gwiaGwholdThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaGwholdThreshTrap.setStatus(
        ""
    )

gwiaGwprobThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 10)
)
gwiaGwprobThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaGwprobThreshTrap.setStatus(
        ""
    )

gwiaInSizeThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 11)
)
gwiaInSizeThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaInSizeThreshTrap.setStatus(
        ""
    )

gwiaOutSizeThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 12)
)
gwiaOutSizeThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiaOutSizeThreshTrap.setStatus(
        ""
    )

gwiasmtpReadErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 48)
)
gwiasmtpReadErrorTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiasmtpReadErrorTrap.setStatus(
        ""
    )

gwiasmtpWriteErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 49)
)
gwiasmtpWriteErrorTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiasmtpWriteErrorTrap.setStatus(
        ""
    )

gwiasmtpSendThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 50)
)
gwiasmtpSendThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiasmtpSendThreshTrap.setStatus(
        ""
    )

gwiasmtpReceiveThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 51)
)
gwiasmtpReceiveThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiasmtpReceiveThreshTrap.setStatus(
        ""
    )

gwiasmtpDeferThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 70, 3, 0, 52)
)
gwiasmtpDeferThreshTrap.setObjects(
      *(("GWIAMIB", "gwiaTrapTime"),
        ("GWIAMIB", "gwiaGatewayName"))
)
if mibBuilder.loadTexts:
    gwiasmtpDeferThreshTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWIAMIB",
    **{"novell": novell,
       "gateways": gateways,
       "gwia": gwia,
       "gwiaInfo": gwiaInfo,
       "gwiaGatewayName": gwiaGatewayName,
       "gwiaTimeUp": gwiaTimeUp,
       "gwiaLinkGroupWise": gwiaLinkGroupWise,
       "gwiaLinkFrgn": gwiaLinkFrgn,
       "gwiaStatBytesOut": gwiaStatBytesOut,
       "gwiaStatBytesIn": gwiaStatBytesIn,
       "gwiaStatMsgsOut": gwiaStatMsgsOut,
       "gwiaStatMsgsIn": gwiaStatMsgsIn,
       "gwiaStatStatusesOut": gwiaStatStatusesOut,
       "gwiaStatStatusesIn": gwiaStatStatusesIn,
       "gwiaStatErrorsOut": gwiaStatErrorsOut,
       "gwiaStatErrorsIn": gwiaStatErrorsIn,
       "gwiaStatTimeReset": gwiaStatTimeReset,
       "gwiaQueueWpcsout": gwiaQueueWpcsout,
       "gwiaQueueWpcsin": gwiaQueueWpcsin,
       "gwiaQueueGwhold": gwiaQueueGwhold,
       "gwiaQueueGwprob": gwiaQueueGwprob,
       "gwiaStatInterval": gwiaStatInterval,
       "gwiaStatIntervalMsgsOut": gwiaStatIntervalMsgsOut,
       "gwiaStatIntervalMsgsIn": gwiaStatIntervalMsgsIn,
       "gwiaStatIntervalStatusesOut": gwiaStatIntervalStatusesOut,
       "gwiaStatIntervalStatusesIn": gwiaStatIntervalStatusesIn,
       "gwiaStatIntervalErrorsOut": gwiaStatIntervalErrorsOut,
       "gwiaStatIntervalErrorsIn": gwiaStatIntervalErrorsIn,
       "gwiaQThresholdCheckInterval": gwiaQThresholdCheckInterval,
       "gwiaQThresholdWpcsout": gwiaQThresholdWpcsout,
       "gwiaQThresholdWpcsin": gwiaQThresholdWpcsin,
       "gwiaQThresholdGwhold": gwiaQThresholdGwhold,
       "gwiaQThresholdGwprob": gwiaQThresholdGwprob,
       "gwiaThresholdMsgSizeIn": gwiaThresholdMsgSizeIn,
       "gwiaThresholdMsgSizeOut": gwiaThresholdMsgSizeOut,
       "gwiaActionResetStats": gwiaActionResetStats,
       "gwiaActionRestartGateway": gwiaActionRestartGateway,
       "gwiaHTTPPort": gwiaHTTPPort,
       "gwiasmtpdThreadsAvailSend": gwiasmtpdThreadsAvailSend,
       "gwiasmtpdThreadsAvailReceive": gwiasmtpdThreadsAvailReceive,
       "gwiasmtpdThreadsActiveSend": gwiasmtpdThreadsActiveSend,
       "gwiasmtpdThreadsActiveReceive": gwiasmtpdThreadsActiveReceive,
       "gwiasmtpdErrorsMXLookup": gwiasmtpdErrorsMXLookup,
       "gwiasmtpdErrorsHostsUnknown": gwiasmtpdErrorsHostsUnknown,
       "gwiasmtpdErrorsHostsDown": gwiasmtpdErrorsHostsDown,
       "gwiasmtpdErrorsTCPRead": gwiasmtpdErrorsTCPRead,
       "gwiasmtpdErrorsTCPWrite": gwiasmtpdErrorsTCPWrite,
       "gwiasmtpdMessagesIn": gwiasmtpdMessagesIn,
       "gwiasmtpdMessagesOut": gwiasmtpdMessagesOut,
       "gwiasmtpQThresholdSend": gwiasmtpQThresholdSend,
       "gwiasmtpQThresholdReceive": gwiasmtpQThresholdReceive,
       "gwiasmtpQThresholdDefer": gwiasmtpQThresholdDefer,
       "gwiasmtpQueueSend": gwiasmtpQueueSend,
       "gwiasmtpQueueReceive": gwiasmtpQueueReceive,
       "gwiasmtpQueueDefer": gwiasmtpQueueDefer,
       "gwiapop3SessionsAvail": gwiapop3SessionsAvail,
       "gwiapop3SessionsActive": gwiapop3SessionsActive,
       "gwiapop3SessionsTotal": gwiapop3SessionsTotal,
       "gwiapop3MessagesSent": gwiapop3MessagesSent,
       "gwiapop3StoreLoginErrs": gwiapop3StoreLoginErrs,
       "gwiapop3StoreRetrievalErrs": gwiapop3StoreRetrievalErrs,
       "gwiapop3ConversionErrs": gwiapop3ConversionErrs,
       "gwiapop3UnknownUsers": gwiapop3UnknownUsers,
       "gwiapop3BadPassword": gwiapop3BadPassword,
       "gwiapop3AccessDenied": gwiapop3AccessDenied,
       "gwiapop3ErrorsTCPRead": gwiapop3ErrorsTCPRead,
       "gwiapop3ErrorsTCPWrite": gwiapop3ErrorsTCPWrite,
       "gwiaLdapPublic": gwiaLdapPublic,
       "gwiaLdapAuth": gwiaLdapAuth,
       "gwiaLdapThreadsFree": gwiaLdapThreadsFree,
       "gwiaLdapSearchReq": gwiaLdapSearchReq,
       "gwiaLdapReturnedItems": gwiaLdapReturnedItems,
       "gwiaLdapActive": gwiaLdapActive,
       "gwiaimap4SessionsAvail": gwiaimap4SessionsAvail,
       "gwiaimap4SessionsActive": gwiaimap4SessionsActive,
       "gwiaimap4SessionsTotal": gwiaimap4SessionsTotal,
       "gwiaimap4MessagesSent": gwiaimap4MessagesSent,
       "gwiaimap4StoreLoginErrs": gwiaimap4StoreLoginErrs,
       "gwiaimap4StoreRetrievalErrs": gwiaimap4StoreRetrievalErrs,
       "gwiaimap4ConversionErrs": gwiaimap4ConversionErrs,
       "gwiaimap4UnknownUsers": gwiaimap4UnknownUsers,
       "gwiaimap4BadPassword": gwiaimap4BadPassword,
       "gwiaimap4AccessDenied": gwiaimap4AccessDenied,
       "gwiaimap4ErrorsTCPRead": gwiaimap4ErrorsTCPRead,
       "gwiaimap4ErrorsTCPWrite": gwiaimap4ErrorsTCPWrite,
       "gwiaTrapInfo": gwiaTrapInfo,
       "gwiaTrapTime": gwiaTrapTime,
       "gwiaTrapDomainName": gwiaTrapDomainName,
       "gwiaTraps": gwiaTraps,
       "gwiaStartTrap": gwiaStartTrap,
       "gwiaStopTrap": gwiaStopTrap,
       "gwiaRestartTrap": gwiaRestartTrap,
       "gwiaGroupWiseLinkTrap": gwiaGroupWiseLinkTrap,
       "gwiaMovedToProbTrap": gwiaMovedToProbTrap,
       "gwiaWpcsoutThreshTrap": gwiaWpcsoutThreshTrap,
       "gwiaWpcsinThreshTrap": gwiaWpcsinThreshTrap,
       "gwiaGwholdThreshTrap": gwiaGwholdThreshTrap,
       "gwiaGwprobThreshTrap": gwiaGwprobThreshTrap,
       "gwiaInSizeThreshTrap": gwiaInSizeThreshTrap,
       "gwiaOutSizeThreshTrap": gwiaOutSizeThreshTrap,
       "gwiasmtpReadErrorTrap": gwiasmtpReadErrorTrap,
       "gwiasmtpWriteErrorTrap": gwiasmtpWriteErrorTrap,
       "gwiasmtpSendThreshTrap": gwiasmtpSendThreshTrap,
       "gwiasmtpReceiveThreshTrap": gwiasmtpReceiveThreshTrap,
       "gwiasmtpDeferThreshTrap": gwiasmtpDeferThreshTrap}
)
