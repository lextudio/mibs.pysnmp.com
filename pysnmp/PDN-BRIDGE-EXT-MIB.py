# SNMP MIB module (PDN-BRIDGE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-BRIDGE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:20 2024
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

(dot1dBasePort,
 dot1dBasePortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(PdnTestAndIncrDerivedIndexTC,) = mibBuilder.importSymbols(
    "PDN-TC",
    "PdnTestAndIncrDerivedIndexTC")

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
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

pdnBridgeExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58)
)
pdnBridgeExtMIB.setRevisions(
        ("2005-10-26 00:00",
         "2005-10-05 00:00",
         "2005-09-29 00:00",
         "2005-09-12 00:00",
         "2005-08-15 00:00",
         "2004-12-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnBridgeExtNotifications_ObjectIdentity = ObjectIdentity
pdnBridgeExtNotifications = _PdnBridgeExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 0)
)
_PdnBridgeExtObjects_ObjectIdentity = ObjectIdentity
pdnBridgeExtObjects = _PdnBridgeExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1)
)
_PdnDot1dBasePortExtTable_Object = MibTable
pdnDot1dBasePortExtTable = _PdnDot1dBasePortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDot1dBasePortExtTable.setStatus("current")
_PdnDot1dBasePortExtEntry_Object = MibTableRow
pdnDot1dBasePortExtEntry = _PdnDot1dBasePortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDot1dBasePortExtEntry.setStatus("current")


class _PdnDot1dBasePortMaxFdbEntries_Type(Integer32):
    """Custom type pdnDot1dBasePortMaxFdbEntries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_PdnDot1dBasePortMaxFdbEntries_Type.__name__ = "Integer32"
_PdnDot1dBasePortMaxFdbEntries_Object = MibTableColumn
pdnDot1dBasePortMaxFdbEntries = _PdnDot1dBasePortMaxFdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 1),
    _PdnDot1dBasePortMaxFdbEntries_Type()
)
pdnDot1dBasePortMaxFdbEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortMaxFdbEntries.setStatus("current")


class _PdnDot1dBasePortRole_Type(Integer32):
    """Custom type pdnDot1dBasePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("subscriber", 1))
    )


_PdnDot1dBasePortRole_Type.__name__ = "Integer32"
_PdnDot1dBasePortRole_Object = MibTableColumn
pdnDot1dBasePortRole = _PdnDot1dBasePortRole_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 2),
    _PdnDot1dBasePortRole_Type()
)
pdnDot1dBasePortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortRole.setStatus("current")


class _PdnDot1dBasePortUnknownMulticastForwardingMode_Type(Integer32):
    """Custom type pdnDot1dBasePortUnknownMulticastForwardingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("flood", 1))
    )


_PdnDot1dBasePortUnknownMulticastForwardingMode_Type.__name__ = "Integer32"
_PdnDot1dBasePortUnknownMulticastForwardingMode_Object = MibTableColumn
pdnDot1dBasePortUnknownMulticastForwardingMode = _PdnDot1dBasePortUnknownMulticastForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 3),
    _PdnDot1dBasePortUnknownMulticastForwardingMode_Type()
)
pdnDot1dBasePortUnknownMulticastForwardingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortUnknownMulticastForwardingMode.setStatus("current")


class _PdnDot1dBasePortOuterTag_Type(Integer32):
    """Custom type pdnDot1dBasePortOuterTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PdnDot1dBasePortOuterTag_Type.__name__ = "Integer32"
_PdnDot1dBasePortOuterTag_Object = MibTableColumn
pdnDot1dBasePortOuterTag = _PdnDot1dBasePortOuterTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 4),
    _PdnDot1dBasePortOuterTag_Type()
)
pdnDot1dBasePortOuterTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortOuterTag.setStatus("current")


class _PdnDot1dBasePortOuterPriority_Type(Integer32):
    """Custom type pdnDot1dBasePortOuterPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PdnDot1dBasePortOuterPriority_Type.__name__ = "Integer32"
_PdnDot1dBasePortOuterPriority_Object = MibTableColumn
pdnDot1dBasePortOuterPriority = _PdnDot1dBasePortOuterPriority_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 5),
    _PdnDot1dBasePortOuterPriority_Type()
)
pdnDot1dBasePortOuterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortOuterPriority.setStatus("current")


class _PdnDot1dBasePortOuterEthertype_Type(Integer32):
    """Custom type pdnDot1dBasePortOuterEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnDot1dBasePortOuterEthertype_Type.__name__ = "Integer32"
_PdnDot1dBasePortOuterEthertype_Object = MibTableColumn
pdnDot1dBasePortOuterEthertype = _PdnDot1dBasePortOuterEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 1, 1, 6),
    _PdnDot1dBasePortOuterEthertype_Type()
)
pdnDot1dBasePortOuterEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dBasePortOuterEthertype.setStatus("current")
_PdnDot1dTrafficProfile_ObjectIdentity = ObjectIdentity
pdnDot1dTrafficProfile = _PdnDot1dTrafficProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2)
)
_PdnDot1dTrafficProfileNextIndex_Type = TestAndIncr
_PdnDot1dTrafficProfileNextIndex_Object = MibScalar
pdnDot1dTrafficProfileNextIndex = _PdnDot1dTrafficProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 1),
    _PdnDot1dTrafficProfileNextIndex_Type()
)
pdnDot1dTrafficProfileNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileNextIndex.setStatus("current")
_PdnDot1dTrafficProfileTable_Object = MibTable
pdnDot1dTrafficProfileTable = _PdnDot1dTrafficProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileTable.setStatus("current")
_PdnDot1dTrafficProfileEntry_Object = MibTableRow
pdnDot1dTrafficProfileEntry = _PdnDot1dTrafficProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1)
)
pdnDot1dTrafficProfileEntry.setIndexNames(
    (0, "PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileIndex"),
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileEntry.setStatus("current")
_PdnDot1dTrafficProfileIndex_Type = PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileIndex_Object = MibTableColumn
pdnDot1dTrafficProfileIndex = _PdnDot1dTrafficProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 1),
    _PdnDot1dTrafficProfileIndex_Type()
)
pdnDot1dTrafficProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileIndex.setStatus("current")
_PdnDot1dTrafficProfileRowStatus_Type = RowStatus
_PdnDot1dTrafficProfileRowStatus_Object = MibTableColumn
pdnDot1dTrafficProfileRowStatus = _PdnDot1dTrafficProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 2),
    _PdnDot1dTrafficProfileRowStatus_Type()
)
pdnDot1dTrafficProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileRowStatus.setStatus("current")


class _PdnDot1dTrafficProfileName_Type(SnmpAdminString):
    """Custom type pdnDot1dTrafficProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PdnDot1dTrafficProfileName_Type.__name__ = "SnmpAdminString"
_PdnDot1dTrafficProfileName_Object = MibTableColumn
pdnDot1dTrafficProfileName = _PdnDot1dTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 3),
    _PdnDot1dTrafficProfileName_Type()
)
pdnDot1dTrafficProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileName.setStatus("current")


class _PdnDot1dTrafficProfileNbrRefs_Type(Unsigned32):
    """Custom type pdnDot1dTrafficProfileNbrRefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdnDot1dTrafficProfileNbrRefs_Type.__name__ = "Unsigned32"
_PdnDot1dTrafficProfileNbrRefs_Object = MibTableColumn
pdnDot1dTrafficProfileNbrRefs = _PdnDot1dTrafficProfileNbrRefs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 4),
    _PdnDot1dTrafficProfileNbrRefs_Type()
)
pdnDot1dTrafficProfileNbrRefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileNbrRefs.setStatus("current")


class _PdnDot1dTrafficProfileTrafficClass_Type(Integer32):
    """Custom type pdnDot1dTrafficProfileTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("video", 2),
          ("voice", 3))
    )


_PdnDot1dTrafficProfileTrafficClass_Type.__name__ = "Integer32"
_PdnDot1dTrafficProfileTrafficClass_Object = MibTableColumn
pdnDot1dTrafficProfileTrafficClass = _PdnDot1dTrafficProfileTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 5),
    _PdnDot1dTrafficProfileTrafficClass_Type()
)
pdnDot1dTrafficProfileTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileTrafficClass.setStatus("current")


class _PdnDot1dTrafficProfileMaxRate_Type(Unsigned32):
    """Custom type pdnDot1dTrafficProfileMaxRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PdnDot1dTrafficProfileMaxRate_Type.__name__ = "Unsigned32"
_PdnDot1dTrafficProfileMaxRate_Object = MibTableColumn
pdnDot1dTrafficProfileMaxRate = _PdnDot1dTrafficProfileMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 2, 1, 6),
    _PdnDot1dTrafficProfileMaxRate_Type()
)
pdnDot1dTrafficProfileMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMaxRate.setUnits("bps")
_PdnDot1dTrafficProfileInvMappingTable_Object = MibTable
pdnDot1dTrafficProfileInvMappingTable = _PdnDot1dTrafficProfileInvMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileInvMappingTable.setStatus("current")
_PdnDot1dTrafficProfileInvMappingEntry_Object = MibTableRow
pdnDot1dTrafficProfileInvMappingEntry = _PdnDot1dTrafficProfileInvMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 3, 1)
)
pdnDot1dTrafficProfileInvMappingEntry.setIndexNames(
    (1, "PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileName"),
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileInvMappingEntry.setStatus("current")
_PdnDot1dTrafficProfileInvIndex_Type = PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileInvIndex_Object = MibTableColumn
pdnDot1dTrafficProfileInvIndex = _PdnDot1dTrafficProfileInvIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 3, 1, 1),
    _PdnDot1dTrafficProfileInvIndex_Type()
)
pdnDot1dTrafficProfileInvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileInvIndex.setStatus("current")
_PdnDot1dTrafficProfileMappingTable_Object = MibTable
pdnDot1dTrafficProfileMappingTable = _PdnDot1dTrafficProfileMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMappingTable.setStatus("current")
_PdnDot1dTrafficProfileMappingEntry_Object = MibTableRow
pdnDot1dTrafficProfileMappingEntry = _PdnDot1dTrafficProfileMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 4, 1)
)
pdnDot1dTrafficProfileMappingEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileMappingSubPort"),
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMappingEntry.setStatus("current")


class _PdnDot1dTrafficProfileMappingSubPort_Type(Integer32):
    """Custom type pdnDot1dTrafficProfileMappingSubPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PdnDot1dTrafficProfileMappingSubPort_Type.__name__ = "Integer32"
_PdnDot1dTrafficProfileMappingSubPort_Object = MibTableColumn
pdnDot1dTrafficProfileMappingSubPort = _PdnDot1dTrafficProfileMappingSubPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 4, 1, 1),
    _PdnDot1dTrafficProfileMappingSubPort_Type()
)
pdnDot1dTrafficProfileMappingSubPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMappingSubPort.setStatus("current")
_PdnDot1dTrafficProfileMappingRowStatus_Type = RowStatus
_PdnDot1dTrafficProfileMappingRowStatus_Object = MibTableColumn
pdnDot1dTrafficProfileMappingRowStatus = _PdnDot1dTrafficProfileMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 4, 1, 2),
    _PdnDot1dTrafficProfileMappingRowStatus_Type()
)
pdnDot1dTrafficProfileMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMappingRowStatus.setStatus("current")
_PdnDot1dTrafficProfileMappingIndex_Type = PdnTestAndIncrDerivedIndexTC
_PdnDot1dTrafficProfileMappingIndex_Object = MibTableColumn
pdnDot1dTrafficProfileMappingIndex = _PdnDot1dTrafficProfileMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 1, 2, 4, 1, 3),
    _PdnDot1dTrafficProfileMappingIndex_Type()
)
pdnDot1dTrafficProfileMappingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMappingIndex.setStatus("current")
_PdnBridgeExtAFNs_ObjectIdentity = ObjectIdentity
pdnBridgeExtAFNs = _PdnBridgeExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 2)
)
_PdnBridgeExtConformance_ObjectIdentity = ObjectIdentity
pdnBridgeExtConformance = _PdnBridgeExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3)
)
_PdnBridgeExtCompliances_ObjectIdentity = ObjectIdentity
pdnBridgeExtCompliances = _PdnBridgeExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 1)
)
_PdnBridgeExtGroups_ObjectIdentity = ObjectIdentity
pdnBridgeExtGroups = _PdnBridgeExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2)
)
_PdnBridgeExtObjGroups_ObjectIdentity = ObjectIdentity
pdnBridgeExtObjGroups = _PdnBridgeExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1)
)
_PdnBridgeExtTPGroups_ObjectIdentity = ObjectIdentity
pdnBridgeExtTPGroups = _PdnBridgeExtTPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 4)
)
_PdnBridgeExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnBridgeExtAfnGroups = _PdnBridgeExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 2)
)
_PdnBridgeExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnBridgeExtNtfyGroups = _PdnBridgeExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 3)
)
dot1dBasePortEntry.registerAugmentions(
    ("PDN-BRIDGE-EXT-MIB",
     "pdnDot1dBasePortExtEntry")
)
pdnDot1dBasePortExtEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

pdnDot1dBasePortMaxFdbEntriesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 1)
)
pdnDot1dBasePortMaxFdbEntriesGroup.setObjects(
    ("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortMaxFdbEntries")
)
if mibBuilder.loadTexts:
    pdnDot1dBasePortMaxFdbEntriesGroup.setStatus("current")

pdnDot1dBasePortRoleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 2)
)
pdnDot1dBasePortRoleGroup.setObjects(
    ("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortRole")
)
if mibBuilder.loadTexts:
    pdnDot1dBasePortRoleGroup.setStatus("current")

pdnDot1dBasePortUnknownMulticastForwardingModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 3)
)
pdnDot1dBasePortUnknownMulticastForwardingModeGroup.setObjects(
    ("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortUnknownMulticastForwardingMode")
)
if mibBuilder.loadTexts:
    pdnDot1dBasePortUnknownMulticastForwardingModeGroup.setStatus("current")

pdnDot1dTrafficProfileBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 4, 1)
)
pdnDot1dTrafficProfileBasicGroup.setObjects(
      *(("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileNextIndex"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileName"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileRowStatus"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileNbrRefs"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileTrafficClass"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileInvIndex"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileMappingRowStatus"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileMappingIndex"))
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileBasicGroup.setStatus("current")

pdnDot1dTrafficProfileMaxRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 4, 2)
)
pdnDot1dTrafficProfileMaxRateGroup.setObjects(
    ("PDN-BRIDGE-EXT-MIB", "pdnDot1dTrafficProfileMaxRate")
)
if mibBuilder.loadTexts:
    pdnDot1dTrafficProfileMaxRateGroup.setStatus("current")

pdnDot1dQinQVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 2, 1, 5)
)
pdnDot1dQinQVlanGroup.setObjects(
      *(("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortOuterTag"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortOuterPriority"),
        ("PDN-BRIDGE-EXT-MIB", "pdnDot1dBasePortOuterEthertype"))
)
if mibBuilder.loadTexts:
    pdnDot1dQinQVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnBridgeExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 58, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnBridgeExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-BRIDGE-EXT-MIB",
    **{"pdnBridgeExtMIB": pdnBridgeExtMIB,
       "pdnBridgeExtNotifications": pdnBridgeExtNotifications,
       "pdnBridgeExtObjects": pdnBridgeExtObjects,
       "pdnDot1dBasePortExtTable": pdnDot1dBasePortExtTable,
       "pdnDot1dBasePortExtEntry": pdnDot1dBasePortExtEntry,
       "pdnDot1dBasePortMaxFdbEntries": pdnDot1dBasePortMaxFdbEntries,
       "pdnDot1dBasePortRole": pdnDot1dBasePortRole,
       "pdnDot1dBasePortUnknownMulticastForwardingMode": pdnDot1dBasePortUnknownMulticastForwardingMode,
       "pdnDot1dBasePortOuterTag": pdnDot1dBasePortOuterTag,
       "pdnDot1dBasePortOuterPriority": pdnDot1dBasePortOuterPriority,
       "pdnDot1dBasePortOuterEthertype": pdnDot1dBasePortOuterEthertype,
       "pdnDot1dTrafficProfile": pdnDot1dTrafficProfile,
       "pdnDot1dTrafficProfileNextIndex": pdnDot1dTrafficProfileNextIndex,
       "pdnDot1dTrafficProfileTable": pdnDot1dTrafficProfileTable,
       "pdnDot1dTrafficProfileEntry": pdnDot1dTrafficProfileEntry,
       "pdnDot1dTrafficProfileIndex": pdnDot1dTrafficProfileIndex,
       "pdnDot1dTrafficProfileRowStatus": pdnDot1dTrafficProfileRowStatus,
       "pdnDot1dTrafficProfileName": pdnDot1dTrafficProfileName,
       "pdnDot1dTrafficProfileNbrRefs": pdnDot1dTrafficProfileNbrRefs,
       "pdnDot1dTrafficProfileTrafficClass": pdnDot1dTrafficProfileTrafficClass,
       "pdnDot1dTrafficProfileMaxRate": pdnDot1dTrafficProfileMaxRate,
       "pdnDot1dTrafficProfileInvMappingTable": pdnDot1dTrafficProfileInvMappingTable,
       "pdnDot1dTrafficProfileInvMappingEntry": pdnDot1dTrafficProfileInvMappingEntry,
       "pdnDot1dTrafficProfileInvIndex": pdnDot1dTrafficProfileInvIndex,
       "pdnDot1dTrafficProfileMappingTable": pdnDot1dTrafficProfileMappingTable,
       "pdnDot1dTrafficProfileMappingEntry": pdnDot1dTrafficProfileMappingEntry,
       "pdnDot1dTrafficProfileMappingSubPort": pdnDot1dTrafficProfileMappingSubPort,
       "pdnDot1dTrafficProfileMappingRowStatus": pdnDot1dTrafficProfileMappingRowStatus,
       "pdnDot1dTrafficProfileMappingIndex": pdnDot1dTrafficProfileMappingIndex,
       "pdnBridgeExtAFNs": pdnBridgeExtAFNs,
       "pdnBridgeExtConformance": pdnBridgeExtConformance,
       "pdnBridgeExtCompliances": pdnBridgeExtCompliances,
       "pdnBridgeExtCompliance": pdnBridgeExtCompliance,
       "pdnBridgeExtGroups": pdnBridgeExtGroups,
       "pdnBridgeExtObjGroups": pdnBridgeExtObjGroups,
       "pdnDot1dBasePortMaxFdbEntriesGroup": pdnDot1dBasePortMaxFdbEntriesGroup,
       "pdnDot1dBasePortRoleGroup": pdnDot1dBasePortRoleGroup,
       "pdnDot1dBasePortUnknownMulticastForwardingModeGroup": pdnDot1dBasePortUnknownMulticastForwardingModeGroup,
       "pdnBridgeExtTPGroups": pdnBridgeExtTPGroups,
       "pdnDot1dTrafficProfileBasicGroup": pdnDot1dTrafficProfileBasicGroup,
       "pdnDot1dTrafficProfileMaxRateGroup": pdnDot1dTrafficProfileMaxRateGroup,
       "pdnDot1dQinQVlanGroup": pdnDot1dQinQVlanGroup,
       "pdnBridgeExtAfnGroups": pdnBridgeExtAfnGroups,
       "pdnBridgeExtNtfyGroups": pdnBridgeExtNtfyGroups}
)
