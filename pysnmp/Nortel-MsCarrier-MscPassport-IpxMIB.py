# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpxMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpxMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:43 2024
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

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 PhysAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 AsciiStringIndex,
 DashedHexString,
 Hex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "Hex",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex,
 mscVrPp,
 mscVrPpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex",
    "mscVrPp",
    "mscVrPpIndex")

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

_MscVrPpIpxP_ObjectIdentity = ObjectIdentity
mscVrPpIpxP = _MscVrPpIpxP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6)
)
_MscVrPpIpxPRowStatusTable_Object = MibTable
mscVrPpIpxPRowStatusTable = _MscVrPpIpxPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRowStatusTable.setStatus("mandatory")
_MscVrPpIpxPRowStatusEntry_Object = MibTableRow
mscVrPpIpxPRowStatusEntry = _MscVrPpIpxPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1, 1)
)
mscVrPpIpxPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpxPRowStatus_Type = RowStatus
_MscVrPpIpxPRowStatus_Object = MibTableColumn
mscVrPpIpxPRowStatus = _MscVrPpIpxPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1, 1, 1),
    _MscVrPpIpxPRowStatus_Type()
)
mscVrPpIpxPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPRowStatus.setStatus("mandatory")
_MscVrPpIpxPComponentName_Type = DisplayString
_MscVrPpIpxPComponentName_Object = MibTableColumn
mscVrPpIpxPComponentName = _MscVrPpIpxPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1, 1, 2),
    _MscVrPpIpxPComponentName_Type()
)
mscVrPpIpxPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPComponentName.setStatus("mandatory")
_MscVrPpIpxPStorageType_Type = StorageType
_MscVrPpIpxPStorageType_Object = MibTableColumn
mscVrPpIpxPStorageType = _MscVrPpIpxPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1, 1, 4),
    _MscVrPpIpxPStorageType_Type()
)
mscVrPpIpxPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPStorageType.setStatus("mandatory")


class _MscVrPpIpxPIndex_Type(Integer32):
    """Custom type mscVrPpIpxPIndex based on Integer32"""
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
        *(("ethernet", 2),
          ("link", 1),
          ("novell", 3),
          ("sap", 4),
          ("snap", 5),
          ("tunnel", 7),
          ("vns", 6))
    )


_MscVrPpIpxPIndex_Type.__name__ = "Integer32"
_MscVrPpIpxPIndex_Object = MibTableColumn
mscVrPpIpxPIndex = _MscVrPpIpxPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 1, 1, 10),
    _MscVrPpIpxPIndex_Type()
)
mscVrPpIpxPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpxPIndex.setStatus("mandatory")
_MscVrPpIpxPRipP_ObjectIdentity = ObjectIdentity
mscVrPpIpxPRipP = _MscVrPpIpxPRipP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2)
)
_MscVrPpIpxPRipPRowStatusTable_Object = MibTable
mscVrPpIpxPRipPRowStatusTable = _MscVrPpIpxPRipPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPRowStatusTable.setStatus("mandatory")
_MscVrPpIpxPRipPRowStatusEntry_Object = MibTableRow
mscVrPpIpxPRipPRowStatusEntry = _MscVrPpIpxPRipPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1, 1)
)
mscVrPpIpxPRipPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPRipPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpxPRipPRowStatus_Type = RowStatus
_MscVrPpIpxPRipPRowStatus_Object = MibTableColumn
mscVrPpIpxPRipPRowStatus = _MscVrPpIpxPRipPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1, 1, 1),
    _MscVrPpIpxPRipPRowStatus_Type()
)
mscVrPpIpxPRipPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPRowStatus.setStatus("mandatory")
_MscVrPpIpxPRipPComponentName_Type = DisplayString
_MscVrPpIpxPRipPComponentName_Object = MibTableColumn
mscVrPpIpxPRipPComponentName = _MscVrPpIpxPRipPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1, 1, 2),
    _MscVrPpIpxPRipPComponentName_Type()
)
mscVrPpIpxPRipPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPComponentName.setStatus("mandatory")
_MscVrPpIpxPRipPStorageType_Type = StorageType
_MscVrPpIpxPRipPStorageType_Object = MibTableColumn
mscVrPpIpxPRipPStorageType = _MscVrPpIpxPRipPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1, 1, 4),
    _MscVrPpIpxPRipPStorageType_Type()
)
mscVrPpIpxPRipPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPStorageType.setStatus("mandatory")
_MscVrPpIpxPRipPIndex_Type = NonReplicated
_MscVrPpIpxPRipPIndex_Object = MibTableColumn
mscVrPpIpxPRipPIndex = _MscVrPpIpxPRipPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 1, 1, 10),
    _MscVrPpIpxPRipPIndex_Type()
)
mscVrPpIpxPRipPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPIndex.setStatus("mandatory")
_MscVrPpIpxPRipPStatsTable_Object = MibTable
mscVrPpIpxPRipPStatsTable = _MscVrPpIpxPRipPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPStatsTable.setStatus("mandatory")
_MscVrPpIpxPRipPStatsEntry_Object = MibTableRow
mscVrPpIpxPRipPStatsEntry = _MscVrPpIpxPRipPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1)
)
mscVrPpIpxPRipPStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPRipPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPStatsEntry.setStatus("mandatory")
_MscVrPpIpxPRipPInPackets_Type = Counter32
_MscVrPpIpxPRipPInPackets_Object = MibTableColumn
mscVrPpIpxPRipPInPackets = _MscVrPpIpxPRipPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 1),
    _MscVrPpIpxPRipPInPackets_Type()
)
mscVrPpIpxPRipPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPInPackets.setStatus("mandatory")
_MscVrPpIpxPRipPInRequests_Type = Counter32
_MscVrPpIpxPRipPInRequests_Object = MibTableColumn
mscVrPpIpxPRipPInRequests = _MscVrPpIpxPRipPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 2),
    _MscVrPpIpxPRipPInRequests_Type()
)
mscVrPpIpxPRipPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPInRequests.setStatus("mandatory")
_MscVrPpIpxPRipPInResponses_Type = Counter32
_MscVrPpIpxPRipPInResponses_Object = MibTableColumn
mscVrPpIpxPRipPInResponses = _MscVrPpIpxPRipPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 3),
    _MscVrPpIpxPRipPInResponses_Type()
)
mscVrPpIpxPRipPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPInResponses.setStatus("mandatory")
_MscVrPpIpxPRipPOutPackets_Type = Counter32
_MscVrPpIpxPRipPOutPackets_Object = MibTableColumn
mscVrPpIpxPRipPOutPackets = _MscVrPpIpxPRipPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 4),
    _MscVrPpIpxPRipPOutPackets_Type()
)
mscVrPpIpxPRipPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPOutPackets.setStatus("mandatory")
_MscVrPpIpxPRipPOutRequests_Type = Counter32
_MscVrPpIpxPRipPOutRequests_Object = MibTableColumn
mscVrPpIpxPRipPOutRequests = _MscVrPpIpxPRipPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 5),
    _MscVrPpIpxPRipPOutRequests_Type()
)
mscVrPpIpxPRipPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPOutRequests.setStatus("mandatory")
_MscVrPpIpxPRipPOutResponses_Type = Counter32
_MscVrPpIpxPRipPOutResponses_Object = MibTableColumn
mscVrPpIpxPRipPOutResponses = _MscVrPpIpxPRipPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 6),
    _MscVrPpIpxPRipPOutResponses_Type()
)
mscVrPpIpxPRipPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPOutResponses.setStatus("mandatory")
_MscVrPpIpxPRipPIncorrectPackets_Type = Counter32
_MscVrPpIpxPRipPIncorrectPackets_Object = MibTableColumn
mscVrPpIpxPRipPIncorrectPackets = _MscVrPpIpxPRipPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 2, 10, 1, 7),
    _MscVrPpIpxPRipPIncorrectPackets_Type()
)
mscVrPpIpxPRipPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPRipPIncorrectPackets.setStatus("mandatory")
_MscVrPpIpxPSapP_ObjectIdentity = ObjectIdentity
mscVrPpIpxPSapP = _MscVrPpIpxPSapP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3)
)
_MscVrPpIpxPSapPRowStatusTable_Object = MibTable
mscVrPpIpxPSapPRowStatusTable = _MscVrPpIpxPSapPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPRowStatusTable.setStatus("mandatory")
_MscVrPpIpxPSapPRowStatusEntry_Object = MibTableRow
mscVrPpIpxPSapPRowStatusEntry = _MscVrPpIpxPSapPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1, 1)
)
mscVrPpIpxPSapPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPSapPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpxPSapPRowStatus_Type = RowStatus
_MscVrPpIpxPSapPRowStatus_Object = MibTableColumn
mscVrPpIpxPSapPRowStatus = _MscVrPpIpxPSapPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1, 1, 1),
    _MscVrPpIpxPSapPRowStatus_Type()
)
mscVrPpIpxPSapPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPRowStatus.setStatus("mandatory")
_MscVrPpIpxPSapPComponentName_Type = DisplayString
_MscVrPpIpxPSapPComponentName_Object = MibTableColumn
mscVrPpIpxPSapPComponentName = _MscVrPpIpxPSapPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1, 1, 2),
    _MscVrPpIpxPSapPComponentName_Type()
)
mscVrPpIpxPSapPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPComponentName.setStatus("mandatory")
_MscVrPpIpxPSapPStorageType_Type = StorageType
_MscVrPpIpxPSapPStorageType_Object = MibTableColumn
mscVrPpIpxPSapPStorageType = _MscVrPpIpxPSapPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1, 1, 4),
    _MscVrPpIpxPSapPStorageType_Type()
)
mscVrPpIpxPSapPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPStorageType.setStatus("mandatory")
_MscVrPpIpxPSapPIndex_Type = NonReplicated
_MscVrPpIpxPSapPIndex_Object = MibTableColumn
mscVrPpIpxPSapPIndex = _MscVrPpIpxPSapPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 1, 1, 10),
    _MscVrPpIpxPSapPIndex_Type()
)
mscVrPpIpxPSapPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPIndex.setStatus("mandatory")
_MscVrPpIpxPSapPStatsTable_Object = MibTable
mscVrPpIpxPSapPStatsTable = _MscVrPpIpxPSapPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPStatsTable.setStatus("mandatory")
_MscVrPpIpxPSapPStatsEntry_Object = MibTableRow
mscVrPpIpxPSapPStatsEntry = _MscVrPpIpxPSapPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1)
)
mscVrPpIpxPSapPStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPSapPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPStatsEntry.setStatus("mandatory")
_MscVrPpIpxPSapPInPackets_Type = Counter32
_MscVrPpIpxPSapPInPackets_Object = MibTableColumn
mscVrPpIpxPSapPInPackets = _MscVrPpIpxPSapPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 1),
    _MscVrPpIpxPSapPInPackets_Type()
)
mscVrPpIpxPSapPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPInPackets.setStatus("mandatory")
_MscVrPpIpxPSapPInRequests_Type = Counter32
_MscVrPpIpxPSapPInRequests_Object = MibTableColumn
mscVrPpIpxPSapPInRequests = _MscVrPpIpxPSapPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 2),
    _MscVrPpIpxPSapPInRequests_Type()
)
mscVrPpIpxPSapPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPInRequests.setStatus("mandatory")
_MscVrPpIpxPSapPInResponses_Type = Counter32
_MscVrPpIpxPSapPInResponses_Object = MibTableColumn
mscVrPpIpxPSapPInResponses = _MscVrPpIpxPSapPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 3),
    _MscVrPpIpxPSapPInResponses_Type()
)
mscVrPpIpxPSapPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPInResponses.setStatus("mandatory")
_MscVrPpIpxPSapPOutPackets_Type = Counter32
_MscVrPpIpxPSapPOutPackets_Object = MibTableColumn
mscVrPpIpxPSapPOutPackets = _MscVrPpIpxPSapPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 4),
    _MscVrPpIpxPSapPOutPackets_Type()
)
mscVrPpIpxPSapPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPOutPackets.setStatus("mandatory")
_MscVrPpIpxPSapPOutRequests_Type = Counter32
_MscVrPpIpxPSapPOutRequests_Object = MibTableColumn
mscVrPpIpxPSapPOutRequests = _MscVrPpIpxPSapPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 5),
    _MscVrPpIpxPSapPOutRequests_Type()
)
mscVrPpIpxPSapPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPOutRequests.setStatus("mandatory")
_MscVrPpIpxPSapPOutResponses_Type = Counter32
_MscVrPpIpxPSapPOutResponses_Object = MibTableColumn
mscVrPpIpxPSapPOutResponses = _MscVrPpIpxPSapPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 6),
    _MscVrPpIpxPSapPOutResponses_Type()
)
mscVrPpIpxPSapPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPOutResponses.setStatus("mandatory")
_MscVrPpIpxPSapPIncorrectPackets_Type = Counter32
_MscVrPpIpxPSapPIncorrectPackets_Object = MibTableColumn
mscVrPpIpxPSapPIncorrectPackets = _MscVrPpIpxPSapPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 3, 10, 1, 7),
    _MscVrPpIpxPSapPIncorrectPackets_Type()
)
mscVrPpIpxPSapPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSapPIncorrectPackets.setStatus("mandatory")
_MscVrPpIpxPIWP_ObjectIdentity = ObjectIdentity
mscVrPpIpxPIWP = _MscVrPpIpxPIWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4)
)
_MscVrPpIpxPIWPRowStatusTable_Object = MibTable
mscVrPpIpxPIWPRowStatusTable = _MscVrPpIpxPIWPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPRowStatusTable.setStatus("mandatory")
_MscVrPpIpxPIWPRowStatusEntry_Object = MibTableRow
mscVrPpIpxPIWPRowStatusEntry = _MscVrPpIpxPIWPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1, 1)
)
mscVrPpIpxPIWPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIWPRemoteStationIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpxPIWPRowStatus_Type = RowStatus
_MscVrPpIpxPIWPRowStatus_Object = MibTableColumn
mscVrPpIpxPIWPRowStatus = _MscVrPpIpxPIWPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1, 1, 1),
    _MscVrPpIpxPIWPRowStatus_Type()
)
mscVrPpIpxPIWPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPRowStatus.setStatus("mandatory")
_MscVrPpIpxPIWPComponentName_Type = DisplayString
_MscVrPpIpxPIWPComponentName_Object = MibTableColumn
mscVrPpIpxPIWPComponentName = _MscVrPpIpxPIWPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1, 1, 2),
    _MscVrPpIpxPIWPComponentName_Type()
)
mscVrPpIpxPIWPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPComponentName.setStatus("mandatory")
_MscVrPpIpxPIWPStorageType_Type = StorageType
_MscVrPpIpxPIWPStorageType_Object = MibTableColumn
mscVrPpIpxPIWPStorageType = _MscVrPpIpxPIWPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1, 1, 4),
    _MscVrPpIpxPIWPStorageType_Type()
)
mscVrPpIpxPIWPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPStorageType.setStatus("mandatory")


class _MscVrPpIpxPIWPRemoteStationIdentifierIndex_Type(DashedHexString):
    """Custom type mscVrPpIpxPIWPRemoteStationIdentifierIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscVrPpIpxPIWPRemoteStationIdentifierIndex_Type.__name__ = "DashedHexString"
_MscVrPpIpxPIWPRemoteStationIdentifierIndex_Object = MibTableColumn
mscVrPpIpxPIWPRemoteStationIdentifierIndex = _MscVrPpIpxPIWPRemoteStationIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 1, 1, 10),
    _MscVrPpIpxPIWPRemoteStationIdentifierIndex_Type()
)
mscVrPpIpxPIWPRemoteStationIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPRemoteStationIdentifierIndex.setStatus("mandatory")
_MscVrPpIpxPIWPOperTable_Object = MibTable
mscVrPpIpxPIWPOperTable = _MscVrPpIpxPIWPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPOperTable.setStatus("mandatory")
_MscVrPpIpxPIWPOperEntry_Object = MibTableRow
mscVrPpIpxPIWPOperEntry = _MscVrPpIpxPIWPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 10, 1)
)
mscVrPpIpxPIWPOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIWPRemoteStationIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPOperEntry.setStatus("mandatory")


class _MscVrPpIpxPIWPNeighbourRouterName_Type(AsciiString):
    """Custom type mscVrPpIpxPIWPNeighbourRouterName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MscVrPpIpxPIWPNeighbourRouterName_Type.__name__ = "AsciiString"
_MscVrPpIpxPIWPNeighbourRouterName_Object = MibTableColumn
mscVrPpIpxPIWPNeighbourRouterName = _MscVrPpIpxPIWPNeighbourRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 10, 1, 1),
    _MscVrPpIpxPIWPNeighbourRouterName_Type()
)
mscVrPpIpxPIWPNeighbourRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPNeighbourRouterName.setStatus("mandatory")


class _MscVrPpIpxPIWPNeighbourInternalNetworkNumber_Type(DashedHexString):
    """Custom type mscVrPpIpxPIWPNeighbourInternalNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrPpIpxPIWPNeighbourInternalNetworkNumber_Type.__name__ = "DashedHexString"
_MscVrPpIpxPIWPNeighbourInternalNetworkNumber_Object = MibTableColumn
mscVrPpIpxPIWPNeighbourInternalNetworkNumber = _MscVrPpIpxPIWPNeighbourInternalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 10, 1, 2),
    _MscVrPpIpxPIWPNeighbourInternalNetworkNumber_Type()
)
mscVrPpIpxPIWPNeighbourInternalNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPNeighbourInternalNetworkNumber.setStatus("mandatory")
_MscVrPpIpxPIWPInitFails_Type = Counter32
_MscVrPpIpxPIWPInitFails_Object = MibTableColumn
mscVrPpIpxPIWPInitFails = _MscVrPpIpxPIWPInitFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 4, 10, 1, 3),
    _MscVrPpIpxPIWPInitFails_Type()
)
mscVrPpIpxPIWPInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPIWPInitFails.setStatus("mandatory")
_MscVrPpIpxPNetSentryP_ObjectIdentity = ObjectIdentity
mscVrPpIpxPNetSentryP = _MscVrPpIpxPNetSentryP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5)
)
_MscVrPpIpxPNetSentryPRowStatusTable_Object = MibTable
mscVrPpIpxPNetSentryPRowStatusTable = _MscVrPpIpxPNetSentryPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPRowStatusTable.setStatus("mandatory")
_MscVrPpIpxPNetSentryPRowStatusEntry_Object = MibTableRow
mscVrPpIpxPNetSentryPRowStatusEntry = _MscVrPpIpxPNetSentryPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1, 1)
)
mscVrPpIpxPNetSentryPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPNetSentryPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPRowStatusEntry.setStatus("mandatory")
_MscVrPpIpxPNetSentryPRowStatus_Type = RowStatus
_MscVrPpIpxPNetSentryPRowStatus_Object = MibTableColumn
mscVrPpIpxPNetSentryPRowStatus = _MscVrPpIpxPNetSentryPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1, 1, 1),
    _MscVrPpIpxPNetSentryPRowStatus_Type()
)
mscVrPpIpxPNetSentryPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPRowStatus.setStatus("mandatory")
_MscVrPpIpxPNetSentryPComponentName_Type = DisplayString
_MscVrPpIpxPNetSentryPComponentName_Object = MibTableColumn
mscVrPpIpxPNetSentryPComponentName = _MscVrPpIpxPNetSentryPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1, 1, 2),
    _MscVrPpIpxPNetSentryPComponentName_Type()
)
mscVrPpIpxPNetSentryPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPComponentName.setStatus("mandatory")
_MscVrPpIpxPNetSentryPStorageType_Type = StorageType
_MscVrPpIpxPNetSentryPStorageType_Object = MibTableColumn
mscVrPpIpxPNetSentryPStorageType = _MscVrPpIpxPNetSentryPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1, 1, 4),
    _MscVrPpIpxPNetSentryPStorageType_Type()
)
mscVrPpIpxPNetSentryPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPStorageType.setStatus("mandatory")
_MscVrPpIpxPNetSentryPIndex_Type = NonReplicated
_MscVrPpIpxPNetSentryPIndex_Object = MibTableColumn
mscVrPpIpxPNetSentryPIndex = _MscVrPpIpxPNetSentryPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 1, 1, 10),
    _MscVrPpIpxPNetSentryPIndex_Type()
)
mscVrPpIpxPNetSentryPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPIndex.setStatus("mandatory")
_MscVrPpIpxPNetSentryPProvTable_Object = MibTable
mscVrPpIpxPNetSentryPProvTable = _MscVrPpIpxPNetSentryPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPProvTable.setStatus("mandatory")
_MscVrPpIpxPNetSentryPProvEntry_Object = MibTableRow
mscVrPpIpxPNetSentryPProvEntry = _MscVrPpIpxPNetSentryPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 10, 1)
)
mscVrPpIpxPNetSentryPProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPNetSentryPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPProvEntry.setStatus("mandatory")


class _MscVrPpIpxPNetSentryPInComingFilter_Type(AsciiString):
    """Custom type mscVrPpIpxPNetSentryPInComingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpIpxPNetSentryPInComingFilter_Type.__name__ = "AsciiString"
_MscVrPpIpxPNetSentryPInComingFilter_Object = MibTableColumn
mscVrPpIpxPNetSentryPInComingFilter = _MscVrPpIpxPNetSentryPInComingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 10, 1, 1),
    _MscVrPpIpxPNetSentryPInComingFilter_Type()
)
mscVrPpIpxPNetSentryPInComingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPInComingFilter.setStatus("mandatory")


class _MscVrPpIpxPNetSentryPOutGoingFilter_Type(AsciiString):
    """Custom type mscVrPpIpxPNetSentryPOutGoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrPpIpxPNetSentryPOutGoingFilter_Type.__name__ = "AsciiString"
_MscVrPpIpxPNetSentryPOutGoingFilter_Object = MibTableColumn
mscVrPpIpxPNetSentryPOutGoingFilter = _MscVrPpIpxPNetSentryPOutGoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 5, 10, 1, 2),
    _MscVrPpIpxPNetSentryPOutGoingFilter_Type()
)
mscVrPpIpxPNetSentryPOutGoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetSentryPOutGoingFilter.setStatus("mandatory")
_MscVrPpIpxPAdminControlTable_Object = MibTable
mscVrPpIpxPAdminControlTable = _MscVrPpIpxPAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 100)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPAdminControlTable.setStatus("mandatory")
_MscVrPpIpxPAdminControlEntry_Object = MibTableRow
mscVrPpIpxPAdminControlEntry = _MscVrPpIpxPAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 100, 1)
)
mscVrPpIpxPAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPAdminControlEntry.setStatus("mandatory")


class _MscVrPpIpxPSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrPpIpxPSnmpAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpxPSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrPpIpxPSnmpAdminStatus_Object = MibTableColumn
mscVrPpIpxPSnmpAdminStatus = _MscVrPpIpxPSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 100, 1, 1),
    _MscVrPpIpxPSnmpAdminStatus_Type()
)
mscVrPpIpxPSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPSnmpAdminStatus.setStatus("mandatory")
_MscVrPpIpxPProvTable_Object = MibTable
mscVrPpIpxPProvTable = _MscVrPpIpxPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 101)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPProvTable.setStatus("mandatory")
_MscVrPpIpxPProvEntry_Object = MibTableRow
mscVrPpIpxPProvEntry = _MscVrPpIpxPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 101, 1)
)
mscVrPpIpxPProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPProvEntry.setStatus("mandatory")


class _MscVrPpIpxPNetworkNumberProv_Type(DashedHexString):
    """Custom type mscVrPpIpxPNetworkNumberProv based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscVrPpIpxPNetworkNumberProv_Type.__name__ = "DashedHexString"
_MscVrPpIpxPNetworkNumberProv_Object = MibTableColumn
mscVrPpIpxPNetworkNumberProv = _MscVrPpIpxPNetworkNumberProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 101, 1, 1),
    _MscVrPpIpxPNetworkNumberProv_Type()
)
mscVrPpIpxPNetworkNumberProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetworkNumberProv.setStatus("mandatory")


class _MscVrPpIpxPDefaultType_Type(Integer32):
    """Custom type mscVrPpIpxPDefaultType based on Integer32"""
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
        *(("broadcast", 2),
          ("other", 1),
          ("ppp", 3),
          ("unnumberedRip", 5),
          ("wanRip", 4))
    )


_MscVrPpIpxPDefaultType_Type.__name__ = "Integer32"
_MscVrPpIpxPDefaultType_Object = MibTableColumn
mscVrPpIpxPDefaultType = _MscVrPpIpxPDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 101, 1, 2),
    _MscVrPpIpxPDefaultType_Type()
)
mscVrPpIpxPDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPDefaultType.setStatus("mandatory")


class _MscVrPpIpxPBroadcastInhibit_Type(Integer32):
    """Custom type mscVrPpIpxPBroadcastInhibit based on Integer32"""
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


_MscVrPpIpxPBroadcastInhibit_Type.__name__ = "Integer32"
_MscVrPpIpxPBroadcastInhibit_Object = MibTableColumn
mscVrPpIpxPBroadcastInhibit = _MscVrPpIpxPBroadcastInhibit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 101, 1, 3),
    _MscVrPpIpxPBroadcastInhibit_Type()
)
mscVrPpIpxPBroadcastInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPBroadcastInhibit.setStatus("mandatory")
_MscVrPpIpxPSresProvTable_Object = MibTable
mscVrPpIpxPSresProvTable = _MscVrPpIpxPSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 102)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSresProvTable.setStatus("mandatory")
_MscVrPpIpxPSresProvEntry_Object = MibTableRow
mscVrPpIpxPSresProvEntry = _MscVrPpIpxPSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 102, 1)
)
mscVrPpIpxPSresProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPSresProvEntry.setStatus("mandatory")


class _MscVrPpIpxPSourceRouteEndStationSupport_Type(Integer32):
    """Custom type mscVrPpIpxPSourceRouteEndStationSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MscVrPpIpxPSourceRouteEndStationSupport_Type.__name__ = "Integer32"
_MscVrPpIpxPSourceRouteEndStationSupport_Object = MibTableColumn
mscVrPpIpxPSourceRouteEndStationSupport = _MscVrPpIpxPSourceRouteEndStationSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 102, 1, 1),
    _MscVrPpIpxPSourceRouteEndStationSupport_Type()
)
mscVrPpIpxPSourceRouteEndStationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrPpIpxPSourceRouteEndStationSupport.setStatus("mandatory")
_MscVrPpIpxPStateTable_Object = MibTable
mscVrPpIpxPStateTable = _MscVrPpIpxPStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 103)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPStateTable.setStatus("mandatory")
_MscVrPpIpxPStateEntry_Object = MibTableRow
mscVrPpIpxPStateEntry = _MscVrPpIpxPStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 103, 1)
)
mscVrPpIpxPStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPStateEntry.setStatus("mandatory")


class _MscVrPpIpxPAdminState_Type(Integer32):
    """Custom type mscVrPpIpxPAdminState based on Integer32"""
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


_MscVrPpIpxPAdminState_Type.__name__ = "Integer32"
_MscVrPpIpxPAdminState_Object = MibTableColumn
mscVrPpIpxPAdminState = _MscVrPpIpxPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 103, 1, 1),
    _MscVrPpIpxPAdminState_Type()
)
mscVrPpIpxPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPAdminState.setStatus("mandatory")


class _MscVrPpIpxPOperationalState_Type(Integer32):
    """Custom type mscVrPpIpxPOperationalState based on Integer32"""
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


_MscVrPpIpxPOperationalState_Type.__name__ = "Integer32"
_MscVrPpIpxPOperationalState_Object = MibTableColumn
mscVrPpIpxPOperationalState = _MscVrPpIpxPOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 103, 1, 2),
    _MscVrPpIpxPOperationalState_Type()
)
mscVrPpIpxPOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPOperationalState.setStatus("mandatory")


class _MscVrPpIpxPUsageState_Type(Integer32):
    """Custom type mscVrPpIpxPUsageState based on Integer32"""
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


_MscVrPpIpxPUsageState_Type.__name__ = "Integer32"
_MscVrPpIpxPUsageState_Object = MibTableColumn
mscVrPpIpxPUsageState = _MscVrPpIpxPUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 103, 1, 3),
    _MscVrPpIpxPUsageState_Type()
)
mscVrPpIpxPUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPUsageState.setStatus("mandatory")
_MscVrPpIpxPOperStatusTable_Object = MibTable
mscVrPpIpxPOperStatusTable = _MscVrPpIpxPOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 104)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPOperStatusTable.setStatus("mandatory")
_MscVrPpIpxPOperStatusEntry_Object = MibTableRow
mscVrPpIpxPOperStatusEntry = _MscVrPpIpxPOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 104, 1)
)
mscVrPpIpxPOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPOperStatusEntry.setStatus("mandatory")


class _MscVrPpIpxPSnmpOperStatus_Type(Integer32):
    """Custom type mscVrPpIpxPSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrPpIpxPSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrPpIpxPSnmpOperStatus_Object = MibTableColumn
mscVrPpIpxPSnmpOperStatus = _MscVrPpIpxPSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 104, 1, 1),
    _MscVrPpIpxPSnmpOperStatus_Type()
)
mscVrPpIpxPSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPSnmpOperStatus.setStatus("mandatory")
_MscVrPpIpxPOperTable_Object = MibTable
mscVrPpIpxPOperTable = _MscVrPpIpxPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPOperTable.setStatus("mandatory")
_MscVrPpIpxPOperEntry_Object = MibTableRow
mscVrPpIpxPOperEntry = _MscVrPpIpxPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105, 1)
)
mscVrPpIpxPOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPOperEntry.setStatus("mandatory")


class _MscVrPpIpxPType_Type(Integer32):
    """Custom type mscVrPpIpxPType based on Integer32"""
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
        *(("broadcast", 2),
          ("other", 1),
          ("ppp", 3),
          ("unnumberedRip", 5),
          ("wanRip", 4))
    )


_MscVrPpIpxPType_Type.__name__ = "Integer32"
_MscVrPpIpxPType_Object = MibTableColumn
mscVrPpIpxPType = _MscVrPpIpxPType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105, 1, 1),
    _MscVrPpIpxPType_Type()
)
mscVrPpIpxPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPType.setStatus("mandatory")


class _MscVrPpIpxPEncapsulation_Type(Integer32):
    """Custom type mscVrPpIpxPEncapsulation based on Integer32"""
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
        *(("ethernet", 2),
          ("link", 1),
          ("novell", 3),
          ("sap", 4),
          ("snap", 5),
          ("tunnel", 7),
          ("vns", 6))
    )


_MscVrPpIpxPEncapsulation_Type.__name__ = "Integer32"
_MscVrPpIpxPEncapsulation_Object = MibTableColumn
mscVrPpIpxPEncapsulation = _MscVrPpIpxPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105, 1, 2),
    _MscVrPpIpxPEncapsulation_Type()
)
mscVrPpIpxPEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPEncapsulation.setStatus("mandatory")


class _MscVrPpIpxPNetworkNumber_Type(DashedHexString):
    """Custom type mscVrPpIpxPNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscVrPpIpxPNetworkNumber_Type.__name__ = "DashedHexString"
_MscVrPpIpxPNetworkNumber_Object = MibTableColumn
mscVrPpIpxPNetworkNumber = _MscVrPpIpxPNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105, 1, 3),
    _MscVrPpIpxPNetworkNumber_Type()
)
mscVrPpIpxPNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPNetworkNumber.setStatus("mandatory")


class _MscVrPpIpxPNode_Type(DashedHexString):
    """Custom type mscVrPpIpxPNode based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_MscVrPpIpxPNode_Type.__name__ = "DashedHexString"
_MscVrPpIpxPNode_Object = MibTableColumn
mscVrPpIpxPNode = _MscVrPpIpxPNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 105, 1, 4),
    _MscVrPpIpxPNode_Type()
)
mscVrPpIpxPNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPNode.setStatus("mandatory")
_MscVrPpIpxPStatsTable_Object = MibTable
mscVrPpIpxPStatsTable = _MscVrPpIpxPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 106)
)
if mibBuilder.loadTexts:
    mscVrPpIpxPStatsTable.setStatus("mandatory")
_MscVrPpIpxPStatsEntry_Object = MibTableRow
mscVrPpIpxPStatsEntry = _MscVrPpIpxPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 106, 1)
)
mscVrPpIpxPStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrPpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    mscVrPpIpxPStatsEntry.setStatus("mandatory")
_MscVrPpIpxPStateChanges_Type = Counter32
_MscVrPpIpxPStateChanges_Object = MibTableColumn
mscVrPpIpxPStateChanges = _MscVrPpIpxPStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 106, 1, 1),
    _MscVrPpIpxPStateChanges_Type()
)
mscVrPpIpxPStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPStateChanges.setStatus("mandatory")
_MscVrPpIpxPInReceives_Type = Counter32
_MscVrPpIpxPInReceives_Object = MibTableColumn
mscVrPpIpxPInReceives = _MscVrPpIpxPInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 106, 1, 2),
    _MscVrPpIpxPInReceives_Type()
)
mscVrPpIpxPInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPInReceives.setStatus("mandatory")
_MscVrPpIpxPForwarded_Type = Counter32
_MscVrPpIpxPForwarded_Object = MibTableColumn
mscVrPpIpxPForwarded = _MscVrPpIpxPForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 3, 6, 106, 1, 3),
    _MscVrPpIpxPForwarded_Type()
)
mscVrPpIpxPForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrPpIpxPForwarded.setStatus("mandatory")
_MscVrIpx_ObjectIdentity = ObjectIdentity
mscVrIpx = _MscVrIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7)
)
_MscVrIpxRowStatusTable_Object = MibTable
mscVrIpxRowStatusTable = _MscVrIpxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxRowStatusTable.setStatus("mandatory")
_MscVrIpxRowStatusEntry_Object = MibTableRow
mscVrIpxRowStatusEntry = _MscVrIpxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1, 1)
)
mscVrIpxRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRowStatusEntry.setStatus("mandatory")
_MscVrIpxRowStatus_Type = RowStatus
_MscVrIpxRowStatus_Object = MibTableColumn
mscVrIpxRowStatus = _MscVrIpxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1, 1, 1),
    _MscVrIpxRowStatus_Type()
)
mscVrIpxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRowStatus.setStatus("mandatory")
_MscVrIpxComponentName_Type = DisplayString
_MscVrIpxComponentName_Object = MibTableColumn
mscVrIpxComponentName = _MscVrIpxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1, 1, 2),
    _MscVrIpxComponentName_Type()
)
mscVrIpxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxComponentName.setStatus("mandatory")
_MscVrIpxStorageType_Type = StorageType
_MscVrIpxStorageType_Object = MibTableColumn
mscVrIpxStorageType = _MscVrIpxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1, 1, 4),
    _MscVrIpxStorageType_Type()
)
mscVrIpxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxStorageType.setStatus("mandatory")
_MscVrIpxIndex_Type = NonReplicated
_MscVrIpxIndex_Object = MibTableColumn
mscVrIpxIndex = _MscVrIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 1, 1, 10),
    _MscVrIpxIndex_Type()
)
mscVrIpxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxIndex.setStatus("mandatory")
_MscVrIpxRip_ObjectIdentity = ObjectIdentity
mscVrIpxRip = _MscVrIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2)
)
_MscVrIpxRipRowStatusTable_Object = MibTable
mscVrIpxRipRowStatusTable = _MscVrIpxRipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRowStatusTable.setStatus("mandatory")
_MscVrIpxRipRowStatusEntry_Object = MibTableRow
mscVrIpxRipRowStatusEntry = _MscVrIpxRipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1, 1)
)
mscVrIpxRipRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRowStatusEntry.setStatus("mandatory")
_MscVrIpxRipRowStatus_Type = RowStatus
_MscVrIpxRipRowStatus_Object = MibTableColumn
mscVrIpxRipRowStatus = _MscVrIpxRipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1, 1, 1),
    _MscVrIpxRipRowStatus_Type()
)
mscVrIpxRipRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRowStatus.setStatus("mandatory")
_MscVrIpxRipComponentName_Type = DisplayString
_MscVrIpxRipComponentName_Object = MibTableColumn
mscVrIpxRipComponentName = _MscVrIpxRipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1, 1, 2),
    _MscVrIpxRipComponentName_Type()
)
mscVrIpxRipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipComponentName.setStatus("mandatory")
_MscVrIpxRipStorageType_Type = StorageType
_MscVrIpxRipStorageType_Object = MibTableColumn
mscVrIpxRipStorageType = _MscVrIpxRipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1, 1, 4),
    _MscVrIpxRipStorageType_Type()
)
mscVrIpxRipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipStorageType.setStatus("mandatory")
_MscVrIpxRipIndex_Type = NonReplicated
_MscVrIpxRipIndex_Object = MibTableColumn
mscVrIpxRipIndex = _MscVrIpxRipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 1, 1, 10),
    _MscVrIpxRipIndex_Type()
)
mscVrIpxRipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxRipIndex.setStatus("mandatory")
_MscVrIpxRipRFltr_ObjectIdentity = ObjectIdentity
mscVrIpxRipRFltr = _MscVrIpxRipRFltr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2)
)
_MscVrIpxRipRFltrRowStatusTable_Object = MibTable
mscVrIpxRipRFltrRowStatusTable = _MscVrIpxRipRFltrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrRowStatusTable.setStatus("mandatory")
_MscVrIpxRipRFltrRowStatusEntry_Object = MibTableRow
mscVrIpxRipRFltrRowStatusEntry = _MscVrIpxRipRFltrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1, 1)
)
mscVrIpxRipRFltrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrRowStatusEntry.setStatus("mandatory")
_MscVrIpxRipRFltrRowStatus_Type = RowStatus
_MscVrIpxRipRFltrRowStatus_Object = MibTableColumn
mscVrIpxRipRFltrRowStatus = _MscVrIpxRipRFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1, 1, 1),
    _MscVrIpxRipRFltrRowStatus_Type()
)
mscVrIpxRipRFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrRowStatus.setStatus("mandatory")
_MscVrIpxRipRFltrComponentName_Type = DisplayString
_MscVrIpxRipRFltrComponentName_Object = MibTableColumn
mscVrIpxRipRFltrComponentName = _MscVrIpxRipRFltrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1, 1, 2),
    _MscVrIpxRipRFltrComponentName_Type()
)
mscVrIpxRipRFltrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrComponentName.setStatus("mandatory")
_MscVrIpxRipRFltrStorageType_Type = StorageType
_MscVrIpxRipRFltrStorageType_Object = MibTableColumn
mscVrIpxRipRFltrStorageType = _MscVrIpxRipRFltrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1, 1, 4),
    _MscVrIpxRipRFltrStorageType_Type()
)
mscVrIpxRipRFltrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrStorageType.setStatus("mandatory")


class _MscVrIpxRipRFltrIdentifierIndex_Type(Integer32):
    """Custom type mscVrIpxRipRFltrIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrIpxRipRFltrIdentifierIndex_Type.__name__ = "Integer32"
_MscVrIpxRipRFltrIdentifierIndex_Object = MibTableColumn
mscVrIpxRipRFltrIdentifierIndex = _MscVrIpxRipRFltrIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 1, 1, 10),
    _MscVrIpxRipRFltrIdentifierIndex_Type()
)
mscVrIpxRipRFltrIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrIdentifierIndex.setStatus("mandatory")
_MscVrIpxRipRFltrProvTable_Object = MibTable
mscVrIpxRipRFltrProvTable = _MscVrIpxRipRFltrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrProvTable.setStatus("mandatory")
_MscVrIpxRipRFltrProvEntry_Object = MibTableRow
mscVrIpxRipRFltrProvEntry = _MscVrIpxRipRFltrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1)
)
mscVrIpxRipRFltrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrProvEntry.setStatus("mandatory")


class _MscVrIpxRipRFltrHops_Type(AsciiString):
    """Custom type mscVrIpxRipRFltrHops based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscVrIpxRipRFltrHops_Type.__name__ = "AsciiString"
_MscVrIpxRipRFltrHops_Object = MibTableColumn
mscVrIpxRipRFltrHops = _MscVrIpxRipRFltrHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 1),
    _MscVrIpxRipRFltrHops_Type()
)
mscVrIpxRipRFltrHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrHops.setStatus("mandatory")


class _MscVrIpxRipRFltrTicks_Type(AsciiString):
    """Custom type mscVrIpxRipRFltrTicks based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_MscVrIpxRipRFltrTicks_Type.__name__ = "AsciiString"
_MscVrIpxRipRFltrTicks_Object = MibTableColumn
mscVrIpxRipRFltrTicks = _MscVrIpxRipRFltrTicks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 2),
    _MscVrIpxRipRFltrTicks_Type()
)
mscVrIpxRipRFltrTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrTicks.setStatus("mandatory")


class _MscVrIpxRipRFltrNetworkNumber_Type(AsciiString):
    """Custom type mscVrIpxRipRFltrNetworkNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscVrIpxRipRFltrNetworkNumber_Type.__name__ = "AsciiString"
_MscVrIpxRipRFltrNetworkNumber_Object = MibTableColumn
mscVrIpxRipRFltrNetworkNumber = _MscVrIpxRipRFltrNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 3),
    _MscVrIpxRipRFltrNetworkNumber_Type()
)
mscVrIpxRipRFltrNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrNetworkNumber.setStatus("mandatory")


class _MscVrIpxRipRFltrNode_Type(AsciiString):
    """Custom type mscVrIpxRipRFltrNode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_MscVrIpxRipRFltrNode_Type.__name__ = "AsciiString"
_MscVrIpxRipRFltrNode_Object = MibTableColumn
mscVrIpxRipRFltrNode = _MscVrIpxRipRFltrNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 4),
    _MscVrIpxRipRFltrNode_Type()
)
mscVrIpxRipRFltrNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrNode.setStatus("mandatory")


class _MscVrIpxRipRFltrPort_Type(AsciiString):
    """Custom type mscVrIpxRipRFltrPort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_MscVrIpxRipRFltrPort_Type.__name__ = "AsciiString"
_MscVrIpxRipRFltrPort_Object = MibTableColumn
mscVrIpxRipRFltrPort = _MscVrIpxRipRFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 5),
    _MscVrIpxRipRFltrPort_Type()
)
mscVrIpxRipRFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrPort.setStatus("mandatory")


class _MscVrIpxRipRFltrDisposition_Type(Integer32):
    """Custom type mscVrIpxRipRFltrDisposition based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("pass", 1))
    )


_MscVrIpxRipRFltrDisposition_Type.__name__ = "Integer32"
_MscVrIpxRipRFltrDisposition_Object = MibTableColumn
mscVrIpxRipRFltrDisposition = _MscVrIpxRipRFltrDisposition_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 10, 1, 6),
    _MscVrIpxRipRFltrDisposition_Type()
)
mscVrIpxRipRFltrDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrDisposition.setStatus("mandatory")
_MscVrIpxRipRFltrOperTable_Object = MibTable
mscVrIpxRipRFltrOperTable = _MscVrIpxRipRFltrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrOperTable.setStatus("mandatory")
_MscVrIpxRipRFltrOperEntry_Object = MibTableRow
mscVrIpxRipRFltrOperEntry = _MscVrIpxRipRFltrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 11, 1)
)
mscVrIpxRipRFltrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrOperEntry.setStatus("mandatory")


class _MscVrIpxRipRFltrNumberOfApplyEntries_Type(Gauge32):
    """Custom type mscVrIpxRipRFltrNumberOfApplyEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpxRipRFltrNumberOfApplyEntries_Type.__name__ = "Gauge32"
_MscVrIpxRipRFltrNumberOfApplyEntries_Object = MibTableColumn
mscVrIpxRipRFltrNumberOfApplyEntries = _MscVrIpxRipRFltrNumberOfApplyEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 2, 11, 1, 1),
    _MscVrIpxRipRFltrNumberOfApplyEntries_Type()
)
mscVrIpxRipRFltrNumberOfApplyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRFltrNumberOfApplyEntries.setStatus("mandatory")
_MscVrIpxRipRipApp_ObjectIdentity = ObjectIdentity
mscVrIpxRipRipApp = _MscVrIpxRipRipApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3)
)
_MscVrIpxRipRipAppRowStatusTable_Object = MibTable
mscVrIpxRipRipAppRowStatusTable = _MscVrIpxRipRipAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppRowStatusTable.setStatus("mandatory")
_MscVrIpxRipRipAppRowStatusEntry_Object = MibTableRow
mscVrIpxRipRipAppRowStatusEntry = _MscVrIpxRipRipAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1)
)
mscVrIpxRipRipAppRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRipAppProtocolPortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRipAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppRowStatusEntry.setStatus("mandatory")
_MscVrIpxRipRipAppRowStatus_Type = RowStatus
_MscVrIpxRipRipAppRowStatus_Object = MibTableColumn
mscVrIpxRipRipAppRowStatus = _MscVrIpxRipRipAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1, 1),
    _MscVrIpxRipRipAppRowStatus_Type()
)
mscVrIpxRipRipAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppRowStatus.setStatus("mandatory")
_MscVrIpxRipRipAppComponentName_Type = DisplayString
_MscVrIpxRipRipAppComponentName_Object = MibTableColumn
mscVrIpxRipRipAppComponentName = _MscVrIpxRipRipAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1, 2),
    _MscVrIpxRipRipAppComponentName_Type()
)
mscVrIpxRipRipAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppComponentName.setStatus("mandatory")
_MscVrIpxRipRipAppStorageType_Type = StorageType
_MscVrIpxRipRipAppStorageType_Object = MibTableColumn
mscVrIpxRipRipAppStorageType = _MscVrIpxRipRipAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1, 4),
    _MscVrIpxRipRipAppStorageType_Type()
)
mscVrIpxRipRipAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppStorageType.setStatus("mandatory")


class _MscVrIpxRipRipAppProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpxRipRipAppProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpxRipRipAppProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpxRipRipAppProtocolPortNameIndex_Object = MibTableColumn
mscVrIpxRipRipAppProtocolPortNameIndex = _MscVrIpxRipRipAppProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1, 10),
    _MscVrIpxRipRipAppProtocolPortNameIndex_Type()
)
mscVrIpxRipRipAppProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppProtocolPortNameIndex.setStatus("mandatory")


class _MscVrIpxRipRipAppFilterIdentifierIndex_Type(Integer32):
    """Custom type mscVrIpxRipRipAppFilterIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrIpxRipRipAppFilterIdentifierIndex_Type.__name__ = "Integer32"
_MscVrIpxRipRipAppFilterIdentifierIndex_Object = MibTableColumn
mscVrIpxRipRipAppFilterIdentifierIndex = _MscVrIpxRipRipAppFilterIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 1, 1, 11),
    _MscVrIpxRipRipAppFilterIdentifierIndex_Type()
)
mscVrIpxRipRipAppFilterIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppFilterIdentifierIndex.setStatus("mandatory")
_MscVrIpxRipRipAppProvTable_Object = MibTable
mscVrIpxRipRipAppProvTable = _MscVrIpxRipRipAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppProvTable.setStatus("mandatory")
_MscVrIpxRipRipAppProvEntry_Object = MibTableRow
mscVrIpxRipRipAppProvEntry = _MscVrIpxRipRipAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 10, 1)
)
mscVrIpxRipRipAppProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRipAppProtocolPortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipRipAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppProvEntry.setStatus("mandatory")


class _MscVrIpxRipRipAppDirection_Type(Integer32):
    """Custom type mscVrIpxRipRipAppDirection based on Integer32"""
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
        *(("input", 2),
          ("none", 0),
          ("output", 1))
    )


_MscVrIpxRipRipAppDirection_Type.__name__ = "Integer32"
_MscVrIpxRipRipAppDirection_Object = MibTableColumn
mscVrIpxRipRipAppDirection = _MscVrIpxRipRipAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 3, 10, 1, 1),
    _MscVrIpxRipRipAppDirection_Type()
)
mscVrIpxRipRipAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipRipAppDirection.setStatus("mandatory")
_MscVrIpxRipStatsTable_Object = MibTable
mscVrIpxRipStatsTable = _MscVrIpxRipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxRipStatsTable.setStatus("mandatory")
_MscVrIpxRipStatsEntry_Object = MibTableRow
mscVrIpxRipStatsEntry = _MscVrIpxRipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 10, 1)
)
mscVrIpxRipStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxRipIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxRipStatsEntry.setStatus("mandatory")
_MscVrIpxRipRipIn_Type = Counter32
_MscVrIpxRipRipIn_Object = MibTableColumn
mscVrIpxRipRipIn = _MscVrIpxRipRipIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 10, 1, 1),
    _MscVrIpxRipRipIn_Type()
)
mscVrIpxRipRipIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRipIn.setStatus("mandatory")
_MscVrIpxRipRipOut_Type = Counter32
_MscVrIpxRipRipOut_Object = MibTableColumn
mscVrIpxRipRipOut = _MscVrIpxRipRipOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 10, 1, 2),
    _MscVrIpxRipRipOut_Type()
)
mscVrIpxRipRipOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRipOut.setStatus("mandatory")
_MscVrIpxRipRipIncorrectPackets_Type = Counter32
_MscVrIpxRipRipIncorrectPackets_Object = MibTableColumn
mscVrIpxRipRipIncorrectPackets = _MscVrIpxRipRipIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 2, 10, 1, 3),
    _MscVrIpxRipRipIncorrectPackets_Type()
)
mscVrIpxRipRipIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxRipRipIncorrectPackets.setStatus("mandatory")
_MscVrIpxSap_ObjectIdentity = ObjectIdentity
mscVrIpxSap = _MscVrIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3)
)
_MscVrIpxSapRowStatusTable_Object = MibTable
mscVrIpxSapRowStatusTable = _MscVrIpxSapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxSapRowStatusTable.setStatus("mandatory")
_MscVrIpxSapRowStatusEntry_Object = MibTableRow
mscVrIpxSapRowStatusEntry = _MscVrIpxSapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1, 1)
)
mscVrIpxSapRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapRowStatusEntry.setStatus("mandatory")
_MscVrIpxSapRowStatus_Type = RowStatus
_MscVrIpxSapRowStatus_Object = MibTableColumn
mscVrIpxSapRowStatus = _MscVrIpxSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1, 1, 1),
    _MscVrIpxSapRowStatus_Type()
)
mscVrIpxSapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapRowStatus.setStatus("mandatory")
_MscVrIpxSapComponentName_Type = DisplayString
_MscVrIpxSapComponentName_Object = MibTableColumn
mscVrIpxSapComponentName = _MscVrIpxSapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1, 1, 2),
    _MscVrIpxSapComponentName_Type()
)
mscVrIpxSapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapComponentName.setStatus("mandatory")
_MscVrIpxSapStorageType_Type = StorageType
_MscVrIpxSapStorageType_Object = MibTableColumn
mscVrIpxSapStorageType = _MscVrIpxSapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1, 1, 4),
    _MscVrIpxSapStorageType_Type()
)
mscVrIpxSapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapStorageType.setStatus("mandatory")
_MscVrIpxSapIndex_Type = NonReplicated
_MscVrIpxSapIndex_Object = MibTableColumn
mscVrIpxSapIndex = _MscVrIpxSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 1, 1, 10),
    _MscVrIpxSapIndex_Type()
)
mscVrIpxSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSapIndex.setStatus("mandatory")
_MscVrIpxSapSFltr_ObjectIdentity = ObjectIdentity
mscVrIpxSapSFltr = _MscVrIpxSapSFltr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2)
)
_MscVrIpxSapSFltrRowStatusTable_Object = MibTable
mscVrIpxSapSFltrRowStatusTable = _MscVrIpxSapSFltrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrRowStatusTable.setStatus("mandatory")
_MscVrIpxSapSFltrRowStatusEntry_Object = MibTableRow
mscVrIpxSapSFltrRowStatusEntry = _MscVrIpxSapSFltrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1, 1)
)
mscVrIpxSapSFltrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrRowStatusEntry.setStatus("mandatory")
_MscVrIpxSapSFltrRowStatus_Type = RowStatus
_MscVrIpxSapSFltrRowStatus_Object = MibTableColumn
mscVrIpxSapSFltrRowStatus = _MscVrIpxSapSFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1, 1, 1),
    _MscVrIpxSapSFltrRowStatus_Type()
)
mscVrIpxSapSFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrRowStatus.setStatus("mandatory")
_MscVrIpxSapSFltrComponentName_Type = DisplayString
_MscVrIpxSapSFltrComponentName_Object = MibTableColumn
mscVrIpxSapSFltrComponentName = _MscVrIpxSapSFltrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1, 1, 2),
    _MscVrIpxSapSFltrComponentName_Type()
)
mscVrIpxSapSFltrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrComponentName.setStatus("mandatory")
_MscVrIpxSapSFltrStorageType_Type = StorageType
_MscVrIpxSapSFltrStorageType_Object = MibTableColumn
mscVrIpxSapSFltrStorageType = _MscVrIpxSapSFltrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1, 1, 4),
    _MscVrIpxSapSFltrStorageType_Type()
)
mscVrIpxSapSFltrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrStorageType.setStatus("mandatory")


class _MscVrIpxSapSFltrIdentifierIndex_Type(Integer32):
    """Custom type mscVrIpxSapSFltrIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrIpxSapSFltrIdentifierIndex_Type.__name__ = "Integer32"
_MscVrIpxSapSFltrIdentifierIndex_Object = MibTableColumn
mscVrIpxSapSFltrIdentifierIndex = _MscVrIpxSapSFltrIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 1, 1, 10),
    _MscVrIpxSapSFltrIdentifierIndex_Type()
)
mscVrIpxSapSFltrIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrIdentifierIndex.setStatus("mandatory")
_MscVrIpxSapSFltrProvTable_Object = MibTable
mscVrIpxSapSFltrProvTable = _MscVrIpxSapSFltrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrProvTable.setStatus("mandatory")
_MscVrIpxSapSFltrProvEntry_Object = MibTableRow
mscVrIpxSapSFltrProvEntry = _MscVrIpxSapSFltrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1)
)
mscVrIpxSapSFltrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrProvEntry.setStatus("mandatory")


class _MscVrIpxSapSFltrType_Type(AsciiString):
    """Custom type mscVrIpxSapSFltrType based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_MscVrIpxSapSFltrType_Type.__name__ = "AsciiString"
_MscVrIpxSapSFltrType_Object = MibTableColumn
mscVrIpxSapSFltrType = _MscVrIpxSapSFltrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1, 1),
    _MscVrIpxSapSFltrType_Type()
)
mscVrIpxSapSFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrType.setStatus("mandatory")


class _MscVrIpxSapSFltrName_Type(AsciiString):
    """Custom type mscVrIpxSapSFltrName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_MscVrIpxSapSFltrName_Type.__name__ = "AsciiString"
_MscVrIpxSapSFltrName_Object = MibTableColumn
mscVrIpxSapSFltrName = _MscVrIpxSapSFltrName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1, 2),
    _MscVrIpxSapSFltrName_Type()
)
mscVrIpxSapSFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrName.setStatus("mandatory")


class _MscVrIpxSapSFltrNetworkNumber_Type(AsciiString):
    """Custom type mscVrIpxSapSFltrNetworkNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_MscVrIpxSapSFltrNetworkNumber_Type.__name__ = "AsciiString"
_MscVrIpxSapSFltrNetworkNumber_Object = MibTableColumn
mscVrIpxSapSFltrNetworkNumber = _MscVrIpxSapSFltrNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1, 3),
    _MscVrIpxSapSFltrNetworkNumber_Type()
)
mscVrIpxSapSFltrNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrNetworkNumber.setStatus("mandatory")


class _MscVrIpxSapSFltrNode_Type(AsciiString):
    """Custom type mscVrIpxSapSFltrNode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_MscVrIpxSapSFltrNode_Type.__name__ = "AsciiString"
_MscVrIpxSapSFltrNode_Object = MibTableColumn
mscVrIpxSapSFltrNode = _MscVrIpxSapSFltrNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1, 4),
    _MscVrIpxSapSFltrNode_Type()
)
mscVrIpxSapSFltrNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrNode.setStatus("mandatory")


class _MscVrIpxSapSFltrDisposition_Type(Integer32):
    """Custom type mscVrIpxSapSFltrDisposition based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("pass", 1))
    )


_MscVrIpxSapSFltrDisposition_Type.__name__ = "Integer32"
_MscVrIpxSapSFltrDisposition_Object = MibTableColumn
mscVrIpxSapSFltrDisposition = _MscVrIpxSapSFltrDisposition_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 10, 1, 5),
    _MscVrIpxSapSFltrDisposition_Type()
)
mscVrIpxSapSFltrDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrDisposition.setStatus("mandatory")
_MscVrIpxSapSFltrOperTable_Object = MibTable
mscVrIpxSapSFltrOperTable = _MscVrIpxSapSFltrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrOperTable.setStatus("mandatory")
_MscVrIpxSapSFltrOperEntry_Object = MibTableRow
mscVrIpxSapSFltrOperEntry = _MscVrIpxSapSFltrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 11, 1)
)
mscVrIpxSapSFltrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrOperEntry.setStatus("mandatory")


class _MscVrIpxSapSFltrNumberOfApplyEntries_Type(Gauge32):
    """Custom type mscVrIpxSapSFltrNumberOfApplyEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpxSapSFltrNumberOfApplyEntries_Type.__name__ = "Gauge32"
_MscVrIpxSapSFltrNumberOfApplyEntries_Object = MibTableColumn
mscVrIpxSapSFltrNumberOfApplyEntries = _MscVrIpxSapSFltrNumberOfApplyEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 2, 11, 1, 1),
    _MscVrIpxSapSFltrNumberOfApplyEntries_Type()
)
mscVrIpxSapSFltrNumberOfApplyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSFltrNumberOfApplyEntries.setStatus("mandatory")
_MscVrIpxSapSapApp_ObjectIdentity = ObjectIdentity
mscVrIpxSapSapApp = _MscVrIpxSapSapApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3)
)
_MscVrIpxSapSapAppRowStatusTable_Object = MibTable
mscVrIpxSapSapAppRowStatusTable = _MscVrIpxSapSapAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppRowStatusTable.setStatus("mandatory")
_MscVrIpxSapSapAppRowStatusEntry_Object = MibTableRow
mscVrIpxSapSapAppRowStatusEntry = _MscVrIpxSapSapAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1)
)
mscVrIpxSapSapAppRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSapAppProtocolPortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSapAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppRowStatusEntry.setStatus("mandatory")
_MscVrIpxSapSapAppRowStatus_Type = RowStatus
_MscVrIpxSapSapAppRowStatus_Object = MibTableColumn
mscVrIpxSapSapAppRowStatus = _MscVrIpxSapSapAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1, 1),
    _MscVrIpxSapSapAppRowStatus_Type()
)
mscVrIpxSapSapAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppRowStatus.setStatus("mandatory")
_MscVrIpxSapSapAppComponentName_Type = DisplayString
_MscVrIpxSapSapAppComponentName_Object = MibTableColumn
mscVrIpxSapSapAppComponentName = _MscVrIpxSapSapAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1, 2),
    _MscVrIpxSapSapAppComponentName_Type()
)
mscVrIpxSapSapAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppComponentName.setStatus("mandatory")
_MscVrIpxSapSapAppStorageType_Type = StorageType
_MscVrIpxSapSapAppStorageType_Object = MibTableColumn
mscVrIpxSapSapAppStorageType = _MscVrIpxSapSapAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1, 4),
    _MscVrIpxSapSapAppStorageType_Type()
)
mscVrIpxSapSapAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppStorageType.setStatus("mandatory")


class _MscVrIpxSapSapAppProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpxSapSapAppProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpxSapSapAppProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpxSapSapAppProtocolPortNameIndex_Object = MibTableColumn
mscVrIpxSapSapAppProtocolPortNameIndex = _MscVrIpxSapSapAppProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1, 10),
    _MscVrIpxSapSapAppProtocolPortNameIndex_Type()
)
mscVrIpxSapSapAppProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppProtocolPortNameIndex.setStatus("mandatory")


class _MscVrIpxSapSapAppFilterIdentifierIndex_Type(Integer32):
    """Custom type mscVrIpxSapSapAppFilterIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrIpxSapSapAppFilterIdentifierIndex_Type.__name__ = "Integer32"
_MscVrIpxSapSapAppFilterIdentifierIndex_Object = MibTableColumn
mscVrIpxSapSapAppFilterIdentifierIndex = _MscVrIpxSapSapAppFilterIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 1, 1, 11),
    _MscVrIpxSapSapAppFilterIdentifierIndex_Type()
)
mscVrIpxSapSapAppFilterIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppFilterIdentifierIndex.setStatus("mandatory")
_MscVrIpxSapSapAppProvTable_Object = MibTable
mscVrIpxSapSapAppProvTable = _MscVrIpxSapSapAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppProvTable.setStatus("mandatory")
_MscVrIpxSapSapAppProvEntry_Object = MibTableRow
mscVrIpxSapSapAppProvEntry = _MscVrIpxSapSapAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 10, 1)
)
mscVrIpxSapSapAppProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSapAppProtocolPortNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapSapAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppProvEntry.setStatus("mandatory")


class _MscVrIpxSapSapAppDirection_Type(Integer32):
    """Custom type mscVrIpxSapSapAppDirection based on Integer32"""
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
        *(("input", 2),
          ("none", 0),
          ("output", 1))
    )


_MscVrIpxSapSapAppDirection_Type.__name__ = "Integer32"
_MscVrIpxSapSapAppDirection_Object = MibTableColumn
mscVrIpxSapSapAppDirection = _MscVrIpxSapSapAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 3, 10, 1, 1),
    _MscVrIpxSapSapAppDirection_Type()
)
mscVrIpxSapSapAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapSapAppDirection.setStatus("mandatory")
_MscVrIpxSapStatsTable_Object = MibTable
mscVrIpxSapStatsTable = _MscVrIpxSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxSapStatsTable.setStatus("mandatory")
_MscVrIpxSapStatsEntry_Object = MibTableRow
mscVrIpxSapStatsEntry = _MscVrIpxSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 10, 1)
)
mscVrIpxSapStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSapIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSapStatsEntry.setStatus("mandatory")
_MscVrIpxSapSapIn_Type = Counter32
_MscVrIpxSapSapIn_Object = MibTableColumn
mscVrIpxSapSapIn = _MscVrIpxSapSapIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 10, 1, 1),
    _MscVrIpxSapSapIn_Type()
)
mscVrIpxSapSapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSapIn.setStatus("mandatory")
_MscVrIpxSapSapOut_Type = Counter32
_MscVrIpxSapSapOut_Object = MibTableColumn
mscVrIpxSapSapOut = _MscVrIpxSapSapOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 10, 1, 2),
    _MscVrIpxSapSapOut_Type()
)
mscVrIpxSapSapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSapOut.setStatus("mandatory")
_MscVrIpxSapSapIncorrectPackets_Type = Counter32
_MscVrIpxSapSapIncorrectPackets_Object = MibTableColumn
mscVrIpxSapSapIncorrectPackets = _MscVrIpxSapSapIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 3, 10, 1, 3),
    _MscVrIpxSapSapIncorrectPackets_Type()
)
mscVrIpxSapSapIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSapSapIncorrectPackets.setStatus("mandatory")
_MscVrIpxFwd_ObjectIdentity = ObjectIdentity
mscVrIpxFwd = _MscVrIpxFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4)
)
_MscVrIpxFwdRowStatusTable_Object = MibTable
mscVrIpxFwdRowStatusTable = _MscVrIpxFwdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxFwdRowStatusTable.setStatus("mandatory")
_MscVrIpxFwdRowStatusEntry_Object = MibTableRow
mscVrIpxFwdRowStatusEntry = _MscVrIpxFwdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1, 1)
)
mscVrIpxFwdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxFwdNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxFwdRowStatusEntry.setStatus("mandatory")
_MscVrIpxFwdRowStatus_Type = RowStatus
_MscVrIpxFwdRowStatus_Object = MibTableColumn
mscVrIpxFwdRowStatus = _MscVrIpxFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1, 1, 1),
    _MscVrIpxFwdRowStatus_Type()
)
mscVrIpxFwdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdRowStatus.setStatus("mandatory")
_MscVrIpxFwdComponentName_Type = DisplayString
_MscVrIpxFwdComponentName_Object = MibTableColumn
mscVrIpxFwdComponentName = _MscVrIpxFwdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1, 1, 2),
    _MscVrIpxFwdComponentName_Type()
)
mscVrIpxFwdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdComponentName.setStatus("mandatory")
_MscVrIpxFwdStorageType_Type = StorageType
_MscVrIpxFwdStorageType_Object = MibTableColumn
mscVrIpxFwdStorageType = _MscVrIpxFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1, 1, 4),
    _MscVrIpxFwdStorageType_Type()
)
mscVrIpxFwdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdStorageType.setStatus("mandatory")


class _MscVrIpxFwdNetworkNumberIndex_Type(DashedHexString):
    """Custom type mscVrIpxFwdNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrIpxFwdNetworkNumberIndex_Type.__name__ = "DashedHexString"
_MscVrIpxFwdNetworkNumberIndex_Object = MibTableColumn
mscVrIpxFwdNetworkNumberIndex = _MscVrIpxFwdNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 1, 1, 10),
    _MscVrIpxFwdNetworkNumberIndex_Type()
)
mscVrIpxFwdNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxFwdNetworkNumberIndex.setStatus("mandatory")
_MscVrIpxFwdOperTable_Object = MibTable
mscVrIpxFwdOperTable = _MscVrIpxFwdOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxFwdOperTable.setStatus("mandatory")
_MscVrIpxFwdOperEntry_Object = MibTableRow
mscVrIpxFwdOperEntry = _MscVrIpxFwdOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1)
)
mscVrIpxFwdOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxFwdNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxFwdOperEntry.setStatus("mandatory")


class _MscVrIpxFwdProtocol_Type(Integer32):
    """Custom type mscVrIpxFwdProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_MscVrIpxFwdProtocol_Type.__name__ = "Integer32"
_MscVrIpxFwdProtocol_Object = MibTableColumn
mscVrIpxFwdProtocol = _MscVrIpxFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 1),
    _MscVrIpxFwdProtocol_Type()
)
mscVrIpxFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdProtocol.setStatus("mandatory")


class _MscVrIpxFwdTicks_Type(Unsigned32):
    """Custom type mscVrIpxFwdTicks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpxFwdTicks_Type.__name__ = "Unsigned32"
_MscVrIpxFwdTicks_Object = MibTableColumn
mscVrIpxFwdTicks = _MscVrIpxFwdTicks_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 2),
    _MscVrIpxFwdTicks_Type()
)
mscVrIpxFwdTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdTicks.setStatus("mandatory")


class _MscVrIpxFwdHopCount_Type(Gauge32):
    """Custom type mscVrIpxFwdHopCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscVrIpxFwdHopCount_Type.__name__ = "Gauge32"
_MscVrIpxFwdHopCount_Object = MibTableColumn
mscVrIpxFwdHopCount = _MscVrIpxFwdHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 3),
    _MscVrIpxFwdHopCount_Type()
)
mscVrIpxFwdHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdHopCount.setStatus("mandatory")


class _MscVrIpxFwdProtocolPortId_Type(AsciiString):
    """Custom type mscVrIpxFwdProtocolPortId based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpxFwdProtocolPortId_Type.__name__ = "AsciiString"
_MscVrIpxFwdProtocolPortId_Object = MibTableColumn
mscVrIpxFwdProtocolPortId = _MscVrIpxFwdProtocolPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 4),
    _MscVrIpxFwdProtocolPortId_Type()
)
mscVrIpxFwdProtocolPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdProtocolPortId.setStatus("mandatory")


class _MscVrIpxFwdNextHopPhysAddress_Type(PhysAddress):
    """Custom type mscVrIpxFwdNextHopPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_MscVrIpxFwdNextHopPhysAddress_Type.__name__ = "PhysAddress"
_MscVrIpxFwdNextHopPhysAddress_Object = MibTableColumn
mscVrIpxFwdNextHopPhysAddress = _MscVrIpxFwdNextHopPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 5),
    _MscVrIpxFwdNextHopPhysAddress_Type()
)
mscVrIpxFwdNextHopPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdNextHopPhysAddress.setStatus("mandatory")


class _MscVrIpxFwdNextHopNetworkNumber_Type(DashedHexString):
    """Custom type mscVrIpxFwdNextHopNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrIpxFwdNextHopNetworkNumber_Type.__name__ = "DashedHexString"
_MscVrIpxFwdNextHopNetworkNumber_Object = MibTableColumn
mscVrIpxFwdNextHopNetworkNumber = _MscVrIpxFwdNextHopNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 4, 10, 1, 6),
    _MscVrIpxFwdNextHopNetworkNumber_Type()
)
mscVrIpxFwdNextHopNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxFwdNextHopNetworkNumber.setStatus("mandatory")
_MscVrIpxSrvc_ObjectIdentity = ObjectIdentity
mscVrIpxSrvc = _MscVrIpxSrvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5)
)
_MscVrIpxSrvcRowStatusTable_Object = MibTable
mscVrIpxSrvcRowStatusTable = _MscVrIpxSrvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxSrvcRowStatusTable.setStatus("mandatory")
_MscVrIpxSrvcRowStatusEntry_Object = MibTableRow
mscVrIpxSrvcRowStatusEntry = _MscVrIpxSrvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1)
)
mscVrIpxSrvcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNetworkNumberIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNameIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSrvcRowStatusEntry.setStatus("mandatory")
_MscVrIpxSrvcRowStatus_Type = RowStatus
_MscVrIpxSrvcRowStatus_Object = MibTableColumn
mscVrIpxSrvcRowStatus = _MscVrIpxSrvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 1),
    _MscVrIpxSrvcRowStatus_Type()
)
mscVrIpxSrvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcRowStatus.setStatus("mandatory")
_MscVrIpxSrvcComponentName_Type = DisplayString
_MscVrIpxSrvcComponentName_Object = MibTableColumn
mscVrIpxSrvcComponentName = _MscVrIpxSrvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 2),
    _MscVrIpxSrvcComponentName_Type()
)
mscVrIpxSrvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcComponentName.setStatus("mandatory")
_MscVrIpxSrvcStorageType_Type = StorageType
_MscVrIpxSrvcStorageType_Object = MibTableColumn
mscVrIpxSrvcStorageType = _MscVrIpxSrvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 4),
    _MscVrIpxSrvcStorageType_Type()
)
mscVrIpxSrvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcStorageType.setStatus("mandatory")


class _MscVrIpxSrvcNetworkNumberIndex_Type(DashedHexString):
    """Custom type mscVrIpxSrvcNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrIpxSrvcNetworkNumberIndex_Type.__name__ = "DashedHexString"
_MscVrIpxSrvcNetworkNumberIndex_Object = MibTableColumn
mscVrIpxSrvcNetworkNumberIndex = _MscVrIpxSrvcNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 10),
    _MscVrIpxSrvcNetworkNumberIndex_Type()
)
mscVrIpxSrvcNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSrvcNetworkNumberIndex.setStatus("mandatory")


class _MscVrIpxSrvcNodeIndex_Type(DashedHexString):
    """Custom type mscVrIpxSrvcNodeIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_MscVrIpxSrvcNodeIndex_Type.__name__ = "DashedHexString"
_MscVrIpxSrvcNodeIndex_Object = MibTableColumn
mscVrIpxSrvcNodeIndex = _MscVrIpxSrvcNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 11),
    _MscVrIpxSrvcNodeIndex_Type()
)
mscVrIpxSrvcNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSrvcNodeIndex.setStatus("mandatory")


class _MscVrIpxSrvcTypeIndex_Type(Integer32):
    """Custom type mscVrIpxSrvcTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpxSrvcTypeIndex_Type.__name__ = "Integer32"
_MscVrIpxSrvcTypeIndex_Object = MibTableColumn
mscVrIpxSrvcTypeIndex = _MscVrIpxSrvcTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 12),
    _MscVrIpxSrvcTypeIndex_Type()
)
mscVrIpxSrvcTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSrvcTypeIndex.setStatus("mandatory")


class _MscVrIpxSrvcNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpxSrvcNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_MscVrIpxSrvcNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpxSrvcNameIndex_Object = MibTableColumn
mscVrIpxSrvcNameIndex = _MscVrIpxSrvcNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 1, 1, 13),
    _MscVrIpxSrvcNameIndex_Type()
)
mscVrIpxSrvcNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxSrvcNameIndex.setStatus("mandatory")
_MscVrIpxSrvcOperTable_Object = MibTable
mscVrIpxSrvcOperTable = _MscVrIpxSrvcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxSrvcOperTable.setStatus("mandatory")
_MscVrIpxSrvcOperEntry_Object = MibTableRow
mscVrIpxSrvcOperEntry = _MscVrIpxSrvcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 10, 1)
)
mscVrIpxSrvcOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNetworkNumberIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNodeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcTypeIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxSrvcNameIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxSrvcOperEntry.setStatus("mandatory")


class _MscVrIpxSrvcSocket_Type(Hex):
    """Custom type mscVrIpxSrvcSocket based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpxSrvcSocket_Type.__name__ = "Hex"
_MscVrIpxSrvcSocket_Object = MibTableColumn
mscVrIpxSrvcSocket = _MscVrIpxSrvcSocket_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 10, 1, 1),
    _MscVrIpxSrvcSocket_Type()
)
mscVrIpxSrvcSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcSocket.setStatus("mandatory")


class _MscVrIpxSrvcProtocol_Type(Integer32):
    """Custom type mscVrIpxSrvcProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_MscVrIpxSrvcProtocol_Type.__name__ = "Integer32"
_MscVrIpxSrvcProtocol_Object = MibTableColumn
mscVrIpxSrvcProtocol = _MscVrIpxSrvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 10, 1, 2),
    _MscVrIpxSrvcProtocol_Type()
)
mscVrIpxSrvcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcProtocol.setStatus("mandatory")


class _MscVrIpxSrvcHopCount_Type(Gauge32):
    """Custom type mscVrIpxSrvcHopCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_MscVrIpxSrvcHopCount_Type.__name__ = "Gauge32"
_MscVrIpxSrvcHopCount_Object = MibTableColumn
mscVrIpxSrvcHopCount = _MscVrIpxSrvcHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 5, 10, 1, 3),
    _MscVrIpxSrvcHopCount_Type()
)
mscVrIpxSrvcHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSrvcHopCount.setStatus("mandatory")
_MscVrIpxAdj_ObjectIdentity = ObjectIdentity
mscVrIpxAdj = _MscVrIpxAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6)
)
_MscVrIpxAdjRowStatusTable_Object = MibTable
mscVrIpxAdjRowStatusTable = _MscVrIpxAdjRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxAdjRowStatusTable.setStatus("mandatory")
_MscVrIpxAdjRowStatusEntry_Object = MibTableRow
mscVrIpxAdjRowStatusEntry = _MscVrIpxAdjRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1)
)
mscVrIpxAdjRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxAdjProtocolPortIdentifierIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxAdjNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxAdjRowStatusEntry.setStatus("mandatory")
_MscVrIpxAdjRowStatus_Type = RowStatus
_MscVrIpxAdjRowStatus_Object = MibTableColumn
mscVrIpxAdjRowStatus = _MscVrIpxAdjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1, 1),
    _MscVrIpxAdjRowStatus_Type()
)
mscVrIpxAdjRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdjRowStatus.setStatus("mandatory")
_MscVrIpxAdjComponentName_Type = DisplayString
_MscVrIpxAdjComponentName_Object = MibTableColumn
mscVrIpxAdjComponentName = _MscVrIpxAdjComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1, 2),
    _MscVrIpxAdjComponentName_Type()
)
mscVrIpxAdjComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdjComponentName.setStatus("mandatory")
_MscVrIpxAdjStorageType_Type = StorageType
_MscVrIpxAdjStorageType_Object = MibTableColumn
mscVrIpxAdjStorageType = _MscVrIpxAdjStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1, 4),
    _MscVrIpxAdjStorageType_Type()
)
mscVrIpxAdjStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdjStorageType.setStatus("mandatory")


class _MscVrIpxAdjProtocolPortIdentifierIndex_Type(AsciiStringIndex):
    """Custom type mscVrIpxAdjProtocolPortIdentifierIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MscVrIpxAdjProtocolPortIdentifierIndex_Type.__name__ = "AsciiStringIndex"
_MscVrIpxAdjProtocolPortIdentifierIndex_Object = MibTableColumn
mscVrIpxAdjProtocolPortIdentifierIndex = _MscVrIpxAdjProtocolPortIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1, 10),
    _MscVrIpxAdjProtocolPortIdentifierIndex_Type()
)
mscVrIpxAdjProtocolPortIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxAdjProtocolPortIdentifierIndex.setStatus("mandatory")


class _MscVrIpxAdjNetworkNumberIndex_Type(DashedHexString):
    """Custom type mscVrIpxAdjNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrIpxAdjNetworkNumberIndex_Type.__name__ = "DashedHexString"
_MscVrIpxAdjNetworkNumberIndex_Object = MibTableColumn
mscVrIpxAdjNetworkNumberIndex = _MscVrIpxAdjNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 1, 1, 11),
    _MscVrIpxAdjNetworkNumberIndex_Type()
)
mscVrIpxAdjNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxAdjNetworkNumberIndex.setStatus("mandatory")
_MscVrIpxAdjOperTable_Object = MibTable
mscVrIpxAdjOperTable = _MscVrIpxAdjOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxAdjOperTable.setStatus("mandatory")
_MscVrIpxAdjOperEntry_Object = MibTableRow
mscVrIpxAdjOperEntry = _MscVrIpxAdjOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 10, 1)
)
mscVrIpxAdjOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxAdjProtocolPortIdentifierIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxAdjNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxAdjOperEntry.setStatus("mandatory")


class _MscVrIpxAdjPhysAddress_Type(PhysAddress):
    """Custom type mscVrIpxAdjPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_MscVrIpxAdjPhysAddress_Type.__name__ = "PhysAddress"
_MscVrIpxAdjPhysAddress_Object = MibTableColumn
mscVrIpxAdjPhysAddress = _MscVrIpxAdjPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 10, 1, 1),
    _MscVrIpxAdjPhysAddress_Type()
)
mscVrIpxAdjPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdjPhysAddress.setStatus("mandatory")


class _MscVrIpxAdjAdjacencyState_Type(Integer32):
    """Custom type mscVrIpxAdjAdjacencyState based on Integer32"""
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
        *(("down", 4),
          ("failed", 3),
          ("initializing", 1),
          ("up", 2))
    )


_MscVrIpxAdjAdjacencyState_Type.__name__ = "Integer32"
_MscVrIpxAdjAdjacencyState_Object = MibTableColumn
mscVrIpxAdjAdjacencyState = _MscVrIpxAdjAdjacencyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 6, 10, 1, 2),
    _MscVrIpxAdjAdjacencyState_Type()
)
mscVrIpxAdjAdjacencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdjAdjacencyState.setStatus("mandatory")
_MscVrIpxNs_ObjectIdentity = ObjectIdentity
mscVrIpxNs = _MscVrIpxNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7)
)
_MscVrIpxNsRowStatusTable_Object = MibTable
mscVrIpxNsRowStatusTable = _MscVrIpxNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxNsRowStatusTable.setStatus("mandatory")
_MscVrIpxNsRowStatusEntry_Object = MibTableRow
mscVrIpxNsRowStatusEntry = _MscVrIpxNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1, 1)
)
mscVrIpxNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxNsRowStatusEntry.setStatus("mandatory")
_MscVrIpxNsRowStatus_Type = RowStatus
_MscVrIpxNsRowStatus_Object = MibTableColumn
mscVrIpxNsRowStatus = _MscVrIpxNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1, 1, 1),
    _MscVrIpxNsRowStatus_Type()
)
mscVrIpxNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsRowStatus.setStatus("mandatory")
_MscVrIpxNsComponentName_Type = DisplayString
_MscVrIpxNsComponentName_Object = MibTableColumn
mscVrIpxNsComponentName = _MscVrIpxNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1, 1, 2),
    _MscVrIpxNsComponentName_Type()
)
mscVrIpxNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxNsComponentName.setStatus("mandatory")
_MscVrIpxNsStorageType_Type = StorageType
_MscVrIpxNsStorageType_Object = MibTableColumn
mscVrIpxNsStorageType = _MscVrIpxNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1, 1, 4),
    _MscVrIpxNsStorageType_Type()
)
mscVrIpxNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxNsStorageType.setStatus("mandatory")
_MscVrIpxNsIndex_Type = NonReplicated
_MscVrIpxNsIndex_Object = MibTableColumn
mscVrIpxNsIndex = _MscVrIpxNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 1, 1, 10),
    _MscVrIpxNsIndex_Type()
)
mscVrIpxNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxNsIndex.setStatus("mandatory")
_MscVrIpxNsNetSentryApp_ObjectIdentity = ObjectIdentity
mscVrIpxNsNetSentryApp = _MscVrIpxNsNetSentryApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2)
)
_MscVrIpxNsNetSentryAppRowStatusTable_Object = MibTable
mscVrIpxNsNetSentryAppRowStatusTable = _MscVrIpxNsNetSentryAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppRowStatusTable.setStatus("mandatory")
_MscVrIpxNsNetSentryAppRowStatusEntry_Object = MibTableRow
mscVrIpxNsNetSentryAppRowStatusEntry = _MscVrIpxNsNetSentryAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1, 1)
)
mscVrIpxNsNetSentryAppRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsNetSentryAppEntryIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppRowStatusEntry.setStatus("mandatory")
_MscVrIpxNsNetSentryAppRowStatus_Type = RowStatus
_MscVrIpxNsNetSentryAppRowStatus_Object = MibTableColumn
mscVrIpxNsNetSentryAppRowStatus = _MscVrIpxNsNetSentryAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1, 1, 1),
    _MscVrIpxNsNetSentryAppRowStatus_Type()
)
mscVrIpxNsNetSentryAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppRowStatus.setStatus("mandatory")
_MscVrIpxNsNetSentryAppComponentName_Type = DisplayString
_MscVrIpxNsNetSentryAppComponentName_Object = MibTableColumn
mscVrIpxNsNetSentryAppComponentName = _MscVrIpxNsNetSentryAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1, 1, 2),
    _MscVrIpxNsNetSentryAppComponentName_Type()
)
mscVrIpxNsNetSentryAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppComponentName.setStatus("mandatory")
_MscVrIpxNsNetSentryAppStorageType_Type = StorageType
_MscVrIpxNsNetSentryAppStorageType_Object = MibTableColumn
mscVrIpxNsNetSentryAppStorageType = _MscVrIpxNsNetSentryAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1, 1, 4),
    _MscVrIpxNsNetSentryAppStorageType_Type()
)
mscVrIpxNsNetSentryAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppStorageType.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppEntryIndex_Type(Integer32):
    """Custom type mscVrIpxNsNetSentryAppEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_MscVrIpxNsNetSentryAppEntryIndex_Type.__name__ = "Integer32"
_MscVrIpxNsNetSentryAppEntryIndex_Object = MibTableColumn
mscVrIpxNsNetSentryAppEntryIndex = _MscVrIpxNsNetSentryAppEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 1, 1, 10),
    _MscVrIpxNsNetSentryAppEntryIndex_Type()
)
mscVrIpxNsNetSentryAppEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppEntryIndex.setStatus("mandatory")
_MscVrIpxNsNetSentryAppProvTable_Object = MibTable
mscVrIpxNsNetSentryAppProvTable = _MscVrIpxNsNetSentryAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppProvTable.setStatus("mandatory")
_MscVrIpxNsNetSentryAppProvEntry_Object = MibTableRow
mscVrIpxNsNetSentryAppProvEntry = _MscVrIpxNsNetSentryAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1)
)
mscVrIpxNsNetSentryAppProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsNetSentryAppEntryIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppProvEntry.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppFilter_Type(AsciiString):
    """Custom type mscVrIpxNsNetSentryAppFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpxNsNetSentryAppFilter_Type.__name__ = "AsciiString"
_MscVrIpxNsNetSentryAppFilter_Object = MibTableColumn
mscVrIpxNsNetSentryAppFilter = _MscVrIpxNsNetSentryAppFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 1),
    _MscVrIpxNsNetSentryAppFilter_Type()
)
mscVrIpxNsNetSentryAppFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppFilter.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppNetworkNumber1_Type(AsciiString):
    """Custom type mscVrIpxNsNetSentryAppNetworkNumber1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_MscVrIpxNsNetSentryAppNetworkNumber1_Type.__name__ = "AsciiString"
_MscVrIpxNsNetSentryAppNetworkNumber1_Object = MibTableColumn
mscVrIpxNsNetSentryAppNetworkNumber1 = _MscVrIpxNsNetSentryAppNetworkNumber1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 2),
    _MscVrIpxNsNetSentryAppNetworkNumber1_Type()
)
mscVrIpxNsNetSentryAppNetworkNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppNetworkNumber1.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppNode1_Type(AsciiString):
    """Custom type mscVrIpxNsNetSentryAppNode1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscVrIpxNsNetSentryAppNode1_Type.__name__ = "AsciiString"
_MscVrIpxNsNetSentryAppNode1_Object = MibTableColumn
mscVrIpxNsNetSentryAppNode1 = _MscVrIpxNsNetSentryAppNode1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 3),
    _MscVrIpxNsNetSentryAppNode1_Type()
)
mscVrIpxNsNetSentryAppNode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppNode1.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppDirection_Type(Integer32):
    """Custom type mscVrIpxNsNetSentryAppDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("from", 2),
          ("to", 1),
          ("tofrom", 3))
    )


_MscVrIpxNsNetSentryAppDirection_Type.__name__ = "Integer32"
_MscVrIpxNsNetSentryAppDirection_Object = MibTableColumn
mscVrIpxNsNetSentryAppDirection = _MscVrIpxNsNetSentryAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 4),
    _MscVrIpxNsNetSentryAppDirection_Type()
)
mscVrIpxNsNetSentryAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppDirection.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppNetworkNumber2_Type(AsciiString):
    """Custom type mscVrIpxNsNetSentryAppNetworkNumber2 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_MscVrIpxNsNetSentryAppNetworkNumber2_Type.__name__ = "AsciiString"
_MscVrIpxNsNetSentryAppNetworkNumber2_Object = MibTableColumn
mscVrIpxNsNetSentryAppNetworkNumber2 = _MscVrIpxNsNetSentryAppNetworkNumber2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 5),
    _MscVrIpxNsNetSentryAppNetworkNumber2_Type()
)
mscVrIpxNsNetSentryAppNetworkNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppNetworkNumber2.setStatus("mandatory")


class _MscVrIpxNsNetSentryAppNode2_Type(AsciiString):
    """Custom type mscVrIpxNsNetSentryAppNode2 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MscVrIpxNsNetSentryAppNode2_Type.__name__ = "AsciiString"
_MscVrIpxNsNetSentryAppNode2_Object = MibTableColumn
mscVrIpxNsNetSentryAppNode2 = _MscVrIpxNsNetSentryAppNode2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 2, 10, 1, 6),
    _MscVrIpxNsNetSentryAppNode2_Type()
)
mscVrIpxNsNetSentryAppNode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsNetSentryAppNode2.setStatus("mandatory")
_MscVrIpxNsProvTable_Object = MibTable
mscVrIpxNsProvTable = _MscVrIpxNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10)
)
if mibBuilder.loadTexts:
    mscVrIpxNsProvTable.setStatus("mandatory")
_MscVrIpxNsProvEntry_Object = MibTableRow
mscVrIpxNsProvEntry = _MscVrIpxNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10, 1)
)
mscVrIpxNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxNsProvEntry.setStatus("mandatory")


class _MscVrIpxNsFirstFilter_Type(AsciiString):
    """Custom type mscVrIpxNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpxNsFirstFilter_Type.__name__ = "AsciiString"
_MscVrIpxNsFirstFilter_Object = MibTableColumn
mscVrIpxNsFirstFilter = _MscVrIpxNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10, 1, 1),
    _MscVrIpxNsFirstFilter_Type()
)
mscVrIpxNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsFirstFilter.setStatus("mandatory")


class _MscVrIpxNsLastFilter_Type(AsciiString):
    """Custom type mscVrIpxNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpxNsLastFilter_Type.__name__ = "AsciiString"
_MscVrIpxNsLastFilter_Object = MibTableColumn
mscVrIpxNsLastFilter = _MscVrIpxNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10, 1, 2),
    _MscVrIpxNsLastFilter_Type()
)
mscVrIpxNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsLastFilter.setStatus("mandatory")


class _MscVrIpxNsLocalInFilter_Type(AsciiString):
    """Custom type mscVrIpxNsLocalInFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpxNsLocalInFilter_Type.__name__ = "AsciiString"
_MscVrIpxNsLocalInFilter_Object = MibTableColumn
mscVrIpxNsLocalInFilter = _MscVrIpxNsLocalInFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10, 1, 3),
    _MscVrIpxNsLocalInFilter_Type()
)
mscVrIpxNsLocalInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsLocalInFilter.setStatus("mandatory")


class _MscVrIpxNsLocalOutFilter_Type(AsciiString):
    """Custom type mscVrIpxNsLocalOutFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVrIpxNsLocalOutFilter_Type.__name__ = "AsciiString"
_MscVrIpxNsLocalOutFilter_Object = MibTableColumn
mscVrIpxNsLocalOutFilter = _MscVrIpxNsLocalOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 7, 10, 1, 4),
    _MscVrIpxNsLocalOutFilter_Type()
)
mscVrIpxNsLocalOutFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNsLocalOutFilter.setStatus("mandatory")
_MscVrIpxAdminControlTable_Object = MibTable
mscVrIpxAdminControlTable = _MscVrIpxAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 100)
)
if mibBuilder.loadTexts:
    mscVrIpxAdminControlTable.setStatus("mandatory")
_MscVrIpxAdminControlEntry_Object = MibTableRow
mscVrIpxAdminControlEntry = _MscVrIpxAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 100, 1)
)
mscVrIpxAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxAdminControlEntry.setStatus("mandatory")


class _MscVrIpxSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpxSnmpAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpxSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpxSnmpAdminStatus_Object = MibTableColumn
mscVrIpxSnmpAdminStatus = _MscVrIpxSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 100, 1, 1),
    _MscVrIpxSnmpAdminStatus_Type()
)
mscVrIpxSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSnmpAdminStatus.setStatus("mandatory")
_MscVrIpxProvTable_Object = MibTable
mscVrIpxProvTable = _MscVrIpxProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101)
)
if mibBuilder.loadTexts:
    mscVrIpxProvTable.setStatus("mandatory")
_MscVrIpxProvEntry_Object = MibTableRow
mscVrIpxProvEntry = _MscVrIpxProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1)
)
mscVrIpxProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxProvEntry.setStatus("mandatory")


class _MscVrIpxNetworkNumber_Type(DashedHexString):
    """Custom type mscVrIpxNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_MscVrIpxNetworkNumber_Type.__name__ = "DashedHexString"
_MscVrIpxNetworkNumber_Object = MibTableColumn
mscVrIpxNetworkNumber = _MscVrIpxNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 1),
    _MscVrIpxNetworkNumber_Type()
)
mscVrIpxNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxNetworkNumber.setStatus("mandatory")


class _MscVrIpxMaxPathSplits_Type(Unsigned32):
    """Custom type mscVrIpxMaxPathSplits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MscVrIpxMaxPathSplits_Type.__name__ = "Unsigned32"
_MscVrIpxMaxPathSplits_Object = MibTableColumn
mscVrIpxMaxPathSplits = _MscVrIpxMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 2),
    _MscVrIpxMaxPathSplits_Type()
)
mscVrIpxMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxMaxPathSplits.setStatus("mandatory")


class _MscVrIpxMaxHops_Type(Unsigned32):
    """Custom type mscVrIpxMaxHops based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MscVrIpxMaxHops_Type.__name__ = "Unsigned32"
_MscVrIpxMaxHops_Object = MibTableColumn
mscVrIpxMaxHops = _MscVrIpxMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 3),
    _MscVrIpxMaxHops_Type()
)
mscVrIpxMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxMaxHops.setStatus("mandatory")


class _MscVrIpxRipUpdateInterval_Type(Unsigned32):
    """Custom type mscVrIpxRipUpdateInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVrIpxRipUpdateInterval_Type.__name__ = "Unsigned32"
_MscVrIpxRipUpdateInterval_Object = MibTableColumn
mscVrIpxRipUpdateInterval = _MscVrIpxRipUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 4),
    _MscVrIpxRipUpdateInterval_Type()
)
mscVrIpxRipUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipUpdateInterval.setStatus("mandatory")


class _MscVrIpxSapUpdateInterval_Type(Unsigned32):
    """Custom type mscVrIpxSapUpdateInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVrIpxSapUpdateInterval_Type.__name__ = "Unsigned32"
_MscVrIpxSapUpdateInterval_Object = MibTableColumn
mscVrIpxSapUpdateInterval = _MscVrIpxSapUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 5),
    _MscVrIpxSapUpdateInterval_Type()
)
mscVrIpxSapUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapUpdateInterval.setStatus("mandatory")


class _MscVrIpxControlDelay_Type(Unsigned32):
    """Custom type mscVrIpxControlDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscVrIpxControlDelay_Type.__name__ = "Unsigned32"
_MscVrIpxControlDelay_Object = MibTableColumn
mscVrIpxControlDelay = _MscVrIpxControlDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 6),
    _MscVrIpxControlDelay_Type()
)
mscVrIpxControlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxControlDelay.setStatus("mandatory")


class _MscVrIpxUpdateDelay_Type(Unsigned32):
    """Custom type mscVrIpxUpdateDelay based on Unsigned32"""
    defaultValue = 55

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55, 500),
    )


_MscVrIpxUpdateDelay_Type.__name__ = "Unsigned32"
_MscVrIpxUpdateDelay_Object = MibTableColumn
mscVrIpxUpdateDelay = _MscVrIpxUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 7),
    _MscVrIpxUpdateDelay_Type()
)
mscVrIpxUpdateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxUpdateDelay.setStatus("mandatory")


class _MscVrIpxRipAgeMultiplier_Type(Unsigned32):
    """Custom type mscVrIpxRipAgeMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscVrIpxRipAgeMultiplier_Type.__name__ = "Unsigned32"
_MscVrIpxRipAgeMultiplier_Object = MibTableColumn
mscVrIpxRipAgeMultiplier = _MscVrIpxRipAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 8),
    _MscVrIpxRipAgeMultiplier_Type()
)
mscVrIpxRipAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipAgeMultiplier.setStatus("mandatory")


class _MscVrIpxSapAgeMultiplier_Type(Unsigned32):
    """Custom type mscVrIpxSapAgeMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscVrIpxSapAgeMultiplier_Type.__name__ = "Unsigned32"
_MscVrIpxSapAgeMultiplier_Object = MibTableColumn
mscVrIpxSapAgeMultiplier = _MscVrIpxSapAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 9),
    _MscVrIpxSapAgeMultiplier_Type()
)
mscVrIpxSapAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapAgeMultiplier.setStatus("mandatory")


class _MscVrIpxDamping_Type(Integer32):
    """Custom type mscVrIpxDamping based on Integer32"""
    defaultValue = 1

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


_MscVrIpxDamping_Type.__name__ = "Integer32"
_MscVrIpxDamping_Object = MibTableColumn
mscVrIpxDamping = _MscVrIpxDamping_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 10),
    _MscVrIpxDamping_Type()
)
mscVrIpxDamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxDamping.setStatus("mandatory")


class _MscVrIpxRipMaxDampedGeneralRequests_Type(Unsigned32):
    """Custom type mscVrIpxRipMaxDampedGeneralRequests based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscVrIpxRipMaxDampedGeneralRequests_Type.__name__ = "Unsigned32"
_MscVrIpxRipMaxDampedGeneralRequests_Object = MibTableColumn
mscVrIpxRipMaxDampedGeneralRequests = _MscVrIpxRipMaxDampedGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 11),
    _MscVrIpxRipMaxDampedGeneralRequests_Type()
)
mscVrIpxRipMaxDampedGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipMaxDampedGeneralRequests.setStatus("mandatory")


class _MscVrIpxRipMaxDampedSpecificRequests_Type(Unsigned32):
    """Custom type mscVrIpxRipMaxDampedSpecificRequests based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscVrIpxRipMaxDampedSpecificRequests_Type.__name__ = "Unsigned32"
_MscVrIpxRipMaxDampedSpecificRequests_Object = MibTableColumn
mscVrIpxRipMaxDampedSpecificRequests = _MscVrIpxRipMaxDampedSpecificRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 12),
    _MscVrIpxRipMaxDampedSpecificRequests_Type()
)
mscVrIpxRipMaxDampedSpecificRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxRipMaxDampedSpecificRequests.setStatus("mandatory")


class _MscVrIpxSapMaxDampedGeneralRequests_Type(Unsigned32):
    """Custom type mscVrIpxSapMaxDampedGeneralRequests based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscVrIpxSapMaxDampedGeneralRequests_Type.__name__ = "Unsigned32"
_MscVrIpxSapMaxDampedGeneralRequests_Object = MibTableColumn
mscVrIpxSapMaxDampedGeneralRequests = _MscVrIpxSapMaxDampedGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 13),
    _MscVrIpxSapMaxDampedGeneralRequests_Type()
)
mscVrIpxSapMaxDampedGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapMaxDampedGeneralRequests.setStatus("mandatory")


class _MscVrIpxSapMaxDampedSpecificRequests_Type(Unsigned32):
    """Custom type mscVrIpxSapMaxDampedSpecificRequests based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscVrIpxSapMaxDampedSpecificRequests_Type.__name__ = "Unsigned32"
_MscVrIpxSapMaxDampedSpecificRequests_Object = MibTableColumn
mscVrIpxSapMaxDampedSpecificRequests = _MscVrIpxSapMaxDampedSpecificRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 14),
    _MscVrIpxSapMaxDampedSpecificRequests_Type()
)
mscVrIpxSapMaxDampedSpecificRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxSapMaxDampedSpecificRequests.setStatus("mandatory")


class _MscVrIpxInitialGeneralRequests_Type(Integer32):
    """Custom type mscVrIpxInitialGeneralRequests based on Integer32"""
    defaultValue = 1

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


_MscVrIpxInitialGeneralRequests_Type.__name__ = "Integer32"
_MscVrIpxInitialGeneralRequests_Object = MibTableColumn
mscVrIpxInitialGeneralRequests = _MscVrIpxInitialGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 15),
    _MscVrIpxInitialGeneralRequests_Type()
)
mscVrIpxInitialGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxInitialGeneralRequests.setStatus("mandatory")


class _MscVrIpxHoldDownInterval_Type(Unsigned32):
    """Custom type mscVrIpxHoldDownInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpxHoldDownInterval_Type.__name__ = "Unsigned32"
_MscVrIpxHoldDownInterval_Object = MibTableColumn
mscVrIpxHoldDownInterval = _MscVrIpxHoldDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 101, 1, 16),
    _MscVrIpxHoldDownInterval_Type()
)
mscVrIpxHoldDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpxHoldDownInterval.setStatus("mandatory")
_MscVrIpxStateTable_Object = MibTable
mscVrIpxStateTable = _MscVrIpxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 103)
)
if mibBuilder.loadTexts:
    mscVrIpxStateTable.setStatus("mandatory")
_MscVrIpxStateEntry_Object = MibTableRow
mscVrIpxStateEntry = _MscVrIpxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 103, 1)
)
mscVrIpxStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxStateEntry.setStatus("mandatory")


class _MscVrIpxAdminState_Type(Integer32):
    """Custom type mscVrIpxAdminState based on Integer32"""
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


_MscVrIpxAdminState_Type.__name__ = "Integer32"
_MscVrIpxAdminState_Object = MibTableColumn
mscVrIpxAdminState = _MscVrIpxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 103, 1, 1),
    _MscVrIpxAdminState_Type()
)
mscVrIpxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxAdminState.setStatus("mandatory")


class _MscVrIpxOperationalState_Type(Integer32):
    """Custom type mscVrIpxOperationalState based on Integer32"""
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


_MscVrIpxOperationalState_Type.__name__ = "Integer32"
_MscVrIpxOperationalState_Object = MibTableColumn
mscVrIpxOperationalState = _MscVrIpxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 103, 1, 2),
    _MscVrIpxOperationalState_Type()
)
mscVrIpxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOperationalState.setStatus("mandatory")


class _MscVrIpxUsageState_Type(Integer32):
    """Custom type mscVrIpxUsageState based on Integer32"""
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


_MscVrIpxUsageState_Type.__name__ = "Integer32"
_MscVrIpxUsageState_Object = MibTableColumn
mscVrIpxUsageState = _MscVrIpxUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 103, 1, 3),
    _MscVrIpxUsageState_Type()
)
mscVrIpxUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxUsageState.setStatus("mandatory")
_MscVrIpxOperStatusTable_Object = MibTable
mscVrIpxOperStatusTable = _MscVrIpxOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 104)
)
if mibBuilder.loadTexts:
    mscVrIpxOperStatusTable.setStatus("mandatory")
_MscVrIpxOperStatusEntry_Object = MibTableRow
mscVrIpxOperStatusEntry = _MscVrIpxOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 104, 1)
)
mscVrIpxOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxOperStatusEntry.setStatus("mandatory")


class _MscVrIpxSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpxSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpxSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpxSnmpOperStatus_Object = MibTableColumn
mscVrIpxSnmpOperStatus = _MscVrIpxSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 104, 1, 1),
    _MscVrIpxSnmpOperStatus_Type()
)
mscVrIpxSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxSnmpOperStatus.setStatus("mandatory")
_MscVrIpxOperTable_Object = MibTable
mscVrIpxOperTable = _MscVrIpxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 105)
)
if mibBuilder.loadTexts:
    mscVrIpxOperTable.setStatus("mandatory")
_MscVrIpxOperEntry_Object = MibTableRow
mscVrIpxOperEntry = _MscVrIpxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 105, 1)
)
mscVrIpxOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxOperEntry.setStatus("mandatory")


class _MscVrIpxProtocolPortCount_Type(Unsigned32):
    """Custom type mscVrIpxProtocolPortCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpxProtocolPortCount_Type.__name__ = "Unsigned32"
_MscVrIpxProtocolPortCount_Object = MibTableColumn
mscVrIpxProtocolPortCount = _MscVrIpxProtocolPortCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 105, 1, 1),
    _MscVrIpxProtocolPortCount_Type()
)
mscVrIpxProtocolPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxProtocolPortCount.setStatus("mandatory")


class _MscVrIpxDestinationCount_Type(Unsigned32):
    """Custom type mscVrIpxDestinationCount based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpxDestinationCount_Type.__name__ = "Unsigned32"
_MscVrIpxDestinationCount_Object = MibTableColumn
mscVrIpxDestinationCount = _MscVrIpxDestinationCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 105, 1, 2),
    _MscVrIpxDestinationCount_Type()
)
mscVrIpxDestinationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxDestinationCount.setStatus("mandatory")


class _MscVrIpxServicesCount_Type(Unsigned32):
    """Custom type mscVrIpxServicesCount based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpxServicesCount_Type.__name__ = "Unsigned32"
_MscVrIpxServicesCount_Object = MibTableColumn
mscVrIpxServicesCount = _MscVrIpxServicesCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 105, 1, 3),
    _MscVrIpxServicesCount_Type()
)
mscVrIpxServicesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxServicesCount.setStatus("mandatory")
_MscVrIpxStatsTable_Object = MibTable
mscVrIpxStatsTable = _MscVrIpxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107)
)
if mibBuilder.loadTexts:
    mscVrIpxStatsTable.setStatus("mandatory")
_MscVrIpxStatsEntry_Object = MibTableRow
mscVrIpxStatsEntry = _MscVrIpxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1)
)
mscVrIpxStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpxMIB", "mscVrIpxIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpxStatsEntry.setStatus("mandatory")
_MscVrIpxInReceives_Type = Counter32
_MscVrIpxInReceives_Object = MibTableColumn
mscVrIpxInReceives = _MscVrIpxInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 1),
    _MscVrIpxInReceives_Type()
)
mscVrIpxInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInReceives.setStatus("mandatory")
_MscVrIpxInHeaderErrors_Type = Counter32
_MscVrIpxInHeaderErrors_Object = MibTableColumn
mscVrIpxInHeaderErrors = _MscVrIpxInHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 2),
    _MscVrIpxInHeaderErrors_Type()
)
mscVrIpxInHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInHeaderErrors.setStatus("mandatory")
_MscVrIpxInUnknownSocket_Type = Counter32
_MscVrIpxInUnknownSocket_Object = MibTableColumn
mscVrIpxInUnknownSocket = _MscVrIpxInUnknownSocket_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 3),
    _MscVrIpxInUnknownSocket_Type()
)
mscVrIpxInUnknownSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInUnknownSocket.setStatus("mandatory")
_MscVrIpxInDiscards_Type = Counter32
_MscVrIpxInDiscards_Object = MibTableColumn
mscVrIpxInDiscards = _MscVrIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 4),
    _MscVrIpxInDiscards_Type()
)
mscVrIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInDiscards.setStatus("mandatory")
_MscVrIpxInBadChecksums_Type = Counter32
_MscVrIpxInBadChecksums_Object = MibTableColumn
mscVrIpxInBadChecksums = _MscVrIpxInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 5),
    _MscVrIpxInBadChecksums_Type()
)
mscVrIpxInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInBadChecksums.setStatus("mandatory")
_MscVrIpxInDelivers_Type = Counter32
_MscVrIpxInDelivers_Object = MibTableColumn
mscVrIpxInDelivers = _MscVrIpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 6),
    _MscVrIpxInDelivers_Type()
)
mscVrIpxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInDelivers.setStatus("mandatory")
_MscVrIpxNoRoutes_Type = Counter32
_MscVrIpxNoRoutes_Object = MibTableColumn
mscVrIpxNoRoutes = _MscVrIpxNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 7),
    _MscVrIpxNoRoutes_Type()
)
mscVrIpxNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxNoRoutes.setStatus("mandatory")
_MscVrIpxOutRequests_Type = Counter32
_MscVrIpxOutRequests_Object = MibTableColumn
mscVrIpxOutRequests = _MscVrIpxOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 8),
    _MscVrIpxOutRequests_Type()
)
mscVrIpxOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOutRequests.setStatus("mandatory")
_MscVrIpxOutMalformedRequests_Type = Counter32
_MscVrIpxOutMalformedRequests_Object = MibTableColumn
mscVrIpxOutMalformedRequests = _MscVrIpxOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 9),
    _MscVrIpxOutMalformedRequests_Type()
)
mscVrIpxOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOutMalformedRequests.setStatus("mandatory")
_MscVrIpxOutDiscards_Type = Counter32
_MscVrIpxOutDiscards_Object = MibTableColumn
mscVrIpxOutDiscards = _MscVrIpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 10),
    _MscVrIpxOutDiscards_Type()
)
mscVrIpxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOutDiscards.setStatus("mandatory")
_MscVrIpxOutPackets_Type = Counter32
_MscVrIpxOutPackets_Object = MibTableColumn
mscVrIpxOutPackets = _MscVrIpxOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 11),
    _MscVrIpxOutPackets_Type()
)
mscVrIpxOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOutPackets.setStatus("mandatory")
_MscVrIpxInTooManyHops_Type = Counter32
_MscVrIpxInTooManyHops_Object = MibTableColumn
mscVrIpxInTooManyHops = _MscVrIpxInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 12),
    _MscVrIpxInTooManyHops_Type()
)
mscVrIpxInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInTooManyHops.setStatus("mandatory")
_MscVrIpxInFiltered_Type = Counter32
_MscVrIpxInFiltered_Object = MibTableColumn
mscVrIpxInFiltered = _MscVrIpxInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 13),
    _MscVrIpxInFiltered_Type()
)
mscVrIpxInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInFiltered.setStatus("mandatory")
_MscVrIpxInNetBIOS_Type = Counter32
_MscVrIpxInNetBIOS_Object = MibTableColumn
mscVrIpxInNetBIOS = _MscVrIpxInNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 14),
    _MscVrIpxInNetBIOS_Type()
)
mscVrIpxInNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxInNetBIOS.setStatus("mandatory")
_MscVrIpxForwarded_Type = Counter32
_MscVrIpxForwarded_Object = MibTableColumn
mscVrIpxForwarded = _MscVrIpxForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 15),
    _MscVrIpxForwarded_Type()
)
mscVrIpxForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxForwarded.setStatus("mandatory")
_MscVrIpxOutFiltered_Type = Counter32
_MscVrIpxOutFiltered_Object = MibTableColumn
mscVrIpxOutFiltered = _MscVrIpxOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 7, 107, 1, 16),
    _MscVrIpxOutFiltered_Type()
)
mscVrIpxOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpxOutFiltered.setStatus("mandatory")
_IpxMIB_ObjectIdentity = ObjectIdentity
ipxMIB = _IpxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28)
)
_IpxGroup_ObjectIdentity = ObjectIdentity
ipxGroup = _IpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 1)
)
_IpxGroupCA_ObjectIdentity = ObjectIdentity
ipxGroupCA = _IpxGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 1, 1)
)
_IpxGroupCA02_ObjectIdentity = ObjectIdentity
ipxGroupCA02 = _IpxGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 1, 1, 3)
)
_IpxGroupCA02A_ObjectIdentity = ObjectIdentity
ipxGroupCA02A = _IpxGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 1, 1, 3, 2)
)
_IpxCapabilities_ObjectIdentity = ObjectIdentity
ipxCapabilities = _IpxCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 3)
)
_IpxCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipxCapabilitiesCA = _IpxCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 3, 1)
)
_IpxCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipxCapabilitiesCA02 = _IpxCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 3, 1, 3)
)
_IpxCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipxCapabilitiesCA02A = _IpxCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 28, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpxMIB",
    **{"mscVrPpIpxP": mscVrPpIpxP,
       "mscVrPpIpxPRowStatusTable": mscVrPpIpxPRowStatusTable,
       "mscVrPpIpxPRowStatusEntry": mscVrPpIpxPRowStatusEntry,
       "mscVrPpIpxPRowStatus": mscVrPpIpxPRowStatus,
       "mscVrPpIpxPComponentName": mscVrPpIpxPComponentName,
       "mscVrPpIpxPStorageType": mscVrPpIpxPStorageType,
       "mscVrPpIpxPIndex": mscVrPpIpxPIndex,
       "mscVrPpIpxPRipP": mscVrPpIpxPRipP,
       "mscVrPpIpxPRipPRowStatusTable": mscVrPpIpxPRipPRowStatusTable,
       "mscVrPpIpxPRipPRowStatusEntry": mscVrPpIpxPRipPRowStatusEntry,
       "mscVrPpIpxPRipPRowStatus": mscVrPpIpxPRipPRowStatus,
       "mscVrPpIpxPRipPComponentName": mscVrPpIpxPRipPComponentName,
       "mscVrPpIpxPRipPStorageType": mscVrPpIpxPRipPStorageType,
       "mscVrPpIpxPRipPIndex": mscVrPpIpxPRipPIndex,
       "mscVrPpIpxPRipPStatsTable": mscVrPpIpxPRipPStatsTable,
       "mscVrPpIpxPRipPStatsEntry": mscVrPpIpxPRipPStatsEntry,
       "mscVrPpIpxPRipPInPackets": mscVrPpIpxPRipPInPackets,
       "mscVrPpIpxPRipPInRequests": mscVrPpIpxPRipPInRequests,
       "mscVrPpIpxPRipPInResponses": mscVrPpIpxPRipPInResponses,
       "mscVrPpIpxPRipPOutPackets": mscVrPpIpxPRipPOutPackets,
       "mscVrPpIpxPRipPOutRequests": mscVrPpIpxPRipPOutRequests,
       "mscVrPpIpxPRipPOutResponses": mscVrPpIpxPRipPOutResponses,
       "mscVrPpIpxPRipPIncorrectPackets": mscVrPpIpxPRipPIncorrectPackets,
       "mscVrPpIpxPSapP": mscVrPpIpxPSapP,
       "mscVrPpIpxPSapPRowStatusTable": mscVrPpIpxPSapPRowStatusTable,
       "mscVrPpIpxPSapPRowStatusEntry": mscVrPpIpxPSapPRowStatusEntry,
       "mscVrPpIpxPSapPRowStatus": mscVrPpIpxPSapPRowStatus,
       "mscVrPpIpxPSapPComponentName": mscVrPpIpxPSapPComponentName,
       "mscVrPpIpxPSapPStorageType": mscVrPpIpxPSapPStorageType,
       "mscVrPpIpxPSapPIndex": mscVrPpIpxPSapPIndex,
       "mscVrPpIpxPSapPStatsTable": mscVrPpIpxPSapPStatsTable,
       "mscVrPpIpxPSapPStatsEntry": mscVrPpIpxPSapPStatsEntry,
       "mscVrPpIpxPSapPInPackets": mscVrPpIpxPSapPInPackets,
       "mscVrPpIpxPSapPInRequests": mscVrPpIpxPSapPInRequests,
       "mscVrPpIpxPSapPInResponses": mscVrPpIpxPSapPInResponses,
       "mscVrPpIpxPSapPOutPackets": mscVrPpIpxPSapPOutPackets,
       "mscVrPpIpxPSapPOutRequests": mscVrPpIpxPSapPOutRequests,
       "mscVrPpIpxPSapPOutResponses": mscVrPpIpxPSapPOutResponses,
       "mscVrPpIpxPSapPIncorrectPackets": mscVrPpIpxPSapPIncorrectPackets,
       "mscVrPpIpxPIWP": mscVrPpIpxPIWP,
       "mscVrPpIpxPIWPRowStatusTable": mscVrPpIpxPIWPRowStatusTable,
       "mscVrPpIpxPIWPRowStatusEntry": mscVrPpIpxPIWPRowStatusEntry,
       "mscVrPpIpxPIWPRowStatus": mscVrPpIpxPIWPRowStatus,
       "mscVrPpIpxPIWPComponentName": mscVrPpIpxPIWPComponentName,
       "mscVrPpIpxPIWPStorageType": mscVrPpIpxPIWPStorageType,
       "mscVrPpIpxPIWPRemoteStationIdentifierIndex": mscVrPpIpxPIWPRemoteStationIdentifierIndex,
       "mscVrPpIpxPIWPOperTable": mscVrPpIpxPIWPOperTable,
       "mscVrPpIpxPIWPOperEntry": mscVrPpIpxPIWPOperEntry,
       "mscVrPpIpxPIWPNeighbourRouterName": mscVrPpIpxPIWPNeighbourRouterName,
       "mscVrPpIpxPIWPNeighbourInternalNetworkNumber": mscVrPpIpxPIWPNeighbourInternalNetworkNumber,
       "mscVrPpIpxPIWPInitFails": mscVrPpIpxPIWPInitFails,
       "mscVrPpIpxPNetSentryP": mscVrPpIpxPNetSentryP,
       "mscVrPpIpxPNetSentryPRowStatusTable": mscVrPpIpxPNetSentryPRowStatusTable,
       "mscVrPpIpxPNetSentryPRowStatusEntry": mscVrPpIpxPNetSentryPRowStatusEntry,
       "mscVrPpIpxPNetSentryPRowStatus": mscVrPpIpxPNetSentryPRowStatus,
       "mscVrPpIpxPNetSentryPComponentName": mscVrPpIpxPNetSentryPComponentName,
       "mscVrPpIpxPNetSentryPStorageType": mscVrPpIpxPNetSentryPStorageType,
       "mscVrPpIpxPNetSentryPIndex": mscVrPpIpxPNetSentryPIndex,
       "mscVrPpIpxPNetSentryPProvTable": mscVrPpIpxPNetSentryPProvTable,
       "mscVrPpIpxPNetSentryPProvEntry": mscVrPpIpxPNetSentryPProvEntry,
       "mscVrPpIpxPNetSentryPInComingFilter": mscVrPpIpxPNetSentryPInComingFilter,
       "mscVrPpIpxPNetSentryPOutGoingFilter": mscVrPpIpxPNetSentryPOutGoingFilter,
       "mscVrPpIpxPAdminControlTable": mscVrPpIpxPAdminControlTable,
       "mscVrPpIpxPAdminControlEntry": mscVrPpIpxPAdminControlEntry,
       "mscVrPpIpxPSnmpAdminStatus": mscVrPpIpxPSnmpAdminStatus,
       "mscVrPpIpxPProvTable": mscVrPpIpxPProvTable,
       "mscVrPpIpxPProvEntry": mscVrPpIpxPProvEntry,
       "mscVrPpIpxPNetworkNumberProv": mscVrPpIpxPNetworkNumberProv,
       "mscVrPpIpxPDefaultType": mscVrPpIpxPDefaultType,
       "mscVrPpIpxPBroadcastInhibit": mscVrPpIpxPBroadcastInhibit,
       "mscVrPpIpxPSresProvTable": mscVrPpIpxPSresProvTable,
       "mscVrPpIpxPSresProvEntry": mscVrPpIpxPSresProvEntry,
       "mscVrPpIpxPSourceRouteEndStationSupport": mscVrPpIpxPSourceRouteEndStationSupport,
       "mscVrPpIpxPStateTable": mscVrPpIpxPStateTable,
       "mscVrPpIpxPStateEntry": mscVrPpIpxPStateEntry,
       "mscVrPpIpxPAdminState": mscVrPpIpxPAdminState,
       "mscVrPpIpxPOperationalState": mscVrPpIpxPOperationalState,
       "mscVrPpIpxPUsageState": mscVrPpIpxPUsageState,
       "mscVrPpIpxPOperStatusTable": mscVrPpIpxPOperStatusTable,
       "mscVrPpIpxPOperStatusEntry": mscVrPpIpxPOperStatusEntry,
       "mscVrPpIpxPSnmpOperStatus": mscVrPpIpxPSnmpOperStatus,
       "mscVrPpIpxPOperTable": mscVrPpIpxPOperTable,
       "mscVrPpIpxPOperEntry": mscVrPpIpxPOperEntry,
       "mscVrPpIpxPType": mscVrPpIpxPType,
       "mscVrPpIpxPEncapsulation": mscVrPpIpxPEncapsulation,
       "mscVrPpIpxPNetworkNumber": mscVrPpIpxPNetworkNumber,
       "mscVrPpIpxPNode": mscVrPpIpxPNode,
       "mscVrPpIpxPStatsTable": mscVrPpIpxPStatsTable,
       "mscVrPpIpxPStatsEntry": mscVrPpIpxPStatsEntry,
       "mscVrPpIpxPStateChanges": mscVrPpIpxPStateChanges,
       "mscVrPpIpxPInReceives": mscVrPpIpxPInReceives,
       "mscVrPpIpxPForwarded": mscVrPpIpxPForwarded,
       "mscVrIpx": mscVrIpx,
       "mscVrIpxRowStatusTable": mscVrIpxRowStatusTable,
       "mscVrIpxRowStatusEntry": mscVrIpxRowStatusEntry,
       "mscVrIpxRowStatus": mscVrIpxRowStatus,
       "mscVrIpxComponentName": mscVrIpxComponentName,
       "mscVrIpxStorageType": mscVrIpxStorageType,
       "mscVrIpxIndex": mscVrIpxIndex,
       "mscVrIpxRip": mscVrIpxRip,
       "mscVrIpxRipRowStatusTable": mscVrIpxRipRowStatusTable,
       "mscVrIpxRipRowStatusEntry": mscVrIpxRipRowStatusEntry,
       "mscVrIpxRipRowStatus": mscVrIpxRipRowStatus,
       "mscVrIpxRipComponentName": mscVrIpxRipComponentName,
       "mscVrIpxRipStorageType": mscVrIpxRipStorageType,
       "mscVrIpxRipIndex": mscVrIpxRipIndex,
       "mscVrIpxRipRFltr": mscVrIpxRipRFltr,
       "mscVrIpxRipRFltrRowStatusTable": mscVrIpxRipRFltrRowStatusTable,
       "mscVrIpxRipRFltrRowStatusEntry": mscVrIpxRipRFltrRowStatusEntry,
       "mscVrIpxRipRFltrRowStatus": mscVrIpxRipRFltrRowStatus,
       "mscVrIpxRipRFltrComponentName": mscVrIpxRipRFltrComponentName,
       "mscVrIpxRipRFltrStorageType": mscVrIpxRipRFltrStorageType,
       "mscVrIpxRipRFltrIdentifierIndex": mscVrIpxRipRFltrIdentifierIndex,
       "mscVrIpxRipRFltrProvTable": mscVrIpxRipRFltrProvTable,
       "mscVrIpxRipRFltrProvEntry": mscVrIpxRipRFltrProvEntry,
       "mscVrIpxRipRFltrHops": mscVrIpxRipRFltrHops,
       "mscVrIpxRipRFltrTicks": mscVrIpxRipRFltrTicks,
       "mscVrIpxRipRFltrNetworkNumber": mscVrIpxRipRFltrNetworkNumber,
       "mscVrIpxRipRFltrNode": mscVrIpxRipRFltrNode,
       "mscVrIpxRipRFltrPort": mscVrIpxRipRFltrPort,
       "mscVrIpxRipRFltrDisposition": mscVrIpxRipRFltrDisposition,
       "mscVrIpxRipRFltrOperTable": mscVrIpxRipRFltrOperTable,
       "mscVrIpxRipRFltrOperEntry": mscVrIpxRipRFltrOperEntry,
       "mscVrIpxRipRFltrNumberOfApplyEntries": mscVrIpxRipRFltrNumberOfApplyEntries,
       "mscVrIpxRipRipApp": mscVrIpxRipRipApp,
       "mscVrIpxRipRipAppRowStatusTable": mscVrIpxRipRipAppRowStatusTable,
       "mscVrIpxRipRipAppRowStatusEntry": mscVrIpxRipRipAppRowStatusEntry,
       "mscVrIpxRipRipAppRowStatus": mscVrIpxRipRipAppRowStatus,
       "mscVrIpxRipRipAppComponentName": mscVrIpxRipRipAppComponentName,
       "mscVrIpxRipRipAppStorageType": mscVrIpxRipRipAppStorageType,
       "mscVrIpxRipRipAppProtocolPortNameIndex": mscVrIpxRipRipAppProtocolPortNameIndex,
       "mscVrIpxRipRipAppFilterIdentifierIndex": mscVrIpxRipRipAppFilterIdentifierIndex,
       "mscVrIpxRipRipAppProvTable": mscVrIpxRipRipAppProvTable,
       "mscVrIpxRipRipAppProvEntry": mscVrIpxRipRipAppProvEntry,
       "mscVrIpxRipRipAppDirection": mscVrIpxRipRipAppDirection,
       "mscVrIpxRipStatsTable": mscVrIpxRipStatsTable,
       "mscVrIpxRipStatsEntry": mscVrIpxRipStatsEntry,
       "mscVrIpxRipRipIn": mscVrIpxRipRipIn,
       "mscVrIpxRipRipOut": mscVrIpxRipRipOut,
       "mscVrIpxRipRipIncorrectPackets": mscVrIpxRipRipIncorrectPackets,
       "mscVrIpxSap": mscVrIpxSap,
       "mscVrIpxSapRowStatusTable": mscVrIpxSapRowStatusTable,
       "mscVrIpxSapRowStatusEntry": mscVrIpxSapRowStatusEntry,
       "mscVrIpxSapRowStatus": mscVrIpxSapRowStatus,
       "mscVrIpxSapComponentName": mscVrIpxSapComponentName,
       "mscVrIpxSapStorageType": mscVrIpxSapStorageType,
       "mscVrIpxSapIndex": mscVrIpxSapIndex,
       "mscVrIpxSapSFltr": mscVrIpxSapSFltr,
       "mscVrIpxSapSFltrRowStatusTable": mscVrIpxSapSFltrRowStatusTable,
       "mscVrIpxSapSFltrRowStatusEntry": mscVrIpxSapSFltrRowStatusEntry,
       "mscVrIpxSapSFltrRowStatus": mscVrIpxSapSFltrRowStatus,
       "mscVrIpxSapSFltrComponentName": mscVrIpxSapSFltrComponentName,
       "mscVrIpxSapSFltrStorageType": mscVrIpxSapSFltrStorageType,
       "mscVrIpxSapSFltrIdentifierIndex": mscVrIpxSapSFltrIdentifierIndex,
       "mscVrIpxSapSFltrProvTable": mscVrIpxSapSFltrProvTable,
       "mscVrIpxSapSFltrProvEntry": mscVrIpxSapSFltrProvEntry,
       "mscVrIpxSapSFltrType": mscVrIpxSapSFltrType,
       "mscVrIpxSapSFltrName": mscVrIpxSapSFltrName,
       "mscVrIpxSapSFltrNetworkNumber": mscVrIpxSapSFltrNetworkNumber,
       "mscVrIpxSapSFltrNode": mscVrIpxSapSFltrNode,
       "mscVrIpxSapSFltrDisposition": mscVrIpxSapSFltrDisposition,
       "mscVrIpxSapSFltrOperTable": mscVrIpxSapSFltrOperTable,
       "mscVrIpxSapSFltrOperEntry": mscVrIpxSapSFltrOperEntry,
       "mscVrIpxSapSFltrNumberOfApplyEntries": mscVrIpxSapSFltrNumberOfApplyEntries,
       "mscVrIpxSapSapApp": mscVrIpxSapSapApp,
       "mscVrIpxSapSapAppRowStatusTable": mscVrIpxSapSapAppRowStatusTable,
       "mscVrIpxSapSapAppRowStatusEntry": mscVrIpxSapSapAppRowStatusEntry,
       "mscVrIpxSapSapAppRowStatus": mscVrIpxSapSapAppRowStatus,
       "mscVrIpxSapSapAppComponentName": mscVrIpxSapSapAppComponentName,
       "mscVrIpxSapSapAppStorageType": mscVrIpxSapSapAppStorageType,
       "mscVrIpxSapSapAppProtocolPortNameIndex": mscVrIpxSapSapAppProtocolPortNameIndex,
       "mscVrIpxSapSapAppFilterIdentifierIndex": mscVrIpxSapSapAppFilterIdentifierIndex,
       "mscVrIpxSapSapAppProvTable": mscVrIpxSapSapAppProvTable,
       "mscVrIpxSapSapAppProvEntry": mscVrIpxSapSapAppProvEntry,
       "mscVrIpxSapSapAppDirection": mscVrIpxSapSapAppDirection,
       "mscVrIpxSapStatsTable": mscVrIpxSapStatsTable,
       "mscVrIpxSapStatsEntry": mscVrIpxSapStatsEntry,
       "mscVrIpxSapSapIn": mscVrIpxSapSapIn,
       "mscVrIpxSapSapOut": mscVrIpxSapSapOut,
       "mscVrIpxSapSapIncorrectPackets": mscVrIpxSapSapIncorrectPackets,
       "mscVrIpxFwd": mscVrIpxFwd,
       "mscVrIpxFwdRowStatusTable": mscVrIpxFwdRowStatusTable,
       "mscVrIpxFwdRowStatusEntry": mscVrIpxFwdRowStatusEntry,
       "mscVrIpxFwdRowStatus": mscVrIpxFwdRowStatus,
       "mscVrIpxFwdComponentName": mscVrIpxFwdComponentName,
       "mscVrIpxFwdStorageType": mscVrIpxFwdStorageType,
       "mscVrIpxFwdNetworkNumberIndex": mscVrIpxFwdNetworkNumberIndex,
       "mscVrIpxFwdOperTable": mscVrIpxFwdOperTable,
       "mscVrIpxFwdOperEntry": mscVrIpxFwdOperEntry,
       "mscVrIpxFwdProtocol": mscVrIpxFwdProtocol,
       "mscVrIpxFwdTicks": mscVrIpxFwdTicks,
       "mscVrIpxFwdHopCount": mscVrIpxFwdHopCount,
       "mscVrIpxFwdProtocolPortId": mscVrIpxFwdProtocolPortId,
       "mscVrIpxFwdNextHopPhysAddress": mscVrIpxFwdNextHopPhysAddress,
       "mscVrIpxFwdNextHopNetworkNumber": mscVrIpxFwdNextHopNetworkNumber,
       "mscVrIpxSrvc": mscVrIpxSrvc,
       "mscVrIpxSrvcRowStatusTable": mscVrIpxSrvcRowStatusTable,
       "mscVrIpxSrvcRowStatusEntry": mscVrIpxSrvcRowStatusEntry,
       "mscVrIpxSrvcRowStatus": mscVrIpxSrvcRowStatus,
       "mscVrIpxSrvcComponentName": mscVrIpxSrvcComponentName,
       "mscVrIpxSrvcStorageType": mscVrIpxSrvcStorageType,
       "mscVrIpxSrvcNetworkNumberIndex": mscVrIpxSrvcNetworkNumberIndex,
       "mscVrIpxSrvcNodeIndex": mscVrIpxSrvcNodeIndex,
       "mscVrIpxSrvcTypeIndex": mscVrIpxSrvcTypeIndex,
       "mscVrIpxSrvcNameIndex": mscVrIpxSrvcNameIndex,
       "mscVrIpxSrvcOperTable": mscVrIpxSrvcOperTable,
       "mscVrIpxSrvcOperEntry": mscVrIpxSrvcOperEntry,
       "mscVrIpxSrvcSocket": mscVrIpxSrvcSocket,
       "mscVrIpxSrvcProtocol": mscVrIpxSrvcProtocol,
       "mscVrIpxSrvcHopCount": mscVrIpxSrvcHopCount,
       "mscVrIpxAdj": mscVrIpxAdj,
       "mscVrIpxAdjRowStatusTable": mscVrIpxAdjRowStatusTable,
       "mscVrIpxAdjRowStatusEntry": mscVrIpxAdjRowStatusEntry,
       "mscVrIpxAdjRowStatus": mscVrIpxAdjRowStatus,
       "mscVrIpxAdjComponentName": mscVrIpxAdjComponentName,
       "mscVrIpxAdjStorageType": mscVrIpxAdjStorageType,
       "mscVrIpxAdjProtocolPortIdentifierIndex": mscVrIpxAdjProtocolPortIdentifierIndex,
       "mscVrIpxAdjNetworkNumberIndex": mscVrIpxAdjNetworkNumberIndex,
       "mscVrIpxAdjOperTable": mscVrIpxAdjOperTable,
       "mscVrIpxAdjOperEntry": mscVrIpxAdjOperEntry,
       "mscVrIpxAdjPhysAddress": mscVrIpxAdjPhysAddress,
       "mscVrIpxAdjAdjacencyState": mscVrIpxAdjAdjacencyState,
       "mscVrIpxNs": mscVrIpxNs,
       "mscVrIpxNsRowStatusTable": mscVrIpxNsRowStatusTable,
       "mscVrIpxNsRowStatusEntry": mscVrIpxNsRowStatusEntry,
       "mscVrIpxNsRowStatus": mscVrIpxNsRowStatus,
       "mscVrIpxNsComponentName": mscVrIpxNsComponentName,
       "mscVrIpxNsStorageType": mscVrIpxNsStorageType,
       "mscVrIpxNsIndex": mscVrIpxNsIndex,
       "mscVrIpxNsNetSentryApp": mscVrIpxNsNetSentryApp,
       "mscVrIpxNsNetSentryAppRowStatusTable": mscVrIpxNsNetSentryAppRowStatusTable,
       "mscVrIpxNsNetSentryAppRowStatusEntry": mscVrIpxNsNetSentryAppRowStatusEntry,
       "mscVrIpxNsNetSentryAppRowStatus": mscVrIpxNsNetSentryAppRowStatus,
       "mscVrIpxNsNetSentryAppComponentName": mscVrIpxNsNetSentryAppComponentName,
       "mscVrIpxNsNetSentryAppStorageType": mscVrIpxNsNetSentryAppStorageType,
       "mscVrIpxNsNetSentryAppEntryIndex": mscVrIpxNsNetSentryAppEntryIndex,
       "mscVrIpxNsNetSentryAppProvTable": mscVrIpxNsNetSentryAppProvTable,
       "mscVrIpxNsNetSentryAppProvEntry": mscVrIpxNsNetSentryAppProvEntry,
       "mscVrIpxNsNetSentryAppFilter": mscVrIpxNsNetSentryAppFilter,
       "mscVrIpxNsNetSentryAppNetworkNumber1": mscVrIpxNsNetSentryAppNetworkNumber1,
       "mscVrIpxNsNetSentryAppNode1": mscVrIpxNsNetSentryAppNode1,
       "mscVrIpxNsNetSentryAppDirection": mscVrIpxNsNetSentryAppDirection,
       "mscVrIpxNsNetSentryAppNetworkNumber2": mscVrIpxNsNetSentryAppNetworkNumber2,
       "mscVrIpxNsNetSentryAppNode2": mscVrIpxNsNetSentryAppNode2,
       "mscVrIpxNsProvTable": mscVrIpxNsProvTable,
       "mscVrIpxNsProvEntry": mscVrIpxNsProvEntry,
       "mscVrIpxNsFirstFilter": mscVrIpxNsFirstFilter,
       "mscVrIpxNsLastFilter": mscVrIpxNsLastFilter,
       "mscVrIpxNsLocalInFilter": mscVrIpxNsLocalInFilter,
       "mscVrIpxNsLocalOutFilter": mscVrIpxNsLocalOutFilter,
       "mscVrIpxAdminControlTable": mscVrIpxAdminControlTable,
       "mscVrIpxAdminControlEntry": mscVrIpxAdminControlEntry,
       "mscVrIpxSnmpAdminStatus": mscVrIpxSnmpAdminStatus,
       "mscVrIpxProvTable": mscVrIpxProvTable,
       "mscVrIpxProvEntry": mscVrIpxProvEntry,
       "mscVrIpxNetworkNumber": mscVrIpxNetworkNumber,
       "mscVrIpxMaxPathSplits": mscVrIpxMaxPathSplits,
       "mscVrIpxMaxHops": mscVrIpxMaxHops,
       "mscVrIpxRipUpdateInterval": mscVrIpxRipUpdateInterval,
       "mscVrIpxSapUpdateInterval": mscVrIpxSapUpdateInterval,
       "mscVrIpxControlDelay": mscVrIpxControlDelay,
       "mscVrIpxUpdateDelay": mscVrIpxUpdateDelay,
       "mscVrIpxRipAgeMultiplier": mscVrIpxRipAgeMultiplier,
       "mscVrIpxSapAgeMultiplier": mscVrIpxSapAgeMultiplier,
       "mscVrIpxDamping": mscVrIpxDamping,
       "mscVrIpxRipMaxDampedGeneralRequests": mscVrIpxRipMaxDampedGeneralRequests,
       "mscVrIpxRipMaxDampedSpecificRequests": mscVrIpxRipMaxDampedSpecificRequests,
       "mscVrIpxSapMaxDampedGeneralRequests": mscVrIpxSapMaxDampedGeneralRequests,
       "mscVrIpxSapMaxDampedSpecificRequests": mscVrIpxSapMaxDampedSpecificRequests,
       "mscVrIpxInitialGeneralRequests": mscVrIpxInitialGeneralRequests,
       "mscVrIpxHoldDownInterval": mscVrIpxHoldDownInterval,
       "mscVrIpxStateTable": mscVrIpxStateTable,
       "mscVrIpxStateEntry": mscVrIpxStateEntry,
       "mscVrIpxAdminState": mscVrIpxAdminState,
       "mscVrIpxOperationalState": mscVrIpxOperationalState,
       "mscVrIpxUsageState": mscVrIpxUsageState,
       "mscVrIpxOperStatusTable": mscVrIpxOperStatusTable,
       "mscVrIpxOperStatusEntry": mscVrIpxOperStatusEntry,
       "mscVrIpxSnmpOperStatus": mscVrIpxSnmpOperStatus,
       "mscVrIpxOperTable": mscVrIpxOperTable,
       "mscVrIpxOperEntry": mscVrIpxOperEntry,
       "mscVrIpxProtocolPortCount": mscVrIpxProtocolPortCount,
       "mscVrIpxDestinationCount": mscVrIpxDestinationCount,
       "mscVrIpxServicesCount": mscVrIpxServicesCount,
       "mscVrIpxStatsTable": mscVrIpxStatsTable,
       "mscVrIpxStatsEntry": mscVrIpxStatsEntry,
       "mscVrIpxInReceives": mscVrIpxInReceives,
       "mscVrIpxInHeaderErrors": mscVrIpxInHeaderErrors,
       "mscVrIpxInUnknownSocket": mscVrIpxInUnknownSocket,
       "mscVrIpxInDiscards": mscVrIpxInDiscards,
       "mscVrIpxInBadChecksums": mscVrIpxInBadChecksums,
       "mscVrIpxInDelivers": mscVrIpxInDelivers,
       "mscVrIpxNoRoutes": mscVrIpxNoRoutes,
       "mscVrIpxOutRequests": mscVrIpxOutRequests,
       "mscVrIpxOutMalformedRequests": mscVrIpxOutMalformedRequests,
       "mscVrIpxOutDiscards": mscVrIpxOutDiscards,
       "mscVrIpxOutPackets": mscVrIpxOutPackets,
       "mscVrIpxInTooManyHops": mscVrIpxInTooManyHops,
       "mscVrIpxInFiltered": mscVrIpxInFiltered,
       "mscVrIpxInNetBIOS": mscVrIpxInNetBIOS,
       "mscVrIpxForwarded": mscVrIpxForwarded,
       "mscVrIpxOutFiltered": mscVrIpxOutFiltered,
       "ipxMIB": ipxMIB,
       "ipxGroup": ipxGroup,
       "ipxGroupCA": ipxGroupCA,
       "ipxGroupCA02": ipxGroupCA02,
       "ipxGroupCA02A": ipxGroupCA02A,
       "ipxCapabilities": ipxCapabilities,
       "ipxCapabilitiesCA": ipxCapabilitiesCA,
       "ipxCapabilitiesCA02": ipxCapabilitiesCA02,
       "ipxCapabilitiesCA02A": ipxCapabilitiesCA02A}
)
