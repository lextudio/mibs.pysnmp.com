# SNMP MIB module (ATM-DXI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-DXI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:48 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Dfa(Integer32):
    """Custom type Dfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmUniDxi_ObjectIdentity = ObjectIdentity
atmUniDxi = _AtmUniDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 3)
)
_AtmDxi_ObjectIdentity = ObjectIdentity
atmDxi = _AtmDxi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 3, 2)
)
_AtmDxiConfTable_Object = MibTable
atmDxiConfTable = _AtmDxiConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 2)
)
if mibBuilder.loadTexts:
    atmDxiConfTable.setStatus("mandatory")
_AtmDxiConfEntry_Object = MibTableRow
atmDxiConfEntry = _AtmDxiConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1)
)
atmDxiConfEntry.setIndexNames(
    (0, "ATM-DXI-MIB", "atmDxiConfIfIndex"),
)
if mibBuilder.loadTexts:
    atmDxiConfEntry.setStatus("mandatory")
_AtmDxiConfIfIndex_Type = Integer32
_AtmDxiConfIfIndex_Object = MibTableColumn
atmDxiConfIfIndex = _AtmDxiConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 2),
    _AtmDxiConfIfIndex_Type()
)
atmDxiConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiConfIfIndex.setStatus("mandatory")


class _AtmDxiConfMode_Type(Integer32):
    """Custom type atmDxiConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode2", 3))
    )


_AtmDxiConfMode_Type.__name__ = "Integer32"
_AtmDxiConfMode_Object = MibTableColumn
atmDxiConfMode = _AtmDxiConfMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 2, 1, 3),
    _AtmDxiConfMode_Type()
)
atmDxiConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiConfMode.setStatus("mandatory")
_AtmDxiDFAConfTable_Object = MibTable
atmDxiDFAConfTable = _AtmDxiDFAConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 3)
)
if mibBuilder.loadTexts:
    atmDxiDFAConfTable.setStatus("mandatory")
_AtmDxiDFAConfEntry_Object = MibTableRow
atmDxiDFAConfEntry = _AtmDxiDFAConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1)
)
atmDxiDFAConfEntry.setIndexNames(
    (0, "ATM-DXI-MIB", "atmDxiDFAConfIfIndex"),
    (0, "ATM-DXI-MIB", "atmDxiDFAConfDfaIndex"),
)
if mibBuilder.loadTexts:
    atmDxiDFAConfEntry.setStatus("mandatory")
_AtmDxiDFAConfIfIndex_Type = Integer32
_AtmDxiDFAConfIfIndex_Object = MibTableColumn
atmDxiDFAConfIfIndex = _AtmDxiDFAConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 1),
    _AtmDxiDFAConfIfIndex_Type()
)
atmDxiDFAConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiDFAConfIfIndex.setStatus("mandatory")
_AtmDxiDFAConfDfaIndex_Type = Dfa
_AtmDxiDFAConfDfaIndex_Object = MibTableColumn
atmDxiDFAConfDfaIndex = _AtmDxiDFAConfDfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 2),
    _AtmDxiDFAConfDfaIndex_Type()
)
atmDxiDFAConfDfaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiDFAConfDfaIndex.setStatus("mandatory")


class _AtmDxiDFAConfAALType_Type(Integer32):
    """Custom type atmDxiDFAConfAALType based on Integer32"""
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
        *(("aal34", 3),
          ("aal5", 4),
          ("none", 2),
          ("unknown", 1))
    )


_AtmDxiDFAConfAALType_Type.__name__ = "Integer32"
_AtmDxiDFAConfAALType_Object = MibTableColumn
atmDxiDFAConfAALType = _AtmDxiDFAConfAALType_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 3, 1, 3),
    _AtmDxiDFAConfAALType_Type()
)
atmDxiDFAConfAALType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiDFAConfAALType.setStatus("mandatory")
_AtmDxiEnterprise_Type = ObjectIdentifier
_AtmDxiEnterprise_Object = MibScalar
atmDxiEnterprise = _AtmDxiEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 353, 3, 2, 4),
    _AtmDxiEnterprise_Type()
)
atmDxiEnterprise.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmDxiEnterprise.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-DXI-MIB",
    **{"Dfa": Dfa,
       "atmForum": atmForum,
       "atmUniDxi": atmUniDxi,
       "atmDxi": atmDxi,
       "atmDxiConfTable": atmDxiConfTable,
       "atmDxiConfEntry": atmDxiConfEntry,
       "atmDxiConfIfIndex": atmDxiConfIfIndex,
       "atmDxiConfMode": atmDxiConfMode,
       "atmDxiDFAConfTable": atmDxiDFAConfTable,
       "atmDxiDFAConfEntry": atmDxiDFAConfEntry,
       "atmDxiDFAConfIfIndex": atmDxiDFAConfIfIndex,
       "atmDxiDFAConfDfaIndex": atmDxiDFAConfDfaIndex,
       "atmDxiDFAConfAALType": atmDxiDFAConfAALType,
       "atmDxiEnterprise": atmDxiEnterprise}
)
