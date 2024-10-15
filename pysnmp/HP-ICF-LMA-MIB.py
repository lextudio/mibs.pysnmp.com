# SNMP MIB module (HP-ICF-LMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-LMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:44 2024
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

(HpAutzUserRoleName,) = mibBuilder.importSymbols(
    "HP-AUTZ-MIB",
    "HpAutzUserRoleName")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfLmaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97)
)
hpicfLmaMIB.setRevisions(
        ("2017-06-28 07:10",
         "2016-02-12 07:10",
         "2013-04-10 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfLmaNotifications_ObjectIdentity = ObjectIdentity
hpicfLmaNotifications = _HpicfLmaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 0)
)
_HpicfLmaObjects_ObjectIdentity = ObjectIdentity
hpicfLmaObjects = _HpicfLmaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1)
)
_HpicfLmaConfigObjects_ObjectIdentity = ObjectIdentity
hpicfLmaConfigObjects = _HpicfLmaConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1)
)
_HpicfLmaScalarObjects_ObjectIdentity = ObjectIdentity
hpicfLmaScalarObjects = _HpicfLmaScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 1)
)
_HpicfLmaMacGrpTable_Object = MibTable
hpicfLmaMacGrpTable = _HpicfLmaMacGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfLmaMacGrpTable.setStatus("current")
_HpicfLmaMacGrpEntry_Object = MibTableRow
hpicfLmaMacGrpEntry = _HpicfLmaMacGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1)
)
hpicfLmaMacGrpEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaMacGrpName"),
)
if mibBuilder.loadTexts:
    hpicfLmaMacGrpEntry.setStatus("current")


class _HpicfLmaMacGrpName_Type(DisplayString):
    """Custom type hpicfLmaMacGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfLmaMacGrpName_Type.__name__ = "DisplayString"
_HpicfLmaMacGrpName_Object = MibTableColumn
hpicfLmaMacGrpName = _HpicfLmaMacGrpName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1, 1),
    _HpicfLmaMacGrpName_Type()
)
hpicfLmaMacGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaMacGrpName.setStatus("current")
_HpicfLmaMacGrpRowStatus_Type = RowStatus
_HpicfLmaMacGrpRowStatus_Object = MibTableColumn
hpicfLmaMacGrpRowStatus = _HpicfLmaMacGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 2, 1, 2),
    _HpicfLmaMacGrpRowStatus_Type()
)
hpicfLmaMacGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaMacGrpRowStatus.setStatus("current")
_HpicfLmaMacTable_Object = MibTable
hpicfLmaMacTable = _HpicfLmaMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfLmaMacTable.setStatus("current")
_HpicfLmaMacEntry_Object = MibTableRow
hpicfLmaMacEntry = _HpicfLmaMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1)
)
hpicfLmaMacEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaMacGrpName"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaMacType"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaMacValue"),
)
if mibBuilder.loadTexts:
    hpicfLmaMacEntry.setStatus("current")


class _HpicfLmaMacType_Type(Integer32):
    """Custom type hpicfLmaMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("macMask", 2),
          ("macOui", 3))
    )


_HpicfLmaMacType_Type.__name__ = "Integer32"
_HpicfLmaMacType_Object = MibTableColumn
hpicfLmaMacType = _HpicfLmaMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 1),
    _HpicfLmaMacType_Type()
)
hpicfLmaMacType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaMacType.setStatus("current")


class _HpicfLmaMacValue_Type(OctetString):
    """Custom type hpicfLmaMacValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_HpicfLmaMacValue_Type.__name__ = "OctetString"
_HpicfLmaMacValue_Object = MibTableColumn
hpicfLmaMacValue = _HpicfLmaMacValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 2),
    _HpicfLmaMacValue_Type()
)
hpicfLmaMacValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaMacValue.setStatus("current")
_HpicfLmaMacRowStatus_Type = RowStatus
_HpicfLmaMacRowStatus_Object = MibTableColumn
hpicfLmaMacRowStatus = _HpicfLmaMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 3, 1, 3),
    _HpicfLmaMacRowStatus_Type()
)
hpicfLmaMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaMacRowStatus.setStatus("current")
_HpicfLmaProfileTable_Object = MibTable
hpicfLmaProfileTable = _HpicfLmaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfLmaProfileTable.setStatus("current")
_HpicfLmaProfileEntry_Object = MibTableRow
hpicfLmaProfileEntry = _HpicfLmaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1)
)
hpicfLmaProfileEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaProfileName"),
)
if mibBuilder.loadTexts:
    hpicfLmaProfileEntry.setStatus("current")


class _HpicfLmaProfileName_Type(DisplayString):
    """Custom type hpicfLmaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfLmaProfileName_Type.__name__ = "DisplayString"
_HpicfLmaProfileName_Object = MibTableColumn
hpicfLmaProfileName = _HpicfLmaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 1),
    _HpicfLmaProfileName_Type()
)
hpicfLmaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaProfileName.setStatus("current")


class _HpicfLmaProfileUntaggedVid_Type(Integer32):
    """Custom type hpicfLmaProfileUntaggedVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfLmaProfileUntaggedVid_Type.__name__ = "Integer32"
_HpicfLmaProfileUntaggedVid_Object = MibTableColumn
hpicfLmaProfileUntaggedVid = _HpicfLmaProfileUntaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 2),
    _HpicfLmaProfileUntaggedVid_Type()
)
hpicfLmaProfileUntaggedVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaProfileUntaggedVid.setStatus("current")
_HpicfLmaProfileTaggedVids_Type = VidList
_HpicfLmaProfileTaggedVids_Object = MibTableColumn
hpicfLmaProfileTaggedVids = _HpicfLmaProfileTaggedVids_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 3),
    _HpicfLmaProfileTaggedVids_Type()
)
hpicfLmaProfileTaggedVids.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaProfileTaggedVids.setStatus("current")


class _HpicfLmaProfileCoS_Type(Integer32):
    """Custom type hpicfLmaProfileCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_HpicfLmaProfileCoS_Type.__name__ = "Integer32"
_HpicfLmaProfileCoS_Object = MibTableColumn
hpicfLmaProfileCoS = _HpicfLmaProfileCoS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 4),
    _HpicfLmaProfileCoS_Type()
)
hpicfLmaProfileCoS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaProfileCoS.setStatus("current")
_HpicfLmaProfileIsAssociated_Type = TruthValue
_HpicfLmaProfileIsAssociated_Object = MibTableColumn
hpicfLmaProfileIsAssociated = _HpicfLmaProfileIsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 5),
    _HpicfLmaProfileIsAssociated_Type()
)
hpicfLmaProfileIsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaProfileIsAssociated.setStatus("current")
_HpicfLmaProfileRowStatus_Type = RowStatus
_HpicfLmaProfileRowStatus_Object = MibTableColumn
hpicfLmaProfileRowStatus = _HpicfLmaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 4, 1, 6),
    _HpicfLmaProfileRowStatus_Type()
)
hpicfLmaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaProfileRowStatus.setStatus("current")
_HpicfLmaAssociationTable_Object = MibTable
hpicfLmaAssociationTable = _HpicfLmaAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfLmaAssociationTable.setStatus("current")
_HpicfLmaAssociationEntry_Object = MibTableRow
hpicfLmaAssociationEntry = _HpicfLmaAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1)
)
hpicfLmaAssociationEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaProfileName"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaAssociationMacType"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaAssociationMacValue"),
)
if mibBuilder.loadTexts:
    hpicfLmaAssociationEntry.setStatus("current")


class _HpicfLmaAssociationMacType_Type(Integer32):
    """Custom type hpicfLmaAssociationMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("macGrp", 0),
          ("macMask", 2),
          ("macOui", 3))
    )


_HpicfLmaAssociationMacType_Type.__name__ = "Integer32"
_HpicfLmaAssociationMacType_Object = MibTableColumn
hpicfLmaAssociationMacType = _HpicfLmaAssociationMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 2),
    _HpicfLmaAssociationMacType_Type()
)
hpicfLmaAssociationMacType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaAssociationMacType.setStatus("current")


class _HpicfLmaAssociationMacValue_Type(OctetString):
    """Custom type hpicfLmaAssociationMacValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfLmaAssociationMacValue_Type.__name__ = "OctetString"
_HpicfLmaAssociationMacValue_Object = MibTableColumn
hpicfLmaAssociationMacValue = _HpicfLmaAssociationMacValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 4),
    _HpicfLmaAssociationMacValue_Type()
)
hpicfLmaAssociationMacValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaAssociationMacValue.setStatus("current")
_HpicfLmaAssociationRowStatus_Type = RowStatus
_HpicfLmaAssociationRowStatus_Object = MibTableColumn
hpicfLmaAssociationRowStatus = _HpicfLmaAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 5, 1, 5),
    _HpicfLmaAssociationRowStatus_Type()
)
hpicfLmaAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaAssociationRowStatus.setStatus("current")
_HpicfLmaConfigTable_Object = MibTable
hpicfLmaConfigTable = _HpicfLmaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfLmaConfigTable.setStatus("current")
_HpicfLmaConfigEntry_Object = MibTableRow
hpicfLmaConfigEntry = _HpicfLmaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1)
)
hpicfLmaConfigEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaPortNumber"),
)
if mibBuilder.loadTexts:
    hpicfLmaConfigEntry.setStatus("current")
_HpicfLmaPortNumber_Type = InterfaceIndex
_HpicfLmaPortNumber_Object = MibTableColumn
hpicfLmaPortNumber = _HpicfLmaPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 1),
    _HpicfLmaPortNumber_Type()
)
hpicfLmaPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaPortNumber.setStatus("current")


class _HpicfLmaClientLimit_Type(Integer32):
    """Custom type hpicfLmaClientLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HpicfLmaClientLimit_Type.__name__ = "Integer32"
_HpicfLmaClientLimit_Object = MibTableColumn
hpicfLmaClientLimit = _HpicfLmaClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 2),
    _HpicfLmaClientLimit_Type()
)
hpicfLmaClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaClientLimit.setStatus("current")


class _HpicfLmaQuietPeriod_Type(Integer32):
    """Custom type hpicfLmaQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfLmaQuietPeriod_Type.__name__ = "Integer32"
_HpicfLmaQuietPeriod_Object = MibTableColumn
hpicfLmaQuietPeriod = _HpicfLmaQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 4),
    _HpicfLmaQuietPeriod_Type()
)
hpicfLmaQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaQuietPeriod.setStatus("current")


class _HpicfLmaLogoffPeriod_Type(Integer32):
    """Custom type hpicfLmaLogoffPeriod based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999999),
    )


_HpicfLmaLogoffPeriod_Type.__name__ = "Integer32"
_HpicfLmaLogoffPeriod_Object = MibTableColumn
hpicfLmaLogoffPeriod = _HpicfLmaLogoffPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 5),
    _HpicfLmaLogoffPeriod_Type()
)
hpicfLmaLogoffPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaLogoffPeriod.setStatus("current")


class _HpicfLmaAuthVid_Type(Integer32):
    """Custom type hpicfLmaAuthVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfLmaAuthVid_Type.__name__ = "Integer32"
_HpicfLmaAuthVid_Object = MibTableColumn
hpicfLmaAuthVid = _HpicfLmaAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 7),
    _HpicfLmaAuthVid_Type()
)
hpicfLmaAuthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaAuthVid.setStatus("current")


class _HpicfLmaUnauthVid_Type(Integer32):
    """Custom type hpicfLmaUnauthVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfLmaUnauthVid_Type.__name__ = "Integer32"
_HpicfLmaUnauthVid_Object = MibTableColumn
hpicfLmaUnauthVid = _HpicfLmaUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 8),
    _HpicfLmaUnauthVid_Type()
)
hpicfLmaUnauthVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaUnauthVid.setStatus("current")


class _HpicfLmaUnAuthPeriod_Type(Integer32):
    """Custom type hpicfLmaUnAuthPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfLmaUnAuthPeriod_Type.__name__ = "Integer32"
_HpicfLmaUnAuthPeriod_Object = MibTableColumn
hpicfLmaUnAuthPeriod = _HpicfLmaUnAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 9),
    _HpicfLmaUnAuthPeriod_Type()
)
hpicfLmaUnAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaUnAuthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfLmaUnAuthPeriod.setUnits("seconds")
_HpicfLmaReauthenticate_Type = TruthValue
_HpicfLmaReauthenticate_Object = MibTableColumn
hpicfLmaReauthenticate = _HpicfLmaReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 10),
    _HpicfLmaReauthenticate_Type()
)
hpicfLmaReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaReauthenticate.setStatus("current")


class _HpicfLmaMacPin_Type(TruthValue):
    """Custom type hpicfLmaMacPin based on TruthValue"""
    defaultValue = 2


_HpicfLmaMacPin_Object = MibTableColumn
hpicfLmaMacPin = _HpicfLmaMacPin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 6, 1, 11),
    _HpicfLmaMacPin_Type()
)
hpicfLmaMacPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLmaMacPin.setStatus("current")
_HpicfLmaUserRoleAssociationTable_Object = MibTable
hpicfLmaUserRoleAssociationTable = _HpicfLmaUserRoleAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationTable.setStatus("current")
_HpicfLmaUserRoleAssociationEntry_Object = MibTableRow
hpicfLmaUserRoleAssociationEntry = _HpicfLmaUserRoleAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1)
)
hpicfLmaUserRoleAssociationEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationName"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationMacType"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationMacValue"),
)
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationEntry.setStatus("current")
_HpicfLmaUserRoleAssociationName_Type = HpAutzUserRoleName
_HpicfLmaUserRoleAssociationName_Object = MibTableColumn
hpicfLmaUserRoleAssociationName = _HpicfLmaUserRoleAssociationName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 1),
    _HpicfLmaUserRoleAssociationName_Type()
)
hpicfLmaUserRoleAssociationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationName.setStatus("current")


class _HpicfLmaUserRoleAssociationMacType_Type(Integer32):
    """Custom type hpicfLmaUserRoleAssociationMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 1),
          ("macGrp", 0),
          ("macMask", 2),
          ("macOui", 3))
    )


_HpicfLmaUserRoleAssociationMacType_Type.__name__ = "Integer32"
_HpicfLmaUserRoleAssociationMacType_Object = MibTableColumn
hpicfLmaUserRoleAssociationMacType = _HpicfLmaUserRoleAssociationMacType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 2),
    _HpicfLmaUserRoleAssociationMacType_Type()
)
hpicfLmaUserRoleAssociationMacType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationMacType.setStatus("current")


class _HpicfLmaUserRoleAssociationMacValue_Type(OctetString):
    """Custom type hpicfLmaUserRoleAssociationMacValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfLmaUserRoleAssociationMacValue_Type.__name__ = "OctetString"
_HpicfLmaUserRoleAssociationMacValue_Object = MibTableColumn
hpicfLmaUserRoleAssociationMacValue = _HpicfLmaUserRoleAssociationMacValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 3),
    _HpicfLmaUserRoleAssociationMacValue_Type()
)
hpicfLmaUserRoleAssociationMacValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationMacValue.setStatus("current")
_HpicfLmaUserRoleAssociationRowStatus_Type = RowStatus
_HpicfLmaUserRoleAssociationRowStatus_Object = MibTableColumn
hpicfLmaUserRoleAssociationRowStatus = _HpicfLmaUserRoleAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 1, 7, 1, 4),
    _HpicfLmaUserRoleAssociationRowStatus_Type()
)
hpicfLmaUserRoleAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfLmaUserRoleAssociationRowStatus.setStatus("current")
_HpicfLmaStatsObjects_ObjectIdentity = ObjectIdentity
hpicfLmaStatsObjects = _HpicfLmaStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2)
)
_HpicfLmaSessionStatsTable_Object = MibTable
hpicfLmaSessionStatsTable = _HpicfLmaSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfLmaSessionStatsTable.setStatus("current")
_HpicfLmaSessionStatsEntry_Object = MibTableRow
hpicfLmaSessionStatsEntry = _HpicfLmaSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1)
)
hpicfLmaSessionStatsEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaPortNumber"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaSessionMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfLmaSessionStatsEntry.setStatus("current")
_HpicfLmaSessionMacAddr_Type = MacAddress
_HpicfLmaSessionMacAddr_Object = MibTableColumn
hpicfLmaSessionMacAddr = _HpicfLmaSessionMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 1),
    _HpicfLmaSessionMacAddr_Type()
)
hpicfLmaSessionMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaSessionMacAddr.setStatus("current")


class _HpicfLmaSessionState_Type(Integer32):
    """Custom type hpicfLmaSessionState based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("authReqRejectNoVlan", 4),
          ("authReqRejectUnauthVlan", 5),
          ("authReqTimeoutNoVlan", 6),
          ("authReqTimeoutUnauthVlan", 7),
          ("authenticated", 1),
          ("authenticating", 3),
          ("initialRole", 8),
          ("initialRoleFailed", 9),
          ("unauthenticated", 2))
    )


_HpicfLmaSessionState_Type.__name__ = "Integer32"
_HpicfLmaSessionState_Object = MibTableColumn
hpicfLmaSessionState = _HpicfLmaSessionState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 2),
    _HpicfLmaSessionState_Type()
)
hpicfLmaSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionState.setStatus("current")
_HpicfLmaSessionStateTime_Type = Unsigned32
_HpicfLmaSessionStateTime_Object = MibTableColumn
hpicfLmaSessionStateTime = _HpicfLmaSessionStateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 3),
    _HpicfLmaSessionStateTime_Type()
)
hpicfLmaSessionStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionStateTime.setStatus("current")


class _HpicfLmaSessionAuthVid_Type(Integer32):
    """Custom type hpicfLmaSessionAuthVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfLmaSessionAuthVid_Type.__name__ = "Integer32"
_HpicfLmaSessionAuthVid_Object = MibTableColumn
hpicfLmaSessionAuthVid = _HpicfLmaSessionAuthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 4),
    _HpicfLmaSessionAuthVid_Type()
)
hpicfLmaSessionAuthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionAuthVid.setStatus("current")


class _HpicfLmaSessionUnauthVid_Type(Integer32):
    """Custom type hpicfLmaSessionUnauthVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfLmaSessionUnauthVid_Type.__name__ = "Integer32"
_HpicfLmaSessionUnauthVid_Object = MibTableColumn
hpicfLmaSessionUnauthVid = _HpicfLmaSessionUnauthVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 5),
    _HpicfLmaSessionUnauthVid_Type()
)
hpicfLmaSessionUnauthVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionUnauthVid.setStatus("current")


class _HpicfLmaSessionUsrNumberCnt_Type(Counter32):
    """Custom type hpicfLmaSessionUsrNumberCnt based on Counter32"""
    defaultValue = 0


_HpicfLmaSessionUsrNumberCnt_Object = MibTableColumn
hpicfLmaSessionUsrNumberCnt = _HpicfLmaSessionUsrNumberCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 6),
    _HpicfLmaSessionUsrNumberCnt_Type()
)
hpicfLmaSessionUsrNumberCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionUsrNumberCnt.setStatus("current")
_HpicfLmaSessionUserRole_Type = HpAutzUserRoleName
_HpicfLmaSessionUserRole_Object = MibTableColumn
hpicfLmaSessionUserRole = _HpicfLmaSessionUserRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 1, 1, 7),
    _HpicfLmaSessionUserRole_Type()
)
hpicfLmaSessionUserRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaSessionUserRole.setStatus("current")
_HpicfLmaAssocActiveTable_Object = MibTable
hpicfLmaAssocActiveTable = _HpicfLmaAssocActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfLmaAssocActiveTable.setStatus("current")
_HpicfLmaAssocActiveEntry_Object = MibTableRow
hpicfLmaAssocActiveEntry = _HpicfLmaAssocActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1)
)
hpicfLmaAssocActiveEntry.setIndexNames(
    (0, "HP-ICF-LMA-MIB", "hpicfLmaAssocActiveProfileName"),
    (0, "HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"),
)
if mibBuilder.loadTexts:
    hpicfLmaAssocActiveEntry.setStatus("current")


class _HpicfLmaAssocActiveProfileName_Type(DisplayString):
    """Custom type hpicfLmaAssocActiveProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfLmaAssocActiveProfileName_Type.__name__ = "DisplayString"
_HpicfLmaAssocActiveProfileName_Object = MibTableColumn
hpicfLmaAssocActiveProfileName = _HpicfLmaAssocActiveProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1, 1),
    _HpicfLmaAssocActiveProfileName_Type()
)
hpicfLmaAssocActiveProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfLmaAssocActiveProfileName.setStatus("current")
_HpicfLmaAssocActiveMacAddress_Type = MacAddress
_HpicfLmaAssocActiveMacAddress_Object = MibTableColumn
hpicfLmaAssocActiveMacAddress = _HpicfLmaAssocActiveMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 1, 2, 2, 1, 2),
    _HpicfLmaAssocActiveMacAddress_Type()
)
hpicfLmaAssocActiveMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfLmaAssocActiveMacAddress.setStatus("current")
_HpicfLmaConformance_ObjectIdentity = ObjectIdentity
hpicfLmaConformance = _HpicfLmaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2)
)
_HpicfLmaCompliances_ObjectIdentity = ObjectIdentity
hpicfLmaCompliances = _HpicfLmaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1)
)
_HpicfLmaGroups_ObjectIdentity = ObjectIdentity
hpicfLmaGroups = _HpicfLmaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2)
)

# Managed Objects groups

hpicfLmaMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 1)
)
hpicfLmaMacGroup.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaMacGrpRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaMacRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileUntaggedVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileTaggedVids"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileCoS"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileIsAssociated"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaAssociationRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfLmaMacGroup.setStatus("deprecated")

hpicfLmaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 2)
)
hpicfLmaConfigGroup.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"),
        ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"))
)
if mibBuilder.loadTexts:
    hpicfLmaConfigGroup.setStatus("deprecated")

hpicfLmaSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 3)
)
hpicfLmaSessionStatsGroup.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionState"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionStateTime"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionAuthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionUnauthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionUsrNumberCnt"))
)
if mibBuilder.loadTexts:
    hpicfLmaSessionStatsGroup.setStatus("deprecated")

hpicfLmaMacGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 4)
)
hpicfLmaMacGroup1.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaMacGrpRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaMacRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileUntaggedVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileTaggedVids"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileCoS"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileIsAssociated"),
        ("HP-ICF-LMA-MIB", "hpicfLmaProfileRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaAssociationRowStatus"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUserRoleAssociationRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfLmaMacGroup1.setStatus("current")

hpicfLmaConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 5)
)
hpicfLmaConfigGroup1.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"),
        ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"))
)
if mibBuilder.loadTexts:
    hpicfLmaConfigGroup1.setStatus("deprecated")

hpicfLmaSessionStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 6)
)
hpicfLmaSessionStatsGroup1.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaAssocActiveMacAddress"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionState"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionStateTime"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionAuthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionUnauthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionUsrNumberCnt"),
        ("HP-ICF-LMA-MIB", "hpicfLmaSessionUserRole"))
)
if mibBuilder.loadTexts:
    hpicfLmaSessionStatsGroup1.setStatus("current")

hpicfLmaConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 2, 7)
)
hpicfLmaConfigGroup2.setObjects(
      *(("HP-ICF-LMA-MIB", "hpicfLmaClientLimit"),
        ("HP-ICF-LMA-MIB", "hpicfLmaQuietPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaLogoffPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaAuthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnauthVid"),
        ("HP-ICF-LMA-MIB", "hpicfLmaUnAuthPeriod"),
        ("HP-ICF-LMA-MIB", "hpicfLmaReauthenticate"),
        ("HP-ICF-LMA-MIB", "hpicfLmaMacPin"))
)
if mibBuilder.loadTexts:
    hpicfLmaConfigGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfLmaCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfLmaCompliance1.setStatus(
        "deprecated"
    )

hpicfLmaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfLmaCompliance2.setStatus(
        "deprecated"
    )

hpicfLmaCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 97, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfLmaCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-LMA-MIB",
    **{"hpicfLmaMIB": hpicfLmaMIB,
       "hpicfLmaNotifications": hpicfLmaNotifications,
       "hpicfLmaObjects": hpicfLmaObjects,
       "hpicfLmaConfigObjects": hpicfLmaConfigObjects,
       "hpicfLmaScalarObjects": hpicfLmaScalarObjects,
       "hpicfLmaMacGrpTable": hpicfLmaMacGrpTable,
       "hpicfLmaMacGrpEntry": hpicfLmaMacGrpEntry,
       "hpicfLmaMacGrpName": hpicfLmaMacGrpName,
       "hpicfLmaMacGrpRowStatus": hpicfLmaMacGrpRowStatus,
       "hpicfLmaMacTable": hpicfLmaMacTable,
       "hpicfLmaMacEntry": hpicfLmaMacEntry,
       "hpicfLmaMacType": hpicfLmaMacType,
       "hpicfLmaMacValue": hpicfLmaMacValue,
       "hpicfLmaMacRowStatus": hpicfLmaMacRowStatus,
       "hpicfLmaProfileTable": hpicfLmaProfileTable,
       "hpicfLmaProfileEntry": hpicfLmaProfileEntry,
       "hpicfLmaProfileName": hpicfLmaProfileName,
       "hpicfLmaProfileUntaggedVid": hpicfLmaProfileUntaggedVid,
       "hpicfLmaProfileTaggedVids": hpicfLmaProfileTaggedVids,
       "hpicfLmaProfileCoS": hpicfLmaProfileCoS,
       "hpicfLmaProfileIsAssociated": hpicfLmaProfileIsAssociated,
       "hpicfLmaProfileRowStatus": hpicfLmaProfileRowStatus,
       "hpicfLmaAssociationTable": hpicfLmaAssociationTable,
       "hpicfLmaAssociationEntry": hpicfLmaAssociationEntry,
       "hpicfLmaAssociationMacType": hpicfLmaAssociationMacType,
       "hpicfLmaAssociationMacValue": hpicfLmaAssociationMacValue,
       "hpicfLmaAssociationRowStatus": hpicfLmaAssociationRowStatus,
       "hpicfLmaConfigTable": hpicfLmaConfigTable,
       "hpicfLmaConfigEntry": hpicfLmaConfigEntry,
       "hpicfLmaPortNumber": hpicfLmaPortNumber,
       "hpicfLmaClientLimit": hpicfLmaClientLimit,
       "hpicfLmaQuietPeriod": hpicfLmaQuietPeriod,
       "hpicfLmaLogoffPeriod": hpicfLmaLogoffPeriod,
       "hpicfLmaAuthVid": hpicfLmaAuthVid,
       "hpicfLmaUnauthVid": hpicfLmaUnauthVid,
       "hpicfLmaUnAuthPeriod": hpicfLmaUnAuthPeriod,
       "hpicfLmaReauthenticate": hpicfLmaReauthenticate,
       "hpicfLmaMacPin": hpicfLmaMacPin,
       "hpicfLmaUserRoleAssociationTable": hpicfLmaUserRoleAssociationTable,
       "hpicfLmaUserRoleAssociationEntry": hpicfLmaUserRoleAssociationEntry,
       "hpicfLmaUserRoleAssociationName": hpicfLmaUserRoleAssociationName,
       "hpicfLmaUserRoleAssociationMacType": hpicfLmaUserRoleAssociationMacType,
       "hpicfLmaUserRoleAssociationMacValue": hpicfLmaUserRoleAssociationMacValue,
       "hpicfLmaUserRoleAssociationRowStatus": hpicfLmaUserRoleAssociationRowStatus,
       "hpicfLmaStatsObjects": hpicfLmaStatsObjects,
       "hpicfLmaSessionStatsTable": hpicfLmaSessionStatsTable,
       "hpicfLmaSessionStatsEntry": hpicfLmaSessionStatsEntry,
       "hpicfLmaSessionMacAddr": hpicfLmaSessionMacAddr,
       "hpicfLmaSessionState": hpicfLmaSessionState,
       "hpicfLmaSessionStateTime": hpicfLmaSessionStateTime,
       "hpicfLmaSessionAuthVid": hpicfLmaSessionAuthVid,
       "hpicfLmaSessionUnauthVid": hpicfLmaSessionUnauthVid,
       "hpicfLmaSessionUsrNumberCnt": hpicfLmaSessionUsrNumberCnt,
       "hpicfLmaSessionUserRole": hpicfLmaSessionUserRole,
       "hpicfLmaAssocActiveTable": hpicfLmaAssocActiveTable,
       "hpicfLmaAssocActiveEntry": hpicfLmaAssocActiveEntry,
       "hpicfLmaAssocActiveProfileName": hpicfLmaAssocActiveProfileName,
       "hpicfLmaAssocActiveMacAddress": hpicfLmaAssocActiveMacAddress,
       "hpicfLmaConformance": hpicfLmaConformance,
       "hpicfLmaCompliances": hpicfLmaCompliances,
       "hpicfLmaCompliance1": hpicfLmaCompliance1,
       "hpicfLmaCompliance2": hpicfLmaCompliance2,
       "hpicfLmaCompliance3": hpicfLmaCompliance3,
       "hpicfLmaGroups": hpicfLmaGroups,
       "hpicfLmaMacGroup": hpicfLmaMacGroup,
       "hpicfLmaConfigGroup": hpicfLmaConfigGroup,
       "hpicfLmaSessionStatsGroup": hpicfLmaSessionStatsGroup,
       "hpicfLmaMacGroup1": hpicfLmaMacGroup1,
       "hpicfLmaConfigGroup1": hpicfLmaConfigGroup1,
       "hpicfLmaSessionStatsGroup1": hpicfLmaSessionStatsGroup1,
       "hpicfLmaConfigGroup2": hpicfLmaConfigGroup2}
)
