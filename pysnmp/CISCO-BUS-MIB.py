# SNMP MIB module (CISCO-BUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:27 2024
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

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoBusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoVpiInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )



class CiscoVciInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBusMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBusMIBObjects = _CiscoBusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1)
)
_BusTable_Object = MibTable
busTable = _BusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1)
)
if mibBuilder.loadTexts:
    busTable.setStatus("current")
_BusEntry_Object = MibTableRow
busEntry = _BusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1)
)
busEntry.setIndexNames(
    (0, "CISCO-BUS-MIB", "busElanName"),
    (0, "CISCO-BUS-MIB", "busIndex"),
)
if mibBuilder.loadTexts:
    busEntry.setStatus("current")


class _BusElanName_Type(DisplayString):
    """Custom type busElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BusElanName_Type.__name__ = "DisplayString"
_BusElanName_Object = MibTableColumn
busElanName = _BusElanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 1),
    _BusElanName_Type()
)
busElanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busElanName.setStatus("current")


class _BusIndex_Type(Integer32):
    """Custom type busIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BusIndex_Type.__name__ = "Integer32"
_BusIndex_Object = MibTableColumn
busIndex = _BusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 2),
    _BusIndex_Type()
)
busIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busIndex.setStatus("current")
_BusAtmAddrSpec_Type = AtmLaneAddress
_BusAtmAddrSpec_Object = MibTableColumn
busAtmAddrSpec = _BusAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 3),
    _BusAtmAddrSpec_Type()
)
busAtmAddrSpec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busAtmAddrSpec.setStatus("current")


class _BusAtmAddrMask_Type(OctetString):
    """Custom type busAtmAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_BusAtmAddrMask_Type.__name__ = "OctetString"
_BusAtmAddrMask_Object = MibTableColumn
busAtmAddrMask = _BusAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 4),
    _BusAtmAddrMask_Type()
)
busAtmAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busAtmAddrMask.setStatus("current")
_BusAtmAddrActl_Type = AtmLaneAddress
_BusAtmAddrActl_Object = MibTableColumn
busAtmAddrActl = _BusAtmAddrActl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 5),
    _BusAtmAddrActl_Type()
)
busAtmAddrActl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busAtmAddrActl.setStatus("current")
_BusIfIndex_Type = Integer32
_BusIfIndex_Object = MibTableColumn
busIfIndex = _BusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 6),
    _BusIfIndex_Type()
)
busIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busIfIndex.setStatus("current")
_BusSubIfNum_Type = Integer32
_BusSubIfNum_Object = MibTableColumn
busSubIfNum = _BusSubIfNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 7),
    _BusSubIfNum_Type()
)
busSubIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busSubIfNum.setStatus("current")
_BusUpTime_Type = TimeStamp
_BusUpTime_Object = MibTableColumn
busUpTime = _BusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 8),
    _BusUpTime_Type()
)
busUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busUpTime.setStatus("current")


class _BusLanType_Type(Integer32):
    """Custom type busLanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot3", 1),
          ("dot5", 2))
    )


_BusLanType_Type.__name__ = "Integer32"
_BusLanType_Object = MibTableColumn
busLanType = _BusLanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 9),
    _BusLanType_Type()
)
busLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busLanType.setStatus("current")


class _BusMaxFrm_Type(Integer32):
    """Custom type busMaxFrm based on Integer32"""
    defaultValue = 1516

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1516,
              4544,
              9234,
              18190)
        )
    )
    namedValues = NamedValues(
        *(("dot3", 1516),
          ("rfc1626", 9234),
          ("tr16Mb", 18190),
          ("tr4Mb", 4544))
    )


_BusMaxFrm_Type.__name__ = "Integer32"
_BusMaxFrm_Object = MibTableColumn
busMaxFrm = _BusMaxFrm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 10),
    _BusMaxFrm_Type()
)
busMaxFrm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busMaxFrm.setStatus("current")


class _BusMaxFrmAge_Type(Integer32):
    """Custom type busMaxFrmAge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BusMaxFrmAge_Type.__name__ = "Integer32"
_BusMaxFrmAge_Object = MibTableColumn
busMaxFrmAge = _BusMaxFrmAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 11),
    _BusMaxFrmAge_Type()
)
busMaxFrmAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busMaxFrmAge.setStatus("current")
if mibBuilder.loadTexts:
    busMaxFrmAge.setUnits("seconds")
_BusOutFwdOctets_Type = Counter32
_BusOutFwdOctets_Object = MibTableColumn
busOutFwdOctets = _BusOutFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 12),
    _BusOutFwdOctets_Type()
)
busOutFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busOutFwdOctets.setStatus("current")
_BusOutFwdUcastFrms_Type = Counter32
_BusOutFwdUcastFrms_Object = MibTableColumn
busOutFwdUcastFrms = _BusOutFwdUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 13),
    _BusOutFwdUcastFrms_Type()
)
busOutFwdUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busOutFwdUcastFrms.setStatus("current")
_BusOutFwdNUcastFrms_Type = Counter32
_BusOutFwdNUcastFrms_Object = MibTableColumn
busOutFwdNUcastFrms = _BusOutFwdNUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 14),
    _BusOutFwdNUcastFrms_Type()
)
busOutFwdNUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busOutFwdNUcastFrms.setStatus("current")
_BusFrmTimeOuts_Type = Counter32
_BusFrmTimeOuts_Object = MibTableColumn
busFrmTimeOuts = _BusFrmTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 15),
    _BusFrmTimeOuts_Type()
)
busFrmTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busFrmTimeOuts.setStatus("current")
_BusMultiFwdVpi_Type = CiscoVpiInteger
_BusMultiFwdVpi_Object = MibTableColumn
busMultiFwdVpi = _BusMultiFwdVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 16),
    _BusMultiFwdVpi_Type()
)
busMultiFwdVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busMultiFwdVpi.setStatus("current")
_BusMultiFwdVci_Type = CiscoVciInteger
_BusMultiFwdVci_Object = MibTableColumn
busMultiFwdVci = _BusMultiFwdVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 17),
    _BusMultiFwdVci_Type()
)
busMultiFwdVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busMultiFwdVci.setStatus("current")


class _BusOperStatus_Type(Integer32):
    """Custom type busOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_BusOperStatus_Type.__name__ = "Integer32"
_BusOperStatus_Object = MibTableColumn
busOperStatus = _BusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 18),
    _BusOperStatus_Type()
)
busOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busOperStatus.setStatus("current")


class _BusAdminStatus_Type(Integer32):
    """Custom type busAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_BusAdminStatus_Type.__name__ = "Integer32"
_BusAdminStatus_Object = MibTableColumn
busAdminStatus = _BusAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 19),
    _BusAdminStatus_Type()
)
busAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busAdminStatus.setStatus("current")
_BusStatus_Type = RowStatus
_BusStatus_Object = MibTableColumn
busStatus = _BusStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 1, 1, 20),
    _BusStatus_Type()
)
busStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    busStatus.setStatus("current")
_BusClientTable_Object = MibTable
busClientTable = _BusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2)
)
if mibBuilder.loadTexts:
    busClientTable.setStatus("current")
_BusClientEntry_Object = MibTableRow
busClientEntry = _BusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1)
)
busClientEntry.setIndexNames(
    (0, "CISCO-BUS-MIB", "busElanName"),
    (0, "CISCO-BUS-MIB", "busIndex"),
    (0, "CISCO-BUS-MIB", "busClientId"),
)
if mibBuilder.loadTexts:
    busClientEntry.setStatus("current")
_BusClientId_Type = Integer32
_BusClientId_Object = MibTableColumn
busClientId = _BusClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1, 1),
    _BusClientId_Type()
)
busClientId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busClientId.setStatus("current")
_BusClientIfIndex_Type = Integer32
_BusClientIfIndex_Object = MibTableColumn
busClientIfIndex = _BusClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1, 2),
    _BusClientIfIndex_Type()
)
busClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busClientIfIndex.setStatus("current")
_BusClientMSendVpi_Type = CiscoVpiInteger
_BusClientMSendVpi_Object = MibTableColumn
busClientMSendVpi = _BusClientMSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1, 3),
    _BusClientMSendVpi_Type()
)
busClientMSendVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busClientMSendVpi.setStatus("current")
_BusClientMSendVci_Type = CiscoVciInteger
_BusClientMSendVci_Object = MibTableColumn
busClientMSendVci = _BusClientMSendVci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1, 4),
    _BusClientMSendVci_Type()
)
busClientMSendVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busClientMSendVci.setStatus("current")
_BusClientAtmAddress_Type = AtmLaneAddress
_BusClientAtmAddress_Object = MibTableColumn
busClientAtmAddress = _BusClientAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 1, 2, 1, 5),
    _BusClientAtmAddress_Type()
)
busClientAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busClientAtmAddress.setStatus("current")
_CiscoBusMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBusMIBConformance = _CiscoBusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2)
)
_CiscoBusMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBusMIBGroups = _CiscoBusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 1)
)
_CiscoBusMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBusMIBCompliances = _CiscoBusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 2)
)

# Managed Objects groups

ciscoBusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 1, 1)
)
ciscoBusGroup.setObjects(
      *(("CISCO-BUS-MIB", "busAtmAddrSpec"),
        ("CISCO-BUS-MIB", "busAtmAddrMask"),
        ("CISCO-BUS-MIB", "busAtmAddrActl"),
        ("CISCO-BUS-MIB", "busIfIndex"),
        ("CISCO-BUS-MIB", "busUpTime"),
        ("CISCO-BUS-MIB", "busLanType"),
        ("CISCO-BUS-MIB", "busMaxFrm"),
        ("CISCO-BUS-MIB", "busMaxFrmAge"),
        ("CISCO-BUS-MIB", "busOutFwdOctets"),
        ("CISCO-BUS-MIB", "busOutFwdUcastFrms"),
        ("CISCO-BUS-MIB", "busOutFwdNUcastFrms"),
        ("CISCO-BUS-MIB", "busFrmTimeOuts"),
        ("CISCO-BUS-MIB", "busMultiFwdVpi"),
        ("CISCO-BUS-MIB", "busMultiFwdVci"),
        ("CISCO-BUS-MIB", "busOperStatus"),
        ("CISCO-BUS-MIB", "busAdminStatus"),
        ("CISCO-BUS-MIB", "busStatus"))
)
if mibBuilder.loadTexts:
    ciscoBusGroup.setStatus("current")

ciscoBusSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 1, 2)
)
ciscoBusSubIfGroup.setObjects(
    ("CISCO-BUS-MIB", "busSubIfNum")
)
if mibBuilder.loadTexts:
    ciscoBusSubIfGroup.setStatus("current")

ciscoBusClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 1, 3)
)
ciscoBusClientGroup.setObjects(
      *(("CISCO-BUS-MIB", "busClientIfIndex"),
        ("CISCO-BUS-MIB", "busClientMSendVpi"),
        ("CISCO-BUS-MIB", "busClientMSendVci"),
        ("CISCO-BUS-MIB", "busClientAtmAddress"))
)
if mibBuilder.loadTexts:
    ciscoBusClientGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBusMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoBusMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BUS-MIB",
    **{"CiscoVpiInteger": CiscoVpiInteger,
       "CiscoVciInteger": CiscoVciInteger,
       "ciscoBusMIB": ciscoBusMIB,
       "ciscoBusMIBObjects": ciscoBusMIBObjects,
       "busTable": busTable,
       "busEntry": busEntry,
       "busElanName": busElanName,
       "busIndex": busIndex,
       "busAtmAddrSpec": busAtmAddrSpec,
       "busAtmAddrMask": busAtmAddrMask,
       "busAtmAddrActl": busAtmAddrActl,
       "busIfIndex": busIfIndex,
       "busSubIfNum": busSubIfNum,
       "busUpTime": busUpTime,
       "busLanType": busLanType,
       "busMaxFrm": busMaxFrm,
       "busMaxFrmAge": busMaxFrmAge,
       "busOutFwdOctets": busOutFwdOctets,
       "busOutFwdUcastFrms": busOutFwdUcastFrms,
       "busOutFwdNUcastFrms": busOutFwdNUcastFrms,
       "busFrmTimeOuts": busFrmTimeOuts,
       "busMultiFwdVpi": busMultiFwdVpi,
       "busMultiFwdVci": busMultiFwdVci,
       "busOperStatus": busOperStatus,
       "busAdminStatus": busAdminStatus,
       "busStatus": busStatus,
       "busClientTable": busClientTable,
       "busClientEntry": busClientEntry,
       "busClientId": busClientId,
       "busClientIfIndex": busClientIfIndex,
       "busClientMSendVpi": busClientMSendVpi,
       "busClientMSendVci": busClientMSendVci,
       "busClientAtmAddress": busClientAtmAddress,
       "ciscoBusMIBConformance": ciscoBusMIBConformance,
       "ciscoBusMIBGroups": ciscoBusMIBGroups,
       "ciscoBusGroup": ciscoBusGroup,
       "ciscoBusSubIfGroup": ciscoBusSubIfGroup,
       "ciscoBusClientGroup": ciscoBusClientGroup,
       "ciscoBusMIBCompliances": ciscoBusMIBCompliances,
       "ciscoBusMIBCompliance": ciscoBusMIBCompliance}
)
