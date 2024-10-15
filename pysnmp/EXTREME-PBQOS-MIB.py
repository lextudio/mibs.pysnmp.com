# SNMP MIB module (EXTREME-PBQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(L4Port,
 PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "L4Port",
    "PortList",
    "extremeAgent")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeQosPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeNextAvailableQosRuleIndex_Type = Integer32
_ExtremeNextAvailableQosRuleIndex_Object = MibScalar
extremeNextAvailableQosRuleIndex = _ExtremeNextAvailableQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 1),
    _ExtremeNextAvailableQosRuleIndex_Type()
)
extremeNextAvailableQosRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNextAvailableQosRuleIndex.setStatus("current")
_ExtremeQosRuleTable_Object = MibTable
extremeQosRuleTable = _ExtremeQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2)
)
if mibBuilder.loadTexts:
    extremeQosRuleTable.setStatus("current")
_ExtremeQosRuleEntry_Object = MibTableRow
extremeQosRuleEntry = _ExtremeQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1)
)
extremeQosRuleEntry.setIndexNames(
    (0, "EXTREME-PBQOS-MIB", "extremeQosRuleIndex"),
)
if mibBuilder.loadTexts:
    extremeQosRuleEntry.setStatus("current")
_ExtremeQosRuleIndex_Type = Integer32
_ExtremeQosRuleIndex_Object = MibTableColumn
extremeQosRuleIndex = _ExtremeQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 1),
    _ExtremeQosRuleIndex_Type()
)
extremeQosRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleIndex.setStatus("current")


class _ExtremeQosRuleScope_Type(Integer32):
    """Custom type extremeQosRuleScope based on Integer32"""
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
        *(("any", 1),
          ("inband", 3),
          ("signaled", 2))
    )


_ExtremeQosRuleScope_Type.__name__ = "Integer32"
_ExtremeQosRuleScope_Object = MibTableColumn
extremeQosRuleScope = _ExtremeQosRuleScope_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 2),
    _ExtremeQosRuleScope_Type()
)
extremeQosRuleScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleScope.setStatus("current")


class _ExtremeQosRuleDirection_Type(Integer32):
    """Custom type extremeQosRuleDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("backward", 3),
          ("forward", 2))
    )


_ExtremeQosRuleDirection_Type.__name__ = "Integer32"
_ExtremeQosRuleDirection_Object = MibTableColumn
extremeQosRuleDirection = _ExtremeQosRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 3),
    _ExtremeQosRuleDirection_Type()
)
extremeQosRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleDirection.setStatus("current")


class _ExtremeQosRuleInPort_Type(Integer32):
    """Custom type extremeQosRuleInPort based on Integer32"""
    defaultValue = 0


_ExtremeQosRuleInPort_Object = MibTableColumn
extremeQosRuleInPort = _ExtremeQosRuleInPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 4),
    _ExtremeQosRuleInPort_Type()
)
extremeQosRuleInPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleInPort.setStatus("current")
_ExtremeQosRuleInPortMask_Type = PortList
_ExtremeQosRuleInPortMask_Object = MibTableColumn
extremeQosRuleInPortMask = _ExtremeQosRuleInPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 5),
    _ExtremeQosRuleInPortMask_Type()
)
extremeQosRuleInPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleInPortMask.setStatus("current")


class _ExtremeQosRuleDestAddrStart_Type(IpAddress):
    """Custom type extremeQosRuleDestAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_ExtremeQosRuleDestAddrStart_Object = MibTableColumn
extremeQosRuleDestAddrStart = _ExtremeQosRuleDestAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 6),
    _ExtremeQosRuleDestAddrStart_Type()
)
extremeQosRuleDestAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleDestAddrStart.setStatus("current")


class _ExtremeQosRuleDestAddrEnd_Type(IpAddress):
    """Custom type extremeQosRuleDestAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_ExtremeQosRuleDestAddrEnd_Object = MibTableColumn
extremeQosRuleDestAddrEnd = _ExtremeQosRuleDestAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 7),
    _ExtremeQosRuleDestAddrEnd_Type()
)
extremeQosRuleDestAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleDestAddrEnd.setStatus("current")


class _ExtremeQosRuleSrcAddrStart_Type(IpAddress):
    """Custom type extremeQosRuleSrcAddrStart based on IpAddress"""
    defaultHexValue = "00000000"


_ExtremeQosRuleSrcAddrStart_Object = MibTableColumn
extremeQosRuleSrcAddrStart = _ExtremeQosRuleSrcAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 8),
    _ExtremeQosRuleSrcAddrStart_Type()
)
extremeQosRuleSrcAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleSrcAddrStart.setStatus("current")


class _ExtremeQosRuleSrcAddrEnd_Type(IpAddress):
    """Custom type extremeQosRuleSrcAddrEnd based on IpAddress"""
    defaultHexValue = "ffffffff"


_ExtremeQosRuleSrcAddrEnd_Object = MibTableColumn
extremeQosRuleSrcAddrEnd = _ExtremeQosRuleSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 9),
    _ExtremeQosRuleSrcAddrEnd_Type()
)
extremeQosRuleSrcAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleSrcAddrEnd.setStatus("current")


class _ExtremeQosRuleProtocol_Type(Integer32):
    """Custom type extremeQosRuleProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("icmp", 6),
          ("other", 4),
          ("tcp", 3),
          ("tcpPermitEstablished", 5),
          ("udp", 2))
    )


_ExtremeQosRuleProtocol_Type.__name__ = "Integer32"
_ExtremeQosRuleProtocol_Object = MibTableColumn
extremeQosRuleProtocol = _ExtremeQosRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 10),
    _ExtremeQosRuleProtocol_Type()
)
extremeQosRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleProtocol.setStatus("current")


class _ExtremeQosRuleDestL4PortStart_Type(L4Port):
    """Custom type extremeQosRuleDestL4PortStart based on L4Port"""
    defaultValue = 0


_ExtremeQosRuleDestL4PortStart_Object = MibTableColumn
extremeQosRuleDestL4PortStart = _ExtremeQosRuleDestL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 11),
    _ExtremeQosRuleDestL4PortStart_Type()
)
extremeQosRuleDestL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleDestL4PortStart.setStatus("current")


class _ExtremeQosRuleSourceL4PortStart_Type(L4Port):
    """Custom type extremeQosRuleSourceL4PortStart based on L4Port"""
    defaultValue = 0


_ExtremeQosRuleSourceL4PortStart_Object = MibTableColumn
extremeQosRuleSourceL4PortStart = _ExtremeQosRuleSourceL4PortStart_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 12),
    _ExtremeQosRuleSourceL4PortStart_Type()
)
extremeQosRuleSourceL4PortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleSourceL4PortStart.setStatus("current")


class _ExtremeQosRuleTosMask_Type(OctetString):
    """Custom type extremeQosRuleTosMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeQosRuleTosMask_Type.__name__ = "OctetString"
_ExtremeQosRuleTosMask_Object = MibTableColumn
extremeQosRuleTosMask = _ExtremeQosRuleTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 13),
    _ExtremeQosRuleTosMask_Type()
)
extremeQosRuleTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleTosMask.setStatus("deprecated")


class _ExtremeQosRuleTosMatch_Type(OctetString):
    """Custom type extremeQosRuleTosMatch based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ExtremeQosRuleTosMatch_Type.__name__ = "OctetString"
_ExtremeQosRuleTosMatch_Object = MibTableColumn
extremeQosRuleTosMatch = _ExtremeQosRuleTosMatch_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 14),
    _ExtremeQosRuleTosMatch_Type()
)
extremeQosRuleTosMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleTosMatch.setStatus("deprecated")


class _ExtremeQosRuleQosProfileIndex_Type(Integer32):
    """Custom type extremeQosRuleQosProfileIndex based on Integer32"""
    defaultValue = 1


_ExtremeQosRuleQosProfileIndex_Object = MibTableColumn
extremeQosRuleQosProfileIndex = _ExtremeQosRuleQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 15),
    _ExtremeQosRuleQosProfileIndex_Type()
)
extremeQosRuleQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleQosProfileIndex.setStatus("current")


class _ExtremeQosRuleOwner_Type(OwnerString):
    """Custom type extremeQosRuleOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeQosRuleOwner_Type.__name__ = "OwnerString"
_ExtremeQosRuleOwner_Object = MibTableColumn
extremeQosRuleOwner = _ExtremeQosRuleOwner_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 16),
    _ExtremeQosRuleOwner_Type()
)
extremeQosRuleOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleOwner.setStatus("current")
_ExtremeQosRuleRowStatus_Type = RowStatus
_ExtremeQosRuleRowStatus_Object = MibTableColumn
extremeQosRuleRowStatus = _ExtremeQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 17),
    _ExtremeQosRuleRowStatus_Type()
)
extremeQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleRowStatus.setStatus("current")


class _ExtremeQosRuleDestL4PortEnd_Type(L4Port):
    """Custom type extremeQosRuleDestL4PortEnd based on L4Port"""
    defaultValue = 0


_ExtremeQosRuleDestL4PortEnd_Object = MibTableColumn
extremeQosRuleDestL4PortEnd = _ExtremeQosRuleDestL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 18),
    _ExtremeQosRuleDestL4PortEnd_Type()
)
extremeQosRuleDestL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleDestL4PortEnd.setStatus("current")


class _ExtremeQosRuleSourceL4PortEnd_Type(L4Port):
    """Custom type extremeQosRuleSourceL4PortEnd based on L4Port"""
    defaultValue = 0


_ExtremeQosRuleSourceL4PortEnd_Object = MibTableColumn
extremeQosRuleSourceL4PortEnd = _ExtremeQosRuleSourceL4PortEnd_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 19),
    _ExtremeQosRuleSourceL4PortEnd_Type()
)
extremeQosRuleSourceL4PortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleSourceL4PortEnd.setStatus("current")


class _ExtremeQosRulePrecedence_Type(Integer32):
    """Custom type extremeQosRulePrecedence based on Integer32"""
    defaultValue = 0


_ExtremeQosRulePrecedence_Object = MibTableColumn
extremeQosRulePrecedence = _ExtremeQosRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 20),
    _ExtremeQosRulePrecedence_Type()
)
extremeQosRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRulePrecedence.setStatus("current")


class _ExtremeQosRuleCounter_Type(Counter64):
    """Custom type extremeQosRuleCounter based on Counter64"""
    defaultValue = 0


_ExtremeQosRuleCounter_Object = MibTableColumn
extremeQosRuleCounter = _ExtremeQosRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 21),
    _ExtremeQosRuleCounter_Type()
)
extremeQosRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosRuleCounter.setStatus("current")


class _ExtremeQosRuleName_Type(DisplayString):
    """Custom type extremeQosRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeQosRuleName_Type.__name__ = "DisplayString"
_ExtremeQosRuleName_Object = MibTableColumn
extremeQosRuleName = _ExtremeQosRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 2, 1, 22),
    _ExtremeQosRuleName_Type()
)
extremeQosRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeQosRuleName.setStatus("current")
_ExtremeQosCapabilitiesTable_Object = MibTable
extremeQosCapabilitiesTable = _ExtremeQosCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 3)
)
if mibBuilder.loadTexts:
    extremeQosCapabilitiesTable.setStatus("current")
_ExtremeQosCapabilitiesEntry_Object = MibTableRow
extremeQosCapabilitiesEntry = _ExtremeQosCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    extremeQosCapabilitiesEntry.setStatus("current")
_ExtremeQosCapMarkIpTosCapable_Type = TruthValue
_ExtremeQosCapMarkIpTosCapable_Object = MibTableColumn
extremeQosCapMarkIpTosCapable = _ExtremeQosCapMarkIpTosCapable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 3, 1, 1),
    _ExtremeQosCapMarkIpTosCapable_Type()
)
extremeQosCapMarkIpTosCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosCapMarkIpTosCapable.setStatus("current")
_ExtremeQosCapMatchIpTosCapable_Type = TruthValue
_ExtremeQosCapMatchIpTosCapable_Object = MibTableColumn
extremeQosCapMatchIpTosCapable = _ExtremeQosCapMatchIpTosCapable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 3, 1, 2),
    _ExtremeQosCapMatchIpTosCapable_Type()
)
extremeQosCapMatchIpTosCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeQosCapMatchIpTosCapable.setStatus("current")
_ExtremeQosClearIPFdb_Type = TruthValue
_ExtremeQosClearIPFdb_Object = MibScalar
extremeQosClearIPFdb = _ExtremeQosClearIPFdb_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 4),
    _ExtremeQosClearIPFdb_Type()
)
extremeQosClearIPFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeQosClearIPFdb.setStatus("current")
_ExtremeQosClearFdb_Type = TruthValue
_ExtremeQosClearFdb_Object = MibScalar
extremeQosClearFdb = _ExtremeQosClearFdb_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 7, 5),
    _ExtremeQosClearFdb_Type()
)
extremeQosClearFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeQosClearFdb.setStatus("current")
ifEntry.registerAugmentions(
    ("EXTREME-PBQOS-MIB",
     "extremeQosCapabilitiesEntry")
)
extremeQosCapabilitiesEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-PBQOS-MIB",
    **{"extremeQosPolicy": extremeQosPolicy,
       "extremeNextAvailableQosRuleIndex": extremeNextAvailableQosRuleIndex,
       "extremeQosRuleTable": extremeQosRuleTable,
       "extremeQosRuleEntry": extremeQosRuleEntry,
       "extremeQosRuleIndex": extremeQosRuleIndex,
       "extremeQosRuleScope": extremeQosRuleScope,
       "extremeQosRuleDirection": extremeQosRuleDirection,
       "extremeQosRuleInPort": extremeQosRuleInPort,
       "extremeQosRuleInPortMask": extremeQosRuleInPortMask,
       "extremeQosRuleDestAddrStart": extremeQosRuleDestAddrStart,
       "extremeQosRuleDestAddrEnd": extremeQosRuleDestAddrEnd,
       "extremeQosRuleSrcAddrStart": extremeQosRuleSrcAddrStart,
       "extremeQosRuleSrcAddrEnd": extremeQosRuleSrcAddrEnd,
       "extremeQosRuleProtocol": extremeQosRuleProtocol,
       "extremeQosRuleDestL4PortStart": extremeQosRuleDestL4PortStart,
       "extremeQosRuleSourceL4PortStart": extremeQosRuleSourceL4PortStart,
       "extremeQosRuleTosMask": extremeQosRuleTosMask,
       "extremeQosRuleTosMatch": extremeQosRuleTosMatch,
       "extremeQosRuleQosProfileIndex": extremeQosRuleQosProfileIndex,
       "extremeQosRuleOwner": extremeQosRuleOwner,
       "extremeQosRuleRowStatus": extremeQosRuleRowStatus,
       "extremeQosRuleDestL4PortEnd": extremeQosRuleDestL4PortEnd,
       "extremeQosRuleSourceL4PortEnd": extremeQosRuleSourceL4PortEnd,
       "extremeQosRulePrecedence": extremeQosRulePrecedence,
       "extremeQosRuleCounter": extremeQosRuleCounter,
       "extremeQosRuleName": extremeQosRuleName,
       "extremeQosCapabilitiesTable": extremeQosCapabilitiesTable,
       "extremeQosCapabilitiesEntry": extremeQosCapabilitiesEntry,
       "extremeQosCapMarkIpTosCapable": extremeQosCapMarkIpTosCapable,
       "extremeQosCapMatchIpTosCapable": extremeQosCapMatchIpTosCapable,
       "extremeQosClearIPFdb": extremeQosClearIPFdb,
       "extremeQosClearFdb": extremeQosClearFdb}
)
