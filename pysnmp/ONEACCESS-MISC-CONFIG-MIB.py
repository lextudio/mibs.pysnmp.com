# SNMP MIB module (ONEACCESS-MISC-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-MISC-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:58 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(oacExpIMIpAcl,
 oacExpIMManagement,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIpAcl",
    "oacExpIMManagement",
    "oacMIBModules")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oacMiscConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2003)
)
oacMiscConfigMIB.setRevisions(
        ("2011-07-26 00:00",
         "2011-06-15 00:00",
         "2010-12-17 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacMiscConfig_ObjectIdentity = ObjectIdentity
oacMiscConfig = _OacMiscConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21)
)
_OacTelnetServerConfigObjects_ObjectIdentity = ObjectIdentity
oacTelnetServerConfigObjects = _OacTelnetServerConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1)
)
_OacTelnetServerBindInterfaceTable_Object = MibTable
oacTelnetServerBindInterfaceTable = _OacTelnetServerBindInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1)
)
if mibBuilder.loadTexts:
    oacTelnetServerBindInterfaceTable.setStatus("current")
_OacTelnetServerBindInterfaceEntry_Object = MibTableRow
oacTelnetServerBindInterfaceEntry = _OacTelnetServerBindInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1)
)
oacTelnetServerBindInterfaceEntry.setIndexNames(
    (0, "ONEACCESS-MISC-CONFIG-MIB", "oacTelnetServerBindInterfaceIndex"),
)
if mibBuilder.loadTexts:
    oacTelnetServerBindInterfaceEntry.setStatus("current")
_OacTelnetServerBindInterfaceIndex_Type = InterfaceIndex
_OacTelnetServerBindInterfaceIndex_Object = MibTableColumn
oacTelnetServerBindInterfaceIndex = _OacTelnetServerBindInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 1),
    _OacTelnetServerBindInterfaceIndex_Type()
)
oacTelnetServerBindInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacTelnetServerBindInterfaceIndex.setStatus("current")


class _OacTelnetServerBindInterfaceName_Type(OctetString):
    """Custom type oacTelnetServerBindInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacTelnetServerBindInterfaceName_Type.__name__ = "OctetString"
_OacTelnetServerBindInterfaceName_Object = MibTableColumn
oacTelnetServerBindInterfaceName = _OacTelnetServerBindInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 2),
    _OacTelnetServerBindInterfaceName_Type()
)
oacTelnetServerBindInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacTelnetServerBindInterfaceName.setStatus("current")
_OacTelnetServerBindInterfaceRowStatus_Type = RowStatus
_OacTelnetServerBindInterfaceRowStatus_Object = MibTableColumn
oacTelnetServerBindInterfaceRowStatus = _OacTelnetServerBindInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 1, 1, 3),
    _OacTelnetServerBindInterfaceRowStatus_Type()
)
oacTelnetServerBindInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacTelnetServerBindInterfaceRowStatus.setStatus("current")


class _OacTelnetServerBindAcl_Type(OctetString):
    """Custom type oacTelnetServerBindAcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacTelnetServerBindAcl_Type.__name__ = "OctetString"
_OacTelnetServerBindAcl_Object = MibScalar
oacTelnetServerBindAcl = _OacTelnetServerBindAcl_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 2),
    _OacTelnetServerBindAcl_Type()
)
oacTelnetServerBindAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacTelnetServerBindAcl.setStatus("current")


class _OacTelnetServerIdleTimeout_Type(Unsigned32):
    """Custom type oacTelnetServerIdleTimeout based on Unsigned32"""
    defaultValue = 600


_OacTelnetServerIdleTimeout_Object = MibScalar
oacTelnetServerIdleTimeout = _OacTelnetServerIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 3),
    _OacTelnetServerIdleTimeout_Type()
)
oacTelnetServerIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacTelnetServerIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oacTelnetServerIdleTimeout.setUnits("seconds")


class _OacTelnetServerLogEnable_Type(TruthValue):
    """Custom type oacTelnetServerLogEnable based on TruthValue"""


_OacTelnetServerLogEnable_Object = MibScalar
oacTelnetServerLogEnable = _OacTelnetServerLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 4),
    _OacTelnetServerLogEnable_Type()
)
oacTelnetServerLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacTelnetServerLogEnable.setStatus("current")


class _OacTelnetServerLogFileSize_Type(Integer32):
    """Custom type oacTelnetServerLogFileSize based on Integer32"""
    defaultValue = 8200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(82, 8200),
    )


_OacTelnetServerLogFileSize_Type.__name__ = "Integer32"
_OacTelnetServerLogFileSize_Object = MibScalar
oacTelnetServerLogFileSize = _OacTelnetServerLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 1, 5),
    _OacTelnetServerLogFileSize_Type()
)
oacTelnetServerLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacTelnetServerLogFileSize.setStatus("current")
if mibBuilder.loadTexts:
    oacTelnetServerLogFileSize.setUnits("bytes")
_OacSyslogServerConfigObjects_ObjectIdentity = ObjectIdentity
oacSyslogServerConfigObjects = _OacSyslogServerConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2)
)
_OacSyslogServerTable_Object = MibTable
oacSyslogServerTable = _OacSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1)
)
if mibBuilder.loadTexts:
    oacSyslogServerTable.setStatus("current")
_OacSyslogServerEntry_Object = MibTableRow
oacSyslogServerEntry = _OacSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1)
)
oacSyslogServerEntry.setIndexNames(
    (0, "ONEACCESS-MISC-CONFIG-MIB", "oacSyslogServerAddress"),
)
if mibBuilder.loadTexts:
    oacSyslogServerEntry.setStatus("current")


class _OacSyslogServerAddress_Type(OctetString):
    """Custom type oacSyslogServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSyslogServerAddress_Type.__name__ = "OctetString"
_OacSyslogServerAddress_Object = MibTableColumn
oacSyslogServerAddress = _OacSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 1),
    _OacSyslogServerAddress_Type()
)
oacSyslogServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSyslogServerAddress.setStatus("current")


class _OacSyslogServerFacilityNum_Type(Integer32):
    """Custom type oacSyslogServerFacilityNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_OacSyslogServerFacilityNum_Type.__name__ = "Integer32"
_OacSyslogServerFacilityNum_Object = MibTableColumn
oacSyslogServerFacilityNum = _OacSyslogServerFacilityNum_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 2),
    _OacSyslogServerFacilityNum_Type()
)
oacSyslogServerFacilityNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSyslogServerFacilityNum.setStatus("current")
_OacSyslogServerInterface_Type = InterfaceIndex
_OacSyslogServerInterface_Object = MibTableColumn
oacSyslogServerInterface = _OacSyslogServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 3),
    _OacSyslogServerInterface_Type()
)
oacSyslogServerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSyslogServerInterface.setStatus("current")
_OacSyslogServerRowStatus_Type = RowStatus
_OacSyslogServerRowStatus_Object = MibTableColumn
oacSyslogServerRowStatus = _OacSyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 1, 1, 4),
    _OacSyslogServerRowStatus_Type()
)
oacSyslogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSyslogServerRowStatus.setStatus("current")


class _OacSyslogMaxServers_Type(Integer32):
    """Custom type oacSyslogMaxServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_OacSyslogMaxServers_Type.__name__ = "Integer32"
_OacSyslogMaxServers_Object = MibScalar
oacSyslogMaxServers = _OacSyslogMaxServers_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 2, 2),
    _OacSyslogMaxServers_Type()
)
oacSyslogMaxServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSyslogMaxServers.setStatus("current")
_OacSntpClientConfigObjects_ObjectIdentity = ObjectIdentity
oacSntpClientConfigObjects = _OacSntpClientConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3)
)
_OacSntpClientBroadcastEnable_Type = TruthValue
_OacSntpClientBroadcastEnable_Object = MibScalar
oacSntpClientBroadcastEnable = _OacSntpClientBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 1),
    _OacSntpClientBroadcastEnable_Type()
)
oacSntpClientBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSntpClientBroadcastEnable.setStatus("current")
_OacSntpRemoteServerTable_Object = MibTable
oacSntpRemoteServerTable = _OacSntpRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2)
)
if mibBuilder.loadTexts:
    oacSntpRemoteServerTable.setStatus("current")
_OacSntpRemoteServerEntry_Object = MibTableRow
oacSntpRemoteServerEntry = _OacSntpRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1)
)
oacSntpRemoteServerEntry.setIndexNames(
    (0, "ONEACCESS-MISC-CONFIG-MIB", "oacSntpRemoteServerAddress"),
)
if mibBuilder.loadTexts:
    oacSntpRemoteServerEntry.setStatus("current")


class _OacSntpRemoteServerAddress_Type(OctetString):
    """Custom type oacSntpRemoteServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSntpRemoteServerAddress_Type.__name__ = "OctetString"
_OacSntpRemoteServerAddress_Object = MibTableColumn
oacSntpRemoteServerAddress = _OacSntpRemoteServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 1),
    _OacSntpRemoteServerAddress_Type()
)
oacSntpRemoteServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSntpRemoteServerAddress.setStatus("current")
_OacSntpRemoteServerInterface_Type = InterfaceIndex
_OacSntpRemoteServerInterface_Object = MibTableColumn
oacSntpRemoteServerInterface = _OacSntpRemoteServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 2),
    _OacSntpRemoteServerInterface_Type()
)
oacSntpRemoteServerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSntpRemoteServerInterface.setStatus("current")
_OacSntpRemoteServerRowStatus_Type = RowStatus
_OacSntpRemoteServerRowStatus_Object = MibTableColumn
oacSntpRemoteServerRowStatus = _OacSntpRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 2, 1, 3),
    _OacSntpRemoteServerRowStatus_Type()
)
oacSntpRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSntpRemoteServerRowStatus.setStatus("current")


class _OacSntpClientPollInterval_Type(Unsigned32):
    """Custom type oacSntpClientPollInterval based on Unsigned32"""
    defaultValue = 64


_OacSntpClientPollInterval_Object = MibScalar
oacSntpClientPollInterval = _OacSntpClientPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 3, 3),
    _OacSntpClientPollInterval_Type()
)
oacSntpClientPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSntpClientPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    oacSntpClientPollInterval.setUnits("seconds")
_OacBannerConfigObjects_ObjectIdentity = ObjectIdentity
oacBannerConfigObjects = _OacBannerConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4)
)
_OacConfigBannerSeqTable_Object = MibTable
oacConfigBannerSeqTable = _OacConfigBannerSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1)
)
if mibBuilder.loadTexts:
    oacConfigBannerSeqTable.setStatus("current")
_OacConfigBannerSeqEntry_Object = MibTableRow
oacConfigBannerSeqEntry = _OacConfigBannerSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1)
)
oacConfigBannerSeqEntry.setIndexNames(
    (0, "ONEACCESS-MISC-CONFIG-MIB", "oacConfigBannerSequence"),
)
if mibBuilder.loadTexts:
    oacConfigBannerSeqEntry.setStatus("current")


class _OacConfigBannerType_Type(Integer32):
    """Custom type oacConfigBannerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exec", 2),
          ("motd", 1))
    )


_OacConfigBannerType_Type.__name__ = "Integer32"
_OacConfigBannerType_Object = MibTableColumn
oacConfigBannerType = _OacConfigBannerType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 1),
    _OacConfigBannerType_Type()
)
oacConfigBannerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacConfigBannerType.setStatus("current")


class _OacConfigBannerSequence_Type(Integer32):
    """Custom type oacConfigBannerSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_OacConfigBannerSequence_Type.__name__ = "Integer32"
_OacConfigBannerSequence_Object = MibTableColumn
oacConfigBannerSequence = _OacConfigBannerSequence_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 2),
    _OacConfigBannerSequence_Type()
)
oacConfigBannerSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacConfigBannerSequence.setStatus("current")


class _OacConfigBannerString_Type(OctetString):
    """Custom type oacConfigBannerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacConfigBannerString_Type.__name__ = "OctetString"
_OacConfigBannerString_Object = MibTableColumn
oacConfigBannerString = _OacConfigBannerString_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 3),
    _OacConfigBannerString_Type()
)
oacConfigBannerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacConfigBannerString.setStatus("current")
_OacConfigBannerSeqRowStatus_Type = RowStatus
_OacConfigBannerSeqRowStatus_Object = MibTableColumn
oacConfigBannerSeqRowStatus = _OacConfigBannerSeqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 1, 1, 4),
    _OacConfigBannerSeqRowStatus_Type()
)
oacConfigBannerSeqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacConfigBannerSeqRowStatus.setStatus("current")


class _OacConfigMotdBanner_Type(OctetString):
    """Custom type oacConfigMotdBanner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 230),
    )


_OacConfigMotdBanner_Type.__name__ = "OctetString"
_OacConfigMotdBanner_Object = MibScalar
oacConfigMotdBanner = _OacConfigMotdBanner_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 2),
    _OacConfigMotdBanner_Type()
)
oacConfigMotdBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacConfigMotdBanner.setStatus("current")


class _OacConfigExecBanner_Type(OctetString):
    """Custom type oacConfigExecBanner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 230),
    )


_OacConfigExecBanner_Type.__name__ = "OctetString"
_OacConfigExecBanner_Object = MibScalar
oacConfigExecBanner = _OacConfigExecBanner_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 4, 3),
    _OacConfigExecBanner_Type()
)
oacConfigExecBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacConfigExecBanner.setStatus("current")
_OacDateAndTimeConfigObjects_ObjectIdentity = ObjectIdentity
oacDateAndTimeConfigObjects = _OacDateAndTimeConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5)
)
_OacMiscConfigDateAndTime_Type = DateAndTime
_OacMiscConfigDateAndTime_Object = MibScalar
oacMiscConfigDateAndTime = _OacMiscConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 1),
    _OacMiscConfigDateAndTime_Type()
)
oacMiscConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacMiscConfigDateAndTime.setStatus("current")
_OacConfigClockDstTable_Object = MibTable
oacConfigClockDstTable = _OacConfigClockDstTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2)
)
if mibBuilder.loadTexts:
    oacConfigClockDstTable.setStatus("current")
_OacConfigClockDstEntry_Object = MibTableRow
oacConfigClockDstEntry = _OacConfigClockDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1)
)
oacConfigClockDstEntry.setIndexNames(
    (0, "ONEACCESS-MISC-CONFIG-MIB", "oacClockDstName"),
)
if mibBuilder.loadTexts:
    oacConfigClockDstEntry.setStatus("current")


class _OacClockDstName_Type(OctetString):
    """Custom type oacClockDstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacClockDstName_Type.__name__ = "OctetString"
_OacClockDstName_Object = MibTableColumn
oacClockDstName = _OacClockDstName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 1),
    _OacClockDstName_Type()
)
oacClockDstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstName.setStatus("current")


class _OacClockDstSummerStartWeek_Type(OctetString):
    """Custom type oacClockDstSummerStartWeek based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacClockDstSummerStartWeek_Type.__name__ = "OctetString"
_OacClockDstSummerStartWeek_Object = MibTableColumn
oacClockDstSummerStartWeek = _OacClockDstSummerStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 2),
    _OacClockDstSummerStartWeek_Type()
)
oacClockDstSummerStartWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstSummerStartWeek.setStatus("current")


class _OacClockDstSummerStartDate_Type(OctetString):
    """Custom type oacClockDstSummerStartDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacClockDstSummerStartDate_Type.__name__ = "OctetString"
_OacClockDstSummerStartDate_Object = MibTableColumn
oacClockDstSummerStartDate = _OacClockDstSummerStartDate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 3),
    _OacClockDstSummerStartDate_Type()
)
oacClockDstSummerStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstSummerStartDate.setStatus("current")


class _OacClockDstWinterStartWeek_Type(OctetString):
    """Custom type oacClockDstWinterStartWeek based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacClockDstWinterStartWeek_Type.__name__ = "OctetString"
_OacClockDstWinterStartWeek_Object = MibTableColumn
oacClockDstWinterStartWeek = _OacClockDstWinterStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 4),
    _OacClockDstWinterStartWeek_Type()
)
oacClockDstWinterStartWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstWinterStartWeek.setStatus("current")


class _OacClockDstWinterStartDate_Type(OctetString):
    """Custom type oacClockDstWinterStartDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacClockDstWinterStartDate_Type.__name__ = "OctetString"
_OacClockDstWinterStartDate_Object = MibTableColumn
oacClockDstWinterStartDate = _OacClockDstWinterStartDate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 5),
    _OacClockDstWinterStartDate_Type()
)
oacClockDstWinterStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstWinterStartDate.setStatus("current")
_OacClockDstRowStatus_Type = RowStatus
_OacClockDstRowStatus_Object = MibTableColumn
oacClockDstRowStatus = _OacClockDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 5, 2, 1, 6),
    _OacClockDstRowStatus_Type()
)
oacClockDstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacClockDstRowStatus.setStatus("current")
_OacMiscConfigConformance_ObjectIdentity = ObjectIdentity
oacMiscConfigConformance = _OacMiscConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6)
)
_OacMiscConfigGroups_ObjectIdentity = ObjectIdentity
oacMiscConfigGroups = _OacMiscConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 1)
)
_OacMiscCompls_ObjectIdentity = ObjectIdentity
oacMiscCompls = _OacMiscCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 2)
)

# Managed Objects groups

oacMiscConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 21, 6, 1, 1)
)
oacMiscConfigGroup.setObjects(
    ("ONEACCESS-MISC-CONFIG-MIB", "oacConfigBannerString")
)
if mibBuilder.loadTexts:
    oacMiscConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-MISC-CONFIG-MIB",
    **{"oacMiscConfigMIB": oacMiscConfigMIB,
       "oacMiscConfig": oacMiscConfig,
       "oacTelnetServerConfigObjects": oacTelnetServerConfigObjects,
       "oacTelnetServerBindInterfaceTable": oacTelnetServerBindInterfaceTable,
       "oacTelnetServerBindInterfaceEntry": oacTelnetServerBindInterfaceEntry,
       "oacTelnetServerBindInterfaceIndex": oacTelnetServerBindInterfaceIndex,
       "oacTelnetServerBindInterfaceName": oacTelnetServerBindInterfaceName,
       "oacTelnetServerBindInterfaceRowStatus": oacTelnetServerBindInterfaceRowStatus,
       "oacTelnetServerBindAcl": oacTelnetServerBindAcl,
       "oacTelnetServerIdleTimeout": oacTelnetServerIdleTimeout,
       "oacTelnetServerLogEnable": oacTelnetServerLogEnable,
       "oacTelnetServerLogFileSize": oacTelnetServerLogFileSize,
       "oacSyslogServerConfigObjects": oacSyslogServerConfigObjects,
       "oacSyslogServerTable": oacSyslogServerTable,
       "oacSyslogServerEntry": oacSyslogServerEntry,
       "oacSyslogServerAddress": oacSyslogServerAddress,
       "oacSyslogServerFacilityNum": oacSyslogServerFacilityNum,
       "oacSyslogServerInterface": oacSyslogServerInterface,
       "oacSyslogServerRowStatus": oacSyslogServerRowStatus,
       "oacSyslogMaxServers": oacSyslogMaxServers,
       "oacSntpClientConfigObjects": oacSntpClientConfigObjects,
       "oacSntpClientBroadcastEnable": oacSntpClientBroadcastEnable,
       "oacSntpRemoteServerTable": oacSntpRemoteServerTable,
       "oacSntpRemoteServerEntry": oacSntpRemoteServerEntry,
       "oacSntpRemoteServerAddress": oacSntpRemoteServerAddress,
       "oacSntpRemoteServerInterface": oacSntpRemoteServerInterface,
       "oacSntpRemoteServerRowStatus": oacSntpRemoteServerRowStatus,
       "oacSntpClientPollInterval": oacSntpClientPollInterval,
       "oacBannerConfigObjects": oacBannerConfigObjects,
       "oacConfigBannerSeqTable": oacConfigBannerSeqTable,
       "oacConfigBannerSeqEntry": oacConfigBannerSeqEntry,
       "oacConfigBannerType": oacConfigBannerType,
       "oacConfigBannerSequence": oacConfigBannerSequence,
       "oacConfigBannerString": oacConfigBannerString,
       "oacConfigBannerSeqRowStatus": oacConfigBannerSeqRowStatus,
       "oacConfigMotdBanner": oacConfigMotdBanner,
       "oacConfigExecBanner": oacConfigExecBanner,
       "oacDateAndTimeConfigObjects": oacDateAndTimeConfigObjects,
       "oacMiscConfigDateAndTime": oacMiscConfigDateAndTime,
       "oacConfigClockDstTable": oacConfigClockDstTable,
       "oacConfigClockDstEntry": oacConfigClockDstEntry,
       "oacClockDstName": oacClockDstName,
       "oacClockDstSummerStartWeek": oacClockDstSummerStartWeek,
       "oacClockDstSummerStartDate": oacClockDstSummerStartDate,
       "oacClockDstWinterStartWeek": oacClockDstWinterStartWeek,
       "oacClockDstWinterStartDate": oacClockDstWinterStartDate,
       "oacClockDstRowStatus": oacClockDstRowStatus,
       "oacMiscConfigConformance": oacMiscConfigConformance,
       "oacMiscConfigGroups": oacMiscConfigGroups,
       "oacMiscConfigGroup": oacMiscConfigGroup,
       "oacMiscCompls": oacMiscCompls}
)
