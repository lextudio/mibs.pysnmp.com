# SNMP MIB module (Nortel-Magellan-Passport-IpxMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpxMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:03 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "DashedHexString",
    "Hex",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex,
 vrPp,
 vrPpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex",
    "vrPp",
    "vrPpIndex")

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

_VrPpIpxP_ObjectIdentity = ObjectIdentity
vrPpIpxP = _VrPpIpxP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6)
)
_VrPpIpxPRowStatusTable_Object = MibTable
vrPpIpxPRowStatusTable = _VrPpIpxPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1)
)
if mibBuilder.loadTexts:
    vrPpIpxPRowStatusTable.setStatus("mandatory")
_VrPpIpxPRowStatusEntry_Object = MibTableRow
vrPpIpxPRowStatusEntry = _VrPpIpxPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1, 1)
)
vrPpIpxPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPRowStatusEntry.setStatus("mandatory")
_VrPpIpxPRowStatus_Type = RowStatus
_VrPpIpxPRowStatus_Object = MibTableColumn
vrPpIpxPRowStatus = _VrPpIpxPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1, 1, 1),
    _VrPpIpxPRowStatus_Type()
)
vrPpIpxPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPRowStatus.setStatus("mandatory")
_VrPpIpxPComponentName_Type = DisplayString
_VrPpIpxPComponentName_Object = MibTableColumn
vrPpIpxPComponentName = _VrPpIpxPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1, 1, 2),
    _VrPpIpxPComponentName_Type()
)
vrPpIpxPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPComponentName.setStatus("mandatory")
_VrPpIpxPStorageType_Type = StorageType
_VrPpIpxPStorageType_Object = MibTableColumn
vrPpIpxPStorageType = _VrPpIpxPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1, 1, 4),
    _VrPpIpxPStorageType_Type()
)
vrPpIpxPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPStorageType.setStatus("mandatory")


class _VrPpIpxPIndex_Type(Integer32):
    """Custom type vrPpIpxPIndex based on Integer32"""
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


_VrPpIpxPIndex_Type.__name__ = "Integer32"
_VrPpIpxPIndex_Object = MibTableColumn
vrPpIpxPIndex = _VrPpIpxPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 1, 1, 10),
    _VrPpIpxPIndex_Type()
)
vrPpIpxPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpxPIndex.setStatus("mandatory")
_VrPpIpxPRipP_ObjectIdentity = ObjectIdentity
vrPpIpxPRipP = _VrPpIpxPRipP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2)
)
_VrPpIpxPRipPRowStatusTable_Object = MibTable
vrPpIpxPRipPRowStatusTable = _VrPpIpxPRipPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vrPpIpxPRipPRowStatusTable.setStatus("mandatory")
_VrPpIpxPRipPRowStatusEntry_Object = MibTableRow
vrPpIpxPRipPRowStatusEntry = _VrPpIpxPRipPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1, 1)
)
vrPpIpxPRipPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPRipPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPRipPRowStatusEntry.setStatus("mandatory")
_VrPpIpxPRipPRowStatus_Type = RowStatus
_VrPpIpxPRipPRowStatus_Object = MibTableColumn
vrPpIpxPRipPRowStatus = _VrPpIpxPRipPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1, 1, 1),
    _VrPpIpxPRipPRowStatus_Type()
)
vrPpIpxPRipPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPRowStatus.setStatus("mandatory")
_VrPpIpxPRipPComponentName_Type = DisplayString
_VrPpIpxPRipPComponentName_Object = MibTableColumn
vrPpIpxPRipPComponentName = _VrPpIpxPRipPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1, 1, 2),
    _VrPpIpxPRipPComponentName_Type()
)
vrPpIpxPRipPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPComponentName.setStatus("mandatory")
_VrPpIpxPRipPStorageType_Type = StorageType
_VrPpIpxPRipPStorageType_Object = MibTableColumn
vrPpIpxPRipPStorageType = _VrPpIpxPRipPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1, 1, 4),
    _VrPpIpxPRipPStorageType_Type()
)
vrPpIpxPRipPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPStorageType.setStatus("mandatory")
_VrPpIpxPRipPIndex_Type = NonReplicated
_VrPpIpxPRipPIndex_Object = MibTableColumn
vrPpIpxPRipPIndex = _VrPpIpxPRipPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 1, 1, 10),
    _VrPpIpxPRipPIndex_Type()
)
vrPpIpxPRipPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpxPRipPIndex.setStatus("mandatory")
_VrPpIpxPRipPStatsTable_Object = MibTable
vrPpIpxPRipPStatsTable = _VrPpIpxPRipPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10)
)
if mibBuilder.loadTexts:
    vrPpIpxPRipPStatsTable.setStatus("mandatory")
_VrPpIpxPRipPStatsEntry_Object = MibTableRow
vrPpIpxPRipPStatsEntry = _VrPpIpxPRipPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1)
)
vrPpIpxPRipPStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPRipPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPRipPStatsEntry.setStatus("mandatory")
_VrPpIpxPRipPInPackets_Type = Counter32
_VrPpIpxPRipPInPackets_Object = MibTableColumn
vrPpIpxPRipPInPackets = _VrPpIpxPRipPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 1),
    _VrPpIpxPRipPInPackets_Type()
)
vrPpIpxPRipPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPInPackets.setStatus("mandatory")
_VrPpIpxPRipPInRequests_Type = Counter32
_VrPpIpxPRipPInRequests_Object = MibTableColumn
vrPpIpxPRipPInRequests = _VrPpIpxPRipPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 2),
    _VrPpIpxPRipPInRequests_Type()
)
vrPpIpxPRipPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPInRequests.setStatus("mandatory")
_VrPpIpxPRipPInResponses_Type = Counter32
_VrPpIpxPRipPInResponses_Object = MibTableColumn
vrPpIpxPRipPInResponses = _VrPpIpxPRipPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 3),
    _VrPpIpxPRipPInResponses_Type()
)
vrPpIpxPRipPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPInResponses.setStatus("mandatory")
_VrPpIpxPRipPOutPackets_Type = Counter32
_VrPpIpxPRipPOutPackets_Object = MibTableColumn
vrPpIpxPRipPOutPackets = _VrPpIpxPRipPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 4),
    _VrPpIpxPRipPOutPackets_Type()
)
vrPpIpxPRipPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPOutPackets.setStatus("mandatory")
_VrPpIpxPRipPOutRequests_Type = Counter32
_VrPpIpxPRipPOutRequests_Object = MibTableColumn
vrPpIpxPRipPOutRequests = _VrPpIpxPRipPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 5),
    _VrPpIpxPRipPOutRequests_Type()
)
vrPpIpxPRipPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPOutRequests.setStatus("mandatory")
_VrPpIpxPRipPOutResponses_Type = Counter32
_VrPpIpxPRipPOutResponses_Object = MibTableColumn
vrPpIpxPRipPOutResponses = _VrPpIpxPRipPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 6),
    _VrPpIpxPRipPOutResponses_Type()
)
vrPpIpxPRipPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPOutResponses.setStatus("mandatory")
_VrPpIpxPRipPIncorrectPackets_Type = Counter32
_VrPpIpxPRipPIncorrectPackets_Object = MibTableColumn
vrPpIpxPRipPIncorrectPackets = _VrPpIpxPRipPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 2, 10, 1, 7),
    _VrPpIpxPRipPIncorrectPackets_Type()
)
vrPpIpxPRipPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPRipPIncorrectPackets.setStatus("mandatory")
_VrPpIpxPSapP_ObjectIdentity = ObjectIdentity
vrPpIpxPSapP = _VrPpIpxPSapP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3)
)
_VrPpIpxPSapPRowStatusTable_Object = MibTable
vrPpIpxPSapPRowStatusTable = _VrPpIpxPSapPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    vrPpIpxPSapPRowStatusTable.setStatus("mandatory")
_VrPpIpxPSapPRowStatusEntry_Object = MibTableRow
vrPpIpxPSapPRowStatusEntry = _VrPpIpxPSapPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1, 1)
)
vrPpIpxPSapPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPSapPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPSapPRowStatusEntry.setStatus("mandatory")
_VrPpIpxPSapPRowStatus_Type = RowStatus
_VrPpIpxPSapPRowStatus_Object = MibTableColumn
vrPpIpxPSapPRowStatus = _VrPpIpxPSapPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1, 1, 1),
    _VrPpIpxPSapPRowStatus_Type()
)
vrPpIpxPSapPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPRowStatus.setStatus("mandatory")
_VrPpIpxPSapPComponentName_Type = DisplayString
_VrPpIpxPSapPComponentName_Object = MibTableColumn
vrPpIpxPSapPComponentName = _VrPpIpxPSapPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1, 1, 2),
    _VrPpIpxPSapPComponentName_Type()
)
vrPpIpxPSapPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPComponentName.setStatus("mandatory")
_VrPpIpxPSapPStorageType_Type = StorageType
_VrPpIpxPSapPStorageType_Object = MibTableColumn
vrPpIpxPSapPStorageType = _VrPpIpxPSapPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1, 1, 4),
    _VrPpIpxPSapPStorageType_Type()
)
vrPpIpxPSapPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPStorageType.setStatus("mandatory")
_VrPpIpxPSapPIndex_Type = NonReplicated
_VrPpIpxPSapPIndex_Object = MibTableColumn
vrPpIpxPSapPIndex = _VrPpIpxPSapPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 1, 1, 10),
    _VrPpIpxPSapPIndex_Type()
)
vrPpIpxPSapPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpxPSapPIndex.setStatus("mandatory")
_VrPpIpxPSapPStatsTable_Object = MibTable
vrPpIpxPSapPStatsTable = _VrPpIpxPSapPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10)
)
if mibBuilder.loadTexts:
    vrPpIpxPSapPStatsTable.setStatus("mandatory")
_VrPpIpxPSapPStatsEntry_Object = MibTableRow
vrPpIpxPSapPStatsEntry = _VrPpIpxPSapPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1)
)
vrPpIpxPSapPStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPSapPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPSapPStatsEntry.setStatus("mandatory")
_VrPpIpxPSapPInPackets_Type = Counter32
_VrPpIpxPSapPInPackets_Object = MibTableColumn
vrPpIpxPSapPInPackets = _VrPpIpxPSapPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 1),
    _VrPpIpxPSapPInPackets_Type()
)
vrPpIpxPSapPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPInPackets.setStatus("mandatory")
_VrPpIpxPSapPInRequests_Type = Counter32
_VrPpIpxPSapPInRequests_Object = MibTableColumn
vrPpIpxPSapPInRequests = _VrPpIpxPSapPInRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 2),
    _VrPpIpxPSapPInRequests_Type()
)
vrPpIpxPSapPInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPInRequests.setStatus("mandatory")
_VrPpIpxPSapPInResponses_Type = Counter32
_VrPpIpxPSapPInResponses_Object = MibTableColumn
vrPpIpxPSapPInResponses = _VrPpIpxPSapPInResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 3),
    _VrPpIpxPSapPInResponses_Type()
)
vrPpIpxPSapPInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPInResponses.setStatus("mandatory")
_VrPpIpxPSapPOutPackets_Type = Counter32
_VrPpIpxPSapPOutPackets_Object = MibTableColumn
vrPpIpxPSapPOutPackets = _VrPpIpxPSapPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 4),
    _VrPpIpxPSapPOutPackets_Type()
)
vrPpIpxPSapPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPOutPackets.setStatus("mandatory")
_VrPpIpxPSapPOutRequests_Type = Counter32
_VrPpIpxPSapPOutRequests_Object = MibTableColumn
vrPpIpxPSapPOutRequests = _VrPpIpxPSapPOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 5),
    _VrPpIpxPSapPOutRequests_Type()
)
vrPpIpxPSapPOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPOutRequests.setStatus("mandatory")
_VrPpIpxPSapPOutResponses_Type = Counter32
_VrPpIpxPSapPOutResponses_Object = MibTableColumn
vrPpIpxPSapPOutResponses = _VrPpIpxPSapPOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 6),
    _VrPpIpxPSapPOutResponses_Type()
)
vrPpIpxPSapPOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPOutResponses.setStatus("mandatory")
_VrPpIpxPSapPIncorrectPackets_Type = Counter32
_VrPpIpxPSapPIncorrectPackets_Object = MibTableColumn
vrPpIpxPSapPIncorrectPackets = _VrPpIpxPSapPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 3, 10, 1, 7),
    _VrPpIpxPSapPIncorrectPackets_Type()
)
vrPpIpxPSapPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSapPIncorrectPackets.setStatus("mandatory")
_VrPpIpxPIWP_ObjectIdentity = ObjectIdentity
vrPpIpxPIWP = _VrPpIpxPIWP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4)
)
_VrPpIpxPIWPRowStatusTable_Object = MibTable
vrPpIpxPIWPRowStatusTable = _VrPpIpxPIWPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    vrPpIpxPIWPRowStatusTable.setStatus("mandatory")
_VrPpIpxPIWPRowStatusEntry_Object = MibTableRow
vrPpIpxPIWPRowStatusEntry = _VrPpIpxPIWPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1, 1)
)
vrPpIpxPIWPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIWPRemoteStationIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPIWPRowStatusEntry.setStatus("mandatory")
_VrPpIpxPIWPRowStatus_Type = RowStatus
_VrPpIpxPIWPRowStatus_Object = MibTableColumn
vrPpIpxPIWPRowStatus = _VrPpIpxPIWPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1, 1, 1),
    _VrPpIpxPIWPRowStatus_Type()
)
vrPpIpxPIWPRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPRowStatus.setStatus("mandatory")
_VrPpIpxPIWPComponentName_Type = DisplayString
_VrPpIpxPIWPComponentName_Object = MibTableColumn
vrPpIpxPIWPComponentName = _VrPpIpxPIWPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1, 1, 2),
    _VrPpIpxPIWPComponentName_Type()
)
vrPpIpxPIWPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPComponentName.setStatus("mandatory")
_VrPpIpxPIWPStorageType_Type = StorageType
_VrPpIpxPIWPStorageType_Object = MibTableColumn
vrPpIpxPIWPStorageType = _VrPpIpxPIWPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1, 1, 4),
    _VrPpIpxPIWPStorageType_Type()
)
vrPpIpxPIWPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPStorageType.setStatus("mandatory")


class _VrPpIpxPIWPRemoteStationIdentifierIndex_Type(DashedHexString):
    """Custom type vrPpIpxPIWPRemoteStationIdentifierIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_VrPpIpxPIWPRemoteStationIdentifierIndex_Type.__name__ = "DashedHexString"
_VrPpIpxPIWPRemoteStationIdentifierIndex_Object = MibTableColumn
vrPpIpxPIWPRemoteStationIdentifierIndex = _VrPpIpxPIWPRemoteStationIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 1, 1, 10),
    _VrPpIpxPIWPRemoteStationIdentifierIndex_Type()
)
vrPpIpxPIWPRemoteStationIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpxPIWPRemoteStationIdentifierIndex.setStatus("mandatory")
_VrPpIpxPIWPOperTable_Object = MibTable
vrPpIpxPIWPOperTable = _VrPpIpxPIWPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 10)
)
if mibBuilder.loadTexts:
    vrPpIpxPIWPOperTable.setStatus("mandatory")
_VrPpIpxPIWPOperEntry_Object = MibTableRow
vrPpIpxPIWPOperEntry = _VrPpIpxPIWPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 10, 1)
)
vrPpIpxPIWPOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIWPRemoteStationIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPIWPOperEntry.setStatus("mandatory")


class _VrPpIpxPIWPNeighbourRouterName_Type(AsciiString):
    """Custom type vrPpIpxPIWPNeighbourRouterName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_VrPpIpxPIWPNeighbourRouterName_Type.__name__ = "AsciiString"
_VrPpIpxPIWPNeighbourRouterName_Object = MibTableColumn
vrPpIpxPIWPNeighbourRouterName = _VrPpIpxPIWPNeighbourRouterName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 10, 1, 1),
    _VrPpIpxPIWPNeighbourRouterName_Type()
)
vrPpIpxPIWPNeighbourRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPNeighbourRouterName.setStatus("mandatory")


class _VrPpIpxPIWPNeighbourInternalNetworkNumber_Type(DashedHexString):
    """Custom type vrPpIpxPIWPNeighbourInternalNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrPpIpxPIWPNeighbourInternalNetworkNumber_Type.__name__ = "DashedHexString"
_VrPpIpxPIWPNeighbourInternalNetworkNumber_Object = MibTableColumn
vrPpIpxPIWPNeighbourInternalNetworkNumber = _VrPpIpxPIWPNeighbourInternalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 10, 1, 2),
    _VrPpIpxPIWPNeighbourInternalNetworkNumber_Type()
)
vrPpIpxPIWPNeighbourInternalNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPNeighbourInternalNetworkNumber.setStatus("mandatory")
_VrPpIpxPIWPInitFails_Type = Counter32
_VrPpIpxPIWPInitFails_Object = MibTableColumn
vrPpIpxPIWPInitFails = _VrPpIpxPIWPInitFails_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 4, 10, 1, 3),
    _VrPpIpxPIWPInitFails_Type()
)
vrPpIpxPIWPInitFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPIWPInitFails.setStatus("mandatory")
_VrPpIpxPNetSentryP_ObjectIdentity = ObjectIdentity
vrPpIpxPNetSentryP = _VrPpIpxPNetSentryP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5)
)
_VrPpIpxPNetSentryPRowStatusTable_Object = MibTable
vrPpIpxPNetSentryPRowStatusTable = _VrPpIpxPNetSentryPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1)
)
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPRowStatusTable.setStatus("mandatory")
_VrPpIpxPNetSentryPRowStatusEntry_Object = MibTableRow
vrPpIpxPNetSentryPRowStatusEntry = _VrPpIpxPNetSentryPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1, 1)
)
vrPpIpxPNetSentryPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPNetSentryPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPRowStatusEntry.setStatus("mandatory")
_VrPpIpxPNetSentryPRowStatus_Type = RowStatus
_VrPpIpxPNetSentryPRowStatus_Object = MibTableColumn
vrPpIpxPNetSentryPRowStatus = _VrPpIpxPNetSentryPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1, 1, 1),
    _VrPpIpxPNetSentryPRowStatus_Type()
)
vrPpIpxPNetSentryPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPRowStatus.setStatus("mandatory")
_VrPpIpxPNetSentryPComponentName_Type = DisplayString
_VrPpIpxPNetSentryPComponentName_Object = MibTableColumn
vrPpIpxPNetSentryPComponentName = _VrPpIpxPNetSentryPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1, 1, 2),
    _VrPpIpxPNetSentryPComponentName_Type()
)
vrPpIpxPNetSentryPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPComponentName.setStatus("mandatory")
_VrPpIpxPNetSentryPStorageType_Type = StorageType
_VrPpIpxPNetSentryPStorageType_Object = MibTableColumn
vrPpIpxPNetSentryPStorageType = _VrPpIpxPNetSentryPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1, 1, 4),
    _VrPpIpxPNetSentryPStorageType_Type()
)
vrPpIpxPNetSentryPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPStorageType.setStatus("mandatory")
_VrPpIpxPNetSentryPIndex_Type = NonReplicated
_VrPpIpxPNetSentryPIndex_Object = MibTableColumn
vrPpIpxPNetSentryPIndex = _VrPpIpxPNetSentryPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 1, 1, 10),
    _VrPpIpxPNetSentryPIndex_Type()
)
vrPpIpxPNetSentryPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPIndex.setStatus("mandatory")
_VrPpIpxPNetSentryPProvTable_Object = MibTable
vrPpIpxPNetSentryPProvTable = _VrPpIpxPNetSentryPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 10)
)
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPProvTable.setStatus("mandatory")
_VrPpIpxPNetSentryPProvEntry_Object = MibTableRow
vrPpIpxPNetSentryPProvEntry = _VrPpIpxPNetSentryPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 10, 1)
)
vrPpIpxPNetSentryPProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPNetSentryPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPProvEntry.setStatus("mandatory")


class _VrPpIpxPNetSentryPInComingFilter_Type(AsciiString):
    """Custom type vrPpIpxPNetSentryPInComingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpIpxPNetSentryPInComingFilter_Type.__name__ = "AsciiString"
_VrPpIpxPNetSentryPInComingFilter_Object = MibTableColumn
vrPpIpxPNetSentryPInComingFilter = _VrPpIpxPNetSentryPInComingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 10, 1, 1),
    _VrPpIpxPNetSentryPInComingFilter_Type()
)
vrPpIpxPNetSentryPInComingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPInComingFilter.setStatus("mandatory")


class _VrPpIpxPNetSentryPOutGoingFilter_Type(AsciiString):
    """Custom type vrPpIpxPNetSentryPOutGoingFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrPpIpxPNetSentryPOutGoingFilter_Type.__name__ = "AsciiString"
_VrPpIpxPNetSentryPOutGoingFilter_Object = MibTableColumn
vrPpIpxPNetSentryPOutGoingFilter = _VrPpIpxPNetSentryPOutGoingFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 5, 10, 1, 2),
    _VrPpIpxPNetSentryPOutGoingFilter_Type()
)
vrPpIpxPNetSentryPOutGoingFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPNetSentryPOutGoingFilter.setStatus("mandatory")
_VrPpIpxPAdminControlTable_Object = MibTable
vrPpIpxPAdminControlTable = _VrPpIpxPAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 100)
)
if mibBuilder.loadTexts:
    vrPpIpxPAdminControlTable.setStatus("mandatory")
_VrPpIpxPAdminControlEntry_Object = MibTableRow
vrPpIpxPAdminControlEntry = _VrPpIpxPAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 100, 1)
)
vrPpIpxPAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPAdminControlEntry.setStatus("mandatory")


class _VrPpIpxPSnmpAdminStatus_Type(Integer32):
    """Custom type vrPpIpxPSnmpAdminStatus based on Integer32"""
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


_VrPpIpxPSnmpAdminStatus_Type.__name__ = "Integer32"
_VrPpIpxPSnmpAdminStatus_Object = MibTableColumn
vrPpIpxPSnmpAdminStatus = _VrPpIpxPSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 100, 1, 1),
    _VrPpIpxPSnmpAdminStatus_Type()
)
vrPpIpxPSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPSnmpAdminStatus.setStatus("mandatory")
_VrPpIpxPProvTable_Object = MibTable
vrPpIpxPProvTable = _VrPpIpxPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 101)
)
if mibBuilder.loadTexts:
    vrPpIpxPProvTable.setStatus("mandatory")
_VrPpIpxPProvEntry_Object = MibTableRow
vrPpIpxPProvEntry = _VrPpIpxPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 101, 1)
)
vrPpIpxPProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPProvEntry.setStatus("mandatory")


class _VrPpIpxPNetworkNumberProv_Type(DashedHexString):
    """Custom type vrPpIpxPNetworkNumberProv based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VrPpIpxPNetworkNumberProv_Type.__name__ = "DashedHexString"
_VrPpIpxPNetworkNumberProv_Object = MibTableColumn
vrPpIpxPNetworkNumberProv = _VrPpIpxPNetworkNumberProv_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 101, 1, 1),
    _VrPpIpxPNetworkNumberProv_Type()
)
vrPpIpxPNetworkNumberProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPNetworkNumberProv.setStatus("mandatory")


class _VrPpIpxPDefaultType_Type(Integer32):
    """Custom type vrPpIpxPDefaultType based on Integer32"""
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


_VrPpIpxPDefaultType_Type.__name__ = "Integer32"
_VrPpIpxPDefaultType_Object = MibTableColumn
vrPpIpxPDefaultType = _VrPpIpxPDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 101, 1, 2),
    _VrPpIpxPDefaultType_Type()
)
vrPpIpxPDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPDefaultType.setStatus("mandatory")


class _VrPpIpxPBroadcastInhibit_Type(Integer32):
    """Custom type vrPpIpxPBroadcastInhibit based on Integer32"""
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


_VrPpIpxPBroadcastInhibit_Type.__name__ = "Integer32"
_VrPpIpxPBroadcastInhibit_Object = MibTableColumn
vrPpIpxPBroadcastInhibit = _VrPpIpxPBroadcastInhibit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 101, 1, 3),
    _VrPpIpxPBroadcastInhibit_Type()
)
vrPpIpxPBroadcastInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPBroadcastInhibit.setStatus("mandatory")
_VrPpIpxPSresProvTable_Object = MibTable
vrPpIpxPSresProvTable = _VrPpIpxPSresProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 102)
)
if mibBuilder.loadTexts:
    vrPpIpxPSresProvTable.setStatus("mandatory")
_VrPpIpxPSresProvEntry_Object = MibTableRow
vrPpIpxPSresProvEntry = _VrPpIpxPSresProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 102, 1)
)
vrPpIpxPSresProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPSresProvEntry.setStatus("mandatory")


class _VrPpIpxPSourceRouteEndStationSupport_Type(Integer32):
    """Custom type vrPpIpxPSourceRouteEndStationSupport based on Integer32"""
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


_VrPpIpxPSourceRouteEndStationSupport_Type.__name__ = "Integer32"
_VrPpIpxPSourceRouteEndStationSupport_Object = MibTableColumn
vrPpIpxPSourceRouteEndStationSupport = _VrPpIpxPSourceRouteEndStationSupport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 102, 1, 1),
    _VrPpIpxPSourceRouteEndStationSupport_Type()
)
vrPpIpxPSourceRouteEndStationSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrPpIpxPSourceRouteEndStationSupport.setStatus("mandatory")
_VrPpIpxPStateTable_Object = MibTable
vrPpIpxPStateTable = _VrPpIpxPStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 103)
)
if mibBuilder.loadTexts:
    vrPpIpxPStateTable.setStatus("mandatory")
_VrPpIpxPStateEntry_Object = MibTableRow
vrPpIpxPStateEntry = _VrPpIpxPStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 103, 1)
)
vrPpIpxPStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPStateEntry.setStatus("mandatory")


class _VrPpIpxPAdminState_Type(Integer32):
    """Custom type vrPpIpxPAdminState based on Integer32"""
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


_VrPpIpxPAdminState_Type.__name__ = "Integer32"
_VrPpIpxPAdminState_Object = MibTableColumn
vrPpIpxPAdminState = _VrPpIpxPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 103, 1, 1),
    _VrPpIpxPAdminState_Type()
)
vrPpIpxPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPAdminState.setStatus("mandatory")


class _VrPpIpxPOperationalState_Type(Integer32):
    """Custom type vrPpIpxPOperationalState based on Integer32"""
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


_VrPpIpxPOperationalState_Type.__name__ = "Integer32"
_VrPpIpxPOperationalState_Object = MibTableColumn
vrPpIpxPOperationalState = _VrPpIpxPOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 103, 1, 2),
    _VrPpIpxPOperationalState_Type()
)
vrPpIpxPOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPOperationalState.setStatus("mandatory")


class _VrPpIpxPUsageState_Type(Integer32):
    """Custom type vrPpIpxPUsageState based on Integer32"""
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


_VrPpIpxPUsageState_Type.__name__ = "Integer32"
_VrPpIpxPUsageState_Object = MibTableColumn
vrPpIpxPUsageState = _VrPpIpxPUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 103, 1, 3),
    _VrPpIpxPUsageState_Type()
)
vrPpIpxPUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPUsageState.setStatus("mandatory")
_VrPpIpxPOperStatusTable_Object = MibTable
vrPpIpxPOperStatusTable = _VrPpIpxPOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 104)
)
if mibBuilder.loadTexts:
    vrPpIpxPOperStatusTable.setStatus("mandatory")
_VrPpIpxPOperStatusEntry_Object = MibTableRow
vrPpIpxPOperStatusEntry = _VrPpIpxPOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 104, 1)
)
vrPpIpxPOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPOperStatusEntry.setStatus("mandatory")


class _VrPpIpxPSnmpOperStatus_Type(Integer32):
    """Custom type vrPpIpxPSnmpOperStatus based on Integer32"""
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


_VrPpIpxPSnmpOperStatus_Type.__name__ = "Integer32"
_VrPpIpxPSnmpOperStatus_Object = MibTableColumn
vrPpIpxPSnmpOperStatus = _VrPpIpxPSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 104, 1, 1),
    _VrPpIpxPSnmpOperStatus_Type()
)
vrPpIpxPSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPSnmpOperStatus.setStatus("mandatory")
_VrPpIpxPOperTable_Object = MibTable
vrPpIpxPOperTable = _VrPpIpxPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105)
)
if mibBuilder.loadTexts:
    vrPpIpxPOperTable.setStatus("mandatory")
_VrPpIpxPOperEntry_Object = MibTableRow
vrPpIpxPOperEntry = _VrPpIpxPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105, 1)
)
vrPpIpxPOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPOperEntry.setStatus("mandatory")


class _VrPpIpxPType_Type(Integer32):
    """Custom type vrPpIpxPType based on Integer32"""
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


_VrPpIpxPType_Type.__name__ = "Integer32"
_VrPpIpxPType_Object = MibTableColumn
vrPpIpxPType = _VrPpIpxPType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105, 1, 1),
    _VrPpIpxPType_Type()
)
vrPpIpxPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPType.setStatus("mandatory")


class _VrPpIpxPEncapsulation_Type(Integer32):
    """Custom type vrPpIpxPEncapsulation based on Integer32"""
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


_VrPpIpxPEncapsulation_Type.__name__ = "Integer32"
_VrPpIpxPEncapsulation_Object = MibTableColumn
vrPpIpxPEncapsulation = _VrPpIpxPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105, 1, 2),
    _VrPpIpxPEncapsulation_Type()
)
vrPpIpxPEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPEncapsulation.setStatus("mandatory")


class _VrPpIpxPNetworkNumber_Type(DashedHexString):
    """Custom type vrPpIpxPNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VrPpIpxPNetworkNumber_Type.__name__ = "DashedHexString"
_VrPpIpxPNetworkNumber_Object = MibTableColumn
vrPpIpxPNetworkNumber = _VrPpIpxPNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105, 1, 3),
    _VrPpIpxPNetworkNumber_Type()
)
vrPpIpxPNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPNetworkNumber.setStatus("mandatory")


class _VrPpIpxPNode_Type(DashedHexString):
    """Custom type vrPpIpxPNode based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VrPpIpxPNode_Type.__name__ = "DashedHexString"
_VrPpIpxPNode_Object = MibTableColumn
vrPpIpxPNode = _VrPpIpxPNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 105, 1, 4),
    _VrPpIpxPNode_Type()
)
vrPpIpxPNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPNode.setStatus("mandatory")
_VrPpIpxPStatsTable_Object = MibTable
vrPpIpxPStatsTable = _VrPpIpxPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 106)
)
if mibBuilder.loadTexts:
    vrPpIpxPStatsTable.setStatus("mandatory")
_VrPpIpxPStatsEntry_Object = MibTableRow
vrPpIpxPStatsEntry = _VrPpIpxPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 106, 1)
)
vrPpIpxPStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrPpIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrPpIpxPIndex"),
)
if mibBuilder.loadTexts:
    vrPpIpxPStatsEntry.setStatus("mandatory")
_VrPpIpxPStateChanges_Type = Counter32
_VrPpIpxPStateChanges_Object = MibTableColumn
vrPpIpxPStateChanges = _VrPpIpxPStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 106, 1, 1),
    _VrPpIpxPStateChanges_Type()
)
vrPpIpxPStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPStateChanges.setStatus("mandatory")
_VrPpIpxPInReceives_Type = Counter32
_VrPpIpxPInReceives_Object = MibTableColumn
vrPpIpxPInReceives = _VrPpIpxPInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 106, 1, 2),
    _VrPpIpxPInReceives_Type()
)
vrPpIpxPInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPInReceives.setStatus("mandatory")
_VrPpIpxPForwarded_Type = Counter32
_VrPpIpxPForwarded_Object = MibTableColumn
vrPpIpxPForwarded = _VrPpIpxPForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 3, 6, 106, 1, 3),
    _VrPpIpxPForwarded_Type()
)
vrPpIpxPForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrPpIpxPForwarded.setStatus("mandatory")
_VrIpx_ObjectIdentity = ObjectIdentity
vrIpx = _VrIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7)
)
_VrIpxRowStatusTable_Object = MibTable
vrIpxRowStatusTable = _VrIpxRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1)
)
if mibBuilder.loadTexts:
    vrIpxRowStatusTable.setStatus("mandatory")
_VrIpxRowStatusEntry_Object = MibTableRow
vrIpxRowStatusEntry = _VrIpxRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1, 1)
)
vrIpxRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRowStatusEntry.setStatus("mandatory")
_VrIpxRowStatus_Type = RowStatus
_VrIpxRowStatus_Object = MibTableColumn
vrIpxRowStatus = _VrIpxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1, 1, 1),
    _VrIpxRowStatus_Type()
)
vrIpxRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRowStatus.setStatus("mandatory")
_VrIpxComponentName_Type = DisplayString
_VrIpxComponentName_Object = MibTableColumn
vrIpxComponentName = _VrIpxComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1, 1, 2),
    _VrIpxComponentName_Type()
)
vrIpxComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxComponentName.setStatus("mandatory")
_VrIpxStorageType_Type = StorageType
_VrIpxStorageType_Object = MibTableColumn
vrIpxStorageType = _VrIpxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1, 1, 4),
    _VrIpxStorageType_Type()
)
vrIpxStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxStorageType.setStatus("mandatory")
_VrIpxIndex_Type = NonReplicated
_VrIpxIndex_Object = MibTableColumn
vrIpxIndex = _VrIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 1, 1, 10),
    _VrIpxIndex_Type()
)
vrIpxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxIndex.setStatus("mandatory")
_VrIpxRip_ObjectIdentity = ObjectIdentity
vrIpxRip = _VrIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2)
)
_VrIpxRipRowStatusTable_Object = MibTable
vrIpxRipRowStatusTable = _VrIpxRipRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpxRipRowStatusTable.setStatus("mandatory")
_VrIpxRipRowStatusEntry_Object = MibTableRow
vrIpxRipRowStatusEntry = _VrIpxRipRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1, 1)
)
vrIpxRipRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRowStatusEntry.setStatus("mandatory")
_VrIpxRipRowStatus_Type = RowStatus
_VrIpxRipRowStatus_Object = MibTableColumn
vrIpxRipRowStatus = _VrIpxRipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1, 1, 1),
    _VrIpxRipRowStatus_Type()
)
vrIpxRipRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRowStatus.setStatus("mandatory")
_VrIpxRipComponentName_Type = DisplayString
_VrIpxRipComponentName_Object = MibTableColumn
vrIpxRipComponentName = _VrIpxRipComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1, 1, 2),
    _VrIpxRipComponentName_Type()
)
vrIpxRipComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipComponentName.setStatus("mandatory")
_VrIpxRipStorageType_Type = StorageType
_VrIpxRipStorageType_Object = MibTableColumn
vrIpxRipStorageType = _VrIpxRipStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1, 1, 4),
    _VrIpxRipStorageType_Type()
)
vrIpxRipStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipStorageType.setStatus("mandatory")
_VrIpxRipIndex_Type = NonReplicated
_VrIpxRipIndex_Object = MibTableColumn
vrIpxRipIndex = _VrIpxRipIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 1, 1, 10),
    _VrIpxRipIndex_Type()
)
vrIpxRipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxRipIndex.setStatus("mandatory")
_VrIpxRipRFltr_ObjectIdentity = ObjectIdentity
vrIpxRipRFltr = _VrIpxRipRFltr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2)
)
_VrIpxRipRFltrRowStatusTable_Object = MibTable
vrIpxRipRFltrRowStatusTable = _VrIpxRipRFltrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrRowStatusTable.setStatus("mandatory")
_VrIpxRipRFltrRowStatusEntry_Object = MibTableRow
vrIpxRipRFltrRowStatusEntry = _VrIpxRipRFltrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1, 1)
)
vrIpxRipRFltrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrRowStatusEntry.setStatus("mandatory")
_VrIpxRipRFltrRowStatus_Type = RowStatus
_VrIpxRipRFltrRowStatus_Object = MibTableColumn
vrIpxRipRFltrRowStatus = _VrIpxRipRFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1, 1, 1),
    _VrIpxRipRFltrRowStatus_Type()
)
vrIpxRipRFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrRowStatus.setStatus("mandatory")
_VrIpxRipRFltrComponentName_Type = DisplayString
_VrIpxRipRFltrComponentName_Object = MibTableColumn
vrIpxRipRFltrComponentName = _VrIpxRipRFltrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1, 1, 2),
    _VrIpxRipRFltrComponentName_Type()
)
vrIpxRipRFltrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRFltrComponentName.setStatus("mandatory")
_VrIpxRipRFltrStorageType_Type = StorageType
_VrIpxRipRFltrStorageType_Object = MibTableColumn
vrIpxRipRFltrStorageType = _VrIpxRipRFltrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1, 1, 4),
    _VrIpxRipRFltrStorageType_Type()
)
vrIpxRipRFltrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRFltrStorageType.setStatus("mandatory")


class _VrIpxRipRFltrIdentifierIndex_Type(Integer32):
    """Custom type vrIpxRipRFltrIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrIpxRipRFltrIdentifierIndex_Type.__name__ = "Integer32"
_VrIpxRipRFltrIdentifierIndex_Object = MibTableColumn
vrIpxRipRFltrIdentifierIndex = _VrIpxRipRFltrIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 1, 1, 10),
    _VrIpxRipRFltrIdentifierIndex_Type()
)
vrIpxRipRFltrIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxRipRFltrIdentifierIndex.setStatus("mandatory")
_VrIpxRipRFltrProvTable_Object = MibTable
vrIpxRipRFltrProvTable = _VrIpxRipRFltrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrProvTable.setStatus("mandatory")
_VrIpxRipRFltrProvEntry_Object = MibTableRow
vrIpxRipRFltrProvEntry = _VrIpxRipRFltrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1)
)
vrIpxRipRFltrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrProvEntry.setStatus("mandatory")


class _VrIpxRipRFltrHops_Type(AsciiString):
    """Custom type vrIpxRipRFltrHops based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VrIpxRipRFltrHops_Type.__name__ = "AsciiString"
_VrIpxRipRFltrHops_Object = MibTableColumn
vrIpxRipRFltrHops = _VrIpxRipRFltrHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 1),
    _VrIpxRipRFltrHops_Type()
)
vrIpxRipRFltrHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrHops.setStatus("mandatory")


class _VrIpxRipRFltrTicks_Type(AsciiString):
    """Custom type vrIpxRipRFltrTicks based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VrIpxRipRFltrTicks_Type.__name__ = "AsciiString"
_VrIpxRipRFltrTicks_Object = MibTableColumn
vrIpxRipRFltrTicks = _VrIpxRipRFltrTicks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 2),
    _VrIpxRipRFltrTicks_Type()
)
vrIpxRipRFltrTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrTicks.setStatus("mandatory")


class _VrIpxRipRFltrNetworkNumber_Type(AsciiString):
    """Custom type vrIpxRipRFltrNetworkNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VrIpxRipRFltrNetworkNumber_Type.__name__ = "AsciiString"
_VrIpxRipRFltrNetworkNumber_Object = MibTableColumn
vrIpxRipRFltrNetworkNumber = _VrIpxRipRFltrNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 3),
    _VrIpxRipRFltrNetworkNumber_Type()
)
vrIpxRipRFltrNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrNetworkNumber.setStatus("mandatory")


class _VrIpxRipRFltrNode_Type(AsciiString):
    """Custom type vrIpxRipRFltrNode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_VrIpxRipRFltrNode_Type.__name__ = "AsciiString"
_VrIpxRipRFltrNode_Object = MibTableColumn
vrIpxRipRFltrNode = _VrIpxRipRFltrNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 4),
    _VrIpxRipRFltrNode_Type()
)
vrIpxRipRFltrNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrNode.setStatus("mandatory")


class _VrIpxRipRFltrPort_Type(AsciiString):
    """Custom type vrIpxRipRFltrPort based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_VrIpxRipRFltrPort_Type.__name__ = "AsciiString"
_VrIpxRipRFltrPort_Object = MibTableColumn
vrIpxRipRFltrPort = _VrIpxRipRFltrPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 5),
    _VrIpxRipRFltrPort_Type()
)
vrIpxRipRFltrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrPort.setStatus("mandatory")


class _VrIpxRipRFltrDisposition_Type(Integer32):
    """Custom type vrIpxRipRFltrDisposition based on Integer32"""
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


_VrIpxRipRFltrDisposition_Type.__name__ = "Integer32"
_VrIpxRipRFltrDisposition_Object = MibTableColumn
vrIpxRipRFltrDisposition = _VrIpxRipRFltrDisposition_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 10, 1, 6),
    _VrIpxRipRFltrDisposition_Type()
)
vrIpxRipRFltrDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRFltrDisposition.setStatus("mandatory")
_VrIpxRipRFltrOperTable_Object = MibTable
vrIpxRipRFltrOperTable = _VrIpxRipRFltrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrOperTable.setStatus("mandatory")
_VrIpxRipRFltrOperEntry_Object = MibTableRow
vrIpxRipRFltrOperEntry = _VrIpxRipRFltrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 11, 1)
)
vrIpxRipRFltrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRFltrOperEntry.setStatus("mandatory")


class _VrIpxRipRFltrNumberOfApplyEntries_Type(Gauge32):
    """Custom type vrIpxRipRFltrNumberOfApplyEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpxRipRFltrNumberOfApplyEntries_Type.__name__ = "Gauge32"
_VrIpxRipRFltrNumberOfApplyEntries_Object = MibTableColumn
vrIpxRipRFltrNumberOfApplyEntries = _VrIpxRipRFltrNumberOfApplyEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 2, 11, 1, 1),
    _VrIpxRipRFltrNumberOfApplyEntries_Type()
)
vrIpxRipRFltrNumberOfApplyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRFltrNumberOfApplyEntries.setStatus("mandatory")
_VrIpxRipRipApp_ObjectIdentity = ObjectIdentity
vrIpxRipRipApp = _VrIpxRipRipApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3)
)
_VrIpxRipRipAppRowStatusTable_Object = MibTable
vrIpxRipRipAppRowStatusTable = _VrIpxRipRipAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpxRipRipAppRowStatusTable.setStatus("mandatory")
_VrIpxRipRipAppRowStatusEntry_Object = MibTableRow
vrIpxRipRipAppRowStatusEntry = _VrIpxRipRipAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1)
)
vrIpxRipRipAppRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRipAppProtocolPortNameIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRipAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRipAppRowStatusEntry.setStatus("mandatory")
_VrIpxRipRipAppRowStatus_Type = RowStatus
_VrIpxRipRipAppRowStatus_Object = MibTableColumn
vrIpxRipRipAppRowStatus = _VrIpxRipRipAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1, 1),
    _VrIpxRipRipAppRowStatus_Type()
)
vrIpxRipRipAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRipAppRowStatus.setStatus("mandatory")
_VrIpxRipRipAppComponentName_Type = DisplayString
_VrIpxRipRipAppComponentName_Object = MibTableColumn
vrIpxRipRipAppComponentName = _VrIpxRipRipAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1, 2),
    _VrIpxRipRipAppComponentName_Type()
)
vrIpxRipRipAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRipAppComponentName.setStatus("mandatory")
_VrIpxRipRipAppStorageType_Type = StorageType
_VrIpxRipRipAppStorageType_Object = MibTableColumn
vrIpxRipRipAppStorageType = _VrIpxRipRipAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1, 4),
    _VrIpxRipRipAppStorageType_Type()
)
vrIpxRipRipAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRipAppStorageType.setStatus("mandatory")


class _VrIpxRipRipAppProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type vrIpxRipRipAppProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpxRipRipAppProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_VrIpxRipRipAppProtocolPortNameIndex_Object = MibTableColumn
vrIpxRipRipAppProtocolPortNameIndex = _VrIpxRipRipAppProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1, 10),
    _VrIpxRipRipAppProtocolPortNameIndex_Type()
)
vrIpxRipRipAppProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxRipRipAppProtocolPortNameIndex.setStatus("mandatory")


class _VrIpxRipRipAppFilterIdentifierIndex_Type(Integer32):
    """Custom type vrIpxRipRipAppFilterIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrIpxRipRipAppFilterIdentifierIndex_Type.__name__ = "Integer32"
_VrIpxRipRipAppFilterIdentifierIndex_Object = MibTableColumn
vrIpxRipRipAppFilterIdentifierIndex = _VrIpxRipRipAppFilterIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 1, 1, 11),
    _VrIpxRipRipAppFilterIdentifierIndex_Type()
)
vrIpxRipRipAppFilterIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxRipRipAppFilterIdentifierIndex.setStatus("mandatory")
_VrIpxRipRipAppProvTable_Object = MibTable
vrIpxRipRipAppProvTable = _VrIpxRipRipAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpxRipRipAppProvTable.setStatus("mandatory")
_VrIpxRipRipAppProvEntry_Object = MibTableRow
vrIpxRipRipAppProvEntry = _VrIpxRipRipAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 10, 1)
)
vrIpxRipRipAppProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRipAppProtocolPortNameIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipRipAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipRipAppProvEntry.setStatus("mandatory")


class _VrIpxRipRipAppDirection_Type(Integer32):
    """Custom type vrIpxRipRipAppDirection based on Integer32"""
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


_VrIpxRipRipAppDirection_Type.__name__ = "Integer32"
_VrIpxRipRipAppDirection_Object = MibTableColumn
vrIpxRipRipAppDirection = _VrIpxRipRipAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 3, 10, 1, 1),
    _VrIpxRipRipAppDirection_Type()
)
vrIpxRipRipAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipRipAppDirection.setStatus("mandatory")
_VrIpxRipStatsTable_Object = MibTable
vrIpxRipStatsTable = _VrIpxRipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpxRipStatsTable.setStatus("mandatory")
_VrIpxRipStatsEntry_Object = MibTableRow
vrIpxRipStatsEntry = _VrIpxRipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 10, 1)
)
vrIpxRipStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxRipIndex"),
)
if mibBuilder.loadTexts:
    vrIpxRipStatsEntry.setStatus("mandatory")
_VrIpxRipRipIn_Type = Counter32
_VrIpxRipRipIn_Object = MibTableColumn
vrIpxRipRipIn = _VrIpxRipRipIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 10, 1, 1),
    _VrIpxRipRipIn_Type()
)
vrIpxRipRipIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRipIn.setStatus("mandatory")
_VrIpxRipRipOut_Type = Counter32
_VrIpxRipRipOut_Object = MibTableColumn
vrIpxRipRipOut = _VrIpxRipRipOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 10, 1, 2),
    _VrIpxRipRipOut_Type()
)
vrIpxRipRipOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRipOut.setStatus("mandatory")
_VrIpxRipRipIncorrectPackets_Type = Counter32
_VrIpxRipRipIncorrectPackets_Object = MibTableColumn
vrIpxRipRipIncorrectPackets = _VrIpxRipRipIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 2, 10, 1, 3),
    _VrIpxRipRipIncorrectPackets_Type()
)
vrIpxRipRipIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxRipRipIncorrectPackets.setStatus("mandatory")
_VrIpxSap_ObjectIdentity = ObjectIdentity
vrIpxSap = _VrIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3)
)
_VrIpxSapRowStatusTable_Object = MibTable
vrIpxSapRowStatusTable = _VrIpxSapRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpxSapRowStatusTable.setStatus("mandatory")
_VrIpxSapRowStatusEntry_Object = MibTableRow
vrIpxSapRowStatusEntry = _VrIpxSapRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1, 1)
)
vrIpxSapRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapRowStatusEntry.setStatus("mandatory")
_VrIpxSapRowStatus_Type = RowStatus
_VrIpxSapRowStatus_Object = MibTableColumn
vrIpxSapRowStatus = _VrIpxSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1, 1, 1),
    _VrIpxSapRowStatus_Type()
)
vrIpxSapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapRowStatus.setStatus("mandatory")
_VrIpxSapComponentName_Type = DisplayString
_VrIpxSapComponentName_Object = MibTableColumn
vrIpxSapComponentName = _VrIpxSapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1, 1, 2),
    _VrIpxSapComponentName_Type()
)
vrIpxSapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapComponentName.setStatus("mandatory")
_VrIpxSapStorageType_Type = StorageType
_VrIpxSapStorageType_Object = MibTableColumn
vrIpxSapStorageType = _VrIpxSapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1, 1, 4),
    _VrIpxSapStorageType_Type()
)
vrIpxSapStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapStorageType.setStatus("mandatory")
_VrIpxSapIndex_Type = NonReplicated
_VrIpxSapIndex_Object = MibTableColumn
vrIpxSapIndex = _VrIpxSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 1, 1, 10),
    _VrIpxSapIndex_Type()
)
vrIpxSapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSapIndex.setStatus("mandatory")
_VrIpxSapSFltr_ObjectIdentity = ObjectIdentity
vrIpxSapSFltr = _VrIpxSapSFltr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2)
)
_VrIpxSapSFltrRowStatusTable_Object = MibTable
vrIpxSapSFltrRowStatusTable = _VrIpxSapSFltrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrRowStatusTable.setStatus("mandatory")
_VrIpxSapSFltrRowStatusEntry_Object = MibTableRow
vrIpxSapSFltrRowStatusEntry = _VrIpxSapSFltrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1, 1)
)
vrIpxSapSFltrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrRowStatusEntry.setStatus("mandatory")
_VrIpxSapSFltrRowStatus_Type = RowStatus
_VrIpxSapSFltrRowStatus_Object = MibTableColumn
vrIpxSapSFltrRowStatus = _VrIpxSapSFltrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1, 1, 1),
    _VrIpxSapSFltrRowStatus_Type()
)
vrIpxSapSFltrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrRowStatus.setStatus("mandatory")
_VrIpxSapSFltrComponentName_Type = DisplayString
_VrIpxSapSFltrComponentName_Object = MibTableColumn
vrIpxSapSFltrComponentName = _VrIpxSapSFltrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1, 1, 2),
    _VrIpxSapSFltrComponentName_Type()
)
vrIpxSapSFltrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSFltrComponentName.setStatus("mandatory")
_VrIpxSapSFltrStorageType_Type = StorageType
_VrIpxSapSFltrStorageType_Object = MibTableColumn
vrIpxSapSFltrStorageType = _VrIpxSapSFltrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1, 1, 4),
    _VrIpxSapSFltrStorageType_Type()
)
vrIpxSapSFltrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSFltrStorageType.setStatus("mandatory")


class _VrIpxSapSFltrIdentifierIndex_Type(Integer32):
    """Custom type vrIpxSapSFltrIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrIpxSapSFltrIdentifierIndex_Type.__name__ = "Integer32"
_VrIpxSapSFltrIdentifierIndex_Object = MibTableColumn
vrIpxSapSFltrIdentifierIndex = _VrIpxSapSFltrIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 1, 1, 10),
    _VrIpxSapSFltrIdentifierIndex_Type()
)
vrIpxSapSFltrIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSapSFltrIdentifierIndex.setStatus("mandatory")
_VrIpxSapSFltrProvTable_Object = MibTable
vrIpxSapSFltrProvTable = _VrIpxSapSFltrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrProvTable.setStatus("mandatory")
_VrIpxSapSFltrProvEntry_Object = MibTableRow
vrIpxSapSFltrProvEntry = _VrIpxSapSFltrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1)
)
vrIpxSapSFltrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrProvEntry.setStatus("mandatory")


class _VrIpxSapSFltrType_Type(AsciiString):
    """Custom type vrIpxSapSFltrType based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_VrIpxSapSFltrType_Type.__name__ = "AsciiString"
_VrIpxSapSFltrType_Object = MibTableColumn
vrIpxSapSFltrType = _VrIpxSapSFltrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1, 1),
    _VrIpxSapSFltrType_Type()
)
vrIpxSapSFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrType.setStatus("mandatory")


class _VrIpxSapSFltrName_Type(AsciiString):
    """Custom type vrIpxSapSFltrName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_VrIpxSapSFltrName_Type.__name__ = "AsciiString"
_VrIpxSapSFltrName_Object = MibTableColumn
vrIpxSapSFltrName = _VrIpxSapSFltrName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1, 2),
    _VrIpxSapSFltrName_Type()
)
vrIpxSapSFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrName.setStatus("mandatory")


class _VrIpxSapSFltrNetworkNumber_Type(AsciiString):
    """Custom type vrIpxSapSFltrNetworkNumber based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VrIpxSapSFltrNetworkNumber_Type.__name__ = "AsciiString"
_VrIpxSapSFltrNetworkNumber_Object = MibTableColumn
vrIpxSapSFltrNetworkNumber = _VrIpxSapSFltrNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1, 3),
    _VrIpxSapSFltrNetworkNumber_Type()
)
vrIpxSapSFltrNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrNetworkNumber.setStatus("mandatory")


class _VrIpxSapSFltrNode_Type(AsciiString):
    """Custom type vrIpxSapSFltrNode based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_VrIpxSapSFltrNode_Type.__name__ = "AsciiString"
_VrIpxSapSFltrNode_Object = MibTableColumn
vrIpxSapSFltrNode = _VrIpxSapSFltrNode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1, 4),
    _VrIpxSapSFltrNode_Type()
)
vrIpxSapSFltrNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrNode.setStatus("mandatory")


class _VrIpxSapSFltrDisposition_Type(Integer32):
    """Custom type vrIpxSapSFltrDisposition based on Integer32"""
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


_VrIpxSapSFltrDisposition_Type.__name__ = "Integer32"
_VrIpxSapSFltrDisposition_Object = MibTableColumn
vrIpxSapSFltrDisposition = _VrIpxSapSFltrDisposition_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 10, 1, 5),
    _VrIpxSapSFltrDisposition_Type()
)
vrIpxSapSFltrDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSFltrDisposition.setStatus("mandatory")
_VrIpxSapSFltrOperTable_Object = MibTable
vrIpxSapSFltrOperTable = _VrIpxSapSFltrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrOperTable.setStatus("mandatory")
_VrIpxSapSFltrOperEntry_Object = MibTableRow
vrIpxSapSFltrOperEntry = _VrIpxSapSFltrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 11, 1)
)
vrIpxSapSFltrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSFltrIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapSFltrOperEntry.setStatus("mandatory")


class _VrIpxSapSFltrNumberOfApplyEntries_Type(Gauge32):
    """Custom type vrIpxSapSFltrNumberOfApplyEntries based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpxSapSFltrNumberOfApplyEntries_Type.__name__ = "Gauge32"
_VrIpxSapSFltrNumberOfApplyEntries_Object = MibTableColumn
vrIpxSapSFltrNumberOfApplyEntries = _VrIpxSapSFltrNumberOfApplyEntries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 2, 11, 1, 1),
    _VrIpxSapSFltrNumberOfApplyEntries_Type()
)
vrIpxSapSFltrNumberOfApplyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSFltrNumberOfApplyEntries.setStatus("mandatory")
_VrIpxSapSapApp_ObjectIdentity = ObjectIdentity
vrIpxSapSapApp = _VrIpxSapSapApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3)
)
_VrIpxSapSapAppRowStatusTable_Object = MibTable
vrIpxSapSapAppRowStatusTable = _VrIpxSapSapAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpxSapSapAppRowStatusTable.setStatus("mandatory")
_VrIpxSapSapAppRowStatusEntry_Object = MibTableRow
vrIpxSapSapAppRowStatusEntry = _VrIpxSapSapAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1)
)
vrIpxSapSapAppRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSapAppProtocolPortNameIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSapAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapSapAppRowStatusEntry.setStatus("mandatory")
_VrIpxSapSapAppRowStatus_Type = RowStatus
_VrIpxSapSapAppRowStatus_Object = MibTableColumn
vrIpxSapSapAppRowStatus = _VrIpxSapSapAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1, 1),
    _VrIpxSapSapAppRowStatus_Type()
)
vrIpxSapSapAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSapAppRowStatus.setStatus("mandatory")
_VrIpxSapSapAppComponentName_Type = DisplayString
_VrIpxSapSapAppComponentName_Object = MibTableColumn
vrIpxSapSapAppComponentName = _VrIpxSapSapAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1, 2),
    _VrIpxSapSapAppComponentName_Type()
)
vrIpxSapSapAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSapAppComponentName.setStatus("mandatory")
_VrIpxSapSapAppStorageType_Type = StorageType
_VrIpxSapSapAppStorageType_Object = MibTableColumn
vrIpxSapSapAppStorageType = _VrIpxSapSapAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1, 4),
    _VrIpxSapSapAppStorageType_Type()
)
vrIpxSapSapAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSapAppStorageType.setStatus("mandatory")


class _VrIpxSapSapAppProtocolPortNameIndex_Type(AsciiStringIndex):
    """Custom type vrIpxSapSapAppProtocolPortNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpxSapSapAppProtocolPortNameIndex_Type.__name__ = "AsciiStringIndex"
_VrIpxSapSapAppProtocolPortNameIndex_Object = MibTableColumn
vrIpxSapSapAppProtocolPortNameIndex = _VrIpxSapSapAppProtocolPortNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1, 10),
    _VrIpxSapSapAppProtocolPortNameIndex_Type()
)
vrIpxSapSapAppProtocolPortNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSapSapAppProtocolPortNameIndex.setStatus("mandatory")


class _VrIpxSapSapAppFilterIdentifierIndex_Type(Integer32):
    """Custom type vrIpxSapSapAppFilterIdentifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrIpxSapSapAppFilterIdentifierIndex_Type.__name__ = "Integer32"
_VrIpxSapSapAppFilterIdentifierIndex_Object = MibTableColumn
vrIpxSapSapAppFilterIdentifierIndex = _VrIpxSapSapAppFilterIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 1, 1, 11),
    _VrIpxSapSapAppFilterIdentifierIndex_Type()
)
vrIpxSapSapAppFilterIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSapSapAppFilterIdentifierIndex.setStatus("mandatory")
_VrIpxSapSapAppProvTable_Object = MibTable
vrIpxSapSapAppProvTable = _VrIpxSapSapAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpxSapSapAppProvTable.setStatus("mandatory")
_VrIpxSapSapAppProvEntry_Object = MibTableRow
vrIpxSapSapAppProvEntry = _VrIpxSapSapAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 10, 1)
)
vrIpxSapSapAppProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSapAppProtocolPortNameIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapSapAppFilterIdentifierIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapSapAppProvEntry.setStatus("mandatory")


class _VrIpxSapSapAppDirection_Type(Integer32):
    """Custom type vrIpxSapSapAppDirection based on Integer32"""
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


_VrIpxSapSapAppDirection_Type.__name__ = "Integer32"
_VrIpxSapSapAppDirection_Object = MibTableColumn
vrIpxSapSapAppDirection = _VrIpxSapSapAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 3, 10, 1, 1),
    _VrIpxSapSapAppDirection_Type()
)
vrIpxSapSapAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapSapAppDirection.setStatus("mandatory")
_VrIpxSapStatsTable_Object = MibTable
vrIpxSapStatsTable = _VrIpxSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpxSapStatsTable.setStatus("mandatory")
_VrIpxSapStatsEntry_Object = MibTableRow
vrIpxSapStatsEntry = _VrIpxSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 10, 1)
)
vrIpxSapStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSapIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSapStatsEntry.setStatus("mandatory")
_VrIpxSapSapIn_Type = Counter32
_VrIpxSapSapIn_Object = MibTableColumn
vrIpxSapSapIn = _VrIpxSapSapIn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 10, 1, 1),
    _VrIpxSapSapIn_Type()
)
vrIpxSapSapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSapIn.setStatus("mandatory")
_VrIpxSapSapOut_Type = Counter32
_VrIpxSapSapOut_Object = MibTableColumn
vrIpxSapSapOut = _VrIpxSapSapOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 10, 1, 2),
    _VrIpxSapSapOut_Type()
)
vrIpxSapSapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSapOut.setStatus("mandatory")
_VrIpxSapSapIncorrectPackets_Type = Counter32
_VrIpxSapSapIncorrectPackets_Object = MibTableColumn
vrIpxSapSapIncorrectPackets = _VrIpxSapSapIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 3, 10, 1, 3),
    _VrIpxSapSapIncorrectPackets_Type()
)
vrIpxSapSapIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSapSapIncorrectPackets.setStatus("mandatory")
_VrIpxFwd_ObjectIdentity = ObjectIdentity
vrIpxFwd = _VrIpxFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4)
)
_VrIpxFwdRowStatusTable_Object = MibTable
vrIpxFwdRowStatusTable = _VrIpxFwdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpxFwdRowStatusTable.setStatus("mandatory")
_VrIpxFwdRowStatusEntry_Object = MibTableRow
vrIpxFwdRowStatusEntry = _VrIpxFwdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1, 1)
)
vrIpxFwdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxFwdNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    vrIpxFwdRowStatusEntry.setStatus("mandatory")
_VrIpxFwdRowStatus_Type = RowStatus
_VrIpxFwdRowStatus_Object = MibTableColumn
vrIpxFwdRowStatus = _VrIpxFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1, 1, 1),
    _VrIpxFwdRowStatus_Type()
)
vrIpxFwdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdRowStatus.setStatus("mandatory")
_VrIpxFwdComponentName_Type = DisplayString
_VrIpxFwdComponentName_Object = MibTableColumn
vrIpxFwdComponentName = _VrIpxFwdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1, 1, 2),
    _VrIpxFwdComponentName_Type()
)
vrIpxFwdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdComponentName.setStatus("mandatory")
_VrIpxFwdStorageType_Type = StorageType
_VrIpxFwdStorageType_Object = MibTableColumn
vrIpxFwdStorageType = _VrIpxFwdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1, 1, 4),
    _VrIpxFwdStorageType_Type()
)
vrIpxFwdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdStorageType.setStatus("mandatory")


class _VrIpxFwdNetworkNumberIndex_Type(DashedHexString):
    """Custom type vrIpxFwdNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrIpxFwdNetworkNumberIndex_Type.__name__ = "DashedHexString"
_VrIpxFwdNetworkNumberIndex_Object = MibTableColumn
vrIpxFwdNetworkNumberIndex = _VrIpxFwdNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 1, 1, 10),
    _VrIpxFwdNetworkNumberIndex_Type()
)
vrIpxFwdNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxFwdNetworkNumberIndex.setStatus("mandatory")
_VrIpxFwdOperTable_Object = MibTable
vrIpxFwdOperTable = _VrIpxFwdOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpxFwdOperTable.setStatus("mandatory")
_VrIpxFwdOperEntry_Object = MibTableRow
vrIpxFwdOperEntry = _VrIpxFwdOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1)
)
vrIpxFwdOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxFwdNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    vrIpxFwdOperEntry.setStatus("mandatory")


class _VrIpxFwdProtocol_Type(Integer32):
    """Custom type vrIpxFwdProtocol based on Integer32"""
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


_VrIpxFwdProtocol_Type.__name__ = "Integer32"
_VrIpxFwdProtocol_Object = MibTableColumn
vrIpxFwdProtocol = _VrIpxFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 1),
    _VrIpxFwdProtocol_Type()
)
vrIpxFwdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdProtocol.setStatus("mandatory")


class _VrIpxFwdTicks_Type(Unsigned32):
    """Custom type vrIpxFwdTicks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpxFwdTicks_Type.__name__ = "Unsigned32"
_VrIpxFwdTicks_Object = MibTableColumn
vrIpxFwdTicks = _VrIpxFwdTicks_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 2),
    _VrIpxFwdTicks_Type()
)
vrIpxFwdTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdTicks.setStatus("mandatory")


class _VrIpxFwdHopCount_Type(Gauge32):
    """Custom type vrIpxFwdHopCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VrIpxFwdHopCount_Type.__name__ = "Gauge32"
_VrIpxFwdHopCount_Object = MibTableColumn
vrIpxFwdHopCount = _VrIpxFwdHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 3),
    _VrIpxFwdHopCount_Type()
)
vrIpxFwdHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdHopCount.setStatus("mandatory")


class _VrIpxFwdProtocolPortId_Type(AsciiString):
    """Custom type vrIpxFwdProtocolPortId based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpxFwdProtocolPortId_Type.__name__ = "AsciiString"
_VrIpxFwdProtocolPortId_Object = MibTableColumn
vrIpxFwdProtocolPortId = _VrIpxFwdProtocolPortId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 4),
    _VrIpxFwdProtocolPortId_Type()
)
vrIpxFwdProtocolPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdProtocolPortId.setStatus("mandatory")


class _VrIpxFwdNextHopPhysAddress_Type(PhysAddress):
    """Custom type vrIpxFwdNextHopPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VrIpxFwdNextHopPhysAddress_Type.__name__ = "PhysAddress"
_VrIpxFwdNextHopPhysAddress_Object = MibTableColumn
vrIpxFwdNextHopPhysAddress = _VrIpxFwdNextHopPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 5),
    _VrIpxFwdNextHopPhysAddress_Type()
)
vrIpxFwdNextHopPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdNextHopPhysAddress.setStatus("mandatory")


class _VrIpxFwdNextHopNetworkNumber_Type(DashedHexString):
    """Custom type vrIpxFwdNextHopNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrIpxFwdNextHopNetworkNumber_Type.__name__ = "DashedHexString"
_VrIpxFwdNextHopNetworkNumber_Object = MibTableColumn
vrIpxFwdNextHopNetworkNumber = _VrIpxFwdNextHopNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 4, 10, 1, 6),
    _VrIpxFwdNextHopNetworkNumber_Type()
)
vrIpxFwdNextHopNetworkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxFwdNextHopNetworkNumber.setStatus("mandatory")
_VrIpxSrvc_ObjectIdentity = ObjectIdentity
vrIpxSrvc = _VrIpxSrvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5)
)
_VrIpxSrvcRowStatusTable_Object = MibTable
vrIpxSrvcRowStatusTable = _VrIpxSrvcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1)
)
if mibBuilder.loadTexts:
    vrIpxSrvcRowStatusTable.setStatus("mandatory")
_VrIpxSrvcRowStatusEntry_Object = MibTableRow
vrIpxSrvcRowStatusEntry = _VrIpxSrvcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1)
)
vrIpxSrvcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNetworkNumberIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNodeIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNameIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSrvcRowStatusEntry.setStatus("mandatory")
_VrIpxSrvcRowStatus_Type = RowStatus
_VrIpxSrvcRowStatus_Object = MibTableColumn
vrIpxSrvcRowStatus = _VrIpxSrvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 1),
    _VrIpxSrvcRowStatus_Type()
)
vrIpxSrvcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcRowStatus.setStatus("mandatory")
_VrIpxSrvcComponentName_Type = DisplayString
_VrIpxSrvcComponentName_Object = MibTableColumn
vrIpxSrvcComponentName = _VrIpxSrvcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 2),
    _VrIpxSrvcComponentName_Type()
)
vrIpxSrvcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcComponentName.setStatus("mandatory")
_VrIpxSrvcStorageType_Type = StorageType
_VrIpxSrvcStorageType_Object = MibTableColumn
vrIpxSrvcStorageType = _VrIpxSrvcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 4),
    _VrIpxSrvcStorageType_Type()
)
vrIpxSrvcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcStorageType.setStatus("mandatory")


class _VrIpxSrvcNetworkNumberIndex_Type(DashedHexString):
    """Custom type vrIpxSrvcNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrIpxSrvcNetworkNumberIndex_Type.__name__ = "DashedHexString"
_VrIpxSrvcNetworkNumberIndex_Object = MibTableColumn
vrIpxSrvcNetworkNumberIndex = _VrIpxSrvcNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 10),
    _VrIpxSrvcNetworkNumberIndex_Type()
)
vrIpxSrvcNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSrvcNetworkNumberIndex.setStatus("mandatory")


class _VrIpxSrvcNodeIndex_Type(DashedHexString):
    """Custom type vrIpxSrvcNodeIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VrIpxSrvcNodeIndex_Type.__name__ = "DashedHexString"
_VrIpxSrvcNodeIndex_Object = MibTableColumn
vrIpxSrvcNodeIndex = _VrIpxSrvcNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 11),
    _VrIpxSrvcNodeIndex_Type()
)
vrIpxSrvcNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSrvcNodeIndex.setStatus("mandatory")


class _VrIpxSrvcTypeIndex_Type(Integer32):
    """Custom type vrIpxSrvcTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpxSrvcTypeIndex_Type.__name__ = "Integer32"
_VrIpxSrvcTypeIndex_Object = MibTableColumn
vrIpxSrvcTypeIndex = _VrIpxSrvcTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 12),
    _VrIpxSrvcTypeIndex_Type()
)
vrIpxSrvcTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSrvcTypeIndex.setStatus("mandatory")


class _VrIpxSrvcNameIndex_Type(AsciiStringIndex):
    """Custom type vrIpxSrvcNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_VrIpxSrvcNameIndex_Type.__name__ = "AsciiStringIndex"
_VrIpxSrvcNameIndex_Object = MibTableColumn
vrIpxSrvcNameIndex = _VrIpxSrvcNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 1, 1, 13),
    _VrIpxSrvcNameIndex_Type()
)
vrIpxSrvcNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxSrvcNameIndex.setStatus("mandatory")
_VrIpxSrvcOperTable_Object = MibTable
vrIpxSrvcOperTable = _VrIpxSrvcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 10)
)
if mibBuilder.loadTexts:
    vrIpxSrvcOperTable.setStatus("mandatory")
_VrIpxSrvcOperEntry_Object = MibTableRow
vrIpxSrvcOperEntry = _VrIpxSrvcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 10, 1)
)
vrIpxSrvcOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNetworkNumberIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNodeIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcTypeIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxSrvcNameIndex"),
)
if mibBuilder.loadTexts:
    vrIpxSrvcOperEntry.setStatus("mandatory")


class _VrIpxSrvcSocket_Type(Hex):
    """Custom type vrIpxSrvcSocket based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpxSrvcSocket_Type.__name__ = "Hex"
_VrIpxSrvcSocket_Object = MibTableColumn
vrIpxSrvcSocket = _VrIpxSrvcSocket_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 10, 1, 1),
    _VrIpxSrvcSocket_Type()
)
vrIpxSrvcSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcSocket.setStatus("mandatory")


class _VrIpxSrvcProtocol_Type(Integer32):
    """Custom type vrIpxSrvcProtocol based on Integer32"""
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


_VrIpxSrvcProtocol_Type.__name__ = "Integer32"
_VrIpxSrvcProtocol_Object = MibTableColumn
vrIpxSrvcProtocol = _VrIpxSrvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 10, 1, 2),
    _VrIpxSrvcProtocol_Type()
)
vrIpxSrvcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcProtocol.setStatus("mandatory")


class _VrIpxSrvcHopCount_Type(Gauge32):
    """Custom type vrIpxSrvcHopCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VrIpxSrvcHopCount_Type.__name__ = "Gauge32"
_VrIpxSrvcHopCount_Object = MibTableColumn
vrIpxSrvcHopCount = _VrIpxSrvcHopCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 5, 10, 1, 3),
    _VrIpxSrvcHopCount_Type()
)
vrIpxSrvcHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSrvcHopCount.setStatus("mandatory")
_VrIpxAdj_ObjectIdentity = ObjectIdentity
vrIpxAdj = _VrIpxAdj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6)
)
_VrIpxAdjRowStatusTable_Object = MibTable
vrIpxAdjRowStatusTable = _VrIpxAdjRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpxAdjRowStatusTable.setStatus("mandatory")
_VrIpxAdjRowStatusEntry_Object = MibTableRow
vrIpxAdjRowStatusEntry = _VrIpxAdjRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1)
)
vrIpxAdjRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxAdjProtocolPortIdentifierIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxAdjNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    vrIpxAdjRowStatusEntry.setStatus("mandatory")
_VrIpxAdjRowStatus_Type = RowStatus
_VrIpxAdjRowStatus_Object = MibTableColumn
vrIpxAdjRowStatus = _VrIpxAdjRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1, 1),
    _VrIpxAdjRowStatus_Type()
)
vrIpxAdjRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdjRowStatus.setStatus("mandatory")
_VrIpxAdjComponentName_Type = DisplayString
_VrIpxAdjComponentName_Object = MibTableColumn
vrIpxAdjComponentName = _VrIpxAdjComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1, 2),
    _VrIpxAdjComponentName_Type()
)
vrIpxAdjComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdjComponentName.setStatus("mandatory")
_VrIpxAdjStorageType_Type = StorageType
_VrIpxAdjStorageType_Object = MibTableColumn
vrIpxAdjStorageType = _VrIpxAdjStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1, 4),
    _VrIpxAdjStorageType_Type()
)
vrIpxAdjStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdjStorageType.setStatus("mandatory")


class _VrIpxAdjProtocolPortIdentifierIndex_Type(AsciiStringIndex):
    """Custom type vrIpxAdjProtocolPortIdentifierIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_VrIpxAdjProtocolPortIdentifierIndex_Type.__name__ = "AsciiStringIndex"
_VrIpxAdjProtocolPortIdentifierIndex_Object = MibTableColumn
vrIpxAdjProtocolPortIdentifierIndex = _VrIpxAdjProtocolPortIdentifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1, 10),
    _VrIpxAdjProtocolPortIdentifierIndex_Type()
)
vrIpxAdjProtocolPortIdentifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxAdjProtocolPortIdentifierIndex.setStatus("mandatory")


class _VrIpxAdjNetworkNumberIndex_Type(DashedHexString):
    """Custom type vrIpxAdjNetworkNumberIndex based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrIpxAdjNetworkNumberIndex_Type.__name__ = "DashedHexString"
_VrIpxAdjNetworkNumberIndex_Object = MibTableColumn
vrIpxAdjNetworkNumberIndex = _VrIpxAdjNetworkNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 1, 1, 11),
    _VrIpxAdjNetworkNumberIndex_Type()
)
vrIpxAdjNetworkNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxAdjNetworkNumberIndex.setStatus("mandatory")
_VrIpxAdjOperTable_Object = MibTable
vrIpxAdjOperTable = _VrIpxAdjOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 10)
)
if mibBuilder.loadTexts:
    vrIpxAdjOperTable.setStatus("mandatory")
_VrIpxAdjOperEntry_Object = MibTableRow
vrIpxAdjOperEntry = _VrIpxAdjOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 10, 1)
)
vrIpxAdjOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxAdjProtocolPortIdentifierIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxAdjNetworkNumberIndex"),
)
if mibBuilder.loadTexts:
    vrIpxAdjOperEntry.setStatus("mandatory")


class _VrIpxAdjPhysAddress_Type(PhysAddress):
    """Custom type vrIpxAdjPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VrIpxAdjPhysAddress_Type.__name__ = "PhysAddress"
_VrIpxAdjPhysAddress_Object = MibTableColumn
vrIpxAdjPhysAddress = _VrIpxAdjPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 10, 1, 1),
    _VrIpxAdjPhysAddress_Type()
)
vrIpxAdjPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdjPhysAddress.setStatus("mandatory")


class _VrIpxAdjAdjacencyState_Type(Integer32):
    """Custom type vrIpxAdjAdjacencyState based on Integer32"""
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


_VrIpxAdjAdjacencyState_Type.__name__ = "Integer32"
_VrIpxAdjAdjacencyState_Object = MibTableColumn
vrIpxAdjAdjacencyState = _VrIpxAdjAdjacencyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 6, 10, 1, 2),
    _VrIpxAdjAdjacencyState_Type()
)
vrIpxAdjAdjacencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdjAdjacencyState.setStatus("mandatory")
_VrIpxNs_ObjectIdentity = ObjectIdentity
vrIpxNs = _VrIpxNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7)
)
_VrIpxNsRowStatusTable_Object = MibTable
vrIpxNsRowStatusTable = _VrIpxNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1)
)
if mibBuilder.loadTexts:
    vrIpxNsRowStatusTable.setStatus("mandatory")
_VrIpxNsRowStatusEntry_Object = MibTableRow
vrIpxNsRowStatusEntry = _VrIpxNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1, 1)
)
vrIpxNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsIndex"),
)
if mibBuilder.loadTexts:
    vrIpxNsRowStatusEntry.setStatus("mandatory")
_VrIpxNsRowStatus_Type = RowStatus
_VrIpxNsRowStatus_Object = MibTableColumn
vrIpxNsRowStatus = _VrIpxNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1, 1, 1),
    _VrIpxNsRowStatus_Type()
)
vrIpxNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsRowStatus.setStatus("mandatory")
_VrIpxNsComponentName_Type = DisplayString
_VrIpxNsComponentName_Object = MibTableColumn
vrIpxNsComponentName = _VrIpxNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1, 1, 2),
    _VrIpxNsComponentName_Type()
)
vrIpxNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxNsComponentName.setStatus("mandatory")
_VrIpxNsStorageType_Type = StorageType
_VrIpxNsStorageType_Object = MibTableColumn
vrIpxNsStorageType = _VrIpxNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1, 1, 4),
    _VrIpxNsStorageType_Type()
)
vrIpxNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxNsStorageType.setStatus("mandatory")
_VrIpxNsIndex_Type = NonReplicated
_VrIpxNsIndex_Object = MibTableColumn
vrIpxNsIndex = _VrIpxNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 1, 1, 10),
    _VrIpxNsIndex_Type()
)
vrIpxNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxNsIndex.setStatus("mandatory")
_VrIpxNsNetSentryApp_ObjectIdentity = ObjectIdentity
vrIpxNsNetSentryApp = _VrIpxNsNetSentryApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2)
)
_VrIpxNsNetSentryAppRowStatusTable_Object = MibTable
vrIpxNsNetSentryAppRowStatusTable = _VrIpxNsNetSentryAppRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppRowStatusTable.setStatus("mandatory")
_VrIpxNsNetSentryAppRowStatusEntry_Object = MibTableRow
vrIpxNsNetSentryAppRowStatusEntry = _VrIpxNsNetSentryAppRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1, 1)
)
vrIpxNsNetSentryAppRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsNetSentryAppEntryIndex"),
)
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppRowStatusEntry.setStatus("mandatory")
_VrIpxNsNetSentryAppRowStatus_Type = RowStatus
_VrIpxNsNetSentryAppRowStatus_Object = MibTableColumn
vrIpxNsNetSentryAppRowStatus = _VrIpxNsNetSentryAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1, 1, 1),
    _VrIpxNsNetSentryAppRowStatus_Type()
)
vrIpxNsNetSentryAppRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppRowStatus.setStatus("mandatory")
_VrIpxNsNetSentryAppComponentName_Type = DisplayString
_VrIpxNsNetSentryAppComponentName_Object = MibTableColumn
vrIpxNsNetSentryAppComponentName = _VrIpxNsNetSentryAppComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1, 1, 2),
    _VrIpxNsNetSentryAppComponentName_Type()
)
vrIpxNsNetSentryAppComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppComponentName.setStatus("mandatory")
_VrIpxNsNetSentryAppStorageType_Type = StorageType
_VrIpxNsNetSentryAppStorageType_Object = MibTableColumn
vrIpxNsNetSentryAppStorageType = _VrIpxNsNetSentryAppStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1, 1, 4),
    _VrIpxNsNetSentryAppStorageType_Type()
)
vrIpxNsNetSentryAppStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppStorageType.setStatus("mandatory")


class _VrIpxNsNetSentryAppEntryIndex_Type(Integer32):
    """Custom type vrIpxNsNetSentryAppEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 268435455),
    )


_VrIpxNsNetSentryAppEntryIndex_Type.__name__ = "Integer32"
_VrIpxNsNetSentryAppEntryIndex_Object = MibTableColumn
vrIpxNsNetSentryAppEntryIndex = _VrIpxNsNetSentryAppEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 1, 1, 10),
    _VrIpxNsNetSentryAppEntryIndex_Type()
)
vrIpxNsNetSentryAppEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppEntryIndex.setStatus("mandatory")
_VrIpxNsNetSentryAppProvTable_Object = MibTable
vrIpxNsNetSentryAppProvTable = _VrIpxNsNetSentryAppProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppProvTable.setStatus("mandatory")
_VrIpxNsNetSentryAppProvEntry_Object = MibTableRow
vrIpxNsNetSentryAppProvEntry = _VrIpxNsNetSentryAppProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1)
)
vrIpxNsNetSentryAppProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsNetSentryAppEntryIndex"),
)
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppProvEntry.setStatus("mandatory")


class _VrIpxNsNetSentryAppFilter_Type(AsciiString):
    """Custom type vrIpxNsNetSentryAppFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpxNsNetSentryAppFilter_Type.__name__ = "AsciiString"
_VrIpxNsNetSentryAppFilter_Object = MibTableColumn
vrIpxNsNetSentryAppFilter = _VrIpxNsNetSentryAppFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 1),
    _VrIpxNsNetSentryAppFilter_Type()
)
vrIpxNsNetSentryAppFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppFilter.setStatus("mandatory")


class _VrIpxNsNetSentryAppNetworkNumber1_Type(AsciiString):
    """Custom type vrIpxNsNetSentryAppNetworkNumber1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_VrIpxNsNetSentryAppNetworkNumber1_Type.__name__ = "AsciiString"
_VrIpxNsNetSentryAppNetworkNumber1_Object = MibTableColumn
vrIpxNsNetSentryAppNetworkNumber1 = _VrIpxNsNetSentryAppNetworkNumber1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 2),
    _VrIpxNsNetSentryAppNetworkNumber1_Type()
)
vrIpxNsNetSentryAppNetworkNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppNetworkNumber1.setStatus("mandatory")


class _VrIpxNsNetSentryAppNode1_Type(AsciiString):
    """Custom type vrIpxNsNetSentryAppNode1 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_VrIpxNsNetSentryAppNode1_Type.__name__ = "AsciiString"
_VrIpxNsNetSentryAppNode1_Object = MibTableColumn
vrIpxNsNetSentryAppNode1 = _VrIpxNsNetSentryAppNode1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 3),
    _VrIpxNsNetSentryAppNode1_Type()
)
vrIpxNsNetSentryAppNode1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppNode1.setStatus("mandatory")


class _VrIpxNsNetSentryAppDirection_Type(Integer32):
    """Custom type vrIpxNsNetSentryAppDirection based on Integer32"""
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


_VrIpxNsNetSentryAppDirection_Type.__name__ = "Integer32"
_VrIpxNsNetSentryAppDirection_Object = MibTableColumn
vrIpxNsNetSentryAppDirection = _VrIpxNsNetSentryAppDirection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 4),
    _VrIpxNsNetSentryAppDirection_Type()
)
vrIpxNsNetSentryAppDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppDirection.setStatus("mandatory")


class _VrIpxNsNetSentryAppNetworkNumber2_Type(AsciiString):
    """Custom type vrIpxNsNetSentryAppNetworkNumber2 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_VrIpxNsNetSentryAppNetworkNumber2_Type.__name__ = "AsciiString"
_VrIpxNsNetSentryAppNetworkNumber2_Object = MibTableColumn
vrIpxNsNetSentryAppNetworkNumber2 = _VrIpxNsNetSentryAppNetworkNumber2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 5),
    _VrIpxNsNetSentryAppNetworkNumber2_Type()
)
vrIpxNsNetSentryAppNetworkNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppNetworkNumber2.setStatus("mandatory")


class _VrIpxNsNetSentryAppNode2_Type(AsciiString):
    """Custom type vrIpxNsNetSentryAppNode2 based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_VrIpxNsNetSentryAppNode2_Type.__name__ = "AsciiString"
_VrIpxNsNetSentryAppNode2_Object = MibTableColumn
vrIpxNsNetSentryAppNode2 = _VrIpxNsNetSentryAppNode2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 2, 10, 1, 6),
    _VrIpxNsNetSentryAppNode2_Type()
)
vrIpxNsNetSentryAppNode2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsNetSentryAppNode2.setStatus("mandatory")
_VrIpxNsProvTable_Object = MibTable
vrIpxNsProvTable = _VrIpxNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10)
)
if mibBuilder.loadTexts:
    vrIpxNsProvTable.setStatus("mandatory")
_VrIpxNsProvEntry_Object = MibTableRow
vrIpxNsProvEntry = _VrIpxNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10, 1)
)
vrIpxNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxNsIndex"),
)
if mibBuilder.loadTexts:
    vrIpxNsProvEntry.setStatus("mandatory")


class _VrIpxNsFirstFilter_Type(AsciiString):
    """Custom type vrIpxNsFirstFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpxNsFirstFilter_Type.__name__ = "AsciiString"
_VrIpxNsFirstFilter_Object = MibTableColumn
vrIpxNsFirstFilter = _VrIpxNsFirstFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10, 1, 1),
    _VrIpxNsFirstFilter_Type()
)
vrIpxNsFirstFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsFirstFilter.setStatus("mandatory")


class _VrIpxNsLastFilter_Type(AsciiString):
    """Custom type vrIpxNsLastFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpxNsLastFilter_Type.__name__ = "AsciiString"
_VrIpxNsLastFilter_Object = MibTableColumn
vrIpxNsLastFilter = _VrIpxNsLastFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10, 1, 2),
    _VrIpxNsLastFilter_Type()
)
vrIpxNsLastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsLastFilter.setStatus("mandatory")


class _VrIpxNsLocalInFilter_Type(AsciiString):
    """Custom type vrIpxNsLocalInFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpxNsLocalInFilter_Type.__name__ = "AsciiString"
_VrIpxNsLocalInFilter_Object = MibTableColumn
vrIpxNsLocalInFilter = _VrIpxNsLocalInFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10, 1, 3),
    _VrIpxNsLocalInFilter_Type()
)
vrIpxNsLocalInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsLocalInFilter.setStatus("mandatory")


class _VrIpxNsLocalOutFilter_Type(AsciiString):
    """Custom type vrIpxNsLocalOutFilter based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VrIpxNsLocalOutFilter_Type.__name__ = "AsciiString"
_VrIpxNsLocalOutFilter_Object = MibTableColumn
vrIpxNsLocalOutFilter = _VrIpxNsLocalOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 7, 10, 1, 4),
    _VrIpxNsLocalOutFilter_Type()
)
vrIpxNsLocalOutFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNsLocalOutFilter.setStatus("mandatory")
_VrIpxAdminControlTable_Object = MibTable
vrIpxAdminControlTable = _VrIpxAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 100)
)
if mibBuilder.loadTexts:
    vrIpxAdminControlTable.setStatus("mandatory")
_VrIpxAdminControlEntry_Object = MibTableRow
vrIpxAdminControlEntry = _VrIpxAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 100, 1)
)
vrIpxAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxAdminControlEntry.setStatus("mandatory")


class _VrIpxSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpxSnmpAdminStatus based on Integer32"""
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


_VrIpxSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpxSnmpAdminStatus_Object = MibTableColumn
vrIpxSnmpAdminStatus = _VrIpxSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 100, 1, 1),
    _VrIpxSnmpAdminStatus_Type()
)
vrIpxSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSnmpAdminStatus.setStatus("mandatory")
_VrIpxProvTable_Object = MibTable
vrIpxProvTable = _VrIpxProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101)
)
if mibBuilder.loadTexts:
    vrIpxProvTable.setStatus("mandatory")
_VrIpxProvEntry_Object = MibTableRow
vrIpxProvEntry = _VrIpxProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1)
)
vrIpxProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxProvEntry.setStatus("mandatory")


class _VrIpxNetworkNumber_Type(DashedHexString):
    """Custom type vrIpxNetworkNumber based on DashedHexString"""
    subtypeSpec = DashedHexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_VrIpxNetworkNumber_Type.__name__ = "DashedHexString"
_VrIpxNetworkNumber_Object = MibTableColumn
vrIpxNetworkNumber = _VrIpxNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 1),
    _VrIpxNetworkNumber_Type()
)
vrIpxNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxNetworkNumber.setStatus("mandatory")


class _VrIpxMaxPathSplits_Type(Unsigned32):
    """Custom type vrIpxMaxPathSplits based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_VrIpxMaxPathSplits_Type.__name__ = "Unsigned32"
_VrIpxMaxPathSplits_Object = MibTableColumn
vrIpxMaxPathSplits = _VrIpxMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 2),
    _VrIpxMaxPathSplits_Type()
)
vrIpxMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxMaxPathSplits.setStatus("mandatory")


class _VrIpxMaxHops_Type(Unsigned32):
    """Custom type vrIpxMaxHops based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_VrIpxMaxHops_Type.__name__ = "Unsigned32"
_VrIpxMaxHops_Object = MibTableColumn
vrIpxMaxHops = _VrIpxMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 3),
    _VrIpxMaxHops_Type()
)
vrIpxMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxMaxHops.setStatus("mandatory")


class _VrIpxRipUpdateInterval_Type(Unsigned32):
    """Custom type vrIpxRipUpdateInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrIpxRipUpdateInterval_Type.__name__ = "Unsigned32"
_VrIpxRipUpdateInterval_Object = MibTableColumn
vrIpxRipUpdateInterval = _VrIpxRipUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 4),
    _VrIpxRipUpdateInterval_Type()
)
vrIpxRipUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipUpdateInterval.setStatus("mandatory")


class _VrIpxSapUpdateInterval_Type(Unsigned32):
    """Custom type vrIpxSapUpdateInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrIpxSapUpdateInterval_Type.__name__ = "Unsigned32"
_VrIpxSapUpdateInterval_Object = MibTableColumn
vrIpxSapUpdateInterval = _VrIpxSapUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 5),
    _VrIpxSapUpdateInterval_Type()
)
vrIpxSapUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapUpdateInterval.setStatus("mandatory")


class _VrIpxControlDelay_Type(Unsigned32):
    """Custom type vrIpxControlDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VrIpxControlDelay_Type.__name__ = "Unsigned32"
_VrIpxControlDelay_Object = MibTableColumn
vrIpxControlDelay = _VrIpxControlDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 6),
    _VrIpxControlDelay_Type()
)
vrIpxControlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxControlDelay.setStatus("mandatory")


class _VrIpxUpdateDelay_Type(Unsigned32):
    """Custom type vrIpxUpdateDelay based on Unsigned32"""
    defaultValue = 55

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55, 500),
    )


_VrIpxUpdateDelay_Type.__name__ = "Unsigned32"
_VrIpxUpdateDelay_Object = MibTableColumn
vrIpxUpdateDelay = _VrIpxUpdateDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 7),
    _VrIpxUpdateDelay_Type()
)
vrIpxUpdateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxUpdateDelay.setStatus("mandatory")


class _VrIpxRipAgeMultiplier_Type(Unsigned32):
    """Custom type vrIpxRipAgeMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VrIpxRipAgeMultiplier_Type.__name__ = "Unsigned32"
_VrIpxRipAgeMultiplier_Object = MibTableColumn
vrIpxRipAgeMultiplier = _VrIpxRipAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 8),
    _VrIpxRipAgeMultiplier_Type()
)
vrIpxRipAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipAgeMultiplier.setStatus("mandatory")


class _VrIpxSapAgeMultiplier_Type(Unsigned32):
    """Custom type vrIpxSapAgeMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VrIpxSapAgeMultiplier_Type.__name__ = "Unsigned32"
_VrIpxSapAgeMultiplier_Object = MibTableColumn
vrIpxSapAgeMultiplier = _VrIpxSapAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 9),
    _VrIpxSapAgeMultiplier_Type()
)
vrIpxSapAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapAgeMultiplier.setStatus("mandatory")


class _VrIpxDamping_Type(Integer32):
    """Custom type vrIpxDamping based on Integer32"""
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


_VrIpxDamping_Type.__name__ = "Integer32"
_VrIpxDamping_Object = MibTableColumn
vrIpxDamping = _VrIpxDamping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 10),
    _VrIpxDamping_Type()
)
vrIpxDamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxDamping.setStatus("mandatory")


class _VrIpxRipMaxDampedGeneralRequests_Type(Unsigned32):
    """Custom type vrIpxRipMaxDampedGeneralRequests based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrIpxRipMaxDampedGeneralRequests_Type.__name__ = "Unsigned32"
_VrIpxRipMaxDampedGeneralRequests_Object = MibTableColumn
vrIpxRipMaxDampedGeneralRequests = _VrIpxRipMaxDampedGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 11),
    _VrIpxRipMaxDampedGeneralRequests_Type()
)
vrIpxRipMaxDampedGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipMaxDampedGeneralRequests.setStatus("mandatory")


class _VrIpxRipMaxDampedSpecificRequests_Type(Unsigned32):
    """Custom type vrIpxRipMaxDampedSpecificRequests based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrIpxRipMaxDampedSpecificRequests_Type.__name__ = "Unsigned32"
_VrIpxRipMaxDampedSpecificRequests_Object = MibTableColumn
vrIpxRipMaxDampedSpecificRequests = _VrIpxRipMaxDampedSpecificRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 12),
    _VrIpxRipMaxDampedSpecificRequests_Type()
)
vrIpxRipMaxDampedSpecificRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxRipMaxDampedSpecificRequests.setStatus("mandatory")


class _VrIpxSapMaxDampedGeneralRequests_Type(Unsigned32):
    """Custom type vrIpxSapMaxDampedGeneralRequests based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrIpxSapMaxDampedGeneralRequests_Type.__name__ = "Unsigned32"
_VrIpxSapMaxDampedGeneralRequests_Object = MibTableColumn
vrIpxSapMaxDampedGeneralRequests = _VrIpxSapMaxDampedGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 13),
    _VrIpxSapMaxDampedGeneralRequests_Type()
)
vrIpxSapMaxDampedGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapMaxDampedGeneralRequests.setStatus("mandatory")


class _VrIpxSapMaxDampedSpecificRequests_Type(Unsigned32):
    """Custom type vrIpxSapMaxDampedSpecificRequests based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VrIpxSapMaxDampedSpecificRequests_Type.__name__ = "Unsigned32"
_VrIpxSapMaxDampedSpecificRequests_Object = MibTableColumn
vrIpxSapMaxDampedSpecificRequests = _VrIpxSapMaxDampedSpecificRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 14),
    _VrIpxSapMaxDampedSpecificRequests_Type()
)
vrIpxSapMaxDampedSpecificRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxSapMaxDampedSpecificRequests.setStatus("mandatory")


class _VrIpxInitialGeneralRequests_Type(Integer32):
    """Custom type vrIpxInitialGeneralRequests based on Integer32"""
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


_VrIpxInitialGeneralRequests_Type.__name__ = "Integer32"
_VrIpxInitialGeneralRequests_Object = MibTableColumn
vrIpxInitialGeneralRequests = _VrIpxInitialGeneralRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 15),
    _VrIpxInitialGeneralRequests_Type()
)
vrIpxInitialGeneralRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxInitialGeneralRequests.setStatus("mandatory")


class _VrIpxHoldDownInterval_Type(Unsigned32):
    """Custom type vrIpxHoldDownInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpxHoldDownInterval_Type.__name__ = "Unsigned32"
_VrIpxHoldDownInterval_Object = MibTableColumn
vrIpxHoldDownInterval = _VrIpxHoldDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 101, 1, 16),
    _VrIpxHoldDownInterval_Type()
)
vrIpxHoldDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpxHoldDownInterval.setStatus("mandatory")
_VrIpxStateTable_Object = MibTable
vrIpxStateTable = _VrIpxStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 103)
)
if mibBuilder.loadTexts:
    vrIpxStateTable.setStatus("mandatory")
_VrIpxStateEntry_Object = MibTableRow
vrIpxStateEntry = _VrIpxStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 103, 1)
)
vrIpxStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxStateEntry.setStatus("mandatory")


class _VrIpxAdminState_Type(Integer32):
    """Custom type vrIpxAdminState based on Integer32"""
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


_VrIpxAdminState_Type.__name__ = "Integer32"
_VrIpxAdminState_Object = MibTableColumn
vrIpxAdminState = _VrIpxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 103, 1, 1),
    _VrIpxAdminState_Type()
)
vrIpxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxAdminState.setStatus("mandatory")


class _VrIpxOperationalState_Type(Integer32):
    """Custom type vrIpxOperationalState based on Integer32"""
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


_VrIpxOperationalState_Type.__name__ = "Integer32"
_VrIpxOperationalState_Object = MibTableColumn
vrIpxOperationalState = _VrIpxOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 103, 1, 2),
    _VrIpxOperationalState_Type()
)
vrIpxOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOperationalState.setStatus("mandatory")


class _VrIpxUsageState_Type(Integer32):
    """Custom type vrIpxUsageState based on Integer32"""
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


_VrIpxUsageState_Type.__name__ = "Integer32"
_VrIpxUsageState_Object = MibTableColumn
vrIpxUsageState = _VrIpxUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 103, 1, 3),
    _VrIpxUsageState_Type()
)
vrIpxUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxUsageState.setStatus("mandatory")
_VrIpxOperStatusTable_Object = MibTable
vrIpxOperStatusTable = _VrIpxOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 104)
)
if mibBuilder.loadTexts:
    vrIpxOperStatusTable.setStatus("mandatory")
_VrIpxOperStatusEntry_Object = MibTableRow
vrIpxOperStatusEntry = _VrIpxOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 104, 1)
)
vrIpxOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxOperStatusEntry.setStatus("mandatory")


class _VrIpxSnmpOperStatus_Type(Integer32):
    """Custom type vrIpxSnmpOperStatus based on Integer32"""
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


_VrIpxSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpxSnmpOperStatus_Object = MibTableColumn
vrIpxSnmpOperStatus = _VrIpxSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 104, 1, 1),
    _VrIpxSnmpOperStatus_Type()
)
vrIpxSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxSnmpOperStatus.setStatus("mandatory")
_VrIpxOperTable_Object = MibTable
vrIpxOperTable = _VrIpxOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 105)
)
if mibBuilder.loadTexts:
    vrIpxOperTable.setStatus("mandatory")
_VrIpxOperEntry_Object = MibTableRow
vrIpxOperEntry = _VrIpxOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 105, 1)
)
vrIpxOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxOperEntry.setStatus("mandatory")


class _VrIpxProtocolPortCount_Type(Unsigned32):
    """Custom type vrIpxProtocolPortCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpxProtocolPortCount_Type.__name__ = "Unsigned32"
_VrIpxProtocolPortCount_Object = MibTableColumn
vrIpxProtocolPortCount = _VrIpxProtocolPortCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 105, 1, 1),
    _VrIpxProtocolPortCount_Type()
)
vrIpxProtocolPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxProtocolPortCount.setStatus("mandatory")


class _VrIpxDestinationCount_Type(Unsigned32):
    """Custom type vrIpxDestinationCount based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpxDestinationCount_Type.__name__ = "Unsigned32"
_VrIpxDestinationCount_Object = MibTableColumn
vrIpxDestinationCount = _VrIpxDestinationCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 105, 1, 2),
    _VrIpxDestinationCount_Type()
)
vrIpxDestinationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxDestinationCount.setStatus("mandatory")


class _VrIpxServicesCount_Type(Unsigned32):
    """Custom type vrIpxServicesCount based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpxServicesCount_Type.__name__ = "Unsigned32"
_VrIpxServicesCount_Object = MibTableColumn
vrIpxServicesCount = _VrIpxServicesCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 105, 1, 3),
    _VrIpxServicesCount_Type()
)
vrIpxServicesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxServicesCount.setStatus("mandatory")
_VrIpxStatsTable_Object = MibTable
vrIpxStatsTable = _VrIpxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107)
)
if mibBuilder.loadTexts:
    vrIpxStatsTable.setStatus("mandatory")
_VrIpxStatsEntry_Object = MibTableRow
vrIpxStatsEntry = _VrIpxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1)
)
vrIpxStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpxMIB", "vrIpxIndex"),
)
if mibBuilder.loadTexts:
    vrIpxStatsEntry.setStatus("mandatory")
_VrIpxInReceives_Type = Counter32
_VrIpxInReceives_Object = MibTableColumn
vrIpxInReceives = _VrIpxInReceives_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 1),
    _VrIpxInReceives_Type()
)
vrIpxInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInReceives.setStatus("mandatory")
_VrIpxInHeaderErrors_Type = Counter32
_VrIpxInHeaderErrors_Object = MibTableColumn
vrIpxInHeaderErrors = _VrIpxInHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 2),
    _VrIpxInHeaderErrors_Type()
)
vrIpxInHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInHeaderErrors.setStatus("mandatory")
_VrIpxInUnknownSocket_Type = Counter32
_VrIpxInUnknownSocket_Object = MibTableColumn
vrIpxInUnknownSocket = _VrIpxInUnknownSocket_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 3),
    _VrIpxInUnknownSocket_Type()
)
vrIpxInUnknownSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInUnknownSocket.setStatus("mandatory")
_VrIpxInDiscards_Type = Counter32
_VrIpxInDiscards_Object = MibTableColumn
vrIpxInDiscards = _VrIpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 4),
    _VrIpxInDiscards_Type()
)
vrIpxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInDiscards.setStatus("mandatory")
_VrIpxInBadChecksums_Type = Counter32
_VrIpxInBadChecksums_Object = MibTableColumn
vrIpxInBadChecksums = _VrIpxInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 5),
    _VrIpxInBadChecksums_Type()
)
vrIpxInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInBadChecksums.setStatus("mandatory")
_VrIpxInDelivers_Type = Counter32
_VrIpxInDelivers_Object = MibTableColumn
vrIpxInDelivers = _VrIpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 6),
    _VrIpxInDelivers_Type()
)
vrIpxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInDelivers.setStatus("mandatory")
_VrIpxNoRoutes_Type = Counter32
_VrIpxNoRoutes_Object = MibTableColumn
vrIpxNoRoutes = _VrIpxNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 7),
    _VrIpxNoRoutes_Type()
)
vrIpxNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxNoRoutes.setStatus("mandatory")
_VrIpxOutRequests_Type = Counter32
_VrIpxOutRequests_Object = MibTableColumn
vrIpxOutRequests = _VrIpxOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 8),
    _VrIpxOutRequests_Type()
)
vrIpxOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOutRequests.setStatus("mandatory")
_VrIpxOutMalformedRequests_Type = Counter32
_VrIpxOutMalformedRequests_Object = MibTableColumn
vrIpxOutMalformedRequests = _VrIpxOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 9),
    _VrIpxOutMalformedRequests_Type()
)
vrIpxOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOutMalformedRequests.setStatus("mandatory")
_VrIpxOutDiscards_Type = Counter32
_VrIpxOutDiscards_Object = MibTableColumn
vrIpxOutDiscards = _VrIpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 10),
    _VrIpxOutDiscards_Type()
)
vrIpxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOutDiscards.setStatus("mandatory")
_VrIpxOutPackets_Type = Counter32
_VrIpxOutPackets_Object = MibTableColumn
vrIpxOutPackets = _VrIpxOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 11),
    _VrIpxOutPackets_Type()
)
vrIpxOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOutPackets.setStatus("mandatory")
_VrIpxInTooManyHops_Type = Counter32
_VrIpxInTooManyHops_Object = MibTableColumn
vrIpxInTooManyHops = _VrIpxInTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 12),
    _VrIpxInTooManyHops_Type()
)
vrIpxInTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInTooManyHops.setStatus("mandatory")
_VrIpxInFiltered_Type = Counter32
_VrIpxInFiltered_Object = MibTableColumn
vrIpxInFiltered = _VrIpxInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 13),
    _VrIpxInFiltered_Type()
)
vrIpxInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInFiltered.setStatus("mandatory")
_VrIpxInNetBIOS_Type = Counter32
_VrIpxInNetBIOS_Object = MibTableColumn
vrIpxInNetBIOS = _VrIpxInNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 14),
    _VrIpxInNetBIOS_Type()
)
vrIpxInNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxInNetBIOS.setStatus("mandatory")
_VrIpxForwarded_Type = Counter32
_VrIpxForwarded_Object = MibTableColumn
vrIpxForwarded = _VrIpxForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 15),
    _VrIpxForwarded_Type()
)
vrIpxForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxForwarded.setStatus("mandatory")
_VrIpxOutFiltered_Type = Counter32
_VrIpxOutFiltered_Object = MibTableColumn
vrIpxOutFiltered = _VrIpxOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 7, 107, 1, 16),
    _VrIpxOutFiltered_Type()
)
vrIpxOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpxOutFiltered.setStatus("mandatory")
_IpxMIB_ObjectIdentity = ObjectIdentity
ipxMIB = _IpxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28)
)
_IpxGroup_ObjectIdentity = ObjectIdentity
ipxGroup = _IpxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 1)
)
_IpxGroupBE_ObjectIdentity = ObjectIdentity
ipxGroupBE = _IpxGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 1, 5)
)
_IpxGroupBE01_ObjectIdentity = ObjectIdentity
ipxGroupBE01 = _IpxGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 1, 5, 2)
)
_IpxGroupBE01A_ObjectIdentity = ObjectIdentity
ipxGroupBE01A = _IpxGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 1, 5, 2, 2)
)
_IpxCapabilities_ObjectIdentity = ObjectIdentity
ipxCapabilities = _IpxCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 3)
)
_IpxCapabilitiesBE_ObjectIdentity = ObjectIdentity
ipxCapabilitiesBE = _IpxCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 3, 5)
)
_IpxCapabilitiesBE01_ObjectIdentity = ObjectIdentity
ipxCapabilitiesBE01 = _IpxCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 3, 5, 2)
)
_IpxCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
ipxCapabilitiesBE01A = _IpxCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 28, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpxMIB",
    **{"vrPpIpxP": vrPpIpxP,
       "vrPpIpxPRowStatusTable": vrPpIpxPRowStatusTable,
       "vrPpIpxPRowStatusEntry": vrPpIpxPRowStatusEntry,
       "vrPpIpxPRowStatus": vrPpIpxPRowStatus,
       "vrPpIpxPComponentName": vrPpIpxPComponentName,
       "vrPpIpxPStorageType": vrPpIpxPStorageType,
       "vrPpIpxPIndex": vrPpIpxPIndex,
       "vrPpIpxPRipP": vrPpIpxPRipP,
       "vrPpIpxPRipPRowStatusTable": vrPpIpxPRipPRowStatusTable,
       "vrPpIpxPRipPRowStatusEntry": vrPpIpxPRipPRowStatusEntry,
       "vrPpIpxPRipPRowStatus": vrPpIpxPRipPRowStatus,
       "vrPpIpxPRipPComponentName": vrPpIpxPRipPComponentName,
       "vrPpIpxPRipPStorageType": vrPpIpxPRipPStorageType,
       "vrPpIpxPRipPIndex": vrPpIpxPRipPIndex,
       "vrPpIpxPRipPStatsTable": vrPpIpxPRipPStatsTable,
       "vrPpIpxPRipPStatsEntry": vrPpIpxPRipPStatsEntry,
       "vrPpIpxPRipPInPackets": vrPpIpxPRipPInPackets,
       "vrPpIpxPRipPInRequests": vrPpIpxPRipPInRequests,
       "vrPpIpxPRipPInResponses": vrPpIpxPRipPInResponses,
       "vrPpIpxPRipPOutPackets": vrPpIpxPRipPOutPackets,
       "vrPpIpxPRipPOutRequests": vrPpIpxPRipPOutRequests,
       "vrPpIpxPRipPOutResponses": vrPpIpxPRipPOutResponses,
       "vrPpIpxPRipPIncorrectPackets": vrPpIpxPRipPIncorrectPackets,
       "vrPpIpxPSapP": vrPpIpxPSapP,
       "vrPpIpxPSapPRowStatusTable": vrPpIpxPSapPRowStatusTable,
       "vrPpIpxPSapPRowStatusEntry": vrPpIpxPSapPRowStatusEntry,
       "vrPpIpxPSapPRowStatus": vrPpIpxPSapPRowStatus,
       "vrPpIpxPSapPComponentName": vrPpIpxPSapPComponentName,
       "vrPpIpxPSapPStorageType": vrPpIpxPSapPStorageType,
       "vrPpIpxPSapPIndex": vrPpIpxPSapPIndex,
       "vrPpIpxPSapPStatsTable": vrPpIpxPSapPStatsTable,
       "vrPpIpxPSapPStatsEntry": vrPpIpxPSapPStatsEntry,
       "vrPpIpxPSapPInPackets": vrPpIpxPSapPInPackets,
       "vrPpIpxPSapPInRequests": vrPpIpxPSapPInRequests,
       "vrPpIpxPSapPInResponses": vrPpIpxPSapPInResponses,
       "vrPpIpxPSapPOutPackets": vrPpIpxPSapPOutPackets,
       "vrPpIpxPSapPOutRequests": vrPpIpxPSapPOutRequests,
       "vrPpIpxPSapPOutResponses": vrPpIpxPSapPOutResponses,
       "vrPpIpxPSapPIncorrectPackets": vrPpIpxPSapPIncorrectPackets,
       "vrPpIpxPIWP": vrPpIpxPIWP,
       "vrPpIpxPIWPRowStatusTable": vrPpIpxPIWPRowStatusTable,
       "vrPpIpxPIWPRowStatusEntry": vrPpIpxPIWPRowStatusEntry,
       "vrPpIpxPIWPRowStatus": vrPpIpxPIWPRowStatus,
       "vrPpIpxPIWPComponentName": vrPpIpxPIWPComponentName,
       "vrPpIpxPIWPStorageType": vrPpIpxPIWPStorageType,
       "vrPpIpxPIWPRemoteStationIdentifierIndex": vrPpIpxPIWPRemoteStationIdentifierIndex,
       "vrPpIpxPIWPOperTable": vrPpIpxPIWPOperTable,
       "vrPpIpxPIWPOperEntry": vrPpIpxPIWPOperEntry,
       "vrPpIpxPIWPNeighbourRouterName": vrPpIpxPIWPNeighbourRouterName,
       "vrPpIpxPIWPNeighbourInternalNetworkNumber": vrPpIpxPIWPNeighbourInternalNetworkNumber,
       "vrPpIpxPIWPInitFails": vrPpIpxPIWPInitFails,
       "vrPpIpxPNetSentryP": vrPpIpxPNetSentryP,
       "vrPpIpxPNetSentryPRowStatusTable": vrPpIpxPNetSentryPRowStatusTable,
       "vrPpIpxPNetSentryPRowStatusEntry": vrPpIpxPNetSentryPRowStatusEntry,
       "vrPpIpxPNetSentryPRowStatus": vrPpIpxPNetSentryPRowStatus,
       "vrPpIpxPNetSentryPComponentName": vrPpIpxPNetSentryPComponentName,
       "vrPpIpxPNetSentryPStorageType": vrPpIpxPNetSentryPStorageType,
       "vrPpIpxPNetSentryPIndex": vrPpIpxPNetSentryPIndex,
       "vrPpIpxPNetSentryPProvTable": vrPpIpxPNetSentryPProvTable,
       "vrPpIpxPNetSentryPProvEntry": vrPpIpxPNetSentryPProvEntry,
       "vrPpIpxPNetSentryPInComingFilter": vrPpIpxPNetSentryPInComingFilter,
       "vrPpIpxPNetSentryPOutGoingFilter": vrPpIpxPNetSentryPOutGoingFilter,
       "vrPpIpxPAdminControlTable": vrPpIpxPAdminControlTable,
       "vrPpIpxPAdminControlEntry": vrPpIpxPAdminControlEntry,
       "vrPpIpxPSnmpAdminStatus": vrPpIpxPSnmpAdminStatus,
       "vrPpIpxPProvTable": vrPpIpxPProvTable,
       "vrPpIpxPProvEntry": vrPpIpxPProvEntry,
       "vrPpIpxPNetworkNumberProv": vrPpIpxPNetworkNumberProv,
       "vrPpIpxPDefaultType": vrPpIpxPDefaultType,
       "vrPpIpxPBroadcastInhibit": vrPpIpxPBroadcastInhibit,
       "vrPpIpxPSresProvTable": vrPpIpxPSresProvTable,
       "vrPpIpxPSresProvEntry": vrPpIpxPSresProvEntry,
       "vrPpIpxPSourceRouteEndStationSupport": vrPpIpxPSourceRouteEndStationSupport,
       "vrPpIpxPStateTable": vrPpIpxPStateTable,
       "vrPpIpxPStateEntry": vrPpIpxPStateEntry,
       "vrPpIpxPAdminState": vrPpIpxPAdminState,
       "vrPpIpxPOperationalState": vrPpIpxPOperationalState,
       "vrPpIpxPUsageState": vrPpIpxPUsageState,
       "vrPpIpxPOperStatusTable": vrPpIpxPOperStatusTable,
       "vrPpIpxPOperStatusEntry": vrPpIpxPOperStatusEntry,
       "vrPpIpxPSnmpOperStatus": vrPpIpxPSnmpOperStatus,
       "vrPpIpxPOperTable": vrPpIpxPOperTable,
       "vrPpIpxPOperEntry": vrPpIpxPOperEntry,
       "vrPpIpxPType": vrPpIpxPType,
       "vrPpIpxPEncapsulation": vrPpIpxPEncapsulation,
       "vrPpIpxPNetworkNumber": vrPpIpxPNetworkNumber,
       "vrPpIpxPNode": vrPpIpxPNode,
       "vrPpIpxPStatsTable": vrPpIpxPStatsTable,
       "vrPpIpxPStatsEntry": vrPpIpxPStatsEntry,
       "vrPpIpxPStateChanges": vrPpIpxPStateChanges,
       "vrPpIpxPInReceives": vrPpIpxPInReceives,
       "vrPpIpxPForwarded": vrPpIpxPForwarded,
       "vrIpx": vrIpx,
       "vrIpxRowStatusTable": vrIpxRowStatusTable,
       "vrIpxRowStatusEntry": vrIpxRowStatusEntry,
       "vrIpxRowStatus": vrIpxRowStatus,
       "vrIpxComponentName": vrIpxComponentName,
       "vrIpxStorageType": vrIpxStorageType,
       "vrIpxIndex": vrIpxIndex,
       "vrIpxRip": vrIpxRip,
       "vrIpxRipRowStatusTable": vrIpxRipRowStatusTable,
       "vrIpxRipRowStatusEntry": vrIpxRipRowStatusEntry,
       "vrIpxRipRowStatus": vrIpxRipRowStatus,
       "vrIpxRipComponentName": vrIpxRipComponentName,
       "vrIpxRipStorageType": vrIpxRipStorageType,
       "vrIpxRipIndex": vrIpxRipIndex,
       "vrIpxRipRFltr": vrIpxRipRFltr,
       "vrIpxRipRFltrRowStatusTable": vrIpxRipRFltrRowStatusTable,
       "vrIpxRipRFltrRowStatusEntry": vrIpxRipRFltrRowStatusEntry,
       "vrIpxRipRFltrRowStatus": vrIpxRipRFltrRowStatus,
       "vrIpxRipRFltrComponentName": vrIpxRipRFltrComponentName,
       "vrIpxRipRFltrStorageType": vrIpxRipRFltrStorageType,
       "vrIpxRipRFltrIdentifierIndex": vrIpxRipRFltrIdentifierIndex,
       "vrIpxRipRFltrProvTable": vrIpxRipRFltrProvTable,
       "vrIpxRipRFltrProvEntry": vrIpxRipRFltrProvEntry,
       "vrIpxRipRFltrHops": vrIpxRipRFltrHops,
       "vrIpxRipRFltrTicks": vrIpxRipRFltrTicks,
       "vrIpxRipRFltrNetworkNumber": vrIpxRipRFltrNetworkNumber,
       "vrIpxRipRFltrNode": vrIpxRipRFltrNode,
       "vrIpxRipRFltrPort": vrIpxRipRFltrPort,
       "vrIpxRipRFltrDisposition": vrIpxRipRFltrDisposition,
       "vrIpxRipRFltrOperTable": vrIpxRipRFltrOperTable,
       "vrIpxRipRFltrOperEntry": vrIpxRipRFltrOperEntry,
       "vrIpxRipRFltrNumberOfApplyEntries": vrIpxRipRFltrNumberOfApplyEntries,
       "vrIpxRipRipApp": vrIpxRipRipApp,
       "vrIpxRipRipAppRowStatusTable": vrIpxRipRipAppRowStatusTable,
       "vrIpxRipRipAppRowStatusEntry": vrIpxRipRipAppRowStatusEntry,
       "vrIpxRipRipAppRowStatus": vrIpxRipRipAppRowStatus,
       "vrIpxRipRipAppComponentName": vrIpxRipRipAppComponentName,
       "vrIpxRipRipAppStorageType": vrIpxRipRipAppStorageType,
       "vrIpxRipRipAppProtocolPortNameIndex": vrIpxRipRipAppProtocolPortNameIndex,
       "vrIpxRipRipAppFilterIdentifierIndex": vrIpxRipRipAppFilterIdentifierIndex,
       "vrIpxRipRipAppProvTable": vrIpxRipRipAppProvTable,
       "vrIpxRipRipAppProvEntry": vrIpxRipRipAppProvEntry,
       "vrIpxRipRipAppDirection": vrIpxRipRipAppDirection,
       "vrIpxRipStatsTable": vrIpxRipStatsTable,
       "vrIpxRipStatsEntry": vrIpxRipStatsEntry,
       "vrIpxRipRipIn": vrIpxRipRipIn,
       "vrIpxRipRipOut": vrIpxRipRipOut,
       "vrIpxRipRipIncorrectPackets": vrIpxRipRipIncorrectPackets,
       "vrIpxSap": vrIpxSap,
       "vrIpxSapRowStatusTable": vrIpxSapRowStatusTable,
       "vrIpxSapRowStatusEntry": vrIpxSapRowStatusEntry,
       "vrIpxSapRowStatus": vrIpxSapRowStatus,
       "vrIpxSapComponentName": vrIpxSapComponentName,
       "vrIpxSapStorageType": vrIpxSapStorageType,
       "vrIpxSapIndex": vrIpxSapIndex,
       "vrIpxSapSFltr": vrIpxSapSFltr,
       "vrIpxSapSFltrRowStatusTable": vrIpxSapSFltrRowStatusTable,
       "vrIpxSapSFltrRowStatusEntry": vrIpxSapSFltrRowStatusEntry,
       "vrIpxSapSFltrRowStatus": vrIpxSapSFltrRowStatus,
       "vrIpxSapSFltrComponentName": vrIpxSapSFltrComponentName,
       "vrIpxSapSFltrStorageType": vrIpxSapSFltrStorageType,
       "vrIpxSapSFltrIdentifierIndex": vrIpxSapSFltrIdentifierIndex,
       "vrIpxSapSFltrProvTable": vrIpxSapSFltrProvTable,
       "vrIpxSapSFltrProvEntry": vrIpxSapSFltrProvEntry,
       "vrIpxSapSFltrType": vrIpxSapSFltrType,
       "vrIpxSapSFltrName": vrIpxSapSFltrName,
       "vrIpxSapSFltrNetworkNumber": vrIpxSapSFltrNetworkNumber,
       "vrIpxSapSFltrNode": vrIpxSapSFltrNode,
       "vrIpxSapSFltrDisposition": vrIpxSapSFltrDisposition,
       "vrIpxSapSFltrOperTable": vrIpxSapSFltrOperTable,
       "vrIpxSapSFltrOperEntry": vrIpxSapSFltrOperEntry,
       "vrIpxSapSFltrNumberOfApplyEntries": vrIpxSapSFltrNumberOfApplyEntries,
       "vrIpxSapSapApp": vrIpxSapSapApp,
       "vrIpxSapSapAppRowStatusTable": vrIpxSapSapAppRowStatusTable,
       "vrIpxSapSapAppRowStatusEntry": vrIpxSapSapAppRowStatusEntry,
       "vrIpxSapSapAppRowStatus": vrIpxSapSapAppRowStatus,
       "vrIpxSapSapAppComponentName": vrIpxSapSapAppComponentName,
       "vrIpxSapSapAppStorageType": vrIpxSapSapAppStorageType,
       "vrIpxSapSapAppProtocolPortNameIndex": vrIpxSapSapAppProtocolPortNameIndex,
       "vrIpxSapSapAppFilterIdentifierIndex": vrIpxSapSapAppFilterIdentifierIndex,
       "vrIpxSapSapAppProvTable": vrIpxSapSapAppProvTable,
       "vrIpxSapSapAppProvEntry": vrIpxSapSapAppProvEntry,
       "vrIpxSapSapAppDirection": vrIpxSapSapAppDirection,
       "vrIpxSapStatsTable": vrIpxSapStatsTable,
       "vrIpxSapStatsEntry": vrIpxSapStatsEntry,
       "vrIpxSapSapIn": vrIpxSapSapIn,
       "vrIpxSapSapOut": vrIpxSapSapOut,
       "vrIpxSapSapIncorrectPackets": vrIpxSapSapIncorrectPackets,
       "vrIpxFwd": vrIpxFwd,
       "vrIpxFwdRowStatusTable": vrIpxFwdRowStatusTable,
       "vrIpxFwdRowStatusEntry": vrIpxFwdRowStatusEntry,
       "vrIpxFwdRowStatus": vrIpxFwdRowStatus,
       "vrIpxFwdComponentName": vrIpxFwdComponentName,
       "vrIpxFwdStorageType": vrIpxFwdStorageType,
       "vrIpxFwdNetworkNumberIndex": vrIpxFwdNetworkNumberIndex,
       "vrIpxFwdOperTable": vrIpxFwdOperTable,
       "vrIpxFwdOperEntry": vrIpxFwdOperEntry,
       "vrIpxFwdProtocol": vrIpxFwdProtocol,
       "vrIpxFwdTicks": vrIpxFwdTicks,
       "vrIpxFwdHopCount": vrIpxFwdHopCount,
       "vrIpxFwdProtocolPortId": vrIpxFwdProtocolPortId,
       "vrIpxFwdNextHopPhysAddress": vrIpxFwdNextHopPhysAddress,
       "vrIpxFwdNextHopNetworkNumber": vrIpxFwdNextHopNetworkNumber,
       "vrIpxSrvc": vrIpxSrvc,
       "vrIpxSrvcRowStatusTable": vrIpxSrvcRowStatusTable,
       "vrIpxSrvcRowStatusEntry": vrIpxSrvcRowStatusEntry,
       "vrIpxSrvcRowStatus": vrIpxSrvcRowStatus,
       "vrIpxSrvcComponentName": vrIpxSrvcComponentName,
       "vrIpxSrvcStorageType": vrIpxSrvcStorageType,
       "vrIpxSrvcNetworkNumberIndex": vrIpxSrvcNetworkNumberIndex,
       "vrIpxSrvcNodeIndex": vrIpxSrvcNodeIndex,
       "vrIpxSrvcTypeIndex": vrIpxSrvcTypeIndex,
       "vrIpxSrvcNameIndex": vrIpxSrvcNameIndex,
       "vrIpxSrvcOperTable": vrIpxSrvcOperTable,
       "vrIpxSrvcOperEntry": vrIpxSrvcOperEntry,
       "vrIpxSrvcSocket": vrIpxSrvcSocket,
       "vrIpxSrvcProtocol": vrIpxSrvcProtocol,
       "vrIpxSrvcHopCount": vrIpxSrvcHopCount,
       "vrIpxAdj": vrIpxAdj,
       "vrIpxAdjRowStatusTable": vrIpxAdjRowStatusTable,
       "vrIpxAdjRowStatusEntry": vrIpxAdjRowStatusEntry,
       "vrIpxAdjRowStatus": vrIpxAdjRowStatus,
       "vrIpxAdjComponentName": vrIpxAdjComponentName,
       "vrIpxAdjStorageType": vrIpxAdjStorageType,
       "vrIpxAdjProtocolPortIdentifierIndex": vrIpxAdjProtocolPortIdentifierIndex,
       "vrIpxAdjNetworkNumberIndex": vrIpxAdjNetworkNumberIndex,
       "vrIpxAdjOperTable": vrIpxAdjOperTable,
       "vrIpxAdjOperEntry": vrIpxAdjOperEntry,
       "vrIpxAdjPhysAddress": vrIpxAdjPhysAddress,
       "vrIpxAdjAdjacencyState": vrIpxAdjAdjacencyState,
       "vrIpxNs": vrIpxNs,
       "vrIpxNsRowStatusTable": vrIpxNsRowStatusTable,
       "vrIpxNsRowStatusEntry": vrIpxNsRowStatusEntry,
       "vrIpxNsRowStatus": vrIpxNsRowStatus,
       "vrIpxNsComponentName": vrIpxNsComponentName,
       "vrIpxNsStorageType": vrIpxNsStorageType,
       "vrIpxNsIndex": vrIpxNsIndex,
       "vrIpxNsNetSentryApp": vrIpxNsNetSentryApp,
       "vrIpxNsNetSentryAppRowStatusTable": vrIpxNsNetSentryAppRowStatusTable,
       "vrIpxNsNetSentryAppRowStatusEntry": vrIpxNsNetSentryAppRowStatusEntry,
       "vrIpxNsNetSentryAppRowStatus": vrIpxNsNetSentryAppRowStatus,
       "vrIpxNsNetSentryAppComponentName": vrIpxNsNetSentryAppComponentName,
       "vrIpxNsNetSentryAppStorageType": vrIpxNsNetSentryAppStorageType,
       "vrIpxNsNetSentryAppEntryIndex": vrIpxNsNetSentryAppEntryIndex,
       "vrIpxNsNetSentryAppProvTable": vrIpxNsNetSentryAppProvTable,
       "vrIpxNsNetSentryAppProvEntry": vrIpxNsNetSentryAppProvEntry,
       "vrIpxNsNetSentryAppFilter": vrIpxNsNetSentryAppFilter,
       "vrIpxNsNetSentryAppNetworkNumber1": vrIpxNsNetSentryAppNetworkNumber1,
       "vrIpxNsNetSentryAppNode1": vrIpxNsNetSentryAppNode1,
       "vrIpxNsNetSentryAppDirection": vrIpxNsNetSentryAppDirection,
       "vrIpxNsNetSentryAppNetworkNumber2": vrIpxNsNetSentryAppNetworkNumber2,
       "vrIpxNsNetSentryAppNode2": vrIpxNsNetSentryAppNode2,
       "vrIpxNsProvTable": vrIpxNsProvTable,
       "vrIpxNsProvEntry": vrIpxNsProvEntry,
       "vrIpxNsFirstFilter": vrIpxNsFirstFilter,
       "vrIpxNsLastFilter": vrIpxNsLastFilter,
       "vrIpxNsLocalInFilter": vrIpxNsLocalInFilter,
       "vrIpxNsLocalOutFilter": vrIpxNsLocalOutFilter,
       "vrIpxAdminControlTable": vrIpxAdminControlTable,
       "vrIpxAdminControlEntry": vrIpxAdminControlEntry,
       "vrIpxSnmpAdminStatus": vrIpxSnmpAdminStatus,
       "vrIpxProvTable": vrIpxProvTable,
       "vrIpxProvEntry": vrIpxProvEntry,
       "vrIpxNetworkNumber": vrIpxNetworkNumber,
       "vrIpxMaxPathSplits": vrIpxMaxPathSplits,
       "vrIpxMaxHops": vrIpxMaxHops,
       "vrIpxRipUpdateInterval": vrIpxRipUpdateInterval,
       "vrIpxSapUpdateInterval": vrIpxSapUpdateInterval,
       "vrIpxControlDelay": vrIpxControlDelay,
       "vrIpxUpdateDelay": vrIpxUpdateDelay,
       "vrIpxRipAgeMultiplier": vrIpxRipAgeMultiplier,
       "vrIpxSapAgeMultiplier": vrIpxSapAgeMultiplier,
       "vrIpxDamping": vrIpxDamping,
       "vrIpxRipMaxDampedGeneralRequests": vrIpxRipMaxDampedGeneralRequests,
       "vrIpxRipMaxDampedSpecificRequests": vrIpxRipMaxDampedSpecificRequests,
       "vrIpxSapMaxDampedGeneralRequests": vrIpxSapMaxDampedGeneralRequests,
       "vrIpxSapMaxDampedSpecificRequests": vrIpxSapMaxDampedSpecificRequests,
       "vrIpxInitialGeneralRequests": vrIpxInitialGeneralRequests,
       "vrIpxHoldDownInterval": vrIpxHoldDownInterval,
       "vrIpxStateTable": vrIpxStateTable,
       "vrIpxStateEntry": vrIpxStateEntry,
       "vrIpxAdminState": vrIpxAdminState,
       "vrIpxOperationalState": vrIpxOperationalState,
       "vrIpxUsageState": vrIpxUsageState,
       "vrIpxOperStatusTable": vrIpxOperStatusTable,
       "vrIpxOperStatusEntry": vrIpxOperStatusEntry,
       "vrIpxSnmpOperStatus": vrIpxSnmpOperStatus,
       "vrIpxOperTable": vrIpxOperTable,
       "vrIpxOperEntry": vrIpxOperEntry,
       "vrIpxProtocolPortCount": vrIpxProtocolPortCount,
       "vrIpxDestinationCount": vrIpxDestinationCount,
       "vrIpxServicesCount": vrIpxServicesCount,
       "vrIpxStatsTable": vrIpxStatsTable,
       "vrIpxStatsEntry": vrIpxStatsEntry,
       "vrIpxInReceives": vrIpxInReceives,
       "vrIpxInHeaderErrors": vrIpxInHeaderErrors,
       "vrIpxInUnknownSocket": vrIpxInUnknownSocket,
       "vrIpxInDiscards": vrIpxInDiscards,
       "vrIpxInBadChecksums": vrIpxInBadChecksums,
       "vrIpxInDelivers": vrIpxInDelivers,
       "vrIpxNoRoutes": vrIpxNoRoutes,
       "vrIpxOutRequests": vrIpxOutRequests,
       "vrIpxOutMalformedRequests": vrIpxOutMalformedRequests,
       "vrIpxOutDiscards": vrIpxOutDiscards,
       "vrIpxOutPackets": vrIpxOutPackets,
       "vrIpxInTooManyHops": vrIpxInTooManyHops,
       "vrIpxInFiltered": vrIpxInFiltered,
       "vrIpxInNetBIOS": vrIpxInNetBIOS,
       "vrIpxForwarded": vrIpxForwarded,
       "vrIpxOutFiltered": vrIpxOutFiltered,
       "ipxMIB": ipxMIB,
       "ipxGroup": ipxGroup,
       "ipxGroupBE": ipxGroupBE,
       "ipxGroupBE01": ipxGroupBE01,
       "ipxGroupBE01A": ipxGroupBE01A,
       "ipxCapabilities": ipxCapabilities,
       "ipxCapabilitiesBE": ipxCapabilitiesBE,
       "ipxCapabilitiesBE01": ipxCapabilitiesBE01,
       "ipxCapabilitiesBE01A": ipxCapabilitiesBE01A}
)
