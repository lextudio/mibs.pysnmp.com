# SNMP MIB module (GWSMTPMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GWSMTPMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:28 2024
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
_Gwsmtp_ObjectIdentity = ObjectIdentity
gwsmtp = _Gwsmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 51)
)
_GwsmtpInfo_ObjectIdentity = ObjectIdentity
gwsmtpInfo = _GwsmtpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1)
)


class _GwsmtpGatewayName_Type(DisplayString):
    """Custom type gwsmtpGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwsmtpGatewayName_Type.__name__ = "DisplayString"
_GwsmtpGatewayName_Object = MibScalar
gwsmtpGatewayName = _GwsmtpGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 1),
    _GwsmtpGatewayName_Type()
)
gwsmtpGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpGatewayName.setStatus("mandatory")
_GwsmtpTimeUp_Type = TimeTicks
_GwsmtpTimeUp_Object = MibScalar
gwsmtpTimeUp = _GwsmtpTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 2),
    _GwsmtpTimeUp_Type()
)
gwsmtpTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpTimeUp.setStatus("mandatory")


class _GwsmtpLinkGroupWise_Type(DisplayString):
    """Custom type gwsmtpLinkGroupWise based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwsmtpLinkGroupWise_Type.__name__ = "DisplayString"
_GwsmtpLinkGroupWise_Object = MibScalar
gwsmtpLinkGroupWise = _GwsmtpLinkGroupWise_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 3),
    _GwsmtpLinkGroupWise_Type()
)
gwsmtpLinkGroupWise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpLinkGroupWise.setStatus("mandatory")


class _GwsmtpLinkFrgn_Type(DisplayString):
    """Custom type gwsmtpLinkFrgn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_GwsmtpLinkFrgn_Type.__name__ = "DisplayString"
_GwsmtpLinkFrgn_Object = MibScalar
gwsmtpLinkFrgn = _GwsmtpLinkFrgn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 4),
    _GwsmtpLinkFrgn_Type()
)
gwsmtpLinkFrgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpLinkFrgn.setStatus("mandatory")
_GwsmtpStatBytesOut_Type = Counter32
_GwsmtpStatBytesOut_Object = MibScalar
gwsmtpStatBytesOut = _GwsmtpStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 5),
    _GwsmtpStatBytesOut_Type()
)
gwsmtpStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatBytesOut.setStatus("mandatory")
_GwsmtpStatBytesIn_Type = Counter32
_GwsmtpStatBytesIn_Object = MibScalar
gwsmtpStatBytesIn = _GwsmtpStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 6),
    _GwsmtpStatBytesIn_Type()
)
gwsmtpStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatBytesIn.setStatus("mandatory")
_GwsmtpStatMsgsOut_Type = Counter32
_GwsmtpStatMsgsOut_Object = MibScalar
gwsmtpStatMsgsOut = _GwsmtpStatMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 7),
    _GwsmtpStatMsgsOut_Type()
)
gwsmtpStatMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatMsgsOut.setStatus("mandatory")
_GwsmtpStatMsgsIn_Type = Counter32
_GwsmtpStatMsgsIn_Object = MibScalar
gwsmtpStatMsgsIn = _GwsmtpStatMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 8),
    _GwsmtpStatMsgsIn_Type()
)
gwsmtpStatMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatMsgsIn.setStatus("mandatory")
_GwsmtpStatStatusesOut_Type = Counter32
_GwsmtpStatStatusesOut_Object = MibScalar
gwsmtpStatStatusesOut = _GwsmtpStatStatusesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 9),
    _GwsmtpStatStatusesOut_Type()
)
gwsmtpStatStatusesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatStatusesOut.setStatus("mandatory")
_GwsmtpStatStatusesIn_Type = Counter32
_GwsmtpStatStatusesIn_Object = MibScalar
gwsmtpStatStatusesIn = _GwsmtpStatStatusesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 10),
    _GwsmtpStatStatusesIn_Type()
)
gwsmtpStatStatusesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatStatusesIn.setStatus("mandatory")
_GwsmtpStatErrorsOut_Type = Counter32
_GwsmtpStatErrorsOut_Object = MibScalar
gwsmtpStatErrorsOut = _GwsmtpStatErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 11),
    _GwsmtpStatErrorsOut_Type()
)
gwsmtpStatErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatErrorsOut.setStatus("mandatory")
_GwsmtpStatErrorsIn_Type = Counter32
_GwsmtpStatErrorsIn_Object = MibScalar
gwsmtpStatErrorsIn = _GwsmtpStatErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 12),
    _GwsmtpStatErrorsIn_Type()
)
gwsmtpStatErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatErrorsIn.setStatus("mandatory")
_GwsmtpStatTimeReset_Type = TimeTicks
_GwsmtpStatTimeReset_Object = MibScalar
gwsmtpStatTimeReset = _GwsmtpStatTimeReset_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 13),
    _GwsmtpStatTimeReset_Type()
)
gwsmtpStatTimeReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatTimeReset.setStatus("mandatory")
_GwsmtpQueueWpcsout_Type = Counter32
_GwsmtpQueueWpcsout_Object = MibScalar
gwsmtpQueueWpcsout = _GwsmtpQueueWpcsout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 14),
    _GwsmtpQueueWpcsout_Type()
)
gwsmtpQueueWpcsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueWpcsout.setStatus("mandatory")
_GwsmtpQueueWpcsin_Type = Counter32
_GwsmtpQueueWpcsin_Object = MibScalar
gwsmtpQueueWpcsin = _GwsmtpQueueWpcsin_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 15),
    _GwsmtpQueueWpcsin_Type()
)
gwsmtpQueueWpcsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueWpcsin.setStatus("mandatory")
_GwsmtpQueueGwhold_Type = Counter32
_GwsmtpQueueGwhold_Object = MibScalar
gwsmtpQueueGwhold = _GwsmtpQueueGwhold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 16),
    _GwsmtpQueueGwhold_Type()
)
gwsmtpQueueGwhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueGwhold.setStatus("mandatory")
_GwsmtpQueueGwprob_Type = Counter32
_GwsmtpQueueGwprob_Object = MibScalar
gwsmtpQueueGwprob = _GwsmtpQueueGwprob_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 17),
    _GwsmtpQueueGwprob_Type()
)
gwsmtpQueueGwprob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueGwprob.setStatus("mandatory")
_GwsmtpStatInterval_Type = TimeTicks
_GwsmtpStatInterval_Object = MibScalar
gwsmtpStatInterval = _GwsmtpStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 18),
    _GwsmtpStatInterval_Type()
)
gwsmtpStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatInterval.setStatus("mandatory")
_GwsmtpStatIntervalMsgsOut_Type = Counter32
_GwsmtpStatIntervalMsgsOut_Object = MibScalar
gwsmtpStatIntervalMsgsOut = _GwsmtpStatIntervalMsgsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 19),
    _GwsmtpStatIntervalMsgsOut_Type()
)
gwsmtpStatIntervalMsgsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalMsgsOut.setStatus("mandatory")
_GwsmtpStatIntervalMsgsIn_Type = Counter32
_GwsmtpStatIntervalMsgsIn_Object = MibScalar
gwsmtpStatIntervalMsgsIn = _GwsmtpStatIntervalMsgsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 20),
    _GwsmtpStatIntervalMsgsIn_Type()
)
gwsmtpStatIntervalMsgsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalMsgsIn.setStatus("mandatory")
_GwsmtpStatIntervalStatusesOut_Type = Counter32
_GwsmtpStatIntervalStatusesOut_Object = MibScalar
gwsmtpStatIntervalStatusesOut = _GwsmtpStatIntervalStatusesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 21),
    _GwsmtpStatIntervalStatusesOut_Type()
)
gwsmtpStatIntervalStatusesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalStatusesOut.setStatus("mandatory")
_GwsmtpStatIntervalStatusesIn_Type = Counter32
_GwsmtpStatIntervalStatusesIn_Object = MibScalar
gwsmtpStatIntervalStatusesIn = _GwsmtpStatIntervalStatusesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 22),
    _GwsmtpStatIntervalStatusesIn_Type()
)
gwsmtpStatIntervalStatusesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalStatusesIn.setStatus("mandatory")
_GwsmtpStatIntervalErrorsOut_Type = Counter32
_GwsmtpStatIntervalErrorsOut_Object = MibScalar
gwsmtpStatIntervalErrorsOut = _GwsmtpStatIntervalErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 23),
    _GwsmtpStatIntervalErrorsOut_Type()
)
gwsmtpStatIntervalErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalErrorsOut.setStatus("mandatory")
_GwsmtpStatIntervalErrorsIn_Type = Counter32
_GwsmtpStatIntervalErrorsIn_Object = MibScalar
gwsmtpStatIntervalErrorsIn = _GwsmtpStatIntervalErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 24),
    _GwsmtpStatIntervalErrorsIn_Type()
)
gwsmtpStatIntervalErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpStatIntervalErrorsIn.setStatus("mandatory")
_GwsmtpQThresholdCheckInterval_Type = Counter32
_GwsmtpQThresholdCheckInterval_Object = MibScalar
gwsmtpQThresholdCheckInterval = _GwsmtpQThresholdCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 25),
    _GwsmtpQThresholdCheckInterval_Type()
)
gwsmtpQThresholdCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdCheckInterval.setStatus("mandatory")
_GwsmtpQThresholdWpcsout_Type = Counter32
_GwsmtpQThresholdWpcsout_Object = MibScalar
gwsmtpQThresholdWpcsout = _GwsmtpQThresholdWpcsout_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 26),
    _GwsmtpQThresholdWpcsout_Type()
)
gwsmtpQThresholdWpcsout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdWpcsout.setStatus("mandatory")
_GwsmtpQThresholdWpcsin_Type = Counter32
_GwsmtpQThresholdWpcsin_Object = MibScalar
gwsmtpQThresholdWpcsin = _GwsmtpQThresholdWpcsin_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 27),
    _GwsmtpQThresholdWpcsin_Type()
)
gwsmtpQThresholdWpcsin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdWpcsin.setStatus("mandatory")
_GwsmtpQThresholdGwhold_Type = Counter32
_GwsmtpQThresholdGwhold_Object = MibScalar
gwsmtpQThresholdGwhold = _GwsmtpQThresholdGwhold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 28),
    _GwsmtpQThresholdGwhold_Type()
)
gwsmtpQThresholdGwhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdGwhold.setStatus("mandatory")
_GwsmtpQThresholdGwprob_Type = Counter32
_GwsmtpQThresholdGwprob_Object = MibScalar
gwsmtpQThresholdGwprob = _GwsmtpQThresholdGwprob_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 29),
    _GwsmtpQThresholdGwprob_Type()
)
gwsmtpQThresholdGwprob.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdGwprob.setStatus("mandatory")
_GwsmtpThresholdMsgSizeIn_Type = Counter32
_GwsmtpThresholdMsgSizeIn_Object = MibScalar
gwsmtpThresholdMsgSizeIn = _GwsmtpThresholdMsgSizeIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 30),
    _GwsmtpThresholdMsgSizeIn_Type()
)
gwsmtpThresholdMsgSizeIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpThresholdMsgSizeIn.setStatus("mandatory")
_GwsmtpThresholdMsgSizeOut_Type = Counter32
_GwsmtpThresholdMsgSizeOut_Object = MibScalar
gwsmtpThresholdMsgSizeOut = _GwsmtpThresholdMsgSizeOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 31),
    _GwsmtpThresholdMsgSizeOut_Type()
)
gwsmtpThresholdMsgSizeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpThresholdMsgSizeOut.setStatus("mandatory")


class _GwsmtpActionResetStats_Type(Integer32):
    """Custom type gwsmtpActionResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_GwsmtpActionResetStats_Type.__name__ = "Integer32"
_GwsmtpActionResetStats_Object = MibScalar
gwsmtpActionResetStats = _GwsmtpActionResetStats_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 32),
    _GwsmtpActionResetStats_Type()
)
gwsmtpActionResetStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gwsmtpActionResetStats.setStatus("mandatory")


class _GwsmtpActionRestartGateway_Type(Integer32):
    """Custom type gwsmtpActionRestartGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_GwsmtpActionRestartGateway_Type.__name__ = "Integer32"
_GwsmtpActionRestartGateway_Object = MibScalar
gwsmtpActionRestartGateway = _GwsmtpActionRestartGateway_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 33),
    _GwsmtpActionRestartGateway_Type()
)
gwsmtpActionRestartGateway.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gwsmtpActionRestartGateway.setStatus("mandatory")
_GwsmtpdThreadsAvailSend_Type = Counter32
_GwsmtpdThreadsAvailSend_Object = MibScalar
gwsmtpdThreadsAvailSend = _GwsmtpdThreadsAvailSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 48),
    _GwsmtpdThreadsAvailSend_Type()
)
gwsmtpdThreadsAvailSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdThreadsAvailSend.setStatus("mandatory")
_GwsmtpdThreadsAvailReceive_Type = Counter32
_GwsmtpdThreadsAvailReceive_Object = MibScalar
gwsmtpdThreadsAvailReceive = _GwsmtpdThreadsAvailReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 49),
    _GwsmtpdThreadsAvailReceive_Type()
)
gwsmtpdThreadsAvailReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdThreadsAvailReceive.setStatus("mandatory")
_GwsmtpdThreadsActiveSend_Type = Counter32
_GwsmtpdThreadsActiveSend_Object = MibScalar
gwsmtpdThreadsActiveSend = _GwsmtpdThreadsActiveSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 50),
    _GwsmtpdThreadsActiveSend_Type()
)
gwsmtpdThreadsActiveSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdThreadsActiveSend.setStatus("mandatory")
_GwsmtpdThreadsActiveReceive_Type = Counter32
_GwsmtpdThreadsActiveReceive_Object = MibScalar
gwsmtpdThreadsActiveReceive = _GwsmtpdThreadsActiveReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 51),
    _GwsmtpdThreadsActiveReceive_Type()
)
gwsmtpdThreadsActiveReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdThreadsActiveReceive.setStatus("mandatory")
_GwsmtpdErrorsMXLookup_Type = Counter32
_GwsmtpdErrorsMXLookup_Object = MibScalar
gwsmtpdErrorsMXLookup = _GwsmtpdErrorsMXLookup_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 52),
    _GwsmtpdErrorsMXLookup_Type()
)
gwsmtpdErrorsMXLookup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdErrorsMXLookup.setStatus("mandatory")
_GwsmtpdErrorsHostsUnknown_Type = Counter32
_GwsmtpdErrorsHostsUnknown_Object = MibScalar
gwsmtpdErrorsHostsUnknown = _GwsmtpdErrorsHostsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 53),
    _GwsmtpdErrorsHostsUnknown_Type()
)
gwsmtpdErrorsHostsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdErrorsHostsUnknown.setStatus("mandatory")
_GwsmtpdErrorsHostsDown_Type = Counter32
_GwsmtpdErrorsHostsDown_Object = MibScalar
gwsmtpdErrorsHostsDown = _GwsmtpdErrorsHostsDown_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 54),
    _GwsmtpdErrorsHostsDown_Type()
)
gwsmtpdErrorsHostsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdErrorsHostsDown.setStatus("mandatory")
_GwsmtpdErrorsTCPRead_Type = Counter32
_GwsmtpdErrorsTCPRead_Object = MibScalar
gwsmtpdErrorsTCPRead = _GwsmtpdErrorsTCPRead_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 55),
    _GwsmtpdErrorsTCPRead_Type()
)
gwsmtpdErrorsTCPRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdErrorsTCPRead.setStatus("mandatory")
_GwsmtpdErrorsTCPWrite_Type = Counter32
_GwsmtpdErrorsTCPWrite_Object = MibScalar
gwsmtpdErrorsTCPWrite = _GwsmtpdErrorsTCPWrite_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 56),
    _GwsmtpdErrorsTCPWrite_Type()
)
gwsmtpdErrorsTCPWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdErrorsTCPWrite.setStatus("mandatory")
_GwsmtpdMessagesIn_Type = Counter32
_GwsmtpdMessagesIn_Object = MibScalar
gwsmtpdMessagesIn = _GwsmtpdMessagesIn_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 57),
    _GwsmtpdMessagesIn_Type()
)
gwsmtpdMessagesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdMessagesIn.setStatus("mandatory")
_GwsmtpdMessagesOut_Type = Counter32
_GwsmtpdMessagesOut_Object = MibScalar
gwsmtpdMessagesOut = _GwsmtpdMessagesOut_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 58),
    _GwsmtpdMessagesOut_Type()
)
gwsmtpdMessagesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpdMessagesOut.setStatus("mandatory")
_GwsmtpQThresholdSend_Type = Counter32
_GwsmtpQThresholdSend_Object = MibScalar
gwsmtpQThresholdSend = _GwsmtpQThresholdSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 59),
    _GwsmtpQThresholdSend_Type()
)
gwsmtpQThresholdSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdSend.setStatus("mandatory")
_GwsmtpQThresholdReceive_Type = Counter32
_GwsmtpQThresholdReceive_Object = MibScalar
gwsmtpQThresholdReceive = _GwsmtpQThresholdReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 60),
    _GwsmtpQThresholdReceive_Type()
)
gwsmtpQThresholdReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdReceive.setStatus("mandatory")
_GwsmtpQThresholdDefer_Type = Counter32
_GwsmtpQThresholdDefer_Object = MibScalar
gwsmtpQThresholdDefer = _GwsmtpQThresholdDefer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 61),
    _GwsmtpQThresholdDefer_Type()
)
gwsmtpQThresholdDefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwsmtpQThresholdDefer.setStatus("mandatory")
_GwsmtpQueueSend_Type = Counter32
_GwsmtpQueueSend_Object = MibScalar
gwsmtpQueueSend = _GwsmtpQueueSend_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 62),
    _GwsmtpQueueSend_Type()
)
gwsmtpQueueSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueSend.setStatus("mandatory")
_GwsmtpQueueReceive_Type = Counter32
_GwsmtpQueueReceive_Object = MibScalar
gwsmtpQueueReceive = _GwsmtpQueueReceive_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 63),
    _GwsmtpQueueReceive_Type()
)
gwsmtpQueueReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueReceive.setStatus("mandatory")
_GwsmtpQueueDefer_Type = Counter32
_GwsmtpQueueDefer_Object = MibScalar
gwsmtpQueueDefer = _GwsmtpQueueDefer_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 1, 64),
    _GwsmtpQueueDefer_Type()
)
gwsmtpQueueDefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwsmtpQueueDefer.setStatus("mandatory")
_GwsmtpTrapInfo_ObjectIdentity = ObjectIdentity
gwsmtpTrapInfo = _GwsmtpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 2)
)
_GwsmtpTrapTime_Type = Integer32
_GwsmtpTrapTime_Object = MibScalar
gwsmtpTrapTime = _GwsmtpTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 2, 1),
    _GwsmtpTrapTime_Type()
)
gwsmtpTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwsmtpTrapTime.setStatus("mandatory")


class _GwsmtpTrapDomainName_Type(DisplayString):
    """Custom type gwsmtpTrapDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwsmtpTrapDomainName_Type.__name__ = "DisplayString"
_GwsmtpTrapDomainName_Object = MibScalar
gwsmtpTrapDomainName = _GwsmtpTrapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 2, 2),
    _GwsmtpTrapDomainName_Type()
)
gwsmtpTrapDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gwsmtpTrapDomainName.setStatus("mandatory")
_GwsmtpTraps_ObjectIdentity = ObjectIdentity
gwsmtpTraps = _GwsmtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3)
)

# Managed Objects groups


# Notification objects

gwsmtpStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 1)
)
gwsmtpStartTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpStartTrap.setStatus(
        ""
    )

gwsmtpStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 2)
)
gwsmtpStopTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpStopTrap.setStatus(
        ""
    )

gwsmtpRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 3)
)
gwsmtpRestartTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpRestartTrap.setStatus(
        ""
    )

gwsmtpGroupWiseLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 4)
)
gwsmtpGroupWiseLinkTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpGroupWiseLinkTrap.setStatus(
        ""
    )

gwsmtpMovedToProbTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 6)
)
gwsmtpMovedToProbTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpMovedToProbTrap.setStatus(
        ""
    )

gwsmtpWpcsoutThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 7)
)
gwsmtpWpcsoutThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpWpcsoutThreshTrap.setStatus(
        ""
    )

gwsmtpWpcsinThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 8)
)
gwsmtpWpcsinThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpWpcsinThreshTrap.setStatus(
        ""
    )

gwsmtpGwholdThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 9)
)
gwsmtpGwholdThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpGwholdThreshTrap.setStatus(
        ""
    )

gwsmtpGwprobThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 10)
)
gwsmtpGwprobThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpGwprobThreshTrap.setStatus(
        ""
    )

gwsmtpInSizeThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 11)
)
gwsmtpInSizeThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpInSizeThreshTrap.setStatus(
        ""
    )

gwsmtpOutSizeThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 12)
)
gwsmtpOutSizeThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpOutSizeThreshTrap.setStatus(
        ""
    )

gwsmtpReadErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 32)
)
gwsmtpReadErrorTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpReadErrorTrap.setStatus(
        ""
    )

gwsmtpWriteErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 33)
)
gwsmtpWriteErrorTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpWriteErrorTrap.setStatus(
        ""
    )

gwsmtpSendThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 34)
)
gwsmtpSendThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpSendThreshTrap.setStatus(
        ""
    )

gwsmtpReceiveThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 35)
)
gwsmtpReceiveThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpReceiveThreshTrap.setStatus(
        ""
    )

gwsmtpDeferThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 51, 3, 0, 36)
)
gwsmtpDeferThreshTrap.setObjects(
      *(("GWSMTPMIB", "gwsmtpTrapTime"),
        ("GWSMTPMIB", "gwsmtpGatewayName"))
)
if mibBuilder.loadTexts:
    gwsmtpDeferThreshTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GWSMTPMIB",
    **{"novell": novell,
       "gateways": gateways,
       "gwsmtp": gwsmtp,
       "gwsmtpInfo": gwsmtpInfo,
       "gwsmtpGatewayName": gwsmtpGatewayName,
       "gwsmtpTimeUp": gwsmtpTimeUp,
       "gwsmtpLinkGroupWise": gwsmtpLinkGroupWise,
       "gwsmtpLinkFrgn": gwsmtpLinkFrgn,
       "gwsmtpStatBytesOut": gwsmtpStatBytesOut,
       "gwsmtpStatBytesIn": gwsmtpStatBytesIn,
       "gwsmtpStatMsgsOut": gwsmtpStatMsgsOut,
       "gwsmtpStatMsgsIn": gwsmtpStatMsgsIn,
       "gwsmtpStatStatusesOut": gwsmtpStatStatusesOut,
       "gwsmtpStatStatusesIn": gwsmtpStatStatusesIn,
       "gwsmtpStatErrorsOut": gwsmtpStatErrorsOut,
       "gwsmtpStatErrorsIn": gwsmtpStatErrorsIn,
       "gwsmtpStatTimeReset": gwsmtpStatTimeReset,
       "gwsmtpQueueWpcsout": gwsmtpQueueWpcsout,
       "gwsmtpQueueWpcsin": gwsmtpQueueWpcsin,
       "gwsmtpQueueGwhold": gwsmtpQueueGwhold,
       "gwsmtpQueueGwprob": gwsmtpQueueGwprob,
       "gwsmtpStatInterval": gwsmtpStatInterval,
       "gwsmtpStatIntervalMsgsOut": gwsmtpStatIntervalMsgsOut,
       "gwsmtpStatIntervalMsgsIn": gwsmtpStatIntervalMsgsIn,
       "gwsmtpStatIntervalStatusesOut": gwsmtpStatIntervalStatusesOut,
       "gwsmtpStatIntervalStatusesIn": gwsmtpStatIntervalStatusesIn,
       "gwsmtpStatIntervalErrorsOut": gwsmtpStatIntervalErrorsOut,
       "gwsmtpStatIntervalErrorsIn": gwsmtpStatIntervalErrorsIn,
       "gwsmtpQThresholdCheckInterval": gwsmtpQThresholdCheckInterval,
       "gwsmtpQThresholdWpcsout": gwsmtpQThresholdWpcsout,
       "gwsmtpQThresholdWpcsin": gwsmtpQThresholdWpcsin,
       "gwsmtpQThresholdGwhold": gwsmtpQThresholdGwhold,
       "gwsmtpQThresholdGwprob": gwsmtpQThresholdGwprob,
       "gwsmtpThresholdMsgSizeIn": gwsmtpThresholdMsgSizeIn,
       "gwsmtpThresholdMsgSizeOut": gwsmtpThresholdMsgSizeOut,
       "gwsmtpActionResetStats": gwsmtpActionResetStats,
       "gwsmtpActionRestartGateway": gwsmtpActionRestartGateway,
       "gwsmtpdThreadsAvailSend": gwsmtpdThreadsAvailSend,
       "gwsmtpdThreadsAvailReceive": gwsmtpdThreadsAvailReceive,
       "gwsmtpdThreadsActiveSend": gwsmtpdThreadsActiveSend,
       "gwsmtpdThreadsActiveReceive": gwsmtpdThreadsActiveReceive,
       "gwsmtpdErrorsMXLookup": gwsmtpdErrorsMXLookup,
       "gwsmtpdErrorsHostsUnknown": gwsmtpdErrorsHostsUnknown,
       "gwsmtpdErrorsHostsDown": gwsmtpdErrorsHostsDown,
       "gwsmtpdErrorsTCPRead": gwsmtpdErrorsTCPRead,
       "gwsmtpdErrorsTCPWrite": gwsmtpdErrorsTCPWrite,
       "gwsmtpdMessagesIn": gwsmtpdMessagesIn,
       "gwsmtpdMessagesOut": gwsmtpdMessagesOut,
       "gwsmtpQThresholdSend": gwsmtpQThresholdSend,
       "gwsmtpQThresholdReceive": gwsmtpQThresholdReceive,
       "gwsmtpQThresholdDefer": gwsmtpQThresholdDefer,
       "gwsmtpQueueSend": gwsmtpQueueSend,
       "gwsmtpQueueReceive": gwsmtpQueueReceive,
       "gwsmtpQueueDefer": gwsmtpQueueDefer,
       "gwsmtpTrapInfo": gwsmtpTrapInfo,
       "gwsmtpTrapTime": gwsmtpTrapTime,
       "gwsmtpTrapDomainName": gwsmtpTrapDomainName,
       "gwsmtpTraps": gwsmtpTraps,
       "gwsmtpStartTrap": gwsmtpStartTrap,
       "gwsmtpStopTrap": gwsmtpStopTrap,
       "gwsmtpRestartTrap": gwsmtpRestartTrap,
       "gwsmtpGroupWiseLinkTrap": gwsmtpGroupWiseLinkTrap,
       "gwsmtpMovedToProbTrap": gwsmtpMovedToProbTrap,
       "gwsmtpWpcsoutThreshTrap": gwsmtpWpcsoutThreshTrap,
       "gwsmtpWpcsinThreshTrap": gwsmtpWpcsinThreshTrap,
       "gwsmtpGwholdThreshTrap": gwsmtpGwholdThreshTrap,
       "gwsmtpGwprobThreshTrap": gwsmtpGwprobThreshTrap,
       "gwsmtpInSizeThreshTrap": gwsmtpInSizeThreshTrap,
       "gwsmtpOutSizeThreshTrap": gwsmtpOutSizeThreshTrap,
       "gwsmtpReadErrorTrap": gwsmtpReadErrorTrap,
       "gwsmtpWriteErrorTrap": gwsmtpWriteErrorTrap,
       "gwsmtpSendThreshTrap": gwsmtpSendThreshTrap,
       "gwsmtpReceiveThreshTrap": gwsmtpReceiveThreshTrap,
       "gwsmtpDeferThreshTrap": gwsmtpDeferThreshTrap}
)
