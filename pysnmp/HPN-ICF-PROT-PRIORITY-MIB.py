# SNMP MIB module (HPN-ICF-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PROT-PRIORITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:33 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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


# MODULE-IDENTITY

hpnicfProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37)
)
hpnicfProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
hpnicfProtocolPriorityObjects = _HpnicfProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1)
)
_HpnicfPPri_ObjectIdentity = ObjectIdentity
hpnicfPPri = _HpnicfPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1)
)
_HpnicfProtocolPriorityTable_Object = MibTable
hpnicfProtocolPriorityTable = _HpnicfProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfProtocolPriorityTable.setStatus("current")
_HpnicfProtocolPriorityEntry_Object = MibTableRow
hpnicfProtocolPriorityEntry = _HpnicfProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1)
)
hpnicfProtocolPriorityEntry.setIndexNames(
    (0, "HPN-ICF-PROT-PRIORITY-MIB", "hpnicfPPriProtocolType"),
)
if mibBuilder.loadTexts:
    hpnicfProtocolPriorityEntry.setStatus("current")


class _HpnicfPPriProtocolType_Type(Integer32):
    """Custom type hpnicfPPriProtocolType based on Integer32"""
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
        *(("bgp", 5),
          ("icmp", 4),
          ("ldp", 6),
          ("ospf", 1),
          ("snmp", 3),
          ("telnet", 2))
    )


_HpnicfPPriProtocolType_Type.__name__ = "Integer32"
_HpnicfPPriProtocolType_Object = MibTableColumn
hpnicfPPriProtocolType = _HpnicfPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 1),
    _HpnicfPPriProtocolType_Type()
)
hpnicfPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPPriProtocolType.setStatus("current")


class _HpnicfPPriPriorityType_Type(Integer32):
    """Custom type hpnicfPPriPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("ipPrecedence", 1))
    )


_HpnicfPPriPriorityType_Type.__name__ = "Integer32"
_HpnicfPPriPriorityType_Object = MibTableColumn
hpnicfPPriPriorityType = _HpnicfPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 2),
    _HpnicfPPriPriorityType_Type()
)
hpnicfPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriPriorityType.setStatus("current")


class _HpnicfPPriPriorityVlaue_Type(Integer32):
    """Custom type hpnicfPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfPPriPriorityVlaue_Type.__name__ = "Integer32"
_HpnicfPPriPriorityVlaue_Object = MibTableColumn
hpnicfPPriPriorityVlaue = _HpnicfPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 3),
    _HpnicfPPriPriorityVlaue_Type()
)
hpnicfPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriPriorityVlaue.setStatus("current")
_HpnicfPPriRowStatus_Type = RowStatus
_HpnicfPPriRowStatus_Object = MibTableColumn
hpnicfPPriRowStatus = _HpnicfPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 37, 1, 1, 1, 1, 4),
    _HpnicfPPriRowStatus_Type()
)
hpnicfPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PROT-PRIORITY-MIB",
    **{"hpnicfProtocolPriority": hpnicfProtocolPriority,
       "hpnicfProtocolPriorityObjects": hpnicfProtocolPriorityObjects,
       "hpnicfPPri": hpnicfPPri,
       "hpnicfProtocolPriorityTable": hpnicfProtocolPriorityTable,
       "hpnicfProtocolPriorityEntry": hpnicfProtocolPriorityEntry,
       "hpnicfPPriProtocolType": hpnicfPPriProtocolType,
       "hpnicfPPriPriorityType": hpnicfPPriPriorityType,
       "hpnicfPPriPriorityVlaue": hpnicfPPriPriorityVlaue,
       "hpnicfPPriRowStatus": hpnicfPPriRowStatus}
)
