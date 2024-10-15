# SNMP MIB module (UBNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UBNT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:17 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ubntMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1)
)
ubntMIB.setRevisions(
        ("2014-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ubnt_ObjectIdentity = ObjectIdentity
ubnt = _Ubnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112)
)
_UbntORTable_Object = MibTable
ubntORTable = _UbntORTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1)
)
if mibBuilder.loadTexts:
    ubntORTable.setStatus("current")
_UbntOREntry_Object = MibTableRow
ubntOREntry = _UbntOREntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1)
)
ubntOREntry.setIndexNames(
    (0, "UBNT-MIB", "ubntORIndex"),
)
if mibBuilder.loadTexts:
    ubntOREntry.setStatus("current")


class _UbntORIndex_Type(Integer32):
    """Custom type ubntORIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntORIndex_Type.__name__ = "Integer32"
_UbntORIndex_Object = MibTableColumn
ubntORIndex = _UbntORIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 1),
    _UbntORIndex_Type()
)
ubntORIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntORIndex.setStatus("current")
_UbntORID_Type = ObjectIdentifier
_UbntORID_Object = MibTableColumn
ubntORID = _UbntORID_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 2),
    _UbntORID_Type()
)
ubntORID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORID.setStatus("current")
_UbntORDescr_Type = DisplayString
_UbntORDescr_Object = MibTableColumn
ubntORDescr = _UbntORDescr_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 1, 1, 3),
    _UbntORDescr_Type()
)
ubntORDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntORDescr.setStatus("current")
_UbntSnmpInfo_ObjectIdentity = ObjectIdentity
ubntSnmpInfo = _UbntSnmpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2)
)
_UbntSnmpGroups_ObjectIdentity = ObjectIdentity
ubntSnmpGroups = _UbntSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1)
)
_UbntAirosGroups_ObjectIdentity = ObjectIdentity
ubntAirosGroups = _UbntAirosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2)
)
_UbntAirFiberGroups_ObjectIdentity = ObjectIdentity
ubntAirFiberGroups = _UbntAirFiberGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 3)
)
_UbntEdgeMaxGroups_ObjectIdentity = ObjectIdentity
ubntEdgeMaxGroups = _UbntEdgeMaxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 4)
)
_UbntUniFiGroups_ObjectIdentity = ObjectIdentity
ubntUniFiGroups = _UbntUniFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 5)
)
_UbntAirVisionGroups_ObjectIdentity = ObjectIdentity
ubntAirVisionGroups = _UbntAirVisionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 6)
)
_UbntMFiGroups_ObjectIdentity = ObjectIdentity
ubntMFiGroups = _UbntMFiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 7)
)
_UbntUniTelGroups_ObjectIdentity = ObjectIdentity
ubntUniTelGroups = _UbntUniTelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 8)
)
_UbntAirFIBER_ObjectIdentity = ObjectIdentity
ubntAirFIBER = _UbntAirFIBER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 3)
)
_UbntEdgeMax_ObjectIdentity = ObjectIdentity
ubntEdgeMax = _UbntEdgeMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 5)
)
_UbntUniFi_ObjectIdentity = ObjectIdentity
ubntUniFi = _UbntUniFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 6)
)
_UbntAirVision_ObjectIdentity = ObjectIdentity
ubntAirVision = _UbntAirVision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 7)
)
_UbntMFi_ObjectIdentity = ObjectIdentity
ubntMFi = _UbntMFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 8)
)
_UbntUniTel_ObjectIdentity = ObjectIdentity
ubntUniTel = _UbntUniTel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 9)
)

# Managed Objects groups

ubntORInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 1)
)
ubntORInfoGroup.setObjects(
      *(("UBNT-MIB", "ubntORID"),
        ("UBNT-MIB", "ubntORDescr"))
)
if mibBuilder.loadTexts:
    ubntORInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubntORCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ubntORCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-MIB",
    **{"ubnt": ubnt,
       "ubntMIB": ubntMIB,
       "ubntORTable": ubntORTable,
       "ubntOREntry": ubntOREntry,
       "ubntORIndex": ubntORIndex,
       "ubntORID": ubntORID,
       "ubntORDescr": ubntORDescr,
       "ubntSnmpInfo": ubntSnmpInfo,
       "ubntSnmpGroups": ubntSnmpGroups,
       "ubntORInfoGroup": ubntORInfoGroup,
       "ubntORCompliance": ubntORCompliance,
       "ubntAirosGroups": ubntAirosGroups,
       "ubntAirFiberGroups": ubntAirFiberGroups,
       "ubntEdgeMaxGroups": ubntEdgeMaxGroups,
       "ubntUniFiGroups": ubntUniFiGroups,
       "ubntAirVisionGroups": ubntAirVisionGroups,
       "ubntMFiGroups": ubntMFiGroups,
       "ubntUniTelGroups": ubntUniTelGroups,
       "ubntAirFIBER": ubntAirFIBER,
       "ubntEdgeMax": ubntEdgeMax,
       "ubntUniFi": ubntUniFi,
       "ubntAirVision": ubntAirVision,
       "ubntMFi": ubntMFi,
       "ubntUniTel": ubntUniTel}
)
