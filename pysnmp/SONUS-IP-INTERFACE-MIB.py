# SNMP MIB module (SONUS-IP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-IP-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:52 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusPacketMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusPacketMIBs")

(SonusName,) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusName")


# MODULE-IDENTITY

sonusIpInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusIpInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
sonusIpInterfaceMIBObjects = _SonusIpInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1)
)
_SonusNrsConfigObjects_ObjectIdentity = ObjectIdentity
sonusNrsConfigObjects = _SonusNrsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 1)
)


class _SonusNrsVirtExtRouterEnable_Type(Integer32):
    """Custom type sonusNrsVirtExtRouterEnable based on Integer32"""
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


_SonusNrsVirtExtRouterEnable_Type.__name__ = "Integer32"
_SonusNrsVirtExtRouterEnable_Object = MibScalar
sonusNrsVirtExtRouterEnable = _SonusNrsVirtExtRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 1, 1),
    _SonusNrsVirtExtRouterEnable_Type()
)
sonusNrsVirtExtRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsVirtExtRouterEnable.setStatus("current")
_SonusNif_ObjectIdentity = ObjectIdentity
sonusNif = _SonusNif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3)
)
_SonusNifNextIndex_Type = Integer32
_SonusNifNextIndex_Object = MibScalar
sonusNifNextIndex = _SonusNifNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 1),
    _SonusNifNextIndex_Type()
)
sonusNifNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifNextIndex.setStatus("current")
_SonusNifTable_Object = MibTable
sonusNifTable = _SonusNifTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusNifTable.setStatus("current")
_SonusNifEntry_Object = MibTableRow
sonusNifEntry = _SonusNifEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1)
)
sonusNifEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
)
if mibBuilder.loadTexts:
    sonusNifEntry.setStatus("current")
_SonusNifIndex_Type = Integer32
_SonusNifIndex_Object = MibTableColumn
sonusNifIndex = _SonusNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 1),
    _SonusNifIndex_Type()
)
sonusNifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifIndex.setStatus("current")
_SonusNifName_Type = SonusName
_SonusNifName_Object = MibTableColumn
sonusNifName = _SonusNifName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 2),
    _SonusNifName_Type()
)
sonusNifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifName.setStatus("current")


class _SonusNifType_Type(IANAifType):
    """Custom type sonusNifType based on IANAifType"""
    defaultValue = 6


_SonusNifType_Object = MibTableColumn
sonusNifType = _SonusNifType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 3),
    _SonusNifType_Type()
)
sonusNifType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifType.setStatus("current")
_SonusNifIpAddress_Type = IpAddress
_SonusNifIpAddress_Object = MibTableColumn
sonusNifIpAddress = _SonusNifIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 4),
    _SonusNifIpAddress_Type()
)
sonusNifIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifIpAddress.setStatus("current")
_SonusNifIpMask_Type = IpAddress
_SonusNifIpMask_Object = MibTableColumn
sonusNifIpMask = _SonusNifIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 5),
    _SonusNifIpMask_Type()
)
sonusNifIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifIpMask.setStatus("current")


class _SonusNifMtu_Type(Integer32):
    """Custom type sonusNifMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 1500),
    )


_SonusNifMtu_Type.__name__ = "Integer32"
_SonusNifMtu_Object = MibTableColumn
sonusNifMtu = _SonusNifMtu_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 6),
    _SonusNifMtu_Type()
)
sonusNifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifMtu.setStatus("current")


class _SonusNifShelf_Type(Integer32):
    """Custom type sonusNifShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNifShelf_Type.__name__ = "Integer32"
_SonusNifShelf_Object = MibTableColumn
sonusNifShelf = _SonusNifShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 7),
    _SonusNifShelf_Type()
)
sonusNifShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifShelf.setStatus("current")


class _SonusNifSlot_Type(Integer32):
    """Custom type sonusNifSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNifSlot_Type.__name__ = "Integer32"
_SonusNifSlot_Object = MibTableColumn
sonusNifSlot = _SonusNifSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 8),
    _SonusNifSlot_Type()
)
sonusNifSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifSlot.setStatus("current")


class _SonusNifPort_Type(Integer32):
    """Custom type sonusNifPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SonusNifPort_Type.__name__ = "Integer32"
_SonusNifPort_Object = MibTableColumn
sonusNifPort = _SonusNifPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 9),
    _SonusNifPort_Type()
)
sonusNifPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifPort.setStatus("current")


class _SonusNifCircuit_Type(Integer32):
    """Custom type sonusNifCircuit based on Integer32"""
    defaultValue = 1


_SonusNifCircuit_Object = MibTableColumn
sonusNifCircuit = _SonusNifCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 10),
    _SonusNifCircuit_Type()
)
sonusNifCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifCircuit.setStatus("current")
_SonusNifNextHopAddr_Type = IpAddress
_SonusNifNextHopAddr_Object = MibTableColumn
sonusNifNextHopAddr = _SonusNifNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 11),
    _SonusNifNextHopAddr_Type()
)
sonusNifNextHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifNextHopAddr.setStatus("current")


class _SonusNifMode_Type(Integer32):
    """Custom type sonusNifMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("outOfService", 1))
    )


_SonusNifMode_Type.__name__ = "Integer32"
_SonusNifMode_Object = MibTableColumn
sonusNifMode = _SonusNifMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 12),
    _SonusNifMode_Type()
)
sonusNifMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifMode.setStatus("current")


class _SonusNifAction_Type(Integer32):
    """Custom type sonusNifAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 1),
          ("force", 2))
    )


_SonusNifAction_Type.__name__ = "Integer32"
_SonusNifAction_Object = MibTableColumn
sonusNifAction = _SonusNifAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 13),
    _SonusNifAction_Type()
)
sonusNifAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifAction.setStatus("current")


class _SonusNifTimeout_Type(Integer32):
    """Custom type sonusNifTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusNifTimeout_Type.__name__ = "Integer32"
_SonusNifTimeout_Object = MibTableColumn
sonusNifTimeout = _SonusNifTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 14),
    _SonusNifTimeout_Type()
)
sonusNifTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifTimeout.setStatus("current")


class _SonusNifState_Type(Integer32):
    """Custom type sonusNifState based on Integer32"""
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


_SonusNifState_Type.__name__ = "Integer32"
_SonusNifState_Object = MibTableColumn
sonusNifState = _SonusNifState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 15),
    _SonusNifState_Type()
)
sonusNifState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifState.setStatus("current")


class _SonusNifOutOfServiceReason_Type(Integer32):
    """Custom type sonusNifOutOfServiceReason based on Integer32"""
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
        *(("admin", 2),
          ("gateway", 3),
          ("linkDown", 9),
          ("noVc", 7),
          ("notApplicable", 1),
          ("portDown", 4),
          ("serverDown", 5),
          ("srvrAbsent", 8),
          ("vcsDown", 6))
    )


_SonusNifOutOfServiceReason_Type.__name__ = "Integer32"
_SonusNifOutOfServiceReason_Object = MibTableColumn
sonusNifOutOfServiceReason = _SonusNifOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 16),
    _SonusNifOutOfServiceReason_Type()
)
sonusNifOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifOutOfServiceReason.setStatus("current")


class _SonusNifClass_Type(Integer32):
    """Custom type sonusNifClass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("reserved", 2))
    )


_SonusNifClass_Type.__name__ = "Integer32"
_SonusNifClass_Object = MibTableColumn
sonusNifClass = _SonusNifClass_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 17),
    _SonusNifClass_Type()
)
sonusNifClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifClass.setStatus("current")
_SonusNifRowStatus_Type = RowStatus
_SonusNifRowStatus_Object = MibTableColumn
sonusNifRowStatus = _SonusNifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 18),
    _SonusNifRowStatus_Type()
)
sonusNifRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifRowStatus.setStatus("current")


class _SonusNifBwDeviation_Type(Integer32):
    """Custom type sonusNifBwDeviation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusNifBwDeviation_Type.__name__ = "Integer32"
_SonusNifBwDeviation_Object = MibTableColumn
sonusNifBwDeviation = _SonusNifBwDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 19),
    _SonusNifBwDeviation_Type()
)
sonusNifBwDeviation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifBwDeviation.setStatus("current")


class _SonusNifBwContingency_Type(Integer32):
    """Custom type sonusNifBwContingency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusNifBwContingency_Type.__name__ = "Integer32"
_SonusNifBwContingency_Object = MibTableColumn
sonusNifBwContingency = _SonusNifBwContingency_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 3, 2, 1, 20),
    _SonusNifBwContingency_Type()
)
sonusNifBwContingency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNifBwContingency.setStatus("current")
_SonusNifAdmnTable_Object = MibTable
sonusNifAdmnTable = _SonusNifAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sonusNifAdmnTable.setStatus("current")
_SonusNifAdmnEntry_Object = MibTableRow
sonusNifAdmnEntry = _SonusNifAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6, 1)
)
sonusNifAdmnEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNifAdmnShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNifAdmnSlot"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNifAdmnPort"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNifAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusNifAdmnEntry.setStatus("current")
_SonusNifAdmnShelf_Type = Integer32
_SonusNifAdmnShelf_Object = MibTableColumn
sonusNifAdmnShelf = _SonusNifAdmnShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6, 1, 1),
    _SonusNifAdmnShelf_Type()
)
sonusNifAdmnShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifAdmnShelf.setStatus("current")
_SonusNifAdmnSlot_Type = Integer32
_SonusNifAdmnSlot_Object = MibTableColumn
sonusNifAdmnSlot = _SonusNifAdmnSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6, 1, 2),
    _SonusNifAdmnSlot_Type()
)
sonusNifAdmnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifAdmnSlot.setStatus("current")
_SonusNifAdmnPort_Type = Integer32
_SonusNifAdmnPort_Object = MibTableColumn
sonusNifAdmnPort = _SonusNifAdmnPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6, 1, 3),
    _SonusNifAdmnPort_Type()
)
sonusNifAdmnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifAdmnPort.setStatus("current")
_SonusNifAdmnIndex_Type = Integer32
_SonusNifAdmnIndex_Object = MibTableColumn
sonusNifAdmnIndex = _SonusNifAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 6, 1, 4),
    _SonusNifAdmnIndex_Type()
)
sonusNifAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifAdmnIndex.setStatus("current")
_SonusNrsMgmtIfTable_Object = MibTable
sonusNrsMgmtIfTable = _SonusNrsMgmtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sonusNrsMgmtIfTable.setStatus("current")
_SonusNrsMgmtIfEntry_Object = MibTableRow
sonusNrsMgmtIfEntry = _SonusNrsMgmtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1)
)
sonusNrsMgmtIfEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsMgmtIfShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsMgmtIfSlot"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsMgmtIfPort"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsMgmtIfCircuit"),
)
if mibBuilder.loadTexts:
    sonusNrsMgmtIfEntry.setStatus("current")
_SonusNrsMgmtIfIndex_Type = Integer32
_SonusNrsMgmtIfIndex_Object = MibTableColumn
sonusNrsMgmtIfIndex = _SonusNrsMgmtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 1),
    _SonusNrsMgmtIfIndex_Type()
)
sonusNrsMgmtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfIndex.setStatus("current")
_SonusNrsMgmtIfShelf_Type = Integer32
_SonusNrsMgmtIfShelf_Object = MibTableColumn
sonusNrsMgmtIfShelf = _SonusNrsMgmtIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 2),
    _SonusNrsMgmtIfShelf_Type()
)
sonusNrsMgmtIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfShelf.setStatus("current")
_SonusNrsMgmtIfSlot_Type = Integer32
_SonusNrsMgmtIfSlot_Object = MibTableColumn
sonusNrsMgmtIfSlot = _SonusNrsMgmtIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 3),
    _SonusNrsMgmtIfSlot_Type()
)
sonusNrsMgmtIfSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfSlot.setStatus("current")
_SonusNrsMgmtIfPort_Type = Integer32
_SonusNrsMgmtIfPort_Object = MibTableColumn
sonusNrsMgmtIfPort = _SonusNrsMgmtIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 4),
    _SonusNrsMgmtIfPort_Type()
)
sonusNrsMgmtIfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfPort.setStatus("current")
_SonusNrsMgmtIfCircuit_Type = Integer32
_SonusNrsMgmtIfCircuit_Object = MibTableColumn
sonusNrsMgmtIfCircuit = _SonusNrsMgmtIfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 5),
    _SonusNrsMgmtIfCircuit_Type()
)
sonusNrsMgmtIfCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfCircuit.setStatus("current")
_SonusNrsMgmtIfType_Type = IANAifType
_SonusNrsMgmtIfType_Object = MibTableColumn
sonusNrsMgmtIfType = _SonusNrsMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 6),
    _SonusNrsMgmtIfType_Type()
)
sonusNrsMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfType.setStatus("current")
_SonusNrsMgmtIfIpAddress_Type = IpAddress
_SonusNrsMgmtIfIpAddress_Object = MibTableColumn
sonusNrsMgmtIfIpAddress = _SonusNrsMgmtIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 7),
    _SonusNrsMgmtIfIpAddress_Type()
)
sonusNrsMgmtIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfIpAddress.setStatus("current")
_SonusNrsMgmtIfIpMask_Type = IpAddress
_SonusNrsMgmtIfIpMask_Object = MibTableColumn
sonusNrsMgmtIfIpMask = _SonusNrsMgmtIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 8),
    _SonusNrsMgmtIfIpMask_Type()
)
sonusNrsMgmtIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfIpMask.setStatus("current")
_SonusNrsMgmtIfMtu_Type = Integer32
_SonusNrsMgmtIfMtu_Object = MibTableColumn
sonusNrsMgmtIfMtu = _SonusNrsMgmtIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 9),
    _SonusNrsMgmtIfMtu_Type()
)
sonusNrsMgmtIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfMtu.setStatus("current")
_SonusNrsMgmtIfGatewayAddress_Type = IpAddress
_SonusNrsMgmtIfGatewayAddress_Object = MibTableColumn
sonusNrsMgmtIfGatewayAddress = _SonusNrsMgmtIfGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 10),
    _SonusNrsMgmtIfGatewayAddress_Type()
)
sonusNrsMgmtIfGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfGatewayAddress.setStatus("current")


class _SonusNrsMgmtIfMode_Type(Integer32):
    """Custom type sonusNrsMgmtIfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1))
    )


_SonusNrsMgmtIfMode_Type.__name__ = "Integer32"
_SonusNrsMgmtIfMode_Object = MibTableColumn
sonusNrsMgmtIfMode = _SonusNrsMgmtIfMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 11),
    _SonusNrsMgmtIfMode_Type()
)
sonusNrsMgmtIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfMode.setStatus("current")


class _SonusNrsMgmtIfAdminStatus_Type(Integer32):
    """Custom type sonusNrsMgmtIfAdminStatus based on Integer32"""
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


_SonusNrsMgmtIfAdminStatus_Type.__name__ = "Integer32"
_SonusNrsMgmtIfAdminStatus_Object = MibTableColumn
sonusNrsMgmtIfAdminStatus = _SonusNrsMgmtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 12),
    _SonusNrsMgmtIfAdminStatus_Type()
)
sonusNrsMgmtIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfAdminStatus.setStatus("current")


class _SonusNrsMgmtIfOperStatus_Type(Integer32):
    """Custom type sonusNrsMgmtIfOperStatus based on Integer32"""
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
        *(("inService", 2),
          ("outOfService", 1),
          ("outOfServiceDisabled", 3),
          ("outOfServiceLinkDown", 4))
    )


_SonusNrsMgmtIfOperStatus_Type.__name__ = "Integer32"
_SonusNrsMgmtIfOperStatus_Object = MibTableColumn
sonusNrsMgmtIfOperStatus = _SonusNrsMgmtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 13),
    _SonusNrsMgmtIfOperStatus_Type()
)
sonusNrsMgmtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfOperStatus.setStatus("current")
_SonusNrsMgmtIfLogicMgmtIpAddress_Type = IpAddress
_SonusNrsMgmtIfLogicMgmtIpAddress_Object = MibTableColumn
sonusNrsMgmtIfLogicMgmtIpAddress = _SonusNrsMgmtIfLogicMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 7, 1, 14),
    _SonusNrsMgmtIfLogicMgmtIpAddress_Type()
)
sonusNrsMgmtIfLogicMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsMgmtIfLogicMgmtIpAddress.setStatus("current")
_SonusNrsLogicMgmtIfAdmnTable_Object = MibTable
sonusNrsLogicMgmtIfAdmnTable = _SonusNrsLogicMgmtIfAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    sonusNrsLogicMgmtIfAdmnTable.setStatus("current")
_SonusNrsLogicMgmtIfAdmnEntry_Object = MibTableRow
sonusNrsLogicMgmtIfAdmnEntry = _SonusNrsLogicMgmtIfAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 8, 1)
)
sonusNrsLogicMgmtIfAdmnEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsLogicMgmtIfAdmnShelf"),
)
if mibBuilder.loadTexts:
    sonusNrsLogicMgmtIfAdmnEntry.setStatus("current")


class _SonusNrsLogicMgmtIfAdmnShelf_Type(Integer32):
    """Custom type sonusNrsLogicMgmtIfAdmnShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNrsLogicMgmtIfAdmnShelf_Type.__name__ = "Integer32"
_SonusNrsLogicMgmtIfAdmnShelf_Object = MibTableColumn
sonusNrsLogicMgmtIfAdmnShelf = _SonusNrsLogicMgmtIfAdmnShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 8, 1, 1),
    _SonusNrsLogicMgmtIfAdmnShelf_Type()
)
sonusNrsLogicMgmtIfAdmnShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLogicMgmtIfAdmnShelf.setStatus("current")
_SonusNrsLogicMgmtIfAdmnIpAddress_Type = IpAddress
_SonusNrsLogicMgmtIfAdmnIpAddress_Object = MibTableColumn
sonusNrsLogicMgmtIfAdmnIpAddress = _SonusNrsLogicMgmtIfAdmnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 8, 1, 2),
    _SonusNrsLogicMgmtIfAdmnIpAddress_Type()
)
sonusNrsLogicMgmtIfAdmnIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLogicMgmtIfAdmnIpAddress.setStatus("current")
_SonusNrsLogicMgmtIfAdmnIpAddressB_Type = IpAddress
_SonusNrsLogicMgmtIfAdmnIpAddressB_Object = MibTableColumn
sonusNrsLogicMgmtIfAdmnIpAddressB = _SonusNrsLogicMgmtIfAdmnIpAddressB_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 8, 1, 3),
    _SonusNrsLogicMgmtIfAdmnIpAddressB_Type()
)
sonusNrsLogicMgmtIfAdmnIpAddressB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLogicMgmtIfAdmnIpAddressB.setStatus("current")
_SonusNrsLinkFailureParamAdmnTable_Object = MibTable
sonusNrsLinkFailureParamAdmnTable = _SonusNrsLinkFailureParamAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnTable.setStatus("current")
_SonusNrsLinkFailureParamAdmnEntry_Object = MibTableRow
sonusNrsLinkFailureParamAdmnEntry = _SonusNrsLinkFailureParamAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1)
)
sonusNrsLinkFailureParamAdmnEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsLinkFailureParamAdmnShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsLinkFailureParamAdmnSlot"),
)
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnEntry.setStatus("current")


class _SonusNrsLinkFailureParamAdmnShelf_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNrsLinkFailureParamAdmnShelf_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnShelf_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnShelf = _SonusNrsLinkFailureParamAdmnShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 1),
    _SonusNrsLinkFailureParamAdmnShelf_Type()
)
sonusNrsLinkFailureParamAdmnShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnShelf.setStatus("current")


class _SonusNrsLinkFailureParamAdmnSlot_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNrsLinkFailureParamAdmnSlot_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnSlot_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnSlot = _SonusNrsLinkFailureParamAdmnSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 2),
    _SonusNrsLinkFailureParamAdmnSlot_Type()
)
sonusNrsLinkFailureParamAdmnSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnSlot.setStatus("current")


class _SonusNrsLinkFailureParamAdmnThreshold_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusNrsLinkFailureParamAdmnThreshold_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnThreshold_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnThreshold = _SonusNrsLinkFailureParamAdmnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 3),
    _SonusNrsLinkFailureParamAdmnThreshold_Type()
)
sonusNrsLinkFailureParamAdmnThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnThreshold.setStatus("current")


class _SonusNrsLinkFailureParamAdmnRetries_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SonusNrsLinkFailureParamAdmnRetries_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnRetries_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnRetries = _SonusNrsLinkFailureParamAdmnRetries_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 4),
    _SonusNrsLinkFailureParamAdmnRetries_Type()
)
sonusNrsLinkFailureParamAdmnRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnRetries.setStatus("current")


class _SonusNrsLinkFailureParamAdmnVerifyTimer_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnVerifyTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SonusNrsLinkFailureParamAdmnVerifyTimer_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnVerifyTimer_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnVerifyTimer = _SonusNrsLinkFailureParamAdmnVerifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 5),
    _SonusNrsLinkFailureParamAdmnVerifyTimer_Type()
)
sonusNrsLinkFailureParamAdmnVerifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnVerifyTimer.setStatus("current")


class _SonusNrsLinkFailureParamAdmnReattemptTimer_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnReattemptTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SonusNrsLinkFailureParamAdmnReattemptTimer_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnReattemptTimer_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnReattemptTimer = _SonusNrsLinkFailureParamAdmnReattemptTimer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 6),
    _SonusNrsLinkFailureParamAdmnReattemptTimer_Type()
)
sonusNrsLinkFailureParamAdmnReattemptTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnReattemptTimer.setStatus("current")


class _SonusNrsLinkFailureParamAdmnState_Type(Integer32):
    """Custom type sonusNrsLinkFailureParamAdmnState based on Integer32"""
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


_SonusNrsLinkFailureParamAdmnState_Type.__name__ = "Integer32"
_SonusNrsLinkFailureParamAdmnState_Object = MibTableColumn
sonusNrsLinkFailureParamAdmnState = _SonusNrsLinkFailureParamAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 9, 1, 7),
    _SonusNrsLinkFailureParamAdmnState_Type()
)
sonusNrsLinkFailureParamAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureParamAdmnState.setStatus("current")
_SonusNrsLinkFailureStatTable_Object = MibTable
sonusNrsLinkFailureStatTable = _SonusNrsLinkFailureStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatTable.setStatus("current")
_SonusNrsLinkFailureStatEntry_Object = MibTableRow
sonusNrsLinkFailureStatEntry = _SonusNrsLinkFailureStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10, 1)
)
sonusNrsLinkFailureStatEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsLinkFailureStatShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsLinkFailureStatSlot"),
)
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatEntry.setStatus("current")
_SonusNrsLinkFailureStatShelf_Type = Integer32
_SonusNrsLinkFailureStatShelf_Object = MibTableColumn
sonusNrsLinkFailureStatShelf = _SonusNrsLinkFailureStatShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10, 1, 1),
    _SonusNrsLinkFailureStatShelf_Type()
)
sonusNrsLinkFailureStatShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatShelf.setStatus("current")
_SonusNrsLinkFailureStatSlot_Type = Integer32
_SonusNrsLinkFailureStatSlot_Object = MibTableColumn
sonusNrsLinkFailureStatSlot = _SonusNrsLinkFailureStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10, 1, 2),
    _SonusNrsLinkFailureStatSlot_Type()
)
sonusNrsLinkFailureStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatSlot.setStatus("current")
_SonusNrsLinkFailureStatFailures_Type = Integer32
_SonusNrsLinkFailureStatFailures_Object = MibTableColumn
sonusNrsLinkFailureStatFailures = _SonusNrsLinkFailureStatFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10, 1, 3),
    _SonusNrsLinkFailureStatFailures_Type()
)
sonusNrsLinkFailureStatFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatFailures.setStatus("current")
_SonusNrsLinkFailureStatRedundFailures_Type = Integer32
_SonusNrsLinkFailureStatRedundFailures_Object = MibTableColumn
sonusNrsLinkFailureStatRedundFailures = _SonusNrsLinkFailureStatRedundFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 10, 1, 4),
    _SonusNrsLinkFailureStatRedundFailures_Type()
)
sonusNrsLinkFailureStatRedundFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsLinkFailureStatRedundFailures.setStatus("current")
_SonusNrsPerDestLinkFailureStatTable_Object = MibTable
sonusNrsPerDestLinkFailureStatTable = _SonusNrsPerDestLinkFailureStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatTable.setStatus("current")
_SonusNrsPerDestLinkFailureStatEntry_Object = MibTableRow
sonusNrsPerDestLinkFailureStatEntry = _SonusNrsPerDestLinkFailureStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1)
)
sonusNrsPerDestLinkFailureStatEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsPerDestLinkFailureStatIfIndex"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsPerDestLinkFailureStatIpAddress"),
)
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatEntry.setStatus("current")
_SonusNrsPerDestLinkFailureStatIfIndex_Type = Integer32
_SonusNrsPerDestLinkFailureStatIfIndex_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatIfIndex = _SonusNrsPerDestLinkFailureStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 1),
    _SonusNrsPerDestLinkFailureStatIfIndex_Type()
)
sonusNrsPerDestLinkFailureStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatIfIndex.setStatus("current")
_SonusNrsPerDestLinkFailureStatIpAddress_Type = IpAddress
_SonusNrsPerDestLinkFailureStatIpAddress_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatIpAddress = _SonusNrsPerDestLinkFailureStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 2),
    _SonusNrsPerDestLinkFailureStatIpAddress_Type()
)
sonusNrsPerDestLinkFailureStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatIpAddress.setStatus("current")
_SonusNrsPerDestLinkFailureStatMinTime_Type = Integer32
_SonusNrsPerDestLinkFailureStatMinTime_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatMinTime = _SonusNrsPerDestLinkFailureStatMinTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 3),
    _SonusNrsPerDestLinkFailureStatMinTime_Type()
)
sonusNrsPerDestLinkFailureStatMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatMinTime.setStatus("current")
_SonusNrsPerDestLinkFailureStatMaxTime_Type = Integer32
_SonusNrsPerDestLinkFailureStatMaxTime_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatMaxTime = _SonusNrsPerDestLinkFailureStatMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 4),
    _SonusNrsPerDestLinkFailureStatMaxTime_Type()
)
sonusNrsPerDestLinkFailureStatMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatMaxTime.setStatus("current")
_SonusNrsPerDestLinkFailureStatAverageTime_Type = Integer32
_SonusNrsPerDestLinkFailureStatAverageTime_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatAverageTime = _SonusNrsPerDestLinkFailureStatAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 5),
    _SonusNrsPerDestLinkFailureStatAverageTime_Type()
)
sonusNrsPerDestLinkFailureStatAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatAverageTime.setStatus("current")
_SonusNrsPerDestLinkFailureStatSumTime_Type = Integer32
_SonusNrsPerDestLinkFailureStatSumTime_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatSumTime = _SonusNrsPerDestLinkFailureStatSumTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 6),
    _SonusNrsPerDestLinkFailureStatSumTime_Type()
)
sonusNrsPerDestLinkFailureStatSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatSumTime.setStatus("current")
_SonusNrsPerDestLinkFailureStat1Failure_Type = Integer32
_SonusNrsPerDestLinkFailureStat1Failure_Object = MibTableColumn
sonusNrsPerDestLinkFailureStat1Failure = _SonusNrsPerDestLinkFailureStat1Failure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 7),
    _SonusNrsPerDestLinkFailureStat1Failure_Type()
)
sonusNrsPerDestLinkFailureStat1Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStat1Failure.setStatus("current")
_SonusNrsPerDestLinkFailureStat2Failure_Type = Integer32
_SonusNrsPerDestLinkFailureStat2Failure_Object = MibTableColumn
sonusNrsPerDestLinkFailureStat2Failure = _SonusNrsPerDestLinkFailureStat2Failure_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 8),
    _SonusNrsPerDestLinkFailureStat2Failure_Type()
)
sonusNrsPerDestLinkFailureStat2Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStat2Failure.setStatus("current")
_SonusNrsPerDestLinkFailureStatFailures_Type = Integer32
_SonusNrsPerDestLinkFailureStatFailures_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatFailures = _SonusNrsPerDestLinkFailureStatFailures_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 9),
    _SonusNrsPerDestLinkFailureStatFailures_Type()
)
sonusNrsPerDestLinkFailureStatFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatFailures.setStatus("current")
_SonusNrsPerDestLinkFailureStatReplies_Type = Integer32
_SonusNrsPerDestLinkFailureStatReplies_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatReplies = _SonusNrsPerDestLinkFailureStatReplies_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 10),
    _SonusNrsPerDestLinkFailureStatReplies_Type()
)
sonusNrsPerDestLinkFailureStatReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatReplies.setStatus("current")
_SonusNrsPerDestLinkFailureStatDupeReplies_Type = Integer32
_SonusNrsPerDestLinkFailureStatDupeReplies_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatDupeReplies = _SonusNrsPerDestLinkFailureStatDupeReplies_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 11),
    _SonusNrsPerDestLinkFailureStatDupeReplies_Type()
)
sonusNrsPerDestLinkFailureStatDupeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatDupeReplies.setStatus("current")
_SonusNrsPerDestLinkFailureStatLateReplies_Type = Integer32
_SonusNrsPerDestLinkFailureStatLateReplies_Object = MibTableColumn
sonusNrsPerDestLinkFailureStatLateReplies = _SonusNrsPerDestLinkFailureStatLateReplies_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 11, 1, 12),
    _SonusNrsPerDestLinkFailureStatLateReplies_Type()
)
sonusNrsPerDestLinkFailureStatLateReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsPerDestLinkFailureStatLateReplies.setStatus("current")
_SonusSrvrEthernetSwitchIpTable_Object = MibTable
sonusSrvrEthernetSwitchIpTable = _SonusSrvrEthernetSwitchIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12)
)
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpTable.setStatus("current")
_SonusSrvrEthernetSwitchIpEntry_Object = MibTableRow
sonusSrvrEthernetSwitchIpEntry = _SonusSrvrEthernetSwitchIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12, 1)
)
sonusSrvrEthernetSwitchIpEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusSrvrEthernetSwitchIpShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusSrvrEthernetSwitchIpSlot"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusSrvrEthernetSwitchIpPort"),
)
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpEntry.setStatus("current")


class _SonusSrvrEthernetSwitchIpShelf_Type(Integer32):
    """Custom type sonusSrvrEthernetSwitchIpShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusSrvrEthernetSwitchIpShelf_Type.__name__ = "Integer32"
_SonusSrvrEthernetSwitchIpShelf_Object = MibTableColumn
sonusSrvrEthernetSwitchIpShelf = _SonusSrvrEthernetSwitchIpShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12, 1, 1),
    _SonusSrvrEthernetSwitchIpShelf_Type()
)
sonusSrvrEthernetSwitchIpShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpShelf.setStatus("current")


class _SonusSrvrEthernetSwitchIpSlot_Type(Integer32):
    """Custom type sonusSrvrEthernetSwitchIpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusSrvrEthernetSwitchIpSlot_Type.__name__ = "Integer32"
_SonusSrvrEthernetSwitchIpSlot_Object = MibTableColumn
sonusSrvrEthernetSwitchIpSlot = _SonusSrvrEthernetSwitchIpSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12, 1, 2),
    _SonusSrvrEthernetSwitchIpSlot_Type()
)
sonusSrvrEthernetSwitchIpSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpSlot.setStatus("current")
_SonusSrvrEthernetSwitchIpIpAddress_Type = IpAddress
_SonusSrvrEthernetSwitchIpIpAddress_Object = MibTableColumn
sonusSrvrEthernetSwitchIpIpAddress = _SonusSrvrEthernetSwitchIpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12, 1, 3),
    _SonusSrvrEthernetSwitchIpIpAddress_Type()
)
sonusSrvrEthernetSwitchIpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpIpAddress.setStatus("current")


class _SonusSrvrEthernetSwitchIpPort_Type(Integer32):
    """Custom type sonusSrvrEthernetSwitchIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusSrvrEthernetSwitchIpPort_Type.__name__ = "Integer32"
_SonusSrvrEthernetSwitchIpPort_Object = MibTableColumn
sonusSrvrEthernetSwitchIpPort = _SonusSrvrEthernetSwitchIpPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 12, 1, 4),
    _SonusSrvrEthernetSwitchIpPort_Type()
)
sonusSrvrEthernetSwitchIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSrvrEthernetSwitchIpPort.setStatus("current")
_SonusNrsSocketAccessAdmnTable_Object = MibTable
sonusNrsSocketAccessAdmnTable = _SonusNrsSocketAccessAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13)
)
if mibBuilder.loadTexts:
    sonusNrsSocketAccessAdmnTable.setStatus("current")
_SonusNrsSocketAccessAdmnEntry_Object = MibTableRow
sonusNrsSocketAccessAdmnEntry = _SonusNrsSocketAccessAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1)
)
sonusNrsSocketAccessAdmnEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsSocketAccessProtocol"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsSocketAccessPort"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsSocketAccessIfIndex"),
)
if mibBuilder.loadTexts:
    sonusNrsSocketAccessAdmnEntry.setStatus("current")


class _SonusNrsSocketAccessProtocol_Type(Integer32):
    """Custom type sonusNrsSocketAccessProtocol based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_SonusNrsSocketAccessProtocol_Type.__name__ = "Integer32"
_SonusNrsSocketAccessProtocol_Object = MibTableColumn
sonusNrsSocketAccessProtocol = _SonusNrsSocketAccessProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1, 1),
    _SonusNrsSocketAccessProtocol_Type()
)
sonusNrsSocketAccessProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsSocketAccessProtocol.setStatus("current")


class _SonusNrsSocketAccessPort_Type(Integer32):
    """Custom type sonusNrsSocketAccessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusNrsSocketAccessPort_Type.__name__ = "Integer32"
_SonusNrsSocketAccessPort_Object = MibTableColumn
sonusNrsSocketAccessPort = _SonusNrsSocketAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1, 2),
    _SonusNrsSocketAccessPort_Type()
)
sonusNrsSocketAccessPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsSocketAccessPort.setStatus("current")


class _SonusNrsSocketAccessIfIndex_Type(Integer32):
    """Custom type sonusNrsSocketAccessIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusNrsSocketAccessIfIndex_Type.__name__ = "Integer32"
_SonusNrsSocketAccessIfIndex_Object = MibTableColumn
sonusNrsSocketAccessIfIndex = _SonusNrsSocketAccessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1, 3),
    _SonusNrsSocketAccessIfIndex_Type()
)
sonusNrsSocketAccessIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsSocketAccessIfIndex.setStatus("current")


class _SonusNrsSocketAccessPermission_Type(Integer32):
    """Custom type sonusNrsSocketAccessPermission based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_SonusNrsSocketAccessPermission_Type.__name__ = "Integer32"
_SonusNrsSocketAccessPermission_Object = MibTableColumn
sonusNrsSocketAccessPermission = _SonusNrsSocketAccessPermission_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1, 4),
    _SonusNrsSocketAccessPermission_Type()
)
sonusNrsSocketAccessPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsSocketAccessPermission.setStatus("current")
_SonusNrsSocketAccessRowStatus_Type = RowStatus
_SonusNrsSocketAccessRowStatus_Object = MibTableColumn
sonusNrsSocketAccessRowStatus = _SonusNrsSocketAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 13, 1, 5),
    _SonusNrsSocketAccessRowStatus_Type()
)
sonusNrsSocketAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsSocketAccessRowStatus.setStatus("current")
_SonusNrsDebugIfTable_Object = MibTable
sonusNrsDebugIfTable = _SonusNrsDebugIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99)
)
if mibBuilder.loadTexts:
    sonusNrsDebugIfTable.setStatus("current")
_SonusNrsDebugIfEntry_Object = MibTableRow
sonusNrsDebugIfEntry = _SonusNrsDebugIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1)
)
sonusNrsDebugIfEntry.setIndexNames(
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsDebugIfShelf"),
    (0, "SONUS-IP-INTERFACE-MIB", "sonusNrsDebugIfSlot"),
)
if mibBuilder.loadTexts:
    sonusNrsDebugIfEntry.setStatus("current")
_SonusNrsDebugIfIndex_Type = Integer32
_SonusNrsDebugIfIndex_Object = MibTableColumn
sonusNrsDebugIfIndex = _SonusNrsDebugIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 1),
    _SonusNrsDebugIfIndex_Type()
)
sonusNrsDebugIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsDebugIfIndex.setStatus("current")
_SonusNrsDebugIfShelf_Type = Integer32
_SonusNrsDebugIfShelf_Object = MibTableColumn
sonusNrsDebugIfShelf = _SonusNrsDebugIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 2),
    _SonusNrsDebugIfShelf_Type()
)
sonusNrsDebugIfShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfShelf.setStatus("current")
_SonusNrsDebugIfSlot_Type = Integer32
_SonusNrsDebugIfSlot_Object = MibTableColumn
sonusNrsDebugIfSlot = _SonusNrsDebugIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 3),
    _SonusNrsDebugIfSlot_Type()
)
sonusNrsDebugIfSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfSlot.setStatus("current")
_SonusNrsDebugIfPort_Type = Integer32
_SonusNrsDebugIfPort_Object = MibTableColumn
sonusNrsDebugIfPort = _SonusNrsDebugIfPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 4),
    _SonusNrsDebugIfPort_Type()
)
sonusNrsDebugIfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfPort.setStatus("current")
_SonusNrsDebugIfCircuit_Type = Integer32
_SonusNrsDebugIfCircuit_Object = MibTableColumn
sonusNrsDebugIfCircuit = _SonusNrsDebugIfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 5),
    _SonusNrsDebugIfCircuit_Type()
)
sonusNrsDebugIfCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfCircuit.setStatus("current")
_SonusNrsDebugIfType_Type = IANAifType
_SonusNrsDebugIfType_Object = MibTableColumn
sonusNrsDebugIfType = _SonusNrsDebugIfType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 6),
    _SonusNrsDebugIfType_Type()
)
sonusNrsDebugIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfType.setStatus("current")
_SonusNrsDebugIfIpAddress_Type = IpAddress
_SonusNrsDebugIfIpAddress_Object = MibTableColumn
sonusNrsDebugIfIpAddress = _SonusNrsDebugIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 7),
    _SonusNrsDebugIfIpAddress_Type()
)
sonusNrsDebugIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfIpAddress.setStatus("current")
_SonusNrsDebugIfIpMask_Type = IpAddress
_SonusNrsDebugIfIpMask_Object = MibTableColumn
sonusNrsDebugIfIpMask = _SonusNrsDebugIfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 8),
    _SonusNrsDebugIfIpMask_Type()
)
sonusNrsDebugIfIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfIpMask.setStatus("current")
_SonusNrsDebugIfMtu_Type = Integer32
_SonusNrsDebugIfMtu_Object = MibTableColumn
sonusNrsDebugIfMtu = _SonusNrsDebugIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 9),
    _SonusNrsDebugIfMtu_Type()
)
sonusNrsDebugIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfMtu.setStatus("current")
_SonusNrsDebugIfGatewayAddress_Type = IpAddress
_SonusNrsDebugIfGatewayAddress_Object = MibTableColumn
sonusNrsDebugIfGatewayAddress = _SonusNrsDebugIfGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 10),
    _SonusNrsDebugIfGatewayAddress_Type()
)
sonusNrsDebugIfGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfGatewayAddress.setStatus("current")


class _SonusNrsDebugIfAdminStatus_Type(Integer32):
    """Custom type sonusNrsDebugIfAdminStatus based on Integer32"""
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


_SonusNrsDebugIfAdminStatus_Type.__name__ = "Integer32"
_SonusNrsDebugIfAdminStatus_Object = MibTableColumn
sonusNrsDebugIfAdminStatus = _SonusNrsDebugIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 11),
    _SonusNrsDebugIfAdminStatus_Type()
)
sonusNrsDebugIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNrsDebugIfAdminStatus.setStatus("current")


class _SonusNrsDebugIfOperStatus_Type(Integer32):
    """Custom type sonusNrsDebugIfOperStatus based on Integer32"""
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
        *(("inService", 2),
          ("outOfService", 1),
          ("outOfServiceDisabled", 3),
          ("outOfServiceLinkDown", 4))
    )


_SonusNrsDebugIfOperStatus_Type.__name__ = "Integer32"
_SonusNrsDebugIfOperStatus_Object = MibTableColumn
sonusNrsDebugIfOperStatus = _SonusNrsDebugIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 1, 99, 1, 12),
    _SonusNrsDebugIfOperStatus_Type()
)
sonusNrsDebugIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNrsDebugIfOperStatus.setStatus("current")
_SonusIpInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
sonusIpInterfaceMIBNotifications = _SonusIpInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2)
)
_SonusIpInterfaceMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusIpInterfaceMIBNotificationsPrefix = _SonusIpInterfaceMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0)
)
_SonusIpInterfaceMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusIpInterfaceMIBNotificationsObjects = _SonusIpInterfaceMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 1)
)

# Managed Objects groups


# Notification objects

sonusNrsNifInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 1)
)
sonusNrsNifInServiceNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifInServiceNotification.setStatus(
        "current"
    )

sonusNrsNifOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 2)
)
sonusNrsNifOutOfServiceNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifOutOfServiceNotification.setStatus(
        "current"
    )

sonusNrsNifEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 3)
)
sonusNrsNifEnabledNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifEnabledNotification.setStatus(
        "current"
    )

sonusNrsNifDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 4)
)
sonusNrsNifDisabledNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifDisabledNotification.setStatus(
        "current"
    )

sonusNrsNifDeletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 5)
)
sonusNrsNifDeletedNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifDeletedNotification.setStatus(
        "current"
    )

sonusNrsNifHighWatermarkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 6)
)
sonusNrsNifHighWatermarkNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifHighWatermarkNotification.setStatus(
        "current"
    )

sonusNrsNifLowWatermarkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 7)
)
sonusNrsNifLowWatermarkNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifLowWatermarkNotification.setStatus(
        "current"
    )

sonusNrsNifBwHighDeviationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 8)
)
sonusNrsNifBwHighDeviationNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifBwHighDeviationNotification.setStatus(
        "current"
    )

sonusNrsNifBwLowDeviationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 9)
)
sonusNrsNifBwLowDeviationNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifBwLowDeviationNotification.setStatus(
        "current"
    )

sonusNrsLinkDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 10)
)
sonusNrsLinkDownNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsLinkDownNotification.setStatus(
        "current"
    )

sonusNrsLinkUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 11)
)
sonusNrsLinkUpNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsLinkUpNotification.setStatus(
        "current"
    )

sonusNrsNifCreatedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 1, 2, 0, 12)
)
sonusNrsNifCreatedNotification.setObjects(
      *(("SONUS-IP-INTERFACE-MIB", "sonusNifShelf"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifSlot"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifPort"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifIndex"),
        ("SONUS-IP-INTERFACE-MIB", "sonusNifName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNrsNifCreatedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-IP-INTERFACE-MIB",
    **{"sonusIpInterfaceMIB": sonusIpInterfaceMIB,
       "sonusIpInterfaceMIBObjects": sonusIpInterfaceMIBObjects,
       "sonusNrsConfigObjects": sonusNrsConfigObjects,
       "sonusNrsVirtExtRouterEnable": sonusNrsVirtExtRouterEnable,
       "sonusNif": sonusNif,
       "sonusNifNextIndex": sonusNifNextIndex,
       "sonusNifTable": sonusNifTable,
       "sonusNifEntry": sonusNifEntry,
       "sonusNifIndex": sonusNifIndex,
       "sonusNifName": sonusNifName,
       "sonusNifType": sonusNifType,
       "sonusNifIpAddress": sonusNifIpAddress,
       "sonusNifIpMask": sonusNifIpMask,
       "sonusNifMtu": sonusNifMtu,
       "sonusNifShelf": sonusNifShelf,
       "sonusNifSlot": sonusNifSlot,
       "sonusNifPort": sonusNifPort,
       "sonusNifCircuit": sonusNifCircuit,
       "sonusNifNextHopAddr": sonusNifNextHopAddr,
       "sonusNifMode": sonusNifMode,
       "sonusNifAction": sonusNifAction,
       "sonusNifTimeout": sonusNifTimeout,
       "sonusNifState": sonusNifState,
       "sonusNifOutOfServiceReason": sonusNifOutOfServiceReason,
       "sonusNifClass": sonusNifClass,
       "sonusNifRowStatus": sonusNifRowStatus,
       "sonusNifBwDeviation": sonusNifBwDeviation,
       "sonusNifBwContingency": sonusNifBwContingency,
       "sonusNifAdmnTable": sonusNifAdmnTable,
       "sonusNifAdmnEntry": sonusNifAdmnEntry,
       "sonusNifAdmnShelf": sonusNifAdmnShelf,
       "sonusNifAdmnSlot": sonusNifAdmnSlot,
       "sonusNifAdmnPort": sonusNifAdmnPort,
       "sonusNifAdmnIndex": sonusNifAdmnIndex,
       "sonusNrsMgmtIfTable": sonusNrsMgmtIfTable,
       "sonusNrsMgmtIfEntry": sonusNrsMgmtIfEntry,
       "sonusNrsMgmtIfIndex": sonusNrsMgmtIfIndex,
       "sonusNrsMgmtIfShelf": sonusNrsMgmtIfShelf,
       "sonusNrsMgmtIfSlot": sonusNrsMgmtIfSlot,
       "sonusNrsMgmtIfPort": sonusNrsMgmtIfPort,
       "sonusNrsMgmtIfCircuit": sonusNrsMgmtIfCircuit,
       "sonusNrsMgmtIfType": sonusNrsMgmtIfType,
       "sonusNrsMgmtIfIpAddress": sonusNrsMgmtIfIpAddress,
       "sonusNrsMgmtIfIpMask": sonusNrsMgmtIfIpMask,
       "sonusNrsMgmtIfMtu": sonusNrsMgmtIfMtu,
       "sonusNrsMgmtIfGatewayAddress": sonusNrsMgmtIfGatewayAddress,
       "sonusNrsMgmtIfMode": sonusNrsMgmtIfMode,
       "sonusNrsMgmtIfAdminStatus": sonusNrsMgmtIfAdminStatus,
       "sonusNrsMgmtIfOperStatus": sonusNrsMgmtIfOperStatus,
       "sonusNrsMgmtIfLogicMgmtIpAddress": sonusNrsMgmtIfLogicMgmtIpAddress,
       "sonusNrsLogicMgmtIfAdmnTable": sonusNrsLogicMgmtIfAdmnTable,
       "sonusNrsLogicMgmtIfAdmnEntry": sonusNrsLogicMgmtIfAdmnEntry,
       "sonusNrsLogicMgmtIfAdmnShelf": sonusNrsLogicMgmtIfAdmnShelf,
       "sonusNrsLogicMgmtIfAdmnIpAddress": sonusNrsLogicMgmtIfAdmnIpAddress,
       "sonusNrsLogicMgmtIfAdmnIpAddressB": sonusNrsLogicMgmtIfAdmnIpAddressB,
       "sonusNrsLinkFailureParamAdmnTable": sonusNrsLinkFailureParamAdmnTable,
       "sonusNrsLinkFailureParamAdmnEntry": sonusNrsLinkFailureParamAdmnEntry,
       "sonusNrsLinkFailureParamAdmnShelf": sonusNrsLinkFailureParamAdmnShelf,
       "sonusNrsLinkFailureParamAdmnSlot": sonusNrsLinkFailureParamAdmnSlot,
       "sonusNrsLinkFailureParamAdmnThreshold": sonusNrsLinkFailureParamAdmnThreshold,
       "sonusNrsLinkFailureParamAdmnRetries": sonusNrsLinkFailureParamAdmnRetries,
       "sonusNrsLinkFailureParamAdmnVerifyTimer": sonusNrsLinkFailureParamAdmnVerifyTimer,
       "sonusNrsLinkFailureParamAdmnReattemptTimer": sonusNrsLinkFailureParamAdmnReattemptTimer,
       "sonusNrsLinkFailureParamAdmnState": sonusNrsLinkFailureParamAdmnState,
       "sonusNrsLinkFailureStatTable": sonusNrsLinkFailureStatTable,
       "sonusNrsLinkFailureStatEntry": sonusNrsLinkFailureStatEntry,
       "sonusNrsLinkFailureStatShelf": sonusNrsLinkFailureStatShelf,
       "sonusNrsLinkFailureStatSlot": sonusNrsLinkFailureStatSlot,
       "sonusNrsLinkFailureStatFailures": sonusNrsLinkFailureStatFailures,
       "sonusNrsLinkFailureStatRedundFailures": sonusNrsLinkFailureStatRedundFailures,
       "sonusNrsPerDestLinkFailureStatTable": sonusNrsPerDestLinkFailureStatTable,
       "sonusNrsPerDestLinkFailureStatEntry": sonusNrsPerDestLinkFailureStatEntry,
       "sonusNrsPerDestLinkFailureStatIfIndex": sonusNrsPerDestLinkFailureStatIfIndex,
       "sonusNrsPerDestLinkFailureStatIpAddress": sonusNrsPerDestLinkFailureStatIpAddress,
       "sonusNrsPerDestLinkFailureStatMinTime": sonusNrsPerDestLinkFailureStatMinTime,
       "sonusNrsPerDestLinkFailureStatMaxTime": sonusNrsPerDestLinkFailureStatMaxTime,
       "sonusNrsPerDestLinkFailureStatAverageTime": sonusNrsPerDestLinkFailureStatAverageTime,
       "sonusNrsPerDestLinkFailureStatSumTime": sonusNrsPerDestLinkFailureStatSumTime,
       "sonusNrsPerDestLinkFailureStat1Failure": sonusNrsPerDestLinkFailureStat1Failure,
       "sonusNrsPerDestLinkFailureStat2Failure": sonusNrsPerDestLinkFailureStat2Failure,
       "sonusNrsPerDestLinkFailureStatFailures": sonusNrsPerDestLinkFailureStatFailures,
       "sonusNrsPerDestLinkFailureStatReplies": sonusNrsPerDestLinkFailureStatReplies,
       "sonusNrsPerDestLinkFailureStatDupeReplies": sonusNrsPerDestLinkFailureStatDupeReplies,
       "sonusNrsPerDestLinkFailureStatLateReplies": sonusNrsPerDestLinkFailureStatLateReplies,
       "sonusSrvrEthernetSwitchIpTable": sonusSrvrEthernetSwitchIpTable,
       "sonusSrvrEthernetSwitchIpEntry": sonusSrvrEthernetSwitchIpEntry,
       "sonusSrvrEthernetSwitchIpShelf": sonusSrvrEthernetSwitchIpShelf,
       "sonusSrvrEthernetSwitchIpSlot": sonusSrvrEthernetSwitchIpSlot,
       "sonusSrvrEthernetSwitchIpIpAddress": sonusSrvrEthernetSwitchIpIpAddress,
       "sonusSrvrEthernetSwitchIpPort": sonusSrvrEthernetSwitchIpPort,
       "sonusNrsSocketAccessAdmnTable": sonusNrsSocketAccessAdmnTable,
       "sonusNrsSocketAccessAdmnEntry": sonusNrsSocketAccessAdmnEntry,
       "sonusNrsSocketAccessProtocol": sonusNrsSocketAccessProtocol,
       "sonusNrsSocketAccessPort": sonusNrsSocketAccessPort,
       "sonusNrsSocketAccessIfIndex": sonusNrsSocketAccessIfIndex,
       "sonusNrsSocketAccessPermission": sonusNrsSocketAccessPermission,
       "sonusNrsSocketAccessRowStatus": sonusNrsSocketAccessRowStatus,
       "sonusNrsDebugIfTable": sonusNrsDebugIfTable,
       "sonusNrsDebugIfEntry": sonusNrsDebugIfEntry,
       "sonusNrsDebugIfIndex": sonusNrsDebugIfIndex,
       "sonusNrsDebugIfShelf": sonusNrsDebugIfShelf,
       "sonusNrsDebugIfSlot": sonusNrsDebugIfSlot,
       "sonusNrsDebugIfPort": sonusNrsDebugIfPort,
       "sonusNrsDebugIfCircuit": sonusNrsDebugIfCircuit,
       "sonusNrsDebugIfType": sonusNrsDebugIfType,
       "sonusNrsDebugIfIpAddress": sonusNrsDebugIfIpAddress,
       "sonusNrsDebugIfIpMask": sonusNrsDebugIfIpMask,
       "sonusNrsDebugIfMtu": sonusNrsDebugIfMtu,
       "sonusNrsDebugIfGatewayAddress": sonusNrsDebugIfGatewayAddress,
       "sonusNrsDebugIfAdminStatus": sonusNrsDebugIfAdminStatus,
       "sonusNrsDebugIfOperStatus": sonusNrsDebugIfOperStatus,
       "sonusIpInterfaceMIBNotifications": sonusIpInterfaceMIBNotifications,
       "sonusIpInterfaceMIBNotificationsPrefix": sonusIpInterfaceMIBNotificationsPrefix,
       "sonusNrsNifInServiceNotification": sonusNrsNifInServiceNotification,
       "sonusNrsNifOutOfServiceNotification": sonusNrsNifOutOfServiceNotification,
       "sonusNrsNifEnabledNotification": sonusNrsNifEnabledNotification,
       "sonusNrsNifDisabledNotification": sonusNrsNifDisabledNotification,
       "sonusNrsNifDeletedNotification": sonusNrsNifDeletedNotification,
       "sonusNrsNifHighWatermarkNotification": sonusNrsNifHighWatermarkNotification,
       "sonusNrsNifLowWatermarkNotification": sonusNrsNifLowWatermarkNotification,
       "sonusNrsNifBwHighDeviationNotification": sonusNrsNifBwHighDeviationNotification,
       "sonusNrsNifBwLowDeviationNotification": sonusNrsNifBwLowDeviationNotification,
       "sonusNrsLinkDownNotification": sonusNrsLinkDownNotification,
       "sonusNrsLinkUpNotification": sonusNrsLinkUpNotification,
       "sonusNrsNifCreatedNotification": sonusNrsNifCreatedNotification,
       "sonusIpInterfaceMIBNotificationsObjects": sonusIpInterfaceMIBNotificationsObjects}
)
