# SNMP MIB module (HP-ICF-SRCIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SRCIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:13 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

hpicfSrcIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13)
)
hpicfSrcIpMIB.setRevisions(
        ("2016-08-29 00:00",
         "2011-07-21 00:00",
         "2009-04-30 00:00",
         "2008-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSrcIpConfig_ObjectIdentity = ObjectIdentity
hpicfSrcIpConfig = _HpicfSrcIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1)
)
_HpicfSrcIpAddrPolicyTable_Object = MibTable
hpicfSrcIpAddrPolicyTable = _HpicfSrcIpAddrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicyTable.setStatus("current")
_HpicfSrcIpAddrPolicyEntry_Object = MibTableRow
hpicfSrcIpAddrPolicyEntry = _HpicfSrcIpAddrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1)
)
hpicfSrcIpAddrPolicyEntry.setIndexNames(
    (0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpAddressType"),
    (0, "HP-ICF-SRCIP-MIB", "hpicfSrcIpProtocolIndex"),
)
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicyEntry.setStatus("current")
_HpicfSrcIpAddressType_Type = InetAddressType
_HpicfSrcIpAddressType_Object = MibTableColumn
hpicfSrcIpAddressType = _HpicfSrcIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 1),
    _HpicfSrcIpAddressType_Type()
)
hpicfSrcIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSrcIpAddressType.setStatus("current")


class _HpicfSrcIpProtocolIndex_Type(Integer32):
    """Custom type hpicfSrcIpProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("sflow", 7),
          ("sntp", 6),
          ("syslog", 3),
          ("tacacs", 1),
          ("telnet", 4),
          ("tftp", 5),
          ("tunnelednodeserver", 8))
    )


_HpicfSrcIpProtocolIndex_Type.__name__ = "Integer32"
_HpicfSrcIpProtocolIndex_Object = MibTableColumn
hpicfSrcIpProtocolIndex = _HpicfSrcIpProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 2),
    _HpicfSrcIpProtocolIndex_Type()
)
hpicfSrcIpProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSrcIpProtocolIndex.setStatus("current")


class _HpicfSrcIpAddrPolicy_Type(Integer32):
    """Custom type hpicfSrcIpAddrPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuredInterface", 3),
          ("configuredIpAddr", 2),
          ("outgoingInterface", 1))
    )


_HpicfSrcIpAddrPolicy_Type.__name__ = "Integer32"
_HpicfSrcIpAddrPolicy_Object = MibTableColumn
hpicfSrcIpAddrPolicy = _HpicfSrcIpAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 3),
    _HpicfSrcIpAddrPolicy_Type()
)
hpicfSrcIpAddrPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddrPolicy.setStatus("current")
_HpicfSrcIpAddrIfIndex_Type = InterfaceIndexOrZero
_HpicfSrcIpAddrIfIndex_Object = MibTableColumn
hpicfSrcIpAddrIfIndex = _HpicfSrcIpAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 4),
    _HpicfSrcIpAddrIfIndex_Type()
)
hpicfSrcIpAddrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddrIfIndex.setStatus("current")
_HpicfSrcIpAddress_Type = InetAddress
_HpicfSrcIpAddress_Object = MibTableColumn
hpicfSrcIpAddress = _HpicfSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 1, 1, 1, 5),
    _HpicfSrcIpAddress_Type()
)
hpicfSrcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSrcIpAddress.setStatus("current")
_HpicfSrcIpConformance_ObjectIdentity = ObjectIdentity
hpicfSrcIpConformance = _HpicfSrcIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2)
)
_HpicfSrcIpGroups_ObjectIdentity = ObjectIdentity
hpicfSrcIpGroups = _HpicfSrcIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1)
)
_HpicfSrcIpCompliances_ObjectIdentity = ObjectIdentity
hpicfSrcIpCompliances = _HpicfSrcIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2)
)

# Managed Objects groups

hpicfSrcIpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 1, 1)
)
hpicfSrcIpBaseGroup.setObjects(
      *(("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrPolicy"),
        ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddrIfIndex"),
        ("HP-ICF-SRCIP-MIB", "hpicfSrcIpAddress"))
)
if mibBuilder.loadTexts:
    hpicfSrcIpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSrcIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfSrcIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SRCIP-MIB",
    **{"hpicfSrcIpMIB": hpicfSrcIpMIB,
       "hpicfSrcIpConfig": hpicfSrcIpConfig,
       "hpicfSrcIpAddrPolicyTable": hpicfSrcIpAddrPolicyTable,
       "hpicfSrcIpAddrPolicyEntry": hpicfSrcIpAddrPolicyEntry,
       "hpicfSrcIpAddressType": hpicfSrcIpAddressType,
       "hpicfSrcIpProtocolIndex": hpicfSrcIpProtocolIndex,
       "hpicfSrcIpAddrPolicy": hpicfSrcIpAddrPolicy,
       "hpicfSrcIpAddrIfIndex": hpicfSrcIpAddrIfIndex,
       "hpicfSrcIpAddress": hpicfSrcIpAddress,
       "hpicfSrcIpConformance": hpicfSrcIpConformance,
       "hpicfSrcIpGroups": hpicfSrcIpGroups,
       "hpicfSrcIpBaseGroup": hpicfSrcIpBaseGroup,
       "hpicfSrcIpCompliances": hpicfSrcIpCompliances,
       "hpicfSrcIpCompliance": hpicfSrcIpCompliance}
)
