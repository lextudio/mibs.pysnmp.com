# SNMP MIB module (ENGENIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENGENIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:33 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

engeniusmesh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1)
)
engeniusmesh.setRevisions(
        ("2007-05-02 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Engenius_ObjectIdentity = ObjectIdentity
engenius = _Engenius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125)
)
_NodeConfiguration_ObjectIdentity = ObjectIdentity
nodeConfiguration = _NodeConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2)
)
_NodeConfigurationSignallevel_ObjectIdentity = ObjectIdentity
nodeConfigurationSignallevel = _NodeConfigurationSignallevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30)
)


class _SignallevelExecute_Type(Integer32):
    """Custom type signallevelExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SignallevelExecute_Type.__name__ = "Integer32"
_SignallevelExecute_Object = MibScalar
signallevelExecute = _SignallevelExecute_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 1),
    _SignallevelExecute_Type()
)
signallevelExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelExecute.setStatus("current")
_SignallevelTable_Object = MibTable
signallevelTable = _SignallevelTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2)
)
if mibBuilder.loadTexts:
    signallevelTable.setStatus("current")
_SignallevelTableEntry_Object = MibTableRow
signallevelTableEntry = _SignallevelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1)
)
signallevelTableEntry.setIndexNames(
    (0, "ENGENIUS-CLIENT-MIB", "signallevelTableIndex"),
)
if mibBuilder.loadTexts:
    signallevelTableEntry.setStatus("current")


class _SignallevelTableIndex_Type(Integer32):
    """Custom type signallevelTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SignallevelTableIndex_Type.__name__ = "Integer32"
_SignallevelTableIndex_Object = MibTableColumn
signallevelTableIndex = _SignallevelTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 1),
    _SignallevelTableIndex_Type()
)
signallevelTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    signallevelTableIndex.setStatus("current")
_SignallevelTableSource_Type = OctetString
_SignallevelTableSource_Object = MibTableColumn
signallevelTableSource = _SignallevelTableSource_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 2),
    _SignallevelTableSource_Type()
)
signallevelTableSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableSource.setStatus("current")
_SignallevelTableDestination_Type = OctetString
_SignallevelTableDestination_Object = MibTableColumn
signallevelTableDestination = _SignallevelTableDestination_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 3),
    _SignallevelTableDestination_Type()
)
signallevelTableDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableDestination.setStatus("current")
_SignallevelTableRssi_Type = OctetString
_SignallevelTableRssi_Object = MibTableColumn
signallevelTableRssi = _SignallevelTableRssi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 2, 1, 4),
    _SignallevelTableRssi_Type()
)
signallevelTableRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallevelTableRssi.setStatus("current")
_ClientInfoTable_Object = MibTable
clientInfoTable = _ClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3)
)
if mibBuilder.loadTexts:
    clientInfoTable.setStatus("current")
_ClientInfoTableEntry_Object = MibTableRow
clientInfoTableEntry = _ClientInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1)
)
clientInfoTableEntry.setIndexNames(
    (0, "ENGENIUS-CLIENT-MIB", "clientInfoTableIndex"),
)
if mibBuilder.loadTexts:
    clientInfoTableEntry.setStatus("current")


class _ClientInfoTableIndex_Type(Integer32):
    """Custom type clientInfoTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ClientInfoTableIndex_Type.__name__ = "Integer32"
_ClientInfoTableIndex_Object = MibTableColumn
clientInfoTableIndex = _ClientInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 1),
    _ClientInfoTableIndex_Type()
)
clientInfoTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clientInfoTableIndex.setStatus("current")
_ClientInfoTableEssid_Type = OctetString
_ClientInfoTableEssid_Object = MibTableColumn
clientInfoTableEssid = _ClientInfoTableEssid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 2),
    _ClientInfoTableEssid_Type()
)
clientInfoTableEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableEssid.setStatus("current")
_ClientInfoTableMac_Type = OctetString
_ClientInfoTableMac_Object = MibTableColumn
clientInfoTableMac = _ClientInfoTableMac_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 3),
    _ClientInfoTableMac_Type()
)
clientInfoTableMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableMac.setStatus("current")
_ClientInfoTableChannel_Type = OctetString
_ClientInfoTableChannel_Object = MibTableColumn
clientInfoTableChannel = _ClientInfoTableChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 4),
    _ClientInfoTableChannel_Type()
)
clientInfoTableChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableChannel.setStatus("current")
_ClientInfoTableRate_Type = OctetString
_ClientInfoTableRate_Object = MibTableColumn
clientInfoTableRate = _ClientInfoTableRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 5),
    _ClientInfoTableRate_Type()
)
clientInfoTableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableRate.setStatus("current")
_ClientInfoTableRssi_Type = OctetString
_ClientInfoTableRssi_Object = MibTableColumn
clientInfoTableRssi = _ClientInfoTableRssi_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 6),
    _ClientInfoTableRssi_Type()
)
clientInfoTableRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableRssi.setStatus("current")
_ClientInfoTableIdletime_Type = OctetString
_ClientInfoTableIdletime_Object = MibTableColumn
clientInfoTableIdletime = _ClientInfoTableIdletime_Object(
    (1, 3, 6, 1, 4, 1, 14125, 1, 2, 30, 3, 1, 7),
    _ClientInfoTableIdletime_Type()
)
clientInfoTableIdletime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientInfoTableIdletime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENGENIUS-CLIENT-MIB",
    **{"engenius": engenius,
       "engeniusmesh": engeniusmesh,
       "nodeConfiguration": nodeConfiguration,
       "nodeConfigurationSignallevel": nodeConfigurationSignallevel,
       "signallevelExecute": signallevelExecute,
       "signallevelTable": signallevelTable,
       "signallevelTableEntry": signallevelTableEntry,
       "signallevelTableIndex": signallevelTableIndex,
       "signallevelTableSource": signallevelTableSource,
       "signallevelTableDestination": signallevelTableDestination,
       "signallevelTableRssi": signallevelTableRssi,
       "clientInfoTable": clientInfoTable,
       "clientInfoTableEntry": clientInfoTableEntry,
       "clientInfoTableIndex": clientInfoTableIndex,
       "clientInfoTableEssid": clientInfoTableEssid,
       "clientInfoTableMac": clientInfoTableMac,
       "clientInfoTableChannel": clientInfoTableChannel,
       "clientInfoTableRate": clientInfoTableRate,
       "clientInfoTableRssi": clientInfoTableRssi,
       "clientInfoTableIdletime": clientInfoTableIdletime}
)
