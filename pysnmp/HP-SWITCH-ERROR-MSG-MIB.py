# SNMP MIB module (HP-SWITCH-ERROR-MSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-ERROR-MSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:02 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpSwitchErrorMsgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68)
)
hpSwitchErrorMsgMIB.setRevisions(
        ("2009-04-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchErrorMsgObjects_ObjectIdentity = ObjectIdentity
hpSwitchErrorMsgObjects = _HpSwitchErrorMsgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1)
)
_HpSwitchErrorMsgTable_Object = MibTable
hpSwitchErrorMsgTable = _HpSwitchErrorMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchErrorMsgTable.setStatus("current")
_HpSwitchErrorMsgEntry_Object = MibTableRow
hpSwitchErrorMsgEntry = _HpSwitchErrorMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1)
)
hpSwitchErrorMsgEntry.setIndexNames(
    (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityType"),
    (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorEntityHandle"),
    (0, "HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorSnmpSeqCode"),
)
if mibBuilder.loadTexts:
    hpSwitchErrorMsgEntry.setStatus("current")


class _HpSwitchErrorEntityType_Type(Integer32):
    """Custom type hpSwitchErrorEntityType based on Integer32"""
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
        *(("cliSession", 2),
          ("ipV4Address", 4),
          ("ipV6Address", 5),
          ("oaApplication", 6),
          ("others", 1),
          ("webSession", 3))
    )


_HpSwitchErrorEntityType_Type.__name__ = "Integer32"
_HpSwitchErrorEntityType_Object = MibTableColumn
hpSwitchErrorEntityType = _HpSwitchErrorEntityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 1),
    _HpSwitchErrorEntityType_Type()
)
hpSwitchErrorEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchErrorEntityType.setStatus("current")


class _HpSwitchErrorEntityHandle_Type(OctetString):
    """Custom type hpSwitchErrorEntityHandle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_HpSwitchErrorEntityHandle_Type.__name__ = "OctetString"
_HpSwitchErrorEntityHandle_Object = MibTableColumn
hpSwitchErrorEntityHandle = _HpSwitchErrorEntityHandle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 2),
    _HpSwitchErrorEntityHandle_Type()
)
hpSwitchErrorEntityHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchErrorEntityHandle.setStatus("current")


class _HpSwitchErrorSnmpSeqCode_Type(Integer32):
    """Custom type hpSwitchErrorSnmpSeqCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpSwitchErrorSnmpSeqCode_Type.__name__ = "Integer32"
_HpSwitchErrorSnmpSeqCode_Object = MibTableColumn
hpSwitchErrorSnmpSeqCode = _HpSwitchErrorSnmpSeqCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 3),
    _HpSwitchErrorSnmpSeqCode_Type()
)
hpSwitchErrorSnmpSeqCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchErrorSnmpSeqCode.setStatus("current")
_HpSwitchErrorTime_Type = DateAndTime
_HpSwitchErrorTime_Object = MibTableColumn
hpSwitchErrorTime = _HpSwitchErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 4),
    _HpSwitchErrorTime_Type()
)
hpSwitchErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchErrorTime.setStatus("current")
_HpSwitchErrorFailedOID_Type = ObjectIdentifier
_HpSwitchErrorFailedOID_Object = MibTableColumn
hpSwitchErrorFailedOID = _HpSwitchErrorFailedOID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 5),
    _HpSwitchErrorFailedOID_Type()
)
hpSwitchErrorFailedOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchErrorFailedOID.setStatus("current")
_HpSwitchEntityErrorMsg_Type = OctetString
_HpSwitchEntityErrorMsg_Object = MibTableColumn
hpSwitchEntityErrorMsg = _HpSwitchEntityErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 6),
    _HpSwitchEntityErrorMsg_Type()
)
hpSwitchEntityErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchEntityErrorMsg.setStatus("current")


class _HpSwitchSnmpErrorCode_Type(Integer32):
    """Custom type hpSwitchSnmpErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_HpSwitchSnmpErrorCode_Type.__name__ = "Integer32"
_HpSwitchSnmpErrorCode_Object = MibTableColumn
hpSwitchSnmpErrorCode = _HpSwitchSnmpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 1, 1, 1, 7),
    _HpSwitchSnmpErrorCode_Type()
)
hpSwitchSnmpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchSnmpErrorCode.setStatus("current")
_HpSwitchErrorMsgMIBConformance_ObjectIdentity = ObjectIdentity
hpSwitchErrorMsgMIBConformance = _HpSwitchErrorMsgMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2)
)
_HpSwitchErrorMsgMIBCompliances_ObjectIdentity = ObjectIdentity
hpSwitchErrorMsgMIBCompliances = _HpSwitchErrorMsgMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1)
)
_HpSwitchErrorMsgMIBGroups_ObjectIdentity = ObjectIdentity
hpSwitchErrorMsgMIBGroups = _HpSwitchErrorMsgMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2)
)

# Managed Objects groups

hpSwitchErrorMsgMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 2, 1)
)
hpSwitchErrorMsgMIBGroup.setObjects(
      *(("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorTime"),
        ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchErrorFailedOID"),
        ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchEntityErrorMsg"),
        ("HP-SWITCH-ERROR-MSG-MIB", "hpSwitchSnmpErrorCode"))
)
if mibBuilder.loadTexts:
    hpSwitchErrorMsgMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchErrorMsgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchErrorMsgMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-ERROR-MSG-MIB",
    **{"hpSwitchErrorMsgMIB": hpSwitchErrorMsgMIB,
       "hpSwitchErrorMsgObjects": hpSwitchErrorMsgObjects,
       "hpSwitchErrorMsgTable": hpSwitchErrorMsgTable,
       "hpSwitchErrorMsgEntry": hpSwitchErrorMsgEntry,
       "hpSwitchErrorEntityType": hpSwitchErrorEntityType,
       "hpSwitchErrorEntityHandle": hpSwitchErrorEntityHandle,
       "hpSwitchErrorSnmpSeqCode": hpSwitchErrorSnmpSeqCode,
       "hpSwitchErrorTime": hpSwitchErrorTime,
       "hpSwitchErrorFailedOID": hpSwitchErrorFailedOID,
       "hpSwitchEntityErrorMsg": hpSwitchEntityErrorMsg,
       "hpSwitchSnmpErrorCode": hpSwitchSnmpErrorCode,
       "hpSwitchErrorMsgMIBConformance": hpSwitchErrorMsgMIBConformance,
       "hpSwitchErrorMsgMIBCompliances": hpSwitchErrorMsgMIBCompliances,
       "hpSwitchErrorMsgMIBCompliance": hpSwitchErrorMsgMIBCompliance,
       "hpSwitchErrorMsgMIBGroups": hpSwitchErrorMsgMIBGroups,
       "hpSwitchErrorMsgMIBGroup": hpSwitchErrorMsgMIBGroup}
)
