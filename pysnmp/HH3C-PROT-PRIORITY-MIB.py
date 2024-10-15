# SNMP MIB module (HH3C-PROT-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PROT-PRIORITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:34 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cProtocolPriority = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37)
)
hh3cProtocolPriority.setRevisions(
        ("2005-01-17 16:33",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cProtocolPriorityObjects_ObjectIdentity = ObjectIdentity
hh3cProtocolPriorityObjects = _Hh3cProtocolPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1)
)
_Hh3cPPri_ObjectIdentity = ObjectIdentity
hh3cPPri = _Hh3cPPri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1)
)
_Hh3cProtocolPriorityTable_Object = MibTable
hh3cProtocolPriorityTable = _Hh3cProtocolPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cProtocolPriorityTable.setStatus("current")
_Hh3cProtocolPriorityEntry_Object = MibTableRow
hh3cProtocolPriorityEntry = _Hh3cProtocolPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1)
)
hh3cProtocolPriorityEntry.setIndexNames(
    (0, "HH3C-PROT-PRIORITY-MIB", "hh3cPPriProtocolType"),
)
if mibBuilder.loadTexts:
    hh3cProtocolPriorityEntry.setStatus("current")


class _Hh3cPPriProtocolType_Type(Integer32):
    """Custom type hh3cPPriProtocolType based on Integer32"""
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


_Hh3cPPriProtocolType_Type.__name__ = "Integer32"
_Hh3cPPriProtocolType_Object = MibTableColumn
hh3cPPriProtocolType = _Hh3cPPriProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 1),
    _Hh3cPPriProtocolType_Type()
)
hh3cPPriProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPPriProtocolType.setStatus("current")


class _Hh3cPPriPriorityType_Type(Integer32):
    """Custom type hh3cPPriPriorityType based on Integer32"""
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


_Hh3cPPriPriorityType_Type.__name__ = "Integer32"
_Hh3cPPriPriorityType_Object = MibTableColumn
hh3cPPriPriorityType = _Hh3cPPriPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 2),
    _Hh3cPPriPriorityType_Type()
)
hh3cPPriPriorityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriPriorityType.setStatus("current")


class _Hh3cPPriPriorityVlaue_Type(Integer32):
    """Custom type hh3cPPriPriorityVlaue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cPPriPriorityVlaue_Type.__name__ = "Integer32"
_Hh3cPPriPriorityVlaue_Object = MibTableColumn
hh3cPPriPriorityVlaue = _Hh3cPPriPriorityVlaue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 3),
    _Hh3cPPriPriorityVlaue_Type()
)
hh3cPPriPriorityVlaue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriPriorityVlaue.setStatus("current")
_Hh3cPPriRowStatus_Type = RowStatus
_Hh3cPPriRowStatus_Object = MibTableColumn
hh3cPPriRowStatus = _Hh3cPPriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 37, 1, 1, 1, 1, 4),
    _Hh3cPPriRowStatus_Type()
)
hh3cPPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPPriRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PROT-PRIORITY-MIB",
    **{"hh3cProtocolPriority": hh3cProtocolPriority,
       "hh3cProtocolPriorityObjects": hh3cProtocolPriorityObjects,
       "hh3cPPri": hh3cPPri,
       "hh3cProtocolPriorityTable": hh3cProtocolPriorityTable,
       "hh3cProtocolPriorityEntry": hh3cProtocolPriorityEntry,
       "hh3cPPriProtocolType": hh3cPPriProtocolType,
       "hh3cPPriPriorityType": hh3cPPriPriorityType,
       "hh3cPPriPriorityVlaue": hh3cPPriPriorityVlaue,
       "hh3cPPriRowStatus": hh3cPPriRowStatus}
)
