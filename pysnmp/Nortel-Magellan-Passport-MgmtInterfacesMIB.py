# SNMP MIB module (Nortel-Magellan-Passport-MgmtInterfacesMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-MgmtInterfacesMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:09 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
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

_Nmis_ObjectIdentity = ObjectIdentity
nmis = _Nmis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17)
)
_NmisRowStatusTable_Object = MibTable
nmisRowStatusTable = _NmisRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1)
)
if mibBuilder.loadTexts:
    nmisRowStatusTable.setStatus("mandatory")
_NmisRowStatusEntry_Object = MibTableRow
nmisRowStatusEntry = _NmisRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1, 1)
)
nmisRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
)
if mibBuilder.loadTexts:
    nmisRowStatusEntry.setStatus("mandatory")
_NmisRowStatus_Type = RowStatus
_NmisRowStatus_Object = MibTableColumn
nmisRowStatus = _NmisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1, 1, 1),
    _NmisRowStatus_Type()
)
nmisRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisRowStatus.setStatus("mandatory")
_NmisComponentName_Type = DisplayString
_NmisComponentName_Object = MibTableColumn
nmisComponentName = _NmisComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1, 1, 2),
    _NmisComponentName_Type()
)
nmisComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisComponentName.setStatus("mandatory")
_NmisStorageType_Type = StorageType
_NmisStorageType_Object = MibTableColumn
nmisStorageType = _NmisStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1, 1, 4),
    _NmisStorageType_Type()
)
nmisStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisStorageType.setStatus("mandatory")
_NmisIndex_Type = NonReplicated
_NmisIndex_Object = MibTableColumn
nmisIndex = _NmisIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 1, 1, 10),
    _NmisIndex_Type()
)
nmisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisIndex.setStatus("mandatory")
_NmisLocal_ObjectIdentity = ObjectIdentity
nmisLocal = _NmisLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2)
)
_NmisLocalRowStatusTable_Object = MibTable
nmisLocalRowStatusTable = _NmisLocalRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    nmisLocalRowStatusTable.setStatus("mandatory")
_NmisLocalRowStatusEntry_Object = MibTableRow
nmisLocalRowStatusEntry = _NmisLocalRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1, 1)
)
nmisLocalRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalIndex"),
)
if mibBuilder.loadTexts:
    nmisLocalRowStatusEntry.setStatus("mandatory")
_NmisLocalRowStatus_Type = RowStatus
_NmisLocalRowStatus_Object = MibTableColumn
nmisLocalRowStatus = _NmisLocalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1, 1, 1),
    _NmisLocalRowStatus_Type()
)
nmisLocalRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalRowStatus.setStatus("mandatory")
_NmisLocalComponentName_Type = DisplayString
_NmisLocalComponentName_Object = MibTableColumn
nmisLocalComponentName = _NmisLocalComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1, 1, 2),
    _NmisLocalComponentName_Type()
)
nmisLocalComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalComponentName.setStatus("mandatory")
_NmisLocalStorageType_Type = StorageType
_NmisLocalStorageType_Object = MibTableColumn
nmisLocalStorageType = _NmisLocalStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1, 1, 4),
    _NmisLocalStorageType_Type()
)
nmisLocalStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalStorageType.setStatus("mandatory")
_NmisLocalIndex_Type = NonReplicated
_NmisLocalIndex_Object = MibTableColumn
nmisLocalIndex = _NmisLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 1, 1, 10),
    _NmisLocalIndex_Type()
)
nmisLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisLocalIndex.setStatus("mandatory")
_NmisLocalSession_ObjectIdentity = ObjectIdentity
nmisLocalSession = _NmisLocalSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2)
)
_NmisLocalSessionRowStatusTable_Object = MibTable
nmisLocalSessionRowStatusTable = _NmisLocalSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nmisLocalSessionRowStatusTable.setStatus("mandatory")
_NmisLocalSessionRowStatusEntry_Object = MibTableRow
nmisLocalSessionRowStatusEntry = _NmisLocalSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1, 1)
)
nmisLocalSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisLocalSessionRowStatusEntry.setStatus("mandatory")
_NmisLocalSessionRowStatus_Type = RowStatus
_NmisLocalSessionRowStatus_Object = MibTableColumn
nmisLocalSessionRowStatus = _NmisLocalSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1, 1, 1),
    _NmisLocalSessionRowStatus_Type()
)
nmisLocalSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalSessionRowStatus.setStatus("mandatory")
_NmisLocalSessionComponentName_Type = DisplayString
_NmisLocalSessionComponentName_Object = MibTableColumn
nmisLocalSessionComponentName = _NmisLocalSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1, 1, 2),
    _NmisLocalSessionComponentName_Type()
)
nmisLocalSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalSessionComponentName.setStatus("mandatory")
_NmisLocalSessionStorageType_Type = StorageType
_NmisLocalSessionStorageType_Object = MibTableColumn
nmisLocalSessionStorageType = _NmisLocalSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1, 1, 4),
    _NmisLocalSessionStorageType_Type()
)
nmisLocalSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalSessionStorageType.setStatus("mandatory")


class _NmisLocalSessionIndex_Type(Integer32):
    """Custom type nmisLocalSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NmisLocalSessionIndex_Type.__name__ = "Integer32"
_NmisLocalSessionIndex_Object = MibTableColumn
nmisLocalSessionIndex = _NmisLocalSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 1, 1, 10),
    _NmisLocalSessionIndex_Type()
)
nmisLocalSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisLocalSessionIndex.setStatus("mandatory")
_NmisLocalSessionOperTable_Object = MibTable
nmisLocalSessionOperTable = _NmisLocalSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10)
)
if mibBuilder.loadTexts:
    nmisLocalSessionOperTable.setStatus("mandatory")
_NmisLocalSessionOperEntry_Object = MibTableRow
nmisLocalSessionOperEntry = _NmisLocalSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10, 1)
)
nmisLocalSessionOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisLocalSessionOperEntry.setStatus("mandatory")


class _NmisLocalSessionUserid_Type(AsciiString):
    """Custom type nmisLocalSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NmisLocalSessionUserid_Type.__name__ = "AsciiString"
_NmisLocalSessionUserid_Object = MibTableColumn
nmisLocalSessionUserid = _NmisLocalSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10, 1, 1),
    _NmisLocalSessionUserid_Type()
)
nmisLocalSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalSessionUserid.setStatus("mandatory")


class _NmisLocalSessionDataStreams_Type(OctetString):
    """Custom type nmisLocalSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NmisLocalSessionDataStreams_Type.__name__ = "OctetString"
_NmisLocalSessionDataStreams_Object = MibTableColumn
nmisLocalSessionDataStreams = _NmisLocalSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10, 1, 2),
    _NmisLocalSessionDataStreams_Type()
)
nmisLocalSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisLocalSessionDataStreams.setStatus("mandatory")
_NmisLocalSessionHostCard_Type = RowPointer
_NmisLocalSessionHostCard_Object = MibTableColumn
nmisLocalSessionHostCard = _NmisLocalSessionHostCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10, 1, 3),
    _NmisLocalSessionHostCard_Type()
)
nmisLocalSessionHostCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalSessionHostCard.setStatus("mandatory")


class _NmisLocalSessionScreenWidth_Type(Unsigned32):
    """Custom type nmisLocalSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_NmisLocalSessionScreenWidth_Type.__name__ = "Unsigned32"
_NmisLocalSessionScreenWidth_Object = MibTableColumn
nmisLocalSessionScreenWidth = _NmisLocalSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 2, 10, 1, 4),
    _NmisLocalSessionScreenWidth_Type()
)
nmisLocalSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisLocalSessionScreenWidth.setStatus("mandatory")
_NmisLocalStateTable_Object = MibTable
nmisLocalStateTable = _NmisLocalStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 10)
)
if mibBuilder.loadTexts:
    nmisLocalStateTable.setStatus("mandatory")
_NmisLocalStateEntry_Object = MibTableRow
nmisLocalStateEntry = _NmisLocalStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 10, 1)
)
nmisLocalStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalIndex"),
)
if mibBuilder.loadTexts:
    nmisLocalStateEntry.setStatus("mandatory")


class _NmisLocalAdminState_Type(Integer32):
    """Custom type nmisLocalAdminState based on Integer32"""
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


_NmisLocalAdminState_Type.__name__ = "Integer32"
_NmisLocalAdminState_Object = MibTableColumn
nmisLocalAdminState = _NmisLocalAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 10, 1, 1),
    _NmisLocalAdminState_Type()
)
nmisLocalAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalAdminState.setStatus("mandatory")


class _NmisLocalOperationalState_Type(Integer32):
    """Custom type nmisLocalOperationalState based on Integer32"""
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


_NmisLocalOperationalState_Type.__name__ = "Integer32"
_NmisLocalOperationalState_Object = MibTableColumn
nmisLocalOperationalState = _NmisLocalOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 10, 1, 2),
    _NmisLocalOperationalState_Type()
)
nmisLocalOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalOperationalState.setStatus("mandatory")


class _NmisLocalUsageState_Type(Integer32):
    """Custom type nmisLocalUsageState based on Integer32"""
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


_NmisLocalUsageState_Type.__name__ = "Integer32"
_NmisLocalUsageState_Object = MibTableColumn
nmisLocalUsageState = _NmisLocalUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 10, 1, 3),
    _NmisLocalUsageState_Type()
)
nmisLocalUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalUsageState.setStatus("mandatory")
_NmisLocalOperTable_Object = MibTable
nmisLocalOperTable = _NmisLocalOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 11)
)
if mibBuilder.loadTexts:
    nmisLocalOperTable.setStatus("mandatory")
_NmisLocalOperEntry_Object = MibTableRow
nmisLocalOperEntry = _NmisLocalOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 11, 1)
)
nmisLocalOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisLocalIndex"),
)
if mibBuilder.loadTexts:
    nmisLocalOperEntry.setStatus("mandatory")


class _NmisLocalMaxAllowedSessions_Type(Unsigned32):
    """Custom type nmisLocalMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_NmisLocalMaxAllowedSessions_Type.__name__ = "Unsigned32"
_NmisLocalMaxAllowedSessions_Object = MibTableColumn
nmisLocalMaxAllowedSessions = _NmisLocalMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 11, 1, 1),
    _NmisLocalMaxAllowedSessions_Type()
)
nmisLocalMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalMaxAllowedSessions.setStatus("mandatory")


class _NmisLocalActiveSessions_Type(Unsigned32):
    """Custom type nmisLocalActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_NmisLocalActiveSessions_Type.__name__ = "Unsigned32"
_NmisLocalActiveSessions_Object = MibTableColumn
nmisLocalActiveSessions = _NmisLocalActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 2, 11, 1, 2),
    _NmisLocalActiveSessions_Type()
)
nmisLocalActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisLocalActiveSessions.setStatus("mandatory")
_NmisTelnet_ObjectIdentity = ObjectIdentity
nmisTelnet = _NmisTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3)
)
_NmisTelnetRowStatusTable_Object = MibTable
nmisTelnetRowStatusTable = _NmisTelnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    nmisTelnetRowStatusTable.setStatus("mandatory")
_NmisTelnetRowStatusEntry_Object = MibTableRow
nmisTelnetRowStatusEntry = _NmisTelnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1, 1)
)
nmisTelnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetRowStatusEntry.setStatus("mandatory")
_NmisTelnetRowStatus_Type = RowStatus
_NmisTelnetRowStatus_Object = MibTableColumn
nmisTelnetRowStatus = _NmisTelnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1, 1, 1),
    _NmisTelnetRowStatus_Type()
)
nmisTelnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetRowStatus.setStatus("mandatory")
_NmisTelnetComponentName_Type = DisplayString
_NmisTelnetComponentName_Object = MibTableColumn
nmisTelnetComponentName = _NmisTelnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1, 1, 2),
    _NmisTelnetComponentName_Type()
)
nmisTelnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetComponentName.setStatus("mandatory")
_NmisTelnetStorageType_Type = StorageType
_NmisTelnetStorageType_Object = MibTableColumn
nmisTelnetStorageType = _NmisTelnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1, 1, 4),
    _NmisTelnetStorageType_Type()
)
nmisTelnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetStorageType.setStatus("mandatory")
_NmisTelnetIndex_Type = NonReplicated
_NmisTelnetIndex_Object = MibTableColumn
nmisTelnetIndex = _NmisTelnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 1, 1, 10),
    _NmisTelnetIndex_Type()
)
nmisTelnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisTelnetIndex.setStatus("mandatory")
_NmisTelnetSession_ObjectIdentity = ObjectIdentity
nmisTelnetSession = _NmisTelnetSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2)
)
_NmisTelnetSessionRowStatusTable_Object = MibTable
nmisTelnetSessionRowStatusTable = _NmisTelnetSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nmisTelnetSessionRowStatusTable.setStatus("mandatory")
_NmisTelnetSessionRowStatusEntry_Object = MibTableRow
nmisTelnetSessionRowStatusEntry = _NmisTelnetSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1, 1)
)
nmisTelnetSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetSessionRowStatusEntry.setStatus("mandatory")
_NmisTelnetSessionRowStatus_Type = RowStatus
_NmisTelnetSessionRowStatus_Object = MibTableColumn
nmisTelnetSessionRowStatus = _NmisTelnetSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1, 1, 1),
    _NmisTelnetSessionRowStatus_Type()
)
nmisTelnetSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionRowStatus.setStatus("mandatory")
_NmisTelnetSessionComponentName_Type = DisplayString
_NmisTelnetSessionComponentName_Object = MibTableColumn
nmisTelnetSessionComponentName = _NmisTelnetSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1, 1, 2),
    _NmisTelnetSessionComponentName_Type()
)
nmisTelnetSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionComponentName.setStatus("mandatory")
_NmisTelnetSessionStorageType_Type = StorageType
_NmisTelnetSessionStorageType_Object = MibTableColumn
nmisTelnetSessionStorageType = _NmisTelnetSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1, 1, 4),
    _NmisTelnetSessionStorageType_Type()
)
nmisTelnetSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionStorageType.setStatus("mandatory")


class _NmisTelnetSessionIndex_Type(Integer32):
    """Custom type nmisTelnetSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NmisTelnetSessionIndex_Type.__name__ = "Integer32"
_NmisTelnetSessionIndex_Object = MibTableColumn
nmisTelnetSessionIndex = _NmisTelnetSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 1, 1, 10),
    _NmisTelnetSessionIndex_Type()
)
nmisTelnetSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisTelnetSessionIndex.setStatus("mandatory")
_NmisTelnetSessionClient_ObjectIdentity = ObjectIdentity
nmisTelnetSessionClient = _NmisTelnetSessionClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2)
)
_NmisTelnetSessionClientRowStatusTable_Object = MibTable
nmisTelnetSessionClientRowStatusTable = _NmisTelnetSessionClientRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nmisTelnetSessionClientRowStatusTable.setStatus("mandatory")
_NmisTelnetSessionClientRowStatusEntry_Object = MibTableRow
nmisTelnetSessionClientRowStatusEntry = _NmisTelnetSessionClientRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1, 1)
)
nmisTelnetSessionClientRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionClientIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetSessionClientRowStatusEntry.setStatus("mandatory")
_NmisTelnetSessionClientRowStatus_Type = RowStatus
_NmisTelnetSessionClientRowStatus_Object = MibTableColumn
nmisTelnetSessionClientRowStatus = _NmisTelnetSessionClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1, 1, 1),
    _NmisTelnetSessionClientRowStatus_Type()
)
nmisTelnetSessionClientRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientRowStatus.setStatus("mandatory")
_NmisTelnetSessionClientComponentName_Type = DisplayString
_NmisTelnetSessionClientComponentName_Object = MibTableColumn
nmisTelnetSessionClientComponentName = _NmisTelnetSessionClientComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1, 1, 2),
    _NmisTelnetSessionClientComponentName_Type()
)
nmisTelnetSessionClientComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientComponentName.setStatus("mandatory")
_NmisTelnetSessionClientStorageType_Type = StorageType
_NmisTelnetSessionClientStorageType_Object = MibTableColumn
nmisTelnetSessionClientStorageType = _NmisTelnetSessionClientStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1, 1, 4),
    _NmisTelnetSessionClientStorageType_Type()
)
nmisTelnetSessionClientStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientStorageType.setStatus("mandatory")
_NmisTelnetSessionClientIndex_Type = NonReplicated
_NmisTelnetSessionClientIndex_Object = MibTableColumn
nmisTelnetSessionClientIndex = _NmisTelnetSessionClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 1, 1, 10),
    _NmisTelnetSessionClientIndex_Type()
)
nmisTelnetSessionClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientIndex.setStatus("mandatory")
_NmisTelnetSessionClientOperTable_Object = MibTable
nmisTelnetSessionClientOperTable = _NmisTelnetSessionClientOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    nmisTelnetSessionClientOperTable.setStatus("mandatory")
_NmisTelnetSessionClientOperEntry_Object = MibTableRow
nmisTelnetSessionClientOperEntry = _NmisTelnetSessionClientOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 10, 1)
)
nmisTelnetSessionClientOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionClientIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetSessionClientOperEntry.setStatus("mandatory")
_NmisTelnetSessionClientVirtualRouter_Type = RowPointer
_NmisTelnetSessionClientVirtualRouter_Object = MibTableColumn
nmisTelnetSessionClientVirtualRouter = _NmisTelnetSessionClientVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 10, 1, 1),
    _NmisTelnetSessionClientVirtualRouter_Type()
)
nmisTelnetSessionClientVirtualRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientVirtualRouter.setStatus("mandatory")
_NmisTelnetSessionClientRemoteIpAddr_Type = IpAddress
_NmisTelnetSessionClientRemoteIpAddr_Object = MibTableColumn
nmisTelnetSessionClientRemoteIpAddr = _NmisTelnetSessionClientRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 10, 1, 2),
    _NmisTelnetSessionClientRemoteIpAddr_Type()
)
nmisTelnetSessionClientRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientRemoteIpAddr.setStatus("mandatory")


class _NmisTelnetSessionClientRemoteTcpPort_Type(Unsigned32):
    """Custom type nmisTelnetSessionClientRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmisTelnetSessionClientRemoteTcpPort_Type.__name__ = "Unsigned32"
_NmisTelnetSessionClientRemoteTcpPort_Object = MibTableColumn
nmisTelnetSessionClientRemoteTcpPort = _NmisTelnetSessionClientRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 2, 10, 1, 3),
    _NmisTelnetSessionClientRemoteTcpPort_Type()
)
nmisTelnetSessionClientRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionClientRemoteTcpPort.setStatus("mandatory")
_NmisTelnetSessionOperTable_Object = MibTable
nmisTelnetSessionOperTable = _NmisTelnetSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10)
)
if mibBuilder.loadTexts:
    nmisTelnetSessionOperTable.setStatus("mandatory")
_NmisTelnetSessionOperEntry_Object = MibTableRow
nmisTelnetSessionOperEntry = _NmisTelnetSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1)
)
nmisTelnetSessionOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetSessionOperEntry.setStatus("mandatory")


class _NmisTelnetSessionUserid_Type(AsciiString):
    """Custom type nmisTelnetSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NmisTelnetSessionUserid_Type.__name__ = "AsciiString"
_NmisTelnetSessionUserid_Object = MibTableColumn
nmisTelnetSessionUserid = _NmisTelnetSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1, 1),
    _NmisTelnetSessionUserid_Type()
)
nmisTelnetSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionUserid.setStatus("mandatory")


class _NmisTelnetSessionDataStreams_Type(OctetString):
    """Custom type nmisTelnetSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NmisTelnetSessionDataStreams_Type.__name__ = "OctetString"
_NmisTelnetSessionDataStreams_Object = MibTableColumn
nmisTelnetSessionDataStreams = _NmisTelnetSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1, 2),
    _NmisTelnetSessionDataStreams_Type()
)
nmisTelnetSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisTelnetSessionDataStreams.setStatus("mandatory")
_NmisTelnetSessionRemoteIpAddr_Type = IpAddress
_NmisTelnetSessionRemoteIpAddr_Object = MibTableColumn
nmisTelnetSessionRemoteIpAddr = _NmisTelnetSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1, 3),
    _NmisTelnetSessionRemoteIpAddr_Type()
)
nmisTelnetSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionRemoteIpAddr.setStatus("mandatory")


class _NmisTelnetSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type nmisTelnetSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmisTelnetSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_NmisTelnetSessionRemoteTcpPort_Object = MibTableColumn
nmisTelnetSessionRemoteTcpPort = _NmisTelnetSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1, 4),
    _NmisTelnetSessionRemoteTcpPort_Type()
)
nmisTelnetSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetSessionRemoteTcpPort.setStatus("mandatory")


class _NmisTelnetSessionScreenWidth_Type(Unsigned32):
    """Custom type nmisTelnetSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_NmisTelnetSessionScreenWidth_Type.__name__ = "Unsigned32"
_NmisTelnetSessionScreenWidth_Object = MibTableColumn
nmisTelnetSessionScreenWidth = _NmisTelnetSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 2, 10, 1, 5),
    _NmisTelnetSessionScreenWidth_Type()
)
nmisTelnetSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisTelnetSessionScreenWidth.setStatus("mandatory")
_NmisTelnetStateTable_Object = MibTable
nmisTelnetStateTable = _NmisTelnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 10)
)
if mibBuilder.loadTexts:
    nmisTelnetStateTable.setStatus("mandatory")
_NmisTelnetStateEntry_Object = MibTableRow
nmisTelnetStateEntry = _NmisTelnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 10, 1)
)
nmisTelnetStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetStateEntry.setStatus("mandatory")


class _NmisTelnetAdminState_Type(Integer32):
    """Custom type nmisTelnetAdminState based on Integer32"""
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


_NmisTelnetAdminState_Type.__name__ = "Integer32"
_NmisTelnetAdminState_Object = MibTableColumn
nmisTelnetAdminState = _NmisTelnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 10, 1, 1),
    _NmisTelnetAdminState_Type()
)
nmisTelnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetAdminState.setStatus("mandatory")


class _NmisTelnetOperationalState_Type(Integer32):
    """Custom type nmisTelnetOperationalState based on Integer32"""
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


_NmisTelnetOperationalState_Type.__name__ = "Integer32"
_NmisTelnetOperationalState_Object = MibTableColumn
nmisTelnetOperationalState = _NmisTelnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 10, 1, 2),
    _NmisTelnetOperationalState_Type()
)
nmisTelnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetOperationalState.setStatus("mandatory")


class _NmisTelnetUsageState_Type(Integer32):
    """Custom type nmisTelnetUsageState based on Integer32"""
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


_NmisTelnetUsageState_Type.__name__ = "Integer32"
_NmisTelnetUsageState_Object = MibTableColumn
nmisTelnetUsageState = _NmisTelnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 10, 1, 3),
    _NmisTelnetUsageState_Type()
)
nmisTelnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetUsageState.setStatus("mandatory")
_NmisTelnetOperTable_Object = MibTable
nmisTelnetOperTable = _NmisTelnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 11)
)
if mibBuilder.loadTexts:
    nmisTelnetOperTable.setStatus("mandatory")
_NmisTelnetOperEntry_Object = MibTableRow
nmisTelnetOperEntry = _NmisTelnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 11, 1)
)
nmisTelnetOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisTelnetIndex"),
)
if mibBuilder.loadTexts:
    nmisTelnetOperEntry.setStatus("mandatory")


class _NmisTelnetMaxAllowedSessions_Type(Unsigned32):
    """Custom type nmisTelnetMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_NmisTelnetMaxAllowedSessions_Type.__name__ = "Unsigned32"
_NmisTelnetMaxAllowedSessions_Object = MibTableColumn
nmisTelnetMaxAllowedSessions = _NmisTelnetMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 11, 1, 1),
    _NmisTelnetMaxAllowedSessions_Type()
)
nmisTelnetMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetMaxAllowedSessions.setStatus("mandatory")


class _NmisTelnetActiveSessions_Type(Unsigned32):
    """Custom type nmisTelnetActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_NmisTelnetActiveSessions_Type.__name__ = "Unsigned32"
_NmisTelnetActiveSessions_Object = MibTableColumn
nmisTelnetActiveSessions = _NmisTelnetActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 3, 11, 1, 2),
    _NmisTelnetActiveSessions_Type()
)
nmisTelnetActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisTelnetActiveSessions.setStatus("mandatory")
_NmisFmip_ObjectIdentity = ObjectIdentity
nmisFmip = _NmisFmip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4)
)
_NmisFmipRowStatusTable_Object = MibTable
nmisFmipRowStatusTable = _NmisFmipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1)
)
if mibBuilder.loadTexts:
    nmisFmipRowStatusTable.setStatus("mandatory")
_NmisFmipRowStatusEntry_Object = MibTableRow
nmisFmipRowStatusEntry = _NmisFmipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1, 1)
)
nmisFmipRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipIndex"),
)
if mibBuilder.loadTexts:
    nmisFmipRowStatusEntry.setStatus("mandatory")
_NmisFmipRowStatus_Type = RowStatus
_NmisFmipRowStatus_Object = MibTableColumn
nmisFmipRowStatus = _NmisFmipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1, 1, 1),
    _NmisFmipRowStatus_Type()
)
nmisFmipRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipRowStatus.setStatus("mandatory")
_NmisFmipComponentName_Type = DisplayString
_NmisFmipComponentName_Object = MibTableColumn
nmisFmipComponentName = _NmisFmipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1, 1, 2),
    _NmisFmipComponentName_Type()
)
nmisFmipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipComponentName.setStatus("mandatory")
_NmisFmipStorageType_Type = StorageType
_NmisFmipStorageType_Object = MibTableColumn
nmisFmipStorageType = _NmisFmipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1, 1, 4),
    _NmisFmipStorageType_Type()
)
nmisFmipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipStorageType.setStatus("mandatory")
_NmisFmipIndex_Type = NonReplicated
_NmisFmipIndex_Object = MibTableColumn
nmisFmipIndex = _NmisFmipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 1, 1, 10),
    _NmisFmipIndex_Type()
)
nmisFmipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisFmipIndex.setStatus("mandatory")
_NmisFmipSession_ObjectIdentity = ObjectIdentity
nmisFmipSession = _NmisFmipSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2)
)
_NmisFmipSessionRowStatusTable_Object = MibTable
nmisFmipSessionRowStatusTable = _NmisFmipSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nmisFmipSessionRowStatusTable.setStatus("mandatory")
_NmisFmipSessionRowStatusEntry_Object = MibTableRow
nmisFmipSessionRowStatusEntry = _NmisFmipSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1, 1)
)
nmisFmipSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisFmipSessionRowStatusEntry.setStatus("mandatory")
_NmisFmipSessionRowStatus_Type = RowStatus
_NmisFmipSessionRowStatus_Object = MibTableColumn
nmisFmipSessionRowStatus = _NmisFmipSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1, 1, 1),
    _NmisFmipSessionRowStatus_Type()
)
nmisFmipSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionRowStatus.setStatus("mandatory")
_NmisFmipSessionComponentName_Type = DisplayString
_NmisFmipSessionComponentName_Object = MibTableColumn
nmisFmipSessionComponentName = _NmisFmipSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1, 1, 2),
    _NmisFmipSessionComponentName_Type()
)
nmisFmipSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionComponentName.setStatus("mandatory")
_NmisFmipSessionStorageType_Type = StorageType
_NmisFmipSessionStorageType_Object = MibTableColumn
nmisFmipSessionStorageType = _NmisFmipSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1, 1, 4),
    _NmisFmipSessionStorageType_Type()
)
nmisFmipSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionStorageType.setStatus("mandatory")


class _NmisFmipSessionIndex_Type(Integer32):
    """Custom type nmisFmipSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35),
    )


_NmisFmipSessionIndex_Type.__name__ = "Integer32"
_NmisFmipSessionIndex_Object = MibTableColumn
nmisFmipSessionIndex = _NmisFmipSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 1, 1, 10),
    _NmisFmipSessionIndex_Type()
)
nmisFmipSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisFmipSessionIndex.setStatus("mandatory")
_NmisFmipSessionOperTable_Object = MibTable
nmisFmipSessionOperTable = _NmisFmipSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10)
)
if mibBuilder.loadTexts:
    nmisFmipSessionOperTable.setStatus("mandatory")
_NmisFmipSessionOperEntry_Object = MibTableRow
nmisFmipSessionOperEntry = _NmisFmipSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1)
)
nmisFmipSessionOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisFmipSessionOperEntry.setStatus("mandatory")


class _NmisFmipSessionUserid_Type(AsciiString):
    """Custom type nmisFmipSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NmisFmipSessionUserid_Type.__name__ = "AsciiString"
_NmisFmipSessionUserid_Object = MibTableColumn
nmisFmipSessionUserid = _NmisFmipSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1, 1),
    _NmisFmipSessionUserid_Type()
)
nmisFmipSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionUserid.setStatus("mandatory")


class _NmisFmipSessionDataStreams_Type(OctetString):
    """Custom type nmisFmipSessionDataStreams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NmisFmipSessionDataStreams_Type.__name__ = "OctetString"
_NmisFmipSessionDataStreams_Object = MibTableColumn
nmisFmipSessionDataStreams = _NmisFmipSessionDataStreams_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1, 2),
    _NmisFmipSessionDataStreams_Type()
)
nmisFmipSessionDataStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisFmipSessionDataStreams.setStatus("mandatory")
_NmisFmipSessionRemoteIpAddr_Type = IpAddress
_NmisFmipSessionRemoteIpAddr_Object = MibTableColumn
nmisFmipSessionRemoteIpAddr = _NmisFmipSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1, 3),
    _NmisFmipSessionRemoteIpAddr_Type()
)
nmisFmipSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionRemoteIpAddr.setStatus("mandatory")


class _NmisFmipSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type nmisFmipSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmisFmipSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_NmisFmipSessionRemoteTcpPort_Object = MibTableColumn
nmisFmipSessionRemoteTcpPort = _NmisFmipSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1, 4),
    _NmisFmipSessionRemoteTcpPort_Type()
)
nmisFmipSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipSessionRemoteTcpPort.setStatus("mandatory")


class _NmisFmipSessionScreenWidth_Type(Unsigned32):
    """Custom type nmisFmipSessionScreenWidth based on Unsigned32"""
    defaultValue = 79

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(79, 2000),
    )


_NmisFmipSessionScreenWidth_Type.__name__ = "Unsigned32"
_NmisFmipSessionScreenWidth_Object = MibTableColumn
nmisFmipSessionScreenWidth = _NmisFmipSessionScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 2, 10, 1, 5),
    _NmisFmipSessionScreenWidth_Type()
)
nmisFmipSessionScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmisFmipSessionScreenWidth.setStatus("mandatory")
_NmisFmipStateTable_Object = MibTable
nmisFmipStateTable = _NmisFmipStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 10)
)
if mibBuilder.loadTexts:
    nmisFmipStateTable.setStatus("mandatory")
_NmisFmipStateEntry_Object = MibTableRow
nmisFmipStateEntry = _NmisFmipStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 10, 1)
)
nmisFmipStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipIndex"),
)
if mibBuilder.loadTexts:
    nmisFmipStateEntry.setStatus("mandatory")


class _NmisFmipAdminState_Type(Integer32):
    """Custom type nmisFmipAdminState based on Integer32"""
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


_NmisFmipAdminState_Type.__name__ = "Integer32"
_NmisFmipAdminState_Object = MibTableColumn
nmisFmipAdminState = _NmisFmipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 10, 1, 1),
    _NmisFmipAdminState_Type()
)
nmisFmipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipAdminState.setStatus("mandatory")


class _NmisFmipOperationalState_Type(Integer32):
    """Custom type nmisFmipOperationalState based on Integer32"""
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


_NmisFmipOperationalState_Type.__name__ = "Integer32"
_NmisFmipOperationalState_Object = MibTableColumn
nmisFmipOperationalState = _NmisFmipOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 10, 1, 2),
    _NmisFmipOperationalState_Type()
)
nmisFmipOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipOperationalState.setStatus("mandatory")


class _NmisFmipUsageState_Type(Integer32):
    """Custom type nmisFmipUsageState based on Integer32"""
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


_NmisFmipUsageState_Type.__name__ = "Integer32"
_NmisFmipUsageState_Object = MibTableColumn
nmisFmipUsageState = _NmisFmipUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 10, 1, 3),
    _NmisFmipUsageState_Type()
)
nmisFmipUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipUsageState.setStatus("mandatory")
_NmisFmipOperTable_Object = MibTable
nmisFmipOperTable = _NmisFmipOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 11)
)
if mibBuilder.loadTexts:
    nmisFmipOperTable.setStatus("mandatory")
_NmisFmipOperEntry_Object = MibTableRow
nmisFmipOperEntry = _NmisFmipOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 11, 1)
)
nmisFmipOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFmipIndex"),
)
if mibBuilder.loadTexts:
    nmisFmipOperEntry.setStatus("mandatory")


class _NmisFmipMaxAllowedSessions_Type(Unsigned32):
    """Custom type nmisFmipMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_NmisFmipMaxAllowedSessions_Type.__name__ = "Unsigned32"
_NmisFmipMaxAllowedSessions_Object = MibTableColumn
nmisFmipMaxAllowedSessions = _NmisFmipMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 11, 1, 1),
    _NmisFmipMaxAllowedSessions_Type()
)
nmisFmipMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipMaxAllowedSessions.setStatus("mandatory")


class _NmisFmipActiveSessions_Type(Unsigned32):
    """Custom type nmisFmipActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_NmisFmipActiveSessions_Type.__name__ = "Unsigned32"
_NmisFmipActiveSessions_Object = MibTableColumn
nmisFmipActiveSessions = _NmisFmipActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 4, 11, 1, 2),
    _NmisFmipActiveSessions_Type()
)
nmisFmipActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFmipActiveSessions.setStatus("mandatory")
_NmisFtp_ObjectIdentity = ObjectIdentity
nmisFtp = _NmisFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5)
)
_NmisFtpRowStatusTable_Object = MibTable
nmisFtpRowStatusTable = _NmisFtpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1)
)
if mibBuilder.loadTexts:
    nmisFtpRowStatusTable.setStatus("mandatory")
_NmisFtpRowStatusEntry_Object = MibTableRow
nmisFtpRowStatusEntry = _NmisFtpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1, 1)
)
nmisFtpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpIndex"),
)
if mibBuilder.loadTexts:
    nmisFtpRowStatusEntry.setStatus("mandatory")
_NmisFtpRowStatus_Type = RowStatus
_NmisFtpRowStatus_Object = MibTableColumn
nmisFtpRowStatus = _NmisFtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1, 1, 1),
    _NmisFtpRowStatus_Type()
)
nmisFtpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpRowStatus.setStatus("mandatory")
_NmisFtpComponentName_Type = DisplayString
_NmisFtpComponentName_Object = MibTableColumn
nmisFtpComponentName = _NmisFtpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1, 1, 2),
    _NmisFtpComponentName_Type()
)
nmisFtpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpComponentName.setStatus("mandatory")
_NmisFtpStorageType_Type = StorageType
_NmisFtpStorageType_Object = MibTableColumn
nmisFtpStorageType = _NmisFtpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1, 1, 4),
    _NmisFtpStorageType_Type()
)
nmisFtpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpStorageType.setStatus("mandatory")
_NmisFtpIndex_Type = NonReplicated
_NmisFtpIndex_Object = MibTableColumn
nmisFtpIndex = _NmisFtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 1, 1, 10),
    _NmisFtpIndex_Type()
)
nmisFtpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisFtpIndex.setStatus("mandatory")
_NmisFtpSession_ObjectIdentity = ObjectIdentity
nmisFtpSession = _NmisFtpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2)
)
_NmisFtpSessionRowStatusTable_Object = MibTable
nmisFtpSessionRowStatusTable = _NmisFtpSessionRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1)
)
if mibBuilder.loadTexts:
    nmisFtpSessionRowStatusTable.setStatus("mandatory")
_NmisFtpSessionRowStatusEntry_Object = MibTableRow
nmisFtpSessionRowStatusEntry = _NmisFtpSessionRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1, 1)
)
nmisFtpSessionRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisFtpSessionRowStatusEntry.setStatus("mandatory")
_NmisFtpSessionRowStatus_Type = RowStatus
_NmisFtpSessionRowStatus_Object = MibTableColumn
nmisFtpSessionRowStatus = _NmisFtpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1, 1, 1),
    _NmisFtpSessionRowStatus_Type()
)
nmisFtpSessionRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionRowStatus.setStatus("mandatory")
_NmisFtpSessionComponentName_Type = DisplayString
_NmisFtpSessionComponentName_Object = MibTableColumn
nmisFtpSessionComponentName = _NmisFtpSessionComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1, 1, 2),
    _NmisFtpSessionComponentName_Type()
)
nmisFtpSessionComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionComponentName.setStatus("mandatory")
_NmisFtpSessionStorageType_Type = StorageType
_NmisFtpSessionStorageType_Object = MibTableColumn
nmisFtpSessionStorageType = _NmisFtpSessionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1, 1, 4),
    _NmisFtpSessionStorageType_Type()
)
nmisFtpSessionStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionStorageType.setStatus("mandatory")


class _NmisFtpSessionIndex_Type(Integer32):
    """Custom type nmisFtpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NmisFtpSessionIndex_Type.__name__ = "Integer32"
_NmisFtpSessionIndex_Object = MibTableColumn
nmisFtpSessionIndex = _NmisFtpSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 1, 1, 10),
    _NmisFtpSessionIndex_Type()
)
nmisFtpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmisFtpSessionIndex.setStatus("mandatory")
_NmisFtpSessionOperTable_Object = MibTable
nmisFtpSessionOperTable = _NmisFtpSessionOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 10)
)
if mibBuilder.loadTexts:
    nmisFtpSessionOperTable.setStatus("mandatory")
_NmisFtpSessionOperEntry_Object = MibTableRow
nmisFtpSessionOperEntry = _NmisFtpSessionOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 10, 1)
)
nmisFtpSessionOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpSessionIndex"),
)
if mibBuilder.loadTexts:
    nmisFtpSessionOperEntry.setStatus("mandatory")


class _NmisFtpSessionUserid_Type(AsciiString):
    """Custom type nmisFtpSessionUserid based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NmisFtpSessionUserid_Type.__name__ = "AsciiString"
_NmisFtpSessionUserid_Object = MibTableColumn
nmisFtpSessionUserid = _NmisFtpSessionUserid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 10, 1, 1),
    _NmisFtpSessionUserid_Type()
)
nmisFtpSessionUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionUserid.setStatus("mandatory")
_NmisFtpSessionRemoteIpAddr_Type = IpAddress
_NmisFtpSessionRemoteIpAddr_Object = MibTableColumn
nmisFtpSessionRemoteIpAddr = _NmisFtpSessionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 10, 1, 2),
    _NmisFtpSessionRemoteIpAddr_Type()
)
nmisFtpSessionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionRemoteIpAddr.setStatus("mandatory")


class _NmisFtpSessionRemoteTcpPort_Type(Unsigned32):
    """Custom type nmisFtpSessionRemoteTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmisFtpSessionRemoteTcpPort_Type.__name__ = "Unsigned32"
_NmisFtpSessionRemoteTcpPort_Object = MibTableColumn
nmisFtpSessionRemoteTcpPort = _NmisFtpSessionRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 2, 10, 1, 3),
    _NmisFtpSessionRemoteTcpPort_Type()
)
nmisFtpSessionRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpSessionRemoteTcpPort.setStatus("mandatory")
_NmisFtpStateTable_Object = MibTable
nmisFtpStateTable = _NmisFtpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 10)
)
if mibBuilder.loadTexts:
    nmisFtpStateTable.setStatus("mandatory")
_NmisFtpStateEntry_Object = MibTableRow
nmisFtpStateEntry = _NmisFtpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 10, 1)
)
nmisFtpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpIndex"),
)
if mibBuilder.loadTexts:
    nmisFtpStateEntry.setStatus("mandatory")


class _NmisFtpAdminState_Type(Integer32):
    """Custom type nmisFtpAdminState based on Integer32"""
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


_NmisFtpAdminState_Type.__name__ = "Integer32"
_NmisFtpAdminState_Object = MibTableColumn
nmisFtpAdminState = _NmisFtpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 10, 1, 1),
    _NmisFtpAdminState_Type()
)
nmisFtpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpAdminState.setStatus("mandatory")


class _NmisFtpOperationalState_Type(Integer32):
    """Custom type nmisFtpOperationalState based on Integer32"""
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


_NmisFtpOperationalState_Type.__name__ = "Integer32"
_NmisFtpOperationalState_Object = MibTableColumn
nmisFtpOperationalState = _NmisFtpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 10, 1, 2),
    _NmisFtpOperationalState_Type()
)
nmisFtpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpOperationalState.setStatus("mandatory")


class _NmisFtpUsageState_Type(Integer32):
    """Custom type nmisFtpUsageState based on Integer32"""
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


_NmisFtpUsageState_Type.__name__ = "Integer32"
_NmisFtpUsageState_Object = MibTableColumn
nmisFtpUsageState = _NmisFtpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 10, 1, 3),
    _NmisFtpUsageState_Type()
)
nmisFtpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpUsageState.setStatus("mandatory")
_NmisFtpOperTable_Object = MibTable
nmisFtpOperTable = _NmisFtpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 11)
)
if mibBuilder.loadTexts:
    nmisFtpOperTable.setStatus("mandatory")
_NmisFtpOperEntry_Object = MibTableRow
nmisFtpOperEntry = _NmisFtpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 11, 1)
)
nmisFtpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "nmisFtpIndex"),
)
if mibBuilder.loadTexts:
    nmisFtpOperEntry.setStatus("mandatory")


class _NmisFtpMaxAllowedSessions_Type(Unsigned32):
    """Custom type nmisFtpMaxAllowedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 35),
    )


_NmisFtpMaxAllowedSessions_Type.__name__ = "Unsigned32"
_NmisFtpMaxAllowedSessions_Object = MibTableColumn
nmisFtpMaxAllowedSessions = _NmisFtpMaxAllowedSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 11, 1, 1),
    _NmisFtpMaxAllowedSessions_Type()
)
nmisFtpMaxAllowedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpMaxAllowedSessions.setStatus("mandatory")


class _NmisFtpActiveSessions_Type(Unsigned32):
    """Custom type nmisFtpActiveSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_NmisFtpActiveSessions_Type.__name__ = "Unsigned32"
_NmisFtpActiveSessions_Object = MibTableColumn
nmisFtpActiveSessions = _NmisFtpActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 17, 5, 11, 1, 2),
    _NmisFtpActiveSessions_Type()
)
nmisFtpActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmisFtpActiveSessions.setStatus("mandatory")
_Ac_ObjectIdentity = ObjectIdentity
ac = _Ac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18)
)
_AcRowStatusTable_Object = MibTable
acRowStatusTable = _AcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1)
)
if mibBuilder.loadTexts:
    acRowStatusTable.setStatus("mandatory")
_AcRowStatusEntry_Object = MibTableRow
acRowStatusEntry = _AcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1, 1)
)
acRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
)
if mibBuilder.loadTexts:
    acRowStatusEntry.setStatus("mandatory")
_AcRowStatus_Type = RowStatus
_AcRowStatus_Object = MibTableColumn
acRowStatus = _AcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1, 1, 1),
    _AcRowStatus_Type()
)
acRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acRowStatus.setStatus("mandatory")
_AcComponentName_Type = DisplayString
_AcComponentName_Object = MibTableColumn
acComponentName = _AcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1, 1, 2),
    _AcComponentName_Type()
)
acComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acComponentName.setStatus("mandatory")
_AcStorageType_Type = StorageType
_AcStorageType_Object = MibTableColumn
acStorageType = _AcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1, 1, 4),
    _AcStorageType_Type()
)
acStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acStorageType.setStatus("mandatory")
_AcIndex_Type = NonReplicated
_AcIndex_Object = MibTableColumn
acIndex = _AcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 1, 1, 10),
    _AcIndex_Type()
)
acIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acIndex.setStatus("mandatory")
_AcUserid_ObjectIdentity = ObjectIdentity
acUserid = _AcUserid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2)
)
_AcUseridRowStatusTable_Object = MibTable
acUseridRowStatusTable = _AcUseridRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    acUseridRowStatusTable.setStatus("mandatory")
_AcUseridRowStatusEntry_Object = MibTableRow
acUseridRowStatusEntry = _AcUseridRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1, 1)
)
acUseridRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acUseridIndex"),
)
if mibBuilder.loadTexts:
    acUseridRowStatusEntry.setStatus("mandatory")
_AcUseridRowStatus_Type = RowStatus
_AcUseridRowStatus_Object = MibTableColumn
acUseridRowStatus = _AcUseridRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1, 1, 1),
    _AcUseridRowStatus_Type()
)
acUseridRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridRowStatus.setStatus("mandatory")
_AcUseridComponentName_Type = DisplayString
_AcUseridComponentName_Object = MibTableColumn
acUseridComponentName = _AcUseridComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1, 1, 2),
    _AcUseridComponentName_Type()
)
acUseridComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acUseridComponentName.setStatus("mandatory")
_AcUseridStorageType_Type = StorageType
_AcUseridStorageType_Object = MibTableColumn
acUseridStorageType = _AcUseridStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1, 1, 4),
    _AcUseridStorageType_Type()
)
acUseridStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acUseridStorageType.setStatus("mandatory")


class _AcUseridIndex_Type(AsciiStringIndex):
    """Custom type acUseridIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AcUseridIndex_Type.__name__ = "AsciiStringIndex"
_AcUseridIndex_Object = MibTableColumn
acUseridIndex = _AcUseridIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 1, 1, 10),
    _AcUseridIndex_Type()
)
acUseridIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acUseridIndex.setStatus("mandatory")
_AcUseridProvTable_Object = MibTable
acUseridProvTable = _AcUseridProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10)
)
if mibBuilder.loadTexts:
    acUseridProvTable.setStatus("mandatory")
_AcUseridProvEntry_Object = MibTableRow
acUseridProvEntry = _AcUseridProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1)
)
acUseridProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acUseridIndex"),
)
if mibBuilder.loadTexts:
    acUseridProvEntry.setStatus("mandatory")


class _AcUseridPassword_Type(AsciiString):
    """Custom type acUseridPassword based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 8),
    )


_AcUseridPassword_Type.__name__ = "AsciiString"
_AcUseridPassword_Object = MibTableColumn
acUseridPassword = _AcUseridPassword_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 1),
    _AcUseridPassword_Type()
)
acUseridPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    acUseridPassword.setStatus("mandatory")


class _AcUseridCustomerIdentifier_Type(Unsigned32):
    """Custom type acUseridCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_AcUseridCustomerIdentifier_Type.__name__ = "Unsigned32"
_AcUseridCustomerIdentifier_Object = MibTableColumn
acUseridCustomerIdentifier = _AcUseridCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 2),
    _AcUseridCustomerIdentifier_Type()
)
acUseridCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridCustomerIdentifier.setStatus("mandatory")


class _AcUseridCommandScope_Type(Integer32):
    """Custom type acUseridCommandScope based on Integer32"""
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


_AcUseridCommandScope_Type.__name__ = "Integer32"
_AcUseridCommandScope_Object = MibTableColumn
acUseridCommandScope = _AcUseridCommandScope_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 3),
    _AcUseridCommandScope_Type()
)
acUseridCommandScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridCommandScope.setStatus("mandatory")


class _AcUseridCommandImpact_Type(Integer32):
    """Custom type acUseridCommandImpact based on Integer32"""
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


_AcUseridCommandImpact_Type.__name__ = "Integer32"
_AcUseridCommandImpact_Object = MibTableColumn
acUseridCommandImpact = _AcUseridCommandImpact_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 4),
    _AcUseridCommandImpact_Type()
)
acUseridCommandImpact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridCommandImpact.setStatus("mandatory")


class _AcUseridAllowedAccess_Type(OctetString):
    """Custom type acUseridAllowedAccess based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AcUseridAllowedAccess_Type.__name__ = "OctetString"
_AcUseridAllowedAccess_Object = MibTableColumn
acUseridAllowedAccess = _AcUseridAllowedAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 5),
    _AcUseridAllowedAccess_Type()
)
acUseridAllowedAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridAllowedAccess.setStatus("mandatory")


class _AcUseridLoginDirectory_Type(AsciiString):
    """Custom type acUseridLoginDirectory based on AsciiString"""
    defaultHexValue = "2f"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AcUseridLoginDirectory_Type.__name__ = "AsciiString"
_AcUseridLoginDirectory_Object = MibTableColumn
acUseridLoginDirectory = _AcUseridLoginDirectory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 6),
    _AcUseridLoginDirectory_Type()
)
acUseridLoginDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridLoginDirectory.setStatus("mandatory")


class _AcUseridAllowedOutAccess_Type(OctetString):
    """Custom type acUseridAllowedOutAccess based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AcUseridAllowedOutAccess_Type.__name__ = "OctetString"
_AcUseridAllowedOutAccess_Object = MibTableColumn
acUseridAllowedOutAccess = _AcUseridAllowedOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 2, 10, 1, 7),
    _AcUseridAllowedOutAccess_Type()
)
acUseridAllowedOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acUseridAllowedOutAccess.setStatus("mandatory")
_AcIpAccess_ObjectIdentity = ObjectIdentity
acIpAccess = _AcIpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3)
)
_AcIpAccessRowStatusTable_Object = MibTable
acIpAccessRowStatusTable = _AcIpAccessRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    acIpAccessRowStatusTable.setStatus("mandatory")
_AcIpAccessRowStatusEntry_Object = MibTableRow
acIpAccessRowStatusEntry = _AcIpAccessRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1, 1)
)
acIpAccessRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIpAccessIndex"),
)
if mibBuilder.loadTexts:
    acIpAccessRowStatusEntry.setStatus("mandatory")
_AcIpAccessRowStatus_Type = RowStatus
_AcIpAccessRowStatus_Object = MibTableColumn
acIpAccessRowStatus = _AcIpAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1, 1, 1),
    _AcIpAccessRowStatus_Type()
)
acIpAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIpAccessRowStatus.setStatus("mandatory")
_AcIpAccessComponentName_Type = DisplayString
_AcIpAccessComponentName_Object = MibTableColumn
acIpAccessComponentName = _AcIpAccessComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1, 1, 2),
    _AcIpAccessComponentName_Type()
)
acIpAccessComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIpAccessComponentName.setStatus("mandatory")
_AcIpAccessStorageType_Type = StorageType
_AcIpAccessStorageType_Object = MibTableColumn
acIpAccessStorageType = _AcIpAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1, 1, 4),
    _AcIpAccessStorageType_Type()
)
acIpAccessStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acIpAccessStorageType.setStatus("mandatory")
_AcIpAccessIndex_Type = IpAddress
_AcIpAccessIndex_Object = MibTableColumn
acIpAccessIndex = _AcIpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 1, 1, 10),
    _AcIpAccessIndex_Type()
)
acIpAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acIpAccessIndex.setStatus("mandatory")
_AcIpAccessProvTable_Object = MibTable
acIpAccessProvTable = _AcIpAccessProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 10)
)
if mibBuilder.loadTexts:
    acIpAccessProvTable.setStatus("mandatory")
_AcIpAccessProvEntry_Object = MibTableRow
acIpAccessProvEntry = _AcIpAccessProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 10, 1)
)
acIpAccessProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIpAccessIndex"),
)
if mibBuilder.loadTexts:
    acIpAccessProvEntry.setStatus("mandatory")


class _AcIpAccessIpAddressMask_Type(IpAddress):
    """Custom type acIpAccessIpAddressMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AcIpAccessIpAddressMask_Object = MibTableColumn
acIpAccessIpAddressMask = _AcIpAccessIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 3, 10, 1, 1),
    _AcIpAccessIpAddressMask_Type()
)
acIpAccessIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIpAccessIpAddressMask.setStatus("mandatory")
_AcProvTable_Object = MibTable
acProvTable = _AcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 10)
)
if mibBuilder.loadTexts:
    acProvTable.setStatus("mandatory")
_AcProvEntry_Object = MibTableRow
acProvEntry = _AcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 10, 1)
)
acProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-MgmtInterfacesMIB", "acIndex"),
)
if mibBuilder.loadTexts:
    acProvEntry.setStatus("mandatory")


class _AcPublicKeyAuth_Type(OctetString):
    """Custom type acPublicKeyAuth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AcPublicKeyAuth_Type.__name__ = "OctetString"
_AcPublicKeyAuth_Object = MibTableColumn
acPublicKeyAuth = _AcPublicKeyAuth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 18, 10, 1, 1),
    _AcPublicKeyAuth_Type()
)
acPublicKeyAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPublicKeyAuth.setStatus("mandatory")
_MgmtInterfacesMIB_ObjectIdentity = ObjectIdentity
mgmtInterfacesMIB = _MgmtInterfacesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15)
)
_MgmtInterfacesGroup_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroup = _MgmtInterfacesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 1)
)
_MgmtInterfacesGroupBE_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupBE = _MgmtInterfacesGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 1, 5)
)
_MgmtInterfacesGroupBE01_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupBE01 = _MgmtInterfacesGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 1, 5, 2)
)
_MgmtInterfacesGroupBE01A_ObjectIdentity = ObjectIdentity
mgmtInterfacesGroupBE01A = _MgmtInterfacesGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 1, 5, 2, 2)
)
_MgmtInterfacesCapabilities_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilities = _MgmtInterfacesCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 3)
)
_MgmtInterfacesCapabilitiesBE_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesBE = _MgmtInterfacesCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 3, 5)
)
_MgmtInterfacesCapabilitiesBE01_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesBE01 = _MgmtInterfacesCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 3, 5, 2)
)
_MgmtInterfacesCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
mgmtInterfacesCapabilitiesBE01A = _MgmtInterfacesCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 15, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-MgmtInterfacesMIB",
    **{"nmis": nmis,
       "nmisRowStatusTable": nmisRowStatusTable,
       "nmisRowStatusEntry": nmisRowStatusEntry,
       "nmisRowStatus": nmisRowStatus,
       "nmisComponentName": nmisComponentName,
       "nmisStorageType": nmisStorageType,
       "nmisIndex": nmisIndex,
       "nmisLocal": nmisLocal,
       "nmisLocalRowStatusTable": nmisLocalRowStatusTable,
       "nmisLocalRowStatusEntry": nmisLocalRowStatusEntry,
       "nmisLocalRowStatus": nmisLocalRowStatus,
       "nmisLocalComponentName": nmisLocalComponentName,
       "nmisLocalStorageType": nmisLocalStorageType,
       "nmisLocalIndex": nmisLocalIndex,
       "nmisLocalSession": nmisLocalSession,
       "nmisLocalSessionRowStatusTable": nmisLocalSessionRowStatusTable,
       "nmisLocalSessionRowStatusEntry": nmisLocalSessionRowStatusEntry,
       "nmisLocalSessionRowStatus": nmisLocalSessionRowStatus,
       "nmisLocalSessionComponentName": nmisLocalSessionComponentName,
       "nmisLocalSessionStorageType": nmisLocalSessionStorageType,
       "nmisLocalSessionIndex": nmisLocalSessionIndex,
       "nmisLocalSessionOperTable": nmisLocalSessionOperTable,
       "nmisLocalSessionOperEntry": nmisLocalSessionOperEntry,
       "nmisLocalSessionUserid": nmisLocalSessionUserid,
       "nmisLocalSessionDataStreams": nmisLocalSessionDataStreams,
       "nmisLocalSessionHostCard": nmisLocalSessionHostCard,
       "nmisLocalSessionScreenWidth": nmisLocalSessionScreenWidth,
       "nmisLocalStateTable": nmisLocalStateTable,
       "nmisLocalStateEntry": nmisLocalStateEntry,
       "nmisLocalAdminState": nmisLocalAdminState,
       "nmisLocalOperationalState": nmisLocalOperationalState,
       "nmisLocalUsageState": nmisLocalUsageState,
       "nmisLocalOperTable": nmisLocalOperTable,
       "nmisLocalOperEntry": nmisLocalOperEntry,
       "nmisLocalMaxAllowedSessions": nmisLocalMaxAllowedSessions,
       "nmisLocalActiveSessions": nmisLocalActiveSessions,
       "nmisTelnet": nmisTelnet,
       "nmisTelnetRowStatusTable": nmisTelnetRowStatusTable,
       "nmisTelnetRowStatusEntry": nmisTelnetRowStatusEntry,
       "nmisTelnetRowStatus": nmisTelnetRowStatus,
       "nmisTelnetComponentName": nmisTelnetComponentName,
       "nmisTelnetStorageType": nmisTelnetStorageType,
       "nmisTelnetIndex": nmisTelnetIndex,
       "nmisTelnetSession": nmisTelnetSession,
       "nmisTelnetSessionRowStatusTable": nmisTelnetSessionRowStatusTable,
       "nmisTelnetSessionRowStatusEntry": nmisTelnetSessionRowStatusEntry,
       "nmisTelnetSessionRowStatus": nmisTelnetSessionRowStatus,
       "nmisTelnetSessionComponentName": nmisTelnetSessionComponentName,
       "nmisTelnetSessionStorageType": nmisTelnetSessionStorageType,
       "nmisTelnetSessionIndex": nmisTelnetSessionIndex,
       "nmisTelnetSessionClient": nmisTelnetSessionClient,
       "nmisTelnetSessionClientRowStatusTable": nmisTelnetSessionClientRowStatusTable,
       "nmisTelnetSessionClientRowStatusEntry": nmisTelnetSessionClientRowStatusEntry,
       "nmisTelnetSessionClientRowStatus": nmisTelnetSessionClientRowStatus,
       "nmisTelnetSessionClientComponentName": nmisTelnetSessionClientComponentName,
       "nmisTelnetSessionClientStorageType": nmisTelnetSessionClientStorageType,
       "nmisTelnetSessionClientIndex": nmisTelnetSessionClientIndex,
       "nmisTelnetSessionClientOperTable": nmisTelnetSessionClientOperTable,
       "nmisTelnetSessionClientOperEntry": nmisTelnetSessionClientOperEntry,
       "nmisTelnetSessionClientVirtualRouter": nmisTelnetSessionClientVirtualRouter,
       "nmisTelnetSessionClientRemoteIpAddr": nmisTelnetSessionClientRemoteIpAddr,
       "nmisTelnetSessionClientRemoteTcpPort": nmisTelnetSessionClientRemoteTcpPort,
       "nmisTelnetSessionOperTable": nmisTelnetSessionOperTable,
       "nmisTelnetSessionOperEntry": nmisTelnetSessionOperEntry,
       "nmisTelnetSessionUserid": nmisTelnetSessionUserid,
       "nmisTelnetSessionDataStreams": nmisTelnetSessionDataStreams,
       "nmisTelnetSessionRemoteIpAddr": nmisTelnetSessionRemoteIpAddr,
       "nmisTelnetSessionRemoteTcpPort": nmisTelnetSessionRemoteTcpPort,
       "nmisTelnetSessionScreenWidth": nmisTelnetSessionScreenWidth,
       "nmisTelnetStateTable": nmisTelnetStateTable,
       "nmisTelnetStateEntry": nmisTelnetStateEntry,
       "nmisTelnetAdminState": nmisTelnetAdminState,
       "nmisTelnetOperationalState": nmisTelnetOperationalState,
       "nmisTelnetUsageState": nmisTelnetUsageState,
       "nmisTelnetOperTable": nmisTelnetOperTable,
       "nmisTelnetOperEntry": nmisTelnetOperEntry,
       "nmisTelnetMaxAllowedSessions": nmisTelnetMaxAllowedSessions,
       "nmisTelnetActiveSessions": nmisTelnetActiveSessions,
       "nmisFmip": nmisFmip,
       "nmisFmipRowStatusTable": nmisFmipRowStatusTable,
       "nmisFmipRowStatusEntry": nmisFmipRowStatusEntry,
       "nmisFmipRowStatus": nmisFmipRowStatus,
       "nmisFmipComponentName": nmisFmipComponentName,
       "nmisFmipStorageType": nmisFmipStorageType,
       "nmisFmipIndex": nmisFmipIndex,
       "nmisFmipSession": nmisFmipSession,
       "nmisFmipSessionRowStatusTable": nmisFmipSessionRowStatusTable,
       "nmisFmipSessionRowStatusEntry": nmisFmipSessionRowStatusEntry,
       "nmisFmipSessionRowStatus": nmisFmipSessionRowStatus,
       "nmisFmipSessionComponentName": nmisFmipSessionComponentName,
       "nmisFmipSessionStorageType": nmisFmipSessionStorageType,
       "nmisFmipSessionIndex": nmisFmipSessionIndex,
       "nmisFmipSessionOperTable": nmisFmipSessionOperTable,
       "nmisFmipSessionOperEntry": nmisFmipSessionOperEntry,
       "nmisFmipSessionUserid": nmisFmipSessionUserid,
       "nmisFmipSessionDataStreams": nmisFmipSessionDataStreams,
       "nmisFmipSessionRemoteIpAddr": nmisFmipSessionRemoteIpAddr,
       "nmisFmipSessionRemoteTcpPort": nmisFmipSessionRemoteTcpPort,
       "nmisFmipSessionScreenWidth": nmisFmipSessionScreenWidth,
       "nmisFmipStateTable": nmisFmipStateTable,
       "nmisFmipStateEntry": nmisFmipStateEntry,
       "nmisFmipAdminState": nmisFmipAdminState,
       "nmisFmipOperationalState": nmisFmipOperationalState,
       "nmisFmipUsageState": nmisFmipUsageState,
       "nmisFmipOperTable": nmisFmipOperTable,
       "nmisFmipOperEntry": nmisFmipOperEntry,
       "nmisFmipMaxAllowedSessions": nmisFmipMaxAllowedSessions,
       "nmisFmipActiveSessions": nmisFmipActiveSessions,
       "nmisFtp": nmisFtp,
       "nmisFtpRowStatusTable": nmisFtpRowStatusTable,
       "nmisFtpRowStatusEntry": nmisFtpRowStatusEntry,
       "nmisFtpRowStatus": nmisFtpRowStatus,
       "nmisFtpComponentName": nmisFtpComponentName,
       "nmisFtpStorageType": nmisFtpStorageType,
       "nmisFtpIndex": nmisFtpIndex,
       "nmisFtpSession": nmisFtpSession,
       "nmisFtpSessionRowStatusTable": nmisFtpSessionRowStatusTable,
       "nmisFtpSessionRowStatusEntry": nmisFtpSessionRowStatusEntry,
       "nmisFtpSessionRowStatus": nmisFtpSessionRowStatus,
       "nmisFtpSessionComponentName": nmisFtpSessionComponentName,
       "nmisFtpSessionStorageType": nmisFtpSessionStorageType,
       "nmisFtpSessionIndex": nmisFtpSessionIndex,
       "nmisFtpSessionOperTable": nmisFtpSessionOperTable,
       "nmisFtpSessionOperEntry": nmisFtpSessionOperEntry,
       "nmisFtpSessionUserid": nmisFtpSessionUserid,
       "nmisFtpSessionRemoteIpAddr": nmisFtpSessionRemoteIpAddr,
       "nmisFtpSessionRemoteTcpPort": nmisFtpSessionRemoteTcpPort,
       "nmisFtpStateTable": nmisFtpStateTable,
       "nmisFtpStateEntry": nmisFtpStateEntry,
       "nmisFtpAdminState": nmisFtpAdminState,
       "nmisFtpOperationalState": nmisFtpOperationalState,
       "nmisFtpUsageState": nmisFtpUsageState,
       "nmisFtpOperTable": nmisFtpOperTable,
       "nmisFtpOperEntry": nmisFtpOperEntry,
       "nmisFtpMaxAllowedSessions": nmisFtpMaxAllowedSessions,
       "nmisFtpActiveSessions": nmisFtpActiveSessions,
       "ac": ac,
       "acRowStatusTable": acRowStatusTable,
       "acRowStatusEntry": acRowStatusEntry,
       "acRowStatus": acRowStatus,
       "acComponentName": acComponentName,
       "acStorageType": acStorageType,
       "acIndex": acIndex,
       "acUserid": acUserid,
       "acUseridRowStatusTable": acUseridRowStatusTable,
       "acUseridRowStatusEntry": acUseridRowStatusEntry,
       "acUseridRowStatus": acUseridRowStatus,
       "acUseridComponentName": acUseridComponentName,
       "acUseridStorageType": acUseridStorageType,
       "acUseridIndex": acUseridIndex,
       "acUseridProvTable": acUseridProvTable,
       "acUseridProvEntry": acUseridProvEntry,
       "acUseridPassword": acUseridPassword,
       "acUseridCustomerIdentifier": acUseridCustomerIdentifier,
       "acUseridCommandScope": acUseridCommandScope,
       "acUseridCommandImpact": acUseridCommandImpact,
       "acUseridAllowedAccess": acUseridAllowedAccess,
       "acUseridLoginDirectory": acUseridLoginDirectory,
       "acUseridAllowedOutAccess": acUseridAllowedOutAccess,
       "acIpAccess": acIpAccess,
       "acIpAccessRowStatusTable": acIpAccessRowStatusTable,
       "acIpAccessRowStatusEntry": acIpAccessRowStatusEntry,
       "acIpAccessRowStatus": acIpAccessRowStatus,
       "acIpAccessComponentName": acIpAccessComponentName,
       "acIpAccessStorageType": acIpAccessStorageType,
       "acIpAccessIndex": acIpAccessIndex,
       "acIpAccessProvTable": acIpAccessProvTable,
       "acIpAccessProvEntry": acIpAccessProvEntry,
       "acIpAccessIpAddressMask": acIpAccessIpAddressMask,
       "acProvTable": acProvTable,
       "acProvEntry": acProvEntry,
       "acPublicKeyAuth": acPublicKeyAuth,
       "mgmtInterfacesMIB": mgmtInterfacesMIB,
       "mgmtInterfacesGroup": mgmtInterfacesGroup,
       "mgmtInterfacesGroupBE": mgmtInterfacesGroupBE,
       "mgmtInterfacesGroupBE01": mgmtInterfacesGroupBE01,
       "mgmtInterfacesGroupBE01A": mgmtInterfacesGroupBE01A,
       "mgmtInterfacesCapabilities": mgmtInterfacesCapabilities,
       "mgmtInterfacesCapabilitiesBE": mgmtInterfacesCapabilitiesBE,
       "mgmtInterfacesCapabilitiesBE01": mgmtInterfacesCapabilitiesBE01,
       "mgmtInterfacesCapabilitiesBE01A": mgmtInterfacesCapabilitiesBE01A}
)
