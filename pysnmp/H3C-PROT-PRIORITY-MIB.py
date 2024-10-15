# SNMP MIB module (H3C-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PROT-PRIORITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:11 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37)
)
h3cProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
h3cProtocolPriorityObjects = _H3cProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1)
)
_H3cPPri_ObjectIdentity = ObjectIdentity
h3cPPri = _H3cPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1)
)
_H3cProtocolPriorityTable_Object = MibTable
h3cProtocolPriorityTable = _H3cProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cProtocolPriorityTable.setStatus("current")
_H3cProtocolPriorityEntry_Object = MibTableRow
h3cProtocolPriorityEntry = _H3cProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1)
)
h3cProtocolPriorityEntry.setIndexNames(
    (0, "H3C-PROT-PRIORITY-MIB", "h3cPPriProtocolType"),
)
if mibBuilder.loadTexts:
    h3cProtocolPriorityEntry.setStatus("current")


class _H3cPPriProtocolType_Type(Integer32):
    """Custom type h3cPPriProtocolType based on Integer32"""
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


_H3cPPriProtocolType_Type.__name__ = "Integer32"
_H3cPPriProtocolType_Object = MibTableColumn
h3cPPriProtocolType = _H3cPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 1),
    _H3cPPriProtocolType_Type()
)
h3cPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPPriProtocolType.setStatus("current")


class _H3cPPriPriorityType_Type(Integer32):
    """Custom type h3cPPriPriorityType based on Integer32"""
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


_H3cPPriPriorityType_Type.__name__ = "Integer32"
_H3cPPriPriorityType_Object = MibTableColumn
h3cPPriPriorityType = _H3cPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 2),
    _H3cPPriPriorityType_Type()
)
h3cPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriPriorityType.setStatus("current")


class _H3cPPriPriorityVlaue_Type(Integer32):
    """Custom type h3cPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cPPriPriorityVlaue_Type.__name__ = "Integer32"
_H3cPPriPriorityVlaue_Object = MibTableColumn
h3cPPriPriorityVlaue = _H3cPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 3),
    _H3cPPriPriorityVlaue_Type()
)
h3cPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriPriorityVlaue.setStatus("current")
_H3cPPriRowStatus_Type = RowStatus
_H3cPPriRowStatus_Object = MibTableColumn
h3cPPriRowStatus = _H3cPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 37, 1, 1, 1, 1, 4),
    _H3cPPriRowStatus_Type()
)
h3cPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PROT-PRIORITY-MIB",
    **{"h3cProtocolPriority": h3cProtocolPriority,
       "h3cProtocolPriorityObjects": h3cProtocolPriorityObjects,
       "h3cPPri": h3cPPri,
       "h3cProtocolPriorityTable": h3cProtocolPriorityTable,
       "h3cProtocolPriorityEntry": h3cProtocolPriorityEntry,
       "h3cPPriProtocolType": h3cPPriProtocolType,
       "h3cPPriPriorityType": h3cPPriPriorityType,
       "h3cPPriPriorityVlaue": h3cPPriPriorityVlaue,
       "h3cPPriRowStatus": h3cPPriRowStatus}
)
