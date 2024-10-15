# SNMP MIB module (HPN-ICF-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LLDP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:49 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(LldpPortNumber,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicflldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100)
)
hpnicflldp.setRevisions(
        ("2009-03-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicflldpObjects_ObjectIdentity = ObjectIdentity
hpnicflldpObjects = _HpnicflldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1)
)
_HpnicflldpConfiguration_ObjectIdentity = ObjectIdentity
hpnicflldpConfiguration = _HpnicflldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1)
)
_HpnicflldpAdminStatus_Type = TruthValue
_HpnicflldpAdminStatus_Object = MibScalar
hpnicflldpAdminStatus = _HpnicflldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 1),
    _HpnicflldpAdminStatus_Type()
)
hpnicflldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicflldpAdminStatus.setStatus("current")
_HpnicflldpComplianceCDPStatus_Type = TruthValue
_HpnicflldpComplianceCDPStatus_Object = MibScalar
hpnicflldpComplianceCDPStatus = _HpnicflldpComplianceCDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 2),
    _HpnicflldpComplianceCDPStatus_Type()
)
hpnicflldpComplianceCDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicflldpComplianceCDPStatus.setStatus("current")
_HpnicflldpPortConfigTable_Object = MibTable
hpnicflldpPortConfigTable = _HpnicflldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicflldpPortConfigTable.setStatus("current")
_HpnicflldpPortConfigEntry_Object = MibTableRow
hpnicflldpPortConfigEntry = _HpnicflldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1)
)
hpnicflldpPortConfigEntry.setIndexNames(
    (0, "HPN-ICF-LLDP-EXT-MIB", "hpnicflldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    hpnicflldpPortConfigEntry.setStatus("current")
_HpnicflldpPortConfigPortNum_Type = LldpPortNumber
_HpnicflldpPortConfigPortNum_Object = MibTableColumn
hpnicflldpPortConfigPortNum = _HpnicflldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1, 1),
    _HpnicflldpPortConfigPortNum_Type()
)
hpnicflldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicflldpPortConfigPortNum.setStatus("current")


class _HpnicflldpPortConfigCDPComplianceStatus_Type(Integer32):
    """Custom type hpnicflldpPortConfigCDPComplianceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("txAndRx", 1))
    )


_HpnicflldpPortConfigCDPComplianceStatus_Type.__name__ = "Integer32"
_HpnicflldpPortConfigCDPComplianceStatus_Object = MibTableColumn
hpnicflldpPortConfigCDPComplianceStatus = _HpnicflldpPortConfigCDPComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 100, 1, 1, 3, 1, 2),
    _HpnicflldpPortConfigCDPComplianceStatus_Type()
)
hpnicflldpPortConfigCDPComplianceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicflldpPortConfigCDPComplianceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LLDP-EXT-MIB",
    **{"hpnicflldp": hpnicflldp,
       "hpnicflldpObjects": hpnicflldpObjects,
       "hpnicflldpConfiguration": hpnicflldpConfiguration,
       "hpnicflldpAdminStatus": hpnicflldpAdminStatus,
       "hpnicflldpComplianceCDPStatus": hpnicflldpComplianceCDPStatus,
       "hpnicflldpPortConfigTable": hpnicflldpPortConfigTable,
       "hpnicflldpPortConfigEntry": hpnicflldpPortConfigEntry,
       "hpnicflldpPortConfigPortNum": hpnicflldpPortConfigPortNum,
       "hpnicflldpPortConfigCDPComplianceStatus": hpnicflldpPortConfigCDPComplianceStatus}
)
