# SNMP MIB module (CISCO-IGMP-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IGMP-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:15 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoIGMPFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238)
)
ciscoIGMPFilterMIB.setRevisions(
        ("2005-11-29 00:00",
         "2002-05-09 00:00",
         "2001-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIgmpFilterMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIgmpFilterMIBObjects = _CiscoIgmpFilterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1)
)
_CIgmpFilterGeneral_ObjectIdentity = ObjectIdentity
cIgmpFilterGeneral = _CIgmpFilterGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 1)
)


class _CIgmpFilterEnable_Type(TruthValue):
    """Custom type cIgmpFilterEnable based on TruthValue"""


_CIgmpFilterEnable_Object = MibScalar
cIgmpFilterEnable = _CIgmpFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 1, 1),
    _CIgmpFilterEnable_Type()
)
cIgmpFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEnable.setStatus("current")
_CIgmpFilterMaxProfiles_Type = Unsigned32
_CIgmpFilterMaxProfiles_Object = MibScalar
cIgmpFilterMaxProfiles = _CIgmpFilterMaxProfiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 1, 2),
    _CIgmpFilterMaxProfiles_Type()
)
cIgmpFilterMaxProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIgmpFilterMaxProfiles.setStatus("current")
if mibBuilder.loadTexts:
    cIgmpFilterMaxProfiles.setUnits("profiles")
_CIgmpFilterInfo_ObjectIdentity = ObjectIdentity
cIgmpFilterInfo = _CIgmpFilterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2)
)
_CIgmpFilterTable_Object = MibTable
cIgmpFilterTable = _CIgmpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIgmpFilterTable.setStatus("current")
_CIgmpFilterEntry_Object = MibTableRow
cIgmpFilterEntry = _CIgmpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1)
)
cIgmpFilterEntry.setIndexNames(
    (0, "CISCO-IGMP-FILTER-MIB", "cIgmpFilterProfileIndex"),
    (0, "CISCO-IGMP-FILTER-MIB", "cIgmpFilterStartAddressType"),
    (0, "CISCO-IGMP-FILTER-MIB", "cIgmpFilterStartAddress"),
)
if mibBuilder.loadTexts:
    cIgmpFilterEntry.setStatus("current")
_CIgmpFilterProfileIndex_Type = Unsigned32
_CIgmpFilterProfileIndex_Object = MibTableColumn
cIgmpFilterProfileIndex = _CIgmpFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 1),
    _CIgmpFilterProfileIndex_Type()
)
cIgmpFilterProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIgmpFilterProfileIndex.setStatus("current")
_CIgmpFilterStartAddressType_Type = InetAddressType
_CIgmpFilterStartAddressType_Object = MibTableColumn
cIgmpFilterStartAddressType = _CIgmpFilterStartAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 2),
    _CIgmpFilterStartAddressType_Type()
)
cIgmpFilterStartAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIgmpFilterStartAddressType.setStatus("current")


class _CIgmpFilterStartAddress_Type(InetAddress):
    """Custom type cIgmpFilterStartAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CIgmpFilterStartAddress_Type.__name__ = "InetAddress"
_CIgmpFilterStartAddress_Object = MibTableColumn
cIgmpFilterStartAddress = _CIgmpFilterStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 3),
    _CIgmpFilterStartAddress_Type()
)
cIgmpFilterStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIgmpFilterStartAddress.setStatus("current")
_CIgmpFilterEndAddressType_Type = InetAddressType
_CIgmpFilterEndAddressType_Object = MibTableColumn
cIgmpFilterEndAddressType = _CIgmpFilterEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 4),
    _CIgmpFilterEndAddressType_Type()
)
cIgmpFilterEndAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIgmpFilterEndAddressType.setStatus("current")
_CIgmpFilterEndAddress_Type = InetAddress
_CIgmpFilterEndAddress_Object = MibTableColumn
cIgmpFilterEndAddress = _CIgmpFilterEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 5),
    _CIgmpFilterEndAddress_Type()
)
cIgmpFilterEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIgmpFilterEndAddress.setStatus("current")


class _CIgmpFilterProfileAction_Type(Integer32):
    """Custom type cIgmpFilterProfileAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CIgmpFilterProfileAction_Type.__name__ = "Integer32"
_CIgmpFilterProfileAction_Object = MibTableColumn
cIgmpFilterProfileAction = _CIgmpFilterProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 1, 1, 6),
    _CIgmpFilterProfileAction_Type()
)
cIgmpFilterProfileAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIgmpFilterProfileAction.setStatus("current")
_CIgmpFilterInterfaceTable_Object = MibTable
cIgmpFilterInterfaceTable = _CIgmpFilterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIgmpFilterInterfaceTable.setStatus("current")
_CIgmpFilterInterfaceEntry_Object = MibTableRow
cIgmpFilterInterfaceEntry = _CIgmpFilterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 2, 1)
)
cIgmpFilterInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cIgmpFilterInterfaceEntry.setStatus("current")


class _CIgmpFilterInterfaceProfileIndex_Type(Unsigned32):
    """Custom type cIgmpFilterInterfaceProfileIndex based on Unsigned32"""
    defaultValue = 0


_CIgmpFilterInterfaceProfileIndex_Object = MibTableColumn
cIgmpFilterInterfaceProfileIndex = _CIgmpFilterInterfaceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 2, 2, 1, 1),
    _CIgmpFilterInterfaceProfileIndex_Type()
)
cIgmpFilterInterfaceProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterInterfaceProfileIndex.setStatus("current")
_CIgmpFilterEditor_ObjectIdentity = ObjectIdentity
cIgmpFilterEditor = _CIgmpFilterEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3)
)
_CIgmpFilterEditSpinLock_Type = TestAndIncr
_CIgmpFilterEditSpinLock_Object = MibScalar
cIgmpFilterEditSpinLock = _CIgmpFilterEditSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 1),
    _CIgmpFilterEditSpinLock_Type()
)
cIgmpFilterEditSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditSpinLock.setStatus("current")
_CIgmpFilterEditProfileIndex_Type = Unsigned32
_CIgmpFilterEditProfileIndex_Object = MibScalar
cIgmpFilterEditProfileIndex = _CIgmpFilterEditProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 2),
    _CIgmpFilterEditProfileIndex_Type()
)
cIgmpFilterEditProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditProfileIndex.setStatus("current")
_CIgmpFilterEditStartAddressType_Type = InetAddressType
_CIgmpFilterEditStartAddressType_Object = MibScalar
cIgmpFilterEditStartAddressType = _CIgmpFilterEditStartAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 3),
    _CIgmpFilterEditStartAddressType_Type()
)
cIgmpFilterEditStartAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditStartAddressType.setStatus("current")


class _CIgmpFilterEditStartAddress_Type(InetAddress):
    """Custom type cIgmpFilterEditStartAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CIgmpFilterEditStartAddress_Type.__name__ = "InetAddress"
_CIgmpFilterEditStartAddress_Object = MibScalar
cIgmpFilterEditStartAddress = _CIgmpFilterEditStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 4),
    _CIgmpFilterEditStartAddress_Type()
)
cIgmpFilterEditStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditStartAddress.setStatus("current")
_CIgmpFilterEditEndAddressType_Type = InetAddressType
_CIgmpFilterEditEndAddressType_Object = MibScalar
cIgmpFilterEditEndAddressType = _CIgmpFilterEditEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 5),
    _CIgmpFilterEditEndAddressType_Type()
)
cIgmpFilterEditEndAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditEndAddressType.setStatus("current")
_CIgmpFilterEditEndAddress_Type = InetAddress
_CIgmpFilterEditEndAddress_Object = MibScalar
cIgmpFilterEditEndAddress = _CIgmpFilterEditEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 6),
    _CIgmpFilterEditEndAddress_Type()
)
cIgmpFilterEditEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditEndAddress.setStatus("current")


class _CIgmpFilterEditProfileAction_Type(Integer32):
    """Custom type cIgmpFilterEditProfileAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_CIgmpFilterEditProfileAction_Type.__name__ = "Integer32"
_CIgmpFilterEditProfileAction_Object = MibScalar
cIgmpFilterEditProfileAction = _CIgmpFilterEditProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 7),
    _CIgmpFilterEditProfileAction_Type()
)
cIgmpFilterEditProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditProfileAction.setStatus("current")


class _CIgmpFilterEditOperation_Type(Integer32):
    """Custom type cIgmpFilterEditOperation based on Integer32"""
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
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("none", 1))
    )


_CIgmpFilterEditOperation_Type.__name__ = "Integer32"
_CIgmpFilterEditOperation_Object = MibScalar
cIgmpFilterEditOperation = _CIgmpFilterEditOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 8),
    _CIgmpFilterEditOperation_Type()
)
cIgmpFilterEditOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIgmpFilterEditOperation.setStatus("current")


class _CIgmpFilterApplyStatus_Type(Integer32):
    """Custom type cIgmpFilterApplyStatus based on Integer32"""
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
        *(("entryNotPresentError", 5),
          ("entryPresentError", 4),
          ("inconsistentEdit", 3),
          ("someOtherError", 1),
          ("succeeded", 2))
    )


_CIgmpFilterApplyStatus_Type.__name__ = "Integer32"
_CIgmpFilterApplyStatus_Object = MibScalar
cIgmpFilterApplyStatus = _CIgmpFilterApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 1, 3, 9),
    _CIgmpFilterApplyStatus_Type()
)
cIgmpFilterApplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIgmpFilterApplyStatus.setStatus("current")
_CiscoIgmpFilterMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIgmpFilterMIBConformance = _CiscoIgmpFilterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2)
)
_CiscoIgmpFilterMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIgmpFilterMIBCompliances = _CiscoIgmpFilterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 1)
)
_CiscoIgmpFilterMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIgmpFilterMIBGroups = _CiscoIgmpFilterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 2)
)

# Managed Objects groups

ciscoIgmpFilterGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 2, 1)
)
ciscoIgmpFilterGlobalGroup.setObjects(
      *(("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEnable"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterMaxProfiles"))
)
if mibBuilder.loadTexts:
    ciscoIgmpFilterGlobalGroup.setStatus("current")

ciscoIgmpFilterInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 2, 2)
)
ciscoIgmpFilterInfoGroup.setObjects(
      *(("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEndAddressType"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEndAddress"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterProfileAction"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterInterfaceProfileIndex"))
)
if mibBuilder.loadTexts:
    ciscoIgmpFilterInfoGroup.setStatus("current")

ciscoIgmpFilterEditorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 2, 3)
)
ciscoIgmpFilterEditorGroup.setObjects(
      *(("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditSpinLock"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditProfileIndex"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditStartAddressType"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditStartAddress"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditEndAddressType"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditEndAddress"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditProfileAction"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterEditOperation"),
        ("CISCO-IGMP-FILTER-MIB", "cIgmpFilterApplyStatus"))
)
if mibBuilder.loadTexts:
    ciscoIgmpFilterEditorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIgmpFilterGolbalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIgmpFilterGolbalMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIgmpFilterGlobalMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 238, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIgmpFilterGlobalMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IGMP-FILTER-MIB",
    **{"ciscoIGMPFilterMIB": ciscoIGMPFilterMIB,
       "ciscoIgmpFilterMIBObjects": ciscoIgmpFilterMIBObjects,
       "cIgmpFilterGeneral": cIgmpFilterGeneral,
       "cIgmpFilterEnable": cIgmpFilterEnable,
       "cIgmpFilterMaxProfiles": cIgmpFilterMaxProfiles,
       "cIgmpFilterInfo": cIgmpFilterInfo,
       "cIgmpFilterTable": cIgmpFilterTable,
       "cIgmpFilterEntry": cIgmpFilterEntry,
       "cIgmpFilterProfileIndex": cIgmpFilterProfileIndex,
       "cIgmpFilterStartAddressType": cIgmpFilterStartAddressType,
       "cIgmpFilterStartAddress": cIgmpFilterStartAddress,
       "cIgmpFilterEndAddressType": cIgmpFilterEndAddressType,
       "cIgmpFilterEndAddress": cIgmpFilterEndAddress,
       "cIgmpFilterProfileAction": cIgmpFilterProfileAction,
       "cIgmpFilterInterfaceTable": cIgmpFilterInterfaceTable,
       "cIgmpFilterInterfaceEntry": cIgmpFilterInterfaceEntry,
       "cIgmpFilterInterfaceProfileIndex": cIgmpFilterInterfaceProfileIndex,
       "cIgmpFilterEditor": cIgmpFilterEditor,
       "cIgmpFilterEditSpinLock": cIgmpFilterEditSpinLock,
       "cIgmpFilterEditProfileIndex": cIgmpFilterEditProfileIndex,
       "cIgmpFilterEditStartAddressType": cIgmpFilterEditStartAddressType,
       "cIgmpFilterEditStartAddress": cIgmpFilterEditStartAddress,
       "cIgmpFilterEditEndAddressType": cIgmpFilterEditEndAddressType,
       "cIgmpFilterEditEndAddress": cIgmpFilterEditEndAddress,
       "cIgmpFilterEditProfileAction": cIgmpFilterEditProfileAction,
       "cIgmpFilterEditOperation": cIgmpFilterEditOperation,
       "cIgmpFilterApplyStatus": cIgmpFilterApplyStatus,
       "ciscoIgmpFilterMIBConformance": ciscoIgmpFilterMIBConformance,
       "ciscoIgmpFilterMIBCompliances": ciscoIgmpFilterMIBCompliances,
       "ciscoIgmpFilterGolbalMIBCompliance": ciscoIgmpFilterGolbalMIBCompliance,
       "ciscoIgmpFilterGlobalMIBComplianceRev1": ciscoIgmpFilterGlobalMIBComplianceRev1,
       "ciscoIgmpFilterMIBGroups": ciscoIgmpFilterMIBGroups,
       "ciscoIgmpFilterGlobalGroup": ciscoIgmpFilterGlobalGroup,
       "ciscoIgmpFilterInfoGroup": ciscoIgmpFilterInfoGroup,
       "ciscoIgmpFilterEditorGroup": ciscoIgmpFilterEditorGroup}
)
