# SNMP MIB module (ASCEND-MIBBILL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBILL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:16 2024
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

_MibbillingProfile_ObjectIdentity = ObjectIdentity
mibbillingProfile = _MibbillingProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 61)
)
_MibbillingProfileTable_Object = MibTable
mibbillingProfileTable = _MibbillingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 1)
)
if mibBuilder.loadTexts:
    mibbillingProfileTable.setStatus("mandatory")
_MibbillingProfileEntry_Object = MibTableRow
mibbillingProfileEntry = _MibbillingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1)
)
mibbillingProfileEntry.setIndexNames(
    (0, "ASCEND-MIBBILL-MIB", "billingProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibbillingProfileEntry.setStatus("mandatory")
_BillingProfile_Index_o_Type = Integer32
_BillingProfile_Index_o_Object = MibScalar
billingProfile_Index_o = _BillingProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 1),
    _BillingProfile_Index_o_Type()
)
billingProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingProfile_Index_o.setStatus("mandatory")
_BillingProfile_SystemDs0Minutes_Type = Integer32
_BillingProfile_SystemDs0Minutes_Object = MibScalar
billingProfile_SystemDs0Minutes = _BillingProfile_SystemDs0Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 2),
    _BillingProfile_SystemDs0Minutes_Type()
)
billingProfile_SystemDs0Minutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billingProfile_SystemDs0Minutes.setStatus("mandatory")


class _BillingProfile_Action_o_Type(Integer32):
    """Custom type billingProfile_Action_o based on Integer32"""
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


_BillingProfile_Action_o_Type.__name__ = "Integer32"
_BillingProfile_Action_o_Object = MibScalar
billingProfile_Action_o = _BillingProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 1, 1, 3),
    _BillingProfile_Action_o_Type()
)
billingProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billingProfile_Action_o.setStatus("mandatory")
_MibbillingProfile_PortDs0MinutesTable_Object = MibTable
mibbillingProfile_PortDs0MinutesTable = _MibbillingProfile_PortDs0MinutesTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 2)
)
if mibBuilder.loadTexts:
    mibbillingProfile_PortDs0MinutesTable.setStatus("mandatory")
_MibbillingProfile_PortDs0MinutesEntry_Object = MibTableRow
mibbillingProfile_PortDs0MinutesEntry = _MibbillingProfile_PortDs0MinutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1)
)
mibbillingProfile_PortDs0MinutesEntry.setIndexNames(
    (0, "ASCEND-MIBBILL-MIB", "billingProfile-PortDs0Minutes-Index-o"),
    (0, "ASCEND-MIBBILL-MIB", "billingProfile-PortDs0Minutes-Index1-o"),
)
if mibBuilder.loadTexts:
    mibbillingProfile_PortDs0MinutesEntry.setStatus("mandatory")
_BillingProfile_PortDs0Minutes_Index_o_Type = Integer32
_BillingProfile_PortDs0Minutes_Index_o_Object = MibScalar
billingProfile_PortDs0Minutes_Index_o = _BillingProfile_PortDs0Minutes_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 1),
    _BillingProfile_PortDs0Minutes_Index_o_Type()
)
billingProfile_PortDs0Minutes_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingProfile_PortDs0Minutes_Index_o.setStatus("mandatory")
_BillingProfile_PortDs0Minutes_Index1_o_Type = Integer32
_BillingProfile_PortDs0Minutes_Index1_o_Object = MibScalar
billingProfile_PortDs0Minutes_Index1_o = _BillingProfile_PortDs0Minutes_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 2),
    _BillingProfile_PortDs0Minutes_Index1_o_Type()
)
billingProfile_PortDs0Minutes_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billingProfile_PortDs0Minutes_Index1_o.setStatus("mandatory")
_BillingProfile_PortDs0Minutes_Type = Integer32
_BillingProfile_PortDs0Minutes_Object = MibScalar
billingProfile_PortDs0Minutes = _BillingProfile_PortDs0Minutes_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 61, 2, 1, 3),
    _BillingProfile_PortDs0Minutes_Type()
)
billingProfile_PortDs0Minutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billingProfile_PortDs0Minutes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBILL-MIB",
    **{"DisplayString": DisplayString,
       "mibbillingProfile": mibbillingProfile,
       "mibbillingProfileTable": mibbillingProfileTable,
       "mibbillingProfileEntry": mibbillingProfileEntry,
       "billingProfile-Index-o": billingProfile_Index_o,
       "billingProfile-SystemDs0Minutes": billingProfile_SystemDs0Minutes,
       "billingProfile-Action-o": billingProfile_Action_o,
       "mibbillingProfile-PortDs0MinutesTable": mibbillingProfile_PortDs0MinutesTable,
       "mibbillingProfile-PortDs0MinutesEntry": mibbillingProfile_PortDs0MinutesEntry,
       "billingProfile-PortDs0Minutes-Index-o": billingProfile_PortDs0Minutes_Index_o,
       "billingProfile-PortDs0Minutes-Index1-o": billingProfile_PortDs0Minutes_Index1_o,
       "billingProfile-PortDs0Minutes": billingProfile_PortDs0Minutes}
)
