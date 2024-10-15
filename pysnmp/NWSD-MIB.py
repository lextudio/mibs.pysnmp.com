# SNMP MIB module (NWSD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NWSD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:05 2024
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(rsNWSD,) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rsNWSD")

(rndErrorDesc,
 rndErrorSeverity,
 rsServerDispatcher) = mibBuilder.importSymbols(
    "RND-MIB",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsServerDispatcher")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsNWSDProximity_ObjectIdentity = ObjectIdentity
rsNWSDProximity = _RsNWSDProximity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1)
)


class _RsWSDProximityHopsWeight_Type(Integer32):
    """Custom type rsWSDProximityHopsWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityHopsWeight_Type.__name__ = "Integer32"
_RsWSDProximityHopsWeight_Object = MibScalar
rsWSDProximityHopsWeight = _RsWSDProximityHopsWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 1),
    _RsWSDProximityHopsWeight_Type()
)
rsWSDProximityHopsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityHopsWeight.setStatus("mandatory")


class _RsWSDProximityLatencyWeight_Type(Integer32):
    """Custom type rsWSDProximityLatencyWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityLatencyWeight_Type.__name__ = "Integer32"
_RsWSDProximityLatencyWeight_Object = MibScalar
rsWSDProximityLatencyWeight = _RsWSDProximityLatencyWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 2),
    _RsWSDProximityLatencyWeight_Type()
)
rsWSDProximityLatencyWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityLatencyWeight.setStatus("mandatory")


class _RsWSDProximityLoadWeight_Type(Integer32):
    """Custom type rsWSDProximityLoadWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsWSDProximityLoadWeight_Type.__name__ = "Integer32"
_RsWSDProximityLoadWeight_Object = MibScalar
rsWSDProximityLoadWeight = _RsWSDProximityLoadWeight_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 3),
    _RsWSDProximityLoadWeight_Type()
)
rsWSDProximityLoadWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDProximityLoadWeight.setStatus("mandatory")
_RsWSDDNSttl_Type = Integer32
_RsWSDDNSttl_Object = MibScalar
rsWSDDNSttl = _RsWSDDNSttl_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 2),
    _RsWSDDNSttl_Type()
)
rsWSDDNSttl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDDNSttl.setStatus("mandatory")
_RsWSDURLSuperFarmTable_Object = MibTable
rsWSDURLSuperFarmTable = _RsWSDURLSuperFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3)
)
if mibBuilder.loadTexts:
    rsWSDURLSuperFarmTable.setStatus("mandatory")
_RsWSDURLSuperFarmEntry_Object = MibTableRow
rsWSDURLSuperFarmEntry = _RsWSDURLSuperFarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1)
)
rsWSDURLSuperFarmEntry.setIndexNames(
    (0, "NWSD-MIB", "rsWSDURL"),
)
if mibBuilder.loadTexts:
    rsWSDURLSuperFarmEntry.setStatus("mandatory")
_RsWSDURLFarmAddress_Type = IpAddress
_RsWSDURLFarmAddress_Object = MibTableColumn
rsWSDURLFarmAddress = _RsWSDURLFarmAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 1),
    _RsWSDURLFarmAddress_Type()
)
rsWSDURLFarmAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLFarmAddress.setStatus("mandatory")


class _RsWSDURL_Type(DisplayString):
    """Custom type rsWSDURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RsWSDURL_Type.__name__ = "DisplayString"
_RsWSDURL_Object = MibTableColumn
rsWSDURL = _RsWSDURL_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 2),
    _RsWSDURL_Type()
)
rsWSDURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURL.setStatus("mandatory")
_RsWSDURLStatus_Type = RowStatus
_RsWSDURLStatus_Object = MibTableColumn
rsWSDURLStatus = _RsWSDURLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 3),
    _RsWSDURLStatus_Type()
)
rsWSDURLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDURLStatus.setStatus("mandatory")
_RsWSDClientGroupingMask_Type = IpAddress
_RsWSDClientGroupingMask_Object = MibScalar
rsWSDClientGroupingMask = _RsWSDClientGroupingMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 26),
    _RsWSDClientGroupingMask_Type()
)
rsWSDClientGroupingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDClientGroupingMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NWSD-MIB",
    **{"TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "NetNumber": NetNumber,
       "rsNWSDProximity": rsNWSDProximity,
       "rsWSDProximityHopsWeight": rsWSDProximityHopsWeight,
       "rsWSDProximityLatencyWeight": rsWSDProximityLatencyWeight,
       "rsWSDProximityLoadWeight": rsWSDProximityLoadWeight,
       "rsWSDDNSttl": rsWSDDNSttl,
       "rsWSDURLSuperFarmTable": rsWSDURLSuperFarmTable,
       "rsWSDURLSuperFarmEntry": rsWSDURLSuperFarmEntry,
       "rsWSDURLFarmAddress": rsWSDURLFarmAddress,
       "rsWSDURL": rsWSDURL,
       "rsWSDURLStatus": rsWSDURLStatus,
       "rsWSDClientGroupingMask": rsWSDClientGroupingMask}
)
