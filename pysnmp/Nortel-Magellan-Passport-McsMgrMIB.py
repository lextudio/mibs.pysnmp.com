# SNMP MIB module (Nortel-Magellan-Passport-McsMgrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-McsMgrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:40 2024
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

(DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McsMgr_ObjectIdentity = ObjectIdentity
mcsMgr = _McsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122)
)
_McsMgrRowStatusTable_Object = MibTable
mcsMgrRowStatusTable = _McsMgrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1)
)
if mibBuilder.loadTexts:
    mcsMgrRowStatusTable.setStatus("mandatory")
_McsMgrRowStatusEntry_Object = MibTableRow
mcsMgrRowStatusEntry = _McsMgrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1, 1)
)
mcsMgrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrRowStatusEntry.setStatus("mandatory")
_McsMgrRowStatus_Type = RowStatus
_McsMgrRowStatus_Object = MibTableColumn
mcsMgrRowStatus = _McsMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1, 1, 1),
    _McsMgrRowStatus_Type()
)
mcsMgrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrRowStatus.setStatus("mandatory")
_McsMgrComponentName_Type = DisplayString
_McsMgrComponentName_Object = MibTableColumn
mcsMgrComponentName = _McsMgrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1, 1, 2),
    _McsMgrComponentName_Type()
)
mcsMgrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrComponentName.setStatus("mandatory")
_McsMgrStorageType_Type = StorageType
_McsMgrStorageType_Object = MibTableColumn
mcsMgrStorageType = _McsMgrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1, 1, 4),
    _McsMgrStorageType_Type()
)
mcsMgrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrStorageType.setStatus("mandatory")
_McsMgrIndex_Type = NonReplicated
_McsMgrIndex_Object = MibTableColumn
mcsMgrIndex = _McsMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 1, 1, 10),
    _McsMgrIndex_Type()
)
mcsMgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrIndex.setStatus("mandatory")
_McsMgrProvTable_Object = MibTable
mcsMgrProvTable = _McsMgrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10)
)
if mibBuilder.loadTexts:
    mcsMgrProvTable.setStatus("mandatory")
_McsMgrProvEntry_Object = MibTableRow
mcsMgrProvEntry = _McsMgrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1)
)
mcsMgrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrProvEntry.setStatus("mandatory")


class _McsMgrMaxEps_Type(Integer32):
    """Custom type mcsMgrMaxEps based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_McsMgrMaxEps_Type.__name__ = "Integer32"
_McsMgrMaxEps_Object = MibTableColumn
mcsMgrMaxEps = _McsMgrMaxEps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1, 1),
    _McsMgrMaxEps_Type()
)
mcsMgrMaxEps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrMaxEps.setStatus("mandatory")


class _McsMgrEpAlarmThreshold_Type(Integer32):
    """Custom type mcsMgrEpAlarmThreshold based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_McsMgrEpAlarmThreshold_Type.__name__ = "Integer32"
_McsMgrEpAlarmThreshold_Object = MibTableColumn
mcsMgrEpAlarmThreshold = _McsMgrEpAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1, 2),
    _McsMgrEpAlarmThreshold_Type()
)
mcsMgrEpAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrEpAlarmThreshold.setStatus("mandatory")


class _McsMgrOverrideNsapAddress_Type(AsciiString):
    """Custom type mcsMgrOverrideNsapAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_McsMgrOverrideNsapAddress_Type.__name__ = "AsciiString"
_McsMgrOverrideNsapAddress_Object = MibTableColumn
mcsMgrOverrideNsapAddress = _McsMgrOverrideNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1, 3),
    _McsMgrOverrideNsapAddress_Type()
)
mcsMgrOverrideNsapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrOverrideNsapAddress.setStatus("mandatory")
_McsMgrLogicalProcessor_Type = Link
_McsMgrLogicalProcessor_Object = MibTableColumn
mcsMgrLogicalProcessor = _McsMgrLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1, 4),
    _McsMgrLogicalProcessor_Type()
)
mcsMgrLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrLogicalProcessor.setStatus("obsolete")


class _McsMgrSecurity_Type(Integer32):
    """Custom type mcsMgrSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_McsMgrSecurity_Type.__name__ = "Integer32"
_McsMgrSecurity_Object = MibTableColumn
mcsMgrSecurity = _McsMgrSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 10, 1, 5),
    _McsMgrSecurity_Type()
)
mcsMgrSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrSecurity.setStatus("mandatory")
_McsMgrStateTable_Object = MibTable
mcsMgrStateTable = _McsMgrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11)
)
if mibBuilder.loadTexts:
    mcsMgrStateTable.setStatus("mandatory")
_McsMgrStateEntry_Object = MibTableRow
mcsMgrStateEntry = _McsMgrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1)
)
mcsMgrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrStateEntry.setStatus("mandatory")


class _McsMgrAdminState_Type(Integer32):
    """Custom type mcsMgrAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_McsMgrAdminState_Type.__name__ = "Integer32"
_McsMgrAdminState_Object = MibTableColumn
mcsMgrAdminState = _McsMgrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 1),
    _McsMgrAdminState_Type()
)
mcsMgrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrAdminState.setStatus("mandatory")


class _McsMgrOperationalState_Type(Integer32):
    """Custom type mcsMgrOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_McsMgrOperationalState_Type.__name__ = "Integer32"
_McsMgrOperationalState_Object = MibTableColumn
mcsMgrOperationalState = _McsMgrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 2),
    _McsMgrOperationalState_Type()
)
mcsMgrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrOperationalState.setStatus("mandatory")


class _McsMgrUsageState_Type(Integer32):
    """Custom type mcsMgrUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_McsMgrUsageState_Type.__name__ = "Integer32"
_McsMgrUsageState_Object = MibTableColumn
mcsMgrUsageState = _McsMgrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 3),
    _McsMgrUsageState_Type()
)
mcsMgrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrUsageState.setStatus("mandatory")


class _McsMgrAvailabilityStatus_Type(OctetString):
    """Custom type mcsMgrAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_McsMgrAvailabilityStatus_Type.__name__ = "OctetString"
_McsMgrAvailabilityStatus_Object = MibTableColumn
mcsMgrAvailabilityStatus = _McsMgrAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 4),
    _McsMgrAvailabilityStatus_Type()
)
mcsMgrAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrAvailabilityStatus.setStatus("mandatory")


class _McsMgrProceduralStatus_Type(OctetString):
    """Custom type mcsMgrProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrProceduralStatus_Type.__name__ = "OctetString"
_McsMgrProceduralStatus_Object = MibTableColumn
mcsMgrProceduralStatus = _McsMgrProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 5),
    _McsMgrProceduralStatus_Type()
)
mcsMgrProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrProceduralStatus.setStatus("mandatory")


class _McsMgrControlStatus_Type(OctetString):
    """Custom type mcsMgrControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrControlStatus_Type.__name__ = "OctetString"
_McsMgrControlStatus_Object = MibTableColumn
mcsMgrControlStatus = _McsMgrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 6),
    _McsMgrControlStatus_Type()
)
mcsMgrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrControlStatus.setStatus("mandatory")


class _McsMgrAlarmStatus_Type(OctetString):
    """Custom type mcsMgrAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrAlarmStatus_Type.__name__ = "OctetString"
_McsMgrAlarmStatus_Object = MibTableColumn
mcsMgrAlarmStatus = _McsMgrAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 7),
    _McsMgrAlarmStatus_Type()
)
mcsMgrAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrAlarmStatus.setStatus("mandatory")


class _McsMgrStandbyStatus_Type(Integer32):
    """Custom type mcsMgrStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_McsMgrStandbyStatus_Type.__name__ = "Integer32"
_McsMgrStandbyStatus_Object = MibTableColumn
mcsMgrStandbyStatus = _McsMgrStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 8),
    _McsMgrStandbyStatus_Type()
)
mcsMgrStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrStandbyStatus.setStatus("mandatory")


class _McsMgrUnknownStatus_Type(Integer32):
    """Custom type mcsMgrUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_McsMgrUnknownStatus_Type.__name__ = "Integer32"
_McsMgrUnknownStatus_Object = MibTableColumn
mcsMgrUnknownStatus = _McsMgrUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 11, 1, 9),
    _McsMgrUnknownStatus_Type()
)
mcsMgrUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrUnknownStatus.setStatus("mandatory")
_McsMgrOperTable_Object = MibTable
mcsMgrOperTable = _McsMgrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 12)
)
if mibBuilder.loadTexts:
    mcsMgrOperTable.setStatus("mandatory")
_McsMgrOperEntry_Object = MibTableRow
mcsMgrOperEntry = _McsMgrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 12, 1)
)
mcsMgrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrOperEntry.setStatus("mandatory")
_McsMgrCurrentLp_Type = RowPointer
_McsMgrCurrentLp_Object = MibTableColumn
mcsMgrCurrentLp = _McsMgrCurrentLp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 12, 1, 1),
    _McsMgrCurrentLp_Type()
)
mcsMgrCurrentLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrCurrentLp.setStatus("mandatory")


class _McsMgrCurrentEps_Type(Unsigned32):
    """Custom type mcsMgrCurrentEps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_McsMgrCurrentEps_Type.__name__ = "Unsigned32"
_McsMgrCurrentEps_Object = MibTableColumn
mcsMgrCurrentEps = _McsMgrCurrentEps_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 12, 1, 3),
    _McsMgrCurrentEps_Type()
)
mcsMgrCurrentEps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrCurrentEps.setStatus("mandatory")


class _McsMgrNsapAddress_Type(AsciiString):
    """Custom type mcsMgrNsapAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_McsMgrNsapAddress_Type.__name__ = "AsciiString"
_McsMgrNsapAddress_Object = MibTableColumn
mcsMgrNsapAddress = _McsMgrNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 12, 1, 4),
    _McsMgrNsapAddress_Type()
)
mcsMgrNsapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrNsapAddress.setStatus("mandatory")
_McsMgrCanLpsTable_Object = MibTable
mcsMgrCanLpsTable = _McsMgrCanLpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 418)
)
if mibBuilder.loadTexts:
    mcsMgrCanLpsTable.setStatus("mandatory")
_McsMgrCanLpsEntry_Object = MibTableRow
mcsMgrCanLpsEntry = _McsMgrCanLpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 418, 1)
)
mcsMgrCanLpsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrCanLpsValue"),
)
if mibBuilder.loadTexts:
    mcsMgrCanLpsEntry.setStatus("mandatory")
_McsMgrCanLpsValue_Type = RowPointer
_McsMgrCanLpsValue_Object = MibTableColumn
mcsMgrCanLpsValue = _McsMgrCanLpsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 418, 1, 1),
    _McsMgrCanLpsValue_Type()
)
mcsMgrCanLpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrCanLpsValue.setStatus("mandatory")
_McsMgrMIB_ObjectIdentity = ObjectIdentity
mcsMgrMIB = _McsMgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124)
)
_McsMgrGroup_ObjectIdentity = ObjectIdentity
mcsMgrGroup = _McsMgrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 1)
)
_McsMgrGroupBE_ObjectIdentity = ObjectIdentity
mcsMgrGroupBE = _McsMgrGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 1, 5)
)
_McsMgrGroupBE00_ObjectIdentity = ObjectIdentity
mcsMgrGroupBE00 = _McsMgrGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 1, 5, 1)
)
_McsMgrGroupBE00A_ObjectIdentity = ObjectIdentity
mcsMgrGroupBE00A = _McsMgrGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 1, 5, 1, 2)
)
_McsMgrCapabilities_ObjectIdentity = ObjectIdentity
mcsMgrCapabilities = _McsMgrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 3)
)
_McsMgrCapabilitiesBE_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesBE = _McsMgrCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 3, 5)
)
_McsMgrCapabilitiesBE00_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesBE00 = _McsMgrCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 3, 5, 1)
)
_McsMgrCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesBE00A = _McsMgrCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 124, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-McsMgrMIB",
    **{"mcsMgr": mcsMgr,
       "mcsMgrRowStatusTable": mcsMgrRowStatusTable,
       "mcsMgrRowStatusEntry": mcsMgrRowStatusEntry,
       "mcsMgrRowStatus": mcsMgrRowStatus,
       "mcsMgrComponentName": mcsMgrComponentName,
       "mcsMgrStorageType": mcsMgrStorageType,
       "mcsMgrIndex": mcsMgrIndex,
       "mcsMgrProvTable": mcsMgrProvTable,
       "mcsMgrProvEntry": mcsMgrProvEntry,
       "mcsMgrMaxEps": mcsMgrMaxEps,
       "mcsMgrEpAlarmThreshold": mcsMgrEpAlarmThreshold,
       "mcsMgrOverrideNsapAddress": mcsMgrOverrideNsapAddress,
       "mcsMgrLogicalProcessor": mcsMgrLogicalProcessor,
       "mcsMgrSecurity": mcsMgrSecurity,
       "mcsMgrStateTable": mcsMgrStateTable,
       "mcsMgrStateEntry": mcsMgrStateEntry,
       "mcsMgrAdminState": mcsMgrAdminState,
       "mcsMgrOperationalState": mcsMgrOperationalState,
       "mcsMgrUsageState": mcsMgrUsageState,
       "mcsMgrAvailabilityStatus": mcsMgrAvailabilityStatus,
       "mcsMgrProceduralStatus": mcsMgrProceduralStatus,
       "mcsMgrControlStatus": mcsMgrControlStatus,
       "mcsMgrAlarmStatus": mcsMgrAlarmStatus,
       "mcsMgrStandbyStatus": mcsMgrStandbyStatus,
       "mcsMgrUnknownStatus": mcsMgrUnknownStatus,
       "mcsMgrOperTable": mcsMgrOperTable,
       "mcsMgrOperEntry": mcsMgrOperEntry,
       "mcsMgrCurrentLp": mcsMgrCurrentLp,
       "mcsMgrCurrentEps": mcsMgrCurrentEps,
       "mcsMgrNsapAddress": mcsMgrNsapAddress,
       "mcsMgrCanLpsTable": mcsMgrCanLpsTable,
       "mcsMgrCanLpsEntry": mcsMgrCanLpsEntry,
       "mcsMgrCanLpsValue": mcsMgrCanLpsValue,
       "mcsMgrMIB": mcsMgrMIB,
       "mcsMgrGroup": mcsMgrGroup,
       "mcsMgrGroupBE": mcsMgrGroupBE,
       "mcsMgrGroupBE00": mcsMgrGroupBE00,
       "mcsMgrGroupBE00A": mcsMgrGroupBE00A,
       "mcsMgrCapabilities": mcsMgrCapabilities,
       "mcsMgrCapabilitiesBE": mcsMgrCapabilitiesBE,
       "mcsMgrCapabilitiesBE00": mcsMgrCapabilitiesBE00,
       "mcsMgrCapabilitiesBE00A": mcsMgrCapabilitiesBE00A}
)
