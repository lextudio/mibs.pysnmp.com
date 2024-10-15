# SNMP MIB module (JUNIPER-FRU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-FRU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:03 2024
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

(jnxFruMibRoot,
 jnxFruTraps) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxFruMibRoot",
    "jnxFruTraps")

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

jnxFruMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1)
)
jnxFruMib.setRevisions(
        ("2012-01-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxFruAdminStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outOfService", 2))
    )



class JnxFruOperStates(Integer32, TextualConvention):
    status = "current"
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
        *(("fault", 5),
          ("init", 2),
          ("mismatched", 4),
          ("normal", 3),
          ("swul", 6),
          ("unEquipped", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JnxFruCfg_ObjectIdentity = ObjectIdentity
jnxFruCfg = _JnxFruCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1)
)
_JnxFruCfgTable_Object = MibTable
jnxFruCfgTable = _JnxFruCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxFruCfgTable.setStatus("current")
_JnxFruCfgEntry_Object = MibTableRow
jnxFruCfgEntry = _JnxFruCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1)
)
jnxFruCfgEntry.setIndexNames(
    (0, "JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"),
    (0, "JUNIPER-FRU-MIB", "jnxFruCfgL1Index"),
    (0, "JUNIPER-FRU-MIB", "jnxFruCfgL2Index"),
    (0, "JUNIPER-FRU-MIB", "jnxFruCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxFruCfgEntry.setStatus("current")


class _JnxFruCfgContentsIndex_Type(Integer32):
    """Custom type jnxFruCfgContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFruCfgContentsIndex_Type.__name__ = "Integer32"
_JnxFruCfgContentsIndex_Object = MibTableColumn
jnxFruCfgContentsIndex = _JnxFruCfgContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 1),
    _JnxFruCfgContentsIndex_Type()
)
jnxFruCfgContentsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxFruCfgContentsIndex.setStatus("current")


class _JnxFruCfgL1Index_Type(Integer32):
    """Custom type jnxFruCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruCfgL1Index_Type.__name__ = "Integer32"
_JnxFruCfgL1Index_Object = MibTableColumn
jnxFruCfgL1Index = _JnxFruCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 2),
    _JnxFruCfgL1Index_Type()
)
jnxFruCfgL1Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxFruCfgL1Index.setStatus("current")


class _JnxFruCfgL2Index_Type(Integer32):
    """Custom type jnxFruCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruCfgL2Index_Type.__name__ = "Integer32"
_JnxFruCfgL2Index_Object = MibTableColumn
jnxFruCfgL2Index = _JnxFruCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 3),
    _JnxFruCfgL2Index_Type()
)
jnxFruCfgL2Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxFruCfgL2Index.setStatus("current")


class _JnxFruCfgL3Index_Type(Integer32):
    """Custom type jnxFruCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruCfgL3Index_Type.__name__ = "Integer32"
_JnxFruCfgL3Index_Object = MibTableColumn
jnxFruCfgL3Index = _JnxFruCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 4),
    _JnxFruCfgL3Index_Type()
)
jnxFruCfgL3Index.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxFruCfgL3Index.setStatus("current")
_JnxFruCfgType_Type = ObjectIdentifier
_JnxFruCfgType_Object = MibTableColumn
jnxFruCfgType = _JnxFruCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 5),
    _JnxFruCfgType_Type()
)
jnxFruCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxFruCfgType.setStatus("current")
_JnxFruCfgAdminState_Type = JnxFruAdminStates
_JnxFruCfgAdminState_Object = MibTableColumn
jnxFruCfgAdminState = _JnxFruCfgAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 6),
    _JnxFruCfgAdminState_Type()
)
jnxFruCfgAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxFruCfgAdminState.setStatus("current")
_JnxFruCfgOperState_Type = JnxFruOperStates
_JnxFruCfgOperState_Object = MibTableColumn
jnxFruCfgOperState = _JnxFruCfgOperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 74, 1, 1, 1, 1, 7),
    _JnxFruCfgOperState_Type()
)
jnxFruCfgOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruCfgOperState.setStatus("current")

# Managed Objects groups


# Notification objects

jnxFruNotifMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 23, 1)
)
jnxFruNotifMismatch.setObjects(
      *(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgType"))
)
if mibBuilder.loadTexts:
    jnxFruNotifMismatch.setStatus(
        "current"
    )

jnxFruNotifAdminStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 23, 2)
)
jnxFruNotifAdminStatus.setObjects(
      *(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgAdminState"))
)
if mibBuilder.loadTexts:
    jnxFruNotifAdminStatus.setStatus(
        "current"
    )

jnxFruNotifOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 23, 3)
)
jnxFruNotifOperStatus.setObjects(
      *(("JUNIPER-FRU-MIB", "jnxFruCfgContentsIndex"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL1Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL2Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgL3Index"),
        ("JUNIPER-FRU-MIB", "jnxFruCfgOperState"))
)
if mibBuilder.loadTexts:
    jnxFruNotifOperStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-FRU-MIB",
    **{"JnxFruAdminStates": JnxFruAdminStates,
       "JnxFruOperStates": JnxFruOperStates,
       "jnxFruMib": jnxFruMib,
       "jnxFruCfg": jnxFruCfg,
       "jnxFruCfgTable": jnxFruCfgTable,
       "jnxFruCfgEntry": jnxFruCfgEntry,
       "jnxFruCfgContentsIndex": jnxFruCfgContentsIndex,
       "jnxFruCfgL1Index": jnxFruCfgL1Index,
       "jnxFruCfgL2Index": jnxFruCfgL2Index,
       "jnxFruCfgL3Index": jnxFruCfgL3Index,
       "jnxFruCfgType": jnxFruCfgType,
       "jnxFruCfgAdminState": jnxFruCfgAdminState,
       "jnxFruCfgOperState": jnxFruCfgOperState,
       "jnxFruNotifMismatch": jnxFruNotifMismatch,
       "jnxFruNotifAdminStatus": jnxFruNotifAdminStatus,
       "jnxFruNotifOperStatus": jnxFruNotifOperStatus}
)
