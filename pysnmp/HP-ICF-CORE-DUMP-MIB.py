# SNMP MIB module (HP-ICF-CORE-DUMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-CORE-DUMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:13 2024
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

(hpicfCommon,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hpicfCoreDumpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14)
)
hpicfCoreDumpMIB.setRevisions(
        ("2010-06-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfCoreDumpObjects_ObjectIdentity = ObjectIdentity
hpicfCoreDumpObjects = _HpicfCoreDumpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1)
)
_HpicfCoreDumpConfig_ObjectIdentity = ObjectIdentity
hpicfCoreDumpConfig = _HpicfCoreDumpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1)
)
_HpicfCoreDumpTable_Object = MibTable
hpicfCoreDumpTable = _HpicfCoreDumpTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfCoreDumpTable.setStatus("current")
_HpicfCoreDumpEntry_Object = MibTableRow
hpicfCoreDumpEntry = _HpicfCoreDumpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1)
)
hpicfCoreDumpEntry.setIndexNames(
    (0, "HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpModule"),
)
if mibBuilder.loadTexts:
    hpicfCoreDumpEntry.setStatus("current")


class _HpicfCoreDumpModule_Type(Integer32):
    """Custom type hpicfCoreDumpModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfCoreDumpModule_Type.__name__ = "Integer32"
_HpicfCoreDumpModule_Object = MibTableColumn
hpicfCoreDumpModule = _HpicfCoreDumpModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 1),
    _HpicfCoreDumpModule_Type()
)
hpicfCoreDumpModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfCoreDumpModule.setStatus("current")


class _HpicfCoreDumpMmStatus_Type(Integer32):
    """Custom type hpicfCoreDumpMmStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfCoreDumpMmStatus_Type.__name__ = "Integer32"
_HpicfCoreDumpMmStatus_Object = MibTableColumn
hpicfCoreDumpMmStatus = _HpicfCoreDumpMmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 2),
    _HpicfCoreDumpMmStatus_Type()
)
hpicfCoreDumpMmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfCoreDumpMmStatus.setStatus("current")


class _HpicfCoreDumpImStatus_Type(Integer32):
    """Custom type hpicfCoreDumpImStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfCoreDumpImStatus_Type.__name__ = "Integer32"
_HpicfCoreDumpImStatus_Object = MibTableColumn
hpicfCoreDumpImStatus = _HpicfCoreDumpImStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 1, 1, 3),
    _HpicfCoreDumpImStatus_Type()
)
hpicfCoreDumpImStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfCoreDumpImStatus.setStatus("current")
_HpicfCoreDumpTftpServerAddressType_Type = InetAddressType
_HpicfCoreDumpTftpServerAddressType_Object = MibScalar
hpicfCoreDumpTftpServerAddressType = _HpicfCoreDumpTftpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 2),
    _HpicfCoreDumpTftpServerAddressType_Type()
)
hpicfCoreDumpTftpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfCoreDumpTftpServerAddressType.setStatus("current")
_HpicfCoreDumpTftpServerAddress_Type = InetAddress
_HpicfCoreDumpTftpServerAddress_Object = MibScalar
hpicfCoreDumpTftpServerAddress = _HpicfCoreDumpTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 1, 1, 3),
    _HpicfCoreDumpTftpServerAddress_Type()
)
hpicfCoreDumpTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfCoreDumpTftpServerAddress.setStatus("current")
_HpicfCoreDumpConformance_ObjectIdentity = ObjectIdentity
hpicfCoreDumpConformance = _HpicfCoreDumpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2)
)
_HpicfCoreDumpConfigGroups_ObjectIdentity = ObjectIdentity
hpicfCoreDumpConfigGroups = _HpicfCoreDumpConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 1)
)
_HpicfCoreDumpCompliances_ObjectIdentity = ObjectIdentity
hpicfCoreDumpCompliances = _HpicfCoreDumpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 2)
)

# Managed Objects groups

hpicfCoreDumpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 1, 1)
)
hpicfCoreDumpConfigGroup.setObjects(
      *(("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpMmStatus"),
        ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpImStatus"),
        ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpTftpServerAddress"),
        ("HP-ICF-CORE-DUMP-MIB", "hpicfCoreDumpTftpServerAddressType"))
)
if mibBuilder.loadTexts:
    hpicfCoreDumpConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfCoreDumpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfCoreDumpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-CORE-DUMP-MIB",
    **{"hpicfCoreDumpMIB": hpicfCoreDumpMIB,
       "hpicfCoreDumpObjects": hpicfCoreDumpObjects,
       "hpicfCoreDumpConfig": hpicfCoreDumpConfig,
       "hpicfCoreDumpTable": hpicfCoreDumpTable,
       "hpicfCoreDumpEntry": hpicfCoreDumpEntry,
       "hpicfCoreDumpModule": hpicfCoreDumpModule,
       "hpicfCoreDumpMmStatus": hpicfCoreDumpMmStatus,
       "hpicfCoreDumpImStatus": hpicfCoreDumpImStatus,
       "hpicfCoreDumpTftpServerAddressType": hpicfCoreDumpTftpServerAddressType,
       "hpicfCoreDumpTftpServerAddress": hpicfCoreDumpTftpServerAddress,
       "hpicfCoreDumpConformance": hpicfCoreDumpConformance,
       "hpicfCoreDumpConfigGroups": hpicfCoreDumpConfigGroups,
       "hpicfCoreDumpConfigGroup": hpicfCoreDumpConfigGroup,
       "hpicfCoreDumpCompliances": hpicfCoreDumpCompliances,
       "hpicfCoreDumpCompliance": hpicfCoreDumpCompliance}
)
