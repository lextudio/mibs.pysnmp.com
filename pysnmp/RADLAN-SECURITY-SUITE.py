# SNMP MIB module (RADLAN-SECURITY-SUITE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-SECURITY-SUITE
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:18 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(Percents,
 rnd) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "Percents",
    "rnd")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlSecuritySuiteMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 120)
)
rlSecuritySuiteMib.setRevisions(
        ("2006-01-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlsecuritySuiteGlobalEnableType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable-all-rules-types", 2),
          ("enable-global-rules-only", 1))
    )



class RlSecuritySuiteKnownDosAttackType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("back-orifice-Trojan", 3),
          ("invasor-Trojan", 2),
          ("stacheldraht", 1))
    )



class RlSecuritySuiteKnownDosAttackProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("upd", 2))
    )



class RlSecuritySuiteAllMartianEntryType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("static", 2))
    )



class RlSecuritySuiteDenyAttackType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fragmented", 3),
          ("icmp-echo-request", 2),
          ("syn", 1))
    )



class RlSecuritySuiteDenySynFinTcp(Integer32, TextualConvention):
    status = "current"
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



class RlSecuritySuiteSynProtectionMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 3),
          ("disabled", 1),
          ("report", 2))
    )



class RlSecuritySuiteSynProtectionPortMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attacked", 2),
          ("blocked", 3),
          ("normal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlSecuritySuiteGlobalEnable_Type = RlsecuritySuiteGlobalEnableType
_RlSecuritySuiteGlobalEnable_Object = MibScalar
rlSecuritySuiteGlobalEnable = _RlSecuritySuiteGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 1),
    _RlSecuritySuiteGlobalEnable_Type()
)
rlSecuritySuiteGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteGlobalEnable.setStatus("current")
_RlSecuritySuiteKnownDoSAttacksTable_Object = MibTable
rlSecuritySuiteKnownDoSAttacksTable = _RlSecuritySuiteKnownDoSAttacksTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 2)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttacksTable.setStatus("current")
_RlSecuritySuiteKnownDoSAttacksEntry_Object = MibTableRow
rlSecuritySuiteKnownDoSAttacksEntry = _RlSecuritySuiteKnownDoSAttacksEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 2, 1)
)
rlSecuritySuiteKnownDoSAttacksEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttacksEntry.setStatus("current")
_RlSecuritySuiteKnownDoSAttack_Type = RlSecuritySuiteKnownDosAttackType
_RlSecuritySuiteKnownDoSAttack_Object = MibTableColumn
rlSecuritySuiteKnownDoSAttack = _RlSecuritySuiteKnownDoSAttack_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 2, 1, 1),
    _RlSecuritySuiteKnownDoSAttack_Type()
)
rlSecuritySuiteKnownDoSAttack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttack.setStatus("current")
_RlSecuritySuiteKnownDoSAttackEnable_Type = TruthValue
_RlSecuritySuiteKnownDoSAttackEnable_Object = MibTableColumn
rlSecuritySuiteKnownDoSAttackEnable = _RlSecuritySuiteKnownDoSAttackEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 2, 1, 2),
    _RlSecuritySuiteKnownDoSAttackEnable_Type()
)
rlSecuritySuiteKnownDoSAttackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttackEnable.setStatus("current")
_RlSecuritySuiteKnownDoSAttacksDetailsTable_Object = MibTable
rlSecuritySuiteKnownDoSAttacksDetailsTable = _RlSecuritySuiteKnownDoSAttacksDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 3)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttacksDetailsTable.setStatus("current")
_RlSecuritySuiteKnownDoSAttacksDetailsEntry_Object = MibTableRow
rlSecuritySuiteKnownDoSAttacksDetailsEntry = _RlSecuritySuiteKnownDoSAttacksDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 3, 1)
)
rlSecuritySuiteKnownDoSAttacksDetailsEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttacksDetailsEntry.setStatus("current")
_RlSecuritySuiteKnownDoSAttackProtocl_Type = RlSecuritySuiteKnownDosAttackProtocolType
_RlSecuritySuiteKnownDoSAttackProtocl_Object = MibTableColumn
rlSecuritySuiteKnownDoSAttackProtocl = _RlSecuritySuiteKnownDoSAttackProtocl_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 1),
    _RlSecuritySuiteKnownDoSAttackProtocl_Type()
)
rlSecuritySuiteKnownDoSAttackProtocl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttackProtocl.setStatus("current")
_RlSecuritySuiteKnownDoSAttackSrcTcpUdpPort_Type = Integer32
_RlSecuritySuiteKnownDoSAttackSrcTcpUdpPort_Object = MibTableColumn
rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort = _RlSecuritySuiteKnownDoSAttackSrcTcpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 2),
    _RlSecuritySuiteKnownDoSAttackSrcTcpUdpPort_Type()
)
rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setStatus("current")
_RlSecuritySuiteKnownDoSAttackDestTcpUdpPort_Type = Integer32
_RlSecuritySuiteKnownDoSAttackDestTcpUdpPort_Object = MibTableColumn
rlSecuritySuiteKnownDoSAttackDestTcpUdpPort = _RlSecuritySuiteKnownDoSAttackDestTcpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 3),
    _RlSecuritySuiteKnownDoSAttackDestTcpUdpPort_Type()
)
rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setStatus("current")
_RlSecuritySuiteReservedMartianAddresses_Type = TruthValue
_RlSecuritySuiteReservedMartianAddresses_Object = MibScalar
rlSecuritySuiteReservedMartianAddresses = _RlSecuritySuiteReservedMartianAddresses_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 4),
    _RlSecuritySuiteReservedMartianAddresses_Type()
)
rlSecuritySuiteReservedMartianAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteReservedMartianAddresses.setStatus("current")
_RlSecuritySuiteMartianAddrAllTable_Object = MibTable
rlSecuritySuiteMartianAddrAllTable = _RlSecuritySuiteMartianAddrAllTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 5)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrAllTable.setStatus("current")
_RlSecuritySuiteMartianAddrAllEntry_Object = MibTableRow
rlSecuritySuiteMartianAddrAllEntry = _RlSecuritySuiteMartianAddrAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 5, 1)
)
rlSecuritySuiteMartianAddrAllEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrAllEntry.setStatus("current")
_RlSecuritySuiteMartianAddr_Type = IpAddress
_RlSecuritySuiteMartianAddr_Object = MibTableColumn
rlSecuritySuiteMartianAddr = _RlSecuritySuiteMartianAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 1),
    _RlSecuritySuiteMartianAddr_Type()
)
rlSecuritySuiteMartianAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddr.setStatus("current")
_RlSecuritySuiteMartianAddrNetMask_Type = IpAddress
_RlSecuritySuiteMartianAddrNetMask_Object = MibTableColumn
rlSecuritySuiteMartianAddrNetMask = _RlSecuritySuiteMartianAddrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 2),
    _RlSecuritySuiteMartianAddrNetMask_Type()
)
rlSecuritySuiteMartianAddrNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrNetMask.setStatus("current")
_RlSecuritySuiteAllMartianEntryType_Type = RlSecuritySuiteAllMartianEntryType
_RlSecuritySuiteAllMartianEntryType_Object = MibTableColumn
rlSecuritySuiteAllMartianEntryType = _RlSecuritySuiteAllMartianEntryType_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 3),
    _RlSecuritySuiteAllMartianEntryType_Type()
)
rlSecuritySuiteAllMartianEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteAllMartianEntryType.setStatus("current")
_RlSecuritySuiteMartianAddrTable_Object = MibTable
rlSecuritySuiteMartianAddrTable = _RlSecuritySuiteMartianAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 6)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrTable.setStatus("current")
_RlSecuritySuiteMartianAddrEntry_Object = MibTableRow
rlSecuritySuiteMartianAddrEntry = _RlSecuritySuiteMartianAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 6, 1)
)
rlSecuritySuiteMartianAddrEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrEntry.setStatus("current")
_RlSecuritySuiteMartianAddrStatus_Type = RowStatus
_RlSecuritySuiteMartianAddrStatus_Object = MibTableColumn
rlSecuritySuiteMartianAddrStatus = _RlSecuritySuiteMartianAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 6, 1, 1),
    _RlSecuritySuiteMartianAddrStatus_Type()
)
rlSecuritySuiteMartianAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSecuritySuiteMartianAddrStatus.setStatus("current")
_RlSecuritySuiteDoSSynAttackTable_Object = MibTable
rlSecuritySuiteDoSSynAttackTable = _RlSecuritySuiteDoSSynAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackTable.setStatus("current")
_RlSecuritySuiteDoSSynAttackEntry_Object = MibTableRow
rlSecuritySuiteDoSSynAttackEntry = _RlSecuritySuiteDoSSynAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1)
)
rlSecuritySuiteDoSSynAttackEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackIfIndex"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackAddr"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackNetMask"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackEntry.setStatus("current")
_RlSecuritySuiteDoSSynAttackIfIndex_Type = InterfaceIndex
_RlSecuritySuiteDoSSynAttackIfIndex_Object = MibTableColumn
rlSecuritySuiteDoSSynAttackIfIndex = _RlSecuritySuiteDoSSynAttackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 1),
    _RlSecuritySuiteDoSSynAttackIfIndex_Type()
)
rlSecuritySuiteDoSSynAttackIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackIfIndex.setStatus("current")
_RlSecuritySuiteDoSSynAttackAddr_Type = IpAddress
_RlSecuritySuiteDoSSynAttackAddr_Object = MibTableColumn
rlSecuritySuiteDoSSynAttackAddr = _RlSecuritySuiteDoSSynAttackAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 2),
    _RlSecuritySuiteDoSSynAttackAddr_Type()
)
rlSecuritySuiteDoSSynAttackAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackAddr.setStatus("current")
_RlSecuritySuiteDoSSynAttackNetMask_Type = IpAddress
_RlSecuritySuiteDoSSynAttackNetMask_Object = MibTableColumn
rlSecuritySuiteDoSSynAttackNetMask = _RlSecuritySuiteDoSSynAttackNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 3),
    _RlSecuritySuiteDoSSynAttackNetMask_Type()
)
rlSecuritySuiteDoSSynAttackNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackNetMask.setStatus("current")
_RlSecuritySuiteDoSSynAttackSynRate_Type = Integer32
_RlSecuritySuiteDoSSynAttackSynRate_Object = MibTableColumn
rlSecuritySuiteDoSSynAttackSynRate = _RlSecuritySuiteDoSSynAttackSynRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 4),
    _RlSecuritySuiteDoSSynAttackSynRate_Type()
)
rlSecuritySuiteDoSSynAttackSynRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackSynRate.setStatus("current")
_RlSecuritySuiteDoSSynAttackStatus_Type = RowStatus
_RlSecuritySuiteDoSSynAttackStatus_Object = MibTableColumn
rlSecuritySuiteDoSSynAttackStatus = _RlSecuritySuiteDoSSynAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 6),
    _RlSecuritySuiteDoSSynAttackStatus_Type()
)
rlSecuritySuiteDoSSynAttackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSecuritySuiteDoSSynAttackStatus.setStatus("current")
_RlSecuritySuiteDenyTypesTable_Object = MibTable
rlSecuritySuiteDenyTypesTable = _RlSecuritySuiteDenyTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyTypesTable.setStatus("current")
_RlSecuritySuiteDenyTypesEntry_Object = MibTableRow
rlSecuritySuiteDenyTypesEntry = _RlSecuritySuiteDenyTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1)
)
rlSecuritySuiteDenyTypesEntry.setIndexNames(
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyIfIndex"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyAttackType"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyDestAddr"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyNetMask"),
    (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyDestPort"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyTypesEntry.setStatus("current")
_RlSecuritySuiteDenyIfIndex_Type = InterfaceIndex
_RlSecuritySuiteDenyIfIndex_Object = MibTableColumn
rlSecuritySuiteDenyIfIndex = _RlSecuritySuiteDenyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 1),
    _RlSecuritySuiteDenyIfIndex_Type()
)
rlSecuritySuiteDenyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyIfIndex.setStatus("current")
_RlSecuritySuiteDenyAttackType_Type = RlSecuritySuiteDenyAttackType
_RlSecuritySuiteDenyAttackType_Object = MibTableColumn
rlSecuritySuiteDenyAttackType = _RlSecuritySuiteDenyAttackType_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 2),
    _RlSecuritySuiteDenyAttackType_Type()
)
rlSecuritySuiteDenyAttackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyAttackType.setStatus("current")
_RlSecuritySuiteDenyDestAddr_Type = IpAddress
_RlSecuritySuiteDenyDestAddr_Object = MibTableColumn
rlSecuritySuiteDenyDestAddr = _RlSecuritySuiteDenyDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 3),
    _RlSecuritySuiteDenyDestAddr_Type()
)
rlSecuritySuiteDenyDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyDestAddr.setStatus("current")
_RlSecuritySuiteDenyNetMask_Type = IpAddress
_RlSecuritySuiteDenyNetMask_Object = MibTableColumn
rlSecuritySuiteDenyNetMask = _RlSecuritySuiteDenyNetMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 4),
    _RlSecuritySuiteDenyNetMask_Type()
)
rlSecuritySuiteDenyNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyNetMask.setStatus("current")
_RlSecuritySuiteDenyDestPort_Type = Integer32
_RlSecuritySuiteDenyDestPort_Object = MibTableColumn
rlSecuritySuiteDenyDestPort = _RlSecuritySuiteDenyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 5),
    _RlSecuritySuiteDenyDestPort_Type()
)
rlSecuritySuiteDenyDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyDestPort.setStatus("current")
_RlSecuritySuiteDenyStatus_Type = RowStatus
_RlSecuritySuiteDenyStatus_Object = MibTableColumn
rlSecuritySuiteDenyStatus = _RlSecuritySuiteDenyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 6),
    _RlSecuritySuiteDenyStatus_Type()
)
rlSecuritySuiteDenyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenyStatus.setStatus("current")
_RlSecuritySuiteDenySynFinTcp_Type = RlSecuritySuiteDenySynFinTcp
_RlSecuritySuiteDenySynFinTcp_Object = MibScalar
rlSecuritySuiteDenySynFinTcp = _RlSecuritySuiteDenySynFinTcp_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 9),
    _RlSecuritySuiteDenySynFinTcp_Type()
)
rlSecuritySuiteDenySynFinTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteDenySynFinTcp.setStatus("current")
_RlSecuritySuiteSynProtectionMode_Type = RlSecuritySuiteSynProtectionMode
_RlSecuritySuiteSynProtectionMode_Object = MibScalar
rlSecuritySuiteSynProtectionMode = _RlSecuritySuiteSynProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 10),
    _RlSecuritySuiteSynProtectionMode_Type()
)
rlSecuritySuiteSynProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionMode.setStatus("current")
_RlSecuritySuiteSynProtectionTreshold_Type = Integer32
_RlSecuritySuiteSynProtectionTreshold_Object = MibScalar
rlSecuritySuiteSynProtectionTreshold = _RlSecuritySuiteSynProtectionTreshold_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 11),
    _RlSecuritySuiteSynProtectionTreshold_Type()
)
rlSecuritySuiteSynProtectionTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionTreshold.setStatus("current")
_RlSecuritySuiteSynProtectionRecoveryTimeout_Type = Integer32
_RlSecuritySuiteSynProtectionRecoveryTimeout_Object = MibScalar
rlSecuritySuiteSynProtectionRecoveryTimeout = _RlSecuritySuiteSynProtectionRecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 12),
    _RlSecuritySuiteSynProtectionRecoveryTimeout_Type()
)
rlSecuritySuiteSynProtectionRecoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionRecoveryTimeout.setStatus("current")
_RlSecuritySuiteSynProtectionPortTable_Object = MibTable
rlSecuritySuiteSynProtectionPortTable = _RlSecuritySuiteSynProtectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 13)
)
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionPortTable.setStatus("current")
_RlSecuritySuiteSynProtectionPortEntry_Object = MibTableRow
rlSecuritySuiteSynProtectionPortEntry = _RlSecuritySuiteSynProtectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 13, 1)
)
rlSecuritySuiteSynProtectionPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionPortEntry.setStatus("current")
_RlSecuritySuiteSynProtectionPortMode_Type = RlSecuritySuiteSynProtectionPortMode
_RlSecuritySuiteSynProtectionPortMode_Object = MibTableColumn
rlSecuritySuiteSynProtectionPortMode = _RlSecuritySuiteSynProtectionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 1),
    _RlSecuritySuiteSynProtectionPortMode_Type()
)
rlSecuritySuiteSynProtectionPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionPortMode.setStatus("current")
_RlSecuritySuiteSynProtectionPortModeLastTimeAttack_Type = RlSecuritySuiteSynProtectionPortMode
_RlSecuritySuiteSynProtectionPortModeLastTimeAttack_Object = MibTableColumn
rlSecuritySuiteSynProtectionPortModeLastTimeAttack = _RlSecuritySuiteSynProtectionPortModeLastTimeAttack_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 2),
    _RlSecuritySuiteSynProtectionPortModeLastTimeAttack_Type()
)
rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setStatus("current")
_RlSecuritySuiteSynProtectionPortLastTimeAttack_Type = DisplayString
_RlSecuritySuiteSynProtectionPortLastTimeAttack_Object = MibTableColumn
rlSecuritySuiteSynProtectionPortLastTimeAttack = _RlSecuritySuiteSynProtectionPortLastTimeAttack_Object(
    (1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 3),
    _RlSecuritySuiteSynProtectionPortLastTimeAttack_Type()
)
rlSecuritySuiteSynProtectionPortLastTimeAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSecuritySuiteSynProtectionPortLastTimeAttack.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-SECURITY-SUITE",
    **{"RlsecuritySuiteGlobalEnableType": RlsecuritySuiteGlobalEnableType,
       "RlSecuritySuiteKnownDosAttackType": RlSecuritySuiteKnownDosAttackType,
       "RlSecuritySuiteKnownDosAttackProtocolType": RlSecuritySuiteKnownDosAttackProtocolType,
       "RlSecuritySuiteAllMartianEntryType": RlSecuritySuiteAllMartianEntryType,
       "RlSecuritySuiteDenyAttackType": RlSecuritySuiteDenyAttackType,
       "RlSecuritySuiteDenySynFinTcp": RlSecuritySuiteDenySynFinTcp,
       "RlSecuritySuiteSynProtectionMode": RlSecuritySuiteSynProtectionMode,
       "RlSecuritySuiteSynProtectionPortMode": RlSecuritySuiteSynProtectionPortMode,
       "rlSecuritySuiteMib": rlSecuritySuiteMib,
       "rlSecuritySuiteGlobalEnable": rlSecuritySuiteGlobalEnable,
       "rlSecuritySuiteKnownDoSAttacksTable": rlSecuritySuiteKnownDoSAttacksTable,
       "rlSecuritySuiteKnownDoSAttacksEntry": rlSecuritySuiteKnownDoSAttacksEntry,
       "rlSecuritySuiteKnownDoSAttack": rlSecuritySuiteKnownDoSAttack,
       "rlSecuritySuiteKnownDoSAttackEnable": rlSecuritySuiteKnownDoSAttackEnable,
       "rlSecuritySuiteKnownDoSAttacksDetailsTable": rlSecuritySuiteKnownDoSAttacksDetailsTable,
       "rlSecuritySuiteKnownDoSAttacksDetailsEntry": rlSecuritySuiteKnownDoSAttacksDetailsEntry,
       "rlSecuritySuiteKnownDoSAttackProtocl": rlSecuritySuiteKnownDoSAttackProtocl,
       "rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort": rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort,
       "rlSecuritySuiteKnownDoSAttackDestTcpUdpPort": rlSecuritySuiteKnownDoSAttackDestTcpUdpPort,
       "rlSecuritySuiteReservedMartianAddresses": rlSecuritySuiteReservedMartianAddresses,
       "rlSecuritySuiteMartianAddrAllTable": rlSecuritySuiteMartianAddrAllTable,
       "rlSecuritySuiteMartianAddrAllEntry": rlSecuritySuiteMartianAddrAllEntry,
       "rlSecuritySuiteMartianAddr": rlSecuritySuiteMartianAddr,
       "rlSecuritySuiteMartianAddrNetMask": rlSecuritySuiteMartianAddrNetMask,
       "rlSecuritySuiteAllMartianEntryType": rlSecuritySuiteAllMartianEntryType,
       "rlSecuritySuiteMartianAddrTable": rlSecuritySuiteMartianAddrTable,
       "rlSecuritySuiteMartianAddrEntry": rlSecuritySuiteMartianAddrEntry,
       "rlSecuritySuiteMartianAddrStatus": rlSecuritySuiteMartianAddrStatus,
       "rlSecuritySuiteDoSSynAttackTable": rlSecuritySuiteDoSSynAttackTable,
       "rlSecuritySuiteDoSSynAttackEntry": rlSecuritySuiteDoSSynAttackEntry,
       "rlSecuritySuiteDoSSynAttackIfIndex": rlSecuritySuiteDoSSynAttackIfIndex,
       "rlSecuritySuiteDoSSynAttackAddr": rlSecuritySuiteDoSSynAttackAddr,
       "rlSecuritySuiteDoSSynAttackNetMask": rlSecuritySuiteDoSSynAttackNetMask,
       "rlSecuritySuiteDoSSynAttackSynRate": rlSecuritySuiteDoSSynAttackSynRate,
       "rlSecuritySuiteDoSSynAttackStatus": rlSecuritySuiteDoSSynAttackStatus,
       "rlSecuritySuiteDenyTypesTable": rlSecuritySuiteDenyTypesTable,
       "rlSecuritySuiteDenyTypesEntry": rlSecuritySuiteDenyTypesEntry,
       "rlSecuritySuiteDenyIfIndex": rlSecuritySuiteDenyIfIndex,
       "rlSecuritySuiteDenyAttackType": rlSecuritySuiteDenyAttackType,
       "rlSecuritySuiteDenyDestAddr": rlSecuritySuiteDenyDestAddr,
       "rlSecuritySuiteDenyNetMask": rlSecuritySuiteDenyNetMask,
       "rlSecuritySuiteDenyDestPort": rlSecuritySuiteDenyDestPort,
       "rlSecuritySuiteDenyStatus": rlSecuritySuiteDenyStatus,
       "rlSecuritySuiteDenySynFinTcp": rlSecuritySuiteDenySynFinTcp,
       "rlSecuritySuiteSynProtectionMode": rlSecuritySuiteSynProtectionMode,
       "rlSecuritySuiteSynProtectionTreshold": rlSecuritySuiteSynProtectionTreshold,
       "rlSecuritySuiteSynProtectionRecoveryTimeout": rlSecuritySuiteSynProtectionRecoveryTimeout,
       "rlSecuritySuiteSynProtectionPortTable": rlSecuritySuiteSynProtectionPortTable,
       "rlSecuritySuiteSynProtectionPortEntry": rlSecuritySuiteSynProtectionPortEntry,
       "rlSecuritySuiteSynProtectionPortMode": rlSecuritySuiteSynProtectionPortMode,
       "rlSecuritySuiteSynProtectionPortModeLastTimeAttack": rlSecuritySuiteSynProtectionPortModeLastTimeAttack,
       "rlSecuritySuiteSynProtectionPortLastTimeAttack": rlSecuritySuiteSynProtectionPortLastTimeAttack}
)
