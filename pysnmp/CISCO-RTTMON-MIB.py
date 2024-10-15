# SNMP MIB module (CISCO-RTTMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RTTMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:00 2024
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

(CfmMepid,) = mibBuilder.importSymbols(
    "CISCO-ETHER-CFM-MIB",
    "CfmMepid")

(QosLayer2Cos,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "QosLayer2Cos")

(RttMonCodecType,
 RttMonLSPPingReplyMode,
 RttMonOperation,
 RttMonProtocol,
 RttMonReactVar,
 RttMonRttType,
 RttMonScheduleStartType,
 RttMonTargetAddress,
 RttMplsVpnMonLpdFailureSense,
 RttMplsVpnMonLpdGrpStatus,
 RttMplsVpnMonRttType,
 RttReset,
 RttResponseSense) = mibBuilder.importSymbols(
    "CISCO-RTTMON-TC-MIB",
    "RttMonCodecType",
    "RttMonLSPPingReplyMode",
    "RttMonOperation",
    "RttMonProtocol",
    "RttMonReactVar",
    "RttMonRttType",
    "RttMonScheduleStartType",
    "RttMonTargetAddress",
    "RttMplsVpnMonLpdFailureSense",
    "RttMplsVpnMonLpdGrpStatus",
    "RttMplsVpnMonRttType",
    "RttReset",
    "RttResponseSense")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoRttMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42)
)
ciscoRttMonMIB.setRevisions(
        ("2016-04-14 00:00",
         "2014-04-10 00:00",
         "2012-08-16 00:00",
         "2011-09-15 00:00",
         "2011-02-21 00:00",
         "2010-10-18 00:00",
         "2010-06-04 00:00",
         "2009-04-07 00:00",
         "2008-03-24 00:00",
         "2008-01-06 00:00",
         "2006-12-08 00:00",
         "2006-06-08 00:00",
         "2006-03-02 00:00",
         "2005-08-11 00:00",
         "2005-04-21 00:00",
         "2005-01-04 00:00",
         "2004-08-26 00:00",
         "2004-05-18 00:00",
         "2004-01-20 00:00",
         "2003-08-11 00:00",
         "2003-05-21 00:00",
         "2003-04-15 00:00",
         "2003-03-12 00:00",
         "2000-11-03 00:00",
         "1999-06-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoRttMonObjects_ObjectIdentity = ObjectIdentity
ciscoRttMonObjects = _CiscoRttMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1)
)
_RttMonAppl_ObjectIdentity = ObjectIdentity
rttMonAppl = _RttMonAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1)
)
_RttMonApplVersion_Type = DisplayString
_RttMonApplVersion_Object = MibScalar
rttMonApplVersion = _RttMonApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 1),
    _RttMonApplVersion_Type()
)
rttMonApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplVersion.setStatus("current")


class _RttMonApplMaxPacketDataSize_Type(Integer32):
    """Custom type rttMonApplMaxPacketDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonApplMaxPacketDataSize_Type.__name__ = "Integer32"
_RttMonApplMaxPacketDataSize_Object = MibScalar
rttMonApplMaxPacketDataSize = _RttMonApplMaxPacketDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 2),
    _RttMonApplMaxPacketDataSize_Type()
)
rttMonApplMaxPacketDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplMaxPacketDataSize.setStatus("current")
if mibBuilder.loadTexts:
    rttMonApplMaxPacketDataSize.setUnits("octets")
_RttMonApplTimeOfLastSet_Type = TimeStamp
_RttMonApplTimeOfLastSet_Object = MibScalar
rttMonApplTimeOfLastSet = _RttMonApplTimeOfLastSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 3),
    _RttMonApplTimeOfLastSet_Type()
)
rttMonApplTimeOfLastSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplTimeOfLastSet.setStatus("current")


class _RttMonApplNumCtrlAdminEntry_Type(Integer32):
    """Custom type rttMonApplNumCtrlAdminEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonApplNumCtrlAdminEntry_Type.__name__ = "Integer32"
_RttMonApplNumCtrlAdminEntry_Object = MibScalar
rttMonApplNumCtrlAdminEntry = _RttMonApplNumCtrlAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 4),
    _RttMonApplNumCtrlAdminEntry_Type()
)
rttMonApplNumCtrlAdminEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplNumCtrlAdminEntry.setStatus("current")
_RttMonApplReset_Type = RttReset
_RttMonApplReset_Object = MibScalar
rttMonApplReset = _RttMonApplReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 5),
    _RttMonApplReset_Type()
)
rttMonApplReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplReset.setStatus("current")
_RttMonApplPreConfigedReset_Type = RttReset
_RttMonApplPreConfigedReset_Object = MibScalar
rttMonApplPreConfigedReset = _RttMonApplPreConfigedReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 6),
    _RttMonApplPreConfigedReset_Type()
)
rttMonApplPreConfigedReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedReset.setStatus("obsolete")
_RttMonApplSupportedRttTypesTable_Object = MibTable
rttMonApplSupportedRttTypesTable = _RttMonApplSupportedRttTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesTable.setStatus("current")
_RttMonApplSupportedRttTypesEntry_Object = MibTableRow
rttMonApplSupportedRttTypesEntry = _RttMonApplSupportedRttTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1)
)
rttMonApplSupportedRttTypesEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplSupportedRttTypes"),
)
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesEntry.setStatus("current")
_RttMonApplSupportedRttTypes_Type = RttMonRttType
_RttMonApplSupportedRttTypes_Object = MibTableColumn
rttMonApplSupportedRttTypes = _RttMonApplSupportedRttTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1, 1),
    _RttMonApplSupportedRttTypes_Type()
)
rttMonApplSupportedRttTypes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypes.setStatus("current")
_RttMonApplSupportedRttTypesValid_Type = TruthValue
_RttMonApplSupportedRttTypesValid_Object = MibTableColumn
rttMonApplSupportedRttTypesValid = _RttMonApplSupportedRttTypesValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1, 2),
    _RttMonApplSupportedRttTypesValid_Type()
)
rttMonApplSupportedRttTypesValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesValid.setStatus("current")
_RttMonApplSupportedProtocolsTable_Object = MibTable
rttMonApplSupportedProtocolsTable = _RttMonApplSupportedProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsTable.setStatus("current")
_RttMonApplSupportedProtocolsEntry_Object = MibTableRow
rttMonApplSupportedProtocolsEntry = _RttMonApplSupportedProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1)
)
rttMonApplSupportedProtocolsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplSupportedProtocols"),
)
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsEntry.setStatus("current")
_RttMonApplSupportedProtocols_Type = RttMonProtocol
_RttMonApplSupportedProtocols_Object = MibTableColumn
rttMonApplSupportedProtocols = _RttMonApplSupportedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1, 1),
    _RttMonApplSupportedProtocols_Type()
)
rttMonApplSupportedProtocols.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocols.setStatus("current")
_RttMonApplSupportedProtocolsValid_Type = TruthValue
_RttMonApplSupportedProtocolsValid_Object = MibTableColumn
rttMonApplSupportedProtocolsValid = _RttMonApplSupportedProtocolsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1, 2),
    _RttMonApplSupportedProtocolsValid_Type()
)
rttMonApplSupportedProtocolsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsValid.setStatus("current")
_RttMonApplPreConfigedTable_Object = MibTable
rttMonApplPreConfigedTable = _RttMonApplPreConfigedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rttMonApplPreConfigedTable.setStatus("obsolete")
_RttMonApplPreConfigedEntry_Object = MibTableRow
rttMonApplPreConfigedEntry = _RttMonApplPreConfigedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1)
)
rttMonApplPreConfigedEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplPreConfigedType"),
    (0, "CISCO-RTTMON-MIB", "rttMonApplPreConfigedName"),
)
if mibBuilder.loadTexts:
    rttMonApplPreConfigedEntry.setStatus("obsolete")


class _RttMonApplPreConfigedType_Type(Integer32):
    """Custom type rttMonApplPreConfigedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filePath", 1),
          ("scriptName", 2))
    )


_RttMonApplPreConfigedType_Type.__name__ = "Integer32"
_RttMonApplPreConfigedType_Object = MibTableColumn
rttMonApplPreConfigedType = _RttMonApplPreConfigedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 2),
    _RttMonApplPreConfigedType_Type()
)
rttMonApplPreConfigedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedType.setStatus("obsolete")
_RttMonApplPreConfigedName_Type = DisplayString
_RttMonApplPreConfigedName_Object = MibTableColumn
rttMonApplPreConfigedName = _RttMonApplPreConfigedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 3),
    _RttMonApplPreConfigedName_Type()
)
rttMonApplPreConfigedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedName.setStatus("obsolete")
_RttMonApplPreConfigedValid_Type = TruthValue
_RttMonApplPreConfigedValid_Object = MibTableColumn
rttMonApplPreConfigedValid = _RttMonApplPreConfigedValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 4),
    _RttMonApplPreConfigedValid_Type()
)
rttMonApplPreConfigedValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedValid.setStatus("obsolete")


class _RttMonApplProbeCapacity_Type(Integer32):
    """Custom type rttMonApplProbeCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonApplProbeCapacity_Type.__name__ = "Integer32"
_RttMonApplProbeCapacity_Object = MibScalar
rttMonApplProbeCapacity = _RttMonApplProbeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 10),
    _RttMonApplProbeCapacity_Type()
)
rttMonApplProbeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplProbeCapacity.setStatus("current")


class _RttMonApplFreeMemLowWaterMark_Type(Integer32):
    """Custom type rttMonApplFreeMemLowWaterMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonApplFreeMemLowWaterMark_Type.__name__ = "Integer32"
_RttMonApplFreeMemLowWaterMark_Object = MibScalar
rttMonApplFreeMemLowWaterMark = _RttMonApplFreeMemLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 11),
    _RttMonApplFreeMemLowWaterMark_Type()
)
rttMonApplFreeMemLowWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplFreeMemLowWaterMark.setStatus("current")
_RttMonApplLatestSetError_Type = DisplayString
_RttMonApplLatestSetError_Object = MibScalar
rttMonApplLatestSetError = _RttMonApplLatestSetError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 12),
    _RttMonApplLatestSetError_Type()
)
rttMonApplLatestSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplLatestSetError.setStatus("current")
_RttMonApplResponder_Type = TruthValue
_RttMonApplResponder_Object = MibScalar
rttMonApplResponder = _RttMonApplResponder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 13),
    _RttMonApplResponder_Type()
)
rttMonApplResponder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplResponder.setStatus("current")
_RttMonApplAuthTable_Object = MibTable
rttMonApplAuthTable = _RttMonApplAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14)
)
if mibBuilder.loadTexts:
    rttMonApplAuthTable.setStatus("current")
_RttMonApplAuthEntry_Object = MibTableRow
rttMonApplAuthEntry = _RttMonApplAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1)
)
rttMonApplAuthEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplAuthIndex"),
)
if mibBuilder.loadTexts:
    rttMonApplAuthEntry.setStatus("current")


class _RttMonApplAuthIndex_Type(Integer32):
    """Custom type rttMonApplAuthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonApplAuthIndex_Type.__name__ = "Integer32"
_RttMonApplAuthIndex_Object = MibTableColumn
rttMonApplAuthIndex = _RttMonApplAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 1),
    _RttMonApplAuthIndex_Type()
)
rttMonApplAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplAuthIndex.setStatus("current")


class _RttMonApplAuthKeyChain_Type(DisplayString):
    """Custom type rttMonApplAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyChain_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyChain_Object = MibTableColumn
rttMonApplAuthKeyChain = _RttMonApplAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 2),
    _RttMonApplAuthKeyChain_Type()
)
rttMonApplAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyChain.setStatus("current")


class _RttMonApplAuthKeyString1_Type(DisplayString):
    """Custom type rttMonApplAuthKeyString1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyString1_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyString1_Object = MibTableColumn
rttMonApplAuthKeyString1 = _RttMonApplAuthKeyString1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 3),
    _RttMonApplAuthKeyString1_Type()
)
rttMonApplAuthKeyString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyString1.setStatus("current")


class _RttMonApplAuthKeyString2_Type(DisplayString):
    """Custom type rttMonApplAuthKeyString2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyString2_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyString2_Object = MibTableColumn
rttMonApplAuthKeyString2 = _RttMonApplAuthKeyString2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 4),
    _RttMonApplAuthKeyString2_Type()
)
rttMonApplAuthKeyString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyString2.setStatus("current")


class _RttMonApplAuthKeyString3_Type(DisplayString):
    """Custom type rttMonApplAuthKeyString3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyString3_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyString3_Object = MibTableColumn
rttMonApplAuthKeyString3 = _RttMonApplAuthKeyString3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 5),
    _RttMonApplAuthKeyString3_Type()
)
rttMonApplAuthKeyString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyString3.setStatus("current")


class _RttMonApplAuthKeyString4_Type(DisplayString):
    """Custom type rttMonApplAuthKeyString4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyString4_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyString4_Object = MibTableColumn
rttMonApplAuthKeyString4 = _RttMonApplAuthKeyString4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 6),
    _RttMonApplAuthKeyString4_Type()
)
rttMonApplAuthKeyString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyString4.setStatus("current")


class _RttMonApplAuthKeyString5_Type(DisplayString):
    """Custom type rttMonApplAuthKeyString5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RttMonApplAuthKeyString5_Type.__name__ = "DisplayString"
_RttMonApplAuthKeyString5_Object = MibTableColumn
rttMonApplAuthKeyString5 = _RttMonApplAuthKeyString5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 7),
    _RttMonApplAuthKeyString5_Type()
)
rttMonApplAuthKeyString5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthKeyString5.setStatus("current")
_RttMonApplAuthStatus_Type = RowStatus
_RttMonApplAuthStatus_Object = MibTableColumn
rttMonApplAuthStatus = _RttMonApplAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 14, 1, 8),
    _RttMonApplAuthStatus_Type()
)
rttMonApplAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonApplAuthStatus.setStatus("current")


class _RttMonApplLpdGrpStatsReset_Type(Integer32):
    """Custom type rttMonApplLpdGrpStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonApplLpdGrpStatsReset_Type.__name__ = "Integer32"
_RttMonApplLpdGrpStatsReset_Object = MibScalar
rttMonApplLpdGrpStatsReset = _RttMonApplLpdGrpStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 15),
    _RttMonApplLpdGrpStatsReset_Type()
)
rttMonApplLpdGrpStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplLpdGrpStatsReset.setStatus("current")
_RttMonCtrl_ObjectIdentity = ObjectIdentity
rttMonCtrl = _RttMonCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2)
)
_RttMonCtrlAdminTable_Object = MibTable
rttMonCtrlAdminTable = _RttMonCtrlAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rttMonCtrlAdminTable.setStatus("current")
_RttMonCtrlAdminEntry_Object = MibTableRow
rttMonCtrlAdminEntry = _RttMonCtrlAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1)
)
rttMonCtrlAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonCtrlAdminEntry.setStatus("current")


class _RttMonCtrlAdminIndex_Type(Integer32):
    """Custom type rttMonCtrlAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonCtrlAdminIndex_Type.__name__ = "Integer32"
_RttMonCtrlAdminIndex_Object = MibTableColumn
rttMonCtrlAdminIndex = _RttMonCtrlAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 1),
    _RttMonCtrlAdminIndex_Type()
)
rttMonCtrlAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonCtrlAdminIndex.setStatus("current")


class _RttMonCtrlAdminOwner_Type(OctetString):
    """Custom type rttMonCtrlAdminOwner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RttMonCtrlAdminOwner_Type.__name__ = "OctetString"
_RttMonCtrlAdminOwner_Object = MibTableColumn
rttMonCtrlAdminOwner = _RttMonCtrlAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 2),
    _RttMonCtrlAdminOwner_Type()
)
rttMonCtrlAdminOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminOwner.setStatus("current")


class _RttMonCtrlAdminTag_Type(DisplayString):
    """Custom type rttMonCtrlAdminTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RttMonCtrlAdminTag_Type.__name__ = "DisplayString"
_RttMonCtrlAdminTag_Object = MibTableColumn
rttMonCtrlAdminTag = _RttMonCtrlAdminTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 3),
    _RttMonCtrlAdminTag_Type()
)
rttMonCtrlAdminTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTag.setStatus("deprecated")


class _RttMonCtrlAdminRttType_Type(RttMonRttType):
    """Custom type rttMonCtrlAdminRttType based on RttMonRttType"""


_RttMonCtrlAdminRttType_Object = MibTableColumn
rttMonCtrlAdminRttType = _RttMonCtrlAdminRttType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 4),
    _RttMonCtrlAdminRttType_Type()
)
rttMonCtrlAdminRttType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminRttType.setStatus("current")


class _RttMonCtrlAdminThreshold_Type(Integer32):
    """Custom type rttMonCtrlAdminThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlAdminThreshold_Type.__name__ = "Integer32"
_RttMonCtrlAdminThreshold_Object = MibTableColumn
rttMonCtrlAdminThreshold = _RttMonCtrlAdminThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 5),
    _RttMonCtrlAdminThreshold_Type()
)
rttMonCtrlAdminThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminThreshold.setUnits("milliseconds")


class _RttMonCtrlAdminFrequency_Type(Integer32):
    """Custom type rttMonCtrlAdminFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonCtrlAdminFrequency_Type.__name__ = "Integer32"
_RttMonCtrlAdminFrequency_Object = MibTableColumn
rttMonCtrlAdminFrequency = _RttMonCtrlAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 6),
    _RttMonCtrlAdminFrequency_Type()
)
rttMonCtrlAdminFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminFrequency.setUnits("seconds")


class _RttMonCtrlAdminTimeout_Type(Integer32):
    """Custom type rttMonCtrlAdminTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RttMonCtrlAdminTimeout_Type.__name__ = "Integer32"
_RttMonCtrlAdminTimeout_Object = MibTableColumn
rttMonCtrlAdminTimeout = _RttMonCtrlAdminTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 7),
    _RttMonCtrlAdminTimeout_Type()
)
rttMonCtrlAdminTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTimeout.setUnits("milliseconds")


class _RttMonCtrlAdminVerifyData_Type(TruthValue):
    """Custom type rttMonCtrlAdminVerifyData based on TruthValue"""


_RttMonCtrlAdminVerifyData_Object = MibTableColumn
rttMonCtrlAdminVerifyData = _RttMonCtrlAdminVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 8),
    _RttMonCtrlAdminVerifyData_Type()
)
rttMonCtrlAdminVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminVerifyData.setStatus("current")
_RttMonCtrlAdminStatus_Type = RowStatus
_RttMonCtrlAdminStatus_Object = MibTableColumn
rttMonCtrlAdminStatus = _RttMonCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 9),
    _RttMonCtrlAdminStatus_Type()
)
rttMonCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminStatus.setStatus("current")


class _RttMonCtrlAdminNvgen_Type(TruthValue):
    """Custom type rttMonCtrlAdminNvgen based on TruthValue"""


_RttMonCtrlAdminNvgen_Object = MibTableColumn
rttMonCtrlAdminNvgen = _RttMonCtrlAdminNvgen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 10),
    _RttMonCtrlAdminNvgen_Type()
)
rttMonCtrlAdminNvgen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminNvgen.setStatus("current")


class _RttMonCtrlAdminGroupName_Type(SnmpAdminString):
    """Custom type rttMonCtrlAdminGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RttMonCtrlAdminGroupName_Type.__name__ = "SnmpAdminString"
_RttMonCtrlAdminGroupName_Object = MibTableColumn
rttMonCtrlAdminGroupName = _RttMonCtrlAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 11),
    _RttMonCtrlAdminGroupName_Type()
)
rttMonCtrlAdminGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlAdminGroupName.setStatus("current")


class _RttMonCtrlAdminLongTag_Type(SnmpAdminString):
    """Custom type rttMonCtrlAdminLongTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RttMonCtrlAdminLongTag_Type.__name__ = "SnmpAdminString"
_RttMonCtrlAdminLongTag_Object = MibTableColumn
rttMonCtrlAdminLongTag = _RttMonCtrlAdminLongTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 12),
    _RttMonCtrlAdminLongTag_Type()
)
rttMonCtrlAdminLongTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminLongTag.setStatus("current")
_RttMonEchoAdminTable_Object = MibTable
rttMonEchoAdminTable = _RttMonEchoAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rttMonEchoAdminTable.setStatus("current")
_RttMonEchoAdminEntry_Object = MibTableRow
rttMonEchoAdminEntry = _RttMonEchoAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1)
)
rttMonEchoAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonEchoAdminEntry.setStatus("current")


class _RttMonEchoAdminProtocol_Type(RttMonProtocol):
    """Custom type rttMonEchoAdminProtocol based on RttMonProtocol"""


_RttMonEchoAdminProtocol_Object = MibTableColumn
rttMonEchoAdminProtocol = _RttMonEchoAdminProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 1),
    _RttMonEchoAdminProtocol_Type()
)
rttMonEchoAdminProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProtocol.setStatus("current")
_RttMonEchoAdminTargetAddress_Type = RttMonTargetAddress
_RttMonEchoAdminTargetAddress_Object = MibTableColumn
rttMonEchoAdminTargetAddress = _RttMonEchoAdminTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 2),
    _RttMonEchoAdminTargetAddress_Type()
)
rttMonEchoAdminTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetAddress.setStatus("current")


class _RttMonEchoAdminPktDataRequestSize_Type(Integer32):
    """Custom type rttMonEchoAdminPktDataRequestSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonEchoAdminPktDataRequestSize_Type.__name__ = "Integer32"
_RttMonEchoAdminPktDataRequestSize_Object = MibTableColumn
rttMonEchoAdminPktDataRequestSize = _RttMonEchoAdminPktDataRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 3),
    _RttMonEchoAdminPktDataRequestSize_Type()
)
rttMonEchoAdminPktDataRequestSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataRequestSize.setUnits("octets")


class _RttMonEchoAdminPktDataResponseSize_Type(Integer32):
    """Custom type rttMonEchoAdminPktDataResponseSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonEchoAdminPktDataResponseSize_Type.__name__ = "Integer32"
_RttMonEchoAdminPktDataResponseSize_Object = MibTableColumn
rttMonEchoAdminPktDataResponseSize = _RttMonEchoAdminPktDataResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 4),
    _RttMonEchoAdminPktDataResponseSize_Type()
)
rttMonEchoAdminPktDataResponseSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataResponseSize.setStatus("current")


class _RttMonEchoAdminTargetPort_Type(Integer32):
    """Custom type rttMonEchoAdminTargetPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminTargetPort_Type.__name__ = "Integer32"
_RttMonEchoAdminTargetPort_Object = MibTableColumn
rttMonEchoAdminTargetPort = _RttMonEchoAdminTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 5),
    _RttMonEchoAdminTargetPort_Type()
)
rttMonEchoAdminTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetPort.setStatus("current")
_RttMonEchoAdminSourceAddress_Type = RttMonTargetAddress
_RttMonEchoAdminSourceAddress_Object = MibTableColumn
rttMonEchoAdminSourceAddress = _RttMonEchoAdminSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 6),
    _RttMonEchoAdminSourceAddress_Type()
)
rttMonEchoAdminSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourceAddress.setStatus("current")


class _RttMonEchoAdminSourcePort_Type(Integer32):
    """Custom type rttMonEchoAdminSourcePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminSourcePort_Type.__name__ = "Integer32"
_RttMonEchoAdminSourcePort_Object = MibTableColumn
rttMonEchoAdminSourcePort = _RttMonEchoAdminSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 7),
    _RttMonEchoAdminSourcePort_Type()
)
rttMonEchoAdminSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourcePort.setStatus("current")


class _RttMonEchoAdminControlEnable_Type(TruthValue):
    """Custom type rttMonEchoAdminControlEnable based on TruthValue"""


_RttMonEchoAdminControlEnable_Object = MibTableColumn
rttMonEchoAdminControlEnable = _RttMonEchoAdminControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 8),
    _RttMonEchoAdminControlEnable_Type()
)
rttMonEchoAdminControlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminControlEnable.setStatus("current")


class _RttMonEchoAdminTOS_Type(Integer32):
    """Custom type rttMonEchoAdminTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RttMonEchoAdminTOS_Type.__name__ = "Integer32"
_RttMonEchoAdminTOS_Object = MibTableColumn
rttMonEchoAdminTOS = _RttMonEchoAdminTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 9),
    _RttMonEchoAdminTOS_Type()
)
rttMonEchoAdminTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTOS.setStatus("current")


class _RttMonEchoAdminLSREnable_Type(TruthValue):
    """Custom type rttMonEchoAdminLSREnable based on TruthValue"""


_RttMonEchoAdminLSREnable_Object = MibTableColumn
rttMonEchoAdminLSREnable = _RttMonEchoAdminLSREnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 10),
    _RttMonEchoAdminLSREnable_Type()
)
rttMonEchoAdminLSREnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSREnable.setStatus("current")
_RttMonEchoAdminTargetAddressString_Type = DisplayString
_RttMonEchoAdminTargetAddressString_Object = MibTableColumn
rttMonEchoAdminTargetAddressString = _RttMonEchoAdminTargetAddressString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 11),
    _RttMonEchoAdminTargetAddressString_Type()
)
rttMonEchoAdminTargetAddressString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetAddressString.setStatus("current")
_RttMonEchoAdminNameServer_Type = RttMonTargetAddress
_RttMonEchoAdminNameServer_Object = MibTableColumn
rttMonEchoAdminNameServer = _RttMonEchoAdminNameServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 12),
    _RttMonEchoAdminNameServer_Type()
)
rttMonEchoAdminNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminNameServer.setStatus("current")
_RttMonEchoAdminOperation_Type = RttMonOperation
_RttMonEchoAdminOperation_Object = MibTableColumn
rttMonEchoAdminOperation = _RttMonEchoAdminOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 13),
    _RttMonEchoAdminOperation_Type()
)
rttMonEchoAdminOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOperation.setStatus("current")


class _RttMonEchoAdminHTTPVersion_Type(DisplayString):
    """Custom type rttMonEchoAdminHTTPVersion based on DisplayString"""
    defaultValue = OctetString("1.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_RttMonEchoAdminHTTPVersion_Type.__name__ = "DisplayString"
_RttMonEchoAdminHTTPVersion_Object = MibTableColumn
rttMonEchoAdminHTTPVersion = _RttMonEchoAdminHTTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 14),
    _RttMonEchoAdminHTTPVersion_Type()
)
rttMonEchoAdminHTTPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminHTTPVersion.setStatus("current")
_RttMonEchoAdminURL_Type = DisplayString
_RttMonEchoAdminURL_Object = MibTableColumn
rttMonEchoAdminURL = _RttMonEchoAdminURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 15),
    _RttMonEchoAdminURL_Type()
)
rttMonEchoAdminURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminURL.setStatus("current")


class _RttMonEchoAdminCache_Type(TruthValue):
    """Custom type rttMonEchoAdminCache based on TruthValue"""


_RttMonEchoAdminCache_Object = MibTableColumn
rttMonEchoAdminCache = _RttMonEchoAdminCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 16),
    _RttMonEchoAdminCache_Type()
)
rttMonEchoAdminCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCache.setStatus("current")


class _RttMonEchoAdminInterval_Type(Integer32):
    """Custom type rttMonEchoAdminInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_RttMonEchoAdminInterval_Type.__name__ = "Integer32"
_RttMonEchoAdminInterval_Object = MibTableColumn
rttMonEchoAdminInterval = _RttMonEchoAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 17),
    _RttMonEchoAdminInterval_Type()
)
rttMonEchoAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminInterval.setUnits("milliseconds")


class _RttMonEchoAdminNumPackets_Type(Integer32):
    """Custom type rttMonEchoAdminNumPackets based on Integer32"""
    defaultValue = 10


_RttMonEchoAdminNumPackets_Object = MibTableColumn
rttMonEchoAdminNumPackets = _RttMonEchoAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 18),
    _RttMonEchoAdminNumPackets_Type()
)
rttMonEchoAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminNumPackets.setStatus("current")
_RttMonEchoAdminProxy_Type = DisplayString
_RttMonEchoAdminProxy_Object = MibTableColumn
rttMonEchoAdminProxy = _RttMonEchoAdminProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 19),
    _RttMonEchoAdminProxy_Type()
)
rttMonEchoAdminProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProxy.setStatus("current")
_RttMonEchoAdminString1_Type = DisplayString
_RttMonEchoAdminString1_Object = MibTableColumn
rttMonEchoAdminString1 = _RttMonEchoAdminString1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 20),
    _RttMonEchoAdminString1_Type()
)
rttMonEchoAdminString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString1.setStatus("current")
_RttMonEchoAdminString2_Type = DisplayString
_RttMonEchoAdminString2_Object = MibTableColumn
rttMonEchoAdminString2 = _RttMonEchoAdminString2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 21),
    _RttMonEchoAdminString2_Type()
)
rttMonEchoAdminString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString2.setStatus("current")
_RttMonEchoAdminString3_Type = DisplayString
_RttMonEchoAdminString3_Object = MibTableColumn
rttMonEchoAdminString3 = _RttMonEchoAdminString3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 22),
    _RttMonEchoAdminString3_Type()
)
rttMonEchoAdminString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString3.setStatus("current")
_RttMonEchoAdminString4_Type = DisplayString
_RttMonEchoAdminString4_Object = MibTableColumn
rttMonEchoAdminString4 = _RttMonEchoAdminString4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 23),
    _RttMonEchoAdminString4_Type()
)
rttMonEchoAdminString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString4.setStatus("current")
_RttMonEchoAdminString5_Type = DisplayString
_RttMonEchoAdminString5_Object = MibTableColumn
rttMonEchoAdminString5 = _RttMonEchoAdminString5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 24),
    _RttMonEchoAdminString5_Type()
)
rttMonEchoAdminString5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString5.setStatus("current")


class _RttMonEchoAdminMode_Type(RttMonOperation):
    """Custom type rttMonEchoAdminMode based on RttMonOperation"""


_RttMonEchoAdminMode_Object = MibTableColumn
rttMonEchoAdminMode = _RttMonEchoAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 25),
    _RttMonEchoAdminMode_Type()
)
rttMonEchoAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminMode.setStatus("current")


class _RttMonEchoAdminVrfName_Type(OctetString):
    """Custom type rttMonEchoAdminVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RttMonEchoAdminVrfName_Type.__name__ = "OctetString"
_RttMonEchoAdminVrfName_Object = MibTableColumn
rttMonEchoAdminVrfName = _RttMonEchoAdminVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 26),
    _RttMonEchoAdminVrfName_Type()
)
rttMonEchoAdminVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminVrfName.setStatus("current")
_RttMonEchoAdminCodecType_Type = RttMonCodecType
_RttMonEchoAdminCodecType_Object = MibTableColumn
rttMonEchoAdminCodecType = _RttMonEchoAdminCodecType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 27),
    _RttMonEchoAdminCodecType_Type()
)
rttMonEchoAdminCodecType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecType.setStatus("current")


class _RttMonEchoAdminCodecInterval_Type(Integer32):
    """Custom type rttMonEchoAdminCodecInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_RttMonEchoAdminCodecInterval_Type.__name__ = "Integer32"
_RttMonEchoAdminCodecInterval_Object = MibTableColumn
rttMonEchoAdminCodecInterval = _RttMonEchoAdminCodecInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 28),
    _RttMonEchoAdminCodecInterval_Type()
)
rttMonEchoAdminCodecInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecInterval.setUnits("milliseconds")


class _RttMonEchoAdminCodecPayload_Type(Integer32):
    """Custom type rttMonEchoAdminCodecPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonEchoAdminCodecPayload_Type.__name__ = "Integer32"
_RttMonEchoAdminCodecPayload_Object = MibTableColumn
rttMonEchoAdminCodecPayload = _RttMonEchoAdminCodecPayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 29),
    _RttMonEchoAdminCodecPayload_Type()
)
rttMonEchoAdminCodecPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecPayload.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecPayload.setUnits("octets")


class _RttMonEchoAdminCodecNumPackets_Type(Integer32):
    """Custom type rttMonEchoAdminCodecNumPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_RttMonEchoAdminCodecNumPackets_Type.__name__ = "Integer32"
_RttMonEchoAdminCodecNumPackets_Object = MibTableColumn
rttMonEchoAdminCodecNumPackets = _RttMonEchoAdminCodecNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 30),
    _RttMonEchoAdminCodecNumPackets_Type()
)
rttMonEchoAdminCodecNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCodecNumPackets.setStatus("current")


class _RttMonEchoAdminICPIFAdvFactor_Type(Integer32):
    """Custom type rttMonEchoAdminICPIFAdvFactor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_RttMonEchoAdminICPIFAdvFactor_Type.__name__ = "Integer32"
_RttMonEchoAdminICPIFAdvFactor_Object = MibTableColumn
rttMonEchoAdminICPIFAdvFactor = _RttMonEchoAdminICPIFAdvFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 31),
    _RttMonEchoAdminICPIFAdvFactor_Type()
)
rttMonEchoAdminICPIFAdvFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminICPIFAdvFactor.setStatus("current")


class _RttMonEchoAdminLSPFECType_Type(Integer32):
    """Custom type rttMonEchoAdminLSPFECType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ldpIpv4Prefix", 1)
    )


_RttMonEchoAdminLSPFECType_Type.__name__ = "Integer32"
_RttMonEchoAdminLSPFECType_Object = MibTableColumn
rttMonEchoAdminLSPFECType = _RttMonEchoAdminLSPFECType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 32),
    _RttMonEchoAdminLSPFECType_Type()
)
rttMonEchoAdminLSPFECType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPFECType.setStatus("current")


class _RttMonEchoAdminLSPSelector_Type(RttMonTargetAddress):
    """Custom type rttMonEchoAdminLSPSelector based on RttMonTargetAddress"""
    defaultValue = OctetString("7F 00 00 01")


_RttMonEchoAdminLSPSelector_Object = MibTableColumn
rttMonEchoAdminLSPSelector = _RttMonEchoAdminLSPSelector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 33),
    _RttMonEchoAdminLSPSelector_Type()
)
rttMonEchoAdminLSPSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPSelector.setStatus("current")


class _RttMonEchoAdminLSPReplyMode_Type(RttMonLSPPingReplyMode):
    """Custom type rttMonEchoAdminLSPReplyMode based on RttMonLSPPingReplyMode"""


_RttMonEchoAdminLSPReplyMode_Object = MibTableColumn
rttMonEchoAdminLSPReplyMode = _RttMonEchoAdminLSPReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 34),
    _RttMonEchoAdminLSPReplyMode_Type()
)
rttMonEchoAdminLSPReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPReplyMode.setStatus("current")


class _RttMonEchoAdminLSPTTL_Type(Integer32):
    """Custom type rttMonEchoAdminLSPTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RttMonEchoAdminLSPTTL_Type.__name__ = "Integer32"
_RttMonEchoAdminLSPTTL_Object = MibTableColumn
rttMonEchoAdminLSPTTL = _RttMonEchoAdminLSPTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 35),
    _RttMonEchoAdminLSPTTL_Type()
)
rttMonEchoAdminLSPTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPTTL.setStatus("current")


class _RttMonEchoAdminLSPExp_Type(Integer32):
    """Custom type rttMonEchoAdminLSPExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RttMonEchoAdminLSPExp_Type.__name__ = "Integer32"
_RttMonEchoAdminLSPExp_Object = MibTableColumn
rttMonEchoAdminLSPExp = _RttMonEchoAdminLSPExp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 36),
    _RttMonEchoAdminLSPExp_Type()
)
rttMonEchoAdminLSPExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPExp.setStatus("current")


class _RttMonEchoAdminPrecision_Type(Integer32):
    """Custom type rttMonEchoAdminPrecision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("microseconds", 2),
          ("milliseconds", 1))
    )


_RttMonEchoAdminPrecision_Type.__name__ = "Integer32"
_RttMonEchoAdminPrecision_Object = MibTableColumn
rttMonEchoAdminPrecision = _RttMonEchoAdminPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 37),
    _RttMonEchoAdminPrecision_Type()
)
rttMonEchoAdminPrecision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminPrecision.setStatus("current")


class _RttMonEchoAdminProbePakPriority_Type(Integer32):
    """Custom type rttMonEchoAdminProbePakPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_RttMonEchoAdminProbePakPriority_Type.__name__ = "Integer32"
_RttMonEchoAdminProbePakPriority_Object = MibTableColumn
rttMonEchoAdminProbePakPriority = _RttMonEchoAdminProbePakPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 38),
    _RttMonEchoAdminProbePakPriority_Type()
)
rttMonEchoAdminProbePakPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProbePakPriority.setStatus("current")


class _RttMonEchoAdminOWNTPSyncTolAbs_Type(Integer32):
    """Custom type rttMonEchoAdminOWNTPSyncTolAbs based on Integer32"""
    defaultValue = 0


_RttMonEchoAdminOWNTPSyncTolAbs_Object = MibTableColumn
rttMonEchoAdminOWNTPSyncTolAbs = _RttMonEchoAdminOWNTPSyncTolAbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 39),
    _RttMonEchoAdminOWNTPSyncTolAbs_Type()
)
rttMonEchoAdminOWNTPSyncTolAbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOWNTPSyncTolAbs.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminOWNTPSyncTolAbs.setUnits("microseconds")


class _RttMonEchoAdminOWNTPSyncTolPct_Type(Integer32):
    """Custom type rttMonEchoAdminOWNTPSyncTolPct based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RttMonEchoAdminOWNTPSyncTolPct_Type.__name__ = "Integer32"
_RttMonEchoAdminOWNTPSyncTolPct_Object = MibTableColumn
rttMonEchoAdminOWNTPSyncTolPct = _RttMonEchoAdminOWNTPSyncTolPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 40),
    _RttMonEchoAdminOWNTPSyncTolPct_Type()
)
rttMonEchoAdminOWNTPSyncTolPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOWNTPSyncTolPct.setStatus("current")


class _RttMonEchoAdminOWNTPSyncTolType_Type(Integer32):
    """Custom type rttMonEchoAdminOWNTPSyncTolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("percent", 1))
    )


_RttMonEchoAdminOWNTPSyncTolType_Type.__name__ = "Integer32"
_RttMonEchoAdminOWNTPSyncTolType_Object = MibTableColumn
rttMonEchoAdminOWNTPSyncTolType = _RttMonEchoAdminOWNTPSyncTolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 41),
    _RttMonEchoAdminOWNTPSyncTolType_Type()
)
rttMonEchoAdminOWNTPSyncTolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOWNTPSyncTolType.setStatus("current")


class _RttMonEchoAdminCalledNumber_Type(SnmpAdminString):
    """Custom type rttMonEchoAdminCalledNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_RttMonEchoAdminCalledNumber_Type.__name__ = "SnmpAdminString"
_RttMonEchoAdminCalledNumber_Object = MibTableColumn
rttMonEchoAdminCalledNumber = _RttMonEchoAdminCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 42),
    _RttMonEchoAdminCalledNumber_Type()
)
rttMonEchoAdminCalledNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCalledNumber.setStatus("current")


class _RttMonEchoAdminDetectPoint_Type(RttMonOperation):
    """Custom type rttMonEchoAdminDetectPoint based on RttMonOperation"""


_RttMonEchoAdminDetectPoint_Object = MibTableColumn
rttMonEchoAdminDetectPoint = _RttMonEchoAdminDetectPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 43),
    _RttMonEchoAdminDetectPoint_Type()
)
rttMonEchoAdminDetectPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminDetectPoint.setStatus("current")


class _RttMonEchoAdminGKRegistration_Type(TruthValue):
    """Custom type rttMonEchoAdminGKRegistration based on TruthValue"""


_RttMonEchoAdminGKRegistration_Object = MibTableColumn
rttMonEchoAdminGKRegistration = _RttMonEchoAdminGKRegistration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 44),
    _RttMonEchoAdminGKRegistration_Type()
)
rttMonEchoAdminGKRegistration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminGKRegistration.setStatus("current")
_RttMonEchoAdminSourceVoicePort_Type = DisplayString
_RttMonEchoAdminSourceVoicePort_Object = MibTableColumn
rttMonEchoAdminSourceVoicePort = _RttMonEchoAdminSourceVoicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 45),
    _RttMonEchoAdminSourceVoicePort_Type()
)
rttMonEchoAdminSourceVoicePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourceVoicePort.setStatus("current")


class _RttMonEchoAdminCallDuration_Type(Integer32):
    """Custom type rttMonEchoAdminCallDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RttMonEchoAdminCallDuration_Type.__name__ = "Integer32"
_RttMonEchoAdminCallDuration_Object = MibTableColumn
rttMonEchoAdminCallDuration = _RttMonEchoAdminCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 46),
    _RttMonEchoAdminCallDuration_Type()
)
rttMonEchoAdminCallDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCallDuration.setStatus("current")


class _RttMonEchoAdminLSPReplyDscp_Type(Integer32):
    """Custom type rttMonEchoAdminLSPReplyDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_RttMonEchoAdminLSPReplyDscp_Type.__name__ = "Integer32"
_RttMonEchoAdminLSPReplyDscp_Object = MibTableColumn
rttMonEchoAdminLSPReplyDscp = _RttMonEchoAdminLSPReplyDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 47),
    _RttMonEchoAdminLSPReplyDscp_Type()
)
rttMonEchoAdminLSPReplyDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPReplyDscp.setStatus("current")


class _RttMonEchoAdminLSPNullShim_Type(TruthValue):
    """Custom type rttMonEchoAdminLSPNullShim based on TruthValue"""


_RttMonEchoAdminLSPNullShim_Object = MibTableColumn
rttMonEchoAdminLSPNullShim = _RttMonEchoAdminLSPNullShim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 48),
    _RttMonEchoAdminLSPNullShim_Type()
)
rttMonEchoAdminLSPNullShim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPNullShim.setStatus("current")
_RttMonEchoAdminTargetMPID_Type = CfmMepid
_RttMonEchoAdminTargetMPID_Object = MibTableColumn
rttMonEchoAdminTargetMPID = _RttMonEchoAdminTargetMPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 49),
    _RttMonEchoAdminTargetMPID_Type()
)
rttMonEchoAdminTargetMPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetMPID.setStatus("current")
_RttMonEchoAdminTargetDomainName_Type = SnmpAdminString
_RttMonEchoAdminTargetDomainName_Object = MibTableColumn
rttMonEchoAdminTargetDomainName = _RttMonEchoAdminTargetDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 50),
    _RttMonEchoAdminTargetDomainName_Type()
)
rttMonEchoAdminTargetDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetDomainName.setStatus("current")
_RttMonEchoAdminTargetVLAN_Type = VlanId
_RttMonEchoAdminTargetVLAN_Object = MibTableColumn
rttMonEchoAdminTargetVLAN = _RttMonEchoAdminTargetVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 51),
    _RttMonEchoAdminTargetVLAN_Type()
)
rttMonEchoAdminTargetVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetVLAN.setStatus("current")


class _RttMonEchoAdminEthernetCOS_Type(QosLayer2Cos):
    """Custom type rttMonEchoAdminEthernetCOS based on QosLayer2Cos"""
    defaultValue = 0

    subtypeSpec = QosLayer2Cos.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RttMonEchoAdminEthernetCOS_Type.__name__ = "QosLayer2Cos"
_RttMonEchoAdminEthernetCOS_Object = MibTableColumn
rttMonEchoAdminEthernetCOS = _RttMonEchoAdminEthernetCOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 52),
    _RttMonEchoAdminEthernetCOS_Type()
)
rttMonEchoAdminEthernetCOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEthernetCOS.setStatus("current")


class _RttMonEchoAdminLSPVccvID_Type(Integer32):
    """Custom type rttMonEchoAdminLSPVccvID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonEchoAdminLSPVccvID_Type.__name__ = "Integer32"
_RttMonEchoAdminLSPVccvID_Object = MibTableColumn
rttMonEchoAdminLSPVccvID = _RttMonEchoAdminLSPVccvID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 53),
    _RttMonEchoAdminLSPVccvID_Type()
)
rttMonEchoAdminLSPVccvID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSPVccvID.setStatus("current")


class _RttMonEchoAdminTargetEVC_Type(SnmpAdminString):
    """Custom type rttMonEchoAdminTargetEVC based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RttMonEchoAdminTargetEVC_Type.__name__ = "SnmpAdminString"
_RttMonEchoAdminTargetEVC_Object = MibTableColumn
rttMonEchoAdminTargetEVC = _RttMonEchoAdminTargetEVC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 54),
    _RttMonEchoAdminTargetEVC_Type()
)
rttMonEchoAdminTargetEVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetEVC.setStatus("current")


class _RttMonEchoAdminTargetMEPPort_Type(TruthValue):
    """Custom type rttMonEchoAdminTargetMEPPort based on TruthValue"""


_RttMonEchoAdminTargetMEPPort_Object = MibTableColumn
rttMonEchoAdminTargetMEPPort = _RttMonEchoAdminTargetMEPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 55),
    _RttMonEchoAdminTargetMEPPort_Type()
)
rttMonEchoAdminTargetMEPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetMEPPort.setStatus("current")


class _RttMonEchoAdminVideoTrafficProfile_Type(SnmpAdminString):
    """Custom type rttMonEchoAdminVideoTrafficProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RttMonEchoAdminVideoTrafficProfile_Type.__name__ = "SnmpAdminString"
_RttMonEchoAdminVideoTrafficProfile_Object = MibTableColumn
rttMonEchoAdminVideoTrafficProfile = _RttMonEchoAdminVideoTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 56),
    _RttMonEchoAdminVideoTrafficProfile_Type()
)
rttMonEchoAdminVideoTrafficProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminVideoTrafficProfile.setStatus("current")


class _RttMonEchoAdminDscp_Type(Dscp):
    """Custom type rttMonEchoAdminDscp based on Dscp"""
    defaultValue = 0


_RttMonEchoAdminDscp_Object = MibTableColumn
rttMonEchoAdminDscp = _RttMonEchoAdminDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 57),
    _RttMonEchoAdminDscp_Type()
)
rttMonEchoAdminDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminDscp.setStatus("current")


class _RttMonEchoAdminReserveDsp_Type(Integer32):
    """Custom type rttMonEchoAdminReserveDsp based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("be", 1),
          ("gs", 2),
          ("na", 3))
    )


_RttMonEchoAdminReserveDsp_Type.__name__ = "Integer32"
_RttMonEchoAdminReserveDsp_Object = MibTableColumn
rttMonEchoAdminReserveDsp = _RttMonEchoAdminReserveDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 58),
    _RttMonEchoAdminReserveDsp_Type()
)
rttMonEchoAdminReserveDsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminReserveDsp.setStatus("current")
_RttMonEchoAdminInputInterface_Type = InterfaceIndexOrZero
_RttMonEchoAdminInputInterface_Object = MibTableColumn
rttMonEchoAdminInputInterface = _RttMonEchoAdminInputInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 59),
    _RttMonEchoAdminInputInterface_Type()
)
rttMonEchoAdminInputInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminInputInterface.setStatus("current")
_RttMonEchoAdminEmulateSourceAddress_Type = RttMonTargetAddress
_RttMonEchoAdminEmulateSourceAddress_Object = MibTableColumn
rttMonEchoAdminEmulateSourceAddress = _RttMonEchoAdminEmulateSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 60),
    _RttMonEchoAdminEmulateSourceAddress_Type()
)
rttMonEchoAdminEmulateSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEmulateSourceAddress.setStatus("current")


class _RttMonEchoAdminEmulateSourcePort_Type(Integer32):
    """Custom type rttMonEchoAdminEmulateSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminEmulateSourcePort_Type.__name__ = "Integer32"
_RttMonEchoAdminEmulateSourcePort_Object = MibTableColumn
rttMonEchoAdminEmulateSourcePort = _RttMonEchoAdminEmulateSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 61),
    _RttMonEchoAdminEmulateSourcePort_Type()
)
rttMonEchoAdminEmulateSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEmulateSourcePort.setStatus("current")
_RttMonEchoAdminEmulateTargetAddress_Type = RttMonTargetAddress
_RttMonEchoAdminEmulateTargetAddress_Object = MibTableColumn
rttMonEchoAdminEmulateTargetAddress = _RttMonEchoAdminEmulateTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 62),
    _RttMonEchoAdminEmulateTargetAddress_Type()
)
rttMonEchoAdminEmulateTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEmulateTargetAddress.setStatus("current")


class _RttMonEchoAdminEmulateTargetPort_Type(Integer32):
    """Custom type rttMonEchoAdminEmulateTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminEmulateTargetPort_Type.__name__ = "Integer32"
_RttMonEchoAdminEmulateTargetPort_Object = MibTableColumn
rttMonEchoAdminEmulateTargetPort = _RttMonEchoAdminEmulateTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 63),
    _RttMonEchoAdminEmulateTargetPort_Type()
)
rttMonEchoAdminEmulateTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEmulateTargetPort.setStatus("current")
_RttMonEchoAdminTargetMacAddress_Type = MacAddress
_RttMonEchoAdminTargetMacAddress_Object = MibTableColumn
rttMonEchoAdminTargetMacAddress = _RttMonEchoAdminTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 64),
    _RttMonEchoAdminTargetMacAddress_Type()
)
rttMonEchoAdminTargetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetMacAddress.setStatus("current")
_RttMonEchoAdminSourceMacAddress_Type = MacAddress
_RttMonEchoAdminSourceMacAddress_Object = MibTableColumn
rttMonEchoAdminSourceMacAddress = _RttMonEchoAdminSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 65),
    _RttMonEchoAdminSourceMacAddress_Type()
)
rttMonEchoAdminSourceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourceMacAddress.setStatus("current")
_RttMonEchoAdminSourceMPID_Type = CfmMepid
_RttMonEchoAdminSourceMPID_Object = MibTableColumn
rttMonEchoAdminSourceMPID = _RttMonEchoAdminSourceMPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 66),
    _RttMonEchoAdminSourceMPID_Type()
)
rttMonEchoAdminSourceMPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourceMPID.setStatus("current")


class _RttMonEchoAdminEndPointListName_Type(SnmpAdminString):
    """Custom type rttMonEchoAdminEndPointListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RttMonEchoAdminEndPointListName_Type.__name__ = "SnmpAdminString"
_RttMonEchoAdminEndPointListName_Object = MibTableColumn
rttMonEchoAdminEndPointListName = _RttMonEchoAdminEndPointListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 67),
    _RttMonEchoAdminEndPointListName_Type()
)
rttMonEchoAdminEndPointListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminEndPointListName.setStatus("current")


class _RttMonEchoAdminSSM_Type(TruthValue):
    """Custom type rttMonEchoAdminSSM based on TruthValue"""


_RttMonEchoAdminSSM_Object = MibTableColumn
rttMonEchoAdminSSM = _RttMonEchoAdminSSM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 68),
    _RttMonEchoAdminSSM_Type()
)
rttMonEchoAdminSSM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSSM.setStatus("current")


class _RttMonEchoAdminControlRetry_Type(Unsigned32):
    """Custom type rttMonEchoAdminControlRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RttMonEchoAdminControlRetry_Type.__name__ = "Unsigned32"
_RttMonEchoAdminControlRetry_Object = MibTableColumn
rttMonEchoAdminControlRetry = _RttMonEchoAdminControlRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 69),
    _RttMonEchoAdminControlRetry_Type()
)
rttMonEchoAdminControlRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminControlRetry.setStatus("current")


class _RttMonEchoAdminControlTimeout_Type(Unsigned32):
    """Custom type rttMonEchoAdminControlTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RttMonEchoAdminControlTimeout_Type.__name__ = "Unsigned32"
_RttMonEchoAdminControlTimeout_Object = MibTableColumn
rttMonEchoAdminControlTimeout = _RttMonEchoAdminControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 70),
    _RttMonEchoAdminControlTimeout_Type()
)
rttMonEchoAdminControlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminControlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminControlTimeout.setUnits("milliseconds")


class _RttMonEchoAdminIgmpTreeInit_Type(Unsigned32):
    """Custom type rttMonEchoAdminIgmpTreeInit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_RttMonEchoAdminIgmpTreeInit_Type.__name__ = "Unsigned32"
_RttMonEchoAdminIgmpTreeInit_Object = MibTableColumn
rttMonEchoAdminIgmpTreeInit = _RttMonEchoAdminIgmpTreeInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 71),
    _RttMonEchoAdminIgmpTreeInit_Type()
)
rttMonEchoAdminIgmpTreeInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminIgmpTreeInit.setStatus("current")


class _RttMonEchoAdminEnableBurst_Type(TruthValue):
    """Custom type rttMonEchoAdminEnableBurst based on TruthValue"""


_RttMonEchoAdminEnableBurst_Object = MibTableColumn
rttMonEchoAdminEnableBurst = _RttMonEchoAdminEnableBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 72),
    _RttMonEchoAdminEnableBurst_Type()
)
rttMonEchoAdminEnableBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminEnableBurst.setStatus("current")


class _RttMonEchoAdminAggBurstCycles_Type(Integer32):
    """Custom type rttMonEchoAdminAggBurstCycles based on Integer32"""
    defaultValue = 0


_RttMonEchoAdminAggBurstCycles_Object = MibTableColumn
rttMonEchoAdminAggBurstCycles = _RttMonEchoAdminAggBurstCycles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 73),
    _RttMonEchoAdminAggBurstCycles_Type()
)
rttMonEchoAdminAggBurstCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminAggBurstCycles.setStatus("current")


class _RttMonEchoAdminLossRatioNumFrames_Type(Integer32):
    """Custom type rttMonEchoAdminLossRatioNumFrames based on Integer32"""
    defaultValue = 10


_RttMonEchoAdminLossRatioNumFrames_Object = MibTableColumn
rttMonEchoAdminLossRatioNumFrames = _RttMonEchoAdminLossRatioNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 74),
    _RttMonEchoAdminLossRatioNumFrames_Type()
)
rttMonEchoAdminLossRatioNumFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminLossRatioNumFrames.setStatus("current")


class _RttMonEchoAdminAvailNumFrames_Type(Integer32):
    """Custom type rttMonEchoAdminAvailNumFrames based on Integer32"""
    defaultValue = 10


_RttMonEchoAdminAvailNumFrames_Object = MibTableColumn
rttMonEchoAdminAvailNumFrames = _RttMonEchoAdminAvailNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 75),
    _RttMonEchoAdminAvailNumFrames_Type()
)
rttMonEchoAdminAvailNumFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminAvailNumFrames.setStatus("current")


class _RttMonEchoAdminTstampOptimization_Type(TruthValue):
    """Custom type rttMonEchoAdminTstampOptimization based on TruthValue"""


_RttMonEchoAdminTstampOptimization_Object = MibTableColumn
rttMonEchoAdminTstampOptimization = _RttMonEchoAdminTstampOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 76),
    _RttMonEchoAdminTstampOptimization_Type()
)
rttMonEchoAdminTstampOptimization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTstampOptimization.setStatus("current")


class _RttMonEchoAdminTargetSwitchId_Type(Unsigned32):
    """Custom type rttMonEchoAdminTargetSwitchId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_RttMonEchoAdminTargetSwitchId_Type.__name__ = "Unsigned32"
_RttMonEchoAdminTargetSwitchId_Object = MibTableColumn
rttMonEchoAdminTargetSwitchId = _RttMonEchoAdminTargetSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 77),
    _RttMonEchoAdminTargetSwitchId_Type()
)
rttMonEchoAdminTargetSwitchId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetSwitchId.setStatus("current")


class _RttMonEchoAdminProfileId_Type(Unsigned32):
    """Custom type rttMonEchoAdminProfileId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1023),
    )


_RttMonEchoAdminProfileId_Type.__name__ = "Unsigned32"
_RttMonEchoAdminProfileId_Object = MibTableColumn
rttMonEchoAdminProfileId = _RttMonEchoAdminProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 78),
    _RttMonEchoAdminProfileId_Type()
)
rttMonEchoAdminProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProfileId.setStatus("current")


class _RttMonEchoAdminOutputInterface_Type(InterfaceIndexOrZero):
    """Custom type rttMonEchoAdminOutputInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_RttMonEchoAdminOutputInterface_Object = MibTableColumn
rttMonEchoAdminOutputInterface = _RttMonEchoAdminOutputInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 79),
    _RttMonEchoAdminOutputInterface_Type()
)
rttMonEchoAdminOutputInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOutputInterface.setStatus("current")
_RttMonFileIOAdminTable_Object = MibTable
rttMonFileIOAdminTable = _RttMonFileIOAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rttMonFileIOAdminTable.setStatus("obsolete")
_RttMonFileIOAdminEntry_Object = MibTableRow
rttMonFileIOAdminEntry = _RttMonFileIOAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1)
)
rttMonFileIOAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonFileIOAdminEntry.setStatus("obsolete")
_RttMonFileIOAdminFilePath_Type = DisplayString
_RttMonFileIOAdminFilePath_Object = MibTableColumn
rttMonFileIOAdminFilePath = _RttMonFileIOAdminFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 1),
    _RttMonFileIOAdminFilePath_Type()
)
rttMonFileIOAdminFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminFilePath.setStatus("obsolete")


class _RttMonFileIOAdminSize_Type(Integer32):
    """Custom type rttMonFileIOAdminSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("n128k", 4),
          ("n1k", 2),
          ("n256", 1),
          ("n256k", 5),
          ("n64k", 3))
    )


_RttMonFileIOAdminSize_Type.__name__ = "Integer32"
_RttMonFileIOAdminSize_Object = MibTableColumn
rttMonFileIOAdminSize = _RttMonFileIOAdminSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 2),
    _RttMonFileIOAdminSize_Type()
)
rttMonFileIOAdminSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    rttMonFileIOAdminSize.setUnits("bytes")


class _RttMonFileIOAdminAction_Type(Integer32):
    """Custom type rttMonFileIOAdminAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 2),
          ("write", 1),
          ("writeRead", 3))
    )


_RttMonFileIOAdminAction_Type.__name__ = "Integer32"
_RttMonFileIOAdminAction_Object = MibTableColumn
rttMonFileIOAdminAction = _RttMonFileIOAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 3),
    _RttMonFileIOAdminAction_Type()
)
rttMonFileIOAdminAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminAction.setStatus("obsolete")
_RttMonScriptAdminTable_Object = MibTable
rttMonScriptAdminTable = _RttMonScriptAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rttMonScriptAdminTable.setStatus("obsolete")
_RttMonScriptAdminEntry_Object = MibTableRow
rttMonScriptAdminEntry = _RttMonScriptAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1)
)
rttMonScriptAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonScriptAdminEntry.setStatus("obsolete")
_RttMonScriptAdminName_Type = DisplayString
_RttMonScriptAdminName_Object = MibTableColumn
rttMonScriptAdminName = _RttMonScriptAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1, 1),
    _RttMonScriptAdminName_Type()
)
rttMonScriptAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScriptAdminName.setStatus("obsolete")
_RttMonScriptAdminCmdLineParams_Type = DisplayString
_RttMonScriptAdminCmdLineParams_Object = MibTableColumn
rttMonScriptAdminCmdLineParams = _RttMonScriptAdminCmdLineParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1, 2),
    _RttMonScriptAdminCmdLineParams_Type()
)
rttMonScriptAdminCmdLineParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScriptAdminCmdLineParams.setStatus("obsolete")
_RttMonScheduleAdminTable_Object = MibTable
rttMonScheduleAdminTable = _RttMonScheduleAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rttMonScheduleAdminTable.setStatus("current")
_RttMonScheduleAdminEntry_Object = MibTableRow
rttMonScheduleAdminEntry = _RttMonScheduleAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rttMonScheduleAdminEntry.setStatus("current")


class _RttMonScheduleAdminRttLife_Type(Integer32):
    """Custom type rttMonScheduleAdminRttLife based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonScheduleAdminRttLife_Type.__name__ = "Integer32"
_RttMonScheduleAdminRttLife_Object = MibTableColumn
rttMonScheduleAdminRttLife = _RttMonScheduleAdminRttLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 1),
    _RttMonScheduleAdminRttLife_Type()
)
rttMonScheduleAdminRttLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttLife.setStatus("current")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttLife.setUnits("seconds")


class _RttMonScheduleAdminRttStartTime_Type(TimeTicks):
    """Custom type rttMonScheduleAdminRttStartTime based on TimeTicks"""
    defaultValue = 0


_RttMonScheduleAdminRttStartTime_Object = MibTableColumn
rttMonScheduleAdminRttStartTime = _RttMonScheduleAdminRttStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 2),
    _RttMonScheduleAdminRttStartTime_Type()
)
rttMonScheduleAdminRttStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttStartTime.setStatus("current")


class _RttMonScheduleAdminConceptRowAgeout_Type(Integer32):
    """Custom type rttMonScheduleAdminConceptRowAgeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_RttMonScheduleAdminConceptRowAgeout_Type.__name__ = "Integer32"
_RttMonScheduleAdminConceptRowAgeout_Object = MibTableColumn
rttMonScheduleAdminConceptRowAgeout = _RttMonScheduleAdminConceptRowAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 3),
    _RttMonScheduleAdminConceptRowAgeout_Type()
)
rttMonScheduleAdminConceptRowAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeout.setStatus("deprecated")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeout.setUnits("seconds")


class _RttMonScheduleAdminRttRecurring_Type(TruthValue):
    """Custom type rttMonScheduleAdminRttRecurring based on TruthValue"""


_RttMonScheduleAdminRttRecurring_Object = MibTableColumn
rttMonScheduleAdminRttRecurring = _RttMonScheduleAdminRttRecurring_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 4),
    _RttMonScheduleAdminRttRecurring_Type()
)
rttMonScheduleAdminRttRecurring.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttRecurring.setStatus("current")


class _RttMonScheduleAdminConceptRowAgeoutV2_Type(Integer32):
    """Custom type rttMonScheduleAdminConceptRowAgeoutV2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_RttMonScheduleAdminConceptRowAgeoutV2_Type.__name__ = "Integer32"
_RttMonScheduleAdminConceptRowAgeoutV2_Object = MibTableColumn
rttMonScheduleAdminConceptRowAgeoutV2 = _RttMonScheduleAdminConceptRowAgeoutV2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 5),
    _RttMonScheduleAdminConceptRowAgeoutV2_Type()
)
rttMonScheduleAdminConceptRowAgeoutV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeoutV2.setStatus("current")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeoutV2.setUnits("seconds")


class _RttMonScheduleAdminStartType_Type(RttMonScheduleStartType):
    """Custom type rttMonScheduleAdminStartType based on RttMonScheduleStartType"""


_RttMonScheduleAdminStartType_Object = MibTableColumn
rttMonScheduleAdminStartType = _RttMonScheduleAdminStartType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 6),
    _RttMonScheduleAdminStartType_Type()
)
rttMonScheduleAdminStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminStartType.setStatus("current")


class _RttMonScheduleAdminStartDelay_Type(Integer32):
    """Custom type rttMonScheduleAdminStartDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 10000),
    )


_RttMonScheduleAdminStartDelay_Type.__name__ = "Integer32"
_RttMonScheduleAdminStartDelay_Object = MibTableColumn
rttMonScheduleAdminStartDelay = _RttMonScheduleAdminStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 7),
    _RttMonScheduleAdminStartDelay_Type()
)
rttMonScheduleAdminStartDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminStartDelay.setStatus("current")
_RttMonReactAdminTable_Object = MibTable
rttMonReactAdminTable = _RttMonReactAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rttMonReactAdminTable.setStatus("deprecated")
_RttMonReactAdminEntry_Object = MibTableRow
rttMonReactAdminEntry = _RttMonReactAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    rttMonReactAdminEntry.setStatus("deprecated")


class _RttMonReactAdminConnectionEnable_Type(TruthValue):
    """Custom type rttMonReactAdminConnectionEnable based on TruthValue"""


_RttMonReactAdminConnectionEnable_Object = MibTableColumn
rttMonReactAdminConnectionEnable = _RttMonReactAdminConnectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 1),
    _RttMonReactAdminConnectionEnable_Type()
)
rttMonReactAdminConnectionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminConnectionEnable.setStatus("deprecated")


class _RttMonReactAdminTimeoutEnable_Type(TruthValue):
    """Custom type rttMonReactAdminTimeoutEnable based on TruthValue"""


_RttMonReactAdminTimeoutEnable_Object = MibTableColumn
rttMonReactAdminTimeoutEnable = _RttMonReactAdminTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 2),
    _RttMonReactAdminTimeoutEnable_Type()
)
rttMonReactAdminTimeoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminTimeoutEnable.setStatus("deprecated")


class _RttMonReactAdminThresholdType_Type(Integer32):
    """Custom type rttMonReactAdminThresholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("average", 5),
          ("consecutive", 3),
          ("immediate", 2),
          ("never", 1),
          ("xOfy", 4))
    )


_RttMonReactAdminThresholdType_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdType_Object = MibTableColumn
rttMonReactAdminThresholdType = _RttMonReactAdminThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 3),
    _RttMonReactAdminThresholdType_Type()
)
rttMonReactAdminThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdType.setStatus("deprecated")


class _RttMonReactAdminThresholdFalling_Type(Integer32):
    """Custom type rttMonReactAdminThresholdFalling based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonReactAdminThresholdFalling_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdFalling_Object = MibTableColumn
rttMonReactAdminThresholdFalling = _RttMonReactAdminThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 4),
    _RttMonReactAdminThresholdFalling_Type()
)
rttMonReactAdminThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdFalling.setStatus("deprecated")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdFalling.setUnits("milliseconds")


class _RttMonReactAdminThresholdCount_Type(Integer32):
    """Custom type rttMonReactAdminThresholdCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactAdminThresholdCount_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdCount_Object = MibTableColumn
rttMonReactAdminThresholdCount = _RttMonReactAdminThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 5),
    _RttMonReactAdminThresholdCount_Type()
)
rttMonReactAdminThresholdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdCount.setStatus("deprecated")


class _RttMonReactAdminThresholdCount2_Type(Integer32):
    """Custom type rttMonReactAdminThresholdCount2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactAdminThresholdCount2_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdCount2_Object = MibTableColumn
rttMonReactAdminThresholdCount2 = _RttMonReactAdminThresholdCount2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 6),
    _RttMonReactAdminThresholdCount2_Type()
)
rttMonReactAdminThresholdCount2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdCount2.setStatus("deprecated")


class _RttMonReactAdminActionType_Type(Integer32):
    """Custom type rttMonReactAdminActionType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("nmvtAndTrigger", 7),
          ("nmvtOnly", 3),
          ("none", 1),
          ("trapAndNmvt", 5),
          ("trapAndTrigger", 6),
          ("trapNmvtAndTrigger", 8),
          ("trapOnly", 2),
          ("triggerOnly", 4))
    )


_RttMonReactAdminActionType_Type.__name__ = "Integer32"
_RttMonReactAdminActionType_Object = MibTableColumn
rttMonReactAdminActionType = _RttMonReactAdminActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 7),
    _RttMonReactAdminActionType_Type()
)
rttMonReactAdminActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminActionType.setStatus("deprecated")


class _RttMonReactAdminVerifyErrorEnable_Type(TruthValue):
    """Custom type rttMonReactAdminVerifyErrorEnable based on TruthValue"""


_RttMonReactAdminVerifyErrorEnable_Object = MibTableColumn
rttMonReactAdminVerifyErrorEnable = _RttMonReactAdminVerifyErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 8),
    _RttMonReactAdminVerifyErrorEnable_Type()
)
rttMonReactAdminVerifyErrorEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminVerifyErrorEnable.setStatus("deprecated")
_RttMonStatisticsAdminTable_Object = MibTable
rttMonStatisticsAdminTable = _RttMonStatisticsAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rttMonStatisticsAdminTable.setStatus("current")
_RttMonStatisticsAdminEntry_Object = MibTableRow
rttMonStatisticsAdminEntry = _RttMonStatisticsAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    rttMonStatisticsAdminEntry.setStatus("current")


class _RttMonStatisticsAdminNumHourGroups_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumHourGroups based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_RttMonStatisticsAdminNumHourGroups_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumHourGroups_Object = MibTableColumn
rttMonStatisticsAdminNumHourGroups = _RttMonStatisticsAdminNumHourGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 1),
    _RttMonStatisticsAdminNumHourGroups_Type()
)
rttMonStatisticsAdminNumHourGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumHourGroups.setStatus("current")


class _RttMonStatisticsAdminNumPaths_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumPaths based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RttMonStatisticsAdminNumPaths_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumPaths_Object = MibTableColumn
rttMonStatisticsAdminNumPaths = _RttMonStatisticsAdminNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 2),
    _RttMonStatisticsAdminNumPaths_Type()
)
rttMonStatisticsAdminNumPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumPaths.setStatus("current")


class _RttMonStatisticsAdminNumHops_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumHops based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonStatisticsAdminNumHops_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumHops_Object = MibTableColumn
rttMonStatisticsAdminNumHops = _RttMonStatisticsAdminNumHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 3),
    _RttMonStatisticsAdminNumHops_Type()
)
rttMonStatisticsAdminNumHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumHops.setStatus("current")


class _RttMonStatisticsAdminNumDistBuckets_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumDistBuckets based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RttMonStatisticsAdminNumDistBuckets_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumDistBuckets_Object = MibTableColumn
rttMonStatisticsAdminNumDistBuckets = _RttMonStatisticsAdminNumDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 4),
    _RttMonStatisticsAdminNumDistBuckets_Type()
)
rttMonStatisticsAdminNumDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumDistBuckets.setStatus("current")


class _RttMonStatisticsAdminDistInterval_Type(Integer32):
    """Custom type rttMonStatisticsAdminDistInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RttMonStatisticsAdminDistInterval_Type.__name__ = "Integer32"
_RttMonStatisticsAdminDistInterval_Object = MibTableColumn
rttMonStatisticsAdminDistInterval = _RttMonStatisticsAdminDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 5),
    _RttMonStatisticsAdminDistInterval_Type()
)
rttMonStatisticsAdminDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminDistInterval.setUnits("milliseconds")
_RttMonHistoryAdminTable_Object = MibTable
rttMonHistoryAdminTable = _RttMonHistoryAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8)
)
if mibBuilder.loadTexts:
    rttMonHistoryAdminTable.setStatus("current")
_RttMonHistoryAdminEntry_Object = MibTableRow
rttMonHistoryAdminEntry = _RttMonHistoryAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    rttMonHistoryAdminEntry.setStatus("current")


class _RttMonHistoryAdminNumLives_Type(Integer32):
    """Custom type rttMonHistoryAdminNumLives based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RttMonHistoryAdminNumLives_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumLives_Object = MibTableColumn
rttMonHistoryAdminNumLives = _RttMonHistoryAdminNumLives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 1),
    _RttMonHistoryAdminNumLives_Type()
)
rttMonHistoryAdminNumLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumLives.setStatus("current")


class _RttMonHistoryAdminNumBuckets_Type(Integer32):
    """Custom type rttMonHistoryAdminNumBuckets based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RttMonHistoryAdminNumBuckets_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumBuckets_Object = MibTableColumn
rttMonHistoryAdminNumBuckets = _RttMonHistoryAdminNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 2),
    _RttMonHistoryAdminNumBuckets_Type()
)
rttMonHistoryAdminNumBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumBuckets.setStatus("current")


class _RttMonHistoryAdminNumSamples_Type(Integer32):
    """Custom type rttMonHistoryAdminNumSamples based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonHistoryAdminNumSamples_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumSamples_Object = MibTableColumn
rttMonHistoryAdminNumSamples = _RttMonHistoryAdminNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 3),
    _RttMonHistoryAdminNumSamples_Type()
)
rttMonHistoryAdminNumSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumSamples.setStatus("current")


class _RttMonHistoryAdminFilter_Type(Integer32):
    """Custom type rttMonHistoryAdminFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("failures", 4),
          ("none", 1),
          ("overThreshold", 3))
    )


_RttMonHistoryAdminFilter_Type.__name__ = "Integer32"
_RttMonHistoryAdminFilter_Object = MibTableColumn
rttMonHistoryAdminFilter = _RttMonHistoryAdminFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 4),
    _RttMonHistoryAdminFilter_Type()
)
rttMonHistoryAdminFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminFilter.setStatus("current")
_RttMonCtrlOperTable_Object = MibTable
rttMonCtrlOperTable = _RttMonCtrlOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9)
)
if mibBuilder.loadTexts:
    rttMonCtrlOperTable.setStatus("current")
_RttMonCtrlOperEntry_Object = MibTableRow
rttMonCtrlOperEntry = _RttMonCtrlOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    rttMonCtrlOperEntry.setStatus("current")
_RttMonCtrlOperModificationTime_Type = TimeStamp
_RttMonCtrlOperModificationTime_Object = MibTableColumn
rttMonCtrlOperModificationTime = _RttMonCtrlOperModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 1),
    _RttMonCtrlOperModificationTime_Type()
)
rttMonCtrlOperModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperModificationTime.setStatus("current")


class _RttMonCtrlOperDiagText_Type(DisplayString):
    """Custom type rttMonCtrlOperDiagText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_RttMonCtrlOperDiagText_Type.__name__ = "DisplayString"
_RttMonCtrlOperDiagText_Object = MibTableColumn
rttMonCtrlOperDiagText = _RttMonCtrlOperDiagText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 2),
    _RttMonCtrlOperDiagText_Type()
)
rttMonCtrlOperDiagText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperDiagText.setStatus("current")
_RttMonCtrlOperResetTime_Type = TimeStamp
_RttMonCtrlOperResetTime_Object = MibTableColumn
rttMonCtrlOperResetTime = _RttMonCtrlOperResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 3),
    _RttMonCtrlOperResetTime_Type()
)
rttMonCtrlOperResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperResetTime.setStatus("current")
_RttMonCtrlOperOctetsInUse_Type = Gauge32
_RttMonCtrlOperOctetsInUse_Object = MibTableColumn
rttMonCtrlOperOctetsInUse = _RttMonCtrlOperOctetsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 4),
    _RttMonCtrlOperOctetsInUse_Type()
)
rttMonCtrlOperOctetsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperOctetsInUse.setStatus("current")


class _RttMonCtrlOperConnectionLostOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperConnectionLostOccurred based on TruthValue"""


_RttMonCtrlOperConnectionLostOccurred_Object = MibTableColumn
rttMonCtrlOperConnectionLostOccurred = _RttMonCtrlOperConnectionLostOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 5),
    _RttMonCtrlOperConnectionLostOccurred_Type()
)
rttMonCtrlOperConnectionLostOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperConnectionLostOccurred.setStatus("current")


class _RttMonCtrlOperTimeoutOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperTimeoutOccurred based on TruthValue"""


_RttMonCtrlOperTimeoutOccurred_Object = MibTableColumn
rttMonCtrlOperTimeoutOccurred = _RttMonCtrlOperTimeoutOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 6),
    _RttMonCtrlOperTimeoutOccurred_Type()
)
rttMonCtrlOperTimeoutOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperTimeoutOccurred.setStatus("current")


class _RttMonCtrlOperOverThresholdOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperOverThresholdOccurred based on TruthValue"""


_RttMonCtrlOperOverThresholdOccurred_Object = MibTableColumn
rttMonCtrlOperOverThresholdOccurred = _RttMonCtrlOperOverThresholdOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 7),
    _RttMonCtrlOperOverThresholdOccurred_Type()
)
rttMonCtrlOperOverThresholdOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperOverThresholdOccurred.setStatus("current")


class _RttMonCtrlOperNumRtts_Type(Integer32):
    """Custom type rttMonCtrlOperNumRtts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlOperNumRtts_Type.__name__ = "Integer32"
_RttMonCtrlOperNumRtts_Object = MibTableColumn
rttMonCtrlOperNumRtts = _RttMonCtrlOperNumRtts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 8),
    _RttMonCtrlOperNumRtts_Type()
)
rttMonCtrlOperNumRtts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperNumRtts.setStatus("current")


class _RttMonCtrlOperRttLife_Type(Integer32):
    """Custom type rttMonCtrlOperRttLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlOperRttLife_Type.__name__ = "Integer32"
_RttMonCtrlOperRttLife_Object = MibTableColumn
rttMonCtrlOperRttLife = _RttMonCtrlOperRttLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 9),
    _RttMonCtrlOperRttLife_Type()
)
rttMonCtrlOperRttLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperRttLife.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlOperRttLife.setUnits("seconds")


class _RttMonCtrlOperState_Type(Integer32):
    """Custom type rttMonCtrlOperState based on Integer32"""
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
        *(("active", 6),
          ("immediateStop", 3),
          ("inactive", 5),
          ("orderlyStop", 2),
          ("pending", 4),
          ("reset", 1),
          ("restart", 7))
    )


_RttMonCtrlOperState_Type.__name__ = "Integer32"
_RttMonCtrlOperState_Object = MibTableColumn
rttMonCtrlOperState = _RttMonCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 10),
    _RttMonCtrlOperState_Type()
)
rttMonCtrlOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonCtrlOperState.setStatus("current")


class _RttMonCtrlOperVerifyErrorOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperVerifyErrorOccurred based on TruthValue"""


_RttMonCtrlOperVerifyErrorOccurred_Object = MibTableColumn
rttMonCtrlOperVerifyErrorOccurred = _RttMonCtrlOperVerifyErrorOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 11),
    _RttMonCtrlOperVerifyErrorOccurred_Type()
)
rttMonCtrlOperVerifyErrorOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperVerifyErrorOccurred.setStatus("current")
_RttMonLatestRttOperTable_Object = MibTable
rttMonLatestRttOperTable = _RttMonLatestRttOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10)
)
if mibBuilder.loadTexts:
    rttMonLatestRttOperTable.setStatus("current")
_RttMonLatestRttOperEntry_Object = MibTableRow
rttMonLatestRttOperEntry = _RttMonLatestRttOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    rttMonLatestRttOperEntry.setStatus("current")
_RttMonLatestRttOperCompletionTime_Type = Gauge32
_RttMonLatestRttOperCompletionTime_Object = MibTableColumn
rttMonLatestRttOperCompletionTime = _RttMonLatestRttOperCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 1),
    _RttMonLatestRttOperCompletionTime_Type()
)
rttMonLatestRttOperCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRttOperCompletionTime.setUnits("milliseconds/microseconds")
_RttMonLatestRttOperSense_Type = RttResponseSense
_RttMonLatestRttOperSense_Object = MibTableColumn
rttMonLatestRttOperSense = _RttMonLatestRttOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 2),
    _RttMonLatestRttOperSense_Type()
)
rttMonLatestRttOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperSense.setStatus("current")


class _RttMonLatestRttOperApplSpecificSense_Type(Integer32):
    """Custom type rttMonLatestRttOperApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestRttOperApplSpecificSense_Type.__name__ = "Integer32"
_RttMonLatestRttOperApplSpecificSense_Object = MibTableColumn
rttMonLatestRttOperApplSpecificSense = _RttMonLatestRttOperApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 3),
    _RttMonLatestRttOperApplSpecificSense_Type()
)
rttMonLatestRttOperApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperApplSpecificSense.setStatus("current")
_RttMonLatestRttOperSenseDescription_Type = DisplayString
_RttMonLatestRttOperSenseDescription_Object = MibTableColumn
rttMonLatestRttOperSenseDescription = _RttMonLatestRttOperSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 4),
    _RttMonLatestRttOperSenseDescription_Type()
)
rttMonLatestRttOperSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperSenseDescription.setStatus("current")
_RttMonLatestRttOperTime_Type = TimeStamp
_RttMonLatestRttOperTime_Object = MibTableColumn
rttMonLatestRttOperTime = _RttMonLatestRttOperTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 5),
    _RttMonLatestRttOperTime_Type()
)
rttMonLatestRttOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperTime.setStatus("current")
_RttMonLatestRttOperAddress_Type = RttMonTargetAddress
_RttMonLatestRttOperAddress_Object = MibTableColumn
rttMonLatestRttOperAddress = _RttMonLatestRttOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 6),
    _RttMonLatestRttOperAddress_Type()
)
rttMonLatestRttOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperAddress.setStatus("current")
_RttMonReactTriggerAdminTable_Object = MibTable
rttMonReactTriggerAdminTable = _RttMonReactTriggerAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminTable.setStatus("current")
_RttMonReactTriggerAdminEntry_Object = MibTableRow
rttMonReactTriggerAdminEntry = _RttMonReactTriggerAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1)
)
rttMonReactTriggerAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonReactTriggerAdminRttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminEntry.setStatus("current")


class _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type(Integer32):
    """Custom type rttMonReactTriggerAdminRttMonCtrlAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type.__name__ = "Integer32"
_RttMonReactTriggerAdminRttMonCtrlAdminIndex_Object = MibTableColumn
rttMonReactTriggerAdminRttMonCtrlAdminIndex = _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1, 1),
    _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type()
)
rttMonReactTriggerAdminRttMonCtrlAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminRttMonCtrlAdminIndex.setStatus("current")
_RttMonReactTriggerAdminStatus_Type = RowStatus
_RttMonReactTriggerAdminStatus_Object = MibTableColumn
rttMonReactTriggerAdminStatus = _RttMonReactTriggerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1, 2),
    _RttMonReactTriggerAdminStatus_Type()
)
rttMonReactTriggerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminStatus.setStatus("current")
_RttMonReactTriggerOperTable_Object = MibTable
rttMonReactTriggerOperTable = _RttMonReactTriggerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerOperTable.setStatus("current")
_RttMonReactTriggerOperEntry_Object = MibTableRow
rttMonReactTriggerOperEntry = _RttMonReactTriggerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerOperEntry.setStatus("current")


class _RttMonReactTriggerOperState_Type(Integer32):
    """Custom type rttMonReactTriggerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("pending", 2))
    )


_RttMonReactTriggerOperState_Type.__name__ = "Integer32"
_RttMonReactTriggerOperState_Object = MibTableColumn
rttMonReactTriggerOperState = _RttMonReactTriggerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12, 1, 1),
    _RttMonReactTriggerOperState_Type()
)
rttMonReactTriggerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonReactTriggerOperState.setStatus("current")
_RttMonEchoPathAdminTable_Object = MibTable
rttMonEchoPathAdminTable = _RttMonEchoPathAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13)
)
if mibBuilder.loadTexts:
    rttMonEchoPathAdminTable.setStatus("current")
_RttMonEchoPathAdminEntry_Object = MibTableRow
rttMonEchoPathAdminEntry = _RttMonEchoPathAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1)
)
rttMonEchoPathAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonEchoPathAdminHopIndex"),
)
if mibBuilder.loadTexts:
    rttMonEchoPathAdminEntry.setStatus("current")


class _RttMonEchoPathAdminHopIndex_Type(Integer32):
    """Custom type rttMonEchoPathAdminHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RttMonEchoPathAdminHopIndex_Type.__name__ = "Integer32"
_RttMonEchoPathAdminHopIndex_Object = MibTableColumn
rttMonEchoPathAdminHopIndex = _RttMonEchoPathAdminHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1, 1),
    _RttMonEchoPathAdminHopIndex_Type()
)
rttMonEchoPathAdminHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonEchoPathAdminHopIndex.setStatus("current")
_RttMonEchoPathAdminHopAddress_Type = RttMonTargetAddress
_RttMonEchoPathAdminHopAddress_Object = MibTableColumn
rttMonEchoPathAdminHopAddress = _RttMonEchoPathAdminHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1, 2),
    _RttMonEchoPathAdminHopAddress_Type()
)
rttMonEchoPathAdminHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoPathAdminHopAddress.setStatus("current")
_RttMonGrpScheduleAdminTable_Object = MibTable
rttMonGrpScheduleAdminTable = _RttMonGrpScheduleAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14)
)
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminTable.setStatus("current")
_RttMonGrpScheduleAdminEntry_Object = MibTableRow
rttMonGrpScheduleAdminEntry = _RttMonGrpScheduleAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1)
)
rttMonGrpScheduleAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminEntry.setStatus("current")


class _RttMonGrpScheduleAdminIndex_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonGrpScheduleAdminIndex_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminIndex_Object = MibTableColumn
rttMonGrpScheduleAdminIndex = _RttMonGrpScheduleAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 1),
    _RttMonGrpScheduleAdminIndex_Type()
)
rttMonGrpScheduleAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminIndex.setStatus("current")


class _RttMonGrpScheduleAdminProbes_Type(DisplayString):
    """Custom type rttMonGrpScheduleAdminProbes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_RttMonGrpScheduleAdminProbes_Type.__name__ = "DisplayString"
_RttMonGrpScheduleAdminProbes_Object = MibTableColumn
rttMonGrpScheduleAdminProbes = _RttMonGrpScheduleAdminProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 2),
    _RttMonGrpScheduleAdminProbes_Type()
)
rttMonGrpScheduleAdminProbes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminProbes.setStatus("current")


class _RttMonGrpScheduleAdminPeriod_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonGrpScheduleAdminPeriod_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminPeriod_Object = MibTableColumn
rttMonGrpScheduleAdminPeriod = _RttMonGrpScheduleAdminPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 3),
    _RttMonGrpScheduleAdminPeriod_Type()
)
rttMonGrpScheduleAdminPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminPeriod.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminPeriod.setUnits("seconds")


class _RttMonGrpScheduleAdminFrequency_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonGrpScheduleAdminFrequency_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminFrequency_Object = MibTableColumn
rttMonGrpScheduleAdminFrequency = _RttMonGrpScheduleAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 4),
    _RttMonGrpScheduleAdminFrequency_Type()
)
rttMonGrpScheduleAdminFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFrequency.setUnits("seconds")


class _RttMonGrpScheduleAdminLife_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminLife based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonGrpScheduleAdminLife_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminLife_Object = MibTableColumn
rttMonGrpScheduleAdminLife = _RttMonGrpScheduleAdminLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 5),
    _RttMonGrpScheduleAdminLife_Type()
)
rttMonGrpScheduleAdminLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminLife.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminLife.setUnits("seconds")


class _RttMonGrpScheduleAdminAgeout_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminAgeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_RttMonGrpScheduleAdminAgeout_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminAgeout_Object = MibTableColumn
rttMonGrpScheduleAdminAgeout = _RttMonGrpScheduleAdminAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 6),
    _RttMonGrpScheduleAdminAgeout_Type()
)
rttMonGrpScheduleAdminAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminAgeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminAgeout.setUnits("seconds")
_RttMonGrpScheduleAdminStatus_Type = RowStatus
_RttMonGrpScheduleAdminStatus_Object = MibTableColumn
rttMonGrpScheduleAdminStatus = _RttMonGrpScheduleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 7),
    _RttMonGrpScheduleAdminStatus_Type()
)
rttMonGrpScheduleAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminStatus.setStatus("current")


class _RttMonGrpScheduleAdminFreqMax_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminFreqMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonGrpScheduleAdminFreqMax_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminFreqMax_Object = MibTableColumn
rttMonGrpScheduleAdminFreqMax = _RttMonGrpScheduleAdminFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 8),
    _RttMonGrpScheduleAdminFreqMax_Type()
)
rttMonGrpScheduleAdminFreqMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFreqMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFreqMax.setUnits("seconds")


class _RttMonGrpScheduleAdminFreqMin_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminFreqMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonGrpScheduleAdminFreqMin_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminFreqMin_Object = MibTableColumn
rttMonGrpScheduleAdminFreqMin = _RttMonGrpScheduleAdminFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 9),
    _RttMonGrpScheduleAdminFreqMin_Type()
)
rttMonGrpScheduleAdminFreqMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFreqMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminFreqMin.setUnits("seconds")


class _RttMonGrpScheduleAdminStartTime_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonGrpScheduleAdminStartTime_Type.__name__ = "Integer32"
_RttMonGrpScheduleAdminStartTime_Object = MibTableColumn
rttMonGrpScheduleAdminStartTime = _RttMonGrpScheduleAdminStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 10),
    _RttMonGrpScheduleAdminStartTime_Type()
)
rttMonGrpScheduleAdminStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminStartTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminStartTime.setUnits("seconds")
_RttMonGrpScheduleAdminAdd_Type = TruthValue
_RttMonGrpScheduleAdminAdd_Object = MibTableColumn
rttMonGrpScheduleAdminAdd = _RttMonGrpScheduleAdminAdd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 11),
    _RttMonGrpScheduleAdminAdd_Type()
)
rttMonGrpScheduleAdminAdd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminAdd.setStatus("current")
_RttMonGrpScheduleAdminDelete_Type = TruthValue
_RttMonGrpScheduleAdminDelete_Object = MibTableColumn
rttMonGrpScheduleAdminDelete = _RttMonGrpScheduleAdminDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 12),
    _RttMonGrpScheduleAdminDelete_Type()
)
rttMonGrpScheduleAdminDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminDelete.setStatus("current")
_RttMonGrpScheduleAdminReset_Type = TruthValue
_RttMonGrpScheduleAdminReset_Object = MibTableColumn
rttMonGrpScheduleAdminReset = _RttMonGrpScheduleAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 13),
    _RttMonGrpScheduleAdminReset_Type()
)
rttMonGrpScheduleAdminReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminReset.setStatus("current")


class _RttMonGrpScheduleAdminStartType_Type(RttMonScheduleStartType):
    """Custom type rttMonGrpScheduleAdminStartType based on RttMonScheduleStartType"""


_RttMonGrpScheduleAdminStartType_Object = MibTableColumn
rttMonGrpScheduleAdminStartType = _RttMonGrpScheduleAdminStartType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 14),
    _RttMonGrpScheduleAdminStartType_Type()
)
rttMonGrpScheduleAdminStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminStartType.setStatus("current")


class _RttMonGrpScheduleAdminStartDelay_Type(Integer32):
    """Custom type rttMonGrpScheduleAdminStartDelay based on Integer32"""
    defaultValue = 0


_RttMonGrpScheduleAdminStartDelay_Object = MibTableColumn
rttMonGrpScheduleAdminStartDelay = _RttMonGrpScheduleAdminStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 14, 1, 15),
    _RttMonGrpScheduleAdminStartDelay_Type()
)
rttMonGrpScheduleAdminStartDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonGrpScheduleAdminStartDelay.setStatus("current")
_RttMplsVpnMonCtrlTable_Object = MibTable
rttMplsVpnMonCtrlTable = _RttMplsVpnMonCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlTable.setStatus("current")
_RttMplsVpnMonCtrlEntry_Object = MibTableRow
rttMplsVpnMonCtrlEntry = _RttMplsVpnMonCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1)
)
rttMplsVpnMonCtrlEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlIndex"),
)
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlEntry.setStatus("current")


class _RttMplsVpnMonCtrlIndex_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMplsVpnMonCtrlIndex_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlIndex_Object = MibTableColumn
rttMplsVpnMonCtrlIndex = _RttMplsVpnMonCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 1),
    _RttMplsVpnMonCtrlIndex_Type()
)
rttMplsVpnMonCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlIndex.setStatus("current")
_RttMplsVpnMonCtrlRttType_Type = RttMplsVpnMonRttType
_RttMplsVpnMonCtrlRttType_Object = MibTableColumn
rttMplsVpnMonCtrlRttType = _RttMplsVpnMonCtrlRttType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 2),
    _RttMplsVpnMonCtrlRttType_Type()
)
rttMplsVpnMonCtrlRttType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlRttType.setStatus("current")


class _RttMplsVpnMonCtrlVrfName_Type(OctetString):
    """Custom type rttMplsVpnMonCtrlVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RttMplsVpnMonCtrlVrfName_Type.__name__ = "OctetString"
_RttMplsVpnMonCtrlVrfName_Object = MibTableColumn
rttMplsVpnMonCtrlVrfName = _RttMplsVpnMonCtrlVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 3),
    _RttMplsVpnMonCtrlVrfName_Type()
)
rttMplsVpnMonCtrlVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlVrfName.setStatus("current")


class _RttMplsVpnMonCtrlTag_Type(DisplayString):
    """Custom type rttMplsVpnMonCtrlTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RttMplsVpnMonCtrlTag_Type.__name__ = "DisplayString"
_RttMplsVpnMonCtrlTag_Object = MibTableColumn
rttMplsVpnMonCtrlTag = _RttMplsVpnMonCtrlTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 4),
    _RttMplsVpnMonCtrlTag_Type()
)
rttMplsVpnMonCtrlTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlTag.setStatus("current")


class _RttMplsVpnMonCtrlThreshold_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMplsVpnMonCtrlThreshold_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlThreshold_Object = MibTableColumn
rttMplsVpnMonCtrlThreshold = _RttMplsVpnMonCtrlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 5),
    _RttMplsVpnMonCtrlThreshold_Type()
)
rttMplsVpnMonCtrlThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlThreshold.setUnits("milliseconds")


class _RttMplsVpnMonCtrlTimeout_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RttMplsVpnMonCtrlTimeout_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlTimeout_Object = MibTableColumn
rttMplsVpnMonCtrlTimeout = _RttMplsVpnMonCtrlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 6),
    _RttMplsVpnMonCtrlTimeout_Type()
)
rttMplsVpnMonCtrlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlTimeout.setUnits("milliseconds")


class _RttMplsVpnMonCtrlScanInterval_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlScanInterval based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 70560),
    )


_RttMplsVpnMonCtrlScanInterval_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlScanInterval_Object = MibTableColumn
rttMplsVpnMonCtrlScanInterval = _RttMplsVpnMonCtrlScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 7),
    _RttMplsVpnMonCtrlScanInterval_Type()
)
rttMplsVpnMonCtrlScanInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlScanInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlScanInterval.setUnits("minutes")


class _RttMplsVpnMonCtrlDelScanFactor_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlDelScanFactor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMplsVpnMonCtrlDelScanFactor_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlDelScanFactor_Object = MibTableColumn
rttMplsVpnMonCtrlDelScanFactor = _RttMplsVpnMonCtrlDelScanFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 8),
    _RttMplsVpnMonCtrlDelScanFactor_Type()
)
rttMplsVpnMonCtrlDelScanFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlDelScanFactor.setStatus("current")


class _RttMplsVpnMonCtrlEXP_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlEXP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RttMplsVpnMonCtrlEXP_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlEXP_Object = MibTableColumn
rttMplsVpnMonCtrlEXP = _RttMplsVpnMonCtrlEXP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 9),
    _RttMplsVpnMonCtrlEXP_Type()
)
rttMplsVpnMonCtrlEXP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlEXP.setStatus("current")


class _RttMplsVpnMonCtrlRequestSize_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlRequestSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMplsVpnMonCtrlRequestSize_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlRequestSize_Object = MibTableColumn
rttMplsVpnMonCtrlRequestSize = _RttMplsVpnMonCtrlRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 10),
    _RttMplsVpnMonCtrlRequestSize_Type()
)
rttMplsVpnMonCtrlRequestSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlRequestSize.setUnits("octets")


class _RttMplsVpnMonCtrlVerifyData_Type(TruthValue):
    """Custom type rttMplsVpnMonCtrlVerifyData based on TruthValue"""


_RttMplsVpnMonCtrlVerifyData_Object = MibTableColumn
rttMplsVpnMonCtrlVerifyData = _RttMplsVpnMonCtrlVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 11),
    _RttMplsVpnMonCtrlVerifyData_Type()
)
rttMplsVpnMonCtrlVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlVerifyData.setStatus("current")


class _RttMplsVpnMonCtrlStorageType_Type(StorageType):
    """Custom type rttMplsVpnMonCtrlStorageType based on StorageType"""


_RttMplsVpnMonCtrlStorageType_Object = MibTableColumn
rttMplsVpnMonCtrlStorageType = _RttMplsVpnMonCtrlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 12),
    _RttMplsVpnMonCtrlStorageType_Type()
)
rttMplsVpnMonCtrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlStorageType.setStatus("current")
_RttMplsVpnMonCtrlProbeList_Type = DisplayString
_RttMplsVpnMonCtrlProbeList_Object = MibTableColumn
rttMplsVpnMonCtrlProbeList = _RttMplsVpnMonCtrlProbeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 13),
    _RttMplsVpnMonCtrlProbeList_Type()
)
rttMplsVpnMonCtrlProbeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlProbeList.setStatus("current")
_RttMplsVpnMonCtrlStatus_Type = RowStatus
_RttMplsVpnMonCtrlStatus_Object = MibTableColumn
rttMplsVpnMonCtrlStatus = _RttMplsVpnMonCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 14),
    _RttMplsVpnMonCtrlStatus_Type()
)
rttMplsVpnMonCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlStatus.setStatus("current")


class _RttMplsVpnMonCtrlLpd_Type(TruthValue):
    """Custom type rttMplsVpnMonCtrlLpd based on TruthValue"""


_RttMplsVpnMonCtrlLpd_Object = MibTableColumn
rttMplsVpnMonCtrlLpd = _RttMplsVpnMonCtrlLpd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 15),
    _RttMplsVpnMonCtrlLpd_Type()
)
rttMplsVpnMonCtrlLpd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlLpd.setStatus("current")
_RttMplsVpnMonCtrlLpdGrpList_Type = DisplayString
_RttMplsVpnMonCtrlLpdGrpList_Object = MibTableColumn
rttMplsVpnMonCtrlLpdGrpList = _RttMplsVpnMonCtrlLpdGrpList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 16),
    _RttMplsVpnMonCtrlLpdGrpList_Type()
)
rttMplsVpnMonCtrlLpdGrpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlLpdGrpList.setStatus("current")


class _RttMplsVpnMonCtrlLpdCompTime_Type(Integer32):
    """Custom type rttMplsVpnMonCtrlLpdCompTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RttMplsVpnMonCtrlLpdCompTime_Type.__name__ = "Integer32"
_RttMplsVpnMonCtrlLpdCompTime_Object = MibTableColumn
rttMplsVpnMonCtrlLpdCompTime = _RttMplsVpnMonCtrlLpdCompTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 15, 1, 17),
    _RttMplsVpnMonCtrlLpdCompTime_Type()
)
rttMplsVpnMonCtrlLpdCompTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlLpdCompTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonCtrlLpdCompTime.setUnits("minutes")
_RttMplsVpnMonTypeTable_Object = MibTable
rttMplsVpnMonTypeTable = _RttMplsVpnMonTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeTable.setStatus("current")
_RttMplsVpnMonTypeEntry_Object = MibTableRow
rttMplsVpnMonTypeEntry = _RttMplsVpnMonTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeEntry.setStatus("current")


class _RttMplsVpnMonTypeInterval_Type(Integer32):
    """Custom type rttMplsVpnMonTypeInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_RttMplsVpnMonTypeInterval_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeInterval_Object = MibTableColumn
rttMplsVpnMonTypeInterval = _RttMplsVpnMonTypeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 1),
    _RttMplsVpnMonTypeInterval_Type()
)
rttMplsVpnMonTypeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeInterval.setUnits("milliseconds")


class _RttMplsVpnMonTypeNumPackets_Type(Integer32):
    """Custom type rttMplsVpnMonTypeNumPackets based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_RttMplsVpnMonTypeNumPackets_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeNumPackets_Object = MibTableColumn
rttMplsVpnMonTypeNumPackets = _RttMplsVpnMonTypeNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 2),
    _RttMplsVpnMonTypeNumPackets_Type()
)
rttMplsVpnMonTypeNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeNumPackets.setStatus("current")


class _RttMplsVpnMonTypeDestPort_Type(Integer32):
    """Custom type rttMplsVpnMonTypeDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_RttMplsVpnMonTypeDestPort_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeDestPort_Object = MibTableColumn
rttMplsVpnMonTypeDestPort = _RttMplsVpnMonTypeDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 3),
    _RttMplsVpnMonTypeDestPort_Type()
)
rttMplsVpnMonTypeDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeDestPort.setStatus("current")


class _RttMplsVpnMonTypeSecFreqType_Type(Integer32):
    """Custom type rttMplsVpnMonTypeSecFreqType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("connectionLoss", 3),
          ("none", 1),
          ("timeout", 2))
    )


_RttMplsVpnMonTypeSecFreqType_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeSecFreqType_Object = MibTableColumn
rttMplsVpnMonTypeSecFreqType = _RttMplsVpnMonTypeSecFreqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 4),
    _RttMplsVpnMonTypeSecFreqType_Type()
)
rttMplsVpnMonTypeSecFreqType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeSecFreqType.setStatus("current")


class _RttMplsVpnMonTypeSecFreqValue_Type(Integer32):
    """Custom type rttMplsVpnMonTypeSecFreqValue based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_RttMplsVpnMonTypeSecFreqValue_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeSecFreqValue_Object = MibTableColumn
rttMplsVpnMonTypeSecFreqValue = _RttMplsVpnMonTypeSecFreqValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 5),
    _RttMplsVpnMonTypeSecFreqValue_Type()
)
rttMplsVpnMonTypeSecFreqValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeSecFreqValue.setStatus("current")


class _RttMplsVpnMonTypeLspSelector_Type(OctetString):
    """Custom type rttMplsVpnMonTypeLspSelector based on OctetString"""
    defaultValue = OctetString("7F 00 00 01")


_RttMplsVpnMonTypeLspSelector_Object = MibTableColumn
rttMplsVpnMonTypeLspSelector = _RttMplsVpnMonTypeLspSelector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 6),
    _RttMplsVpnMonTypeLspSelector_Type()
)
rttMplsVpnMonTypeLspSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLspSelector.setStatus("current")


class _RttMplsVpnMonTypeLSPReplyMode_Type(RttMonLSPPingReplyMode):
    """Custom type rttMplsVpnMonTypeLSPReplyMode based on RttMonLSPPingReplyMode"""


_RttMplsVpnMonTypeLSPReplyMode_Object = MibTableColumn
rttMplsVpnMonTypeLSPReplyMode = _RttMplsVpnMonTypeLSPReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 7),
    _RttMplsVpnMonTypeLSPReplyMode_Type()
)
rttMplsVpnMonTypeLSPReplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLSPReplyMode.setStatus("current")


class _RttMplsVpnMonTypeLSPTTL_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLSPTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RttMplsVpnMonTypeLSPTTL_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLSPTTL_Object = MibTableColumn
rttMplsVpnMonTypeLSPTTL = _RttMplsVpnMonTypeLSPTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 8),
    _RttMplsVpnMonTypeLSPTTL_Type()
)
rttMplsVpnMonTypeLSPTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLSPTTL.setStatus("current")


class _RttMplsVpnMonTypeLSPReplyDscp_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLSPReplyDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_RttMplsVpnMonTypeLSPReplyDscp_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLSPReplyDscp_Object = MibTableColumn
rttMplsVpnMonTypeLSPReplyDscp = _RttMplsVpnMonTypeLSPReplyDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 9),
    _RttMplsVpnMonTypeLSPReplyDscp_Type()
)
rttMplsVpnMonTypeLSPReplyDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLSPReplyDscp.setStatus("current")


class _RttMplsVpnMonTypeLpdMaxSessions_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdMaxSessions based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RttMplsVpnMonTypeLpdMaxSessions_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdMaxSessions_Object = MibTableColumn
rttMplsVpnMonTypeLpdMaxSessions = _RttMplsVpnMonTypeLpdMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 10),
    _RttMplsVpnMonTypeLpdMaxSessions_Type()
)
rttMplsVpnMonTypeLpdMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdMaxSessions.setStatus("current")


class _RttMplsVpnMonTypeLpdSessTimeout_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdSessTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_RttMplsVpnMonTypeLpdSessTimeout_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdSessTimeout_Object = MibTableColumn
rttMplsVpnMonTypeLpdSessTimeout = _RttMplsVpnMonTypeLpdSessTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 11),
    _RttMplsVpnMonTypeLpdSessTimeout_Type()
)
rttMplsVpnMonTypeLpdSessTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdSessTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdSessTimeout.setUnits("seconds")


class _RttMplsVpnMonTypeLpdEchoTimeout_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdEchoTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RttMplsVpnMonTypeLpdEchoTimeout_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdEchoTimeout_Object = MibTableColumn
rttMplsVpnMonTypeLpdEchoTimeout = _RttMplsVpnMonTypeLpdEchoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 12),
    _RttMplsVpnMonTypeLpdEchoTimeout_Type()
)
rttMplsVpnMonTypeLpdEchoTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdEchoTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdEchoTimeout.setUnits("milliseconds")


class _RttMplsVpnMonTypeLpdEchoInterval_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdEchoInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RttMplsVpnMonTypeLpdEchoInterval_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdEchoInterval_Object = MibTableColumn
rttMplsVpnMonTypeLpdEchoInterval = _RttMplsVpnMonTypeLpdEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 13),
    _RttMplsVpnMonTypeLpdEchoInterval_Type()
)
rttMplsVpnMonTypeLpdEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdEchoInterval.setUnits("milliseconds")


class _RttMplsVpnMonTypeLpdEchoNullShim_Type(TruthValue):
    """Custom type rttMplsVpnMonTypeLpdEchoNullShim based on TruthValue"""


_RttMplsVpnMonTypeLpdEchoNullShim_Object = MibTableColumn
rttMplsVpnMonTypeLpdEchoNullShim = _RttMplsVpnMonTypeLpdEchoNullShim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 14),
    _RttMplsVpnMonTypeLpdEchoNullShim_Type()
)
rttMplsVpnMonTypeLpdEchoNullShim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdEchoNullShim.setStatus("current")


class _RttMplsVpnMonTypeLpdScanPeriod_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdScanPeriod based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_RttMplsVpnMonTypeLpdScanPeriod_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdScanPeriod_Object = MibTableColumn
rttMplsVpnMonTypeLpdScanPeriod = _RttMplsVpnMonTypeLpdScanPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 15),
    _RttMplsVpnMonTypeLpdScanPeriod_Type()
)
rttMplsVpnMonTypeLpdScanPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdScanPeriod.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdScanPeriod.setUnits("minutes")


class _RttMplsVpnMonTypeLpdStatHours_Type(Integer32):
    """Custom type rttMplsVpnMonTypeLpdStatHours based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RttMplsVpnMonTypeLpdStatHours_Type.__name__ = "Integer32"
_RttMplsVpnMonTypeLpdStatHours_Object = MibTableColumn
rttMplsVpnMonTypeLpdStatHours = _RttMplsVpnMonTypeLpdStatHours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 16, 1, 16),
    _RttMplsVpnMonTypeLpdStatHours_Type()
)
rttMplsVpnMonTypeLpdStatHours.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonTypeLpdStatHours.setStatus("current")
_RttMplsVpnMonScheduleTable_Object = MibTable
rttMplsVpnMonScheduleTable = _RttMplsVpnMonScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 17)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonScheduleTable.setStatus("current")
_RttMplsVpnMonScheduleEntry_Object = MibTableRow
rttMplsVpnMonScheduleEntry = _RttMplsVpnMonScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonScheduleEntry.setStatus("current")


class _RttMplsVpnMonScheduleRttStartTime_Type(TimeTicks):
    """Custom type rttMplsVpnMonScheduleRttStartTime based on TimeTicks"""
    defaultValue = 0


_RttMplsVpnMonScheduleRttStartTime_Object = MibTableColumn
rttMplsVpnMonScheduleRttStartTime = _RttMplsVpnMonScheduleRttStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 17, 1, 1),
    _RttMplsVpnMonScheduleRttStartTime_Type()
)
rttMplsVpnMonScheduleRttStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonScheduleRttStartTime.setStatus("current")


class _RttMplsVpnMonSchedulePeriod_Type(Integer32):
    """Custom type rttMplsVpnMonSchedulePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_RttMplsVpnMonSchedulePeriod_Type.__name__ = "Integer32"
_RttMplsVpnMonSchedulePeriod_Object = MibTableColumn
rttMplsVpnMonSchedulePeriod = _RttMplsVpnMonSchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 17, 1, 2),
    _RttMplsVpnMonSchedulePeriod_Type()
)
rttMplsVpnMonSchedulePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonSchedulePeriod.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonSchedulePeriod.setUnits("seconds")


class _RttMplsVpnMonScheduleFrequency_Type(Integer32):
    """Custom type rttMplsVpnMonScheduleFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_RttMplsVpnMonScheduleFrequency_Type.__name__ = "Integer32"
_RttMplsVpnMonScheduleFrequency_Object = MibTableColumn
rttMplsVpnMonScheduleFrequency = _RttMplsVpnMonScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 17, 1, 3),
    _RttMplsVpnMonScheduleFrequency_Type()
)
rttMplsVpnMonScheduleFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonScheduleFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonScheduleFrequency.setUnits("seconds")
_RttMplsVpnMonReactTable_Object = MibTable
rttMplsVpnMonReactTable = _RttMplsVpnMonReactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonReactTable.setStatus("current")
_RttMplsVpnMonReactEntry_Object = MibTableRow
rttMplsVpnMonReactEntry = _RttMplsVpnMonReactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    rttMplsVpnMonReactEntry.setStatus("current")


class _RttMplsVpnMonReactConnectionEnable_Type(TruthValue):
    """Custom type rttMplsVpnMonReactConnectionEnable based on TruthValue"""


_RttMplsVpnMonReactConnectionEnable_Object = MibTableColumn
rttMplsVpnMonReactConnectionEnable = _RttMplsVpnMonReactConnectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 1),
    _RttMplsVpnMonReactConnectionEnable_Type()
)
rttMplsVpnMonReactConnectionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactConnectionEnable.setStatus("current")


class _RttMplsVpnMonReactTimeoutEnable_Type(TruthValue):
    """Custom type rttMplsVpnMonReactTimeoutEnable based on TruthValue"""


_RttMplsVpnMonReactTimeoutEnable_Object = MibTableColumn
rttMplsVpnMonReactTimeoutEnable = _RttMplsVpnMonReactTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 2),
    _RttMplsVpnMonReactTimeoutEnable_Type()
)
rttMplsVpnMonReactTimeoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactTimeoutEnable.setStatus("current")


class _RttMplsVpnMonReactThresholdType_Type(Integer32):
    """Custom type rttMplsVpnMonReactThresholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("consecutive", 3),
          ("immediate", 2),
          ("never", 1))
    )


_RttMplsVpnMonReactThresholdType_Type.__name__ = "Integer32"
_RttMplsVpnMonReactThresholdType_Object = MibTableColumn
rttMplsVpnMonReactThresholdType = _RttMplsVpnMonReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 3),
    _RttMplsVpnMonReactThresholdType_Type()
)
rttMplsVpnMonReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactThresholdType.setStatus("current")


class _RttMplsVpnMonReactThresholdCount_Type(Integer32):
    """Custom type rttMplsVpnMonReactThresholdCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMplsVpnMonReactThresholdCount_Type.__name__ = "Integer32"
_RttMplsVpnMonReactThresholdCount_Object = MibTableColumn
rttMplsVpnMonReactThresholdCount = _RttMplsVpnMonReactThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 4),
    _RttMplsVpnMonReactThresholdCount_Type()
)
rttMplsVpnMonReactThresholdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactThresholdCount.setStatus("current")


class _RttMplsVpnMonReactActionType_Type(Integer32):
    """Custom type rttMplsVpnMonReactActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("trapOnly", 2))
    )


_RttMplsVpnMonReactActionType_Type.__name__ = "Integer32"
_RttMplsVpnMonReactActionType_Object = MibTableColumn
rttMplsVpnMonReactActionType = _RttMplsVpnMonReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 5),
    _RttMplsVpnMonReactActionType_Type()
)
rttMplsVpnMonReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactActionType.setStatus("current")


class _RttMplsVpnMonReactLpdNotifyType_Type(Integer32):
    """Custom type rttMplsVpnMonReactLpdNotifyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lpdAll", 4),
          ("lpdGroupStatus", 3),
          ("lpdPathDiscovery", 2),
          ("none", 1))
    )


_RttMplsVpnMonReactLpdNotifyType_Type.__name__ = "Integer32"
_RttMplsVpnMonReactLpdNotifyType_Object = MibTableColumn
rttMplsVpnMonReactLpdNotifyType = _RttMplsVpnMonReactLpdNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 6),
    _RttMplsVpnMonReactLpdNotifyType_Type()
)
rttMplsVpnMonReactLpdNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactLpdNotifyType.setStatus("current")


class _RttMplsVpnMonReactLpdRetryCount_Type(Integer32):
    """Custom type rttMplsVpnMonReactLpdRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMplsVpnMonReactLpdRetryCount_Type.__name__ = "Integer32"
_RttMplsVpnMonReactLpdRetryCount_Object = MibTableColumn
rttMplsVpnMonReactLpdRetryCount = _RttMplsVpnMonReactLpdRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 18, 1, 7),
    _RttMplsVpnMonReactLpdRetryCount_Type()
)
rttMplsVpnMonReactLpdRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactLpdRetryCount.setStatus("current")
if mibBuilder.loadTexts:
    rttMplsVpnMonReactLpdRetryCount.setUnits("attempts")
_RttMonReactTable_Object = MibTable
rttMonReactTable = _RttMonReactTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19)
)
if mibBuilder.loadTexts:
    rttMonReactTable.setStatus("current")
_RttMonReactEntry_Object = MibTableRow
rttMonReactEntry = _RttMonReactEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1)
)
rttMonReactEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonReactConfigIndex"),
)
if mibBuilder.loadTexts:
    rttMonReactEntry.setStatus("current")


class _RttMonReactConfigIndex_Type(Integer32):
    """Custom type rttMonReactConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonReactConfigIndex_Type.__name__ = "Integer32"
_RttMonReactConfigIndex_Object = MibTableColumn
rttMonReactConfigIndex = _RttMonReactConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 1),
    _RttMonReactConfigIndex_Type()
)
rttMonReactConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonReactConfigIndex.setStatus("current")
_RttMonReactVar_Type = RttMonReactVar
_RttMonReactVar_Object = MibTableColumn
rttMonReactVar = _RttMonReactVar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 2),
    _RttMonReactVar_Type()
)
rttMonReactVar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactVar.setStatus("current")


class _RttMonReactThresholdType_Type(Integer32):
    """Custom type rttMonReactThresholdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("average", 5),
          ("consecutive", 3),
          ("immediate", 2),
          ("never", 1),
          ("xOfy", 4))
    )


_RttMonReactThresholdType_Type.__name__ = "Integer32"
_RttMonReactThresholdType_Object = MibTableColumn
rttMonReactThresholdType = _RttMonReactThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 3),
    _RttMonReactThresholdType_Type()
)
rttMonReactThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactThresholdType.setStatus("current")


class _RttMonReactActionType_Type(Integer32):
    """Custom type rttMonReactActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("trapAndTrigger", 4),
          ("trapOnly", 2),
          ("triggerOnly", 3))
    )


_RttMonReactActionType_Type.__name__ = "Integer32"
_RttMonReactActionType_Object = MibTableColumn
rttMonReactActionType = _RttMonReactActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 4),
    _RttMonReactActionType_Type()
)
rttMonReactActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactActionType.setStatus("current")


class _RttMonReactThresholdRising_Type(Integer32):
    """Custom type rttMonReactThresholdRising based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonReactThresholdRising_Type.__name__ = "Integer32"
_RttMonReactThresholdRising_Object = MibTableColumn
rttMonReactThresholdRising = _RttMonReactThresholdRising_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 5),
    _RttMonReactThresholdRising_Type()
)
rttMonReactThresholdRising.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactThresholdRising.setStatus("current")


class _RttMonReactThresholdFalling_Type(Integer32):
    """Custom type rttMonReactThresholdFalling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonReactThresholdFalling_Type.__name__ = "Integer32"
_RttMonReactThresholdFalling_Object = MibTableColumn
rttMonReactThresholdFalling = _RttMonReactThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 6),
    _RttMonReactThresholdFalling_Type()
)
rttMonReactThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactThresholdFalling.setStatus("current")


class _RttMonReactThresholdCountX_Type(Integer32):
    """Custom type rttMonReactThresholdCountX based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactThresholdCountX_Type.__name__ = "Integer32"
_RttMonReactThresholdCountX_Object = MibTableColumn
rttMonReactThresholdCountX = _RttMonReactThresholdCountX_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 7),
    _RttMonReactThresholdCountX_Type()
)
rttMonReactThresholdCountX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactThresholdCountX.setStatus("current")


class _RttMonReactThresholdCountY_Type(Integer32):
    """Custom type rttMonReactThresholdCountY based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactThresholdCountY_Type.__name__ = "Integer32"
_RttMonReactThresholdCountY_Object = MibTableColumn
rttMonReactThresholdCountY = _RttMonReactThresholdCountY_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 8),
    _RttMonReactThresholdCountY_Type()
)
rttMonReactThresholdCountY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactThresholdCountY.setStatus("current")


class _RttMonReactValue_Type(Integer32):
    """Custom type rttMonReactValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonReactValue_Type.__name__ = "Integer32"
_RttMonReactValue_Object = MibTableColumn
rttMonReactValue = _RttMonReactValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 9),
    _RttMonReactValue_Type()
)
rttMonReactValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonReactValue.setStatus("current")


class _RttMonReactOccurred_Type(TruthValue):
    """Custom type rttMonReactOccurred based on TruthValue"""


_RttMonReactOccurred_Object = MibTableColumn
rttMonReactOccurred = _RttMonReactOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 10),
    _RttMonReactOccurred_Type()
)
rttMonReactOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonReactOccurred.setStatus("current")
_RttMonReactStatus_Type = RowStatus
_RttMonReactStatus_Object = MibTableColumn
rttMonReactStatus = _RttMonReactStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 19, 1, 11),
    _RttMonReactStatus_Type()
)
rttMonReactStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactStatus.setStatus("current")
_RttMonGeneratedOperTable_Object = MibTable
rttMonGeneratedOperTable = _RttMonGeneratedOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 20)
)
if mibBuilder.loadTexts:
    rttMonGeneratedOperTable.setStatus("current")
_RttMonGeneratedOperEntry_Object = MibTableRow
rttMonGeneratedOperEntry = _RttMonGeneratedOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 20, 1)
)
rttMonGeneratedOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonGeneratedOperRespIpAddrType"),
    (0, "CISCO-RTTMON-MIB", "rttMonGeneratedOperRespIpAddr"),
)
if mibBuilder.loadTexts:
    rttMonGeneratedOperEntry.setStatus("current")
_RttMonGeneratedOperRespIpAddrType_Type = InetAddressType
_RttMonGeneratedOperRespIpAddrType_Object = MibTableColumn
rttMonGeneratedOperRespIpAddrType = _RttMonGeneratedOperRespIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 20, 1, 1),
    _RttMonGeneratedOperRespIpAddrType_Type()
)
rttMonGeneratedOperRespIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonGeneratedOperRespIpAddrType.setStatus("current")
_RttMonGeneratedOperRespIpAddr_Type = InetAddress
_RttMonGeneratedOperRespIpAddr_Object = MibTableColumn
rttMonGeneratedOperRespIpAddr = _RttMonGeneratedOperRespIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 20, 1, 2),
    _RttMonGeneratedOperRespIpAddr_Type()
)
rttMonGeneratedOperRespIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonGeneratedOperRespIpAddr.setStatus("current")


class _RttMonGeneratedOperCtrlAdminIndex_Type(Unsigned32):
    """Custom type rttMonGeneratedOperCtrlAdminIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonGeneratedOperCtrlAdminIndex_Type.__name__ = "Unsigned32"
_RttMonGeneratedOperCtrlAdminIndex_Object = MibTableColumn
rttMonGeneratedOperCtrlAdminIndex = _RttMonGeneratedOperCtrlAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 20, 1, 3),
    _RttMonGeneratedOperCtrlAdminIndex_Type()
)
rttMonGeneratedOperCtrlAdminIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonGeneratedOperCtrlAdminIndex.setStatus("current")
_RttMonStats_ObjectIdentity = ObjectIdentity
rttMonStats = _RttMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3)
)
_RttMonStatsCaptureTable_Object = MibTable
rttMonStatsCaptureTable = _RttMonStatsCaptureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rttMonStatsCaptureTable.setStatus("current")
_RttMonStatsCaptureEntry_Object = MibTableRow
rttMonStatsCaptureEntry = _RttMonStatsCaptureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1)
)
rttMonStatsCaptureEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCapturePathIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureHopIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureDistIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsCaptureEntry.setStatus("current")
_RttMonStatsCaptureStartTimeIndex_Type = TimeStamp
_RttMonStatsCaptureStartTimeIndex_Object = MibTableColumn
rttMonStatsCaptureStartTimeIndex = _RttMonStatsCaptureStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 1),
    _RttMonStatsCaptureStartTimeIndex_Type()
)
rttMonStatsCaptureStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureStartTimeIndex.setStatus("current")


class _RttMonStatsCapturePathIndex_Type(Integer32):
    """Custom type rttMonStatsCapturePathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RttMonStatsCapturePathIndex_Type.__name__ = "Integer32"
_RttMonStatsCapturePathIndex_Object = MibTableColumn
rttMonStatsCapturePathIndex = _RttMonStatsCapturePathIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 2),
    _RttMonStatsCapturePathIndex_Type()
)
rttMonStatsCapturePathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCapturePathIndex.setStatus("current")


class _RttMonStatsCaptureHopIndex_Type(Integer32):
    """Custom type rttMonStatsCaptureHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonStatsCaptureHopIndex_Type.__name__ = "Integer32"
_RttMonStatsCaptureHopIndex_Object = MibTableColumn
rttMonStatsCaptureHopIndex = _RttMonStatsCaptureHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 3),
    _RttMonStatsCaptureHopIndex_Type()
)
rttMonStatsCaptureHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureHopIndex.setStatus("current")


class _RttMonStatsCaptureDistIndex_Type(Integer32):
    """Custom type rttMonStatsCaptureDistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RttMonStatsCaptureDistIndex_Type.__name__ = "Integer32"
_RttMonStatsCaptureDistIndex_Object = MibTableColumn
rttMonStatsCaptureDistIndex = _RttMonStatsCaptureDistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 4),
    _RttMonStatsCaptureDistIndex_Type()
)
rttMonStatsCaptureDistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureDistIndex.setStatus("current")


class _RttMonStatsCaptureCompletions_Type(Integer32):
    """Custom type rttMonStatsCaptureCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCaptureCompletions_Type.__name__ = "Integer32"
_RttMonStatsCaptureCompletions_Object = MibTableColumn
rttMonStatsCaptureCompletions = _RttMonStatsCaptureCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 5),
    _RttMonStatsCaptureCompletions_Type()
)
rttMonStatsCaptureCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletions.setStatus("current")


class _RttMonStatsCaptureOverThresholds_Type(Integer32):
    """Custom type rttMonStatsCaptureOverThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCaptureOverThresholds_Type.__name__ = "Integer32"
_RttMonStatsCaptureOverThresholds_Object = MibTableColumn
rttMonStatsCaptureOverThresholds = _RttMonStatsCaptureOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 6),
    _RttMonStatsCaptureOverThresholds_Type()
)
rttMonStatsCaptureOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureOverThresholds.setStatus("current")
_RttMonStatsCaptureSumCompletionTime_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime = _RttMonStatsCaptureSumCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 7),
    _RttMonStatsCaptureSumCompletionTime_Type()
)
rttMonStatsCaptureSumCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime.setUnits("milliseconds")
_RttMonStatsCaptureSumCompletionTime2Low_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime2Low_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime2Low = _RttMonStatsCaptureSumCompletionTime2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 8),
    _RttMonStatsCaptureSumCompletionTime2Low_Type()
)
rttMonStatsCaptureSumCompletionTime2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime2Low.setStatus("current")
_RttMonStatsCaptureSumCompletionTime2High_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime2High_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime2High = _RttMonStatsCaptureSumCompletionTime2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 9),
    _RttMonStatsCaptureSumCompletionTime2High_Type()
)
rttMonStatsCaptureSumCompletionTime2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime2High.setStatus("current")
_RttMonStatsCaptureCompletionTimeMax_Type = Gauge32
_RttMonStatsCaptureCompletionTimeMax_Object = MibTableColumn
rttMonStatsCaptureCompletionTimeMax = _RttMonStatsCaptureCompletionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 10),
    _RttMonStatsCaptureCompletionTimeMax_Type()
)
rttMonStatsCaptureCompletionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMax.setUnits("milliseconds")
_RttMonStatsCaptureCompletionTimeMin_Type = Gauge32
_RttMonStatsCaptureCompletionTimeMin_Object = MibTableColumn
rttMonStatsCaptureCompletionTimeMin = _RttMonStatsCaptureCompletionTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 11),
    _RttMonStatsCaptureCompletionTimeMin_Type()
)
rttMonStatsCaptureCompletionTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMin.setUnits("milliseconds")
_RttMonStatsCollectTable_Object = MibTable
rttMonStatsCollectTable = _RttMonStatsCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rttMonStatsCollectTable.setStatus("current")
_RttMonStatsCollectEntry_Object = MibTableRow
rttMonStatsCollectEntry = _RttMonStatsCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1)
)
rttMonStatsCollectEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCapturePathIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureHopIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsCollectEntry.setStatus("current")


class _RttMonStatsCollectNumDisconnects_Type(Integer32):
    """Custom type rttMonStatsCollectNumDisconnects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectNumDisconnects_Type.__name__ = "Integer32"
_RttMonStatsCollectNumDisconnects_Object = MibTableColumn
rttMonStatsCollectNumDisconnects = _RttMonStatsCollectNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 1),
    _RttMonStatsCollectNumDisconnects_Type()
)
rttMonStatsCollectNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectNumDisconnects.setStatus("current")


class _RttMonStatsCollectTimeouts_Type(Integer32):
    """Custom type rttMonStatsCollectTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectTimeouts_Type.__name__ = "Integer32"
_RttMonStatsCollectTimeouts_Object = MibTableColumn
rttMonStatsCollectTimeouts = _RttMonStatsCollectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 2),
    _RttMonStatsCollectTimeouts_Type()
)
rttMonStatsCollectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectTimeouts.setStatus("current")


class _RttMonStatsCollectBusies_Type(Integer32):
    """Custom type rttMonStatsCollectBusies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectBusies_Type.__name__ = "Integer32"
_RttMonStatsCollectBusies_Object = MibTableColumn
rttMonStatsCollectBusies = _RttMonStatsCollectBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 3),
    _RttMonStatsCollectBusies_Type()
)
rttMonStatsCollectBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectBusies.setStatus("current")


class _RttMonStatsCollectNoConnections_Type(Integer32):
    """Custom type rttMonStatsCollectNoConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectNoConnections_Type.__name__ = "Integer32"
_RttMonStatsCollectNoConnections_Object = MibTableColumn
rttMonStatsCollectNoConnections = _RttMonStatsCollectNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 4),
    _RttMonStatsCollectNoConnections_Type()
)
rttMonStatsCollectNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectNoConnections.setStatus("current")


class _RttMonStatsCollectDrops_Type(Integer32):
    """Custom type rttMonStatsCollectDrops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectDrops_Type.__name__ = "Integer32"
_RttMonStatsCollectDrops_Object = MibTableColumn
rttMonStatsCollectDrops = _RttMonStatsCollectDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 5),
    _RttMonStatsCollectDrops_Type()
)
rttMonStatsCollectDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectDrops.setStatus("current")


class _RttMonStatsCollectSequenceErrors_Type(Integer32):
    """Custom type rttMonStatsCollectSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectSequenceErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectSequenceErrors_Object = MibTableColumn
rttMonStatsCollectSequenceErrors = _RttMonStatsCollectSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 6),
    _RttMonStatsCollectSequenceErrors_Type()
)
rttMonStatsCollectSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectSequenceErrors.setStatus("current")


class _RttMonStatsCollectVerifyErrors_Type(Integer32):
    """Custom type rttMonStatsCollectVerifyErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectVerifyErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectVerifyErrors_Object = MibTableColumn
rttMonStatsCollectVerifyErrors = _RttMonStatsCollectVerifyErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 7),
    _RttMonStatsCollectVerifyErrors_Type()
)
rttMonStatsCollectVerifyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectVerifyErrors.setStatus("current")
_RttMonStatsCollectAddress_Type = RttMonTargetAddress
_RttMonStatsCollectAddress_Object = MibTableColumn
rttMonStatsCollectAddress = _RttMonStatsCollectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 8),
    _RttMonStatsCollectAddress_Type()
)
rttMonStatsCollectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectAddress.setStatus("current")


class _RttMonControlEnableErrors_Type(Integer32):
    """Custom type rttMonControlEnableErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonControlEnableErrors_Type.__name__ = "Integer32"
_RttMonControlEnableErrors_Object = MibTableColumn
rttMonControlEnableErrors = _RttMonControlEnableErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 9),
    _RttMonControlEnableErrors_Type()
)
rttMonControlEnableErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonControlEnableErrors.setStatus("deprecated")


class _RttMonStatsRetrieveErrors_Type(Integer32):
    """Custom type rttMonStatsRetrieveErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsRetrieveErrors_Type.__name__ = "Integer32"
_RttMonStatsRetrieveErrors_Object = MibTableColumn
rttMonStatsRetrieveErrors = _RttMonStatsRetrieveErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 10),
    _RttMonStatsRetrieveErrors_Type()
)
rttMonStatsRetrieveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsRetrieveErrors.setStatus("deprecated")


class _RttMonStatsCollectCtrlEnErrors_Type(Integer32):
    """Custom type rttMonStatsCollectCtrlEnErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectCtrlEnErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectCtrlEnErrors_Object = MibTableColumn
rttMonStatsCollectCtrlEnErrors = _RttMonStatsCollectCtrlEnErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 11),
    _RttMonStatsCollectCtrlEnErrors_Type()
)
rttMonStatsCollectCtrlEnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectCtrlEnErrors.setStatus("current")


class _RttMonStatsCollectRetrieveErrors_Type(Integer32):
    """Custom type rttMonStatsCollectRetrieveErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectRetrieveErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectRetrieveErrors_Object = MibTableColumn
rttMonStatsCollectRetrieveErrors = _RttMonStatsCollectRetrieveErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 12),
    _RttMonStatsCollectRetrieveErrors_Type()
)
rttMonStatsCollectRetrieveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectRetrieveErrors.setStatus("current")
_RttMonStatsTotalsTable_Object = MibTable
rttMonStatsTotalsTable = _RttMonStatsTotalsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rttMonStatsTotalsTable.setStatus("current")
_RttMonStatsTotalsEntry_Object = MibTableRow
rttMonStatsTotalsEntry = _RttMonStatsTotalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1)
)
rttMonStatsTotalsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsTotalsEntry.setStatus("current")
_RttMonStatsTotalsElapsedTime_Type = TimeInterval
_RttMonStatsTotalsElapsedTime_Object = MibTableColumn
rttMonStatsTotalsElapsedTime = _RttMonStatsTotalsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1, 1),
    _RttMonStatsTotalsElapsedTime_Type()
)
rttMonStatsTotalsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsTotalsElapsedTime.setStatus("current")


class _RttMonStatsTotalsInitiations_Type(Integer32):
    """Custom type rttMonStatsTotalsInitiations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsTotalsInitiations_Type.__name__ = "Integer32"
_RttMonStatsTotalsInitiations_Object = MibTableColumn
rttMonStatsTotalsInitiations = _RttMonStatsTotalsInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1, 2),
    _RttMonStatsTotalsInitiations_Type()
)
rttMonStatsTotalsInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsTotalsInitiations.setStatus("current")
_RttMonHTTPStatsTable_Object = MibTable
rttMonHTTPStatsTable = _RttMonHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4)
)
if mibBuilder.loadTexts:
    rttMonHTTPStatsTable.setStatus("current")
_RttMonHTTPStatsEntry_Object = MibTableRow
rttMonHTTPStatsEntry = _RttMonHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1)
)
rttMonHTTPStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHTTPStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonHTTPStatsEntry.setStatus("current")
_RttMonHTTPStatsStartTimeIndex_Type = TimeStamp
_RttMonHTTPStatsStartTimeIndex_Object = MibTableColumn
rttMonHTTPStatsStartTimeIndex = _RttMonHTTPStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 1),
    _RttMonHTTPStatsStartTimeIndex_Type()
)
rttMonHTTPStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHTTPStatsStartTimeIndex.setStatus("current")
_RttMonHTTPStatsCompletions_Type = Counter32
_RttMonHTTPStatsCompletions_Object = MibTableColumn
rttMonHTTPStatsCompletions = _RttMonHTTPStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 2),
    _RttMonHTTPStatsCompletions_Type()
)
rttMonHTTPStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsCompletions.setStatus("current")
_RttMonHTTPStatsOverThresholds_Type = Counter32
_RttMonHTTPStatsOverThresholds_Object = MibTableColumn
rttMonHTTPStatsOverThresholds = _RttMonHTTPStatsOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 3),
    _RttMonHTTPStatsOverThresholds_Type()
)
rttMonHTTPStatsOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsOverThresholds.setStatus("current")
_RttMonHTTPStatsRTTSum_Type = Counter32
_RttMonHTTPStatsRTTSum_Object = MibTableColumn
rttMonHTTPStatsRTTSum = _RttMonHTTPStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 4),
    _RttMonHTTPStatsRTTSum_Type()
)
rttMonHTTPStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum.setStatus("current")
_RttMonHTTPStatsRTTSum2Low_Type = Counter32
_RttMonHTTPStatsRTTSum2Low_Object = MibTableColumn
rttMonHTTPStatsRTTSum2Low = _RttMonHTTPStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 5),
    _RttMonHTTPStatsRTTSum2Low_Type()
)
rttMonHTTPStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum2Low.setStatus("current")
_RttMonHTTPStatsRTTSum2High_Type = Counter32
_RttMonHTTPStatsRTTSum2High_Object = MibTableColumn
rttMonHTTPStatsRTTSum2High = _RttMonHTTPStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 6),
    _RttMonHTTPStatsRTTSum2High_Type()
)
rttMonHTTPStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum2High.setStatus("current")
_RttMonHTTPStatsRTTMin_Type = Gauge32
_RttMonHTTPStatsRTTMin_Object = MibTableColumn
rttMonHTTPStatsRTTMin = _RttMonHTTPStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 7),
    _RttMonHTTPStatsRTTMin_Type()
)
rttMonHTTPStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTMin.setStatus("current")
_RttMonHTTPStatsRTTMax_Type = Gauge32
_RttMonHTTPStatsRTTMax_Object = MibTableColumn
rttMonHTTPStatsRTTMax = _RttMonHTTPStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 8),
    _RttMonHTTPStatsRTTMax_Type()
)
rttMonHTTPStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTMax.setUnits("milliseconds")
_RttMonHTTPStatsDNSRTTSum_Type = Counter32
_RttMonHTTPStatsDNSRTTSum_Object = MibTableColumn
rttMonHTTPStatsDNSRTTSum = _RttMonHTTPStatsDNSRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 9),
    _RttMonHTTPStatsDNSRTTSum_Type()
)
rttMonHTTPStatsDNSRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSRTTSum.setStatus("current")
_RttMonHTTPStatsTCPConnectRTTSum_Type = Counter32
_RttMonHTTPStatsTCPConnectRTTSum_Object = MibTableColumn
rttMonHTTPStatsTCPConnectRTTSum = _RttMonHTTPStatsTCPConnectRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 10),
    _RttMonHTTPStatsTCPConnectRTTSum_Type()
)
rttMonHTTPStatsTCPConnectRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTCPConnectRTTSum.setStatus("current")
_RttMonHTTPStatsTransactionRTTSum_Type = Counter32
_RttMonHTTPStatsTransactionRTTSum_Object = MibTableColumn
rttMonHTTPStatsTransactionRTTSum = _RttMonHTTPStatsTransactionRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 11),
    _RttMonHTTPStatsTransactionRTTSum_Type()
)
rttMonHTTPStatsTransactionRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTransactionRTTSum.setStatus("current")
_RttMonHTTPStatsMessageBodyOctetsSum_Type = Counter32
_RttMonHTTPStatsMessageBodyOctetsSum_Object = MibTableColumn
rttMonHTTPStatsMessageBodyOctetsSum = _RttMonHTTPStatsMessageBodyOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 12),
    _RttMonHTTPStatsMessageBodyOctetsSum_Type()
)
rttMonHTTPStatsMessageBodyOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsMessageBodyOctetsSum.setStatus("current")
_RttMonHTTPStatsDNSServerTimeout_Type = Counter32
_RttMonHTTPStatsDNSServerTimeout_Object = MibTableColumn
rttMonHTTPStatsDNSServerTimeout = _RttMonHTTPStatsDNSServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 13),
    _RttMonHTTPStatsDNSServerTimeout_Type()
)
rttMonHTTPStatsDNSServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSServerTimeout.setStatus("current")
_RttMonHTTPStatsTCPConnectTimeout_Type = Counter32
_RttMonHTTPStatsTCPConnectTimeout_Object = MibTableColumn
rttMonHTTPStatsTCPConnectTimeout = _RttMonHTTPStatsTCPConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 14),
    _RttMonHTTPStatsTCPConnectTimeout_Type()
)
rttMonHTTPStatsTCPConnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTCPConnectTimeout.setStatus("current")
_RttMonHTTPStatsTransactionTimeout_Type = Counter32
_RttMonHTTPStatsTransactionTimeout_Object = MibTableColumn
rttMonHTTPStatsTransactionTimeout = _RttMonHTTPStatsTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 15),
    _RttMonHTTPStatsTransactionTimeout_Type()
)
rttMonHTTPStatsTransactionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTransactionTimeout.setStatus("current")
_RttMonHTTPStatsDNSQueryError_Type = Counter32
_RttMonHTTPStatsDNSQueryError_Object = MibTableColumn
rttMonHTTPStatsDNSQueryError = _RttMonHTTPStatsDNSQueryError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 16),
    _RttMonHTTPStatsDNSQueryError_Type()
)
rttMonHTTPStatsDNSQueryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSQueryError.setStatus("current")
_RttMonHTTPStatsHTTPError_Type = Counter32
_RttMonHTTPStatsHTTPError_Object = MibTableColumn
rttMonHTTPStatsHTTPError = _RttMonHTTPStatsHTTPError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 17),
    _RttMonHTTPStatsHTTPError_Type()
)
rttMonHTTPStatsHTTPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsHTTPError.setStatus("current")
_RttMonHTTPStatsError_Type = Counter32
_RttMonHTTPStatsError_Object = MibTableColumn
rttMonHTTPStatsError = _RttMonHTTPStatsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 18),
    _RttMonHTTPStatsError_Type()
)
rttMonHTTPStatsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsError.setStatus("current")
_RttMonHTTPStatsBusies_Type = Counter32
_RttMonHTTPStatsBusies_Object = MibTableColumn
rttMonHTTPStatsBusies = _RttMonHTTPStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 19),
    _RttMonHTTPStatsBusies_Type()
)
rttMonHTTPStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsBusies.setStatus("current")
_RttMonJitterStatsTable_Object = MibTable
rttMonJitterStatsTable = _RttMonJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5)
)
if mibBuilder.loadTexts:
    rttMonJitterStatsTable.setStatus("current")
_RttMonJitterStatsEntry_Object = MibTableRow
rttMonJitterStatsEntry = _RttMonJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1)
)
rttMonJitterStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonJitterStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonJitterStatsEntry.setStatus("current")
_RttMonJitterStatsStartTimeIndex_Type = TimeStamp
_RttMonJitterStatsStartTimeIndex_Object = MibTableColumn
rttMonJitterStatsStartTimeIndex = _RttMonJitterStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 1),
    _RttMonJitterStatsStartTimeIndex_Type()
)
rttMonJitterStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonJitterStatsStartTimeIndex.setStatus("current")
_RttMonJitterStatsCompletions_Type = Counter32
_RttMonJitterStatsCompletions_Object = MibTableColumn
rttMonJitterStatsCompletions = _RttMonJitterStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 2),
    _RttMonJitterStatsCompletions_Type()
)
rttMonJitterStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsCompletions.setStatus("current")
_RttMonJitterStatsOverThresholds_Type = Counter32
_RttMonJitterStatsOverThresholds_Object = MibTableColumn
rttMonJitterStatsOverThresholds = _RttMonJitterStatsOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 3),
    _RttMonJitterStatsOverThresholds_Type()
)
rttMonJitterStatsOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOverThresholds.setStatus("current")
_RttMonJitterStatsNumOfRTT_Type = Counter32
_RttMonJitterStatsNumOfRTT_Object = MibTableColumn
rttMonJitterStatsNumOfRTT = _RttMonJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 4),
    _RttMonJitterStatsNumOfRTT_Type()
)
rttMonJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfRTT.setStatus("current")
_RttMonJitterStatsRTTSum_Type = Counter32
_RttMonJitterStatsRTTSum_Object = MibTableColumn
rttMonJitterStatsRTTSum = _RttMonJitterStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 5),
    _RttMonJitterStatsRTTSum_Type()
)
rttMonJitterStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum.setStatus("current")
_RttMonJitterStatsRTTSum2Low_Type = Counter32
_RttMonJitterStatsRTTSum2Low_Object = MibTableColumn
rttMonJitterStatsRTTSum2Low = _RttMonJitterStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 6),
    _RttMonJitterStatsRTTSum2Low_Type()
)
rttMonJitterStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum2Low.setStatus("current")
_RttMonJitterStatsRTTSum2High_Type = Counter32
_RttMonJitterStatsRTTSum2High_Object = MibTableColumn
rttMonJitterStatsRTTSum2High = _RttMonJitterStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 7),
    _RttMonJitterStatsRTTSum2High_Type()
)
rttMonJitterStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum2High.setStatus("current")
_RttMonJitterStatsRTTMin_Type = Gauge32
_RttMonJitterStatsRTTMin_Object = MibTableColumn
rttMonJitterStatsRTTMin = _RttMonJitterStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 8),
    _RttMonJitterStatsRTTMin_Type()
)
rttMonJitterStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTMin.setStatus("current")
_RttMonJitterStatsRTTMax_Type = Gauge32
_RttMonJitterStatsRTTMax_Object = MibTableColumn
rttMonJitterStatsRTTMax = _RttMonJitterStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 9),
    _RttMonJitterStatsRTTMax_Type()
)
rttMonJitterStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTMax.setStatus("current")
_RttMonJitterStatsMinOfPositivesSD_Type = Gauge32
_RttMonJitterStatsMinOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsMinOfPositivesSD = _RttMonJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 10),
    _RttMonJitterStatsMinOfPositivesSD_Type()
)
rttMonJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfPositivesSD.setStatus("current")
_RttMonJitterStatsMaxOfPositivesSD_Type = Gauge32
_RttMonJitterStatsMaxOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsMaxOfPositivesSD = _RttMonJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 11),
    _RttMonJitterStatsMaxOfPositivesSD_Type()
)
rttMonJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfPositivesSD.setStatus("current")
_RttMonJitterStatsNumOfPositivesSD_Type = Counter32
_RttMonJitterStatsNumOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsNumOfPositivesSD = _RttMonJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 12),
    _RttMonJitterStatsNumOfPositivesSD_Type()
)
rttMonJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfPositivesSD.setStatus("current")
_RttMonJitterStatsSumOfPositivesSD_Type = Counter32
_RttMonJitterStatsSumOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsSumOfPositivesSD = _RttMonJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 13),
    _RttMonJitterStatsSumOfPositivesSD_Type()
)
rttMonJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfPositivesSD.setStatus("current")
_RttMonJitterStatsSum2PositivesSDLow_Type = Counter32
_RttMonJitterStatsSum2PositivesSDLow_Object = MibTableColumn
rttMonJitterStatsSum2PositivesSDLow = _RttMonJitterStatsSum2PositivesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 14),
    _RttMonJitterStatsSum2PositivesSDLow_Type()
)
rttMonJitterStatsSum2PositivesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesSDLow.setStatus("current")
_RttMonJitterStatsSum2PositivesSDHigh_Type = Counter32
_RttMonJitterStatsSum2PositivesSDHigh_Object = MibTableColumn
rttMonJitterStatsSum2PositivesSDHigh = _RttMonJitterStatsSum2PositivesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 15),
    _RttMonJitterStatsSum2PositivesSDHigh_Type()
)
rttMonJitterStatsSum2PositivesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesSDHigh.setStatus("current")
_RttMonJitterStatsMinOfNegativesSD_Type = Gauge32
_RttMonJitterStatsMinOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsMinOfNegativesSD = _RttMonJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 16),
    _RttMonJitterStatsMinOfNegativesSD_Type()
)
rttMonJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfNegativesSD.setStatus("current")
_RttMonJitterStatsMaxOfNegativesSD_Type = Gauge32
_RttMonJitterStatsMaxOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsMaxOfNegativesSD = _RttMonJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 17),
    _RttMonJitterStatsMaxOfNegativesSD_Type()
)
rttMonJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfNegativesSD.setStatus("current")
_RttMonJitterStatsNumOfNegativesSD_Type = Counter32
_RttMonJitterStatsNumOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsNumOfNegativesSD = _RttMonJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 18),
    _RttMonJitterStatsNumOfNegativesSD_Type()
)
rttMonJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfNegativesSD.setStatus("current")
_RttMonJitterStatsSumOfNegativesSD_Type = Counter32
_RttMonJitterStatsSumOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsSumOfNegativesSD = _RttMonJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 19),
    _RttMonJitterStatsSumOfNegativesSD_Type()
)
rttMonJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfNegativesSD.setStatus("current")
_RttMonJitterStatsSum2NegativesSDLow_Type = Counter32
_RttMonJitterStatsSum2NegativesSDLow_Object = MibTableColumn
rttMonJitterStatsSum2NegativesSDLow = _RttMonJitterStatsSum2NegativesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 20),
    _RttMonJitterStatsSum2NegativesSDLow_Type()
)
rttMonJitterStatsSum2NegativesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesSDLow.setStatus("current")
_RttMonJitterStatsSum2NegativesSDHigh_Type = Counter32
_RttMonJitterStatsSum2NegativesSDHigh_Object = MibTableColumn
rttMonJitterStatsSum2NegativesSDHigh = _RttMonJitterStatsSum2NegativesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 21),
    _RttMonJitterStatsSum2NegativesSDHigh_Type()
)
rttMonJitterStatsSum2NegativesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesSDHigh.setStatus("current")
_RttMonJitterStatsMinOfPositivesDS_Type = Gauge32
_RttMonJitterStatsMinOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsMinOfPositivesDS = _RttMonJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 22),
    _RttMonJitterStatsMinOfPositivesDS_Type()
)
rttMonJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfPositivesDS.setStatus("current")
_RttMonJitterStatsMaxOfPositivesDS_Type = Gauge32
_RttMonJitterStatsMaxOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsMaxOfPositivesDS = _RttMonJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 23),
    _RttMonJitterStatsMaxOfPositivesDS_Type()
)
rttMonJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfPositivesDS.setStatus("current")
_RttMonJitterStatsNumOfPositivesDS_Type = Counter32
_RttMonJitterStatsNumOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsNumOfPositivesDS = _RttMonJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 24),
    _RttMonJitterStatsNumOfPositivesDS_Type()
)
rttMonJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfPositivesDS.setStatus("current")
_RttMonJitterStatsSumOfPositivesDS_Type = Counter32
_RttMonJitterStatsSumOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsSumOfPositivesDS = _RttMonJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 25),
    _RttMonJitterStatsSumOfPositivesDS_Type()
)
rttMonJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfPositivesDS.setStatus("current")
_RttMonJitterStatsSum2PositivesDSLow_Type = Counter32
_RttMonJitterStatsSum2PositivesDSLow_Object = MibTableColumn
rttMonJitterStatsSum2PositivesDSLow = _RttMonJitterStatsSum2PositivesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 26),
    _RttMonJitterStatsSum2PositivesDSLow_Type()
)
rttMonJitterStatsSum2PositivesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesDSLow.setStatus("current")
_RttMonJitterStatsSum2PositivesDSHigh_Type = Counter32
_RttMonJitterStatsSum2PositivesDSHigh_Object = MibTableColumn
rttMonJitterStatsSum2PositivesDSHigh = _RttMonJitterStatsSum2PositivesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 27),
    _RttMonJitterStatsSum2PositivesDSHigh_Type()
)
rttMonJitterStatsSum2PositivesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesDSHigh.setStatus("current")
_RttMonJitterStatsMinOfNegativesDS_Type = Gauge32
_RttMonJitterStatsMinOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsMinOfNegativesDS = _RttMonJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 28),
    _RttMonJitterStatsMinOfNegativesDS_Type()
)
rttMonJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfNegativesDS.setStatus("current")
_RttMonJitterStatsMaxOfNegativesDS_Type = Gauge32
_RttMonJitterStatsMaxOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsMaxOfNegativesDS = _RttMonJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 29),
    _RttMonJitterStatsMaxOfNegativesDS_Type()
)
rttMonJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfNegativesDS.setStatus("current")
_RttMonJitterStatsNumOfNegativesDS_Type = Counter32
_RttMonJitterStatsNumOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsNumOfNegativesDS = _RttMonJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 30),
    _RttMonJitterStatsNumOfNegativesDS_Type()
)
rttMonJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfNegativesDS.setStatus("current")
_RttMonJitterStatsSumOfNegativesDS_Type = Counter32
_RttMonJitterStatsSumOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsSumOfNegativesDS = _RttMonJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 31),
    _RttMonJitterStatsSumOfNegativesDS_Type()
)
rttMonJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfNegativesDS.setStatus("current")
_RttMonJitterStatsSum2NegativesDSLow_Type = Counter32
_RttMonJitterStatsSum2NegativesDSLow_Object = MibTableColumn
rttMonJitterStatsSum2NegativesDSLow = _RttMonJitterStatsSum2NegativesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 32),
    _RttMonJitterStatsSum2NegativesDSLow_Type()
)
rttMonJitterStatsSum2NegativesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesDSLow.setStatus("current")
_RttMonJitterStatsSum2NegativesDSHigh_Type = Counter32
_RttMonJitterStatsSum2NegativesDSHigh_Object = MibTableColumn
rttMonJitterStatsSum2NegativesDSHigh = _RttMonJitterStatsSum2NegativesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 33),
    _RttMonJitterStatsSum2NegativesDSHigh_Type()
)
rttMonJitterStatsSum2NegativesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesDSHigh.setStatus("current")
_RttMonJitterStatsPacketLossSD_Type = Counter32
_RttMonJitterStatsPacketLossSD_Object = MibTableColumn
rttMonJitterStatsPacketLossSD = _RttMonJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 34),
    _RttMonJitterStatsPacketLossSD_Type()
)
rttMonJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLossSD.setStatus("current")
_RttMonJitterStatsPacketLossDS_Type = Counter32
_RttMonJitterStatsPacketLossDS_Object = MibTableColumn
rttMonJitterStatsPacketLossDS = _RttMonJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 35),
    _RttMonJitterStatsPacketLossDS_Type()
)
rttMonJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLossDS.setStatus("current")
_RttMonJitterStatsPacketOutOfSequence_Type = Counter32
_RttMonJitterStatsPacketOutOfSequence_Object = MibTableColumn
rttMonJitterStatsPacketOutOfSequence = _RttMonJitterStatsPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 36),
    _RttMonJitterStatsPacketOutOfSequence_Type()
)
rttMonJitterStatsPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketOutOfSequence.setStatus("current")
_RttMonJitterStatsPacketMIA_Type = Counter32
_RttMonJitterStatsPacketMIA_Object = MibTableColumn
rttMonJitterStatsPacketMIA = _RttMonJitterStatsPacketMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 37),
    _RttMonJitterStatsPacketMIA_Type()
)
rttMonJitterStatsPacketMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketMIA.setStatus("current")
_RttMonJitterStatsPacketLateArrival_Type = Counter32
_RttMonJitterStatsPacketLateArrival_Object = MibTableColumn
rttMonJitterStatsPacketLateArrival = _RttMonJitterStatsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 38),
    _RttMonJitterStatsPacketLateArrival_Type()
)
rttMonJitterStatsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLateArrival.setStatus("current")
_RttMonJitterStatsError_Type = Counter32
_RttMonJitterStatsError_Object = MibTableColumn
rttMonJitterStatsError = _RttMonJitterStatsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 39),
    _RttMonJitterStatsError_Type()
)
rttMonJitterStatsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsError.setStatus("current")
_RttMonJitterStatsBusies_Type = Counter32
_RttMonJitterStatsBusies_Object = MibTableColumn
rttMonJitterStatsBusies = _RttMonJitterStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 40),
    _RttMonJitterStatsBusies_Type()
)
rttMonJitterStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsBusies.setStatus("current")
_RttMonJitterStatsOWSumSD_Type = Counter32
_RttMonJitterStatsOWSumSD_Object = MibTableColumn
rttMonJitterStatsOWSumSD = _RttMonJitterStatsOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 41),
    _RttMonJitterStatsOWSumSD_Type()
)
rttMonJitterStatsOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSumSD.setStatus("current")
_RttMonJitterStatsOWSum2SDLow_Type = Counter32
_RttMonJitterStatsOWSum2SDLow_Object = MibTableColumn
rttMonJitterStatsOWSum2SDLow = _RttMonJitterStatsOWSum2SDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 42),
    _RttMonJitterStatsOWSum2SDLow_Type()
)
rttMonJitterStatsOWSum2SDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSum2SDLow.setStatus("current")
_RttMonJitterStatsOWSum2SDHigh_Type = Counter32
_RttMonJitterStatsOWSum2SDHigh_Object = MibTableColumn
rttMonJitterStatsOWSum2SDHigh = _RttMonJitterStatsOWSum2SDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 43),
    _RttMonJitterStatsOWSum2SDHigh_Type()
)
rttMonJitterStatsOWSum2SDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSum2SDHigh.setStatus("current")
_RttMonJitterStatsOWMinSD_Type = Counter32
_RttMonJitterStatsOWMinSD_Object = MibTableColumn
rttMonJitterStatsOWMinSD = _RttMonJitterStatsOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 44),
    _RttMonJitterStatsOWMinSD_Type()
)
rttMonJitterStatsOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMinSD.setStatus("deprecated")
_RttMonJitterStatsOWMaxSD_Type = Counter32
_RttMonJitterStatsOWMaxSD_Object = MibTableColumn
rttMonJitterStatsOWMaxSD = _RttMonJitterStatsOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 45),
    _RttMonJitterStatsOWMaxSD_Type()
)
rttMonJitterStatsOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMaxSD.setStatus("deprecated")
_RttMonJitterStatsOWSumDS_Type = Counter32
_RttMonJitterStatsOWSumDS_Object = MibTableColumn
rttMonJitterStatsOWSumDS = _RttMonJitterStatsOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 46),
    _RttMonJitterStatsOWSumDS_Type()
)
rttMonJitterStatsOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSumDS.setStatus("current")
_RttMonJitterStatsOWSum2DSLow_Type = Counter32
_RttMonJitterStatsOWSum2DSLow_Object = MibTableColumn
rttMonJitterStatsOWSum2DSLow = _RttMonJitterStatsOWSum2DSLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 47),
    _RttMonJitterStatsOWSum2DSLow_Type()
)
rttMonJitterStatsOWSum2DSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSum2DSLow.setStatus("current")
_RttMonJitterStatsOWSum2DSHigh_Type = Counter32
_RttMonJitterStatsOWSum2DSHigh_Object = MibTableColumn
rttMonJitterStatsOWSum2DSHigh = _RttMonJitterStatsOWSum2DSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 48),
    _RttMonJitterStatsOWSum2DSHigh_Type()
)
rttMonJitterStatsOWSum2DSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSum2DSHigh.setStatus("current")
_RttMonJitterStatsOWMinDS_Type = Counter32
_RttMonJitterStatsOWMinDS_Object = MibTableColumn
rttMonJitterStatsOWMinDS = _RttMonJitterStatsOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 49),
    _RttMonJitterStatsOWMinDS_Type()
)
rttMonJitterStatsOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMinDS.setStatus("deprecated")
_RttMonJitterStatsOWMaxDS_Type = Counter32
_RttMonJitterStatsOWMaxDS_Object = MibTableColumn
rttMonJitterStatsOWMaxDS = _RttMonJitterStatsOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 50),
    _RttMonJitterStatsOWMaxDS_Type()
)
rttMonJitterStatsOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMaxDS.setStatus("deprecated")
_RttMonJitterStatsNumOfOW_Type = Counter32
_RttMonJitterStatsNumOfOW_Object = MibTableColumn
rttMonJitterStatsNumOfOW = _RttMonJitterStatsNumOfOW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 51),
    _RttMonJitterStatsNumOfOW_Type()
)
rttMonJitterStatsNumOfOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfOW.setStatus("current")
_RttMonJitterStatsOWMinSDNew_Type = Gauge32
_RttMonJitterStatsOWMinSDNew_Object = MibTableColumn
rttMonJitterStatsOWMinSDNew = _RttMonJitterStatsOWMinSDNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 52),
    _RttMonJitterStatsOWMinSDNew_Type()
)
rttMonJitterStatsOWMinSDNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMinSDNew.setStatus("current")
_RttMonJitterStatsOWMaxSDNew_Type = Gauge32
_RttMonJitterStatsOWMaxSDNew_Object = MibTableColumn
rttMonJitterStatsOWMaxSDNew = _RttMonJitterStatsOWMaxSDNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 53),
    _RttMonJitterStatsOWMaxSDNew_Type()
)
rttMonJitterStatsOWMaxSDNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMaxSDNew.setStatus("current")
_RttMonJitterStatsOWMinDSNew_Type = Gauge32
_RttMonJitterStatsOWMinDSNew_Object = MibTableColumn
rttMonJitterStatsOWMinDSNew = _RttMonJitterStatsOWMinDSNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 54),
    _RttMonJitterStatsOWMinDSNew_Type()
)
rttMonJitterStatsOWMinDSNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMinDSNew.setStatus("current")
_RttMonJitterStatsOWMaxDSNew_Type = Gauge32
_RttMonJitterStatsOWMaxDSNew_Object = MibTableColumn
rttMonJitterStatsOWMaxDSNew = _RttMonJitterStatsOWMaxDSNew_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 55),
    _RttMonJitterStatsOWMaxDSNew_Type()
)
rttMonJitterStatsOWMaxDSNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWMaxDSNew.setStatus("current")


class _RttMonJitterStatsMinOfMOS_Type(Gauge32):
    """Custom type rttMonJitterStatsMinOfMOS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 500),
    )


_RttMonJitterStatsMinOfMOS_Type.__name__ = "Gauge32"
_RttMonJitterStatsMinOfMOS_Object = MibTableColumn
rttMonJitterStatsMinOfMOS = _RttMonJitterStatsMinOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 56),
    _RttMonJitterStatsMinOfMOS_Type()
)
rttMonJitterStatsMinOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfMOS.setStatus("current")


class _RttMonJitterStatsMaxOfMOS_Type(Gauge32):
    """Custom type rttMonJitterStatsMaxOfMOS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 500),
    )


_RttMonJitterStatsMaxOfMOS_Type.__name__ = "Gauge32"
_RttMonJitterStatsMaxOfMOS_Object = MibTableColumn
rttMonJitterStatsMaxOfMOS = _RttMonJitterStatsMaxOfMOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 57),
    _RttMonJitterStatsMaxOfMOS_Type()
)
rttMonJitterStatsMaxOfMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfMOS.setStatus("current")
_RttMonJitterStatsMinOfICPIF_Type = Gauge32
_RttMonJitterStatsMinOfICPIF_Object = MibTableColumn
rttMonJitterStatsMinOfICPIF = _RttMonJitterStatsMinOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 58),
    _RttMonJitterStatsMinOfICPIF_Type()
)
rttMonJitterStatsMinOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfICPIF.setStatus("current")
_RttMonJitterStatsMaxOfICPIF_Type = Gauge32
_RttMonJitterStatsMaxOfICPIF_Object = MibTableColumn
rttMonJitterStatsMaxOfICPIF = _RttMonJitterStatsMaxOfICPIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 59),
    _RttMonJitterStatsMaxOfICPIF_Type()
)
rttMonJitterStatsMaxOfICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfICPIF.setStatus("current")
_RttMonJitterStatsIAJOut_Type = Gauge32
_RttMonJitterStatsIAJOut_Object = MibTableColumn
rttMonJitterStatsIAJOut = _RttMonJitterStatsIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 60),
    _RttMonJitterStatsIAJOut_Type()
)
rttMonJitterStatsIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsIAJOut.setStatus("current")
_RttMonJitterStatsIAJIn_Type = Gauge32
_RttMonJitterStatsIAJIn_Object = MibTableColumn
rttMonJitterStatsIAJIn = _RttMonJitterStatsIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 61),
    _RttMonJitterStatsIAJIn_Type()
)
rttMonJitterStatsIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsIAJIn.setStatus("current")
_RttMonJitterStatsAvgJitter_Type = Gauge32
_RttMonJitterStatsAvgJitter_Object = MibTableColumn
rttMonJitterStatsAvgJitter = _RttMonJitterStatsAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 62),
    _RttMonJitterStatsAvgJitter_Type()
)
rttMonJitterStatsAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsAvgJitter.setStatus("current")
_RttMonJitterStatsAvgJitterSD_Type = Gauge32
_RttMonJitterStatsAvgJitterSD_Object = MibTableColumn
rttMonJitterStatsAvgJitterSD = _RttMonJitterStatsAvgJitterSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 63),
    _RttMonJitterStatsAvgJitterSD_Type()
)
rttMonJitterStatsAvgJitterSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsAvgJitterSD.setStatus("current")
_RttMonJitterStatsAvgJitterDS_Type = Gauge32
_RttMonJitterStatsAvgJitterDS_Object = MibTableColumn
rttMonJitterStatsAvgJitterDS = _RttMonJitterStatsAvgJitterDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 64),
    _RttMonJitterStatsAvgJitterDS_Type()
)
rttMonJitterStatsAvgJitterDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsAvgJitterDS.setStatus("current")
_RttMonJitterStatsUnSyncRTs_Type = Counter32
_RttMonJitterStatsUnSyncRTs_Object = MibTableColumn
rttMonJitterStatsUnSyncRTs = _RttMonJitterStatsUnSyncRTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 65),
    _RttMonJitterStatsUnSyncRTs_Type()
)
rttMonJitterStatsUnSyncRTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsUnSyncRTs.setStatus("current")
_RttMonJitterStatsRTTSumHigh_Type = Counter32
_RttMonJitterStatsRTTSumHigh_Object = MibTableColumn
rttMonJitterStatsRTTSumHigh = _RttMonJitterStatsRTTSumHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 66),
    _RttMonJitterStatsRTTSumHigh_Type()
)
rttMonJitterStatsRTTSumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSumHigh.setStatus("current")
_RttMonJitterStatsOWSumSDHigh_Type = Counter32
_RttMonJitterStatsOWSumSDHigh_Object = MibTableColumn
rttMonJitterStatsOWSumSDHigh = _RttMonJitterStatsOWSumSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 67),
    _RttMonJitterStatsOWSumSDHigh_Type()
)
rttMonJitterStatsOWSumSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSumSDHigh.setStatus("current")
_RttMonJitterStatsOWSumDSHigh_Type = Counter32
_RttMonJitterStatsOWSumDSHigh_Object = MibTableColumn
rttMonJitterStatsOWSumDSHigh = _RttMonJitterStatsOWSumDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 68),
    _RttMonJitterStatsOWSumDSHigh_Type()
)
rttMonJitterStatsOWSumDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOWSumDSHigh.setStatus("current")
_RttMonJitterStatsNumOverThresh_Type = Counter32
_RttMonJitterStatsNumOverThresh_Object = MibTableColumn
rttMonJitterStatsNumOverThresh = _RttMonJitterStatsNumOverThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 69),
    _RttMonJitterStatsNumOverThresh_Type()
)
rttMonJitterStatsNumOverThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOverThresh.setStatus("current")
_RttMonLpdGrpStatsTable_Object = MibTable
rttMonLpdGrpStatsTable = _RttMonLpdGrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7)
)
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsTable.setStatus("current")
_RttMonLpdGrpStatsEntry_Object = MibTableRow
rttMonLpdGrpStatsEntry = _RttMonLpdGrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1)
)
rttMonLpdGrpStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonLpdGrpStatsGroupIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonLpdGrpStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsEntry.setStatus("current")


class _RttMonLpdGrpStatsGroupIndex_Type(Integer32):
    """Custom type rttMonLpdGrpStatsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonLpdGrpStatsGroupIndex_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsGroupIndex_Object = MibTableColumn
rttMonLpdGrpStatsGroupIndex = _RttMonLpdGrpStatsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 1),
    _RttMonLpdGrpStatsGroupIndex_Type()
)
rttMonLpdGrpStatsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsGroupIndex.setStatus("current")
_RttMonLpdGrpStatsStartTimeIndex_Type = TimeStamp
_RttMonLpdGrpStatsStartTimeIndex_Object = MibTableColumn
rttMonLpdGrpStatsStartTimeIndex = _RttMonLpdGrpStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 2),
    _RttMonLpdGrpStatsStartTimeIndex_Type()
)
rttMonLpdGrpStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsStartTimeIndex.setStatus("current")
_RttMonLpdGrpStatsTargetPE_Type = RttMonTargetAddress
_RttMonLpdGrpStatsTargetPE_Object = MibTableColumn
rttMonLpdGrpStatsTargetPE = _RttMonLpdGrpStatsTargetPE_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 3),
    _RttMonLpdGrpStatsTargetPE_Type()
)
rttMonLpdGrpStatsTargetPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsTargetPE.setStatus("current")


class _RttMonLpdGrpStatsNumOfPass_Type(Integer32):
    """Custom type rttMonLpdGrpStatsNumOfPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsNumOfPass_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsNumOfPass_Object = MibTableColumn
rttMonLpdGrpStatsNumOfPass = _RttMonLpdGrpStatsNumOfPass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 4),
    _RttMonLpdGrpStatsNumOfPass_Type()
)
rttMonLpdGrpStatsNumOfPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfPass.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfPass.setUnits("passes")


class _RttMonLpdGrpStatsNumOfFail_Type(Integer32):
    """Custom type rttMonLpdGrpStatsNumOfFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsNumOfFail_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsNumOfFail_Object = MibTableColumn
rttMonLpdGrpStatsNumOfFail = _RttMonLpdGrpStatsNumOfFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 5),
    _RttMonLpdGrpStatsNumOfFail_Type()
)
rttMonLpdGrpStatsNumOfFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfFail.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfFail.setUnits("failures")


class _RttMonLpdGrpStatsNumOfTimeout_Type(Integer32):
    """Custom type rttMonLpdGrpStatsNumOfTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsNumOfTimeout_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsNumOfTimeout_Object = MibTableColumn
rttMonLpdGrpStatsNumOfTimeout = _RttMonLpdGrpStatsNumOfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 6),
    _RttMonLpdGrpStatsNumOfTimeout_Type()
)
rttMonLpdGrpStatsNumOfTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsNumOfTimeout.setUnits("timeouts")


class _RttMonLpdGrpStatsAvgRTT_Type(Integer32):
    """Custom type rttMonLpdGrpStatsAvgRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsAvgRTT_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsAvgRTT_Object = MibTableColumn
rttMonLpdGrpStatsAvgRTT = _RttMonLpdGrpStatsAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 7),
    _RttMonLpdGrpStatsAvgRTT_Type()
)
rttMonLpdGrpStatsAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsAvgRTT.setUnits("milliseconds")


class _RttMonLpdGrpStatsMinRTT_Type(Integer32):
    """Custom type rttMonLpdGrpStatsMinRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsMinRTT_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsMinRTT_Object = MibTableColumn
rttMonLpdGrpStatsMinRTT = _RttMonLpdGrpStatsMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 8),
    _RttMonLpdGrpStatsMinRTT_Type()
)
rttMonLpdGrpStatsMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMinRTT.setUnits("milliseconds")


class _RttMonLpdGrpStatsMaxRTT_Type(Integer32):
    """Custom type rttMonLpdGrpStatsMaxRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsMaxRTT_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsMaxRTT_Object = MibTableColumn
rttMonLpdGrpStatsMaxRTT = _RttMonLpdGrpStatsMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 9),
    _RttMonLpdGrpStatsMaxRTT_Type()
)
rttMonLpdGrpStatsMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMaxRTT.setUnits("milliseconds")


class _RttMonLpdGrpStatsMinNumPaths_Type(Integer32):
    """Custom type rttMonLpdGrpStatsMinNumPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsMinNumPaths_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsMinNumPaths_Object = MibTableColumn
rttMonLpdGrpStatsMinNumPaths = _RttMonLpdGrpStatsMinNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 10),
    _RttMonLpdGrpStatsMinNumPaths_Type()
)
rttMonLpdGrpStatsMinNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMinNumPaths.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMinNumPaths.setUnits("paths")


class _RttMonLpdGrpStatsMaxNumPaths_Type(Integer32):
    """Custom type rttMonLpdGrpStatsMaxNumPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLpdGrpStatsMaxNumPaths_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsMaxNumPaths_Object = MibTableColumn
rttMonLpdGrpStatsMaxNumPaths = _RttMonLpdGrpStatsMaxNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 11),
    _RttMonLpdGrpStatsMaxNumPaths_Type()
)
rttMonLpdGrpStatsMaxNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMaxNumPaths.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsMaxNumPaths.setUnits("paths")
_RttMonLpdGrpStatsLPDStartTime_Type = TimeStamp
_RttMonLpdGrpStatsLPDStartTime_Object = MibTableColumn
rttMonLpdGrpStatsLPDStartTime = _RttMonLpdGrpStatsLPDStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 12),
    _RttMonLpdGrpStatsLPDStartTime_Type()
)
rttMonLpdGrpStatsLPDStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDStartTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDStartTime.setUnits("tenths of milliseconds")
_RttMonLpdGrpStatsLPDFailOccurred_Type = TruthValue
_RttMonLpdGrpStatsLPDFailOccurred_Object = MibTableColumn
rttMonLpdGrpStatsLPDFailOccurred = _RttMonLpdGrpStatsLPDFailOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 13),
    _RttMonLpdGrpStatsLPDFailOccurred_Type()
)
rttMonLpdGrpStatsLPDFailOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDFailOccurred.setStatus("current")
_RttMonLpdGrpStatsLPDFailCause_Type = RttMplsVpnMonLpdFailureSense
_RttMonLpdGrpStatsLPDFailCause_Object = MibTableColumn
rttMonLpdGrpStatsLPDFailCause = _RttMonLpdGrpStatsLPDFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 14),
    _RttMonLpdGrpStatsLPDFailCause_Type()
)
rttMonLpdGrpStatsLPDFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDFailCause.setStatus("current")


class _RttMonLpdGrpStatsLPDCompTime_Type(Integer32):
    """Custom type rttMonLpdGrpStatsLPDCompTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RttMonLpdGrpStatsLPDCompTime_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsLPDCompTime_Object = MibTableColumn
rttMonLpdGrpStatsLPDCompTime = _RttMonLpdGrpStatsLPDCompTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 15),
    _RttMonLpdGrpStatsLPDCompTime_Type()
)
rttMonLpdGrpStatsLPDCompTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDCompTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsLPDCompTime.setUnits("seconds")
_RttMonLpdGrpStatsGroupStatus_Type = RttMplsVpnMonLpdGrpStatus
_RttMonLpdGrpStatsGroupStatus_Object = MibTableColumn
rttMonLpdGrpStatsGroupStatus = _RttMonLpdGrpStatsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 16),
    _RttMonLpdGrpStatsGroupStatus_Type()
)
rttMonLpdGrpStatsGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsGroupStatus.setStatus("current")


class _RttMonLpdGrpStatsGroupProbeIndex_Type(Integer32):
    """Custom type rttMonLpdGrpStatsGroupProbeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonLpdGrpStatsGroupProbeIndex_Type.__name__ = "Integer32"
_RttMonLpdGrpStatsGroupProbeIndex_Object = MibTableColumn
rttMonLpdGrpStatsGroupProbeIndex = _RttMonLpdGrpStatsGroupProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 17),
    _RttMonLpdGrpStatsGroupProbeIndex_Type()
)
rttMonLpdGrpStatsGroupProbeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsGroupProbeIndex.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsGroupProbeIndex.setUnits("identifier")
_RttMonLpdGrpStatsPathIds_Type = DisplayString
_RttMonLpdGrpStatsPathIds_Object = MibTableColumn
rttMonLpdGrpStatsPathIds = _RttMonLpdGrpStatsPathIds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 18),
    _RttMonLpdGrpStatsPathIds_Type()
)
rttMonLpdGrpStatsPathIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsPathIds.setStatus("current")
_RttMonLpdGrpStatsProbeStatus_Type = DisplayString
_RttMonLpdGrpStatsProbeStatus_Object = MibTableColumn
rttMonLpdGrpStatsProbeStatus = _RttMonLpdGrpStatsProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 19),
    _RttMonLpdGrpStatsProbeStatus_Type()
)
rttMonLpdGrpStatsProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsProbeStatus.setStatus("current")
_RttMonLpdGrpStatsResetTime_Type = TimeStamp
_RttMonLpdGrpStatsResetTime_Object = MibTableColumn
rttMonLpdGrpStatsResetTime = _RttMonLpdGrpStatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 7, 1, 20),
    _RttMonLpdGrpStatsResetTime_Type()
)
rttMonLpdGrpStatsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLpdGrpStatsResetTime.setStatus("current")
_RttMonHistory_ObjectIdentity = ObjectIdentity
rttMonHistory = _RttMonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4)
)
_RttMonHistoryCollectionTable_Object = MibTable
rttMonHistoryCollectionTable = _RttMonHistoryCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rttMonHistoryCollectionTable.setStatus("current")
_RttMonHistoryCollectionEntry_Object = MibTableRow
rttMonHistoryCollectionEntry = _RttMonHistoryCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1)
)
rttMonHistoryCollectionEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionLifeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionBucketIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionSampleIndex"),
)
if mibBuilder.loadTexts:
    rttMonHistoryCollectionEntry.setStatus("current")


class _RttMonHistoryCollectionLifeIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionLifeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonHistoryCollectionLifeIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionLifeIndex_Object = MibTableColumn
rttMonHistoryCollectionLifeIndex = _RttMonHistoryCollectionLifeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 1),
    _RttMonHistoryCollectionLifeIndex_Type()
)
rttMonHistoryCollectionLifeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionLifeIndex.setStatus("current")


class _RttMonHistoryCollectionBucketIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionBucketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonHistoryCollectionBucketIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionBucketIndex_Object = MibTableColumn
rttMonHistoryCollectionBucketIndex = _RttMonHistoryCollectionBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 2),
    _RttMonHistoryCollectionBucketIndex_Type()
)
rttMonHistoryCollectionBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionBucketIndex.setStatus("current")


class _RttMonHistoryCollectionSampleIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RttMonHistoryCollectionSampleIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionSampleIndex_Object = MibTableColumn
rttMonHistoryCollectionSampleIndex = _RttMonHistoryCollectionSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 3),
    _RttMonHistoryCollectionSampleIndex_Type()
)
rttMonHistoryCollectionSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSampleIndex.setStatus("current")
_RttMonHistoryCollectionSampleTime_Type = TimeStamp
_RttMonHistoryCollectionSampleTime_Object = MibTableColumn
rttMonHistoryCollectionSampleTime = _RttMonHistoryCollectionSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 4),
    _RttMonHistoryCollectionSampleTime_Type()
)
rttMonHistoryCollectionSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSampleTime.setStatus("current")
_RttMonHistoryCollectionAddress_Type = RttMonTargetAddress
_RttMonHistoryCollectionAddress_Object = MibTableColumn
rttMonHistoryCollectionAddress = _RttMonHistoryCollectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 5),
    _RttMonHistoryCollectionAddress_Type()
)
rttMonHistoryCollectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionAddress.setStatus("current")
_RttMonHistoryCollectionCompletionTime_Type = Gauge32
_RttMonHistoryCollectionCompletionTime_Object = MibTableColumn
rttMonHistoryCollectionCompletionTime = _RttMonHistoryCollectionCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 6),
    _RttMonHistoryCollectionCompletionTime_Type()
)
rttMonHistoryCollectionCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionCompletionTime.setUnits("milliseconds")
_RttMonHistoryCollectionSense_Type = RttResponseSense
_RttMonHistoryCollectionSense_Object = MibTableColumn
rttMonHistoryCollectionSense = _RttMonHistoryCollectionSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 7),
    _RttMonHistoryCollectionSense_Type()
)
rttMonHistoryCollectionSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSense.setStatus("current")


class _RttMonHistoryCollectionApplSpecificSense_Type(Integer32):
    """Custom type rttMonHistoryCollectionApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonHistoryCollectionApplSpecificSense_Type.__name__ = "Integer32"
_RttMonHistoryCollectionApplSpecificSense_Object = MibTableColumn
rttMonHistoryCollectionApplSpecificSense = _RttMonHistoryCollectionApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 8),
    _RttMonHistoryCollectionApplSpecificSense_Type()
)
rttMonHistoryCollectionApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionApplSpecificSense.setStatus("current")
_RttMonHistoryCollectionSenseDescription_Type = DisplayString
_RttMonHistoryCollectionSenseDescription_Object = MibTableColumn
rttMonHistoryCollectionSenseDescription = _RttMonHistoryCollectionSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 9),
    _RttMonHistoryCollectionSenseDescription_Type()
)
rttMonHistoryCollectionSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSenseDescription.setStatus("current")
_RttMonLatestOper_ObjectIdentity = ObjectIdentity
rttMonLatestOper = _RttMonLatestOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5)
)
_RttMonLatestHTTPOperTable_Object = MibTable
rttMonLatestHTTPOperTable = _RttMonLatestHTTPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTable.setStatus("current")
_RttMonLatestHTTPOperEntry_Object = MibTableRow
rttMonLatestHTTPOperEntry = _RttMonLatestHTTPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1)
)
rttMonLatestHTTPOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperEntry.setStatus("current")
_RttMonLatestHTTPOperRTT_Type = Gauge32
_RttMonLatestHTTPOperRTT_Object = MibTableColumn
rttMonLatestHTTPOperRTT = _RttMonLatestHTTPOperRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 1),
    _RttMonLatestHTTPOperRTT_Type()
)
rttMonLatestHTTPOperRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperRTT.setStatus("current")
_RttMonLatestHTTPOperDNSRTT_Type = Gauge32
_RttMonLatestHTTPOperDNSRTT_Object = MibTableColumn
rttMonLatestHTTPOperDNSRTT = _RttMonLatestHTTPOperDNSRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 2),
    _RttMonLatestHTTPOperDNSRTT_Type()
)
rttMonLatestHTTPOperDNSRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperDNSRTT.setStatus("current")
_RttMonLatestHTTPOperTCPConnectRTT_Type = Gauge32
_RttMonLatestHTTPOperTCPConnectRTT_Object = MibTableColumn
rttMonLatestHTTPOperTCPConnectRTT = _RttMonLatestHTTPOperTCPConnectRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 3),
    _RttMonLatestHTTPOperTCPConnectRTT_Type()
)
rttMonLatestHTTPOperTCPConnectRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTCPConnectRTT.setStatus("current")
_RttMonLatestHTTPOperTransactionRTT_Type = Gauge32
_RttMonLatestHTTPOperTransactionRTT_Object = MibTableColumn
rttMonLatestHTTPOperTransactionRTT = _RttMonLatestHTTPOperTransactionRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 4),
    _RttMonLatestHTTPOperTransactionRTT_Type()
)
rttMonLatestHTTPOperTransactionRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTransactionRTT.setStatus("current")
_RttMonLatestHTTPOperMessageBodyOctets_Type = Gauge32
_RttMonLatestHTTPOperMessageBodyOctets_Object = MibTableColumn
rttMonLatestHTTPOperMessageBodyOctets = _RttMonLatestHTTPOperMessageBodyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 5),
    _RttMonLatestHTTPOperMessageBodyOctets_Type()
)
rttMonLatestHTTPOperMessageBodyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperMessageBodyOctets.setStatus("current")
_RttMonLatestHTTPOperSense_Type = RttResponseSense
_RttMonLatestHTTPOperSense_Object = MibTableColumn
rttMonLatestHTTPOperSense = _RttMonLatestHTTPOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 6),
    _RttMonLatestHTTPOperSense_Type()
)
rttMonLatestHTTPOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperSense.setStatus("current")
_RttMonLatestHTTPErrorSenseDescription_Type = DisplayString
_RttMonLatestHTTPErrorSenseDescription_Object = MibTableColumn
rttMonLatestHTTPErrorSenseDescription = _RttMonLatestHTTPErrorSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 7),
    _RttMonLatestHTTPErrorSenseDescription_Type()
)
rttMonLatestHTTPErrorSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPErrorSenseDescription.setStatus("current")
_RttMonLatestJitterOperTable_Object = MibTable
rttMonLatestJitterOperTable = _RttMonLatestJitterOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rttMonLatestJitterOperTable.setStatus("current")
_RttMonLatestJitterOperEntry_Object = MibTableRow
rttMonLatestJitterOperEntry = _RttMonLatestJitterOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1)
)
rttMonLatestJitterOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestJitterOperEntry.setStatus("current")
_RttMonLatestJitterOperNumOfRTT_Type = Gauge32
_RttMonLatestJitterOperNumOfRTT_Object = MibTableColumn
rttMonLatestJitterOperNumOfRTT = _RttMonLatestJitterOperNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 1),
    _RttMonLatestJitterOperNumOfRTT_Type()
)
rttMonLatestJitterOperNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfRTT.setStatus("current")
_RttMonLatestJitterOperRTTSum_Type = Gauge32
_RttMonLatestJitterOperRTTSum_Object = MibTableColumn
rttMonLatestJitterOperRTTSum = _RttMonLatestJitterOperRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 2),
    _RttMonLatestJitterOperRTTSum_Type()
)
rttMonLatestJitterOperRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSum.setStatus("current")
_RttMonLatestJitterOperRTTSum2_Type = Gauge32
_RttMonLatestJitterOperRTTSum2_Object = MibTableColumn
rttMonLatestJitterOperRTTSum2 = _RttMonLatestJitterOperRTTSum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 3),
    _RttMonLatestJitterOperRTTSum2_Type()
)
rttMonLatestJitterOperRTTSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSum2.setStatus("current")
_RttMonLatestJitterOperRTTMin_Type = Gauge32
_RttMonLatestJitterOperRTTMin_Object = MibTableColumn
rttMonLatestJitterOperRTTMin = _RttMonLatestJitterOperRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 4),
    _RttMonLatestJitterOperRTTMin_Type()
)
rttMonLatestJitterOperRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTMin.setStatus("current")
_RttMonLatestJitterOperRTTMax_Type = Gauge32
_RttMonLatestJitterOperRTTMax_Object = MibTableColumn
rttMonLatestJitterOperRTTMax = _RttMonLatestJitterOperRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 5),
    _RttMonLatestJitterOperRTTMax_Type()
)
rttMonLatestJitterOperRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTMax.setStatus("current")
_RttMonLatestJitterOperMinOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperMinOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperMinOfPositivesSD = _RttMonLatestJitterOperMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 6),
    _RttMonLatestJitterOperMinOfPositivesSD_Type()
)
rttMonLatestJitterOperMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperMaxOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperMaxOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperMaxOfPositivesSD = _RttMonLatestJitterOperMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 7),
    _RttMonLatestJitterOperMaxOfPositivesSD_Type()
)
rttMonLatestJitterOperMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperNumOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperNumOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperNumOfPositivesSD = _RttMonLatestJitterOperNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 8),
    _RttMonLatestJitterOperNumOfPositivesSD_Type()
)
rttMonLatestJitterOperNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperSumOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperSumOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperSumOfPositivesSD = _RttMonLatestJitterOperSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 9),
    _RttMonLatestJitterOperSumOfPositivesSD_Type()
)
rttMonLatestJitterOperSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperSum2PositivesSD_Type = Gauge32
_RttMonLatestJitterOperSum2PositivesSD_Object = MibTableColumn
rttMonLatestJitterOperSum2PositivesSD = _RttMonLatestJitterOperSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 10),
    _RttMonLatestJitterOperSum2PositivesSD_Type()
)
rttMonLatestJitterOperSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2PositivesSD.setStatus("current")
_RttMonLatestJitterOperMinOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperMinOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperMinOfNegativesSD = _RttMonLatestJitterOperMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 11),
    _RttMonLatestJitterOperMinOfNegativesSD_Type()
)
rttMonLatestJitterOperMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperMaxOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperMaxOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperMaxOfNegativesSD = _RttMonLatestJitterOperMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 12),
    _RttMonLatestJitterOperMaxOfNegativesSD_Type()
)
rttMonLatestJitterOperMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperNumOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperNumOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperNumOfNegativesSD = _RttMonLatestJitterOperNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 13),
    _RttMonLatestJitterOperNumOfNegativesSD_Type()
)
rttMonLatestJitterOperNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperSumOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperSumOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperSumOfNegativesSD = _RttMonLatestJitterOperSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 14),
    _RttMonLatestJitterOperSumOfNegativesSD_Type()
)
rttMonLatestJitterOperSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperSum2NegativesSD_Type = Gauge32
_RttMonLatestJitterOperSum2NegativesSD_Object = MibTableColumn
rttMonLatestJitterOperSum2NegativesSD = _RttMonLatestJitterOperSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 15),
    _RttMonLatestJitterOperSum2NegativesSD_Type()
)
rttMonLatestJitterOperSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2NegativesSD.setStatus("current")
_RttMonLatestJitterOperMinOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperMinOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperMinOfPositivesDS = _RttMonLatestJitterOperMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 16),
    _RttMonLatestJitterOperMinOfPositivesDS_Type()
)
rttMonLatestJitterOperMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperMaxOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperMaxOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperMaxOfPositivesDS = _RttMonLatestJitterOperMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 17),
    _RttMonLatestJitterOperMaxOfPositivesDS_Type()
)
rttMonLatestJitterOperMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperNumOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperNumOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperNumOfPositivesDS = _RttMonLatestJitterOperNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 18),
    _RttMonLatestJitterOperNumOfPositivesDS_Type()
)
rttMonLatestJitterOperNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperSumOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperSumOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperSumOfPositivesDS = _RttMonLatestJitterOperSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 19),
    _RttMonLatestJitterOperSumOfPositivesDS_Type()
)
rttMonLatestJitterOperSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperSum2PositivesDS_Type = Gauge32
_RttMonLatestJitterOperSum2PositivesDS_Object = MibTableColumn
rttMonLatestJitterOperSum2PositivesDS = _RttMonLatestJitterOperSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 20),
    _RttMonLatestJitterOperSum2PositivesDS_Type()
)
rttMonLatestJitterOperSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2PositivesDS.setStatus("current")
_RttMonLatestJitterOperMinOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperMinOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperMinOfNegativesDS = _RttMonLatestJitterOperMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 21),
    _RttMonLatestJitterOperMinOfNegativesDS_Type()
)
rttMonLatestJitterOperMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperMaxOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperMaxOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperMaxOfNegativesDS = _RttMonLatestJitterOperMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 22),
    _RttMonLatestJitterOperMaxOfNegativesDS_Type()
)
rttMonLatestJitterOperMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperNumOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperNumOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperNumOfNegativesDS = _RttMonLatestJitterOperNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 23),
    _RttMonLatestJitterOperNumOfNegativesDS_Type()
)
rttMonLatestJitterOperNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperSumOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperSumOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperSumOfNegativesDS = _RttMonLatestJitterOperSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 24),
    _RttMonLatestJitterOperSumOfNegativesDS_Type()
)
rttMonLatestJitterOperSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperSum2NegativesDS_Type = Gauge32
_RttMonLatestJitterOperSum2NegativesDS_Object = MibTableColumn
rttMonLatestJitterOperSum2NegativesDS = _RttMonLatestJitterOperSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 25),
    _RttMonLatestJitterOperSum2NegativesDS_Type()
)
rttMonLatestJitterOperSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2NegativesDS.setStatus("current")
_RttMonLatestJitterOperPacketLossSD_Type = Gauge32
_RttMonLatestJitterOperPacketLossSD_Object = MibTableColumn
rttMonLatestJitterOperPacketLossSD = _RttMonLatestJitterOperPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 26),
    _RttMonLatestJitterOperPacketLossSD_Type()
)
rttMonLatestJitterOperPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLossSD.setStatus("current")
_RttMonLatestJitterOperPacketLossDS_Type = Gauge32
_RttMonLatestJitterOperPacketLossDS_Object = MibTableColumn
rttMonLatestJitterOperPacketLossDS = _RttMonLatestJitterOperPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 27),
    _RttMonLatestJitterOperPacketLossDS_Type()
)
rttMonLatestJitterOperPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLossDS.setStatus("current")
_RttMonLatestJitterOperPacketOutOfSequence_Type = Gauge32
_RttMonLatestJitterOperPacketOutOfSequence_Object = MibTableColumn
rttMonLatestJitterOperPacketOutOfSequence = _RttMonLatestJitterOperPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 28),
    _RttMonLatestJitterOperPacketOutOfSequence_Type()
)
rttMonLatestJitterOperPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketOutOfSequence.setStatus("current")
_RttMonLatestJitterOperPacketMIA_Type = Gauge32
_RttMonLatestJitterOperPacketMIA_Object = MibTableColumn
rttMonLatestJitterOperPacketMIA = _RttMonLatestJitterOperPacketMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 29),
    _RttMonLatestJitterOperPacketMIA_Type()
)
rttMonLatestJitterOperPacketMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketMIA.setStatus("current")
_RttMonLatestJitterOperPacketLateArrival_Type = Gauge32
_RttMonLatestJitterOperPacketLateArrival_Object = MibTableColumn
rttMonLatestJitterOperPacketLateArrival = _RttMonLatestJitterOperPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 30),
    _RttMonLatestJitterOperPacketLateArrival_Type()
)
rttMonLatestJitterOperPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLateArrival.setStatus("current")
_RttMonLatestJitterOperSense_Type = RttResponseSense
_RttMonLatestJitterOperSense_Object = MibTableColumn
rttMonLatestJitterOperSense = _RttMonLatestJitterOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 31),
    _RttMonLatestJitterOperSense_Type()
)
rttMonLatestJitterOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSense.setStatus("current")
_RttMonLatestJitterErrorSenseDescription_Type = DisplayString
_RttMonLatestJitterErrorSenseDescription_Object = MibTableColumn
rttMonLatestJitterErrorSenseDescription = _RttMonLatestJitterErrorSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 32),
    _RttMonLatestJitterErrorSenseDescription_Type()
)
rttMonLatestJitterErrorSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterErrorSenseDescription.setStatus("current")
_RttMonLatestJitterOperOWSumSD_Type = Gauge32
_RttMonLatestJitterOperOWSumSD_Object = MibTableColumn
rttMonLatestJitterOperOWSumSD = _RttMonLatestJitterOperOWSumSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 33),
    _RttMonLatestJitterOperOWSumSD_Type()
)
rttMonLatestJitterOperOWSumSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSumSD.setStatus("current")
_RttMonLatestJitterOperOWSum2SD_Type = Gauge32
_RttMonLatestJitterOperOWSum2SD_Object = MibTableColumn
rttMonLatestJitterOperOWSum2SD = _RttMonLatestJitterOperOWSum2SD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 34),
    _RttMonLatestJitterOperOWSum2SD_Type()
)
rttMonLatestJitterOperOWSum2SD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSum2SD.setStatus("current")
_RttMonLatestJitterOperOWMinSD_Type = Gauge32
_RttMonLatestJitterOperOWMinSD_Object = MibTableColumn
rttMonLatestJitterOperOWMinSD = _RttMonLatestJitterOperOWMinSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 35),
    _RttMonLatestJitterOperOWMinSD_Type()
)
rttMonLatestJitterOperOWMinSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWMinSD.setStatus("current")
_RttMonLatestJitterOperOWMaxSD_Type = Gauge32
_RttMonLatestJitterOperOWMaxSD_Object = MibTableColumn
rttMonLatestJitterOperOWMaxSD = _RttMonLatestJitterOperOWMaxSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 36),
    _RttMonLatestJitterOperOWMaxSD_Type()
)
rttMonLatestJitterOperOWMaxSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWMaxSD.setStatus("current")
_RttMonLatestJitterOperOWSumDS_Type = Gauge32
_RttMonLatestJitterOperOWSumDS_Object = MibTableColumn
rttMonLatestJitterOperOWSumDS = _RttMonLatestJitterOperOWSumDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 37),
    _RttMonLatestJitterOperOWSumDS_Type()
)
rttMonLatestJitterOperOWSumDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSumDS.setStatus("current")
_RttMonLatestJitterOperOWSum2DS_Type = Gauge32
_RttMonLatestJitterOperOWSum2DS_Object = MibTableColumn
rttMonLatestJitterOperOWSum2DS = _RttMonLatestJitterOperOWSum2DS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 38),
    _RttMonLatestJitterOperOWSum2DS_Type()
)
rttMonLatestJitterOperOWSum2DS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSum2DS.setStatus("current")
_RttMonLatestJitterOperOWMinDS_Type = Gauge32
_RttMonLatestJitterOperOWMinDS_Object = MibTableColumn
rttMonLatestJitterOperOWMinDS = _RttMonLatestJitterOperOWMinDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 39),
    _RttMonLatestJitterOperOWMinDS_Type()
)
rttMonLatestJitterOperOWMinDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWMinDS.setStatus("current")
_RttMonLatestJitterOperOWMaxDS_Type = Gauge32
_RttMonLatestJitterOperOWMaxDS_Object = MibTableColumn
rttMonLatestJitterOperOWMaxDS = _RttMonLatestJitterOperOWMaxDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 40),
    _RttMonLatestJitterOperOWMaxDS_Type()
)
rttMonLatestJitterOperOWMaxDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWMaxDS.setStatus("current")
_RttMonLatestJitterOperNumOfOW_Type = Gauge32
_RttMonLatestJitterOperNumOfOW_Object = MibTableColumn
rttMonLatestJitterOperNumOfOW = _RttMonLatestJitterOperNumOfOW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 41),
    _RttMonLatestJitterOperNumOfOW_Type()
)
rttMonLatestJitterOperNumOfOW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfOW.setStatus("current")


class _RttMonLatestJitterOperMOS_Type(Gauge32):
    """Custom type rttMonLatestJitterOperMOS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 500),
    )


_RttMonLatestJitterOperMOS_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperMOS_Object = MibTableColumn
rttMonLatestJitterOperMOS = _RttMonLatestJitterOperMOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 42),
    _RttMonLatestJitterOperMOS_Type()
)
rttMonLatestJitterOperMOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMOS.setStatus("current")


class _RttMonLatestJitterOperICPIF_Type(Gauge32):
    """Custom type rttMonLatestJitterOperICPIF based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperICPIF_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperICPIF_Object = MibTableColumn
rttMonLatestJitterOperICPIF = _RttMonLatestJitterOperICPIF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 43),
    _RttMonLatestJitterOperICPIF_Type()
)
rttMonLatestJitterOperICPIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperICPIF.setStatus("current")


class _RttMonLatestJitterOperIAJOut_Type(Gauge32):
    """Custom type rttMonLatestJitterOperIAJOut based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperIAJOut_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperIAJOut_Object = MibTableColumn
rttMonLatestJitterOperIAJOut = _RttMonLatestJitterOperIAJOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 44),
    _RttMonLatestJitterOperIAJOut_Type()
)
rttMonLatestJitterOperIAJOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperIAJOut.setStatus("current")


class _RttMonLatestJitterOperIAJIn_Type(Gauge32):
    """Custom type rttMonLatestJitterOperIAJIn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperIAJIn_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperIAJIn_Object = MibTableColumn
rttMonLatestJitterOperIAJIn = _RttMonLatestJitterOperIAJIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 45),
    _RttMonLatestJitterOperIAJIn_Type()
)
rttMonLatestJitterOperIAJIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperIAJIn.setStatus("current")


class _RttMonLatestJitterOperAvgJitter_Type(Gauge32):
    """Custom type rttMonLatestJitterOperAvgJitter based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperAvgJitter_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperAvgJitter_Object = MibTableColumn
rttMonLatestJitterOperAvgJitter = _RttMonLatestJitterOperAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 46),
    _RttMonLatestJitterOperAvgJitter_Type()
)
rttMonLatestJitterOperAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperAvgJitter.setStatus("current")


class _RttMonLatestJitterOperAvgSDJ_Type(Gauge32):
    """Custom type rttMonLatestJitterOperAvgSDJ based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperAvgSDJ_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperAvgSDJ_Object = MibTableColumn
rttMonLatestJitterOperAvgSDJ = _RttMonLatestJitterOperAvgSDJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 47),
    _RttMonLatestJitterOperAvgSDJ_Type()
)
rttMonLatestJitterOperAvgSDJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperAvgSDJ.setStatus("current")


class _RttMonLatestJitterOperAvgDSJ_Type(Gauge32):
    """Custom type rttMonLatestJitterOperAvgDSJ based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperAvgDSJ_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperAvgDSJ_Object = MibTableColumn
rttMonLatestJitterOperAvgDSJ = _RttMonLatestJitterOperAvgDSJ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 48),
    _RttMonLatestJitterOperAvgDSJ_Type()
)
rttMonLatestJitterOperAvgDSJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperAvgDSJ.setStatus("current")


class _RttMonLatestJitterOperOWAvgSD_Type(Gauge32):
    """Custom type rttMonLatestJitterOperOWAvgSD based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperOWAvgSD_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperOWAvgSD_Object = MibTableColumn
rttMonLatestJitterOperOWAvgSD = _RttMonLatestJitterOperOWAvgSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 49),
    _RttMonLatestJitterOperOWAvgSD_Type()
)
rttMonLatestJitterOperOWAvgSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWAvgSD.setStatus("current")


class _RttMonLatestJitterOperOWAvgDS_Type(Gauge32):
    """Custom type rttMonLatestJitterOperOWAvgDS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonLatestJitterOperOWAvgDS_Type.__name__ = "Gauge32"
_RttMonLatestJitterOperOWAvgDS_Object = MibTableColumn
rttMonLatestJitterOperOWAvgDS = _RttMonLatestJitterOperOWAvgDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 50),
    _RttMonLatestJitterOperOWAvgDS_Type()
)
rttMonLatestJitterOperOWAvgDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWAvgDS.setStatus("current")


class _RttMonLatestJitterOperNTPState_Type(Integer32):
    """Custom type rttMonLatestJitterOperNTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 2),
          ("sync", 1))
    )


_RttMonLatestJitterOperNTPState_Type.__name__ = "Integer32"
_RttMonLatestJitterOperNTPState_Object = MibTableColumn
rttMonLatestJitterOperNTPState = _RttMonLatestJitterOperNTPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 51),
    _RttMonLatestJitterOperNTPState_Type()
)
rttMonLatestJitterOperNTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNTPState.setStatus("current")
_RttMonLatestJitterOperUnSyncRTs_Type = Counter32
_RttMonLatestJitterOperUnSyncRTs_Object = MibTableColumn
rttMonLatestJitterOperUnSyncRTs = _RttMonLatestJitterOperUnSyncRTs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 52),
    _RttMonLatestJitterOperUnSyncRTs_Type()
)
rttMonLatestJitterOperUnSyncRTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperUnSyncRTs.setStatus("current")
_RttMonLatestJitterOperRTTSumHigh_Type = Gauge32
_RttMonLatestJitterOperRTTSumHigh_Object = MibTableColumn
rttMonLatestJitterOperRTTSumHigh = _RttMonLatestJitterOperRTTSumHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 53),
    _RttMonLatestJitterOperRTTSumHigh_Type()
)
rttMonLatestJitterOperRTTSumHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSumHigh.setStatus("current")
_RttMonLatestJitterOperRTTSum2High_Type = Gauge32
_RttMonLatestJitterOperRTTSum2High_Object = MibTableColumn
rttMonLatestJitterOperRTTSum2High = _RttMonLatestJitterOperRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 54),
    _RttMonLatestJitterOperRTTSum2High_Type()
)
rttMonLatestJitterOperRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSum2High.setStatus("current")
_RttMonLatestJitterOperOWSumSDHigh_Type = Gauge32
_RttMonLatestJitterOperOWSumSDHigh_Object = MibTableColumn
rttMonLatestJitterOperOWSumSDHigh = _RttMonLatestJitterOperOWSumSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 55),
    _RttMonLatestJitterOperOWSumSDHigh_Type()
)
rttMonLatestJitterOperOWSumSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSumSDHigh.setStatus("current")
_RttMonLatestJitterOperOWSum2SDHigh_Type = Gauge32
_RttMonLatestJitterOperOWSum2SDHigh_Object = MibTableColumn
rttMonLatestJitterOperOWSum2SDHigh = _RttMonLatestJitterOperOWSum2SDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 56),
    _RttMonLatestJitterOperOWSum2SDHigh_Type()
)
rttMonLatestJitterOperOWSum2SDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSum2SDHigh.setStatus("current")
_RttMonLatestJitterOperOWSumDSHigh_Type = Gauge32
_RttMonLatestJitterOperOWSumDSHigh_Object = MibTableColumn
rttMonLatestJitterOperOWSumDSHigh = _RttMonLatestJitterOperOWSumDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 57),
    _RttMonLatestJitterOperOWSumDSHigh_Type()
)
rttMonLatestJitterOperOWSumDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSumDSHigh.setStatus("current")
_RttMonLatestJitterOperOWSum2DSHigh_Type = Gauge32
_RttMonLatestJitterOperOWSum2DSHigh_Object = MibTableColumn
rttMonLatestJitterOperOWSum2DSHigh = _RttMonLatestJitterOperOWSum2DSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 58),
    _RttMonLatestJitterOperOWSum2DSHigh_Type()
)
rttMonLatestJitterOperOWSum2DSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperOWSum2DSHigh.setStatus("current")
_RttMonLatestJitterOperNumOverThresh_Type = Gauge32
_RttMonLatestJitterOperNumOverThresh_Object = MibTableColumn
rttMonLatestJitterOperNumOverThresh = _RttMonLatestJitterOperNumOverThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 59),
    _RttMonLatestJitterOperNumOverThresh_Type()
)
rttMonLatestJitterOperNumOverThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOverThresh.setStatus("current")
_RttMonNotificationsPrefix_ObjectIdentity = ObjectIdentity
rttMonNotificationsPrefix = _RttMonNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2)
)
_RttMonNotifications_ObjectIdentity = ObjectIdentity
rttMonNotifications = _RttMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0)
)
_CiscoRttMonMibConformance_ObjectIdentity = ObjectIdentity
ciscoRttMonMibConformance = _CiscoRttMonMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3)
)
_CiscoRttMonMibCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonMibCompliances = _CiscoRttMonMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1)
)
_CiscoRttMonMibGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonMibGroups = _CiscoRttMonMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2)
)
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonScheduleAdminEntry")
)
rttMonScheduleAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonReactAdminEntry")
)
rttMonReactAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonStatisticsAdminEntry")
)
rttMonStatisticsAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonHistoryAdminEntry")
)
rttMonHistoryAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonCtrlOperEntry")
)
rttMonCtrlOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonLatestRttOperEntry")
)
rttMonLatestRttOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonReactTriggerAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonReactTriggerOperEntry")
)
rttMonReactTriggerOperEntry.setIndexNames(*rttMonReactTriggerAdminEntry.getIndexNames())
rttMplsVpnMonCtrlEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMplsVpnMonTypeEntry")
)
rttMplsVpnMonTypeEntry.setIndexNames(*rttMplsVpnMonCtrlEntry.getIndexNames())
rttMplsVpnMonCtrlEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMplsVpnMonScheduleEntry")
)
rttMplsVpnMonScheduleEntry.setIndexNames(*rttMplsVpnMonCtrlEntry.getIndexNames())
rttMplsVpnMonCtrlEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMplsVpnMonReactEntry")
)
rttMplsVpnMonReactEntry.setIndexNames(*rttMplsVpnMonCtrlEntry.getIndexNames())

# Managed Objects groups

ciscoStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 3)
)
ciscoStatsGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime2Low"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime2High"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletionTimeMax"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletionTimeMin"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectNumDisconnects"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectTimeouts"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectBusies"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectNoConnections"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectDrops"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectSequenceErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectVerifyErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectAddress"),
        ("CISCO-RTTMON-MIB", "rttMonStatsTotalsElapsedTime"),
        ("CISCO-RTTMON-MIB", "rttMonStatsTotalsInitiations"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroup.setStatus("current")

ciscoHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 4)
)
ciscoHistoryGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSampleTime"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSense"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSenseDescription"))
)
if mibBuilder.loadTexts:
    ciscoHistoryGroup.setStatus("current")

ciscoCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 5)
)
ciscoCtrlGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetPort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourceAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourcePort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminControlEnable"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTOS"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSREnable"),
        ("CISCO-RTTMON-MIB", "rttMonEchoPathAdminHopAddress"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev1.setStatus("current")

ciscoCtrlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 6)
)
ciscoCtrlGroupRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddressString"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminNameServer"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOperation"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminHTTPVersion"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminURL"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCache"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminInterval"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminNumPackets"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProxy"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString1"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString2"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString3"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString4"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString5"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminMode"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev2.setStatus("current")

ciscoLatestOperGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 7)
)
ciscoLatestOperGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperDNSRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperTCPConnectRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperTransactionRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperMessageBodyOctets"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPErrorSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSum2"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2PositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2NegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2PositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2NegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLossSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLossDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketOutOfSequence"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketMIA"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLateArrival"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterErrorSenseDescription"))
)
if mibBuilder.loadTexts:
    ciscoLatestOperGroupRev1.setStatus("current")

ciscoStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 8)
)
ciscoStatsGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonHTTPStatsCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum2Low"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum2High"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTCPConnectRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTransactionRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsMessageBodyOctetsSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSServerTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTCPConnectTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTransactionTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSQueryError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsHTTPError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsBusies"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfRTT"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum2Low"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum2High"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesSDLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesSDLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesDSLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesDSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesDSLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesDSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLossSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLossDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketOutOfSequence"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketMIA"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLateArrival"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsError"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsBusies"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev1.setStatus("current")

ciscoApplGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 11)
)
ciscoApplGroupRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonApplResponder"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyChain"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyString1"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyString2"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyString3"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyString4"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthKeyString5"),
        ("CISCO-RTTMON-MIB", "rttMonApplAuthStatus"))
)
if mibBuilder.loadTexts:
    ciscoApplGroupRev2.setStatus("current")

ciscoCtrlGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 12)
)
ciscoCtrlGroupRev4.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminVrfName")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev4.setStatus("current")

ciscoStatsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 14)
)
ciscoStatsGroupRev3.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSumSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSum2SD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWMinSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWMaxSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSumDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSum2DS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWMinDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWMaxDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfOW"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSumSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSum2SDLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSum2SDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSumDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSum2DSLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSum2DSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfOW"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMinSDNew"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMaxSDNew"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMinDSNew"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMaxDSNew"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev3.setStatus("current")

ciscoCtrlGroupRev6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 16)
)
ciscoCtrlGroupRev6.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminCodecType"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCodecInterval"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCodecPayload"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCodecNumPackets"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminICPIFAdvFactor"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev6.setStatus("current")

ciscoStatsGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 17)
)
ciscoStatsGroupRev4.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMOS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperICPIF"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfMOS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfMOS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfICPIF"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfICPIF"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev4.setStatus("current")

ciscoApplGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 19)
)
ciscoApplGroupRev3.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonApplVersion"),
        ("CISCO-RTTMON-MIB", "rttMonApplMaxPacketDataSize"),
        ("CISCO-RTTMON-MIB", "rttMonApplTimeOfLastSet"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedRttTypesValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedProtocolsValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplNumCtrlAdminEntry"),
        ("CISCO-RTTMON-MIB", "rttMonApplReset"),
        ("CISCO-RTTMON-MIB", "rttMonApplProbeCapacity"),
        ("CISCO-RTTMON-MIB", "rttMonApplFreeMemLowWaterMark"),
        ("CISCO-RTTMON-MIB", "rttMonApplLatestSetError"))
)
if mibBuilder.loadTexts:
    ciscoApplGroupRev3.setStatus("current")

ciscoCtrlGroupRev7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 20)
)
ciscoCtrlGroupRev7.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttRecurring"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminProbes"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminPeriod"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminFrequency"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminLife"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminAgeout"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminStatus"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev7.setStatus("current")

ciscoCtrlGroupRev8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 21)
)
ciscoCtrlGroupRev8.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPFECType"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPSelector"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPReplyMode"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPTTL"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPExp"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlRttType"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlVrfName"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlTag"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlThreshold"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlTimeout"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlScanInterval"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlDelScanFactor"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlEXP"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlRequestSize"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlVerifyData"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlStorageType"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlProbeList"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlStatus"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeInterval"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeNumPackets"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeDestPort"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeSecFreqType"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeSecFreqValue"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLspSelector"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLSPReplyMode"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLSPTTL"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonScheduleRttStartTime"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonSchedulePeriod"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonScheduleFrequency"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactConnectionEnable"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactTimeoutEnable"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactThresholdType"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactThresholdCount"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactActionType"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev8.setStatus("current")

ciscoStatsGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 22)
)
ciscoStatsGroupRev5.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonJitterStatsIAJOut"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsIAJIn"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsAvgJitter"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsAvgJitterSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsAvgJitterDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsUnSyncRTs"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperIAJIn"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperIAJOut"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperAvgJitter"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperAvgSDJ"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperAvgDSJ"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWAvgSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWAvgDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNTPState"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperUnSyncRTs"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev5.setStatus("current")

ciscoCtrlGroupRev9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 23)
)
ciscoCtrlGroupRev9.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminPrecision"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProbePakPriority"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOWNTPSyncTolAbs"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOWNTPSyncTolPct"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOWNTPSyncTolType"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCalledNumber"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminDetectPoint"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminGKRegistration"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev9.setStatus("current")

ciscoCtrlGroupRev10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 24)
)
ciscoCtrlGroupRev10.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminOwner"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminRttType"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminThreshold"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminFrequency"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminVerifyData"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminNvgen"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProtocol"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataRequestSize"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataResponseSize"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminConceptRowAgeout"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHourGroups"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHops"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumDistBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminDistInterval"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumLives"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumSamples"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminFilter"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperModificationTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperDiagText"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperResetTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOctetsInUse"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperVerifyErrorOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperNumRtts"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperState"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerOperState"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev10.setStatus("deprecated")

ciscoCtrlGroupRev11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 25)
)
ciscoCtrlGroupRev11.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonReactVar"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdType"),
        ("CISCO-RTTMON-MIB", "rttMonReactActionType"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdRising"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdCountX"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdCountY"),
        ("CISCO-RTTMON-MIB", "rttMonReactValue"),
        ("CISCO-RTTMON-MIB", "rttMonReactOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonReactStatus"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminFreqMax"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminFreqMin"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev11.setStatus("current")

ciscoCtrlGroupRev12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 27)
)
ciscoCtrlGroupRev12.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminSourceVoicePort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCallDuration"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev12.setStatus("current")

ciscoCtrlGroupRev13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 29)
)
ciscoCtrlGroupRev13.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPReplyDscp"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPNullShim"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlLpd"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlLpdGrpList"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlLpdCompTime"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLSPReplyDscp"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdMaxSessions"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdSessTimeout"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdEchoTimeout"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdEchoInterval"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdEchoNullShim"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdScanPeriod"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonTypeLpdStatHours"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactLpdNotifyType"),
        ("CISCO-RTTMON-MIB", "rttMplsVpnMonReactLpdRetryCount"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev13.setStatus("current")

ciscoStatsGroupRev7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 30)
)
ciscoStatsGroupRev7.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsTargetPE"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsNumOfPass"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsNumOfFail"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsNumOfTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsAvgRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsMinRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsMaxRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsMinNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsMaxNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDFailOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDFailCause"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDCompTime"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsGroupStatus"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsGroupProbeIndex"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsProbeStatus"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsPathIds"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsResetTime"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev7.setStatus("current")

ciscoApplGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 32)
)
ciscoApplGroupRev4.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonApplLpdGrpStatsReset")
)
if mibBuilder.loadTexts:
    ciscoApplGroupRev4.setStatus("current")

ciscoCtrlGroupRev14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 33)
)
ciscoCtrlGroupRev14.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminAdd"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminDelete"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminReset"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev14.setStatus("current")

ciscoCtrlGroupRev15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 34)
)
ciscoCtrlGroupRev15.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetMPID"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetDomainName"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetVLAN"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminEthernetCOS"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev15.setStatus("current")

ciscoRttMonObsoleteGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 35)
)
ciscoRttMonObsoleteGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonApplPreConfigedReset"),
        ("CISCO-RTTMON-MIB", "rttMonApplPreConfigedValid"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminFilePath"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminSize"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminAction"),
        ("CISCO-RTTMON-MIB", "rttMonScriptAdminName"),
        ("CISCO-RTTMON-MIB", "rttMonScriptAdminCmdLineParams"))
)
if mibBuilder.loadTexts:
    ciscoRttMonObsoleteGroupRev1.setStatus("obsolete")

ciscoRttMonDeprecatedGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 36)
)
ciscoRttMonDeprecatedGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMinSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMaxSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMinDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWMaxDS"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminConnectionEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminTimeoutEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdType"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount2"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminActionType"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminVerifyErrorEnable"))
)
if mibBuilder.loadTexts:
    ciscoRttMonDeprecatedGroupRev1.setStatus("deprecated")

ciscoCtrlGroupRev16 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 37)
)
ciscoCtrlGroupRev16.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPVccvID")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev16.setStatus("current")

ciscoCtrlGroupRev17 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 38)
)
ciscoCtrlGroupRev17.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonCtrlAdminGroupName")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev17.setStatus("current")

ciscoCtrlGroupRev18 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 39)
)
ciscoCtrlGroupRev18.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetEVC")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev18.setStatus("current")

ciscoStatsGroupRev8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 40)
)
ciscoStatsGroupRev8.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSumHigh"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSum2High"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSumSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSum2SDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSumDSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperOWSum2DSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSumHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSumSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOWSumDSHigh"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev8.setStatus("current")

ciscoCtrlGroupRev19 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 41)
)
ciscoCtrlGroupRev19.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetMEPPort")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev19.setStatus("current")

ciscoCtrlGroupRev20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 43)
)
ciscoCtrlGroupRev20.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminVideoTrafficProfile")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev20.setStatus("current")

ciscoCtrlGroupRev21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 44)
)
ciscoCtrlGroupRev21.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminDscp"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminReserveDsp"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminInputInterface"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev21.setStatus("current")

ciscoCtrlGroupRev22 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 45)
)
ciscoCtrlGroupRev22.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminEmulateSourceAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminEmulateSourcePort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminEmulateTargetAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminEmulateTargetPort"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev22.setStatus("current")

ciscoCtrlGroupRev23 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 46)
)
ciscoCtrlGroupRev23.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetMacAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourceMacAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourceMPID"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev23.setStatus("current")

ciscoCtrlGroupRev24 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 47)
)
ciscoCtrlGroupRev24.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonGeneratedOperCtrlAdminIndex")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev24.setStatus("current")

ciscoCtrlGroupRev25 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 48)
)
ciscoCtrlGroupRev25.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminEndPointListName"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSSM"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminControlRetry"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminControlTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminIgmpTreeInit"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev25.setStatus("current")

ciscoStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 49)
)
ciscoStatsGroupRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonControlEnableErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsRetrieveErrors"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev2.setStatus("deprecated")

ciscoCtrlGroupRev26 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 50)
)
ciscoCtrlGroupRev26.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminEnableBurst"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminAggBurstCycles"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLossRatioNumFrames"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminAvailNumFrames"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev26.setStatus("current")

ciscoCtrlGroupRev27 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 51)
)
ciscoCtrlGroupRev27.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonEchoAdminTstampOptimization")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev27.setStatus("current")

ciscoCtrlGroupRev28 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 52)
)
ciscoCtrlGroupRev28.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminOwner"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminRttType"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminThreshold"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminFrequency"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminVerifyData"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminNvgen"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProtocol"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataRequestSize"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataResponseSize"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHourGroups"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHops"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumDistBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminDistInterval"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumLives"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumSamples"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminFilter"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperModificationTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperDiagText"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperResetTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOctetsInUse"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperVerifyErrorOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperNumRtts"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperState"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerOperState"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminConceptRowAgeoutV2"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev28.setStatus("current")

ciscoStatsGroupRev9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 53)
)
ciscoStatsGroupRev9.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonStatsCollectCtrlEnErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectRetrieveErrors"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev9.setStatus("current")

ciscoCtrlGroupRev29 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 54)
)
ciscoCtrlGroupRev29.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetSwitchId"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProfileId"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOutputInterface"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev29.setStatus("current")

ciscoCtrlGroupRev30 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 56)
)
ciscoCtrlGroupRev30.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonScheduleAdminStartType"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminStartDelay"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminStartType"),
        ("CISCO-RTTMON-MIB", "rttMonGrpScheduleAdminStartDelay"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev30.setStatus("current")

ciscoCtrlGroupRev31 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 57)
)
ciscoCtrlGroupRev31.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonCtrlAdminLongTag")
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev31.setStatus("current")

ciscoStatsGroupRev10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 58)
)
ciscoStatsGroupRev10.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOverThresh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOverThresh"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev10.setStatus("current")


# Notification objects

rttMonConnectionChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 1)
)
rttMonConnectionChangeNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"))
)
if mibBuilder.loadTexts:
    rttMonConnectionChangeNotification.setStatus(
        "deprecated"
    )

rttMonTimeoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 2)
)
rttMonTimeoutNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"))
)
if mibBuilder.loadTexts:
    rttMonTimeoutNotification.setStatus(
        "deprecated"
    )

rttMonThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 3)
)
rttMonThresholdNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"))
)
if mibBuilder.loadTexts:
    rttMonThresholdNotification.setStatus(
        "deprecated"
    )

rttMonVerifyErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 4)
)
rttMonVerifyErrorNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperVerifyErrorOccurred"))
)
if mibBuilder.loadTexts:
    rttMonVerifyErrorNotification.setStatus(
        "deprecated"
    )

rttMonNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 5)
)
rttMonNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactVar"),
        ("CISCO-RTTMON-MIB", "rttMonReactOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonReactValue"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdRising"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPSelector"))
)
if mibBuilder.loadTexts:
    rttMonNotification.setStatus(
        "deprecated"
    )

rttMonLpdDiscoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 6)
)
rttMonLpdDiscoveryNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlTag"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsTargetPE"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDFailCause"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsLPDFailOccurred"))
)
if mibBuilder.loadTexts:
    rttMonLpdDiscoveryNotification.setStatus(
        "current"
    )

rttMonLpdGrpStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 7)
)
rttMonLpdGrpStatusNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMplsVpnMonCtrlTag"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsTargetPE"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatsGroupStatus"))
)
if mibBuilder.loadTexts:
    rttMonLpdGrpStatusNotification.setStatus(
        "current"
    )

rttMonNotificationV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 8)
)
rttMonNotificationV2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminLongTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactVar"),
        ("CISCO-RTTMON-MIB", "rttMonReactOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonReactValue"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdRising"),
        ("CISCO-RTTMON-MIB", "rttMonReactThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSPSelector"))
)
if mibBuilder.loadTexts:
    rttMonNotificationV2.setStatus(
        "current"
    )


# Notifications groups

ciscoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 18)
)
ciscoNotificationGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonConnectionChangeNotification"),
        ("CISCO-RTTMON-MIB", "rttMonTimeoutNotification"),
        ("CISCO-RTTMON-MIB", "rttMonThresholdNotification"),
        ("CISCO-RTTMON-MIB", "rttMonVerifyErrorNotification"))
)
if mibBuilder.loadTexts:
    ciscoNotificationGroup.setStatus(
        "deprecated"
    )

ciscoNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 26)
)
ciscoNotificationGroupRev1.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonNotification")
)
if mibBuilder.loadTexts:
    ciscoNotificationGroupRev1.setStatus(
        "current"
    )

ciscoNotificationGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 31)
)
ciscoNotificationGroupRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLpdDiscoveryNotification"),
        ("CISCO-RTTMON-MIB", "rttMonLpdGrpStatusNotification"))
)
if mibBuilder.loadTexts:
    ciscoNotificationGroupRev2.setStatus(
        "current"
    )

ciscoNotificationGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 55)
)
ciscoNotificationGroupRev3.setObjects(
    ("CISCO-RTTMON-MIB", "rttMonNotificationV2")
)
if mibBuilder.loadTexts:
    ciscoNotificationGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRttMonMibComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev12.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 13)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev13.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 14)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev14.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 15)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev15.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 16)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev16.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 17)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev17.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 18)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev18.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 19)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev19.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 20)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev20.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 21)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev21.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 22)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev22.setStatus(
        "deprecated"
    )

ciscoRttMonMibComplianceRev23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 23)
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev23.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-MIB",
    **{"ciscoRttMonMIB": ciscoRttMonMIB,
       "ciscoRttMonObjects": ciscoRttMonObjects,
       "rttMonAppl": rttMonAppl,
       "rttMonApplVersion": rttMonApplVersion,
       "rttMonApplMaxPacketDataSize": rttMonApplMaxPacketDataSize,
       "rttMonApplTimeOfLastSet": rttMonApplTimeOfLastSet,
       "rttMonApplNumCtrlAdminEntry": rttMonApplNumCtrlAdminEntry,
       "rttMonApplReset": rttMonApplReset,
       "rttMonApplPreConfigedReset": rttMonApplPreConfigedReset,
       "rttMonApplSupportedRttTypesTable": rttMonApplSupportedRttTypesTable,
       "rttMonApplSupportedRttTypesEntry": rttMonApplSupportedRttTypesEntry,
       "rttMonApplSupportedRttTypes": rttMonApplSupportedRttTypes,
       "rttMonApplSupportedRttTypesValid": rttMonApplSupportedRttTypesValid,
       "rttMonApplSupportedProtocolsTable": rttMonApplSupportedProtocolsTable,
       "rttMonApplSupportedProtocolsEntry": rttMonApplSupportedProtocolsEntry,
       "rttMonApplSupportedProtocols": rttMonApplSupportedProtocols,
       "rttMonApplSupportedProtocolsValid": rttMonApplSupportedProtocolsValid,
       "rttMonApplPreConfigedTable": rttMonApplPreConfigedTable,
       "rttMonApplPreConfigedEntry": rttMonApplPreConfigedEntry,
       "rttMonApplPreConfigedType": rttMonApplPreConfigedType,
       "rttMonApplPreConfigedName": rttMonApplPreConfigedName,
       "rttMonApplPreConfigedValid": rttMonApplPreConfigedValid,
       "rttMonApplProbeCapacity": rttMonApplProbeCapacity,
       "rttMonApplFreeMemLowWaterMark": rttMonApplFreeMemLowWaterMark,
       "rttMonApplLatestSetError": rttMonApplLatestSetError,
       "rttMonApplResponder": rttMonApplResponder,
       "rttMonApplAuthTable": rttMonApplAuthTable,
       "rttMonApplAuthEntry": rttMonApplAuthEntry,
       "rttMonApplAuthIndex": rttMonApplAuthIndex,
       "rttMonApplAuthKeyChain": rttMonApplAuthKeyChain,
       "rttMonApplAuthKeyString1": rttMonApplAuthKeyString1,
       "rttMonApplAuthKeyString2": rttMonApplAuthKeyString2,
       "rttMonApplAuthKeyString3": rttMonApplAuthKeyString3,
       "rttMonApplAuthKeyString4": rttMonApplAuthKeyString4,
       "rttMonApplAuthKeyString5": rttMonApplAuthKeyString5,
       "rttMonApplAuthStatus": rttMonApplAuthStatus,
       "rttMonApplLpdGrpStatsReset": rttMonApplLpdGrpStatsReset,
       "rttMonCtrl": rttMonCtrl,
       "rttMonCtrlAdminTable": rttMonCtrlAdminTable,
       "rttMonCtrlAdminEntry": rttMonCtrlAdminEntry,
       "rttMonCtrlAdminIndex": rttMonCtrlAdminIndex,
       "rttMonCtrlAdminOwner": rttMonCtrlAdminOwner,
       "rttMonCtrlAdminTag": rttMonCtrlAdminTag,
       "rttMonCtrlAdminRttType": rttMonCtrlAdminRttType,
       "rttMonCtrlAdminThreshold": rttMonCtrlAdminThreshold,
       "rttMonCtrlAdminFrequency": rttMonCtrlAdminFrequency,
       "rttMonCtrlAdminTimeout": rttMonCtrlAdminTimeout,
       "rttMonCtrlAdminVerifyData": rttMonCtrlAdminVerifyData,
       "rttMonCtrlAdminStatus": rttMonCtrlAdminStatus,
       "rttMonCtrlAdminNvgen": rttMonCtrlAdminNvgen,
       "rttMonCtrlAdminGroupName": rttMonCtrlAdminGroupName,
       "rttMonCtrlAdminLongTag": rttMonCtrlAdminLongTag,
       "rttMonEchoAdminTable": rttMonEchoAdminTable,
       "rttMonEchoAdminEntry": rttMonEchoAdminEntry,
       "rttMonEchoAdminProtocol": rttMonEchoAdminProtocol,
       "rttMonEchoAdminTargetAddress": rttMonEchoAdminTargetAddress,
       "rttMonEchoAdminPktDataRequestSize": rttMonEchoAdminPktDataRequestSize,
       "rttMonEchoAdminPktDataResponseSize": rttMonEchoAdminPktDataResponseSize,
       "rttMonEchoAdminTargetPort": rttMonEchoAdminTargetPort,
       "rttMonEchoAdminSourceAddress": rttMonEchoAdminSourceAddress,
       "rttMonEchoAdminSourcePort": rttMonEchoAdminSourcePort,
       "rttMonEchoAdminControlEnable": rttMonEchoAdminControlEnable,
       "rttMonEchoAdminTOS": rttMonEchoAdminTOS,
       "rttMonEchoAdminLSREnable": rttMonEchoAdminLSREnable,
       "rttMonEchoAdminTargetAddressString": rttMonEchoAdminTargetAddressString,
       "rttMonEchoAdminNameServer": rttMonEchoAdminNameServer,
       "rttMonEchoAdminOperation": rttMonEchoAdminOperation,
       "rttMonEchoAdminHTTPVersion": rttMonEchoAdminHTTPVersion,
       "rttMonEchoAdminURL": rttMonEchoAdminURL,
       "rttMonEchoAdminCache": rttMonEchoAdminCache,
       "rttMonEchoAdminInterval": rttMonEchoAdminInterval,
       "rttMonEchoAdminNumPackets": rttMonEchoAdminNumPackets,
       "rttMonEchoAdminProxy": rttMonEchoAdminProxy,
       "rttMonEchoAdminString1": rttMonEchoAdminString1,
       "rttMonEchoAdminString2": rttMonEchoAdminString2,
       "rttMonEchoAdminString3": rttMonEchoAdminString3,
       "rttMonEchoAdminString4": rttMonEchoAdminString4,
       "rttMonEchoAdminString5": rttMonEchoAdminString5,
       "rttMonEchoAdminMode": rttMonEchoAdminMode,
       "rttMonEchoAdminVrfName": rttMonEchoAdminVrfName,
       "rttMonEchoAdminCodecType": rttMonEchoAdminCodecType,
       "rttMonEchoAdminCodecInterval": rttMonEchoAdminCodecInterval,
       "rttMonEchoAdminCodecPayload": rttMonEchoAdminCodecPayload,
       "rttMonEchoAdminCodecNumPackets": rttMonEchoAdminCodecNumPackets,
       "rttMonEchoAdminICPIFAdvFactor": rttMonEchoAdminICPIFAdvFactor,
       "rttMonEchoAdminLSPFECType": rttMonEchoAdminLSPFECType,
       "rttMonEchoAdminLSPSelector": rttMonEchoAdminLSPSelector,
       "rttMonEchoAdminLSPReplyMode": rttMonEchoAdminLSPReplyMode,
       "rttMonEchoAdminLSPTTL": rttMonEchoAdminLSPTTL,
       "rttMonEchoAdminLSPExp": rttMonEchoAdminLSPExp,
       "rttMonEchoAdminPrecision": rttMonEchoAdminPrecision,
       "rttMonEchoAdminProbePakPriority": rttMonEchoAdminProbePakPriority,
       "rttMonEchoAdminOWNTPSyncTolAbs": rttMonEchoAdminOWNTPSyncTolAbs,
       "rttMonEchoAdminOWNTPSyncTolPct": rttMonEchoAdminOWNTPSyncTolPct,
       "rttMonEchoAdminOWNTPSyncTolType": rttMonEchoAdminOWNTPSyncTolType,
       "rttMonEchoAdminCalledNumber": rttMonEchoAdminCalledNumber,
       "rttMonEchoAdminDetectPoint": rttMonEchoAdminDetectPoint,
       "rttMonEchoAdminGKRegistration": rttMonEchoAdminGKRegistration,
       "rttMonEchoAdminSourceVoicePort": rttMonEchoAdminSourceVoicePort,
       "rttMonEchoAdminCallDuration": rttMonEchoAdminCallDuration,
       "rttMonEchoAdminLSPReplyDscp": rttMonEchoAdminLSPReplyDscp,
       "rttMonEchoAdminLSPNullShim": rttMonEchoAdminLSPNullShim,
       "rttMonEchoAdminTargetMPID": rttMonEchoAdminTargetMPID,
       "rttMonEchoAdminTargetDomainName": rttMonEchoAdminTargetDomainName,
       "rttMonEchoAdminTargetVLAN": rttMonEchoAdminTargetVLAN,
       "rttMonEchoAdminEthernetCOS": rttMonEchoAdminEthernetCOS,
       "rttMonEchoAdminLSPVccvID": rttMonEchoAdminLSPVccvID,
       "rttMonEchoAdminTargetEVC": rttMonEchoAdminTargetEVC,
       "rttMonEchoAdminTargetMEPPort": rttMonEchoAdminTargetMEPPort,
       "rttMonEchoAdminVideoTrafficProfile": rttMonEchoAdminVideoTrafficProfile,
       "rttMonEchoAdminDscp": rttMonEchoAdminDscp,
       "rttMonEchoAdminReserveDsp": rttMonEchoAdminReserveDsp,
       "rttMonEchoAdminInputInterface": rttMonEchoAdminInputInterface,
       "rttMonEchoAdminEmulateSourceAddress": rttMonEchoAdminEmulateSourceAddress,
       "rttMonEchoAdminEmulateSourcePort": rttMonEchoAdminEmulateSourcePort,
       "rttMonEchoAdminEmulateTargetAddress": rttMonEchoAdminEmulateTargetAddress,
       "rttMonEchoAdminEmulateTargetPort": rttMonEchoAdminEmulateTargetPort,
       "rttMonEchoAdminTargetMacAddress": rttMonEchoAdminTargetMacAddress,
       "rttMonEchoAdminSourceMacAddress": rttMonEchoAdminSourceMacAddress,
       "rttMonEchoAdminSourceMPID": rttMonEchoAdminSourceMPID,
       "rttMonEchoAdminEndPointListName": rttMonEchoAdminEndPointListName,
       "rttMonEchoAdminSSM": rttMonEchoAdminSSM,
       "rttMonEchoAdminControlRetry": rttMonEchoAdminControlRetry,
       "rttMonEchoAdminControlTimeout": rttMonEchoAdminControlTimeout,
       "rttMonEchoAdminIgmpTreeInit": rttMonEchoAdminIgmpTreeInit,
       "rttMonEchoAdminEnableBurst": rttMonEchoAdminEnableBurst,
       "rttMonEchoAdminAggBurstCycles": rttMonEchoAdminAggBurstCycles,
       "rttMonEchoAdminLossRatioNumFrames": rttMonEchoAdminLossRatioNumFrames,
       "rttMonEchoAdminAvailNumFrames": rttMonEchoAdminAvailNumFrames,
       "rttMonEchoAdminTstampOptimization": rttMonEchoAdminTstampOptimization,
       "rttMonEchoAdminTargetSwitchId": rttMonEchoAdminTargetSwitchId,
       "rttMonEchoAdminProfileId": rttMonEchoAdminProfileId,
       "rttMonEchoAdminOutputInterface": rttMonEchoAdminOutputInterface,
       "rttMonFileIOAdminTable": rttMonFileIOAdminTable,
       "rttMonFileIOAdminEntry": rttMonFileIOAdminEntry,
       "rttMonFileIOAdminFilePath": rttMonFileIOAdminFilePath,
       "rttMonFileIOAdminSize": rttMonFileIOAdminSize,
       "rttMonFileIOAdminAction": rttMonFileIOAdminAction,
       "rttMonScriptAdminTable": rttMonScriptAdminTable,
       "rttMonScriptAdminEntry": rttMonScriptAdminEntry,
       "rttMonScriptAdminName": rttMonScriptAdminName,
       "rttMonScriptAdminCmdLineParams": rttMonScriptAdminCmdLineParams,
       "rttMonScheduleAdminTable": rttMonScheduleAdminTable,
       "rttMonScheduleAdminEntry": rttMonScheduleAdminEntry,
       "rttMonScheduleAdminRttLife": rttMonScheduleAdminRttLife,
       "rttMonScheduleAdminRttStartTime": rttMonScheduleAdminRttStartTime,
       "rttMonScheduleAdminConceptRowAgeout": rttMonScheduleAdminConceptRowAgeout,
       "rttMonScheduleAdminRttRecurring": rttMonScheduleAdminRttRecurring,
       "rttMonScheduleAdminConceptRowAgeoutV2": rttMonScheduleAdminConceptRowAgeoutV2,
       "rttMonScheduleAdminStartType": rttMonScheduleAdminStartType,
       "rttMonScheduleAdminStartDelay": rttMonScheduleAdminStartDelay,
       "rttMonReactAdminTable": rttMonReactAdminTable,
       "rttMonReactAdminEntry": rttMonReactAdminEntry,
       "rttMonReactAdminConnectionEnable": rttMonReactAdminConnectionEnable,
       "rttMonReactAdminTimeoutEnable": rttMonReactAdminTimeoutEnable,
       "rttMonReactAdminThresholdType": rttMonReactAdminThresholdType,
       "rttMonReactAdminThresholdFalling": rttMonReactAdminThresholdFalling,
       "rttMonReactAdminThresholdCount": rttMonReactAdminThresholdCount,
       "rttMonReactAdminThresholdCount2": rttMonReactAdminThresholdCount2,
       "rttMonReactAdminActionType": rttMonReactAdminActionType,
       "rttMonReactAdminVerifyErrorEnable": rttMonReactAdminVerifyErrorEnable,
       "rttMonStatisticsAdminTable": rttMonStatisticsAdminTable,
       "rttMonStatisticsAdminEntry": rttMonStatisticsAdminEntry,
       "rttMonStatisticsAdminNumHourGroups": rttMonStatisticsAdminNumHourGroups,
       "rttMonStatisticsAdminNumPaths": rttMonStatisticsAdminNumPaths,
       "rttMonStatisticsAdminNumHops": rttMonStatisticsAdminNumHops,
       "rttMonStatisticsAdminNumDistBuckets": rttMonStatisticsAdminNumDistBuckets,
       "rttMonStatisticsAdminDistInterval": rttMonStatisticsAdminDistInterval,
       "rttMonHistoryAdminTable": rttMonHistoryAdminTable,
       "rttMonHistoryAdminEntry": rttMonHistoryAdminEntry,
       "rttMonHistoryAdminNumLives": rttMonHistoryAdminNumLives,
       "rttMonHistoryAdminNumBuckets": rttMonHistoryAdminNumBuckets,
       "rttMonHistoryAdminNumSamples": rttMonHistoryAdminNumSamples,
       "rttMonHistoryAdminFilter": rttMonHistoryAdminFilter,
       "rttMonCtrlOperTable": rttMonCtrlOperTable,
       "rttMonCtrlOperEntry": rttMonCtrlOperEntry,
       "rttMonCtrlOperModificationTime": rttMonCtrlOperModificationTime,
       "rttMonCtrlOperDiagText": rttMonCtrlOperDiagText,
       "rttMonCtrlOperResetTime": rttMonCtrlOperResetTime,
       "rttMonCtrlOperOctetsInUse": rttMonCtrlOperOctetsInUse,
       "rttMonCtrlOperConnectionLostOccurred": rttMonCtrlOperConnectionLostOccurred,
       "rttMonCtrlOperTimeoutOccurred": rttMonCtrlOperTimeoutOccurred,
       "rttMonCtrlOperOverThresholdOccurred": rttMonCtrlOperOverThresholdOccurred,
       "rttMonCtrlOperNumRtts": rttMonCtrlOperNumRtts,
       "rttMonCtrlOperRttLife": rttMonCtrlOperRttLife,
       "rttMonCtrlOperState": rttMonCtrlOperState,
       "rttMonCtrlOperVerifyErrorOccurred": rttMonCtrlOperVerifyErrorOccurred,
       "rttMonLatestRttOperTable": rttMonLatestRttOperTable,
       "rttMonLatestRttOperEntry": rttMonLatestRttOperEntry,
       "rttMonLatestRttOperCompletionTime": rttMonLatestRttOperCompletionTime,
       "rttMonLatestRttOperSense": rttMonLatestRttOperSense,
       "rttMonLatestRttOperApplSpecificSense": rttMonLatestRttOperApplSpecificSense,
       "rttMonLatestRttOperSenseDescription": rttMonLatestRttOperSenseDescription,
       "rttMonLatestRttOperTime": rttMonLatestRttOperTime,
       "rttMonLatestRttOperAddress": rttMonLatestRttOperAddress,
       "rttMonReactTriggerAdminTable": rttMonReactTriggerAdminTable,
       "rttMonReactTriggerAdminEntry": rttMonReactTriggerAdminEntry,
       "rttMonReactTriggerAdminRttMonCtrlAdminIndex": rttMonReactTriggerAdminRttMonCtrlAdminIndex,
       "rttMonReactTriggerAdminStatus": rttMonReactTriggerAdminStatus,
       "rttMonReactTriggerOperTable": rttMonReactTriggerOperTable,
       "rttMonReactTriggerOperEntry": rttMonReactTriggerOperEntry,
       "rttMonReactTriggerOperState": rttMonReactTriggerOperState,
       "rttMonEchoPathAdminTable": rttMonEchoPathAdminTable,
       "rttMonEchoPathAdminEntry": rttMonEchoPathAdminEntry,
       "rttMonEchoPathAdminHopIndex": rttMonEchoPathAdminHopIndex,
       "rttMonEchoPathAdminHopAddress": rttMonEchoPathAdminHopAddress,
       "rttMonGrpScheduleAdminTable": rttMonGrpScheduleAdminTable,
       "rttMonGrpScheduleAdminEntry": rttMonGrpScheduleAdminEntry,
       "rttMonGrpScheduleAdminIndex": rttMonGrpScheduleAdminIndex,
       "rttMonGrpScheduleAdminProbes": rttMonGrpScheduleAdminProbes,
       "rttMonGrpScheduleAdminPeriod": rttMonGrpScheduleAdminPeriod,
       "rttMonGrpScheduleAdminFrequency": rttMonGrpScheduleAdminFrequency,
       "rttMonGrpScheduleAdminLife": rttMonGrpScheduleAdminLife,
       "rttMonGrpScheduleAdminAgeout": rttMonGrpScheduleAdminAgeout,
       "rttMonGrpScheduleAdminStatus": rttMonGrpScheduleAdminStatus,
       "rttMonGrpScheduleAdminFreqMax": rttMonGrpScheduleAdminFreqMax,
       "rttMonGrpScheduleAdminFreqMin": rttMonGrpScheduleAdminFreqMin,
       "rttMonGrpScheduleAdminStartTime": rttMonGrpScheduleAdminStartTime,
       "rttMonGrpScheduleAdminAdd": rttMonGrpScheduleAdminAdd,
       "rttMonGrpScheduleAdminDelete": rttMonGrpScheduleAdminDelete,
       "rttMonGrpScheduleAdminReset": rttMonGrpScheduleAdminReset,
       "rttMonGrpScheduleAdminStartType": rttMonGrpScheduleAdminStartType,
       "rttMonGrpScheduleAdminStartDelay": rttMonGrpScheduleAdminStartDelay,
       "rttMplsVpnMonCtrlTable": rttMplsVpnMonCtrlTable,
       "rttMplsVpnMonCtrlEntry": rttMplsVpnMonCtrlEntry,
       "rttMplsVpnMonCtrlIndex": rttMplsVpnMonCtrlIndex,
       "rttMplsVpnMonCtrlRttType": rttMplsVpnMonCtrlRttType,
       "rttMplsVpnMonCtrlVrfName": rttMplsVpnMonCtrlVrfName,
       "rttMplsVpnMonCtrlTag": rttMplsVpnMonCtrlTag,
       "rttMplsVpnMonCtrlThreshold": rttMplsVpnMonCtrlThreshold,
       "rttMplsVpnMonCtrlTimeout": rttMplsVpnMonCtrlTimeout,
       "rttMplsVpnMonCtrlScanInterval": rttMplsVpnMonCtrlScanInterval,
       "rttMplsVpnMonCtrlDelScanFactor": rttMplsVpnMonCtrlDelScanFactor,
       "rttMplsVpnMonCtrlEXP": rttMplsVpnMonCtrlEXP,
       "rttMplsVpnMonCtrlRequestSize": rttMplsVpnMonCtrlRequestSize,
       "rttMplsVpnMonCtrlVerifyData": rttMplsVpnMonCtrlVerifyData,
       "rttMplsVpnMonCtrlStorageType": rttMplsVpnMonCtrlStorageType,
       "rttMplsVpnMonCtrlProbeList": rttMplsVpnMonCtrlProbeList,
       "rttMplsVpnMonCtrlStatus": rttMplsVpnMonCtrlStatus,
       "rttMplsVpnMonCtrlLpd": rttMplsVpnMonCtrlLpd,
       "rttMplsVpnMonCtrlLpdGrpList": rttMplsVpnMonCtrlLpdGrpList,
       "rttMplsVpnMonCtrlLpdCompTime": rttMplsVpnMonCtrlLpdCompTime,
       "rttMplsVpnMonTypeTable": rttMplsVpnMonTypeTable,
       "rttMplsVpnMonTypeEntry": rttMplsVpnMonTypeEntry,
       "rttMplsVpnMonTypeInterval": rttMplsVpnMonTypeInterval,
       "rttMplsVpnMonTypeNumPackets": rttMplsVpnMonTypeNumPackets,
       "rttMplsVpnMonTypeDestPort": rttMplsVpnMonTypeDestPort,
       "rttMplsVpnMonTypeSecFreqType": rttMplsVpnMonTypeSecFreqType,
       "rttMplsVpnMonTypeSecFreqValue": rttMplsVpnMonTypeSecFreqValue,
       "rttMplsVpnMonTypeLspSelector": rttMplsVpnMonTypeLspSelector,
       "rttMplsVpnMonTypeLSPReplyMode": rttMplsVpnMonTypeLSPReplyMode,
       "rttMplsVpnMonTypeLSPTTL": rttMplsVpnMonTypeLSPTTL,
       "rttMplsVpnMonTypeLSPReplyDscp": rttMplsVpnMonTypeLSPReplyDscp,
       "rttMplsVpnMonTypeLpdMaxSessions": rttMplsVpnMonTypeLpdMaxSessions,
       "rttMplsVpnMonTypeLpdSessTimeout": rttMplsVpnMonTypeLpdSessTimeout,
       "rttMplsVpnMonTypeLpdEchoTimeout": rttMplsVpnMonTypeLpdEchoTimeout,
       "rttMplsVpnMonTypeLpdEchoInterval": rttMplsVpnMonTypeLpdEchoInterval,
       "rttMplsVpnMonTypeLpdEchoNullShim": rttMplsVpnMonTypeLpdEchoNullShim,
       "rttMplsVpnMonTypeLpdScanPeriod": rttMplsVpnMonTypeLpdScanPeriod,
       "rttMplsVpnMonTypeLpdStatHours": rttMplsVpnMonTypeLpdStatHours,
       "rttMplsVpnMonScheduleTable": rttMplsVpnMonScheduleTable,
       "rttMplsVpnMonScheduleEntry": rttMplsVpnMonScheduleEntry,
       "rttMplsVpnMonScheduleRttStartTime": rttMplsVpnMonScheduleRttStartTime,
       "rttMplsVpnMonSchedulePeriod": rttMplsVpnMonSchedulePeriod,
       "rttMplsVpnMonScheduleFrequency": rttMplsVpnMonScheduleFrequency,
       "rttMplsVpnMonReactTable": rttMplsVpnMonReactTable,
       "rttMplsVpnMonReactEntry": rttMplsVpnMonReactEntry,
       "rttMplsVpnMonReactConnectionEnable": rttMplsVpnMonReactConnectionEnable,
       "rttMplsVpnMonReactTimeoutEnable": rttMplsVpnMonReactTimeoutEnable,
       "rttMplsVpnMonReactThresholdType": rttMplsVpnMonReactThresholdType,
       "rttMplsVpnMonReactThresholdCount": rttMplsVpnMonReactThresholdCount,
       "rttMplsVpnMonReactActionType": rttMplsVpnMonReactActionType,
       "rttMplsVpnMonReactLpdNotifyType": rttMplsVpnMonReactLpdNotifyType,
       "rttMplsVpnMonReactLpdRetryCount": rttMplsVpnMonReactLpdRetryCount,
       "rttMonReactTable": rttMonReactTable,
       "rttMonReactEntry": rttMonReactEntry,
       "rttMonReactConfigIndex": rttMonReactConfigIndex,
       "rttMonReactVar": rttMonReactVar,
       "rttMonReactThresholdType": rttMonReactThresholdType,
       "rttMonReactActionType": rttMonReactActionType,
       "rttMonReactThresholdRising": rttMonReactThresholdRising,
       "rttMonReactThresholdFalling": rttMonReactThresholdFalling,
       "rttMonReactThresholdCountX": rttMonReactThresholdCountX,
       "rttMonReactThresholdCountY": rttMonReactThresholdCountY,
       "rttMonReactValue": rttMonReactValue,
       "rttMonReactOccurred": rttMonReactOccurred,
       "rttMonReactStatus": rttMonReactStatus,
       "rttMonGeneratedOperTable": rttMonGeneratedOperTable,
       "rttMonGeneratedOperEntry": rttMonGeneratedOperEntry,
       "rttMonGeneratedOperRespIpAddrType": rttMonGeneratedOperRespIpAddrType,
       "rttMonGeneratedOperRespIpAddr": rttMonGeneratedOperRespIpAddr,
       "rttMonGeneratedOperCtrlAdminIndex": rttMonGeneratedOperCtrlAdminIndex,
       "rttMonStats": rttMonStats,
       "rttMonStatsCaptureTable": rttMonStatsCaptureTable,
       "rttMonStatsCaptureEntry": rttMonStatsCaptureEntry,
       "rttMonStatsCaptureStartTimeIndex": rttMonStatsCaptureStartTimeIndex,
       "rttMonStatsCapturePathIndex": rttMonStatsCapturePathIndex,
       "rttMonStatsCaptureHopIndex": rttMonStatsCaptureHopIndex,
       "rttMonStatsCaptureDistIndex": rttMonStatsCaptureDistIndex,
       "rttMonStatsCaptureCompletions": rttMonStatsCaptureCompletions,
       "rttMonStatsCaptureOverThresholds": rttMonStatsCaptureOverThresholds,
       "rttMonStatsCaptureSumCompletionTime": rttMonStatsCaptureSumCompletionTime,
       "rttMonStatsCaptureSumCompletionTime2Low": rttMonStatsCaptureSumCompletionTime2Low,
       "rttMonStatsCaptureSumCompletionTime2High": rttMonStatsCaptureSumCompletionTime2High,
       "rttMonStatsCaptureCompletionTimeMax": rttMonStatsCaptureCompletionTimeMax,
       "rttMonStatsCaptureCompletionTimeMin": rttMonStatsCaptureCompletionTimeMin,
       "rttMonStatsCollectTable": rttMonStatsCollectTable,
       "rttMonStatsCollectEntry": rttMonStatsCollectEntry,
       "rttMonStatsCollectNumDisconnects": rttMonStatsCollectNumDisconnects,
       "rttMonStatsCollectTimeouts": rttMonStatsCollectTimeouts,
       "rttMonStatsCollectBusies": rttMonStatsCollectBusies,
       "rttMonStatsCollectNoConnections": rttMonStatsCollectNoConnections,
       "rttMonStatsCollectDrops": rttMonStatsCollectDrops,
       "rttMonStatsCollectSequenceErrors": rttMonStatsCollectSequenceErrors,
       "rttMonStatsCollectVerifyErrors": rttMonStatsCollectVerifyErrors,
       "rttMonStatsCollectAddress": rttMonStatsCollectAddress,
       "rttMonControlEnableErrors": rttMonControlEnableErrors,
       "rttMonStatsRetrieveErrors": rttMonStatsRetrieveErrors,
       "rttMonStatsCollectCtrlEnErrors": rttMonStatsCollectCtrlEnErrors,
       "rttMonStatsCollectRetrieveErrors": rttMonStatsCollectRetrieveErrors,
       "rttMonStatsTotalsTable": rttMonStatsTotalsTable,
       "rttMonStatsTotalsEntry": rttMonStatsTotalsEntry,
       "rttMonStatsTotalsElapsedTime": rttMonStatsTotalsElapsedTime,
       "rttMonStatsTotalsInitiations": rttMonStatsTotalsInitiations,
       "rttMonHTTPStatsTable": rttMonHTTPStatsTable,
       "rttMonHTTPStatsEntry": rttMonHTTPStatsEntry,
       "rttMonHTTPStatsStartTimeIndex": rttMonHTTPStatsStartTimeIndex,
       "rttMonHTTPStatsCompletions": rttMonHTTPStatsCompletions,
       "rttMonHTTPStatsOverThresholds": rttMonHTTPStatsOverThresholds,
       "rttMonHTTPStatsRTTSum": rttMonHTTPStatsRTTSum,
       "rttMonHTTPStatsRTTSum2Low": rttMonHTTPStatsRTTSum2Low,
       "rttMonHTTPStatsRTTSum2High": rttMonHTTPStatsRTTSum2High,
       "rttMonHTTPStatsRTTMin": rttMonHTTPStatsRTTMin,
       "rttMonHTTPStatsRTTMax": rttMonHTTPStatsRTTMax,
       "rttMonHTTPStatsDNSRTTSum": rttMonHTTPStatsDNSRTTSum,
       "rttMonHTTPStatsTCPConnectRTTSum": rttMonHTTPStatsTCPConnectRTTSum,
       "rttMonHTTPStatsTransactionRTTSum": rttMonHTTPStatsTransactionRTTSum,
       "rttMonHTTPStatsMessageBodyOctetsSum": rttMonHTTPStatsMessageBodyOctetsSum,
       "rttMonHTTPStatsDNSServerTimeout": rttMonHTTPStatsDNSServerTimeout,
       "rttMonHTTPStatsTCPConnectTimeout": rttMonHTTPStatsTCPConnectTimeout,
       "rttMonHTTPStatsTransactionTimeout": rttMonHTTPStatsTransactionTimeout,
       "rttMonHTTPStatsDNSQueryError": rttMonHTTPStatsDNSQueryError,
       "rttMonHTTPStatsHTTPError": rttMonHTTPStatsHTTPError,
       "rttMonHTTPStatsError": rttMonHTTPStatsError,
       "rttMonHTTPStatsBusies": rttMonHTTPStatsBusies,
       "rttMonJitterStatsTable": rttMonJitterStatsTable,
       "rttMonJitterStatsEntry": rttMonJitterStatsEntry,
       "rttMonJitterStatsStartTimeIndex": rttMonJitterStatsStartTimeIndex,
       "rttMonJitterStatsCompletions": rttMonJitterStatsCompletions,
       "rttMonJitterStatsOverThresholds": rttMonJitterStatsOverThresholds,
       "rttMonJitterStatsNumOfRTT": rttMonJitterStatsNumOfRTT,
       "rttMonJitterStatsRTTSum": rttMonJitterStatsRTTSum,
       "rttMonJitterStatsRTTSum2Low": rttMonJitterStatsRTTSum2Low,
       "rttMonJitterStatsRTTSum2High": rttMonJitterStatsRTTSum2High,
       "rttMonJitterStatsRTTMin": rttMonJitterStatsRTTMin,
       "rttMonJitterStatsRTTMax": rttMonJitterStatsRTTMax,
       "rttMonJitterStatsMinOfPositivesSD": rttMonJitterStatsMinOfPositivesSD,
       "rttMonJitterStatsMaxOfPositivesSD": rttMonJitterStatsMaxOfPositivesSD,
       "rttMonJitterStatsNumOfPositivesSD": rttMonJitterStatsNumOfPositivesSD,
       "rttMonJitterStatsSumOfPositivesSD": rttMonJitterStatsSumOfPositivesSD,
       "rttMonJitterStatsSum2PositivesSDLow": rttMonJitterStatsSum2PositivesSDLow,
       "rttMonJitterStatsSum2PositivesSDHigh": rttMonJitterStatsSum2PositivesSDHigh,
       "rttMonJitterStatsMinOfNegativesSD": rttMonJitterStatsMinOfNegativesSD,
       "rttMonJitterStatsMaxOfNegativesSD": rttMonJitterStatsMaxOfNegativesSD,
       "rttMonJitterStatsNumOfNegativesSD": rttMonJitterStatsNumOfNegativesSD,
       "rttMonJitterStatsSumOfNegativesSD": rttMonJitterStatsSumOfNegativesSD,
       "rttMonJitterStatsSum2NegativesSDLow": rttMonJitterStatsSum2NegativesSDLow,
       "rttMonJitterStatsSum2NegativesSDHigh": rttMonJitterStatsSum2NegativesSDHigh,
       "rttMonJitterStatsMinOfPositivesDS": rttMonJitterStatsMinOfPositivesDS,
       "rttMonJitterStatsMaxOfPositivesDS": rttMonJitterStatsMaxOfPositivesDS,
       "rttMonJitterStatsNumOfPositivesDS": rttMonJitterStatsNumOfPositivesDS,
       "rttMonJitterStatsSumOfPositivesDS": rttMonJitterStatsSumOfPositivesDS,
       "rttMonJitterStatsSum2PositivesDSLow": rttMonJitterStatsSum2PositivesDSLow,
       "rttMonJitterStatsSum2PositivesDSHigh": rttMonJitterStatsSum2PositivesDSHigh,
       "rttMonJitterStatsMinOfNegativesDS": rttMonJitterStatsMinOfNegativesDS,
       "rttMonJitterStatsMaxOfNegativesDS": rttMonJitterStatsMaxOfNegativesDS,
       "rttMonJitterStatsNumOfNegativesDS": rttMonJitterStatsNumOfNegativesDS,
       "rttMonJitterStatsSumOfNegativesDS": rttMonJitterStatsSumOfNegativesDS,
       "rttMonJitterStatsSum2NegativesDSLow": rttMonJitterStatsSum2NegativesDSLow,
       "rttMonJitterStatsSum2NegativesDSHigh": rttMonJitterStatsSum2NegativesDSHigh,
       "rttMonJitterStatsPacketLossSD": rttMonJitterStatsPacketLossSD,
       "rttMonJitterStatsPacketLossDS": rttMonJitterStatsPacketLossDS,
       "rttMonJitterStatsPacketOutOfSequence": rttMonJitterStatsPacketOutOfSequence,
       "rttMonJitterStatsPacketMIA": rttMonJitterStatsPacketMIA,
       "rttMonJitterStatsPacketLateArrival": rttMonJitterStatsPacketLateArrival,
       "rttMonJitterStatsError": rttMonJitterStatsError,
       "rttMonJitterStatsBusies": rttMonJitterStatsBusies,
       "rttMonJitterStatsOWSumSD": rttMonJitterStatsOWSumSD,
       "rttMonJitterStatsOWSum2SDLow": rttMonJitterStatsOWSum2SDLow,
       "rttMonJitterStatsOWSum2SDHigh": rttMonJitterStatsOWSum2SDHigh,
       "rttMonJitterStatsOWMinSD": rttMonJitterStatsOWMinSD,
       "rttMonJitterStatsOWMaxSD": rttMonJitterStatsOWMaxSD,
       "rttMonJitterStatsOWSumDS": rttMonJitterStatsOWSumDS,
       "rttMonJitterStatsOWSum2DSLow": rttMonJitterStatsOWSum2DSLow,
       "rttMonJitterStatsOWSum2DSHigh": rttMonJitterStatsOWSum2DSHigh,
       "rttMonJitterStatsOWMinDS": rttMonJitterStatsOWMinDS,
       "rttMonJitterStatsOWMaxDS": rttMonJitterStatsOWMaxDS,
       "rttMonJitterStatsNumOfOW": rttMonJitterStatsNumOfOW,
       "rttMonJitterStatsOWMinSDNew": rttMonJitterStatsOWMinSDNew,
       "rttMonJitterStatsOWMaxSDNew": rttMonJitterStatsOWMaxSDNew,
       "rttMonJitterStatsOWMinDSNew": rttMonJitterStatsOWMinDSNew,
       "rttMonJitterStatsOWMaxDSNew": rttMonJitterStatsOWMaxDSNew,
       "rttMonJitterStatsMinOfMOS": rttMonJitterStatsMinOfMOS,
       "rttMonJitterStatsMaxOfMOS": rttMonJitterStatsMaxOfMOS,
       "rttMonJitterStatsMinOfICPIF": rttMonJitterStatsMinOfICPIF,
       "rttMonJitterStatsMaxOfICPIF": rttMonJitterStatsMaxOfICPIF,
       "rttMonJitterStatsIAJOut": rttMonJitterStatsIAJOut,
       "rttMonJitterStatsIAJIn": rttMonJitterStatsIAJIn,
       "rttMonJitterStatsAvgJitter": rttMonJitterStatsAvgJitter,
       "rttMonJitterStatsAvgJitterSD": rttMonJitterStatsAvgJitterSD,
       "rttMonJitterStatsAvgJitterDS": rttMonJitterStatsAvgJitterDS,
       "rttMonJitterStatsUnSyncRTs": rttMonJitterStatsUnSyncRTs,
       "rttMonJitterStatsRTTSumHigh": rttMonJitterStatsRTTSumHigh,
       "rttMonJitterStatsOWSumSDHigh": rttMonJitterStatsOWSumSDHigh,
       "rttMonJitterStatsOWSumDSHigh": rttMonJitterStatsOWSumDSHigh,
       "rttMonJitterStatsNumOverThresh": rttMonJitterStatsNumOverThresh,
       "rttMonLpdGrpStatsTable": rttMonLpdGrpStatsTable,
       "rttMonLpdGrpStatsEntry": rttMonLpdGrpStatsEntry,
       "rttMonLpdGrpStatsGroupIndex": rttMonLpdGrpStatsGroupIndex,
       "rttMonLpdGrpStatsStartTimeIndex": rttMonLpdGrpStatsStartTimeIndex,
       "rttMonLpdGrpStatsTargetPE": rttMonLpdGrpStatsTargetPE,
       "rttMonLpdGrpStatsNumOfPass": rttMonLpdGrpStatsNumOfPass,
       "rttMonLpdGrpStatsNumOfFail": rttMonLpdGrpStatsNumOfFail,
       "rttMonLpdGrpStatsNumOfTimeout": rttMonLpdGrpStatsNumOfTimeout,
       "rttMonLpdGrpStatsAvgRTT": rttMonLpdGrpStatsAvgRTT,
       "rttMonLpdGrpStatsMinRTT": rttMonLpdGrpStatsMinRTT,
       "rttMonLpdGrpStatsMaxRTT": rttMonLpdGrpStatsMaxRTT,
       "rttMonLpdGrpStatsMinNumPaths": rttMonLpdGrpStatsMinNumPaths,
       "rttMonLpdGrpStatsMaxNumPaths": rttMonLpdGrpStatsMaxNumPaths,
       "rttMonLpdGrpStatsLPDStartTime": rttMonLpdGrpStatsLPDStartTime,
       "rttMonLpdGrpStatsLPDFailOccurred": rttMonLpdGrpStatsLPDFailOccurred,
       "rttMonLpdGrpStatsLPDFailCause": rttMonLpdGrpStatsLPDFailCause,
       "rttMonLpdGrpStatsLPDCompTime": rttMonLpdGrpStatsLPDCompTime,
       "rttMonLpdGrpStatsGroupStatus": rttMonLpdGrpStatsGroupStatus,
       "rttMonLpdGrpStatsGroupProbeIndex": rttMonLpdGrpStatsGroupProbeIndex,
       "rttMonLpdGrpStatsPathIds": rttMonLpdGrpStatsPathIds,
       "rttMonLpdGrpStatsProbeStatus": rttMonLpdGrpStatsProbeStatus,
       "rttMonLpdGrpStatsResetTime": rttMonLpdGrpStatsResetTime,
       "rttMonHistory": rttMonHistory,
       "rttMonHistoryCollectionTable": rttMonHistoryCollectionTable,
       "rttMonHistoryCollectionEntry": rttMonHistoryCollectionEntry,
       "rttMonHistoryCollectionLifeIndex": rttMonHistoryCollectionLifeIndex,
       "rttMonHistoryCollectionBucketIndex": rttMonHistoryCollectionBucketIndex,
       "rttMonHistoryCollectionSampleIndex": rttMonHistoryCollectionSampleIndex,
       "rttMonHistoryCollectionSampleTime": rttMonHistoryCollectionSampleTime,
       "rttMonHistoryCollectionAddress": rttMonHistoryCollectionAddress,
       "rttMonHistoryCollectionCompletionTime": rttMonHistoryCollectionCompletionTime,
       "rttMonHistoryCollectionSense": rttMonHistoryCollectionSense,
       "rttMonHistoryCollectionApplSpecificSense": rttMonHistoryCollectionApplSpecificSense,
       "rttMonHistoryCollectionSenseDescription": rttMonHistoryCollectionSenseDescription,
       "rttMonLatestOper": rttMonLatestOper,
       "rttMonLatestHTTPOperTable": rttMonLatestHTTPOperTable,
       "rttMonLatestHTTPOperEntry": rttMonLatestHTTPOperEntry,
       "rttMonLatestHTTPOperRTT": rttMonLatestHTTPOperRTT,
       "rttMonLatestHTTPOperDNSRTT": rttMonLatestHTTPOperDNSRTT,
       "rttMonLatestHTTPOperTCPConnectRTT": rttMonLatestHTTPOperTCPConnectRTT,
       "rttMonLatestHTTPOperTransactionRTT": rttMonLatestHTTPOperTransactionRTT,
       "rttMonLatestHTTPOperMessageBodyOctets": rttMonLatestHTTPOperMessageBodyOctets,
       "rttMonLatestHTTPOperSense": rttMonLatestHTTPOperSense,
       "rttMonLatestHTTPErrorSenseDescription": rttMonLatestHTTPErrorSenseDescription,
       "rttMonLatestJitterOperTable": rttMonLatestJitterOperTable,
       "rttMonLatestJitterOperEntry": rttMonLatestJitterOperEntry,
       "rttMonLatestJitterOperNumOfRTT": rttMonLatestJitterOperNumOfRTT,
       "rttMonLatestJitterOperRTTSum": rttMonLatestJitterOperRTTSum,
       "rttMonLatestJitterOperRTTSum2": rttMonLatestJitterOperRTTSum2,
       "rttMonLatestJitterOperRTTMin": rttMonLatestJitterOperRTTMin,
       "rttMonLatestJitterOperRTTMax": rttMonLatestJitterOperRTTMax,
       "rttMonLatestJitterOperMinOfPositivesSD": rttMonLatestJitterOperMinOfPositivesSD,
       "rttMonLatestJitterOperMaxOfPositivesSD": rttMonLatestJitterOperMaxOfPositivesSD,
       "rttMonLatestJitterOperNumOfPositivesSD": rttMonLatestJitterOperNumOfPositivesSD,
       "rttMonLatestJitterOperSumOfPositivesSD": rttMonLatestJitterOperSumOfPositivesSD,
       "rttMonLatestJitterOperSum2PositivesSD": rttMonLatestJitterOperSum2PositivesSD,
       "rttMonLatestJitterOperMinOfNegativesSD": rttMonLatestJitterOperMinOfNegativesSD,
       "rttMonLatestJitterOperMaxOfNegativesSD": rttMonLatestJitterOperMaxOfNegativesSD,
       "rttMonLatestJitterOperNumOfNegativesSD": rttMonLatestJitterOperNumOfNegativesSD,
       "rttMonLatestJitterOperSumOfNegativesSD": rttMonLatestJitterOperSumOfNegativesSD,
       "rttMonLatestJitterOperSum2NegativesSD": rttMonLatestJitterOperSum2NegativesSD,
       "rttMonLatestJitterOperMinOfPositivesDS": rttMonLatestJitterOperMinOfPositivesDS,
       "rttMonLatestJitterOperMaxOfPositivesDS": rttMonLatestJitterOperMaxOfPositivesDS,
       "rttMonLatestJitterOperNumOfPositivesDS": rttMonLatestJitterOperNumOfPositivesDS,
       "rttMonLatestJitterOperSumOfPositivesDS": rttMonLatestJitterOperSumOfPositivesDS,
       "rttMonLatestJitterOperSum2PositivesDS": rttMonLatestJitterOperSum2PositivesDS,
       "rttMonLatestJitterOperMinOfNegativesDS": rttMonLatestJitterOperMinOfNegativesDS,
       "rttMonLatestJitterOperMaxOfNegativesDS": rttMonLatestJitterOperMaxOfNegativesDS,
       "rttMonLatestJitterOperNumOfNegativesDS": rttMonLatestJitterOperNumOfNegativesDS,
       "rttMonLatestJitterOperSumOfNegativesDS": rttMonLatestJitterOperSumOfNegativesDS,
       "rttMonLatestJitterOperSum2NegativesDS": rttMonLatestJitterOperSum2NegativesDS,
       "rttMonLatestJitterOperPacketLossSD": rttMonLatestJitterOperPacketLossSD,
       "rttMonLatestJitterOperPacketLossDS": rttMonLatestJitterOperPacketLossDS,
       "rttMonLatestJitterOperPacketOutOfSequence": rttMonLatestJitterOperPacketOutOfSequence,
       "rttMonLatestJitterOperPacketMIA": rttMonLatestJitterOperPacketMIA,
       "rttMonLatestJitterOperPacketLateArrival": rttMonLatestJitterOperPacketLateArrival,
       "rttMonLatestJitterOperSense": rttMonLatestJitterOperSense,
       "rttMonLatestJitterErrorSenseDescription": rttMonLatestJitterErrorSenseDescription,
       "rttMonLatestJitterOperOWSumSD": rttMonLatestJitterOperOWSumSD,
       "rttMonLatestJitterOperOWSum2SD": rttMonLatestJitterOperOWSum2SD,
       "rttMonLatestJitterOperOWMinSD": rttMonLatestJitterOperOWMinSD,
       "rttMonLatestJitterOperOWMaxSD": rttMonLatestJitterOperOWMaxSD,
       "rttMonLatestJitterOperOWSumDS": rttMonLatestJitterOperOWSumDS,
       "rttMonLatestJitterOperOWSum2DS": rttMonLatestJitterOperOWSum2DS,
       "rttMonLatestJitterOperOWMinDS": rttMonLatestJitterOperOWMinDS,
       "rttMonLatestJitterOperOWMaxDS": rttMonLatestJitterOperOWMaxDS,
       "rttMonLatestJitterOperNumOfOW": rttMonLatestJitterOperNumOfOW,
       "rttMonLatestJitterOperMOS": rttMonLatestJitterOperMOS,
       "rttMonLatestJitterOperICPIF": rttMonLatestJitterOperICPIF,
       "rttMonLatestJitterOperIAJOut": rttMonLatestJitterOperIAJOut,
       "rttMonLatestJitterOperIAJIn": rttMonLatestJitterOperIAJIn,
       "rttMonLatestJitterOperAvgJitter": rttMonLatestJitterOperAvgJitter,
       "rttMonLatestJitterOperAvgSDJ": rttMonLatestJitterOperAvgSDJ,
       "rttMonLatestJitterOperAvgDSJ": rttMonLatestJitterOperAvgDSJ,
       "rttMonLatestJitterOperOWAvgSD": rttMonLatestJitterOperOWAvgSD,
       "rttMonLatestJitterOperOWAvgDS": rttMonLatestJitterOperOWAvgDS,
       "rttMonLatestJitterOperNTPState": rttMonLatestJitterOperNTPState,
       "rttMonLatestJitterOperUnSyncRTs": rttMonLatestJitterOperUnSyncRTs,
       "rttMonLatestJitterOperRTTSumHigh": rttMonLatestJitterOperRTTSumHigh,
       "rttMonLatestJitterOperRTTSum2High": rttMonLatestJitterOperRTTSum2High,
       "rttMonLatestJitterOperOWSumSDHigh": rttMonLatestJitterOperOWSumSDHigh,
       "rttMonLatestJitterOperOWSum2SDHigh": rttMonLatestJitterOperOWSum2SDHigh,
       "rttMonLatestJitterOperOWSumDSHigh": rttMonLatestJitterOperOWSumDSHigh,
       "rttMonLatestJitterOperOWSum2DSHigh": rttMonLatestJitterOperOWSum2DSHigh,
       "rttMonLatestJitterOperNumOverThresh": rttMonLatestJitterOperNumOverThresh,
       "rttMonNotificationsPrefix": rttMonNotificationsPrefix,
       "rttMonNotifications": rttMonNotifications,
       "rttMonConnectionChangeNotification": rttMonConnectionChangeNotification,
       "rttMonTimeoutNotification": rttMonTimeoutNotification,
       "rttMonThresholdNotification": rttMonThresholdNotification,
       "rttMonVerifyErrorNotification": rttMonVerifyErrorNotification,
       "rttMonNotification": rttMonNotification,
       "rttMonLpdDiscoveryNotification": rttMonLpdDiscoveryNotification,
       "rttMonLpdGrpStatusNotification": rttMonLpdGrpStatusNotification,
       "rttMonNotificationV2": rttMonNotificationV2,
       "ciscoRttMonMibConformance": ciscoRttMonMibConformance,
       "ciscoRttMonMibCompliances": ciscoRttMonMibCompliances,
       "ciscoRttMonMibComplianceRev12": ciscoRttMonMibComplianceRev12,
       "ciscoRttMonMibComplianceRev13": ciscoRttMonMibComplianceRev13,
       "ciscoRttMonMibComplianceRev14": ciscoRttMonMibComplianceRev14,
       "ciscoRttMonMibComplianceRev15": ciscoRttMonMibComplianceRev15,
       "ciscoRttMonMibComplianceRev16": ciscoRttMonMibComplianceRev16,
       "ciscoRttMonMibComplianceRev17": ciscoRttMonMibComplianceRev17,
       "ciscoRttMonMibComplianceRev18": ciscoRttMonMibComplianceRev18,
       "ciscoRttMonMibComplianceRev19": ciscoRttMonMibComplianceRev19,
       "ciscoRttMonMibComplianceRev20": ciscoRttMonMibComplianceRev20,
       "ciscoRttMonMibComplianceRev21": ciscoRttMonMibComplianceRev21,
       "ciscoRttMonMibComplianceRev22": ciscoRttMonMibComplianceRev22,
       "ciscoRttMonMibComplianceRev23": ciscoRttMonMibComplianceRev23,
       "ciscoRttMonMibGroups": ciscoRttMonMibGroups,
       "ciscoStatsGroup": ciscoStatsGroup,
       "ciscoHistoryGroup": ciscoHistoryGroup,
       "ciscoCtrlGroupRev1": ciscoCtrlGroupRev1,
       "ciscoCtrlGroupRev2": ciscoCtrlGroupRev2,
       "ciscoLatestOperGroupRev1": ciscoLatestOperGroupRev1,
       "ciscoStatsGroupRev1": ciscoStatsGroupRev1,
       "ciscoApplGroupRev2": ciscoApplGroupRev2,
       "ciscoCtrlGroupRev4": ciscoCtrlGroupRev4,
       "ciscoStatsGroupRev3": ciscoStatsGroupRev3,
       "ciscoCtrlGroupRev6": ciscoCtrlGroupRev6,
       "ciscoStatsGroupRev4": ciscoStatsGroupRev4,
       "ciscoNotificationGroup": ciscoNotificationGroup,
       "ciscoApplGroupRev3": ciscoApplGroupRev3,
       "ciscoCtrlGroupRev7": ciscoCtrlGroupRev7,
       "ciscoCtrlGroupRev8": ciscoCtrlGroupRev8,
       "ciscoStatsGroupRev5": ciscoStatsGroupRev5,
       "ciscoCtrlGroupRev9": ciscoCtrlGroupRev9,
       "ciscoCtrlGroupRev10": ciscoCtrlGroupRev10,
       "ciscoCtrlGroupRev11": ciscoCtrlGroupRev11,
       "ciscoNotificationGroupRev1": ciscoNotificationGroupRev1,
       "ciscoCtrlGroupRev12": ciscoCtrlGroupRev12,
       "ciscoCtrlGroupRev13": ciscoCtrlGroupRev13,
       "ciscoStatsGroupRev7": ciscoStatsGroupRev7,
       "ciscoNotificationGroupRev2": ciscoNotificationGroupRev2,
       "ciscoApplGroupRev4": ciscoApplGroupRev4,
       "ciscoCtrlGroupRev14": ciscoCtrlGroupRev14,
       "ciscoCtrlGroupRev15": ciscoCtrlGroupRev15,
       "ciscoRttMonObsoleteGroupRev1": ciscoRttMonObsoleteGroupRev1,
       "ciscoRttMonDeprecatedGroupRev1": ciscoRttMonDeprecatedGroupRev1,
       "ciscoCtrlGroupRev16": ciscoCtrlGroupRev16,
       "ciscoCtrlGroupRev17": ciscoCtrlGroupRev17,
       "ciscoCtrlGroupRev18": ciscoCtrlGroupRev18,
       "ciscoStatsGroupRev8": ciscoStatsGroupRev8,
       "ciscoCtrlGroupRev19": ciscoCtrlGroupRev19,
       "ciscoCtrlGroupRev20": ciscoCtrlGroupRev20,
       "ciscoCtrlGroupRev21": ciscoCtrlGroupRev21,
       "ciscoCtrlGroupRev22": ciscoCtrlGroupRev22,
       "ciscoCtrlGroupRev23": ciscoCtrlGroupRev23,
       "ciscoCtrlGroupRev24": ciscoCtrlGroupRev24,
       "ciscoCtrlGroupRev25": ciscoCtrlGroupRev25,
       "ciscoStatsGroupRev2": ciscoStatsGroupRev2,
       "ciscoCtrlGroupRev26": ciscoCtrlGroupRev26,
       "ciscoCtrlGroupRev27": ciscoCtrlGroupRev27,
       "ciscoCtrlGroupRev28": ciscoCtrlGroupRev28,
       "ciscoStatsGroupRev9": ciscoStatsGroupRev9,
       "ciscoCtrlGroupRev29": ciscoCtrlGroupRev29,
       "ciscoNotificationGroupRev3": ciscoNotificationGroupRev3,
       "ciscoCtrlGroupRev30": ciscoCtrlGroupRev30,
       "ciscoCtrlGroupRev31": ciscoCtrlGroupRev31,
       "ciscoStatsGroupRev10": ciscoStatsGroupRev10}
)
