# SNMP MIB module (CISCO-DMN-DSG-MPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-MPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:28 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGMPE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26)
)
ciscoDSGMPE.setRevisions(
        ("2010-08-30 11:00",
         "2010-05-07 06:30",
         "2010-05-03 11:00",
         "2010-04-12 06:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpeTable_ObjectIdentity = ObjectIdentity
mpeTable = _MpeTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2)
)
_MpeConfigTable_Object = MibTable
mpeConfigTable = _MpeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1)
)
if mibBuilder.loadTexts:
    mpeConfigTable.setStatus("current")
_MpeConfigEntry_Object = MibTableRow
mpeConfigEntry = _MpeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1)
)
mpeConfigEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MPE-MIB", "mpeConfigPortID"),
)
if mibBuilder.loadTexts:
    mpeConfigEntry.setStatus("current")


class _MpeConfigPortID_Type(Integer32):
    """Custom type mpeConfigPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MpeConfigPortID_Type.__name__ = "Integer32"
_MpeConfigPortID_Object = MibTableColumn
mpeConfigPortID = _MpeConfigPortID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 1),
    _MpeConfigPortID_Type()
)
mpeConfigPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpeConfigPortID.setStatus("current")


class _MpeConfigForwarding_Type(Integer32):
    """Custom type mpeConfigForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 2),
          ("forwardFilteredList", 3),
          ("forwardNone", 1))
    )


_MpeConfigForwarding_Type.__name__ = "Integer32"
_MpeConfigForwarding_Object = MibTableColumn
mpeConfigForwarding = _MpeConfigForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 2),
    _MpeConfigForwarding_Type()
)
mpeConfigForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeConfigForwarding.setStatus("current")


class _MpeConfigIGMP_Type(Integer32):
    """Custom type mpeConfigIGMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MpeConfigIGMP_Type.__name__ = "Integer32"
_MpeConfigIGMP_Object = MibTableColumn
mpeConfigIGMP = _MpeConfigIGMP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 3),
    _MpeConfigIGMP_Type()
)
mpeConfigIGMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeConfigIGMP.setStatus("current")


class _MpeConfigRIP_Type(Integer32):
    """Custom type mpeConfigRIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MpeConfigRIP_Type.__name__ = "Integer32"
_MpeConfigRIP_Object = MibTableColumn
mpeConfigRIP = _MpeConfigRIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 4),
    _MpeConfigRIP_Type()
)
mpeConfigRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeConfigRIP.setStatus("current")


class _MpeMultipacket_Type(Integer32):
    """Custom type mpeMultipacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              24)
        )
    )
    namedValues = NamedValues(
        *(("higherBitRate", 24),
          ("lowerJitter", 1))
    )


_MpeMultipacket_Type.__name__ = "Integer32"
_MpeMultipacket_Object = MibTableColumn
mpeMultipacket = _MpeMultipacket_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 1, 1, 5),
    _MpeMultipacket_Type()
)
mpeMultipacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeMultipacket.setStatus("current")
_UnicastTable_Object = MibTable
unicastTable = _UnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2)
)
if mibBuilder.loadTexts:
    unicastTable.setStatus("current")
_UnicastEntry_Object = MibTableRow
unicastEntry = _UnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1)
)
unicastEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MPE-MIB", "unicastIdx"),
)
if mibBuilder.loadTexts:
    unicastEntry.setStatus("current")


class _UnicastIdx_Type(Integer32):
    """Custom type unicastIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_UnicastIdx_Type.__name__ = "Integer32"
_UnicastIdx_Object = MibTableColumn
unicastIdx = _UnicastIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 1),
    _UnicastIdx_Type()
)
unicastIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unicastIdx.setStatus("current")
_UnicastRoute_Type = IpAddress
_UnicastRoute_Object = MibTableColumn
unicastRoute = _UnicastRoute_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 2),
    _UnicastRoute_Type()
)
unicastRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unicastRoute.setStatus("current")


class _UnicastMask_Type(Integer32):
    """Custom type unicastMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 32),
    )


_UnicastMask_Type.__name__ = "Integer32"
_UnicastMask_Object = MibTableColumn
unicastMask = _UnicastMask_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 3),
    _UnicastMask_Type()
)
unicastMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unicastMask.setStatus("current")


class _UnicastOutputPortID_Type(Integer32):
    """Custom type unicastOutputPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UnicastOutputPortID_Type.__name__ = "Integer32"
_UnicastOutputPortID_Object = MibTableColumn
unicastOutputPortID = _UnicastOutputPortID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 4),
    _UnicastOutputPortID_Type()
)
unicastOutputPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unicastOutputPortID.setStatus("current")
_UnicastGatewayAddr_Type = IpAddress
_UnicastGatewayAddr_Object = MibTableColumn
unicastGatewayAddr = _UnicastGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 5),
    _UnicastGatewayAddr_Type()
)
unicastGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unicastGatewayAddr.setStatus("current")
_UnicastRowStatus_Type = RowStatus
_UnicastRowStatus_Object = MibTableColumn
unicastRowStatus = _UnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 2, 1, 6),
    _UnicastRowStatus_Type()
)
unicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    unicastRowStatus.setStatus("current")
_StaticMulticastTable_Object = MibTable
staticMulticastTable = _StaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3)
)
if mibBuilder.loadTexts:
    staticMulticastTable.setStatus("current")
_StaticMulticastEntry_Object = MibTableRow
staticMulticastEntry = _StaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1)
)
staticMulticastEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MPE-MIB", "staticMulticastIdx"),
)
if mibBuilder.loadTexts:
    staticMulticastEntry.setStatus("current")


class _StaticMulticastIdx_Type(Integer32):
    """Custom type staticMulticastIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StaticMulticastIdx_Type.__name__ = "Integer32"
_StaticMulticastIdx_Object = MibTableColumn
staticMulticastIdx = _StaticMulticastIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 1),
    _StaticMulticastIdx_Type()
)
staticMulticastIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticMulticastIdx.setStatus("current")
_StaticMulticastGroupAddress_Type = IpAddress
_StaticMulticastGroupAddress_Object = MibTableColumn
staticMulticastGroupAddress = _StaticMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 2),
    _StaticMulticastGroupAddress_Type()
)
staticMulticastGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastGroupAddress.setStatus("current")
_StaticMulticastRowstatus_Type = RowStatus
_StaticMulticastRowstatus_Object = MibTableColumn
staticMulticastRowstatus = _StaticMulticastRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 2, 3, 1, 3),
    _StaticMulticastRowstatus_Type()
)
staticMulticastRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastRowstatus.setStatus("current")
_MpeMIBConformance_ObjectIdentity = ObjectIdentity
mpeMIBConformance = _MpeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3)
)
_MpeMIBCompliances_ObjectIdentity = ObjectIdentity
mpeMIBCompliances = _MpeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 1)
)
_MpeMIBGroups_ObjectIdentity = ObjectIdentity
mpeMIBGroups = _MpeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2)
)

# Managed Objects groups

mpeConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 1)
)
mpeConfigGroup.setObjects(
      *(("CISCO-DMN-DSG-MPE-MIB", "mpeConfigForwarding"),
        ("CISCO-DMN-DSG-MPE-MIB", "mpeConfigIGMP"),
        ("CISCO-DMN-DSG-MPE-MIB", "mpeConfigRIP"),
        ("CISCO-DMN-DSG-MPE-MIB", "mpeMultipacket"))
)
if mibBuilder.loadTexts:
    mpeConfigGroup.setStatus("current")

unicastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 2)
)
unicastGroup.setObjects(
      *(("CISCO-DMN-DSG-MPE-MIB", "unicastRoute"),
        ("CISCO-DMN-DSG-MPE-MIB", "unicastMask"),
        ("CISCO-DMN-DSG-MPE-MIB", "unicastOutputPortID"),
        ("CISCO-DMN-DSG-MPE-MIB", "unicastGatewayAddr"),
        ("CISCO-DMN-DSG-MPE-MIB", "unicastRowStatus"))
)
if mibBuilder.loadTexts:
    unicastGroup.setStatus("current")

staticMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 2, 3)
)
staticMulticastGroup.setObjects(
      *(("CISCO-DMN-DSG-MPE-MIB", "staticMulticastGroupAddress"),
        ("CISCO-DMN-DSG-MPE-MIB", "staticMulticastRowstatus"))
)
if mibBuilder.loadTexts:
    staticMulticastGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 26, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mpeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-MPE-MIB",
    **{"ciscoDSGMPE": ciscoDSGMPE,
       "mpeTable": mpeTable,
       "mpeConfigTable": mpeConfigTable,
       "mpeConfigEntry": mpeConfigEntry,
       "mpeConfigPortID": mpeConfigPortID,
       "mpeConfigForwarding": mpeConfigForwarding,
       "mpeConfigIGMP": mpeConfigIGMP,
       "mpeConfigRIP": mpeConfigRIP,
       "mpeMultipacket": mpeMultipacket,
       "unicastTable": unicastTable,
       "unicastEntry": unicastEntry,
       "unicastIdx": unicastIdx,
       "unicastRoute": unicastRoute,
       "unicastMask": unicastMask,
       "unicastOutputPortID": unicastOutputPortID,
       "unicastGatewayAddr": unicastGatewayAddr,
       "unicastRowStatus": unicastRowStatus,
       "staticMulticastTable": staticMulticastTable,
       "staticMulticastEntry": staticMulticastEntry,
       "staticMulticastIdx": staticMulticastIdx,
       "staticMulticastGroupAddress": staticMulticastGroupAddress,
       "staticMulticastRowstatus": staticMulticastRowstatus,
       "mpeMIBConformance": mpeMIBConformance,
       "mpeMIBCompliances": mpeMIBCompliances,
       "mpeCompliance": mpeCompliance,
       "mpeMIBGroups": mpeMIBGroups,
       "mpeConfigGroup": mpeConfigGroup,
       "unicastGroup": unicastGroup,
       "staticMulticastGroup": staticMulticastGroup}
)
