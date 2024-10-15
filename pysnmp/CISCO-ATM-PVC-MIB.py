# SNMP MIB module (CISCO-ATM-PVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-PVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:54 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoAtmPvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94)
)
ciscoAtmPvcMIB.setRevisions(
        ("2002-04-11 00:00",
         "1997-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmPvcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmPvcMIBObjects = _CiscoAtmPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1)
)
_CiscoAtmPvcCreateBindGroup_ObjectIdentity = ObjectIdentity
ciscoAtmPvcCreateBindGroup = _CiscoAtmPvcCreateBindGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1)
)
_CapvcTable_Object = MibTable
capvcTable = _CapvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1)
)
if mibBuilder.loadTexts:
    capvcTable.setStatus("current")
_CapvcEntry_Object = MibTableRow
capvcEntry = _CapvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1)
)
capvcEntry.setIndexNames(
    (0, "CISCO-ATM-PVC-MIB", "capvcPort"),
    (0, "CISCO-ATM-PVC-MIB", "capvcVPI"),
    (0, "CISCO-ATM-PVC-MIB", "capvcVCI"),
)
if mibBuilder.loadTexts:
    capvcEntry.setStatus("current")
_CapvcPort_Type = Unsigned32
_CapvcPort_Object = MibTableColumn
capvcPort = _CapvcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 1),
    _CapvcPort_Type()
)
capvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capvcPort.setStatus("current")


class _CapvcVPI_Type(Unsigned32):
    """Custom type capvcVPI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CapvcVPI_Type.__name__ = "Unsigned32"
_CapvcVPI_Object = MibTableColumn
capvcVPI = _CapvcVPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 2),
    _CapvcVPI_Type()
)
capvcVPI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capvcVPI.setStatus("current")


class _CapvcVCI_Type(Unsigned32):
    """Custom type capvcVCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CapvcVCI_Type.__name__ = "Unsigned32"
_CapvcVCI_Object = MibTableColumn
capvcVCI = _CapvcVCI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 3),
    _CapvcVCI_Type()
)
capvcVCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capvcVCI.setStatus("current")


class _CapvcVCD_Type(Unsigned32):
    """Custom type capvcVCD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CapvcVCD_Type.__name__ = "Unsigned32"
_CapvcVCD_Object = MibTableColumn
capvcVCD = _CapvcVCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 4),
    _CapvcVCD_Type()
)
capvcVCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capvcVCD.setStatus("current")


class _CapvcType_Type(Integer32):
    """Custom type capvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal5snap", 1),
          ("ilmi", 2),
          ("qsaal", 3))
    )


_CapvcType_Type.__name__ = "Integer32"
_CapvcType_Object = MibTableColumn
capvcType = _CapvcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 5),
    _CapvcType_Type()
)
capvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcType.setStatus("current")


class _CapvcPCR_Type(Unsigned32):
    """Custom type capvcPCR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000),
    )


_CapvcPCR_Type.__name__ = "Unsigned32"
_CapvcPCR_Object = MibTableColumn
capvcPCR = _CapvcPCR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 6),
    _CapvcPCR_Type()
)
capvcPCR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcPCR.setStatus("current")
if mibBuilder.loadTexts:
    capvcPCR.setUnits("kbps")


class _CapvcOAM_Type(TruthValue):
    """Custom type capvcOAM based on TruthValue"""


_CapvcOAM_Object = MibTableColumn
capvcOAM = _CapvcOAM_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 7),
    _CapvcOAM_Type()
)
capvcOAM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcOAM.setStatus("current")


class _CapvcFrequency_Type(Unsigned32):
    """Custom type capvcFrequency based on Unsigned32"""
    defaultValue = 10


_CapvcFrequency_Object = MibTableColumn
capvcFrequency = _CapvcFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 8),
    _CapvcFrequency_Type()
)
capvcFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcFrequency.setStatus("current")
if mibBuilder.loadTexts:
    capvcFrequency.setUnits("seconds")


class _CapvcVlanId_Type(Unsigned32):
    """Custom type capvcVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CapvcVlanId_Type.__name__ = "Unsigned32"
_CapvcVlanId_Object = MibTableColumn
capvcVlanId = _CapvcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 9),
    _CapvcVlanId_Type()
)
capvcVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcVlanId.setStatus("current")
_CapvcRowStatus_Type = RowStatus
_CapvcRowStatus_Object = MibTableColumn
capvcRowStatus = _CapvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 1, 1, 1, 1, 10),
    _CapvcRowStatus_Type()
)
capvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capvcRowStatus.setStatus("current")
_CiscoAtmPvcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmPvcMIBConformance = _CiscoAtmPvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 3)
)
_CiscoAtmPvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmPvcMIBCompliances = _CiscoAtmPvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 3, 1)
)
_CiscoAtmPvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmPvcMIBGroups = _CiscoAtmPvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 3, 2)
)

# Managed Objects groups

ciscoAtmPvcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 3, 2, 1)
)
ciscoAtmPvcMIBGroup.setObjects(
      *(("CISCO-ATM-PVC-MIB", "capvcVCD"),
        ("CISCO-ATM-PVC-MIB", "capvcType"),
        ("CISCO-ATM-PVC-MIB", "capvcPCR"),
        ("CISCO-ATM-PVC-MIB", "capvcOAM"),
        ("CISCO-ATM-PVC-MIB", "capvcFrequency"),
        ("CISCO-ATM-PVC-MIB", "capvcVlanId"),
        ("CISCO-ATM-PVC-MIB", "capvcRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmPvcMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmPvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 94, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmPvcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-PVC-MIB",
    **{"ciscoAtmPvcMIB": ciscoAtmPvcMIB,
       "ciscoAtmPvcMIBObjects": ciscoAtmPvcMIBObjects,
       "ciscoAtmPvcCreateBindGroup": ciscoAtmPvcCreateBindGroup,
       "capvcTable": capvcTable,
       "capvcEntry": capvcEntry,
       "capvcPort": capvcPort,
       "capvcVPI": capvcVPI,
       "capvcVCI": capvcVCI,
       "capvcVCD": capvcVCD,
       "capvcType": capvcType,
       "capvcPCR": capvcPCR,
       "capvcOAM": capvcOAM,
       "capvcFrequency": capvcFrequency,
       "capvcVlanId": capvcVlanId,
       "capvcRowStatus": capvcRowStatus,
       "ciscoAtmPvcMIBConformance": ciscoAtmPvcMIBConformance,
       "ciscoAtmPvcMIBCompliances": ciscoAtmPvcMIBCompliances,
       "ciscoAtmPvcMIBCompliance": ciscoAtmPvcMIBCompliance,
       "ciscoAtmPvcMIBGroups": ciscoAtmPvcMIBGroups,
       "ciscoAtmPvcMIBGroup": ciscoAtmPvcMIBGroup}
)
