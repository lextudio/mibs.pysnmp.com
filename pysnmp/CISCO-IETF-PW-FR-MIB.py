# SNMP MIB module (CISCO-IETF-PW-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PW-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:56 2024
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

(DlciNumber,) = mibBuilder.importSymbols(
    "CISCO-FRAME-RELAY-MIB",
    "DlciNumber")

(CpwVcIndexType,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwVcIndexType")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

cpwVcFrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112)
)
cpwVcFrMIB.setRevisions(
        ("2003-12-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpwVcFrNotifications_ObjectIdentity = ObjectIdentity
cpwVcFrNotifications = _CpwVcFrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 0)
)
_CpwVcFrObjects_ObjectIdentity = ObjectIdentity
cpwVcFrObjects = _CpwVcFrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1)
)
_CpwVcFrTable_Object = MibTable
cpwVcFrTable = _CpwVcFrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1)
)
if mibBuilder.loadTexts:
    cpwVcFrTable.setStatus("current")
_CpwVcFrEntry_Object = MibTableRow
cpwVcFrEntry = _CpwVcFrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1)
)
cpwVcFrEntry.setIndexNames(
    (0, "CISCO-IETF-PW-FR-MIB", "cpwVcFrPwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcFrEntry.setStatus("current")
_CpwVcFrPwVcIndex_Type = CpwVcIndexType
_CpwVcFrPwVcIndex_Object = MibTableColumn
cpwVcFrPwVcIndex = _CpwVcFrPwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 1),
    _CpwVcFrPwVcIndex_Type()
)
cpwVcFrPwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcFrPwVcIndex.setStatus("current")


class _CpwVcFrIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cpwVcFrIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CpwVcFrIfIndex_Object = MibTableColumn
cpwVcFrIfIndex = _CpwVcFrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 2),
    _CpwVcFrIfIndex_Type()
)
cpwVcFrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrIfIndex.setStatus("current")
_CpwVcFrDlci_Type = DlciNumber
_CpwVcFrDlci_Object = MibTableColumn
cpwVcFrDlci = _CpwVcFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 3),
    _CpwVcFrDlci_Type()
)
cpwVcFrDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrDlci.setStatus("current")


class _CpwVcFrAdminStatus_Type(Integer32):
    """Custom type cpwVcFrAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CpwVcFrAdminStatus_Type.__name__ = "Integer32"
_CpwVcFrAdminStatus_Object = MibTableColumn
cpwVcFrAdminStatus = _CpwVcFrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 4),
    _CpwVcFrAdminStatus_Type()
)
cpwVcFrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrAdminStatus.setStatus("current")


class _CpwVcFrOperStatus_Type(Integer32):
    """Custom type cpwVcFrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unknown", 3))
    )


_CpwVcFrOperStatus_Type.__name__ = "Integer32"
_CpwVcFrOperStatus_Object = MibTableColumn
cpwVcFrOperStatus = _CpwVcFrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 5),
    _CpwVcFrOperStatus_Type()
)
cpwVcFrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcFrOperStatus.setStatus("current")


class _CpwVcFrPw2FrOperStatus_Type(Integer32):
    """Custom type cpwVcFrPw2FrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unknown", 3))
    )


_CpwVcFrPw2FrOperStatus_Type.__name__ = "Integer32"
_CpwVcFrPw2FrOperStatus_Object = MibTableColumn
cpwVcFrPw2FrOperStatus = _CpwVcFrPw2FrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 6),
    _CpwVcFrPw2FrOperStatus_Type()
)
cpwVcFrPw2FrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcFrPw2FrOperStatus.setStatus("current")
_CpwVcFrRowStatus_Type = RowStatus
_CpwVcFrRowStatus_Object = MibTableColumn
cpwVcFrRowStatus = _CpwVcFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 7),
    _CpwVcFrRowStatus_Type()
)
cpwVcFrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrRowStatus.setStatus("current")
_CpwVcFrStorageType_Type = StorageType
_CpwVcFrStorageType_Object = MibTableColumn
cpwVcFrStorageType = _CpwVcFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 1, 1, 8),
    _CpwVcFrStorageType_Type()
)
cpwVcFrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrStorageType.setStatus("current")
_CpwVcFrPMTable_Object = MibTable
cpwVcFrPMTable = _CpwVcFrPMTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2)
)
if mibBuilder.loadTexts:
    cpwVcFrPMTable.setStatus("current")
_CpwVcFrPMEntry_Object = MibTableRow
cpwVcFrPMEntry = _CpwVcFrPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1)
)
cpwVcFrPMEntry.setIndexNames(
    (0, "CISCO-IETF-PW-FR-MIB", "cpwVcFrPMPwVcIndex"),
)
if mibBuilder.loadTexts:
    cpwVcFrPMEntry.setStatus("current")
_CpwVcFrPMPwVcIndex_Type = CpwVcIndexType
_CpwVcFrPMPwVcIndex_Object = MibTableColumn
cpwVcFrPMPwVcIndex = _CpwVcFrPMPwVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 1),
    _CpwVcFrPMPwVcIndex_Type()
)
cpwVcFrPMPwVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpwVcFrPMPwVcIndex.setStatus("current")
_CpwVcFrPMIfIndex_Type = InterfaceIndexOrZero
_CpwVcFrPMIfIndex_Object = MibTableColumn
cpwVcFrPMIfIndex = _CpwVcFrPMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 2),
    _CpwVcFrPMIfIndex_Type()
)
cpwVcFrPMIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrPMIfIndex.setStatus("current")


class _CpwVcFrPMAdminStatus_Type(Integer32):
    """Custom type cpwVcFrPMAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CpwVcFrPMAdminStatus_Type.__name__ = "Integer32"
_CpwVcFrPMAdminStatus_Object = MibTableColumn
cpwVcFrPMAdminStatus = _CpwVcFrPMAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 3),
    _CpwVcFrPMAdminStatus_Type()
)
cpwVcFrPMAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrPMAdminStatus.setStatus("current")


class _CpwVcFrPMOperStatus_Type(Integer32):
    """Custom type cpwVcFrPMOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unknown", 3))
    )


_CpwVcFrPMOperStatus_Type.__name__ = "Integer32"
_CpwVcFrPMOperStatus_Object = MibTableColumn
cpwVcFrPMOperStatus = _CpwVcFrPMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 4),
    _CpwVcFrPMOperStatus_Type()
)
cpwVcFrPMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcFrPMOperStatus.setStatus("current")


class _CpwVcFrPMPw2FrOperStatus_Type(Integer32):
    """Custom type cpwVcFrPMPw2FrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unknown", 3))
    )


_CpwVcFrPMPw2FrOperStatus_Type.__name__ = "Integer32"
_CpwVcFrPMPw2FrOperStatus_Object = MibTableColumn
cpwVcFrPMPw2FrOperStatus = _CpwVcFrPMPw2FrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 5),
    _CpwVcFrPMPw2FrOperStatus_Type()
)
cpwVcFrPMPw2FrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpwVcFrPMPw2FrOperStatus.setStatus("current")
_CpwVcFrPMRowStatus_Type = RowStatus
_CpwVcFrPMRowStatus_Object = MibTableColumn
cpwVcFrPMRowStatus = _CpwVcFrPMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 6),
    _CpwVcFrPMRowStatus_Type()
)
cpwVcFrPMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrPMRowStatus.setStatus("current")
_CpwVcFrPMStorageType_Type = StorageType
_CpwVcFrPMStorageType_Object = MibTableColumn
cpwVcFrPMStorageType = _CpwVcFrPMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 1, 2, 1, 7),
    _CpwVcFrPMStorageType_Type()
)
cpwVcFrPMStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpwVcFrPMStorageType.setStatus("current")
_CpwVcFrConformance_ObjectIdentity = ObjectIdentity
cpwVcFrConformance = _CpwVcFrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2)
)
_CpwVcFrCompliances_ObjectIdentity = ObjectIdentity
cpwVcFrCompliances = _CpwVcFrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1)
)
_CpwVcFrGroups_ObjectIdentity = ObjectIdentity
cpwVcFrGroups = _CpwVcFrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2)
)

# Managed Objects groups

cpwVcFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2, 1)
)
cpwVcFrGroup.setObjects(
      *(("CISCO-IETF-PW-FR-MIB", "cpwVcFrIfIndex"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrDlci"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrAdminStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrOperStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPw2FrOperStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrRowStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcFrGroup.setStatus("current")

cpwVcFrPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 2, 2)
)
cpwVcFrPMGroup.setObjects(
      *(("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMIfIndex"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMAdminStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMOperStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMPw2FrOperStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMRowStatus"),
        ("CISCO-IETF-PW-FR-MIB", "cpwVcFrPMStorageType"))
)
if mibBuilder.loadTexts:
    cpwVcFrPMGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cpwVcFrFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpwVcFrFullCompliance.setStatus(
        "current"
    )

cpwVcFrReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 112, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpwVcFrReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PW-FR-MIB",
    **{"cpwVcFrMIB": cpwVcFrMIB,
       "cpwVcFrNotifications": cpwVcFrNotifications,
       "cpwVcFrObjects": cpwVcFrObjects,
       "cpwVcFrTable": cpwVcFrTable,
       "cpwVcFrEntry": cpwVcFrEntry,
       "cpwVcFrPwVcIndex": cpwVcFrPwVcIndex,
       "cpwVcFrIfIndex": cpwVcFrIfIndex,
       "cpwVcFrDlci": cpwVcFrDlci,
       "cpwVcFrAdminStatus": cpwVcFrAdminStatus,
       "cpwVcFrOperStatus": cpwVcFrOperStatus,
       "cpwVcFrPw2FrOperStatus": cpwVcFrPw2FrOperStatus,
       "cpwVcFrRowStatus": cpwVcFrRowStatus,
       "cpwVcFrStorageType": cpwVcFrStorageType,
       "cpwVcFrPMTable": cpwVcFrPMTable,
       "cpwVcFrPMEntry": cpwVcFrPMEntry,
       "cpwVcFrPMPwVcIndex": cpwVcFrPMPwVcIndex,
       "cpwVcFrPMIfIndex": cpwVcFrPMIfIndex,
       "cpwVcFrPMAdminStatus": cpwVcFrPMAdminStatus,
       "cpwVcFrPMOperStatus": cpwVcFrPMOperStatus,
       "cpwVcFrPMPw2FrOperStatus": cpwVcFrPMPw2FrOperStatus,
       "cpwVcFrPMRowStatus": cpwVcFrPMRowStatus,
       "cpwVcFrPMStorageType": cpwVcFrPMStorageType,
       "cpwVcFrConformance": cpwVcFrConformance,
       "cpwVcFrCompliances": cpwVcFrCompliances,
       "cpwVcFrFullCompliance": cpwVcFrFullCompliance,
       "cpwVcFrReadOnlyCompliance": cpwVcFrReadOnlyCompliance,
       "cpwVcFrGroups": cpwVcFrGroups,
       "cpwVcFrGroup": cpwVcFrGroup,
       "cpwVcFrPMGroup": cpwVcFrPMGroup}
)
