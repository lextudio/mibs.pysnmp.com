# SNMP MIB module (HPICF-AMP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-AMP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:16 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfAMPServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125)
)
hpicfAMPServerMIB.setRevisions(
        ("2017-03-07 00:00",
         "2017-01-04 00:00",
         "2016-12-16 00:00",
         "2016-09-15 00:00",
         "2016-04-19 00:00",
         "2016-03-03 00:00",
         "2015-12-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfArubaVPNType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("amp", 2),
          ("any", 3),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfAMPServerObjects_ObjectIdentity = ObjectIdentity
hpicfAMPServerObjects = _HpicfAMPServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1)
)
_HpicfAMPServerIPType_Type = InetAddressType
_HpicfAMPServerIPType_Object = MibScalar
hpicfAMPServerIPType = _HpicfAMPServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 1),
    _HpicfAMPServerIPType_Type()
)
hpicfAMPServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerIPType.setStatus("current")
_HpicfAMPServerIP_Type = InetAddress
_HpicfAMPServerIP_Object = MibScalar
hpicfAMPServerIP = _HpicfAMPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 2),
    _HpicfAMPServerIP_Type()
)
hpicfAMPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerIP.setStatus("current")


class _HpicfAMPServerGroup_Type(OctetString):
    """Custom type hpicfAMPServerGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfAMPServerGroup_Type.__name__ = "OctetString"
_HpicfAMPServerGroup_Object = MibScalar
hpicfAMPServerGroup = _HpicfAMPServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 3),
    _HpicfAMPServerGroup_Type()
)
hpicfAMPServerGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerGroup.setStatus("current")


class _HpicfAMPServerFolder_Type(OctetString):
    """Custom type hpicfAMPServerFolder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfAMPServerFolder_Type.__name__ = "OctetString"
_HpicfAMPServerFolder_Object = MibScalar
hpicfAMPServerFolder = _HpicfAMPServerFolder_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 4),
    _HpicfAMPServerFolder_Type()
)
hpicfAMPServerFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerFolder.setStatus("current")


class _HpicfAMPServerSecret_Type(OctetString):
    """Custom type hpicfAMPServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfAMPServerSecret_Type.__name__ = "OctetString"
_HpicfAMPServerSecret_Object = MibScalar
hpicfAMPServerSecret = _HpicfAMPServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 5),
    _HpicfAMPServerSecret_Type()
)
hpicfAMPServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerSecret.setStatus("current")


class _HpicfAMPServerConfigStatus_Type(Integer32):
    """Custom type hpicfAMPServerConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("notConfigured", 2))
    )


_HpicfAMPServerConfigStatus_Type.__name__ = "Integer32"
_HpicfAMPServerConfigStatus_Object = MibScalar
hpicfAMPServerConfigStatus = _HpicfAMPServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 6),
    _HpicfAMPServerConfigStatus_Type()
)
hpicfAMPServerConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAMPServerConfigStatus.setStatus("current")
_HpicfAMPServerConformance_ObjectIdentity = ObjectIdentity
hpicfAMPServerConformance = _HpicfAMPServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2)
)
_HpicfAMPServerMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfAMPServerMIBCompliances = _HpicfAMPServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1)
)
_HpicfAMPServerMIBGroups_ObjectIdentity = ObjectIdentity
hpicfAMPServerMIBGroups = _HpicfAMPServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2)
)
_HpicfArubaVPNObjects_ObjectIdentity = ObjectIdentity
hpicfArubaVPNObjects = _HpicfArubaVPNObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3)
)
_HpicfArubaVPNTable_Object = MibTable
hpicfArubaVPNTable = _HpicfArubaVPNTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfArubaVPNTable.setStatus("current")
_HpicfArubaVPNEntry_Object = MibTableRow
hpicfArubaVPNEntry = _HpicfArubaVPNEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1)
)
hpicfArubaVPNEntry.setIndexNames(
    (0, "HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIndex"),
)
if mibBuilder.loadTexts:
    hpicfArubaVPNEntry.setStatus("current")
_HpicfArubaVPNIndex_Type = HpicfArubaVPNType
_HpicfArubaVPNIndex_Object = MibTableColumn
hpicfArubaVPNIndex = _HpicfArubaVPNIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 1),
    _HpicfArubaVPNIndex_Type()
)
hpicfArubaVPNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfArubaVPNIndex.setStatus("current")
_HpicfArubaVPNRowStatus_Type = RowStatus
_HpicfArubaVPNRowStatus_Object = MibTableColumn
hpicfArubaVPNRowStatus = _HpicfArubaVPNRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 2),
    _HpicfArubaVPNRowStatus_Type()
)
hpicfArubaVPNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfArubaVPNRowStatus.setStatus("current")
_HpicfArubaVPNIPType_Type = InetAddressType
_HpicfArubaVPNIPType_Object = MibTableColumn
hpicfArubaVPNIPType = _HpicfArubaVPNIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 3),
    _HpicfArubaVPNIPType_Type()
)
hpicfArubaVPNIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNIPType.setStatus("current")
_HpicfArubaVPNIP_Type = InetAddress
_HpicfArubaVPNIP_Object = MibTableColumn
hpicfArubaVPNIP = _HpicfArubaVPNIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 4),
    _HpicfArubaVPNIP_Type()
)
hpicfArubaVPNIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNIP.setStatus("current")
_HpicfArubaVPNTos_Type = Integer32
_HpicfArubaVPNTos_Object = MibTableColumn
hpicfArubaVPNTos = _HpicfArubaVPNTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 5),
    _HpicfArubaVPNTos_Type()
)
hpicfArubaVPNTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNTos.setStatus("current")
_HpicfArubaVPNTtl_Type = Integer32
_HpicfArubaVPNTtl_Object = MibTableColumn
hpicfArubaVPNTtl = _HpicfArubaVPNTtl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 6),
    _HpicfArubaVPNTtl_Type()
)
hpicfArubaVPNTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNTtl.setStatus("current")
_HpicfArubaVPNBkpIPType_Type = InetAddressType
_HpicfArubaVPNBkpIPType_Object = MibTableColumn
hpicfArubaVPNBkpIPType = _HpicfArubaVPNBkpIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 7),
    _HpicfArubaVPNBkpIPType_Type()
)
hpicfArubaVPNBkpIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNBkpIPType.setStatus("current")
_HpicfArubaVPNBkpIP_Type = InetAddress
_HpicfArubaVPNBkpIP_Object = MibTableColumn
hpicfArubaVPNBkpIP = _HpicfArubaVPNBkpIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 8),
    _HpicfArubaVPNBkpIP_Type()
)
hpicfArubaVPNBkpIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNBkpIP.setStatus("current")
_HpicfArubaVPNDefaultGateway_ObjectIdentity = ObjectIdentity
hpicfArubaVPNDefaultGateway = _HpicfArubaVPNDefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4)
)
_HpicfArubaVPNGateway_Type = TruthValue
_HpicfArubaVPNGateway_Object = MibScalar
hpicfArubaVPNGateway = _HpicfArubaVPNGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4, 1),
    _HpicfArubaVPNGateway_Type()
)
hpicfArubaVPNGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArubaVPNGateway.setStatus("current")

# Managed Objects groups

hpicfAMPServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 1)
)
hpicfAMPServerConfigGroup.setObjects(
      *(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIP"),
        ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIPType"),
        ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerGroup"),
        ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerFolder"),
        ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerSecret"),
        ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigStatus"))
)
if mibBuilder.loadTexts:
    hpicfAMPServerConfigGroup.setStatus("current")

hpicfArubaVPNConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 2)
)
hpicfArubaVPNConfigGroup.setObjects(
      *(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"))
)
if mibBuilder.loadTexts:
    hpicfArubaVPNConfigGroup.setStatus("deprecated")

hpicfDefaultGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 3)
)
hpicfDefaultGatewayGroup.setObjects(
    ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNGateway")
)
if mibBuilder.loadTexts:
    hpicfDefaultGatewayGroup.setStatus("current")

hpicfArubaVPNConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 4)
)
hpicfArubaVPNConfigGroup1.setObjects(
      *(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIPType"),
        ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIP"))
)
if mibBuilder.loadTexts:
    hpicfArubaVPNConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfAMPServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfAMPServerMIBCompliance.setStatus(
        "deprecated"
    )

hpicfAMPServerMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfAMPServerMIBCompliance1.setStatus(
        "deprecated"
    )

hpicfAMPServerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfAMPServerMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-AMP-SERVER-MIB",
    **{"HpicfArubaVPNType": HpicfArubaVPNType,
       "hpicfAMPServerMIB": hpicfAMPServerMIB,
       "hpicfAMPServerObjects": hpicfAMPServerObjects,
       "hpicfAMPServerIPType": hpicfAMPServerIPType,
       "hpicfAMPServerIP": hpicfAMPServerIP,
       "hpicfAMPServerGroup": hpicfAMPServerGroup,
       "hpicfAMPServerFolder": hpicfAMPServerFolder,
       "hpicfAMPServerSecret": hpicfAMPServerSecret,
       "hpicfAMPServerConfigStatus": hpicfAMPServerConfigStatus,
       "hpicfAMPServerConformance": hpicfAMPServerConformance,
       "hpicfAMPServerMIBCompliances": hpicfAMPServerMIBCompliances,
       "hpicfAMPServerMIBCompliance": hpicfAMPServerMIBCompliance,
       "hpicfAMPServerMIBCompliance1": hpicfAMPServerMIBCompliance1,
       "hpicfAMPServerMIBCompliance2": hpicfAMPServerMIBCompliance2,
       "hpicfAMPServerMIBGroups": hpicfAMPServerMIBGroups,
       "hpicfAMPServerConfigGroup": hpicfAMPServerConfigGroup,
       "hpicfArubaVPNConfigGroup": hpicfArubaVPNConfigGroup,
       "hpicfDefaultGatewayGroup": hpicfDefaultGatewayGroup,
       "hpicfArubaVPNConfigGroup1": hpicfArubaVPNConfigGroup1,
       "hpicfArubaVPNObjects": hpicfArubaVPNObjects,
       "hpicfArubaVPNTable": hpicfArubaVPNTable,
       "hpicfArubaVPNEntry": hpicfArubaVPNEntry,
       "hpicfArubaVPNIndex": hpicfArubaVPNIndex,
       "hpicfArubaVPNRowStatus": hpicfArubaVPNRowStatus,
       "hpicfArubaVPNIPType": hpicfArubaVPNIPType,
       "hpicfArubaVPNIP": hpicfArubaVPNIP,
       "hpicfArubaVPNTos": hpicfArubaVPNTos,
       "hpicfArubaVPNTtl": hpicfArubaVPNTtl,
       "hpicfArubaVPNBkpIPType": hpicfArubaVPNBkpIPType,
       "hpicfArubaVPNBkpIP": hpicfArubaVPNBkpIP,
       "hpicfArubaVPNDefaultGateway": hpicfArubaVPNDefaultGateway,
       "hpicfArubaVPNGateway": hpicfArubaVPNGateway}
)
