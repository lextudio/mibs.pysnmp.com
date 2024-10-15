# SNMP MIB module (EQL-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQL-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:56 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

eqlLldpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 21)
)
eqlLldpMib.setRevisions(
        ("2010-07-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EqlLldpV2ChassisIdSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("chassisComponent", 1),
          ("interfaceAlias", 2),
          ("interfaceName", 6),
          ("local", 7),
          ("macAddress", 4),
          ("networkAddress", 5),
          ("portComponent", 3))
    )



class EqlLldpV2ChassisId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )



class EqlLldpV2PortIdSubtype(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("interfaceAlias", 1),
          ("interfaceName", 5),
          ("local", 7),
          ("macAddress", 3),
          ("networkAddress", 4),
          ("portComponent", 2))
    )



class EqlLldpV2PortId(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class EqlLldpV2State(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("multiplePeers", 3),
          ("noPeer", 1),
          ("off", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EqlLldpMIBObjects_ObjectIdentity = ObjectIdentity
eqlLldpMIBObjects = _EqlLldpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1)
)
_EqlLldpDynamicIfTable_Object = MibTable
eqlLldpDynamicIfTable = _EqlLldpDynamicIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1)
)
if mibBuilder.loadTexts:
    eqlLldpDynamicIfTable.setStatus("current")
_EqlLldpDynamicIfEntry_Object = MibTableRow
eqlLldpDynamicIfEntry = _EqlLldpDynamicIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1)
)
eqlLldpDynamicIfEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqlLldpDynamicIfEntry.setStatus("current")
_EqlLldpRemMacAddress_Type = MacAddress
_EqlLldpRemMacAddress_Object = MibTableColumn
eqlLldpRemMacAddress = _EqlLldpRemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 1),
    _EqlLldpRemMacAddress_Type()
)
eqlLldpRemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpRemMacAddress.setStatus("current")
_EqlLldpV2RemChassisIdSubtype_Type = EqlLldpV2ChassisIdSubtype
_EqlLldpV2RemChassisIdSubtype_Object = MibTableColumn
eqlLldpV2RemChassisIdSubtype = _EqlLldpV2RemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 2),
    _EqlLldpV2RemChassisIdSubtype_Type()
)
eqlLldpV2RemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemChassisIdSubtype.setStatus("current")
_EqlLldpV2RemChassisId_Type = EqlLldpV2ChassisId
_EqlLldpV2RemChassisId_Object = MibTableColumn
eqlLldpV2RemChassisId = _EqlLldpV2RemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 3),
    _EqlLldpV2RemChassisId_Type()
)
eqlLldpV2RemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemChassisId.setStatus("current")
_EqlLldpV2RemPortIdSubtype_Type = EqlLldpV2PortIdSubtype
_EqlLldpV2RemPortIdSubtype_Object = MibTableColumn
eqlLldpV2RemPortIdSubtype = _EqlLldpV2RemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 4),
    _EqlLldpV2RemPortIdSubtype_Type()
)
eqlLldpV2RemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemPortIdSubtype.setStatus("current")
_EqlLldpV2RemPortId_Type = EqlLldpV2PortId
_EqlLldpV2RemPortId_Object = MibTableColumn
eqlLldpV2RemPortId = _EqlLldpV2RemPortId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 5),
    _EqlLldpV2RemPortId_Type()
)
eqlLldpV2RemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemPortId.setStatus("current")


class _EqlLldpV2RemPortDesc_Type(OctetString):
    """Custom type eqlLldpV2RemPortDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlLldpV2RemPortDesc_Type.__name__ = "OctetString"
_EqlLldpV2RemPortDesc_Object = MibTableColumn
eqlLldpV2RemPortDesc = _EqlLldpV2RemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 6),
    _EqlLldpV2RemPortDesc_Type()
)
eqlLldpV2RemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemPortDesc.setStatus("current")


class _EqlLldpV2RemSysName_Type(OctetString):
    """Custom type eqlLldpV2RemSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlLldpV2RemSysName_Type.__name__ = "OctetString"
_EqlLldpV2RemSysName_Object = MibTableColumn
eqlLldpV2RemSysName = _EqlLldpV2RemSysName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 7),
    _EqlLldpV2RemSysName_Type()
)
eqlLldpV2RemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemSysName.setStatus("current")


class _EqlLldpV2RemSysDesc_Type(OctetString):
    """Custom type eqlLldpV2RemSysDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlLldpV2RemSysDesc_Type.__name__ = "OctetString"
_EqlLldpV2RemSysDesc_Object = MibTableColumn
eqlLldpV2RemSysDesc = _EqlLldpV2RemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 8),
    _EqlLldpV2RemSysDesc_Type()
)
eqlLldpV2RemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemSysDesc.setStatus("current")
_EqlLldpV2State_Type = EqlLldpV2State
_EqlLldpV2State_Object = MibTableColumn
eqlLldpV2State = _EqlLldpV2State_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 9),
    _EqlLldpV2State_Type()
)
eqlLldpV2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2State.setStatus("current")


class _EqlLldpV2RemMgmtAddr_Type(OctetString):
    """Custom type eqlLldpV2RemMgmtAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlLldpV2RemMgmtAddr_Type.__name__ = "OctetString"
_EqlLldpV2RemMgmtAddr_Object = MibTableColumn
eqlLldpV2RemMgmtAddr = _EqlLldpV2RemMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 21, 1, 1, 1, 10),
    _EqlLldpV2RemMgmtAddr_Type()
)
eqlLldpV2RemMgmtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlLldpV2RemMgmtAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQL-LLDP-MIB",
    **{"EqlLldpV2ChassisIdSubtype": EqlLldpV2ChassisIdSubtype,
       "EqlLldpV2ChassisId": EqlLldpV2ChassisId,
       "EqlLldpV2PortIdSubtype": EqlLldpV2PortIdSubtype,
       "EqlLldpV2PortId": EqlLldpV2PortId,
       "EqlLldpV2State": EqlLldpV2State,
       "eqlLldpMib": eqlLldpMib,
       "eqlLldpMIBObjects": eqlLldpMIBObjects,
       "eqlLldpDynamicIfTable": eqlLldpDynamicIfTable,
       "eqlLldpDynamicIfEntry": eqlLldpDynamicIfEntry,
       "eqlLldpRemMacAddress": eqlLldpRemMacAddress,
       "eqlLldpV2RemChassisIdSubtype": eqlLldpV2RemChassisIdSubtype,
       "eqlLldpV2RemChassisId": eqlLldpV2RemChassisId,
       "eqlLldpV2RemPortIdSubtype": eqlLldpV2RemPortIdSubtype,
       "eqlLldpV2RemPortId": eqlLldpV2RemPortId,
       "eqlLldpV2RemPortDesc": eqlLldpV2RemPortDesc,
       "eqlLldpV2RemSysName": eqlLldpV2RemSysName,
       "eqlLldpV2RemSysDesc": eqlLldpV2RemSysDesc,
       "eqlLldpV2State": eqlLldpV2State,
       "eqlLldpV2RemMgmtAddr": eqlLldpV2RemMgmtAddr}
)
