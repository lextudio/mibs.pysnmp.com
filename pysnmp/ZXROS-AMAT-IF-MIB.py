# SNMP MIB module (ZXROS-AMAT-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXROS-AMAT-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:14 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxros_ObjectIdentity = ObjectIdentity
zxros = _Zxros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 100)
)
_ZxrosAMATIF_ObjectIdentity = ObjectIdentity
zxrosAMATIF = _ZxrosAMATIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001)
)
_ZxrosAMATInterfaceEnableTable_Object = MibTable
zxrosAMATInterfaceEnableTable = _ZxrosAMATInterfaceEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1)
)
if mibBuilder.loadTexts:
    zxrosAMATInterfaceEnableTable.setStatus("current")
_ZxrosAMATInterfaceEnableEntry_Object = MibTableRow
zxrosAMATInterfaceEnableEntry = _ZxrosAMATInterfaceEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1)
)
zxrosAMATInterfaceEnableEntry.setIndexNames(
    (0, "ZXROS-AMAT-IF-MIB", "zxrosAMATInterfaceEnableIfIndex"),
)
if mibBuilder.loadTexts:
    zxrosAMATInterfaceEnableEntry.setStatus("current")
_ZxrosAMATInterfaceEnableIfIndex_Type = Integer32
_ZxrosAMATInterfaceEnableIfIndex_Object = MibTableColumn
zxrosAMATInterfaceEnableIfIndex = _ZxrosAMATInterfaceEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 1),
    _ZxrosAMATInterfaceEnableIfIndex_Type()
)
zxrosAMATInterfaceEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATInterfaceEnableIfIndex.setStatus("current")


class _ZxrosAMATInterfaceInAmatEnable_Type(Integer32):
    """Custom type zxrosAMATInterfaceInAmatEnable based on Integer32"""
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


_ZxrosAMATInterfaceInAmatEnable_Type.__name__ = "Integer32"
_ZxrosAMATInterfaceInAmatEnable_Object = MibTableColumn
zxrosAMATInterfaceInAmatEnable = _ZxrosAMATInterfaceInAmatEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 2),
    _ZxrosAMATInterfaceInAmatEnable_Type()
)
zxrosAMATInterfaceInAmatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATInterfaceInAmatEnable.setStatus("current")


class _ZxrosAMATInterfaceOutAmatEnable_Type(Integer32):
    """Custom type zxrosAMATInterfaceOutAmatEnable based on Integer32"""
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


_ZxrosAMATInterfaceOutAmatEnable_Type.__name__ = "Integer32"
_ZxrosAMATInterfaceOutAmatEnable_Object = MibTableColumn
zxrosAMATInterfaceOutAmatEnable = _ZxrosAMATInterfaceOutAmatEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 3),
    _ZxrosAMATInterfaceOutAmatEnable_Type()
)
zxrosAMATInterfaceOutAmatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxrosAMATInterfaceOutAmatEnable.setStatus("current")
_ZxrosAMATInterfaceStatisticTable_Object = MibTable
zxrosAMATInterfaceStatisticTable = _ZxrosAMATInterfaceStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2)
)
if mibBuilder.loadTexts:
    zxrosAMATInterfaceStatisticTable.setStatus("current")
_ZxrosAMATInterfaceStatisticEntry_Object = MibTableRow
zxrosAMATInterfaceStatisticEntry = _ZxrosAMATInterfaceStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1)
)
zxrosAMATInterfaceStatisticEntry.setIndexNames(
    (0, "ZXROS-AMAT-IF-MIB", "zxrosAMATInterfaceStatisticIfIndex"),
)
if mibBuilder.loadTexts:
    zxrosAMATInterfaceStatisticEntry.setStatus("current")
_ZxrosAMATInterfaceStatisticIfIndex_Type = Integer32
_ZxrosAMATInterfaceStatisticIfIndex_Object = MibTableColumn
zxrosAMATInterfaceStatisticIfIndex = _ZxrosAMATInterfaceStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 1),
    _ZxrosAMATInterfaceStatisticIfIndex_Type()
)
zxrosAMATInterfaceStatisticIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATInterfaceStatisticIfIndex.setStatus("current")
_ZxrosAMATInFilterpackets_Type = Counter64
_ZxrosAMATInFilterpackets_Object = MibTableColumn
zxrosAMATInFilterpackets = _ZxrosAMATInFilterpackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 2),
    _ZxrosAMATInFilterpackets_Type()
)
zxrosAMATInFilterpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATInFilterpackets.setStatus("current")
_ZxrosAMATOutFilterpackets_Type = Counter64
_ZxrosAMATOutFilterpackets_Object = MibTableColumn
zxrosAMATOutFilterpackets = _ZxrosAMATOutFilterpackets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 3),
    _ZxrosAMATOutFilterpackets_Type()
)
zxrosAMATOutFilterpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxrosAMATOutFilterpackets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXROS-AMAT-IF-MIB",
    **{"zte": zte,
       "zxros": zxros,
       "zxrosAMATIF": zxrosAMATIF,
       "zxrosAMATInterfaceEnableTable": zxrosAMATInterfaceEnableTable,
       "zxrosAMATInterfaceEnableEntry": zxrosAMATInterfaceEnableEntry,
       "zxrosAMATInterfaceEnableIfIndex": zxrosAMATInterfaceEnableIfIndex,
       "zxrosAMATInterfaceInAmatEnable": zxrosAMATInterfaceInAmatEnable,
       "zxrosAMATInterfaceOutAmatEnable": zxrosAMATInterfaceOutAmatEnable,
       "zxrosAMATInterfaceStatisticTable": zxrosAMATInterfaceStatisticTable,
       "zxrosAMATInterfaceStatisticEntry": zxrosAMATInterfaceStatisticEntry,
       "zxrosAMATInterfaceStatisticIfIndex": zxrosAMATInterfaceStatisticIfIndex,
       "zxrosAMATInFilterpackets": zxrosAMATInFilterpackets,
       "zxrosAMATOutFilterpackets": zxrosAMATOutFilterpackets}
)
