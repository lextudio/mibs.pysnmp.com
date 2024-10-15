# SNMP MIB module (HM2-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:04 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hm2LLDPMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 34)
)
hm2LLDPMib.setRevisions(
        ("2011-04-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2LLDPMibObjects_ObjectIdentity = ObjectIdentity
hm2LLDPMibObjects = _Hm2LLDPMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1)
)
_Hm2LLDPConfigGroup_ObjectIdentity = ObjectIdentity
hm2LLDPConfigGroup = _Hm2LLDPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1)
)


class _Hm2LLDPAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2LLDPAdminStatus based on HmEnabledStatus"""


_Hm2LLDPAdminStatus_Object = MibScalar
hm2LLDPAdminStatus = _Hm2LLDPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 1),
    _Hm2LLDPAdminStatus_Type()
)
hm2LLDPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LLDPAdminStatus.setStatus("current")
_Hm2LLDPIfTable_Object = MibTable
hm2LLDPIfTable = _Hm2LLDPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2LLDPIfTable.setStatus("current")
_Hm2LLDPIfEntry_Object = MibTableRow
hm2LLDPIfEntry = _Hm2LLDPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1)
)
hm2LLDPIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2LLDPIfEntry.setStatus("current")


class _Hm2LLDPIfMaxNeighbors_Type(Integer32):
    """Custom type hm2LLDPIfMaxNeighbors based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Hm2LLDPIfMaxNeighbors_Type.__name__ = "Integer32"
_Hm2LLDPIfMaxNeighbors_Object = MibTableColumn
hm2LLDPIfMaxNeighbors = _Hm2LLDPIfMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1, 1),
    _Hm2LLDPIfMaxNeighbors_Type()
)
hm2LLDPIfMaxNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LLDPIfMaxNeighbors.setStatus("current")


class _Hm2LLDPIfFDBMode_Type(Integer32):
    """Custom type hm2LLDPIfFDBMode based on Integer32"""
    defaultValue = 4

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
        *(("autoDetect", 4),
          ("both", 3),
          ("lldpOnly", 1),
          ("macOnly", 2))
    )


_Hm2LLDPIfFDBMode_Type.__name__ = "Integer32"
_Hm2LLDPIfFDBMode_Object = MibTableColumn
hm2LLDPIfFDBMode = _Hm2LLDPIfFDBMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 34, 1, 1, 2, 1, 2),
    _Hm2LLDPIfFDBMode_Type()
)
hm2LLDPIfFDBMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LLDPIfFDBMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-LLDP-MIB",
    **{"hm2LLDPMib": hm2LLDPMib,
       "hm2LLDPMibObjects": hm2LLDPMibObjects,
       "hm2LLDPConfigGroup": hm2LLDPConfigGroup,
       "hm2LLDPAdminStatus": hm2LLDPAdminStatus,
       "hm2LLDPIfTable": hm2LLDPIfTable,
       "hm2LLDPIfEntry": hm2LLDPIfEntry,
       "hm2LLDPIfMaxNeighbors": hm2LLDPIfMaxNeighbors,
       "hm2LLDPIfFDBMode": hm2LLDPIfFDBMode}
)
