# SNMP MIB module (CISCO-FCIP-MGMT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCIP-MGMT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:23 2024
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

(cfmFcipEntityInstanceEntry,
 cfmFcipLinkEntry) = mibBuilder.importSymbols(
    "CISCO-FCIP-MGMT-MIB",
    "cfmFcipEntityInstanceEntry",
    "cfmFcipLinkEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcipMgmtExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329)
)
ciscoFcipMgmtExtMIB.setRevisions(
        ("2005-10-12 00:00",
         "2005-06-07 00:00",
         "2005-05-14 00:00",
         "2004-09-23 00:00",
         "2004-03-10 00:00",
         "2003-11-05 00:00",
         "2003-09-19 00:00",
         "2003-05-06 00:00",
         "2003-03-25 00:00",
         "2003-01-07 00:00",
         "2002-12-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFcipMgmtExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFcipMgmtExtMIBNotifs = _CiscoFcipMgmtExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 0)
)
_CiscoFcipMgmtExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcipMgmtExtMIBObjects = _CiscoFcipMgmtExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1)
)
_CfmFcipMgmtExtConfig_ObjectIdentity = ObjectIdentity
cfmFcipMgmtExtConfig = _CfmFcipMgmtExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1)
)
_CfmFcipEntityExtTable_Object = MibTable
cfmFcipEntityExtTable = _CfmFcipEntityExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFcipEntityExtTable.setStatus("current")
_CfmFcipEntityExtEntry_Object = MibTableRow
cfmFcipEntityExtEntry = _CfmFcipEntityExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFcipEntityExtEntry.setStatus("current")


class _CfmFcipEntityExtTcpKeepAliveTO_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpKeepAliveTO based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_CfmFcipEntityExtTcpKeepAliveTO_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpKeepAliveTO_Object = MibTableColumn
cfmFcipEntityExtTcpKeepAliveTO = _CfmFcipEntityExtTcpKeepAliveTO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 1),
    _CfmFcipEntityExtTcpKeepAliveTO_Type()
)
cfmFcipEntityExtTcpKeepAliveTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpKeepAliveTO.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpKeepAliveTO.setUnits("seconds")


class _CfmFcipEntityExtTcpMaxReTx_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpMaxReTx based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CfmFcipEntityExtTcpMaxReTx_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpMaxReTx_Object = MibTableColumn
cfmFcipEntityExtTcpMaxReTx = _CfmFcipEntityExtTcpMaxReTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 2),
    _CfmFcipEntityExtTcpMaxReTx_Type()
)
cfmFcipEntityExtTcpMaxReTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMaxReTx.setStatus("current")


class _CfmFcipEntityExtPMTUEnable_Type(TruthValue):
    """Custom type cfmFcipEntityExtPMTUEnable based on TruthValue"""


_CfmFcipEntityExtPMTUEnable_Object = MibTableColumn
cfmFcipEntityExtPMTUEnable = _CfmFcipEntityExtPMTUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 3),
    _CfmFcipEntityExtPMTUEnable_Type()
)
cfmFcipEntityExtPMTUEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtPMTUEnable.setStatus("current")


class _CfmFcipEntityExtPMTUResetTO_Type(Unsigned32):
    """Custom type cfmFcipEntityExtPMTUResetTO based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_CfmFcipEntityExtPMTUResetTO_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtPMTUResetTO_Object = MibTableColumn
cfmFcipEntityExtPMTUResetTO = _CfmFcipEntityExtPMTUResetTO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 4),
    _CfmFcipEntityExtPMTUResetTO_Type()
)
cfmFcipEntityExtPMTUResetTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtPMTUResetTO.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtPMTUResetTO.setUnits("seconds")


class _CfmFcipEntityExtTcpMinRTO_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpMinRTO based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CfmFcipEntityExtTcpMinRTO_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpMinRTO_Object = MibTableColumn
cfmFcipEntityExtTcpMinRTO = _CfmFcipEntityExtTcpMinRTO_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 5),
    _CfmFcipEntityExtTcpMinRTO_Type()
)
cfmFcipEntityExtTcpMinRTO.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMinRTO.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMinRTO.setUnits("milliseconds")


class _CfmFcipEntityExtTcpSendBufSize_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpSendBufSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_CfmFcipEntityExtTcpSendBufSize_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpSendBufSize_Object = MibTableColumn
cfmFcipEntityExtTcpSendBufSize = _CfmFcipEntityExtTcpSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 6),
    _CfmFcipEntityExtTcpSendBufSize_Type()
)
cfmFcipEntityExtTcpSendBufSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpSendBufSize.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpSendBufSize.setUnits("kilobytes")


class _CfmFcipEntityExtTcpMaxBW_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpMaxBW based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_CfmFcipEntityExtTcpMaxBW_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpMaxBW_Object = MibTableColumn
cfmFcipEntityExtTcpMaxBW = _CfmFcipEntityExtTcpMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 7),
    _CfmFcipEntityExtTcpMaxBW_Type()
)
cfmFcipEntityExtTcpMaxBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMaxBW.setUnits("kilobits")


class _CfmFcipEntityExtTcpMinAvailBW_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpMinAvailBW based on Unsigned32"""
    defaultValue = 15000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 1000000),
    )


_CfmFcipEntityExtTcpMinAvailBW_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpMinAvailBW_Object = MibTableColumn
cfmFcipEntityExtTcpMinAvailBW = _CfmFcipEntityExtTcpMinAvailBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 8),
    _CfmFcipEntityExtTcpMinAvailBW_Type()
)
cfmFcipEntityExtTcpMinAvailBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMinAvailBW.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMinAvailBW.setUnits("kilobits")


class _CfmFcipEntityExtTcpRndTrpTimeEst_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpRndTrpTimeEst based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_CfmFcipEntityExtTcpRndTrpTimeEst_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpRndTrpTimeEst_Object = MibTableColumn
cfmFcipEntityExtTcpRndTrpTimeEst = _CfmFcipEntityExtTcpRndTrpTimeEst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 9),
    _CfmFcipEntityExtTcpRndTrpTimeEst_Type()
)
cfmFcipEntityExtTcpRndTrpTimeEst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpRndTrpTimeEst.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpRndTrpTimeEst.setUnits("microseconds")


class _CfmFcipEntityExtCWMEnable_Type(TruthValue):
    """Custom type cfmFcipEntityExtCWMEnable based on TruthValue"""


_CfmFcipEntityExtCWMEnable_Object = MibTableColumn
cfmFcipEntityExtCWMEnable = _CfmFcipEntityExtCWMEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 10),
    _CfmFcipEntityExtCWMEnable_Type()
)
cfmFcipEntityExtCWMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtCWMEnable.setStatus("current")


class _CfmFcipEntityExtCWMBurstSize_Type(Unsigned32):
    """Custom type cfmFcipEntityExtCWMBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CfmFcipEntityExtCWMBurstSize_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtCWMBurstSize_Object = MibTableColumn
cfmFcipEntityExtCWMBurstSize = _CfmFcipEntityExtCWMBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 11),
    _CfmFcipEntityExtCWMBurstSize_Type()
)
cfmFcipEntityExtCWMBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtCWMBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtCWMBurstSize.setUnits("kilobytes")
_CfmFcipEntityExtTcpSACKEnable_Type = TruthValue
_CfmFcipEntityExtTcpSACKEnable_Object = MibTableColumn
cfmFcipEntityExtTcpSACKEnable = _CfmFcipEntityExtTcpSACKEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 12),
    _CfmFcipEntityExtTcpSACKEnable_Type()
)
cfmFcipEntityExtTcpSACKEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpSACKEnable.setStatus("current")
_CfmFcipEntityExtTcpLocalPort_Type = InetPortNumber
_CfmFcipEntityExtTcpLocalPort_Object = MibTableColumn
cfmFcipEntityExtTcpLocalPort = _CfmFcipEntityExtTcpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 13),
    _CfmFcipEntityExtTcpLocalPort_Type()
)
cfmFcipEntityExtTcpLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpLocalPort.setStatus("current")


class _CfmFcipEntityExtTcpMaxJitter_Type(Unsigned32):
    """Custom type cfmFcipEntityExtTcpMaxJitter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfmFcipEntityExtTcpMaxJitter_Type.__name__ = "Unsigned32"
_CfmFcipEntityExtTcpMaxJitter_Object = MibTableColumn
cfmFcipEntityExtTcpMaxJitter = _CfmFcipEntityExtTcpMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 14),
    _CfmFcipEntityExtTcpMaxJitter_Type()
)
cfmFcipEntityExtTcpMaxJitter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipEntityExtTcpMaxJitter.setUnits("milliseconds")
_CfmFcipLinkExtTable_Object = MibTable
cfmFcipLinkExtTable = _CfmFcipLinkExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtTable.setStatus("current")
_CfmFcipLinkExtEntry_Object = MibTableRow
cfmFcipLinkExtEntry = _CfmFcipLinkExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtEntry.setStatus("current")


class _CfmFcipLinkExtPassiveMode_Type(TruthValue):
    """Custom type cfmFcipLinkExtPassiveMode based on TruthValue"""


_CfmFcipLinkExtPassiveMode_Object = MibTableColumn
cfmFcipLinkExtPassiveMode = _CfmFcipLinkExtPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 1),
    _CfmFcipLinkExtPassiveMode_Type()
)
cfmFcipLinkExtPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtPassiveMode.setStatus("current")


class _CfmFcipLinkExtNumTcpConn_Type(Unsigned32):
    """Custom type cfmFcipLinkExtNumTcpConn based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CfmFcipLinkExtNumTcpConn_Type.__name__ = "Unsigned32"
_CfmFcipLinkExtNumTcpConn_Object = MibTableColumn
cfmFcipLinkExtNumTcpConn = _CfmFcipLinkExtNumTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 2),
    _CfmFcipLinkExtNumTcpConn_Type()
)
cfmFcipLinkExtNumTcpConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtNumTcpConn.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipLinkExtNumTcpConn.setUnits("tcp connections")


class _CfmFcipLinkExtCheckTimestamp_Type(TruthValue):
    """Custom type cfmFcipLinkExtCheckTimestamp based on TruthValue"""


_CfmFcipLinkExtCheckTimestamp_Object = MibTableColumn
cfmFcipLinkExtCheckTimestamp = _CfmFcipLinkExtCheckTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 3),
    _CfmFcipLinkExtCheckTimestamp_Type()
)
cfmFcipLinkExtCheckTimestamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtCheckTimestamp.setStatus("current")


class _CfmFcipLinkExtTimestampTolerance_Type(Unsigned32):
    """Custom type cfmFcipLinkExtTimestampTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CfmFcipLinkExtTimestampTolerance_Type.__name__ = "Unsigned32"
_CfmFcipLinkExtTimestampTolerance_Object = MibTableColumn
cfmFcipLinkExtTimestampTolerance = _CfmFcipLinkExtTimestampTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 4),
    _CfmFcipLinkExtTimestampTolerance_Type()
)
cfmFcipLinkExtTimestampTolerance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTimestampTolerance.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTimestampTolerance.setUnits("milliseconds")


class _CfmFcipLinkExtTcpRemPort_Type(CiscoPort):
    """Custom type cfmFcipLinkExtTcpRemPort based on CiscoPort"""
    subtypeSpec = CiscoPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CfmFcipLinkExtTcpRemPort_Type.__name__ = "CiscoPort"
_CfmFcipLinkExtTcpRemPort_Object = MibTableColumn
cfmFcipLinkExtTcpRemPort = _CfmFcipLinkExtTcpRemPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 5),
    _CfmFcipLinkExtTcpRemPort_Type()
)
cfmFcipLinkExtTcpRemPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTcpRemPort.setStatus("current")


class _CfmFcipLinkExtLocalBPortEnable_Type(TruthValue):
    """Custom type cfmFcipLinkExtLocalBPortEnable based on TruthValue"""


_CfmFcipLinkExtLocalBPortEnable_Object = MibTableColumn
cfmFcipLinkExtLocalBPortEnable = _CfmFcipLinkExtLocalBPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 6),
    _CfmFcipLinkExtLocalBPortEnable_Type()
)
cfmFcipLinkExtLocalBPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtLocalBPortEnable.setStatus("current")


class _CfmFcipLinkExtSpecialFrameEnable_Type(TruthValue):
    """Custom type cfmFcipLinkExtSpecialFrameEnable based on TruthValue"""


_CfmFcipLinkExtSpecialFrameEnable_Object = MibTableColumn
cfmFcipLinkExtSpecialFrameEnable = _CfmFcipLinkExtSpecialFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 7),
    _CfmFcipLinkExtSpecialFrameEnable_Type()
)
cfmFcipLinkExtSpecialFrameEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtSpecialFrameEnable.setStatus("current")


class _CfmFcipLinkExtBPortKAEnable_Type(TruthValue):
    """Custom type cfmFcipLinkExtBPortKAEnable based on TruthValue"""


_CfmFcipLinkExtBPortKAEnable_Object = MibTableColumn
cfmFcipLinkExtBPortKAEnable = _CfmFcipLinkExtBPortKAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 8),
    _CfmFcipLinkExtBPortKAEnable_Type()
)
cfmFcipLinkExtBPortKAEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtBPortKAEnable.setStatus("current")


class _CfmFcipLinkExtCntrlQOSField_Type(Unsigned32):
    """Custom type cfmFcipLinkExtCntrlQOSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfmFcipLinkExtCntrlQOSField_Type.__name__ = "Unsigned32"
_CfmFcipLinkExtCntrlQOSField_Object = MibTableColumn
cfmFcipLinkExtCntrlQOSField = _CfmFcipLinkExtCntrlQOSField_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 9),
    _CfmFcipLinkExtCntrlQOSField_Type()
)
cfmFcipLinkExtCntrlQOSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtCntrlQOSField.setStatus("current")


class _CfmFcipLinkExtDataQOSField_Type(Unsigned32):
    """Custom type cfmFcipLinkExtDataQOSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CfmFcipLinkExtDataQOSField_Type.__name__ = "Unsigned32"
_CfmFcipLinkExtDataQOSField_Object = MibTableColumn
cfmFcipLinkExtDataQOSField = _CfmFcipLinkExtDataQOSField_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 10),
    _CfmFcipLinkExtDataQOSField_Type()
)
cfmFcipLinkExtDataQOSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtDataQOSField.setStatus("current")
_CfmFcipLinkExtEthIfIndex_Type = InterfaceIndex
_CfmFcipLinkExtEthIfIndex_Object = MibTableColumn
cfmFcipLinkExtEthIfIndex = _CfmFcipLinkExtEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 11),
    _CfmFcipLinkExtEthIfIndex_Type()
)
cfmFcipLinkExtEthIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtEthIfIndex.setStatus("current")


class _CfmFcipLinkExtWriteAccelerator_Type(TruthValue):
    """Custom type cfmFcipLinkExtWriteAccelerator based on TruthValue"""


_CfmFcipLinkExtWriteAccelerator_Object = MibTableColumn
cfmFcipLinkExtWriteAccelerator = _CfmFcipLinkExtWriteAccelerator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 12),
    _CfmFcipLinkExtWriteAccelerator_Type()
)
cfmFcipLinkExtWriteAccelerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtWriteAccelerator.setStatus("current")


class _CfmFcipLinkExtIPComp_Type(Integer32):
    """Custom type cfmFcipLinkExtIPComp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("highCompressionRatio", 2),
          ("highThroughput", 3),
          ("mode1", 5),
          ("mode2", 6),
          ("mode3", 7),
          ("none", 1))
    )


_CfmFcipLinkExtIPComp_Type.__name__ = "Integer32"
_CfmFcipLinkExtIPComp_Object = MibTableColumn
cfmFcipLinkExtIPComp = _CfmFcipLinkExtIPComp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 13),
    _CfmFcipLinkExtIPComp_Type()
)
cfmFcipLinkExtIPComp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtIPComp.setStatus("current")


class _CfmFcipLinkExtTapeAccelerator_Type(TruthValue):
    """Custom type cfmFcipLinkExtTapeAccelerator based on TruthValue"""


_CfmFcipLinkExtTapeAccelerator_Object = MibTableColumn
cfmFcipLinkExtTapeAccelerator = _CfmFcipLinkExtTapeAccelerator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 14),
    _CfmFcipLinkExtTapeAccelerator_Type()
)
cfmFcipLinkExtTapeAccelerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTapeAccelerator.setStatus("current")


class _CfmFcipLinkExtFlowCtrlBufSize_Type(Unsigned32):
    """Custom type cfmFcipLinkExtFlowCtrlBufSize based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12288),
    )


_CfmFcipLinkExtFlowCtrlBufSize_Type.__name__ = "Unsigned32"
_CfmFcipLinkExtFlowCtrlBufSize_Object = MibTableColumn
cfmFcipLinkExtFlowCtrlBufSize = _CfmFcipLinkExtFlowCtrlBufSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 15),
    _CfmFcipLinkExtFlowCtrlBufSize_Type()
)
cfmFcipLinkExtFlowCtrlBufSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFlowCtrlBufSize.setStatus("current")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFlowCtrlBufSize.setUnits("bytes")


class _CfmFcipLinkExtIPSec_Type(TruthValue):
    """Custom type cfmFcipLinkExtIPSec based on TruthValue"""


_CfmFcipLinkExtIPSec_Object = MibTableColumn
cfmFcipLinkExtIPSec = _CfmFcipLinkExtIPSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 16),
    _CfmFcipLinkExtIPSec_Type()
)
cfmFcipLinkExtIPSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtIPSec.setStatus("current")
_CfmFcipLinkExtPhyIfIndex_Type = InterfaceIndex
_CfmFcipLinkExtPhyIfIndex_Object = MibTableColumn
cfmFcipLinkExtPhyIfIndex = _CfmFcipLinkExtPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 17),
    _CfmFcipLinkExtPhyIfIndex_Type()
)
cfmFcipLinkExtPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtPhyIfIndex.setStatus("current")


class _CfmFcipLinkExtWriteAccOper_Type(TruthValue):
    """Custom type cfmFcipLinkExtWriteAccOper based on TruthValue"""


_CfmFcipLinkExtWriteAccOper_Object = MibTableColumn
cfmFcipLinkExtWriteAccOper = _CfmFcipLinkExtWriteAccOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 18),
    _CfmFcipLinkExtWriteAccOper_Type()
)
cfmFcipLinkExtWriteAccOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtWriteAccOper.setStatus("current")


class _CfmFcipLinkExtTapeAccOper_Type(TruthValue):
    """Custom type cfmFcipLinkExtTapeAccOper based on TruthValue"""


_CfmFcipLinkExtTapeAccOper_Object = MibTableColumn
cfmFcipLinkExtTapeAccOper = _CfmFcipLinkExtTapeAccOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 19),
    _CfmFcipLinkExtTapeAccOper_Type()
)
cfmFcipLinkExtTapeAccOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTapeAccOper.setStatus("current")


class _CfmFcipLinkExtTapeReadAccOper_Type(TruthValue):
    """Custom type cfmFcipLinkExtTapeReadAccOper based on TruthValue"""


_CfmFcipLinkExtTapeReadAccOper_Object = MibTableColumn
cfmFcipLinkExtTapeReadAccOper = _CfmFcipLinkExtTapeReadAccOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 20),
    _CfmFcipLinkExtTapeReadAccOper_Type()
)
cfmFcipLinkExtTapeReadAccOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtTapeReadAccOper.setStatus("current")


class _CfmFcipLinkExtFiconTAVsanL2k_Type(FcList):
    """Custom type cfmFcipLinkExtFiconTAVsanL2k based on FcList"""
    defaultHexValue = ""


_CfmFcipLinkExtFiconTAVsanL2k_Object = MibTableColumn
cfmFcipLinkExtFiconTAVsanL2k = _CfmFcipLinkExtFiconTAVsanL2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 21),
    _CfmFcipLinkExtFiconTAVsanL2k_Type()
)
cfmFcipLinkExtFiconTAVsanL2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFiconTAVsanL2k.setStatus("current")


class _CfmFcipLinkExtFiconTAVsanL4k_Type(FcList):
    """Custom type cfmFcipLinkExtFiconTAVsanL4k based on FcList"""
    defaultHexValue = ""


_CfmFcipLinkExtFiconTAVsanL4k_Object = MibTableColumn
cfmFcipLinkExtFiconTAVsanL4k = _CfmFcipLinkExtFiconTAVsanL4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 22),
    _CfmFcipLinkExtFiconTAVsanL4k_Type()
)
cfmFcipLinkExtFiconTAVsanL4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFiconTAVsanL4k.setStatus("current")
_CfmFcipLinkExtFiconTAVsanLOper2k_Type = FcList
_CfmFcipLinkExtFiconTAVsanLOper2k_Object = MibTableColumn
cfmFcipLinkExtFiconTAVsanLOper2k = _CfmFcipLinkExtFiconTAVsanLOper2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 23),
    _CfmFcipLinkExtFiconTAVsanLOper2k_Type()
)
cfmFcipLinkExtFiconTAVsanLOper2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFiconTAVsanLOper2k.setStatus("current")
_CfmFcipLinkExtFiconTAVsanLOper4k_Type = FcList
_CfmFcipLinkExtFiconTAVsanLOper4k_Object = MibTableColumn
cfmFcipLinkExtFiconTAVsanLOper4k = _CfmFcipLinkExtFiconTAVsanLOper4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 24),
    _CfmFcipLinkExtFiconTAVsanLOper4k_Type()
)
cfmFcipLinkExtFiconTAVsanLOper4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkExtFiconTAVsanLOper4k.setStatus("current")
_CfmFcipLinkMapTable_Object = MibTable
cfmFcipLinkMapTable = _CfmFcipLinkMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmFcipLinkMapTable.setStatus("current")
_CfmFcipLinkMapEntry_Object = MibTableRow
cfmFcipLinkMapEntry = _CfmFcipLinkMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1)
)
cfmFcipLinkMapEntry.setIndexNames(
    (0, "CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkMapIndex"),
)
if mibBuilder.loadTexts:
    cfmFcipLinkMapEntry.setStatus("current")
_CfmFcipLinkMapIndex_Type = Unsigned32
_CfmFcipLinkMapIndex_Object = MibTableColumn
cfmFcipLinkMapIndex = _CfmFcipLinkMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1, 1),
    _CfmFcipLinkMapIndex_Type()
)
cfmFcipLinkMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmFcipLinkMapIndex.setStatus("current")
_CfmFcipMapEntityId_Type = Unsigned32
_CfmFcipMapEntityId_Object = MibTableColumn
cfmFcipMapEntityId = _CfmFcipMapEntityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1, 2),
    _CfmFcipMapEntityId_Type()
)
cfmFcipMapEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipMapEntityId.setStatus("current")
_CfmFcipMgmtExtStats_ObjectIdentity = ObjectIdentity
cfmFcipMgmtExtStats = _CfmFcipMgmtExtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2)
)
_CfmFcipLinkExtStatsTable_Object = MibTable
cfmFcipLinkExtStatsTable = _CfmFcipLinkExtStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtStatsTable.setStatus("current")
_CfmFcipLinkExtStatsEntry_Object = MibTableRow
cfmFcipLinkExtStatsEntry = _CfmFcipLinkExtStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtStatsEntry.setStatus("current")
_CfmFcipLinkStatsRxIPCompRatio_Type = SnmpAdminString
_CfmFcipLinkStatsRxIPCompRatio_Object = MibTableColumn
cfmFcipLinkStatsRxIPCompRatio = _CfmFcipLinkStatsRxIPCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1, 1),
    _CfmFcipLinkStatsRxIPCompRatio_Type()
)
cfmFcipLinkStatsRxIPCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkStatsRxIPCompRatio.setStatus("current")
_CfmFcipLinkStatsTxIPCompRatio_Type = SnmpAdminString
_CfmFcipLinkStatsTxIPCompRatio_Object = MibTableColumn
cfmFcipLinkStatsTxIPCompRatio = _CfmFcipLinkStatsTxIPCompRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1, 2),
    _CfmFcipLinkStatsTxIPCompRatio_Type()
)
cfmFcipLinkStatsTxIPCompRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmFcipLinkStatsTxIPCompRatio.setStatus("current")
_CiscoFcipMgmtExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoFcipMgmtExtMIBConform = _CiscoFcipMgmtExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2)
)
_CfmFcipExtCompliances_ObjectIdentity = ObjectIdentity
cfmFcipExtCompliances = _CfmFcipExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1)
)
_CfmFcipExtGroups_ObjectIdentity = ObjectIdentity
cfmFcipExtGroups = _CfmFcipExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2)
)
cfmFcipEntityInstanceEntry.registerAugmentions(
    ("CISCO-FCIP-MGMT-EXT-MIB",
     "cfmFcipEntityExtEntry")
)
cfmFcipEntityExtEntry.setIndexNames(*cfmFcipEntityInstanceEntry.getIndexNames())
cfmFcipLinkEntry.registerAugmentions(
    ("CISCO-FCIP-MGMT-EXT-MIB",
     "cfmFcipLinkExtEntry")
)
cfmFcipLinkExtEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())
cfmFcipLinkEntry.registerAugmentions(
    ("CISCO-FCIP-MGMT-EXT-MIB",
     "cfmFcipLinkExtStatsEntry")
)
cfmFcipLinkExtStatsEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())

# Managed Objects groups

cfmFcipEntityExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 1)
)
cfmFcipEntityExtGroup.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpKeepAliveTO"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxReTx"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtPMTUEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtPMTUResetTO"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMinRTO"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpSendBufSize"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxBW"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMinAvailBW"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpRndTrpTimeEst"))
)
if mibBuilder.loadTexts:
    cfmFcipEntityExtGroup.setStatus("current")

cfmFcipLinkExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 2)
)
cfmFcipLinkExtGroup.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtPassiveMode"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtNumTcpConn"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtCheckTimestamp"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTimestampTolerance"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTcpRemPort"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtLocalBPortEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtSpecialFrameEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtBPortKAEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtCntrlQOSField"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtDataQOSField"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroup.setStatus("current")

cfmFcipLinkExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 3)
)
cfmFcipLinkExtGroupRev1.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtEthIfIndex"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtWriteAccelerator"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtIPComp"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroupRev1.setStatus("current")

cfmFcipEntityExtCWMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 4)
)
cfmFcipEntityExtCWMGroup.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMBurstSize"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpSACKEnable"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpLocalPort"))
)
if mibBuilder.loadTexts:
    cfmFcipEntityExtCWMGroup.setStatus("current")

cfmFcipLinkExtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 5)
)
cfmFcipLinkExtGroupRev2.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeAccelerator"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFlowCtrlBufSize"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroupRev2.setStatus("current")

cfmFcipLinkExtMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 6)
)
cfmFcipLinkExtMapGroup.setObjects(
    ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipMapEntityId")
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtMapGroup.setStatus("current")

cfmFcipEntityExtGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 7)
)
cfmFcipEntityExtGroupSup1.setObjects(
    ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxJitter")
)
if mibBuilder.loadTexts:
    cfmFcipEntityExtGroupSup1.setStatus("current")

cfmFcipLinkExtGroupRev2Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 8)
)
cfmFcipLinkExtGroupRev2Sup1.setObjects(
    ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtIPSec")
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroupRev2Sup1.setStatus("current")

cfmFcipLinkExtGroupRev2Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 9)
)
cfmFcipLinkExtGroupRev2Sup2.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtPhyIfIndex"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtWriteAccOper"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeAccOper"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroupRev2Sup2.setStatus("current")

cfmFcipLinkExtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 10)
)
cfmFcipLinkExtStatsGroup.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkStatsRxIPCompRatio"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkStatsTxIPCompRatio"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtStatsGroup.setStatus("current")

cfmFcipLinkExtGroupRev2Sup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 11)
)
cfmFcipLinkExtGroupRev2Sup3.setObjects(
      *(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeReadAccOper"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanL2k"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanL4k"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanLOper2k"),
        ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanLOper4k"))
)
if mibBuilder.loadTexts:
    cfmFcipLinkExtGroupRev2Sup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmFcipExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance1.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance2.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance3.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance4.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance5.setStatus(
        "deprecated"
    )

cfmFcipExtCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cfmFcipExtCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCIP-MGMT-EXT-MIB",
    **{"ciscoFcipMgmtExtMIB": ciscoFcipMgmtExtMIB,
       "ciscoFcipMgmtExtMIBNotifs": ciscoFcipMgmtExtMIBNotifs,
       "ciscoFcipMgmtExtMIBObjects": ciscoFcipMgmtExtMIBObjects,
       "cfmFcipMgmtExtConfig": cfmFcipMgmtExtConfig,
       "cfmFcipEntityExtTable": cfmFcipEntityExtTable,
       "cfmFcipEntityExtEntry": cfmFcipEntityExtEntry,
       "cfmFcipEntityExtTcpKeepAliveTO": cfmFcipEntityExtTcpKeepAliveTO,
       "cfmFcipEntityExtTcpMaxReTx": cfmFcipEntityExtTcpMaxReTx,
       "cfmFcipEntityExtPMTUEnable": cfmFcipEntityExtPMTUEnable,
       "cfmFcipEntityExtPMTUResetTO": cfmFcipEntityExtPMTUResetTO,
       "cfmFcipEntityExtTcpMinRTO": cfmFcipEntityExtTcpMinRTO,
       "cfmFcipEntityExtTcpSendBufSize": cfmFcipEntityExtTcpSendBufSize,
       "cfmFcipEntityExtTcpMaxBW": cfmFcipEntityExtTcpMaxBW,
       "cfmFcipEntityExtTcpMinAvailBW": cfmFcipEntityExtTcpMinAvailBW,
       "cfmFcipEntityExtTcpRndTrpTimeEst": cfmFcipEntityExtTcpRndTrpTimeEst,
       "cfmFcipEntityExtCWMEnable": cfmFcipEntityExtCWMEnable,
       "cfmFcipEntityExtCWMBurstSize": cfmFcipEntityExtCWMBurstSize,
       "cfmFcipEntityExtTcpSACKEnable": cfmFcipEntityExtTcpSACKEnable,
       "cfmFcipEntityExtTcpLocalPort": cfmFcipEntityExtTcpLocalPort,
       "cfmFcipEntityExtTcpMaxJitter": cfmFcipEntityExtTcpMaxJitter,
       "cfmFcipLinkExtTable": cfmFcipLinkExtTable,
       "cfmFcipLinkExtEntry": cfmFcipLinkExtEntry,
       "cfmFcipLinkExtPassiveMode": cfmFcipLinkExtPassiveMode,
       "cfmFcipLinkExtNumTcpConn": cfmFcipLinkExtNumTcpConn,
       "cfmFcipLinkExtCheckTimestamp": cfmFcipLinkExtCheckTimestamp,
       "cfmFcipLinkExtTimestampTolerance": cfmFcipLinkExtTimestampTolerance,
       "cfmFcipLinkExtTcpRemPort": cfmFcipLinkExtTcpRemPort,
       "cfmFcipLinkExtLocalBPortEnable": cfmFcipLinkExtLocalBPortEnable,
       "cfmFcipLinkExtSpecialFrameEnable": cfmFcipLinkExtSpecialFrameEnable,
       "cfmFcipLinkExtBPortKAEnable": cfmFcipLinkExtBPortKAEnable,
       "cfmFcipLinkExtCntrlQOSField": cfmFcipLinkExtCntrlQOSField,
       "cfmFcipLinkExtDataQOSField": cfmFcipLinkExtDataQOSField,
       "cfmFcipLinkExtEthIfIndex": cfmFcipLinkExtEthIfIndex,
       "cfmFcipLinkExtWriteAccelerator": cfmFcipLinkExtWriteAccelerator,
       "cfmFcipLinkExtIPComp": cfmFcipLinkExtIPComp,
       "cfmFcipLinkExtTapeAccelerator": cfmFcipLinkExtTapeAccelerator,
       "cfmFcipLinkExtFlowCtrlBufSize": cfmFcipLinkExtFlowCtrlBufSize,
       "cfmFcipLinkExtIPSec": cfmFcipLinkExtIPSec,
       "cfmFcipLinkExtPhyIfIndex": cfmFcipLinkExtPhyIfIndex,
       "cfmFcipLinkExtWriteAccOper": cfmFcipLinkExtWriteAccOper,
       "cfmFcipLinkExtTapeAccOper": cfmFcipLinkExtTapeAccOper,
       "cfmFcipLinkExtTapeReadAccOper": cfmFcipLinkExtTapeReadAccOper,
       "cfmFcipLinkExtFiconTAVsanL2k": cfmFcipLinkExtFiconTAVsanL2k,
       "cfmFcipLinkExtFiconTAVsanL4k": cfmFcipLinkExtFiconTAVsanL4k,
       "cfmFcipLinkExtFiconTAVsanLOper2k": cfmFcipLinkExtFiconTAVsanLOper2k,
       "cfmFcipLinkExtFiconTAVsanLOper4k": cfmFcipLinkExtFiconTAVsanLOper4k,
       "cfmFcipLinkMapTable": cfmFcipLinkMapTable,
       "cfmFcipLinkMapEntry": cfmFcipLinkMapEntry,
       "cfmFcipLinkMapIndex": cfmFcipLinkMapIndex,
       "cfmFcipMapEntityId": cfmFcipMapEntityId,
       "cfmFcipMgmtExtStats": cfmFcipMgmtExtStats,
       "cfmFcipLinkExtStatsTable": cfmFcipLinkExtStatsTable,
       "cfmFcipLinkExtStatsEntry": cfmFcipLinkExtStatsEntry,
       "cfmFcipLinkStatsRxIPCompRatio": cfmFcipLinkStatsRxIPCompRatio,
       "cfmFcipLinkStatsTxIPCompRatio": cfmFcipLinkStatsTxIPCompRatio,
       "ciscoFcipMgmtExtMIBConform": ciscoFcipMgmtExtMIBConform,
       "cfmFcipExtCompliances": cfmFcipExtCompliances,
       "cfmFcipExtCompliance": cfmFcipExtCompliance,
       "cfmFcipExtCompliance1": cfmFcipExtCompliance1,
       "cfmFcipExtCompliance2": cfmFcipExtCompliance2,
       "cfmFcipExtCompliance3": cfmFcipExtCompliance3,
       "cfmFcipExtCompliance4": cfmFcipExtCompliance4,
       "cfmFcipExtCompliance5": cfmFcipExtCompliance5,
       "cfmFcipExtCompliance6": cfmFcipExtCompliance6,
       "cfmFcipExtGroups": cfmFcipExtGroups,
       "cfmFcipEntityExtGroup": cfmFcipEntityExtGroup,
       "cfmFcipLinkExtGroup": cfmFcipLinkExtGroup,
       "cfmFcipLinkExtGroupRev1": cfmFcipLinkExtGroupRev1,
       "cfmFcipEntityExtCWMGroup": cfmFcipEntityExtCWMGroup,
       "cfmFcipLinkExtGroupRev2": cfmFcipLinkExtGroupRev2,
       "cfmFcipLinkExtMapGroup": cfmFcipLinkExtMapGroup,
       "cfmFcipEntityExtGroupSup1": cfmFcipEntityExtGroupSup1,
       "cfmFcipLinkExtGroupRev2Sup1": cfmFcipLinkExtGroupRev2Sup1,
       "cfmFcipLinkExtGroupRev2Sup2": cfmFcipLinkExtGroupRev2Sup2,
       "cfmFcipLinkExtStatsGroup": cfmFcipLinkExtStatsGroup,
       "cfmFcipLinkExtGroupRev2Sup3": cfmFcipLinkExtGroupRev2Sup3}
)
