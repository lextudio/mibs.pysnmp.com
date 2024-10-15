# SNMP MIB module (Fore-Ima-Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Ima-Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:06 2024
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

(asx,
 atmSwitch) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx",
    "atmSwitch")

(imaGroupIndex,) = mibBuilder.importSymbols(
    "IMA-MIB",
    "imaGroupIndex")

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

foreImaExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ForeImaVersionNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v10", 1),
          ("v11", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ForeImaVersion_ObjectIdentity = ObjectIdentity
foreImaVersion = _ForeImaVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1)
)
_ForeImaVersionTable_Object = MibTable
foreImaVersionTable = _ForeImaVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    foreImaVersionTable.setStatus("current")
_ForeImaVersionEntry_Object = MibTableRow
foreImaVersionEntry = _ForeImaVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1)
)
foreImaVersionEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    foreImaVersionEntry.setStatus("current")


class _ForeImaVersionConfigured_Type(ForeImaVersionNumber):
    """Custom type foreImaVersionConfigured based on ForeImaVersionNumber"""
    defaultValue = 2


_ForeImaVersionConfigured_Object = MibTableColumn
foreImaVersionConfigured = _ForeImaVersionConfigured_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 1),
    _ForeImaVersionConfigured_Type()
)
foreImaVersionConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    foreImaVersionConfigured.setStatus("current")
_ForeImaVersionOperational_Type = ForeImaVersionNumber
_ForeImaVersionOperational_Object = MibTableColumn
foreImaVersionOperational = _ForeImaVersionOperational_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 2),
    _ForeImaVersionOperational_Type()
)
foreImaVersionOperational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    foreImaVersionOperational.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Ima-Ext-MIB",
    **{"ForeImaVersionNumber": ForeImaVersionNumber,
       "foreImaExtMib": foreImaExtMib,
       "foreImaVersion": foreImaVersion,
       "foreImaVersionTable": foreImaVersionTable,
       "foreImaVersionEntry": foreImaVersionEntry,
       "foreImaVersionConfigured": foreImaVersionConfigured,
       "foreImaVersionOperational": foreImaVersionOperational}
)
