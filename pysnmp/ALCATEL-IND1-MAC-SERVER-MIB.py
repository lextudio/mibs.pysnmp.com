# SNMP MIB module (ALCATEL-IND1-MAC-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-MAC-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:33 2024
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

(hardentIND1Physical,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "hardentIND1Physical")

(physicalIndex,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-CHASSIS-MIB",
    "physicalIndex")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1MacServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3)
)
alcatelIND1MacServerMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddrGlobalLocalStatusType(Integer32, TextualConvention):
    status = "current"
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
        *(("globallyAdministered", 2),
          ("globallyAdministeredOverlap", 4),
          ("locallyAdministered", 3),
          ("notApplicable", 1))
    )



class MacRangeIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MacServerMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1MacServerMIBNotifications = _AlcatelIND1MacServerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBNotifications.setStatus("current")
_AlcatelIND1MacServerMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MacServerMIBObjects = _AlcatelIND1MacServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBObjects.setStatus("current")
_ChasMacAddressRangeTable_Object = MibTable
chasMacAddressRangeTable = _ChasMacAddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    chasMacAddressRangeTable.setStatus("current")
_ChasMacAddrRangeTableEntry_Object = MibTableRow
chasMacAddrRangeTableEntry = _ChasMacAddrRangeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1)
)
chasMacAddrRangeTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "ALCATEL-IND1-MAC-SERVER-MIB", "chasMacRangeIndex"),
)
if mibBuilder.loadTexts:
    chasMacAddrRangeTableEntry.setStatus("current")
_ChasMacRangeIndex_Type = MacRangeIndex
_ChasMacRangeIndex_Object = MibTableColumn
chasMacRangeIndex = _ChasMacRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1, 1),
    _ChasMacRangeIndex_Type()
)
chasMacRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasMacRangeIndex.setStatus("current")
_ChasMacAddressStart_Type = MacAddress
_ChasMacAddressStart_Object = MibTableColumn
chasMacAddressStart = _ChasMacAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1, 2),
    _ChasMacAddressStart_Type()
)
chasMacAddressStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasMacAddressStart.setStatus("current")


class _ChasMacAddressCount_Type(Integer32):
    """Custom type chasMacAddressCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ChasMacAddressCount_Type.__name__ = "Integer32"
_ChasMacAddressCount_Object = MibTableColumn
chasMacAddressCount = _ChasMacAddressCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1, 3),
    _ChasMacAddressCount_Type()
)
chasMacAddressCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasMacAddressCount.setStatus("current")
_ChasGlobalLocal_Type = MacAddrGlobalLocalStatusType
_ChasGlobalLocal_Object = MibTableColumn
chasGlobalLocal = _ChasGlobalLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1, 4),
    _ChasGlobalLocal_Type()
)
chasGlobalLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasGlobalLocal.setStatus("current")
_ChasMacRowStatus_Type = RowStatus
_ChasMacRowStatus_Object = MibTableColumn
chasMacRowStatus = _ChasMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 1, 1, 5),
    _ChasMacRowStatus_Type()
)
chasMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasMacRowStatus.setStatus("current")
_ChasMacAddressAllocTable_Object = MibTable
chasMacAddressAllocTable = _ChasMacAddressAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    chasMacAddressAllocTable.setStatus("current")
_ChasMacAddressAllocTableEntry_Object = MibTableRow
chasMacAddressAllocTableEntry = _ChasMacAddressAllocTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1)
)
chasMacAddressAllocTableEntry.setIndexNames(
    (0, "ALCATEL-IND1-MAC-SERVER-MIB", "chasAppId"),
    (0, "ALCATEL-IND1-MAC-SERVER-MIB", "chasObjectId"),
)
if mibBuilder.loadTexts:
    chasMacAddressAllocTableEntry.setStatus("current")


class _ChasAppId_Type(Unsigned32):
    """Custom type chasAppId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasAppId_Type.__name__ = "Unsigned32"
_ChasAppId_Object = MibTableColumn
chasAppId = _ChasAppId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1, 1),
    _ChasAppId_Type()
)
chasAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasAppId.setStatus("current")


class _ChasObjectId_Type(Unsigned32):
    """Custom type chasObjectId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChasObjectId_Type.__name__ = "Unsigned32"
_ChasObjectId_Object = MibTableColumn
chasObjectId = _ChasObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1, 2),
    _ChasObjectId_Type()
)
chasObjectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chasObjectId.setStatus("current")
_ChasAllocMacRangeIndex_Type = MacRangeIndex
_ChasAllocMacRangeIndex_Object = MibTableColumn
chasAllocMacRangeIndex = _ChasAllocMacRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1, 3),
    _ChasAllocMacRangeIndex_Type()
)
chasAllocMacRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAllocMacRangeIndex.setStatus("current")
_ChasAllocMacAddress_Type = MacAddress
_ChasAllocMacAddress_Object = MibTableColumn
chasAllocMacAddress = _ChasAllocMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1, 4),
    _ChasAllocMacAddress_Type()
)
chasAllocMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasAllocMacAddress.setStatus("current")
_ChasAllocRowStatus_Type = RowStatus
_ChasAllocRowStatus_Object = MibTableColumn
chasAllocRowStatus = _ChasAllocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 2, 1, 5),
    _ChasAllocRowStatus_Type()
)
chasAllocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    chasAllocRowStatus.setStatus("current")
_ChasMacAddrDupAllocStatusTable_ObjectIdentity = ObjectIdentity
chasMacAddrDupAllocStatusTable = _ChasMacAddrDupAllocStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 3)
)


class _ChasMacAddrDuplicationStatus_Type(Integer32):
    """Custom type chasMacAddrDuplicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChasMacAddrDuplicationStatus_Type.__name__ = "Integer32"
_ChasMacAddrDuplicationStatus_Object = MibScalar
chasMacAddrDuplicationStatus = _ChasMacAddrDuplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 3, 1),
    _ChasMacAddrDuplicationStatus_Type()
)
chasMacAddrDuplicationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasMacAddrDuplicationStatus.setStatus("current")


class _ChasMacAddrAllocLocallyAdminStatus_Type(Integer32):
    """Custom type chasMacAddrAllocLocallyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChasMacAddrAllocLocallyAdminStatus_Type.__name__ = "Integer32"
_ChasMacAddrAllocLocallyAdminStatus_Object = MibScalar
chasMacAddrAllocLocallyAdminStatus = _ChasMacAddrAllocLocallyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 3, 2),
    _ChasMacAddrAllocLocallyAdminStatus_Type()
)
chasMacAddrAllocLocallyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasMacAddrAllocLocallyAdminStatus.setStatus("current")
_ChasMacAddrRetentionObjects_ObjectIdentity = ObjectIdentity
chasMacAddrRetentionObjects = _ChasMacAddrRetentionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4)
)


class _ChasMacAddrRetentionStatus_Type(Integer32):
    """Custom type chasMacAddrRetentionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChasMacAddrRetentionStatus_Type.__name__ = "Integer32"
_ChasMacAddrRetentionStatus_Object = MibScalar
chasMacAddrRetentionStatus = _ChasMacAddrRetentionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 1),
    _ChasMacAddrRetentionStatus_Type()
)
chasMacAddrRetentionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasMacAddrRetentionStatus.setStatus("current")


class _ChasPossibleDuplicateMacTrapStatus_Type(Integer32):
    """Custom type chasPossibleDuplicateMacTrapStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChasPossibleDuplicateMacTrapStatus_Type.__name__ = "Integer32"
_ChasPossibleDuplicateMacTrapStatus_Object = MibScalar
chasPossibleDuplicateMacTrapStatus = _ChasPossibleDuplicateMacTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 2),
    _ChasPossibleDuplicateMacTrapStatus_Type()
)
chasPossibleDuplicateMacTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasPossibleDuplicateMacTrapStatus.setStatus("current")


class _ChasRingStatus_Type(Integer32):
    """Custom type chasRingStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_ChasRingStatus_Type.__name__ = "Integer32"
_ChasRingStatus_Object = MibScalar
chasRingStatus = _ChasRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 3),
    _ChasRingStatus_Type()
)
chasRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasRingStatus.setStatus("current")


class _ChasBaseMacAddrSource_Type(Integer32):
    """Custom type chasBaseMacAddrSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eEPROM", 2),
          ("retained", 1))
    )


_ChasBaseMacAddrSource_Type.__name__ = "Integer32"
_ChasBaseMacAddrSource_Object = MibScalar
chasBaseMacAddrSource = _ChasBaseMacAddrSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 4),
    _ChasBaseMacAddrSource_Type()
)
chasBaseMacAddrSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBaseMacAddrSource.setStatus("current")
_ChasBaseMacAddr_Type = MacAddress
_ChasBaseMacAddr_Object = MibScalar
chasBaseMacAddr = _ChasBaseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 5),
    _ChasBaseMacAddr_Type()
)
chasBaseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasBaseMacAddr.setStatus("current")


class _ChasBaseMacReleaseAction_Type(Integer32):
    """Custom type chasBaseMacReleaseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSignificant", 0),
          ("releaseMac", 1))
    )


_ChasBaseMacReleaseAction_Type.__name__ = "Integer32"
_ChasBaseMacReleaseAction_Object = MibScalar
chasBaseMacReleaseAction = _ChasBaseMacReleaseAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 6),
    _ChasBaseMacReleaseAction_Type()
)
chasBaseMacReleaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBaseMacReleaseAction.setStatus("current")


class _ChasBaseMacAddrRetentionTimer_Type(Unsigned32):
    """Custom type chasBaseMacAddrRetentionTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChasBaseMacAddrRetentionTimer_Type.__name__ = "Unsigned32"
_ChasBaseMacAddrRetentionTimer_Object = MibScalar
chasBaseMacAddrRetentionTimer = _ChasBaseMacAddrRetentionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 4, 7),
    _ChasBaseMacAddrRetentionTimer_Type()
)
chasBaseMacAddrRetentionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chasBaseMacAddrRetentionTimer.setStatus("current")
_AlaMacServerTrapObjs_ObjectIdentity = ObjectIdentity
alaMacServerTrapObjs = _AlaMacServerTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 5)
)
_ChasTrapMacRangeIndex_Type = MacRangeIndex
_ChasTrapMacRangeIndex_Object = MibScalar
chasTrapMacRangeIndex = _ChasTrapMacRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 5, 1),
    _ChasTrapMacRangeIndex_Type()
)
chasTrapMacRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasTrapMacRangeIndex.setStatus("current")
_BaseMacAddress_Type = MacAddress
_BaseMacAddress_Object = MibScalar
baseMacAddress = _BaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 1, 5, 2),
    _BaseMacAddress_Type()
)
baseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseMacAddress.setStatus("current")
_AlcatelIND1MacServerMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MacServerMIBConformance = _AlcatelIND1MacServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBConformance.setStatus("current")
_AlcatelIND1MacServerMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MacServerMIBGroups = _AlcatelIND1MacServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBGroups.setStatus("current")
_AlcatelIND1MacServerMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MacServerMIBCompliances = _AlcatelIND1MacServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBCompliances.setStatus("current")

# Managed Objects groups

chasMacAddrRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 1)
)
chasMacAddrRangeGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacAddressStart"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacAddressCount"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasGlobalLocal"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacRowStatus"))
)
if mibBuilder.loadTexts:
    chasMacAddrRangeGroup.setStatus("current")

chasMacAddressAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 2)
)
chasMacAddressAllocGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "chasAllocMacRangeIndex"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasAllocMacAddress"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasAllocRowStatus"))
)
if mibBuilder.loadTexts:
    chasMacAddressAllocGroup.setStatus("current")

chasMacAddrDupAllocStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 3)
)
chasMacAddrDupAllocStatusGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacAddrDuplicationStatus"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacAddrAllocLocallyAdminStatus"))
)
if mibBuilder.loadTexts:
    chasMacAddrDupAllocStatusGroup.setStatus("current")

chasMacAddrRetentionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 5)
)
chasMacAddrRetentionGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "chasMacAddrRetentionStatus"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasPossibleDuplicateMacTrapStatus"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasRingStatus"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasBaseMacAddrSource"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasBaseMacAddr"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasBaseMacReleaseAction"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasBaseMacAddrRetentionTimer"))
)
if mibBuilder.loadTexts:
    chasMacAddrRetentionGroup.setStatus("current")

chasNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 7)
)
chasNotificationObjectGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "baseMacAddress"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasTrapMacRangeIndex"))
)
if mibBuilder.loadTexts:
    chasNotificationObjectGroup.setStatus("current")


# Notification objects

chassisTrapsMacOverlap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 0, 1)
)
chassisTrapsMacOverlap.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chasTrapMacRangeIndex"))
)
if mibBuilder.loadTexts:
    chassisTrapsMacOverlap.setStatus(
        "current"
    )

chassisTrapsPossibleDuplicateMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 0, 2)
)
chassisTrapsPossibleDuplicateMac.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "baseMacAddress"))
)
if mibBuilder.loadTexts:
    chassisTrapsPossibleDuplicateMac.setStatus(
        "current"
    )

chassisTrapsDuplicateMacCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 0, 3)
)
chassisTrapsDuplicateMacCleared.setObjects(
      *(("ALCATEL-IND1-CHASSIS-MIB", "physicalIndex"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "baseMacAddress"))
)
if mibBuilder.loadTexts:
    chassisTrapsDuplicateMacCleared.setStatus(
        "current"
    )


# Notifications groups

chasTrapsMacOverlapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 4)
)
chasTrapsMacOverlapGroup.setObjects(
    ("ALCATEL-IND1-MAC-SERVER-MIB", "chassisTrapsMacOverlap")
)
if mibBuilder.loadTexts:
    chasTrapsMacOverlapGroup.setStatus(
        "current"
    )

chasTrapsPossibleDuplicateMacGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 1, 6)
)
chasTrapsPossibleDuplicateMacGroup.setObjects(
      *(("ALCATEL-IND1-MAC-SERVER-MIB", "chassisTrapsPossibleDuplicateMac"),
        ("ALCATEL-IND1-MAC-SERVER-MIB", "chassisTrapsDuplicateMacCleared"))
)
if mibBuilder.loadTexts:
    chasTrapsPossibleDuplicateMacGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1MacServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 1, 1, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MAC-SERVER-MIB",
    **{"MacAddrGlobalLocalStatusType": MacAddrGlobalLocalStatusType,
       "MacRangeIndex": MacRangeIndex,
       "alcatelIND1MacServerMIB": alcatelIND1MacServerMIB,
       "alcatelIND1MacServerMIBNotifications": alcatelIND1MacServerMIBNotifications,
       "chassisTrapsMacOverlap": chassisTrapsMacOverlap,
       "chassisTrapsPossibleDuplicateMac": chassisTrapsPossibleDuplicateMac,
       "chassisTrapsDuplicateMacCleared": chassisTrapsDuplicateMacCleared,
       "alcatelIND1MacServerMIBObjects": alcatelIND1MacServerMIBObjects,
       "chasMacAddressRangeTable": chasMacAddressRangeTable,
       "chasMacAddrRangeTableEntry": chasMacAddrRangeTableEntry,
       "chasMacRangeIndex": chasMacRangeIndex,
       "chasMacAddressStart": chasMacAddressStart,
       "chasMacAddressCount": chasMacAddressCount,
       "chasGlobalLocal": chasGlobalLocal,
       "chasMacRowStatus": chasMacRowStatus,
       "chasMacAddressAllocTable": chasMacAddressAllocTable,
       "chasMacAddressAllocTableEntry": chasMacAddressAllocTableEntry,
       "chasAppId": chasAppId,
       "chasObjectId": chasObjectId,
       "chasAllocMacRangeIndex": chasAllocMacRangeIndex,
       "chasAllocMacAddress": chasAllocMacAddress,
       "chasAllocRowStatus": chasAllocRowStatus,
       "chasMacAddrDupAllocStatusTable": chasMacAddrDupAllocStatusTable,
       "chasMacAddrDuplicationStatus": chasMacAddrDuplicationStatus,
       "chasMacAddrAllocLocallyAdminStatus": chasMacAddrAllocLocallyAdminStatus,
       "chasMacAddrRetentionObjects": chasMacAddrRetentionObjects,
       "chasMacAddrRetentionStatus": chasMacAddrRetentionStatus,
       "chasPossibleDuplicateMacTrapStatus": chasPossibleDuplicateMacTrapStatus,
       "chasRingStatus": chasRingStatus,
       "chasBaseMacAddrSource": chasBaseMacAddrSource,
       "chasBaseMacAddr": chasBaseMacAddr,
       "chasBaseMacReleaseAction": chasBaseMacReleaseAction,
       "chasBaseMacAddrRetentionTimer": chasBaseMacAddrRetentionTimer,
       "alaMacServerTrapObjs": alaMacServerTrapObjs,
       "chasTrapMacRangeIndex": chasTrapMacRangeIndex,
       "baseMacAddress": baseMacAddress,
       "alcatelIND1MacServerMIBConformance": alcatelIND1MacServerMIBConformance,
       "alcatelIND1MacServerMIBGroups": alcatelIND1MacServerMIBGroups,
       "chasMacAddrRangeGroup": chasMacAddrRangeGroup,
       "chasMacAddressAllocGroup": chasMacAddressAllocGroup,
       "chasMacAddrDupAllocStatusGroup": chasMacAddrDupAllocStatusGroup,
       "chasTrapsMacOverlapGroup": chasTrapsMacOverlapGroup,
       "chasMacAddrRetentionGroup": chasMacAddrRetentionGroup,
       "chasTrapsPossibleDuplicateMacGroup": chasTrapsPossibleDuplicateMacGroup,
       "chasNotificationObjectGroup": chasNotificationObjectGroup,
       "alcatelIND1MacServerMIBCompliances": alcatelIND1MacServerMIBCompliances,
       "alcatelIND1MacServerMIBCompliance": alcatelIND1MacServerMIBCompliance}
)
