# SNMP MIB module (ASCEND-MIBREDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBREDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:06 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibredundancyProfile_ObjectIdentity = ObjectIdentity
mibredundancyProfile = _MibredundancyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 16)
)
_MibredundancyProfileTable_Object = MibTable
mibredundancyProfileTable = _MibredundancyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1)
)
if mibBuilder.loadTexts:
    mibredundancyProfileTable.setStatus("mandatory")
_MibredundancyProfileEntry_Object = MibTableRow
mibredundancyProfileEntry = _MibredundancyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1)
)
mibredundancyProfileEntry.setIndexNames(
    (0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibredundancyProfileEntry.setStatus("mandatory")
_RedundancyProfile_Index_o_Type = Integer32
_RedundancyProfile_Index_o_Object = MibScalar
redundancyProfile_Index_o = _RedundancyProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 1),
    _RedundancyProfile_Index_o_Type()
)
redundancyProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyProfile_Index_o.setStatus("mandatory")


class _RedundancyProfile_PrimaryPreference_Type(Integer32):
    """Custom type redundancyProfile_PrimaryPreference based on Integer32"""
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
        *(("firstControllerPreferred", 4),
          ("leftControllerPreferred", 2),
          ("noPreference", 1),
          ("rightControllerPreferred", 3),
          ("secondControllerPreferred", 5))
    )


_RedundancyProfile_PrimaryPreference_Type.__name__ = "Integer32"
_RedundancyProfile_PrimaryPreference_Object = MibScalar
redundancyProfile_PrimaryPreference = _RedundancyProfile_PrimaryPreference_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 2),
    _RedundancyProfile_PrimaryPreference_Type()
)
redundancyProfile_PrimaryPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyProfile_PrimaryPreference.setStatus("mandatory")


class _RedundancyProfile_Action_o_Type(Integer32):
    """Custom type redundancyProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_RedundancyProfile_Action_o_Type.__name__ = "Integer32"
_RedundancyProfile_Action_o_Object = MibScalar
redundancyProfile_Action_o = _RedundancyProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 3),
    _RedundancyProfile_Action_o_Type()
)
redundancyProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyProfile_Action_o.setStatus("mandatory")


class _RedundancyProfile_SyncEnabled_Type(Integer32):
    """Custom type redundancyProfile_SyncEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RedundancyProfile_SyncEnabled_Type.__name__ = "Integer32"
_RedundancyProfile_SyncEnabled_Object = MibScalar
redundancyProfile_SyncEnabled = _RedundancyProfile_SyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 1, 1, 4),
    _RedundancyProfile_SyncEnabled_Type()
)
redundancyProfile_SyncEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyProfile_SyncEnabled.setStatus("mandatory")
_MibredundancyProfile_ContextTable_Object = MibTable
mibredundancyProfile_ContextTable = _MibredundancyProfile_ContextTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 2)
)
if mibBuilder.loadTexts:
    mibredundancyProfile_ContextTable.setStatus("mandatory")
_MibredundancyProfile_ContextEntry_Object = MibTableRow
mibredundancyProfile_ContextEntry = _MibredundancyProfile_ContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1)
)
mibredundancyProfile_ContextEntry.setIndexNames(
    (0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Context-Index-o"),
    (0, "ASCEND-MIBREDUNDANCY-MIB", "redundancyProfile-Context-Index1-o"),
)
if mibBuilder.loadTexts:
    mibredundancyProfile_ContextEntry.setStatus("mandatory")
_RedundancyProfile_Context_Index_o_Type = Integer32
_RedundancyProfile_Context_Index_o_Object = MibScalar
redundancyProfile_Context_Index_o = _RedundancyProfile_Context_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 1),
    _RedundancyProfile_Context_Index_o_Type()
)
redundancyProfile_Context_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyProfile_Context_Index_o.setStatus("mandatory")
_RedundancyProfile_Context_Index1_o_Type = Integer32
_RedundancyProfile_Context_Index1_o_Object = MibScalar
redundancyProfile_Context_Index1_o = _RedundancyProfile_Context_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 2),
    _RedundancyProfile_Context_Index1_o_Type()
)
redundancyProfile_Context_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyProfile_Context_Index1_o.setStatus("mandatory")


class _RedundancyProfile_Context_MustAgree_Type(Integer32):
    """Custom type redundancyProfile_Context_MustAgree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RedundancyProfile_Context_MustAgree_Type.__name__ = "Integer32"
_RedundancyProfile_Context_MustAgree_Object = MibScalar
redundancyProfile_Context_MustAgree = _RedundancyProfile_Context_MustAgree_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 16, 2, 1, 3),
    _RedundancyProfile_Context_MustAgree_Type()
)
redundancyProfile_Context_MustAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyProfile_Context_MustAgree.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBREDUNDANCY-MIB",
    **{"DisplayString": DisplayString,
       "mibredundancyProfile": mibredundancyProfile,
       "mibredundancyProfileTable": mibredundancyProfileTable,
       "mibredundancyProfileEntry": mibredundancyProfileEntry,
       "redundancyProfile-Index-o": redundancyProfile_Index_o,
       "redundancyProfile-PrimaryPreference": redundancyProfile_PrimaryPreference,
       "redundancyProfile-Action-o": redundancyProfile_Action_o,
       "redundancyProfile-SyncEnabled": redundancyProfile_SyncEnabled,
       "mibredundancyProfile-ContextTable": mibredundancyProfile_ContextTable,
       "mibredundancyProfile-ContextEntry": mibredundancyProfile_ContextEntry,
       "redundancyProfile-Context-Index-o": redundancyProfile_Context_Index_o,
       "redundancyProfile-Context-Index1-o": redundancyProfile_Context_Index1_o,
       "redundancyProfile-Context-MustAgree": redundancyProfile_Context_MustAgree}
)
