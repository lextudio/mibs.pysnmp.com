# SNMP MIB module (Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:48 2024
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
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
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

_MscNmis_ObjectIdentity = ObjectIdentity
mscNmis = _MscNmis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17)
)
_MscNmisRowStatusTable_Object = MibTable
mscNmisRowStatusTable = _MscNmisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    mscNmisRowStatusTable.setStatus("mandatory")
_MscNmisRowStatusEntry_Object = MibTableRow
mscNmisRowStatusEntry = _MscNmisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1, 1)
)
mscNmisRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
)
if mibBuilder.loadTexts:
    mscNmisRowStatusEntry.setStatus("mandatory")
_MscNmisRowStatus_Type = RowStatus
_MscNmisRowStatus_Object = MibTableColumn
mscNmisRowStatus = _MscNmisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1, 1, 1),
    _MscNmisRowStatus_Type()
)
mscNmisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisRowStatus.setStatus("mandatory")
_MscNmisComponentName_Type = DisplayString
_MscNmisComponentName_Object = MibTableColumn
mscNmisComponentName = _MscNmisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1, 1, 2),
    _MscNmisComponentName_Type()
)
mscNmisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisComponentName.setStatus("mandatory")
_MscNmisStorageType_Type = StorageType
_MscNmisStorageType_Object = MibTableColumn
mscNmisStorageType = _MscNmisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1, 1, 4),
    _MscNmisStorageType_Type()
)
mscNmisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisStorageType.setStatus("mandatory")
_MscNmisIndex_Type = NonReplicated
_MscNmisIndex_Object = MibTableColumn
mscNmisIndex = _MscNmisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 1, 1, 10),
    _MscNmisIndex_Type()
)
mscNmisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisIndex.setStatus("mandatory")
_MscNmisLocal_ObjectIdentity = ObjectIdentity
mscNmisLocal = _MscNmisLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2)
)
_MscNmisLocalRowStatusTable_Object = MibTable
mscNmisLocalRowStatusTable = _MscNmisLocalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisLocalRowStatusTable.setStatus("mandatory")
_MscNmisLocalRowStatusEntry_Object = MibTableRow
mscNmisLocalRowStatusEntry = _MscNmisLocalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1, 1)
)
mscNmisLocalRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalIndex"),
)
if mibBuilder.loadTexts:
    mscNmisLocalRowStatusEntry.setStatus("mandatory")
_MscNmisLocalRowStatus_Type = RowStatus
_MscNmisLocalRowStatus_Object = MibTableColumn
mscNmisLocalRowStatus = _MscNmisLocalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1, 1, 1),
    _MscNmisLocalRowStatus_Type()
)
mscNmisLocalRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalRowStatus.setStatus("mandatory")
_MscNmisLocalComponentName_Type = DisplayString
_MscNmisLocalComponentName_Object = MibTableColumn
mscNmisLocalComponentName = _MscNmisLocalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1, 1, 2),
    _MscNmisLocalComponentName_Type()
)
mscNmisLocalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalComponentName.setStatus("mandatory")
_MscNmisLocalStorageType_Type = StorageType
_MscNmisLocalStorageType_Object = MibTableColumn
mscNmisLocalStorageType = _MscNmisLocalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1, 1, 4),
    _MscNmisLocalStorageType_Type()
)
mscNmisLocalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalStorageType.setStatus("mandatory")
_MscNmisLocalIndex_Type = NonReplicated
_MscNmisLocalIndex_Object = MibTableColumn
mscNmisLocalIndex = _MscNmisLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 1, 1, 10),
    _MscNmisLocalIndex_Type()
)
mscNmisLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisLocalIndex.setStatus("mandatory")
_MscNmisLocalSession_ObjectIdentity = ObjectIdentity
mscNmisLocalSession = _MscNmisLocalSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2)
)
_MscNmisLocalSessionRowStatusTable_Object = MibTable
mscNmisLocalSessionRowStatusTable = _MscNmisLocalSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisLocalSessionRowStatusTable.setStatus("mandatory")
_MscNmisLocalSessionRowStatusEntry_Object = MibTableRow
mscNmisLocalSessionRowStatusEntry = _MscNmisLocalSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1, 1)
)
mscNmisLocalSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisLocalSessionRowStatusEntry.setStatus("mandatory")
_MscNmisLocalSessionRowStatus_Type = RowStatus
_MscNmisLocalSessionRowStatus_Object = MibTableColumn
mscNmisLocalSessionRowStatus = _MscNmisLocalSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1, 1, 1),
    _MscNmisLocalSessionRowStatus_Type()
)
mscNmisLocalSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalSessionRowStatus.setStatus("mandatory")
_MscNmisLocalSessionComponentName_Type = DisplayString
_MscNmisLocalSessionComponentName_Object = MibTableColumn
mscNmisLocalSessionComponentName = _MscNmisLocalSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1, 1, 2),
    _MscNmisLocalSessionComponentName_Type()
)
mscNmisLocalSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalSessionComponentName.setStatus("mandatory")
_MscNmisLocalSessionStorageType_Type = StorageType
_MscNmisLocalSessionStorageType_Object = MibTableColumn
mscNmisLocalSessionStorageType = _MscNmisLocalSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1, 1, 4),
    _MscNmisLocalSessionStorageType_Type()
)
mscNmisLocalSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalSessionStorageType.setStatus("mandatory")


class _MscNmisLocalSessionIndex_Type(Integer32):
    """Custom type mscNmisLocalSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MscNmisLocalSessionIndex_Type.__name__ = "Integer32"
_MscNmisLocalSessionIndex_Object = MibTableColumn
mscNmisLocalSessionIndex = _MscNmisLocalSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 1, 1, 10),
    _MscNmisLocalSessionIndex_Type()
)
mscNmisLocalSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisLocalSessionIndex.setStatus("mandatory")
_MscNmisLocalSessionOperTable_Object = MibTable
mscNmisLocalSessionOperTable = _MscNmisLocalSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisLocalSessionOperTable.setStatus("mandatory")
_MscNmisLocalSessionOperEntry_Object = MibTableRow
mscNmisLocalSessionOperEntry = _MscNmisLocalSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10, 1)
)
mscNmisLocalSessionOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisLocalSessionOperEntry.setStatus("mandatory")


class _MscNmisLocalSessionUserid_Type(AsciiString):
    """Custom type mscNmisLocalSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscNmisLocalSessionUserid_Type.__name__ = "AsciiString"
_MscNmisLocalSessionUserid_Object = MibTableColumn
mscNmisLocalSessionUserid = _MscNmisLocalSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10, 1, 1),
    _MscNmisLocalSessionUserid_Type()
)
mscNmisLocalSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalSessionUserid.setStatus("mandatory")


class _MscNmisLocalSessionDataStreams_Type(OctetString):
    """Custom type mscNmisLocalSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscNmisLocalSessionDataStreams_Type.__name__ = "OctetString"
_MscNmisLocalSessionDataStreams_Object = MibTableColumn
mscNmisLocalSessionDataStreams = _MscNmisLocalSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10, 1, 2),
    _MscNmisLocalSessionDataStreams_Type()
)
mscNmisLocalSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisLocalSessionDataStreams.setStatus("mandatory")
_MscNmisLocalSessionHostCard_Type = RowPointer
_MscNmisLocalSessionHostCard_Object = MibTableColumn
mscNmisLocalSessionHostCard = _MscNmisLocalSessionHostCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10, 1, 3),
    _MscNmisLocalSessionHostCard_Type()
)
mscNmisLocalSessionHostCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalSessionHostCard.setStatus("mandatory")


class _MscNmisLocalSessionScreenWidth_Type(Unsigned32):
    """Custom type mscNmisLocalSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_MscNmisLocalSessionScreenWidth_Type.__name__ = "Unsigned32"
_MscNmisLocalSessionScreenWidth_Object = MibTableColumn
mscNmisLocalSessionScreenWidth = _MscNmisLocalSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 2, 10, 1, 4),
    _MscNmisLocalSessionScreenWidth_Type()
)
mscNmisLocalSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisLocalSessionScreenWidth.setStatus("mandatory")
_MscNmisLocalStateTable_Object = MibTable
mscNmisLocalStateTable = _MscNmisLocalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisLocalStateTable.setStatus("mandatory")
_MscNmisLocalStateEntry_Object = MibTableRow
mscNmisLocalStateEntry = _MscNmisLocalStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 10, 1)
)
mscNmisLocalStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalIndex"),
)
if mibBuilder.loadTexts:
    mscNmisLocalStateEntry.setStatus("mandatory")


class _MscNmisLocalAdminState_Type(Integer32):
    """Custom type mscNmisLocalAdminState based on Integer32"""
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


_MscNmisLocalAdminState_Type.__name__ = "Integer32"
_MscNmisLocalAdminState_Object = MibTableColumn
mscNmisLocalAdminState = _MscNmisLocalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 10, 1, 1),
    _MscNmisLocalAdminState_Type()
)
mscNmisLocalAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalAdminState.setStatus("mandatory")


class _MscNmisLocalOperationalState_Type(Integer32):
    """Custom type mscNmisLocalOperationalState based on Integer32"""
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


_MscNmisLocalOperationalState_Type.__name__ = "Integer32"
_MscNmisLocalOperationalState_Object = MibTableColumn
mscNmisLocalOperationalState = _MscNmisLocalOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 10, 1, 2),
    _MscNmisLocalOperationalState_Type()
)
mscNmisLocalOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalOperationalState.setStatus("mandatory")


class _MscNmisLocalUsageState_Type(Integer32):
    """Custom type mscNmisLocalUsageState based on Integer32"""
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


_MscNmisLocalUsageState_Type.__name__ = "Integer32"
_MscNmisLocalUsageState_Object = MibTableColumn
mscNmisLocalUsageState = _MscNmisLocalUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 10, 1, 3),
    _MscNmisLocalUsageState_Type()
)
mscNmisLocalUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalUsageState.setStatus("mandatory")
_MscNmisLocalOperTable_Object = MibTable
mscNmisLocalOperTable = _MscNmisLocalOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 11)
)
if mibBuilder.loadTexts:
    mscNmisLocalOperTable.setStatus("mandatory")
_MscNmisLocalOperEntry_Object = MibTableRow
mscNmisLocalOperEntry = _MscNmisLocalOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 11, 1)
)
mscNmisLocalOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisLocalIndex"),
)
if mibBuilder.loadTexts:
    mscNmisLocalOperEntry.setStatus("mandatory")


class _MscNmisLocalMaxAllowedSessions_Type(Unsigned32):
    """Custom type mscNmisLocalMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_MscNmisLocalMaxAllowedSessions_Type.__name__ = "Unsigned32"
_MscNmisLocalMaxAllowedSessions_Object = MibTableColumn
mscNmisLocalMaxAllowedSessions = _MscNmisLocalMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 11, 1, 1),
    _MscNmisLocalMaxAllowedSessions_Type()
)
mscNmisLocalMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalMaxAllowedSessions.setStatus("mandatory")


class _MscNmisLocalActiveSessions_Type(Unsigned32):
    """Custom type mscNmisLocalActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_MscNmisLocalActiveSessions_Type.__name__ = "Unsigned32"
_MscNmisLocalActiveSessions_Object = MibTableColumn
mscNmisLocalActiveSessions = _MscNmisLocalActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 2, 11, 1, 2),
    _MscNmisLocalActiveSessions_Type()
)
mscNmisLocalActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisLocalActiveSessions.setStatus("mandatory")
_MscNmisTelnet_ObjectIdentity = ObjectIdentity
mscNmisTelnet = _MscNmisTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3)
)
_MscNmisTelnetRowStatusTable_Object = MibTable
mscNmisTelnetRowStatusTable = _MscNmisTelnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    mscNmisTelnetRowStatusTable.setStatus("mandatory")
_MscNmisTelnetRowStatusEntry_Object = MibTableRow
mscNmisTelnetRowStatusEntry = _MscNmisTelnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1, 1)
)
mscNmisTelnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetRowStatusEntry.setStatus("mandatory")
_MscNmisTelnetRowStatus_Type = RowStatus
_MscNmisTelnetRowStatus_Object = MibTableColumn
mscNmisTelnetRowStatus = _MscNmisTelnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1, 1, 1),
    _MscNmisTelnetRowStatus_Type()
)
mscNmisTelnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetRowStatus.setStatus("mandatory")
_MscNmisTelnetComponentName_Type = DisplayString
_MscNmisTelnetComponentName_Object = MibTableColumn
mscNmisTelnetComponentName = _MscNmisTelnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1, 1, 2),
    _MscNmisTelnetComponentName_Type()
)
mscNmisTelnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetComponentName.setStatus("mandatory")
_MscNmisTelnetStorageType_Type = StorageType
_MscNmisTelnetStorageType_Object = MibTableColumn
mscNmisTelnetStorageType = _MscNmisTelnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1, 1, 4),
    _MscNmisTelnetStorageType_Type()
)
mscNmisTelnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetStorageType.setStatus("mandatory")
_MscNmisTelnetIndex_Type = NonReplicated
_MscNmisTelnetIndex_Object = MibTableColumn
mscNmisTelnetIndex = _MscNmisTelnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 1, 1, 10),
    _MscNmisTelnetIndex_Type()
)
mscNmisTelnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisTelnetIndex.setStatus("mandatory")
_MscNmisTelnetSession_ObjectIdentity = ObjectIdentity
mscNmisTelnetSession = _MscNmisTelnetSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2)
)
_MscNmisTelnetSessionRowStatusTable_Object = MibTable
mscNmisTelnetSessionRowStatusTable = _MscNmisTelnetSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionRowStatusTable.setStatus("mandatory")
_MscNmisTelnetSessionRowStatusEntry_Object = MibTableRow
mscNmisTelnetSessionRowStatusEntry = _MscNmisTelnetSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1, 1)
)
mscNmisTelnetSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionRowStatusEntry.setStatus("mandatory")
_MscNmisTelnetSessionRowStatus_Type = RowStatus
_MscNmisTelnetSessionRowStatus_Object = MibTableColumn
mscNmisTelnetSessionRowStatus = _MscNmisTelnetSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1, 1, 1),
    _MscNmisTelnetSessionRowStatus_Type()
)
mscNmisTelnetSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionRowStatus.setStatus("mandatory")
_MscNmisTelnetSessionComponentName_Type = DisplayString
_MscNmisTelnetSessionComponentName_Object = MibTableColumn
mscNmisTelnetSessionComponentName = _MscNmisTelnetSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1, 1, 2),
    _MscNmisTelnetSessionComponentName_Type()
)
mscNmisTelnetSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionComponentName.setStatus("mandatory")
_MscNmisTelnetSessionStorageType_Type = StorageType
_MscNmisTelnetSessionStorageType_Object = MibTableColumn
mscNmisTelnetSessionStorageType = _MscNmisTelnetSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1, 1, 4),
    _MscNmisTelnetSessionStorageType_Type()
)
mscNmisTelnetSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionStorageType.setStatus("mandatory")


class _MscNmisTelnetSessionIndex_Type(Integer32):
    """Custom type mscNmisTelnetSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MscNmisTelnetSessionIndex_Type.__name__ = "Integer32"
_MscNmisTelnetSessionIndex_Object = MibTableColumn
mscNmisTelnetSessionIndex = _MscNmisTelnetSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 1, 1, 10),
    _MscNmisTelnetSessionIndex_Type()
)
mscNmisTelnetSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionIndex.setStatus("mandatory")
_MscNmisTelnetSessionClient_ObjectIdentity = ObjectIdentity
mscNmisTelnetSessionClient = _MscNmisTelnetSessionClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2)
)
_MscNmisTelnetSessionClientRowStatusTable_Object = MibTable
mscNmisTelnetSessionClientRowStatusTable = _MscNmisTelnetSessionClientRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientRowStatusTable.setStatus("mandatory")
_MscNmisTelnetSessionClientRowStatusEntry_Object = MibTableRow
mscNmisTelnetSessionClientRowStatusEntry = _MscNmisTelnetSessionClientRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1, 1)
)
mscNmisTelnetSessionClientRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionClientIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientRowStatusEntry.setStatus("mandatory")
_MscNmisTelnetSessionClientRowStatus_Type = RowStatus
_MscNmisTelnetSessionClientRowStatus_Object = MibTableColumn
mscNmisTelnetSessionClientRowStatus = _MscNmisTelnetSessionClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1, 1, 1),
    _MscNmisTelnetSessionClientRowStatus_Type()
)
mscNmisTelnetSessionClientRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientRowStatus.setStatus("mandatory")
_MscNmisTelnetSessionClientComponentName_Type = DisplayString
_MscNmisTelnetSessionClientComponentName_Object = MibTableColumn
mscNmisTelnetSessionClientComponentName = _MscNmisTelnetSessionClientComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1, 1, 2),
    _MscNmisTelnetSessionClientComponentName_Type()
)
mscNmisTelnetSessionClientComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientComponentName.setStatus("mandatory")
_MscNmisTelnetSessionClientStorageType_Type = StorageType
_MscNmisTelnetSessionClientStorageType_Object = MibTableColumn
mscNmisTelnetSessionClientStorageType = _MscNmisTelnetSessionClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1, 1, 4),
    _MscNmisTelnetSessionClientStorageType_Type()
)
mscNmisTelnetSessionClientStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientStorageType.setStatus("mandatory")
_MscNmisTelnetSessionClientIndex_Type = NonReplicated
_MscNmisTelnetSessionClientIndex_Object = MibTableColumn
mscNmisTelnetSessionClientIndex = _MscNmisTelnetSessionClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 1, 1, 10),
    _MscNmisTelnetSessionClientIndex_Type()
)
mscNmisTelnetSessionClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientIndex.setStatus("mandatory")
_MscNmisTelnetSessionClientOperTable_Object = MibTable
mscNmisTelnetSessionClientOperTable = _MscNmisTelnetSessionClientOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientOperTable.setStatus("mandatory")
_MscNmisTelnetSessionClientOperEntry_Object = MibTableRow
mscNmisTelnetSessionClientOperEntry = _MscNmisTelnetSessionClientOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 10, 1)
)
mscNmisTelnetSessionClientOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionClientIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientOperEntry.setStatus("mandatory")
_MscNmisTelnetSessionClientVirtualRouter_Type = RowPointer
_MscNmisTelnetSessionClientVirtualRouter_Object = MibTableColumn
mscNmisTelnetSessionClientVirtualRouter = _MscNmisTelnetSessionClientVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 10, 1, 1),
    _MscNmisTelnetSessionClientVirtualRouter_Type()
)
mscNmisTelnetSessionClientVirtualRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientVirtualRouter.setStatus("mandatory")
_MscNmisTelnetSessionClientRemoteIpAddr_Type = IpAddress
_MscNmisTelnetSessionClientRemoteIpAddr_Object = MibTableColumn
mscNmisTelnetSessionClientRemoteIpAddr = _MscNmisTelnetSessionClientRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 10, 1, 2),
    _MscNmisTelnetSessionClientRemoteIpAddr_Type()
)
mscNmisTelnetSessionClientRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientRemoteIpAddr.setStatus("mandatory")


class _MscNmisTelnetSessionClientRemoteTcpPort_Type(Unsigned32):
    """Custom type mscNmisTelnetSessionClientRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscNmisTelnetSessionClientRemoteTcpPort_Type.__name__ = "Unsigned32"
_MscNmisTelnetSessionClientRemoteTcpPort_Object = MibTableColumn
mscNmisTelnetSessionClientRemoteTcpPort = _MscNmisTelnetSessionClientRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 2, 10, 1, 3),
    _MscNmisTelnetSessionClientRemoteTcpPort_Type()
)
mscNmisTelnetSessionClientRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionClientRemoteTcpPort.setStatus("mandatory")
_MscNmisTelnetSessionOperTable_Object = MibTable
mscNmisTelnetSessionOperTable = _MscNmisTelnetSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionOperTable.setStatus("mandatory")
_MscNmisTelnetSessionOperEntry_Object = MibTableRow
mscNmisTelnetSessionOperEntry = _MscNmisTelnetSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1)
)
mscNmisTelnetSessionOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetSessionOperEntry.setStatus("mandatory")


class _MscNmisTelnetSessionUserid_Type(AsciiString):
    """Custom type mscNmisTelnetSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscNmisTelnetSessionUserid_Type.__name__ = "AsciiString"
_MscNmisTelnetSessionUserid_Object = MibTableColumn
mscNmisTelnetSessionUserid = _MscNmisTelnetSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1, 1),
    _MscNmisTelnetSessionUserid_Type()
)
mscNmisTelnetSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionUserid.setStatus("mandatory")


class _MscNmisTelnetSessionDataStreams_Type(OctetString):
    """Custom type mscNmisTelnetSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscNmisTelnetSessionDataStreams_Type.__name__ = "OctetString"
_MscNmisTelnetSessionDataStreams_Object = MibTableColumn
mscNmisTelnetSessionDataStreams = _MscNmisTelnetSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1, 2),
    _MscNmisTelnetSessionDataStreams_Type()
)
mscNmisTelnetSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionDataStreams.setStatus("mandatory")
_MscNmisTelnetSessionRemoteIpAddr_Type = IpAddress
_MscNmisTelnetSessionRemoteIpAddr_Object = MibTableColumn
mscNmisTelnetSessionRemoteIpAddr = _MscNmisTelnetSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1, 3),
    _MscNmisTelnetSessionRemoteIpAddr_Type()
)
mscNmisTelnetSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionRemoteIpAddr.setStatus("mandatory")


class _MscNmisTelnetSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type mscNmisTelnetSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscNmisTelnetSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_MscNmisTelnetSessionRemoteTcpPort_Object = MibTableColumn
mscNmisTelnetSessionRemoteTcpPort = _MscNmisTelnetSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1, 4),
    _MscNmisTelnetSessionRemoteTcpPort_Type()
)
mscNmisTelnetSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionRemoteTcpPort.setStatus("mandatory")


class _MscNmisTelnetSessionScreenWidth_Type(Unsigned32):
    """Custom type mscNmisTelnetSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_MscNmisTelnetSessionScreenWidth_Type.__name__ = "Unsigned32"
_MscNmisTelnetSessionScreenWidth_Object = MibTableColumn
mscNmisTelnetSessionScreenWidth = _MscNmisTelnetSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 2, 10, 1, 5),
    _MscNmisTelnetSessionScreenWidth_Type()
)
mscNmisTelnetSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisTelnetSessionScreenWidth.setStatus("mandatory")
_MscNmisTelnetStateTable_Object = MibTable
mscNmisTelnetStateTable = _MscNmisTelnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 10)
)
if mibBuilder.loadTexts:
    mscNmisTelnetStateTable.setStatus("mandatory")
_MscNmisTelnetStateEntry_Object = MibTableRow
mscNmisTelnetStateEntry = _MscNmisTelnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 10, 1)
)
mscNmisTelnetStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetStateEntry.setStatus("mandatory")


class _MscNmisTelnetAdminState_Type(Integer32):
    """Custom type mscNmisTelnetAdminState based on Integer32"""
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


_MscNmisTelnetAdminState_Type.__name__ = "Integer32"
_MscNmisTelnetAdminState_Object = MibTableColumn
mscNmisTelnetAdminState = _MscNmisTelnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 10, 1, 1),
    _MscNmisTelnetAdminState_Type()
)
mscNmisTelnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetAdminState.setStatus("mandatory")


class _MscNmisTelnetOperationalState_Type(Integer32):
    """Custom type mscNmisTelnetOperationalState based on Integer32"""
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


_MscNmisTelnetOperationalState_Type.__name__ = "Integer32"
_MscNmisTelnetOperationalState_Object = MibTableColumn
mscNmisTelnetOperationalState = _MscNmisTelnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 10, 1, 2),
    _MscNmisTelnetOperationalState_Type()
)
mscNmisTelnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetOperationalState.setStatus("mandatory")


class _MscNmisTelnetUsageState_Type(Integer32):
    """Custom type mscNmisTelnetUsageState based on Integer32"""
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


_MscNmisTelnetUsageState_Type.__name__ = "Integer32"
_MscNmisTelnetUsageState_Object = MibTableColumn
mscNmisTelnetUsageState = _MscNmisTelnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 10, 1, 3),
    _MscNmisTelnetUsageState_Type()
)
mscNmisTelnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetUsageState.setStatus("mandatory")
_MscNmisTelnetOperTable_Object = MibTable
mscNmisTelnetOperTable = _MscNmisTelnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 11)
)
if mibBuilder.loadTexts:
    mscNmisTelnetOperTable.setStatus("mandatory")
_MscNmisTelnetOperEntry_Object = MibTableRow
mscNmisTelnetOperEntry = _MscNmisTelnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 11, 1)
)
mscNmisTelnetOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    mscNmisTelnetOperEntry.setStatus("mandatory")


class _MscNmisTelnetMaxAllowedSessions_Type(Unsigned32):
    """Custom type mscNmisTelnetMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_MscNmisTelnetMaxAllowedSessions_Type.__name__ = "Unsigned32"
_MscNmisTelnetMaxAllowedSessions_Object = MibTableColumn
mscNmisTelnetMaxAllowedSessions = _MscNmisTelnetMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 11, 1, 1),
    _MscNmisTelnetMaxAllowedSessions_Type()
)
mscNmisTelnetMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetMaxAllowedSessions.setStatus("mandatory")


class _MscNmisTelnetActiveSessions_Type(Unsigned32):
    """Custom type mscNmisTelnetActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_MscNmisTelnetActiveSessions_Type.__name__ = "Unsigned32"
_MscNmisTelnetActiveSessions_Object = MibTableColumn
mscNmisTelnetActiveSessions = _MscNmisTelnetActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 3, 11, 1, 2),
    _MscNmisTelnetActiveSessions_Type()
)
mscNmisTelnetActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisTelnetActiveSessions.setStatus("mandatory")
_MscNmisFmip_ObjectIdentity = ObjectIdentity
mscNmisFmip = _MscNmisFmip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4)
)
_MscNmisFmipRowStatusTable_Object = MibTable
mscNmisFmipRowStatusTable = _MscNmisFmipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1)
)
if mibBuilder.loadTexts:
    mscNmisFmipRowStatusTable.setStatus("mandatory")
_MscNmisFmipRowStatusEntry_Object = MibTableRow
mscNmisFmipRowStatusEntry = _MscNmisFmipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1, 1)
)
mscNmisFmipRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFmipRowStatusEntry.setStatus("mandatory")
_MscNmisFmipRowStatus_Type = RowStatus
_MscNmisFmipRowStatus_Object = MibTableColumn
mscNmisFmipRowStatus = _MscNmisFmipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1, 1, 1),
    _MscNmisFmipRowStatus_Type()
)
mscNmisFmipRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipRowStatus.setStatus("mandatory")
_MscNmisFmipComponentName_Type = DisplayString
_MscNmisFmipComponentName_Object = MibTableColumn
mscNmisFmipComponentName = _MscNmisFmipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1, 1, 2),
    _MscNmisFmipComponentName_Type()
)
mscNmisFmipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipComponentName.setStatus("mandatory")
_MscNmisFmipStorageType_Type = StorageType
_MscNmisFmipStorageType_Object = MibTableColumn
mscNmisFmipStorageType = _MscNmisFmipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1, 1, 4),
    _MscNmisFmipStorageType_Type()
)
mscNmisFmipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipStorageType.setStatus("mandatory")
_MscNmisFmipIndex_Type = NonReplicated
_MscNmisFmipIndex_Object = MibTableColumn
mscNmisFmipIndex = _MscNmisFmipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 1, 1, 10),
    _MscNmisFmipIndex_Type()
)
mscNmisFmipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisFmipIndex.setStatus("mandatory")
_MscNmisFmipSession_ObjectIdentity = ObjectIdentity
mscNmisFmipSession = _MscNmisFmipSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2)
)
_MscNmisFmipSessionRowStatusTable_Object = MibTable
mscNmisFmipSessionRowStatusTable = _MscNmisFmipSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisFmipSessionRowStatusTable.setStatus("mandatory")
_MscNmisFmipSessionRowStatusEntry_Object = MibTableRow
mscNmisFmipSessionRowStatusEntry = _MscNmisFmipSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1, 1)
)
mscNmisFmipSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFmipSessionRowStatusEntry.setStatus("mandatory")
_MscNmisFmipSessionRowStatus_Type = RowStatus
_MscNmisFmipSessionRowStatus_Object = MibTableColumn
mscNmisFmipSessionRowStatus = _MscNmisFmipSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1, 1, 1),
    _MscNmisFmipSessionRowStatus_Type()
)
mscNmisFmipSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionRowStatus.setStatus("mandatory")
_MscNmisFmipSessionComponentName_Type = DisplayString
_MscNmisFmipSessionComponentName_Object = MibTableColumn
mscNmisFmipSessionComponentName = _MscNmisFmipSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1, 1, 2),
    _MscNmisFmipSessionComponentName_Type()
)
mscNmisFmipSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionComponentName.setStatus("mandatory")
_MscNmisFmipSessionStorageType_Type = StorageType
_MscNmisFmipSessionStorageType_Object = MibTableColumn
mscNmisFmipSessionStorageType = _MscNmisFmipSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1, 1, 4),
    _MscNmisFmipSessionStorageType_Type()
)
mscNmisFmipSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionStorageType.setStatus("mandatory")


class _MscNmisFmipSessionIndex_Type(Integer32):
    """Custom type mscNmisFmipSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35),
    )


_MscNmisFmipSessionIndex_Type.__name__ = "Integer32"
_MscNmisFmipSessionIndex_Object = MibTableColumn
mscNmisFmipSessionIndex = _MscNmisFmipSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 1, 1, 10),
    _MscNmisFmipSessionIndex_Type()
)
mscNmisFmipSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisFmipSessionIndex.setStatus("mandatory")
_MscNmisFmipSessionOperTable_Object = MibTable
mscNmisFmipSessionOperTable = _MscNmisFmipSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisFmipSessionOperTable.setStatus("mandatory")
_MscNmisFmipSessionOperEntry_Object = MibTableRow
mscNmisFmipSessionOperEntry = _MscNmisFmipSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1)
)
mscNmisFmipSessionOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFmipSessionOperEntry.setStatus("mandatory")


class _MscNmisFmipSessionUserid_Type(AsciiString):
    """Custom type mscNmisFmipSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscNmisFmipSessionUserid_Type.__name__ = "AsciiString"
_MscNmisFmipSessionUserid_Object = MibTableColumn
mscNmisFmipSessionUserid = _MscNmisFmipSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1, 1),
    _MscNmisFmipSessionUserid_Type()
)
mscNmisFmipSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionUserid.setStatus("mandatory")


class _MscNmisFmipSessionDataStreams_Type(OctetString):
    """Custom type mscNmisFmipSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscNmisFmipSessionDataStreams_Type.__name__ = "OctetString"
_MscNmisFmipSessionDataStreams_Object = MibTableColumn
mscNmisFmipSessionDataStreams = _MscNmisFmipSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1, 2),
    _MscNmisFmipSessionDataStreams_Type()
)
mscNmisFmipSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisFmipSessionDataStreams.setStatus("mandatory")
_MscNmisFmipSessionRemoteIpAddr_Type = IpAddress
_MscNmisFmipSessionRemoteIpAddr_Object = MibTableColumn
mscNmisFmipSessionRemoteIpAddr = _MscNmisFmipSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1, 3),
    _MscNmisFmipSessionRemoteIpAddr_Type()
)
mscNmisFmipSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionRemoteIpAddr.setStatus("mandatory")


class _MscNmisFmipSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type mscNmisFmipSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscNmisFmipSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_MscNmisFmipSessionRemoteTcpPort_Object = MibTableColumn
mscNmisFmipSessionRemoteTcpPort = _MscNmisFmipSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1, 4),
    _MscNmisFmipSessionRemoteTcpPort_Type()
)
mscNmisFmipSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipSessionRemoteTcpPort.setStatus("mandatory")


class _MscNmisFmipSessionScreenWidth_Type(Unsigned32):
    """Custom type mscNmisFmipSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_MscNmisFmipSessionScreenWidth_Type.__name__ = "Unsigned32"
_MscNmisFmipSessionScreenWidth_Object = MibTableColumn
mscNmisFmipSessionScreenWidth = _MscNmisFmipSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 2, 10, 1, 5),
    _MscNmisFmipSessionScreenWidth_Type()
)
mscNmisFmipSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscNmisFmipSessionScreenWidth.setStatus("mandatory")
_MscNmisFmipStateTable_Object = MibTable
mscNmisFmipStateTable = _MscNmisFmipStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 10)
)
if mibBuilder.loadTexts:
    mscNmisFmipStateTable.setStatus("mandatory")
_MscNmisFmipStateEntry_Object = MibTableRow
mscNmisFmipStateEntry = _MscNmisFmipStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 10, 1)
)
mscNmisFmipStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFmipStateEntry.setStatus("mandatory")


class _MscNmisFmipAdminState_Type(Integer32):
    """Custom type mscNmisFmipAdminState based on Integer32"""
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


_MscNmisFmipAdminState_Type.__name__ = "Integer32"
_MscNmisFmipAdminState_Object = MibTableColumn
mscNmisFmipAdminState = _MscNmisFmipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 10, 1, 1),
    _MscNmisFmipAdminState_Type()
)
mscNmisFmipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipAdminState.setStatus("mandatory")


class _MscNmisFmipOperationalState_Type(Integer32):
    """Custom type mscNmisFmipOperationalState based on Integer32"""
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


_MscNmisFmipOperationalState_Type.__name__ = "Integer32"
_MscNmisFmipOperationalState_Object = MibTableColumn
mscNmisFmipOperationalState = _MscNmisFmipOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 10, 1, 2),
    _MscNmisFmipOperationalState_Type()
)
mscNmisFmipOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipOperationalState.setStatus("mandatory")


class _MscNmisFmipUsageState_Type(Integer32):
    """Custom type mscNmisFmipUsageState based on Integer32"""
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


_MscNmisFmipUsageState_Type.__name__ = "Integer32"
_MscNmisFmipUsageState_Object = MibTableColumn
mscNmisFmipUsageState = _MscNmisFmipUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 10, 1, 3),
    _MscNmisFmipUsageState_Type()
)
mscNmisFmipUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipUsageState.setStatus("mandatory")
_MscNmisFmipOperTable_Object = MibTable
mscNmisFmipOperTable = _MscNmisFmipOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 11)
)
if mibBuilder.loadTexts:
    mscNmisFmipOperTable.setStatus("mandatory")
_MscNmisFmipOperEntry_Object = MibTableRow
mscNmisFmipOperEntry = _MscNmisFmipOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 11, 1)
)
mscNmisFmipOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFmipIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFmipOperEntry.setStatus("mandatory")


class _MscNmisFmipMaxAllowedSessions_Type(Unsigned32):
    """Custom type mscNmisFmipMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_MscNmisFmipMaxAllowedSessions_Type.__name__ = "Unsigned32"
_MscNmisFmipMaxAllowedSessions_Object = MibTableColumn
mscNmisFmipMaxAllowedSessions = _MscNmisFmipMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 11, 1, 1),
    _MscNmisFmipMaxAllowedSessions_Type()
)
mscNmisFmipMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipMaxAllowedSessions.setStatus("mandatory")


class _MscNmisFmipActiveSessions_Type(Unsigned32):
    """Custom type mscNmisFmipActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_MscNmisFmipActiveSessions_Type.__name__ = "Unsigned32"
_MscNmisFmipActiveSessions_Object = MibTableColumn
mscNmisFmipActiveSessions = _MscNmisFmipActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 4, 11, 1, 2),
    _MscNmisFmipActiveSessions_Type()
)
mscNmisFmipActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFmipActiveSessions.setStatus("mandatory")
_MscNmisFtp_ObjectIdentity = ObjectIdentity
mscNmisFtp = _MscNmisFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5)
)
_MscNmisFtpRowStatusTable_Object = MibTable
mscNmisFtpRowStatusTable = _MscNmisFtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1)
)
if mibBuilder.loadTexts:
    mscNmisFtpRowStatusTable.setStatus("mandatory")
_MscNmisFtpRowStatusEntry_Object = MibTableRow
mscNmisFtpRowStatusEntry = _MscNmisFtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1, 1)
)
mscNmisFtpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFtpRowStatusEntry.setStatus("mandatory")
_MscNmisFtpRowStatus_Type = RowStatus
_MscNmisFtpRowStatus_Object = MibTableColumn
mscNmisFtpRowStatus = _MscNmisFtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1, 1, 1),
    _MscNmisFtpRowStatus_Type()
)
mscNmisFtpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpRowStatus.setStatus("mandatory")
_MscNmisFtpComponentName_Type = DisplayString
_MscNmisFtpComponentName_Object = MibTableColumn
mscNmisFtpComponentName = _MscNmisFtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1, 1, 2),
    _MscNmisFtpComponentName_Type()
)
mscNmisFtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpComponentName.setStatus("mandatory")
_MscNmisFtpStorageType_Type = StorageType
_MscNmisFtpStorageType_Object = MibTableColumn
mscNmisFtpStorageType = _MscNmisFtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1, 1, 4),
    _MscNmisFtpStorageType_Type()
)
mscNmisFtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpStorageType.setStatus("mandatory")
_MscNmisFtpIndex_Type = NonReplicated
_MscNmisFtpIndex_Object = MibTableColumn
mscNmisFtpIndex = _MscNmisFtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 1, 1, 10),
    _MscNmisFtpIndex_Type()
)
mscNmisFtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisFtpIndex.setStatus("mandatory")
_MscNmisFtpSession_ObjectIdentity = ObjectIdentity
mscNmisFtpSession = _MscNmisFtpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2)
)
_MscNmisFtpSessionRowStatusTable_Object = MibTable
mscNmisFtpSessionRowStatusTable = _MscNmisFtpSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscNmisFtpSessionRowStatusTable.setStatus("mandatory")
_MscNmisFtpSessionRowStatusEntry_Object = MibTableRow
mscNmisFtpSessionRowStatusEntry = _MscNmisFtpSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1, 1)
)
mscNmisFtpSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFtpSessionRowStatusEntry.setStatus("mandatory")
_MscNmisFtpSessionRowStatus_Type = RowStatus
_MscNmisFtpSessionRowStatus_Object = MibTableColumn
mscNmisFtpSessionRowStatus = _MscNmisFtpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1, 1, 1),
    _MscNmisFtpSessionRowStatus_Type()
)
mscNmisFtpSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionRowStatus.setStatus("mandatory")
_MscNmisFtpSessionComponentName_Type = DisplayString
_MscNmisFtpSessionComponentName_Object = MibTableColumn
mscNmisFtpSessionComponentName = _MscNmisFtpSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1, 1, 2),
    _MscNmisFtpSessionComponentName_Type()
)
mscNmisFtpSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionComponentName.setStatus("mandatory")
_MscNmisFtpSessionStorageType_Type = StorageType
_MscNmisFtpSessionStorageType_Object = MibTableColumn
mscNmisFtpSessionStorageType = _MscNmisFtpSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1, 1, 4),
    _MscNmisFtpSessionStorageType_Type()
)
mscNmisFtpSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionStorageType.setStatus("mandatory")


class _MscNmisFtpSessionIndex_Type(Integer32):
    """Custom type mscNmisFtpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscNmisFtpSessionIndex_Type.__name__ = "Integer32"
_MscNmisFtpSessionIndex_Object = MibTableColumn
mscNmisFtpSessionIndex = _MscNmisFtpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 1, 1, 10),
    _MscNmisFtpSessionIndex_Type()
)
mscNmisFtpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscNmisFtpSessionIndex.setStatus("mandatory")
_MscNmisFtpSessionOperTable_Object = MibTable
mscNmisFtpSessionOperTable = _MscNmisFtpSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscNmisFtpSessionOperTable.setStatus("mandatory")
_MscNmisFtpSessionOperEntry_Object = MibTableRow
mscNmisFtpSessionOperEntry = _MscNmisFtpSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 10, 1)
)
mscNmisFtpSessionOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpSessionIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFtpSessionOperEntry.setStatus("mandatory")


class _MscNmisFtpSessionUserid_Type(AsciiString):
    """Custom type mscNmisFtpSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscNmisFtpSessionUserid_Type.__name__ = "AsciiString"
_MscNmisFtpSessionUserid_Object = MibTableColumn
mscNmisFtpSessionUserid = _MscNmisFtpSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 10, 1, 1),
    _MscNmisFtpSessionUserid_Type()
)
mscNmisFtpSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionUserid.setStatus("mandatory")
_MscNmisFtpSessionRemoteIpAddr_Type = IpAddress
_MscNmisFtpSessionRemoteIpAddr_Object = MibTableColumn
mscNmisFtpSessionRemoteIpAddr = _MscNmisFtpSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 10, 1, 2),
    _MscNmisFtpSessionRemoteIpAddr_Type()
)
mscNmisFtpSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionRemoteIpAddr.setStatus("mandatory")


class _MscNmisFtpSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type mscNmisFtpSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscNmisFtpSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_MscNmisFtpSessionRemoteTcpPort_Object = MibTableColumn
mscNmisFtpSessionRemoteTcpPort = _MscNmisFtpSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 2, 10, 1, 3),
    _MscNmisFtpSessionRemoteTcpPort_Type()
)
mscNmisFtpSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpSessionRemoteTcpPort.setStatus("mandatory")
_MscNmisFtpStateTable_Object = MibTable
mscNmisFtpStateTable = _MscNmisFtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 10)
)
if mibBuilder.loadTexts:
    mscNmisFtpStateTable.setStatus("mandatory")
_MscNmisFtpStateEntry_Object = MibTableRow
mscNmisFtpStateEntry = _MscNmisFtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 10, 1)
)
mscNmisFtpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFtpStateEntry.setStatus("mandatory")


class _MscNmisFtpAdminState_Type(Integer32):
    """Custom type mscNmisFtpAdminState based on Integer32"""
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


_MscNmisFtpAdminState_Type.__name__ = "Integer32"
_MscNmisFtpAdminState_Object = MibTableColumn
mscNmisFtpAdminState = _MscNmisFtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 10, 1, 1),
    _MscNmisFtpAdminState_Type()
)
mscNmisFtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpAdminState.setStatus("mandatory")


class _MscNmisFtpOperationalState_Type(Integer32):
    """Custom type mscNmisFtpOperationalState based on Integer32"""
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


_MscNmisFtpOperationalState_Type.__name__ = "Integer32"
_MscNmisFtpOperationalState_Object = MibTableColumn
mscNmisFtpOperationalState = _MscNmisFtpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 10, 1, 2),
    _MscNmisFtpOperationalState_Type()
)
mscNmisFtpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpOperationalState.setStatus("mandatory")


class _MscNmisFtpUsageState_Type(Integer32):
    """Custom type mscNmisFtpUsageState based on Integer32"""
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


_MscNmisFtpUsageState_Type.__name__ = "Integer32"
_MscNmisFtpUsageState_Object = MibTableColumn
mscNmisFtpUsageState = _MscNmisFtpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 10, 1, 3),
    _MscNmisFtpUsageState_Type()
)
mscNmisFtpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpUsageState.setStatus("mandatory")
_MscNmisFtpOperTable_Object = MibTable
mscNmisFtpOperTable = _MscNmisFtpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 11)
)
if mibBuilder.loadTexts:
    mscNmisFtpOperTable.setStatus("mandatory")
_MscNmisFtpOperEntry_Object = MibTableRow
mscNmisFtpOperEntry = _MscNmisFtpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 11, 1)
)
mscNmisFtpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscNmisFtpIndex"),
)
if mibBuilder.loadTexts:
    mscNmisFtpOperEntry.setStatus("mandatory")


class _MscNmisFtpMaxAllowedSessions_Type(Unsigned32):
    """Custom type mscNmisFtpMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_MscNmisFtpMaxAllowedSessions_Type.__name__ = "Unsigned32"
_MscNmisFtpMaxAllowedSessions_Object = MibTableColumn
mscNmisFtpMaxAllowedSessions = _MscNmisFtpMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 11, 1, 1),
    _MscNmisFtpMaxAllowedSessions_Type()
)
mscNmisFtpMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpMaxAllowedSessions.setStatus("mandatory")


class _MscNmisFtpActiveSessions_Type(Unsigned32):
    """Custom type mscNmisFtpActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_MscNmisFtpActiveSessions_Type.__name__ = "Unsigned32"
_MscNmisFtpActiveSessions_Object = MibTableColumn
mscNmisFtpActiveSessions = _MscNmisFtpActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 17, 5, 11, 1, 2),
    _MscNmisFtpActiveSessions_Type()
)
mscNmisFtpActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscNmisFtpActiveSessions.setStatus("mandatory")
_MscAc_ObjectIdentity = ObjectIdentity
mscAc = _MscAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18)
)
_MscAcRowStatusTable_Object = MibTable
mscAcRowStatusTable = _MscAcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    mscAcRowStatusTable.setStatus("mandatory")
_MscAcRowStatusEntry_Object = MibTableRow
mscAcRowStatusEntry = _MscAcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1, 1)
)
mscAcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
)
if mibBuilder.loadTexts:
    mscAcRowStatusEntry.setStatus("mandatory")
_MscAcRowStatus_Type = RowStatus
_MscAcRowStatus_Object = MibTableColumn
mscAcRowStatus = _MscAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1, 1, 1),
    _MscAcRowStatus_Type()
)
mscAcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcRowStatus.setStatus("mandatory")
_MscAcComponentName_Type = DisplayString
_MscAcComponentName_Object = MibTableColumn
mscAcComponentName = _MscAcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1, 1, 2),
    _MscAcComponentName_Type()
)
mscAcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcComponentName.setStatus("mandatory")
_MscAcStorageType_Type = StorageType
_MscAcStorageType_Object = MibTableColumn
mscAcStorageType = _MscAcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1, 1, 4),
    _MscAcStorageType_Type()
)
mscAcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcStorageType.setStatus("mandatory")
_MscAcIndex_Type = NonReplicated
_MscAcIndex_Object = MibTableColumn
mscAcIndex = _MscAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 1, 1, 10),
    _MscAcIndex_Type()
)
mscAcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAcIndex.setStatus("mandatory")
_MscAcUserid_ObjectIdentity = ObjectIdentity
mscAcUserid = _MscAcUserid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2)
)
_MscAcUseridRowStatusTable_Object = MibTable
mscAcUseridRowStatusTable = _MscAcUseridRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    mscAcUseridRowStatusTable.setStatus("mandatory")
_MscAcUseridRowStatusEntry_Object = MibTableRow
mscAcUseridRowStatusEntry = _MscAcUseridRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1, 1)
)
mscAcUseridRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcUseridIndex"),
)
if mibBuilder.loadTexts:
    mscAcUseridRowStatusEntry.setStatus("mandatory")
_MscAcUseridRowStatus_Type = RowStatus
_MscAcUseridRowStatus_Object = MibTableColumn
mscAcUseridRowStatus = _MscAcUseridRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1, 1, 1),
    _MscAcUseridRowStatus_Type()
)
mscAcUseridRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridRowStatus.setStatus("mandatory")
_MscAcUseridComponentName_Type = DisplayString
_MscAcUseridComponentName_Object = MibTableColumn
mscAcUseridComponentName = _MscAcUseridComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1, 1, 2),
    _MscAcUseridComponentName_Type()
)
mscAcUseridComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcUseridComponentName.setStatus("mandatory")
_MscAcUseridStorageType_Type = StorageType
_MscAcUseridStorageType_Object = MibTableColumn
mscAcUseridStorageType = _MscAcUseridStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1, 1, 4),
    _MscAcUseridStorageType_Type()
)
mscAcUseridStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcUseridStorageType.setStatus("mandatory")


class _MscAcUseridIndex_Type(AsciiStringIndex):
    """Custom type mscAcUseridIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscAcUseridIndex_Type.__name__ = "AsciiStringIndex"
_MscAcUseridIndex_Object = MibTableColumn
mscAcUseridIndex = _MscAcUseridIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 1, 1, 10),
    _MscAcUseridIndex_Type()
)
mscAcUseridIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAcUseridIndex.setStatus("mandatory")
_MscAcUseridProvTable_Object = MibTable
mscAcUseridProvTable = _MscAcUseridProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10)
)
if mibBuilder.loadTexts:
    mscAcUseridProvTable.setStatus("mandatory")
_MscAcUseridProvEntry_Object = MibTableRow
mscAcUseridProvEntry = _MscAcUseridProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1)
)
mscAcUseridProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcUseridIndex"),
)
if mibBuilder.loadTexts:
    mscAcUseridProvEntry.setStatus("mandatory")


class _MscAcUseridPassword_Type(AsciiString):
    """Custom type mscAcUseridPassword based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_MscAcUseridPassword_Type.__name__ = "AsciiString"
_MscAcUseridPassword_Object = MibTableColumn
mscAcUseridPassword = _MscAcUseridPassword_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 1),
    _MscAcUseridPassword_Type()
)
mscAcUseridPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAcUseridPassword.setStatus("mandatory")


class _MscAcUseridCustomerIdentifier_Type(Unsigned32):
    """Custom type mscAcUseridCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_MscAcUseridCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscAcUseridCustomerIdentifier_Object = MibTableColumn
mscAcUseridCustomerIdentifier = _MscAcUseridCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 2),
    _MscAcUseridCustomerIdentifier_Type()
)
mscAcUseridCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridCustomerIdentifier.setStatus("mandatory")


class _MscAcUseridCommandScope_Type(Integer32):
    """Custom type mscAcUseridCommandScope based on Integer32"""
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
        *(("application", 3),
          ("device", 2),
          ("network", 1))
    )


_MscAcUseridCommandScope_Type.__name__ = "Integer32"
_MscAcUseridCommandScope_Object = MibTableColumn
mscAcUseridCommandScope = _MscAcUseridCommandScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 3),
    _MscAcUseridCommandScope_Type()
)
mscAcUseridCommandScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridCommandScope.setStatus("mandatory")


class _MscAcUseridCommandImpact_Type(Integer32):
    """Custom type mscAcUseridCommandImpact based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 5),
          ("debug", 3),
          ("passive", 7),
          ("service", 6),
          ("systemAdministration", 4))
    )


_MscAcUseridCommandImpact_Type.__name__ = "Integer32"
_MscAcUseridCommandImpact_Object = MibTableColumn
mscAcUseridCommandImpact = _MscAcUseridCommandImpact_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 4),
    _MscAcUseridCommandImpact_Type()
)
mscAcUseridCommandImpact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridCommandImpact.setStatus("mandatory")


class _MscAcUseridAllowedAccess_Type(OctetString):
    """Custom type mscAcUseridAllowedAccess based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAcUseridAllowedAccess_Type.__name__ = "OctetString"
_MscAcUseridAllowedAccess_Object = MibTableColumn
mscAcUseridAllowedAccess = _MscAcUseridAllowedAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 5),
    _MscAcUseridAllowedAccess_Type()
)
mscAcUseridAllowedAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridAllowedAccess.setStatus("mandatory")


class _MscAcUseridLoginDirectory_Type(AsciiString):
    """Custom type mscAcUseridLoginDirectory based on AsciiString"""
    defaultHexValue = "2f"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_MscAcUseridLoginDirectory_Type.__name__ = "AsciiString"
_MscAcUseridLoginDirectory_Object = MibTableColumn
mscAcUseridLoginDirectory = _MscAcUseridLoginDirectory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 6),
    _MscAcUseridLoginDirectory_Type()
)
mscAcUseridLoginDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridLoginDirectory.setStatus("mandatory")


class _MscAcUseridAllowedOutAccess_Type(OctetString):
    """Custom type mscAcUseridAllowedOutAccess based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAcUseridAllowedOutAccess_Type.__name__ = "OctetString"
_MscAcUseridAllowedOutAccess_Object = MibTableColumn
mscAcUseridAllowedOutAccess = _MscAcUseridAllowedOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 2, 10, 1, 7),
    _MscAcUseridAllowedOutAccess_Type()
)
mscAcUseridAllowedOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcUseridAllowedOutAccess.setStatus("mandatory")
_MscAcIpAccess_ObjectIdentity = ObjectIdentity
mscAcIpAccess = _MscAcIpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3)
)
_MscAcIpAccessRowStatusTable_Object = MibTable
mscAcIpAccessRowStatusTable = _MscAcIpAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    mscAcIpAccessRowStatusTable.setStatus("mandatory")
_MscAcIpAccessRowStatusEntry_Object = MibTableRow
mscAcIpAccessRowStatusEntry = _MscAcIpAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1, 1)
)
mscAcIpAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIpAccessIndex"),
)
if mibBuilder.loadTexts:
    mscAcIpAccessRowStatusEntry.setStatus("mandatory")
_MscAcIpAccessRowStatus_Type = RowStatus
_MscAcIpAccessRowStatus_Object = MibTableColumn
mscAcIpAccessRowStatus = _MscAcIpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1, 1, 1),
    _MscAcIpAccessRowStatus_Type()
)
mscAcIpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcIpAccessRowStatus.setStatus("mandatory")
_MscAcIpAccessComponentName_Type = DisplayString
_MscAcIpAccessComponentName_Object = MibTableColumn
mscAcIpAccessComponentName = _MscAcIpAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1, 1, 2),
    _MscAcIpAccessComponentName_Type()
)
mscAcIpAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcIpAccessComponentName.setStatus("mandatory")
_MscAcIpAccessStorageType_Type = StorageType
_MscAcIpAccessStorageType_Object = MibTableColumn
mscAcIpAccessStorageType = _MscAcIpAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1, 1, 4),
    _MscAcIpAccessStorageType_Type()
)
mscAcIpAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAcIpAccessStorageType.setStatus("mandatory")
_MscAcIpAccessIndex_Type = IpAddress
_MscAcIpAccessIndex_Object = MibTableColumn
mscAcIpAccessIndex = _MscAcIpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 1, 1, 10),
    _MscAcIpAccessIndex_Type()
)
mscAcIpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAcIpAccessIndex.setStatus("mandatory")
_MscAcIpAccessProvTable_Object = MibTable
mscAcIpAccessProvTable = _MscAcIpAccessProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 10)
)
if mibBuilder.loadTexts:
    mscAcIpAccessProvTable.setStatus("mandatory")
_MscAcIpAccessProvEntry_Object = MibTableRow
mscAcIpAccessProvEntry = _MscAcIpAccessProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 10, 1)
)
mscAcIpAccessProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIpAccessIndex"),
)
if mibBuilder.loadTexts:
    mscAcIpAccessProvEntry.setStatus("mandatory")


class _MscAcIpAccessIpAddressMask_Type(IpAddress):
    """Custom type mscAcIpAccessIpAddressMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_MscAcIpAccessIpAddressMask_Object = MibTableColumn
mscAcIpAccessIpAddressMask = _MscAcIpAccessIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 3, 10, 1, 1),
    _MscAcIpAccessIpAddressMask_Type()
)
mscAcIpAccessIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcIpAccessIpAddressMask.setStatus("mandatory")
_MscAcProvTable_Object = MibTable
mscAcProvTable = _MscAcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 10)
)
if mibBuilder.loadTexts:
    mscAcProvTable.setStatus("mandatory")
_MscAcProvEntry_Object = MibTableRow
mscAcProvEntry = _MscAcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 10, 1)
)
mscAcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB", "mscAcIndex"),
)
if mibBuilder.loadTexts:
    mscAcProvEntry.setStatus("mandatory")


class _MscAcPublicKeyAuth_Type(OctetString):
    """Custom type mscAcPublicKeyAuth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscAcPublicKeyAuth_Type.__name__ = "OctetString"
_MscAcPublicKeyAuth_Object = MibTableColumn
mscAcPublicKeyAuth = _MscAcPublicKeyAuth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 18, 10, 1, 1),
    _MscAcPublicKeyAuth_Type()
)
mscAcPublicKeyAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAcPublicKeyAuth.setStatus("mandatory")
_MgmtInterfacesMIB_ObjectIdentity = ObjectIdentity
mgmtInterfacesMIB = _MgmtInterfacesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15)
)
_MgmtInterfacesGroup_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroup = _MgmtInterfacesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 1)
)
_MgmtInterfacesGroupCA_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupCA = _MgmtInterfacesGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 1, 1)
)
_MgmtInterfacesGroupCA02_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupCA02 = _MgmtInterfacesGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 1, 1, 3)
)
_MgmtInterfacesGroupCA02A_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupCA02A = _MgmtInterfacesGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 1, 1, 3, 2)
)
_MgmtInterfacesCapabilities_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilities = _MgmtInterfacesCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 3)
)
_MgmtInterfacesCapabilitiesCA_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesCA = _MgmtInterfacesCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 3, 1)
)
_MgmtInterfacesCapabilitiesCA02_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesCA02 = _MgmtInterfacesCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 3, 1, 3)
)
_MgmtInterfacesCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesCA02A = _MgmtInterfacesCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 15, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-MgmtInterfacesMIB",
    **{"mscNmis": mscNmis,
       "mscNmisRowStatusTable": mscNmisRowStatusTable,
       "mscNmisRowStatusEntry": mscNmisRowStatusEntry,
       "mscNmisRowStatus": mscNmisRowStatus,
       "mscNmisComponentName": mscNmisComponentName,
       "mscNmisStorageType": mscNmisStorageType,
       "mscNmisIndex": mscNmisIndex,
       "mscNmisLocal": mscNmisLocal,
       "mscNmisLocalRowStatusTable": mscNmisLocalRowStatusTable,
       "mscNmisLocalRowStatusEntry": mscNmisLocalRowStatusEntry,
       "mscNmisLocalRowStatus": mscNmisLocalRowStatus,
       "mscNmisLocalComponentName": mscNmisLocalComponentName,
       "mscNmisLocalStorageType": mscNmisLocalStorageType,
       "mscNmisLocalIndex": mscNmisLocalIndex,
       "mscNmisLocalSession": mscNmisLocalSession,
       "mscNmisLocalSessionRowStatusTable": mscNmisLocalSessionRowStatusTable,
       "mscNmisLocalSessionRowStatusEntry": mscNmisLocalSessionRowStatusEntry,
       "mscNmisLocalSessionRowStatus": mscNmisLocalSessionRowStatus,
       "mscNmisLocalSessionComponentName": mscNmisLocalSessionComponentName,
       "mscNmisLocalSessionStorageType": mscNmisLocalSessionStorageType,
       "mscNmisLocalSessionIndex": mscNmisLocalSessionIndex,
       "mscNmisLocalSessionOperTable": mscNmisLocalSessionOperTable,
       "mscNmisLocalSessionOperEntry": mscNmisLocalSessionOperEntry,
       "mscNmisLocalSessionUserid": mscNmisLocalSessionUserid,
       "mscNmisLocalSessionDataStreams": mscNmisLocalSessionDataStreams,
       "mscNmisLocalSessionHostCard": mscNmisLocalSessionHostCard,
       "mscNmisLocalSessionScreenWidth": mscNmisLocalSessionScreenWidth,
       "mscNmisLocalStateTable": mscNmisLocalStateTable,
       "mscNmisLocalStateEntry": mscNmisLocalStateEntry,
       "mscNmisLocalAdminState": mscNmisLocalAdminState,
       "mscNmisLocalOperationalState": mscNmisLocalOperationalState,
       "mscNmisLocalUsageState": mscNmisLocalUsageState,
       "mscNmisLocalOperTable": mscNmisLocalOperTable,
       "mscNmisLocalOperEntry": mscNmisLocalOperEntry,
       "mscNmisLocalMaxAllowedSessions": mscNmisLocalMaxAllowedSessions,
       "mscNmisLocalActiveSessions": mscNmisLocalActiveSessions,
       "mscNmisTelnet": mscNmisTelnet,
       "mscNmisTelnetRowStatusTable": mscNmisTelnetRowStatusTable,
       "mscNmisTelnetRowStatusEntry": mscNmisTelnetRowStatusEntry,
       "mscNmisTelnetRowStatus": mscNmisTelnetRowStatus,
       "mscNmisTelnetComponentName": mscNmisTelnetComponentName,
       "mscNmisTelnetStorageType": mscNmisTelnetStorageType,
       "mscNmisTelnetIndex": mscNmisTelnetIndex,
       "mscNmisTelnetSession": mscNmisTelnetSession,
       "mscNmisTelnetSessionRowStatusTable": mscNmisTelnetSessionRowStatusTable,
       "mscNmisTelnetSessionRowStatusEntry": mscNmisTelnetSessionRowStatusEntry,
       "mscNmisTelnetSessionRowStatus": mscNmisTelnetSessionRowStatus,
       "mscNmisTelnetSessionComponentName": mscNmisTelnetSessionComponentName,
       "mscNmisTelnetSessionStorageType": mscNmisTelnetSessionStorageType,
       "mscNmisTelnetSessionIndex": mscNmisTelnetSessionIndex,
       "mscNmisTelnetSessionClient": mscNmisTelnetSessionClient,
       "mscNmisTelnetSessionClientRowStatusTable": mscNmisTelnetSessionClientRowStatusTable,
       "mscNmisTelnetSessionClientRowStatusEntry": mscNmisTelnetSessionClientRowStatusEntry,
       "mscNmisTelnetSessionClientRowStatus": mscNmisTelnetSessionClientRowStatus,
       "mscNmisTelnetSessionClientComponentName": mscNmisTelnetSessionClientComponentName,
       "mscNmisTelnetSessionClientStorageType": mscNmisTelnetSessionClientStorageType,
       "mscNmisTelnetSessionClientIndex": mscNmisTelnetSessionClientIndex,
       "mscNmisTelnetSessionClientOperTable": mscNmisTelnetSessionClientOperTable,
       "mscNmisTelnetSessionClientOperEntry": mscNmisTelnetSessionClientOperEntry,
       "mscNmisTelnetSessionClientVirtualRouter": mscNmisTelnetSessionClientVirtualRouter,
       "mscNmisTelnetSessionClientRemoteIpAddr": mscNmisTelnetSessionClientRemoteIpAddr,
       "mscNmisTelnetSessionClientRemoteTcpPort": mscNmisTelnetSessionClientRemoteTcpPort,
       "mscNmisTelnetSessionOperTable": mscNmisTelnetSessionOperTable,
       "mscNmisTelnetSessionOperEntry": mscNmisTelnetSessionOperEntry,
       "mscNmisTelnetSessionUserid": mscNmisTelnetSessionUserid,
       "mscNmisTelnetSessionDataStreams": mscNmisTelnetSessionDataStreams,
       "mscNmisTelnetSessionRemoteIpAddr": mscNmisTelnetSessionRemoteIpAddr,
       "mscNmisTelnetSessionRemoteTcpPort": mscNmisTelnetSessionRemoteTcpPort,
       "mscNmisTelnetSessionScreenWidth": mscNmisTelnetSessionScreenWidth,
       "mscNmisTelnetStateTable": mscNmisTelnetStateTable,
       "mscNmisTelnetStateEntry": mscNmisTelnetStateEntry,
       "mscNmisTelnetAdminState": mscNmisTelnetAdminState,
       "mscNmisTelnetOperationalState": mscNmisTelnetOperationalState,
       "mscNmisTelnetUsageState": mscNmisTelnetUsageState,
       "mscNmisTelnetOperTable": mscNmisTelnetOperTable,
       "mscNmisTelnetOperEntry": mscNmisTelnetOperEntry,
       "mscNmisTelnetMaxAllowedSessions": mscNmisTelnetMaxAllowedSessions,
       "mscNmisTelnetActiveSessions": mscNmisTelnetActiveSessions,
       "mscNmisFmip": mscNmisFmip,
       "mscNmisFmipRowStatusTable": mscNmisFmipRowStatusTable,
       "mscNmisFmipRowStatusEntry": mscNmisFmipRowStatusEntry,
       "mscNmisFmipRowStatus": mscNmisFmipRowStatus,
       "mscNmisFmipComponentName": mscNmisFmipComponentName,
       "mscNmisFmipStorageType": mscNmisFmipStorageType,
       "mscNmisFmipIndex": mscNmisFmipIndex,
       "mscNmisFmipSession": mscNmisFmipSession,
       "mscNmisFmipSessionRowStatusTable": mscNmisFmipSessionRowStatusTable,
       "mscNmisFmipSessionRowStatusEntry": mscNmisFmipSessionRowStatusEntry,
       "mscNmisFmipSessionRowStatus": mscNmisFmipSessionRowStatus,
       "mscNmisFmipSessionComponentName": mscNmisFmipSessionComponentName,
       "mscNmisFmipSessionStorageType": mscNmisFmipSessionStorageType,
       "mscNmisFmipSessionIndex": mscNmisFmipSessionIndex,
       "mscNmisFmipSessionOperTable": mscNmisFmipSessionOperTable,
       "mscNmisFmipSessionOperEntry": mscNmisFmipSessionOperEntry,
       "mscNmisFmipSessionUserid": mscNmisFmipSessionUserid,
       "mscNmisFmipSessionDataStreams": mscNmisFmipSessionDataStreams,
       "mscNmisFmipSessionRemoteIpAddr": mscNmisFmipSessionRemoteIpAddr,
       "mscNmisFmipSessionRemoteTcpPort": mscNmisFmipSessionRemoteTcpPort,
       "mscNmisFmipSessionScreenWidth": mscNmisFmipSessionScreenWidth,
       "mscNmisFmipStateTable": mscNmisFmipStateTable,
       "mscNmisFmipStateEntry": mscNmisFmipStateEntry,
       "mscNmisFmipAdminState": mscNmisFmipAdminState,
       "mscNmisFmipOperationalState": mscNmisFmipOperationalState,
       "mscNmisFmipUsageState": mscNmisFmipUsageState,
       "mscNmisFmipOperTable": mscNmisFmipOperTable,
       "mscNmisFmipOperEntry": mscNmisFmipOperEntry,
       "mscNmisFmipMaxAllowedSessions": mscNmisFmipMaxAllowedSessions,
       "mscNmisFmipActiveSessions": mscNmisFmipActiveSessions,
       "mscNmisFtp": mscNmisFtp,
       "mscNmisFtpRowStatusTable": mscNmisFtpRowStatusTable,
       "mscNmisFtpRowStatusEntry": mscNmisFtpRowStatusEntry,
       "mscNmisFtpRowStatus": mscNmisFtpRowStatus,
       "mscNmisFtpComponentName": mscNmisFtpComponentName,
       "mscNmisFtpStorageType": mscNmisFtpStorageType,
       "mscNmisFtpIndex": mscNmisFtpIndex,
       "mscNmisFtpSession": mscNmisFtpSession,
       "mscNmisFtpSessionRowStatusTable": mscNmisFtpSessionRowStatusTable,
       "mscNmisFtpSessionRowStatusEntry": mscNmisFtpSessionRowStatusEntry,
       "mscNmisFtpSessionRowStatus": mscNmisFtpSessionRowStatus,
       "mscNmisFtpSessionComponentName": mscNmisFtpSessionComponentName,
       "mscNmisFtpSessionStorageType": mscNmisFtpSessionStorageType,
       "mscNmisFtpSessionIndex": mscNmisFtpSessionIndex,
       "mscNmisFtpSessionOperTable": mscNmisFtpSessionOperTable,
       "mscNmisFtpSessionOperEntry": mscNmisFtpSessionOperEntry,
       "mscNmisFtpSessionUserid": mscNmisFtpSessionUserid,
       "mscNmisFtpSessionRemoteIpAddr": mscNmisFtpSessionRemoteIpAddr,
       "mscNmisFtpSessionRemoteTcpPort": mscNmisFtpSessionRemoteTcpPort,
       "mscNmisFtpStateTable": mscNmisFtpStateTable,
       "mscNmisFtpStateEntry": mscNmisFtpStateEntry,
       "mscNmisFtpAdminState": mscNmisFtpAdminState,
       "mscNmisFtpOperationalState": mscNmisFtpOperationalState,
       "mscNmisFtpUsageState": mscNmisFtpUsageState,
       "mscNmisFtpOperTable": mscNmisFtpOperTable,
       "mscNmisFtpOperEntry": mscNmisFtpOperEntry,
       "mscNmisFtpMaxAllowedSessions": mscNmisFtpMaxAllowedSessions,
       "mscNmisFtpActiveSessions": mscNmisFtpActiveSessions,
       "mscAc": mscAc,
       "mscAcRowStatusTable": mscAcRowStatusTable,
       "mscAcRowStatusEntry": mscAcRowStatusEntry,
       "mscAcRowStatus": mscAcRowStatus,
       "mscAcComponentName": mscAcComponentName,
       "mscAcStorageType": mscAcStorageType,
       "mscAcIndex": mscAcIndex,
       "mscAcUserid": mscAcUserid,
       "mscAcUseridRowStatusTable": mscAcUseridRowStatusTable,
       "mscAcUseridRowStatusEntry": mscAcUseridRowStatusEntry,
       "mscAcUseridRowStatus": mscAcUseridRowStatus,
       "mscAcUseridComponentName": mscAcUseridComponentName,
       "mscAcUseridStorageType": mscAcUseridStorageType,
       "mscAcUseridIndex": mscAcUseridIndex,
       "mscAcUseridProvTable": mscAcUseridProvTable,
       "mscAcUseridProvEntry": mscAcUseridProvEntry,
       "mscAcUseridPassword": mscAcUseridPassword,
       "mscAcUseridCustomerIdentifier": mscAcUseridCustomerIdentifier,
       "mscAcUseridCommandScope": mscAcUseridCommandScope,
       "mscAcUseridCommandImpact": mscAcUseridCommandImpact,
       "mscAcUseridAllowedAccess": mscAcUseridAllowedAccess,
       "mscAcUseridLoginDirectory": mscAcUseridLoginDirectory,
       "mscAcUseridAllowedOutAccess": mscAcUseridAllowedOutAccess,
       "mscAcIpAccess": mscAcIpAccess,
       "mscAcIpAccessRowStatusTable": mscAcIpAccessRowStatusTable,
       "mscAcIpAccessRowStatusEntry": mscAcIpAccessRowStatusEntry,
       "mscAcIpAccessRowStatus": mscAcIpAccessRowStatus,
       "mscAcIpAccessComponentName": mscAcIpAccessComponentName,
       "mscAcIpAccessStorageType": mscAcIpAccessStorageType,
       "mscAcIpAccessIndex": mscAcIpAccessIndex,
       "mscAcIpAccessProvTable": mscAcIpAccessProvTable,
       "mscAcIpAccessProvEntry": mscAcIpAccessProvEntry,
       "mscAcIpAccessIpAddressMask": mscAcIpAccessIpAddressMask,
       "mscAcProvTable": mscAcProvTable,
       "mscAcProvEntry": mscAcProvEntry,
       "mscAcPublicKeyAuth": mscAcPublicKeyAuth,
       "mgmtInterfacesMIB": mgmtInterfacesMIB,
       "mgmtInterfacesGroup": mgmtInterfacesGroup,
       "mgmtInterfacesGroupCA": mgmtInterfacesGroupCA,
       "mgmtInterfacesGroupCA02": mgmtInterfacesGroupCA02,
       "mgmtInterfacesGroupCA02A": mgmtInterfacesGroupCA02A,
       "mgmtInterfacesCapabilities": mgmtInterfacesCapabilities,
       "mgmtInterfacesCapabilitiesCA": mgmtInterfacesCapabilitiesCA,
       "mgmtInterfacesCapabilitiesCA02": mgmtInterfacesCapabilitiesCA02,
       "mgmtInterfacesCapabilitiesCA02A": mgmtInterfacesCapabilitiesCA02A}
)
