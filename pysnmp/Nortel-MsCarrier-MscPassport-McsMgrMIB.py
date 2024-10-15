# SNMP MIB module (Nortel-MsCarrier-MscPassport-McsMgrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-McsMgrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:17 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "Link",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscMcsMgr_ObjectIdentity = ObjectIdentity
mscMcsMgr = _MscMcsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122)
)
_MscMcsMgrRowStatusTable_Object = MibTable
mscMcsMgrRowStatusTable = _MscMcsMgrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrRowStatusTable.setStatus("mandatory")
_MscMcsMgrRowStatusEntry_Object = MibTableRow
mscMcsMgrRowStatusEntry = _MscMcsMgrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1, 1)
)
mscMcsMgrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrRowStatusEntry.setStatus("mandatory")
_MscMcsMgrRowStatus_Type = RowStatus
_MscMcsMgrRowStatus_Object = MibTableColumn
mscMcsMgrRowStatus = _MscMcsMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1, 1, 1),
    _MscMcsMgrRowStatus_Type()
)
mscMcsMgrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrRowStatus.setStatus("mandatory")
_MscMcsMgrComponentName_Type = DisplayString
_MscMcsMgrComponentName_Object = MibTableColumn
mscMcsMgrComponentName = _MscMcsMgrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1, 1, 2),
    _MscMcsMgrComponentName_Type()
)
mscMcsMgrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrComponentName.setStatus("mandatory")
_MscMcsMgrStorageType_Type = StorageType
_MscMcsMgrStorageType_Object = MibTableColumn
mscMcsMgrStorageType = _MscMcsMgrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1, 1, 4),
    _MscMcsMgrStorageType_Type()
)
mscMcsMgrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrStorageType.setStatus("mandatory")
_MscMcsMgrIndex_Type = NonReplicated
_MscMcsMgrIndex_Object = MibTableColumn
mscMcsMgrIndex = _MscMcsMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 1, 1, 10),
    _MscMcsMgrIndex_Type()
)
mscMcsMgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrIndex.setStatus("mandatory")
_MscMcsMgrProvTable_Object = MibTable
mscMcsMgrProvTable = _MscMcsMgrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrProvTable.setStatus("mandatory")
_MscMcsMgrProvEntry_Object = MibTableRow
mscMcsMgrProvEntry = _MscMcsMgrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1)
)
mscMcsMgrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrProvEntry.setStatus("mandatory")


class _MscMcsMgrMaxEps_Type(Integer32):
    """Custom type mscMcsMgrMaxEps based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_MscMcsMgrMaxEps_Type.__name__ = "Integer32"
_MscMcsMgrMaxEps_Object = MibTableColumn
mscMcsMgrMaxEps = _MscMcsMgrMaxEps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1, 1),
    _MscMcsMgrMaxEps_Type()
)
mscMcsMgrMaxEps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrMaxEps.setStatus("mandatory")


class _MscMcsMgrEpAlarmThreshold_Type(Integer32):
    """Custom type mscMcsMgrEpAlarmThreshold based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16384),
    )


_MscMcsMgrEpAlarmThreshold_Type.__name__ = "Integer32"
_MscMcsMgrEpAlarmThreshold_Object = MibTableColumn
mscMcsMgrEpAlarmThreshold = _MscMcsMgrEpAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1, 2),
    _MscMcsMgrEpAlarmThreshold_Type()
)
mscMcsMgrEpAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrEpAlarmThreshold.setStatus("mandatory")


class _MscMcsMgrOverrideNsapAddress_Type(AsciiString):
    """Custom type mscMcsMgrOverrideNsapAddress based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_MscMcsMgrOverrideNsapAddress_Type.__name__ = "AsciiString"
_MscMcsMgrOverrideNsapAddress_Object = MibTableColumn
mscMcsMgrOverrideNsapAddress = _MscMcsMgrOverrideNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1, 3),
    _MscMcsMgrOverrideNsapAddress_Type()
)
mscMcsMgrOverrideNsapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrOverrideNsapAddress.setStatus("mandatory")
_MscMcsMgrLogicalProcessor_Type = Link
_MscMcsMgrLogicalProcessor_Object = MibTableColumn
mscMcsMgrLogicalProcessor = _MscMcsMgrLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1, 4),
    _MscMcsMgrLogicalProcessor_Type()
)
mscMcsMgrLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrLogicalProcessor.setStatus("obsolete")


class _MscMcsMgrSecurity_Type(Integer32):
    """Custom type mscMcsMgrSecurity based on Integer32"""
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


_MscMcsMgrSecurity_Type.__name__ = "Integer32"
_MscMcsMgrSecurity_Object = MibTableColumn
mscMcsMgrSecurity = _MscMcsMgrSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 10, 1, 5),
    _MscMcsMgrSecurity_Type()
)
mscMcsMgrSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrSecurity.setStatus("mandatory")
_MscMcsMgrStateTable_Object = MibTable
mscMcsMgrStateTable = _MscMcsMgrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrStateTable.setStatus("mandatory")
_MscMcsMgrStateEntry_Object = MibTableRow
mscMcsMgrStateEntry = _MscMcsMgrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1)
)
mscMcsMgrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrStateEntry.setStatus("mandatory")


class _MscMcsMgrAdminState_Type(Integer32):
    """Custom type mscMcsMgrAdminState based on Integer32"""
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


_MscMcsMgrAdminState_Type.__name__ = "Integer32"
_MscMcsMgrAdminState_Object = MibTableColumn
mscMcsMgrAdminState = _MscMcsMgrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 1),
    _MscMcsMgrAdminState_Type()
)
mscMcsMgrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrAdminState.setStatus("mandatory")


class _MscMcsMgrOperationalState_Type(Integer32):
    """Custom type mscMcsMgrOperationalState based on Integer32"""
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


_MscMcsMgrOperationalState_Type.__name__ = "Integer32"
_MscMcsMgrOperationalState_Object = MibTableColumn
mscMcsMgrOperationalState = _MscMcsMgrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 2),
    _MscMcsMgrOperationalState_Type()
)
mscMcsMgrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrOperationalState.setStatus("mandatory")


class _MscMcsMgrUsageState_Type(Integer32):
    """Custom type mscMcsMgrUsageState based on Integer32"""
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


_MscMcsMgrUsageState_Type.__name__ = "Integer32"
_MscMcsMgrUsageState_Object = MibTableColumn
mscMcsMgrUsageState = _MscMcsMgrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 3),
    _MscMcsMgrUsageState_Type()
)
mscMcsMgrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrUsageState.setStatus("mandatory")


class _MscMcsMgrAvailabilityStatus_Type(OctetString):
    """Custom type mscMcsMgrAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMcsMgrAvailabilityStatus_Type.__name__ = "OctetString"
_MscMcsMgrAvailabilityStatus_Object = MibTableColumn
mscMcsMgrAvailabilityStatus = _MscMcsMgrAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 4),
    _MscMcsMgrAvailabilityStatus_Type()
)
mscMcsMgrAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrAvailabilityStatus.setStatus("mandatory")


class _MscMcsMgrProceduralStatus_Type(OctetString):
    """Custom type mscMcsMgrProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrProceduralStatus_Type.__name__ = "OctetString"
_MscMcsMgrProceduralStatus_Object = MibTableColumn
mscMcsMgrProceduralStatus = _MscMcsMgrProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 5),
    _MscMcsMgrProceduralStatus_Type()
)
mscMcsMgrProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrProceduralStatus.setStatus("mandatory")


class _MscMcsMgrControlStatus_Type(OctetString):
    """Custom type mscMcsMgrControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrControlStatus_Type.__name__ = "OctetString"
_MscMcsMgrControlStatus_Object = MibTableColumn
mscMcsMgrControlStatus = _MscMcsMgrControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 6),
    _MscMcsMgrControlStatus_Type()
)
mscMcsMgrControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrControlStatus.setStatus("mandatory")


class _MscMcsMgrAlarmStatus_Type(OctetString):
    """Custom type mscMcsMgrAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrAlarmStatus_Type.__name__ = "OctetString"
_MscMcsMgrAlarmStatus_Object = MibTableColumn
mscMcsMgrAlarmStatus = _MscMcsMgrAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 7),
    _MscMcsMgrAlarmStatus_Type()
)
mscMcsMgrAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrAlarmStatus.setStatus("mandatory")


class _MscMcsMgrStandbyStatus_Type(Integer32):
    """Custom type mscMcsMgrStandbyStatus based on Integer32"""
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


_MscMcsMgrStandbyStatus_Type.__name__ = "Integer32"
_MscMcsMgrStandbyStatus_Object = MibTableColumn
mscMcsMgrStandbyStatus = _MscMcsMgrStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 8),
    _MscMcsMgrStandbyStatus_Type()
)
mscMcsMgrStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrStandbyStatus.setStatus("mandatory")


class _MscMcsMgrUnknownStatus_Type(Integer32):
    """Custom type mscMcsMgrUnknownStatus based on Integer32"""
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


_MscMcsMgrUnknownStatus_Type.__name__ = "Integer32"
_MscMcsMgrUnknownStatus_Object = MibTableColumn
mscMcsMgrUnknownStatus = _MscMcsMgrUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 11, 1, 9),
    _MscMcsMgrUnknownStatus_Type()
)
mscMcsMgrUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrUnknownStatus.setStatus("mandatory")
_MscMcsMgrOperTable_Object = MibTable
mscMcsMgrOperTable = _MscMcsMgrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 12)
)
if mibBuilder.loadTexts:
    mscMcsMgrOperTable.setStatus("mandatory")
_MscMcsMgrOperEntry_Object = MibTableRow
mscMcsMgrOperEntry = _MscMcsMgrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 12, 1)
)
mscMcsMgrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrOperEntry.setStatus("mandatory")
_MscMcsMgrCurrentLp_Type = RowPointer
_MscMcsMgrCurrentLp_Object = MibTableColumn
mscMcsMgrCurrentLp = _MscMcsMgrCurrentLp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 12, 1, 1),
    _MscMcsMgrCurrentLp_Type()
)
mscMcsMgrCurrentLp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrCurrentLp.setStatus("mandatory")


class _MscMcsMgrCurrentEps_Type(Unsigned32):
    """Custom type mscMcsMgrCurrentEps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MscMcsMgrCurrentEps_Type.__name__ = "Unsigned32"
_MscMcsMgrCurrentEps_Object = MibTableColumn
mscMcsMgrCurrentEps = _MscMcsMgrCurrentEps_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 12, 1, 3),
    _MscMcsMgrCurrentEps_Type()
)
mscMcsMgrCurrentEps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrCurrentEps.setStatus("mandatory")


class _MscMcsMgrNsapAddress_Type(AsciiString):
    """Custom type mscMcsMgrNsapAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_MscMcsMgrNsapAddress_Type.__name__ = "AsciiString"
_MscMcsMgrNsapAddress_Object = MibTableColumn
mscMcsMgrNsapAddress = _MscMcsMgrNsapAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 12, 1, 4),
    _MscMcsMgrNsapAddress_Type()
)
mscMcsMgrNsapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrNsapAddress.setStatus("mandatory")
_MscMcsMgrCanLpsTable_Object = MibTable
mscMcsMgrCanLpsTable = _MscMcsMgrCanLpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 418)
)
if mibBuilder.loadTexts:
    mscMcsMgrCanLpsTable.setStatus("mandatory")
_MscMcsMgrCanLpsEntry_Object = MibTableRow
mscMcsMgrCanLpsEntry = _MscMcsMgrCanLpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 418, 1)
)
mscMcsMgrCanLpsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrCanLpsValue"),
)
if mibBuilder.loadTexts:
    mscMcsMgrCanLpsEntry.setStatus("mandatory")
_MscMcsMgrCanLpsValue_Type = RowPointer
_MscMcsMgrCanLpsValue_Object = MibTableColumn
mscMcsMgrCanLpsValue = _MscMcsMgrCanLpsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 418, 1, 1),
    _MscMcsMgrCanLpsValue_Type()
)
mscMcsMgrCanLpsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrCanLpsValue.setStatus("mandatory")
_McsMgrMIB_ObjectIdentity = ObjectIdentity
mcsMgrMIB = _McsMgrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124)
)
_McsMgrGroup_ObjectIdentity = ObjectIdentity
mcsMgrGroup = _McsMgrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 1)
)
_McsMgrGroupCA_ObjectIdentity = ObjectIdentity
mcsMgrGroupCA = _McsMgrGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 1, 1)
)
_McsMgrGroupCA02_ObjectIdentity = ObjectIdentity
mcsMgrGroupCA02 = _McsMgrGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 1, 1, 3)
)
_McsMgrGroupCA02A_ObjectIdentity = ObjectIdentity
mcsMgrGroupCA02A = _McsMgrGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 1, 1, 3, 2)
)
_McsMgrCapabilities_ObjectIdentity = ObjectIdentity
mcsMgrCapabilities = _McsMgrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 3)
)
_McsMgrCapabilitiesCA_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesCA = _McsMgrCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 3, 1)
)
_McsMgrCapabilitiesCA02_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesCA02 = _McsMgrCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 3, 1, 3)
)
_McsMgrCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
mcsMgrCapabilitiesCA02A = _McsMgrCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 124, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-McsMgrMIB",
    **{"mscMcsMgr": mscMcsMgr,
       "mscMcsMgrRowStatusTable": mscMcsMgrRowStatusTable,
       "mscMcsMgrRowStatusEntry": mscMcsMgrRowStatusEntry,
       "mscMcsMgrRowStatus": mscMcsMgrRowStatus,
       "mscMcsMgrComponentName": mscMcsMgrComponentName,
       "mscMcsMgrStorageType": mscMcsMgrStorageType,
       "mscMcsMgrIndex": mscMcsMgrIndex,
       "mscMcsMgrProvTable": mscMcsMgrProvTable,
       "mscMcsMgrProvEntry": mscMcsMgrProvEntry,
       "mscMcsMgrMaxEps": mscMcsMgrMaxEps,
       "mscMcsMgrEpAlarmThreshold": mscMcsMgrEpAlarmThreshold,
       "mscMcsMgrOverrideNsapAddress": mscMcsMgrOverrideNsapAddress,
       "mscMcsMgrLogicalProcessor": mscMcsMgrLogicalProcessor,
       "mscMcsMgrSecurity": mscMcsMgrSecurity,
       "mscMcsMgrStateTable": mscMcsMgrStateTable,
       "mscMcsMgrStateEntry": mscMcsMgrStateEntry,
       "mscMcsMgrAdminState": mscMcsMgrAdminState,
       "mscMcsMgrOperationalState": mscMcsMgrOperationalState,
       "mscMcsMgrUsageState": mscMcsMgrUsageState,
       "mscMcsMgrAvailabilityStatus": mscMcsMgrAvailabilityStatus,
       "mscMcsMgrProceduralStatus": mscMcsMgrProceduralStatus,
       "mscMcsMgrControlStatus": mscMcsMgrControlStatus,
       "mscMcsMgrAlarmStatus": mscMcsMgrAlarmStatus,
       "mscMcsMgrStandbyStatus": mscMcsMgrStandbyStatus,
       "mscMcsMgrUnknownStatus": mscMcsMgrUnknownStatus,
       "mscMcsMgrOperTable": mscMcsMgrOperTable,
       "mscMcsMgrOperEntry": mscMcsMgrOperEntry,
       "mscMcsMgrCurrentLp": mscMcsMgrCurrentLp,
       "mscMcsMgrCurrentEps": mscMcsMgrCurrentEps,
       "mscMcsMgrNsapAddress": mscMcsMgrNsapAddress,
       "mscMcsMgrCanLpsTable": mscMcsMgrCanLpsTable,
       "mscMcsMgrCanLpsEntry": mscMcsMgrCanLpsEntry,
       "mscMcsMgrCanLpsValue": mscMcsMgrCanLpsValue,
       "mcsMgrMIB": mcsMgrMIB,
       "mcsMgrGroup": mcsMgrGroup,
       "mcsMgrGroupCA": mcsMgrGroupCA,
       "mcsMgrGroupCA02": mcsMgrGroupCA02,
       "mcsMgrGroupCA02A": mcsMgrGroupCA02A,
       "mcsMgrCapabilities": mcsMgrCapabilities,
       "mcsMgrCapabilitiesCA": mcsMgrCapabilitiesCA,
       "mcsMgrCapabilitiesCA02": mcsMgrCapabilitiesCA02,
       "mcsMgrCapabilitiesCA02A": mcsMgrCapabilitiesCA02A}
)
