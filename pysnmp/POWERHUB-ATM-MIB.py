# SNMP MIB module (POWERHUB-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POWERHUB-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:24 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fore_ObjectIdentity = ObjectIdentity
fore = _Fore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_Lsd_ObjectIdentity = ObjectIdentity
lsd = _Lsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6)
)
_Lsdproducts_ObjectIdentity = ObjectIdentity
lsdproducts = _Lsdproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1)
)
_Powerhub4k6k7k_ObjectIdentity = ObjectIdentity
powerhub4k6k7k = _Powerhub4k6k7k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1)
)
_Alchassis_ObjectIdentity = ObjectIdentity
alchassis = _Alchassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 1)
)
_Alatm_ObjectIdentity = ObjectIdentity
alatm = _Alatm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2)
)
_AlAtmAMASlotTable_Object = MibTable
alAtmAMASlotTable = _AlAtmAMASlotTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    alAtmAMASlotTable.setStatus("mandatory")
_AlAtmAMASlotEntry_Object = MibTableRow
alAtmAMASlotEntry = _AlAtmAMASlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1)
)
alAtmAMASlotEntry.setIndexNames(
    (0, "POWERHUB-ATM-MIB", "alAtmAMASlotNumber"),
)
if mibBuilder.loadTexts:
    alAtmAMASlotEntry.setStatus("mandatory")
_AlAtmAMASlotNumber_Type = Integer32
_AlAtmAMASlotNumber_Object = MibTableColumn
alAtmAMASlotNumber = _AlAtmAMASlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 1),
    _AlAtmAMASlotNumber_Type()
)
alAtmAMASlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMASlotNumber.setStatus("mandatory")


class _AlAtmAMAUserSelect_Type(Integer32):
    """Custom type alAtmAMAUserSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_AlAtmAMAUserSelect_Type.__name__ = "Integer32"
_AlAtmAMAUserSelect_Object = MibTableColumn
alAtmAMAUserSelect = _AlAtmAMAUserSelect_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 2),
    _AlAtmAMAUserSelect_Type()
)
alAtmAMAUserSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alAtmAMAUserSelect.setStatus("mandatory")


class _AlAtmAMAActualUse_Type(Integer32):
    """Custom type alAtmAMAActualUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )


_AlAtmAMAActualUse_Type.__name__ = "Integer32"
_AlAtmAMAActualUse_Object = MibTableColumn
alAtmAMAActualUse = _AlAtmAMAActualUse_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 3),
    _AlAtmAMAActualUse_Type()
)
alAtmAMAActualUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAActualUse.setStatus("mandatory")
_AlAtmAMAUTLevPrime_Type = Integer32
_AlAtmAMAUTLevPrime_Object = MibTableColumn
alAtmAMAUTLevPrime = _AlAtmAMAUTLevPrime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 4),
    _AlAtmAMAUTLevPrime_Type()
)
alAtmAMAUTLevPrime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAUTLevPrime.setStatus("mandatory")
_AlAtmAMAUTLevBack_Type = Integer32
_AlAtmAMAUTLevBack_Object = MibTableColumn
alAtmAMAUTLevBack = _AlAtmAMAUTLevBack_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 5),
    _AlAtmAMAUTLevBack_Type()
)
alAtmAMAUTLevBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAUTLevBack.setStatus("mandatory")
_AlAtmAMAUTVerPrime_Type = Integer32
_AlAtmAMAUTVerPrime_Object = MibTableColumn
alAtmAMAUTVerPrime = _AlAtmAMAUTVerPrime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 6),
    _AlAtmAMAUTVerPrime_Type()
)
alAtmAMAUTVerPrime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAUTVerPrime.setStatus("mandatory")
_AlAtmAMAUTVerBack_Type = Integer32
_AlAtmAMAUTVerBack_Object = MibTableColumn
alAtmAMAUTVerBack = _AlAtmAMAUTVerBack_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 7),
    _AlAtmAMAUTVerBack_Type()
)
alAtmAMAUTVerBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAUTVerBack.setStatus("mandatory")


class _AlAtmAMAProtoPrime_Type(Integer32):
    """Custom type alAtmAMAProtoPrime based on Integer32"""
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
        *(("ds3-45Mbps", 2),
          ("e3-39Mbps", 3),
          ("oc3-155Mbps", 1),
          ("unknown", 4))
    )


_AlAtmAMAProtoPrime_Type.__name__ = "Integer32"
_AlAtmAMAProtoPrime_Object = MibTableColumn
alAtmAMAProtoPrime = _AlAtmAMAProtoPrime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 8),
    _AlAtmAMAProtoPrime_Type()
)
alAtmAMAProtoPrime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAProtoPrime.setStatus("mandatory")


class _AlAtmAMAProtoBack_Type(Integer32):
    """Custom type alAtmAMAProtoBack based on Integer32"""
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
        *(("ds3-45Mbps", 2),
          ("e3-39Mbps", 3),
          ("oc3-155Mbps", 1),
          ("unknown", 4))
    )


_AlAtmAMAProtoBack_Type.__name__ = "Integer32"
_AlAtmAMAProtoBack_Object = MibTableColumn
alAtmAMAProtoBack = _AlAtmAMAProtoBack_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 9),
    _AlAtmAMAProtoBack_Type()
)
alAtmAMAProtoBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAProtoBack.setStatus("mandatory")


class _AlAtmAMAMediaPrime_Type(Integer32):
    """Custom type alAtmAMAMediaPrime based on Integer32"""
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
        *(("cat5utp", 1),
          ("coax", 2),
          ("mf", 3),
          ("sf", 4),
          ("unknown", 5))
    )


_AlAtmAMAMediaPrime_Type.__name__ = "Integer32"
_AlAtmAMAMediaPrime_Object = MibTableColumn
alAtmAMAMediaPrime = _AlAtmAMAMediaPrime_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 10),
    _AlAtmAMAMediaPrime_Type()
)
alAtmAMAMediaPrime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAMediaPrime.setStatus("mandatory")


class _AlAtmAMAMediaBack_Type(Integer32):
    """Custom type alAtmAMAMediaBack based on Integer32"""
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
        *(("cat5utp", 1),
          ("coax", 2),
          ("mf", 3),
          ("sf", 4),
          ("unknown", 5))
    )


_AlAtmAMAMediaBack_Type.__name__ = "Integer32"
_AlAtmAMAMediaBack_Object = MibTableColumn
alAtmAMAMediaBack = _AlAtmAMAMediaBack_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 11),
    _AlAtmAMAMediaBack_Type()
)
alAtmAMAMediaBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmAMAMediaBack.setStatus("mandatory")


class _AlAtmPreviousAMA_Type(Integer32):
    """Custom type alAtmPreviousAMA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1),
          ("unknown", 3))
    )


_AlAtmPreviousAMA_Type.__name__ = "Integer32"
_AlAtmPreviousAMA_Object = MibTableColumn
alAtmPreviousAMA = _AlAtmPreviousAMA_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 12),
    _AlAtmPreviousAMA_Type()
)
alAtmPreviousAMA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmPreviousAMA.setStatus("mandatory")


class _AlAtmPreviousAMAType_Type(Integer32):
    """Custom type alAtmPreviousAMAType based on Integer32"""
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
        *(("ds3-45Mbps", 2),
          ("e3-39Mbps", 3),
          ("oc3-155Mbps", 1),
          ("unknown", 4))
    )


_AlAtmPreviousAMAType_Type.__name__ = "Integer32"
_AlAtmPreviousAMAType_Object = MibTableColumn
alAtmPreviousAMAType = _AlAtmPreviousAMAType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 13),
    _AlAtmPreviousAMAType_Type()
)
alAtmPreviousAMAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmPreviousAMAType.setStatus("mandatory")


class _AlAtmCurrentAMAType_Type(Integer32):
    """Custom type alAtmCurrentAMAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds3-45Mbps", 2),
          ("e3-39Mbps", 3),
          ("oc3-155Mbps", 1))
    )


_AlAtmCurrentAMAType_Type.__name__ = "Integer32"
_AlAtmCurrentAMAType_Object = MibTableColumn
alAtmCurrentAMAType = _AlAtmCurrentAMAType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 8, 1, 14),
    _AlAtmCurrentAMAType_Type()
)
alAtmCurrentAMAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alAtmCurrentAMAType.setStatus("mandatory")
_Powerbits_ObjectIdentity = ObjectIdentity
powerbits = _Powerbits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 2)
)
_Lsdcommon_ObjectIdentity = ObjectIdentity
lsdcommon = _Lsdcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 2)
)

# Managed Objects groups


# Notification objects

atmLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 0, 1)
)
atmLinkUp.setObjects(
      *(("POWERHUB-ATM-MIB", "alAtmAMASlotNumber"),
        ("POWERHUB-ATM-MIB", "alAtmAMAActualUse"),
        ("POWERHUB-ATM-MIB", "alAtmCurrentAMAType"))
)
if mibBuilder.loadTexts:
    atmLinkUp.setStatus(
        ""
    )

atmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 0, 2)
)
atmLinkDown.setObjects(
      *(("POWERHUB-ATM-MIB", "alAtmAMASlotNumber"),
        ("POWERHUB-ATM-MIB", "alAtmPreviousAMA"),
        ("POWERHUB-ATM-MIB", "alAtmPreviousAMAType"))
)
if mibBuilder.loadTexts:
    atmLinkDown.setStatus(
        ""
    )

atmCutOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 0, 3)
)
atmCutOver.setObjects(
      *(("POWERHUB-ATM-MIB", "alAtmAMASlotNumber"),
        ("POWERHUB-ATM-MIB", "alAtmAMAActualUse"),
        ("POWERHUB-ATM-MIB", "alAtmCurrentAMAType"),
        ("POWERHUB-ATM-MIB", "alAtmPreviousAMA"),
        ("POWERHUB-ATM-MIB", "alAtmPreviousAMAType"))
)
if mibBuilder.loadTexts:
    atmCutOver.setStatus(
        ""
    )

atmBootUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 0, 4)
)
atmBootUp.setObjects(
      *(("POWERHUB-ATM-MIB", "alAtmAMASlotNumber"),
        ("POWERHUB-ATM-MIB", "alAtmAMAActualUse"),
        ("POWERHUB-ATM-MIB", "alAtmCurrentAMAType"))
)
if mibBuilder.loadTexts:
    atmBootUp.setStatus(
        ""
    )

atmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 6, 1, 1, 2, 0, 5)
)
atmFault.setObjects(
    ("POWERHUB-ATM-MIB", "alAtmAMASlotNumber")
)
if mibBuilder.loadTexts:
    atmFault.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POWERHUB-ATM-MIB",
    **{"fore": fore,
       "systems": systems,
       "lsd": lsd,
       "lsdproducts": lsdproducts,
       "powerhub4k6k7k": powerhub4k6k7k,
       "alchassis": alchassis,
       "alatm": alatm,
       "atmLinkUp": atmLinkUp,
       "atmLinkDown": atmLinkDown,
       "atmCutOver": atmCutOver,
       "atmBootUp": atmBootUp,
       "atmFault": atmFault,
       "alAtmAMASlotTable": alAtmAMASlotTable,
       "alAtmAMASlotEntry": alAtmAMASlotEntry,
       "alAtmAMASlotNumber": alAtmAMASlotNumber,
       "alAtmAMAUserSelect": alAtmAMAUserSelect,
       "alAtmAMAActualUse": alAtmAMAActualUse,
       "alAtmAMAUTLevPrime": alAtmAMAUTLevPrime,
       "alAtmAMAUTLevBack": alAtmAMAUTLevBack,
       "alAtmAMAUTVerPrime": alAtmAMAUTVerPrime,
       "alAtmAMAUTVerBack": alAtmAMAUTVerBack,
       "alAtmAMAProtoPrime": alAtmAMAProtoPrime,
       "alAtmAMAProtoBack": alAtmAMAProtoBack,
       "alAtmAMAMediaPrime": alAtmAMAMediaPrime,
       "alAtmAMAMediaBack": alAtmAMAMediaBack,
       "alAtmPreviousAMA": alAtmPreviousAMA,
       "alAtmPreviousAMAType": alAtmPreviousAMAType,
       "alAtmCurrentAMAType": alAtmCurrentAMAType,
       "powerbits": powerbits,
       "lsdcommon": lsdcommon}
)
