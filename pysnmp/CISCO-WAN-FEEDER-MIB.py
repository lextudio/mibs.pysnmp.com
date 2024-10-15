# SNMP MIB module (CISCO-WAN-FEEDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FEEDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:01 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoWanFeederMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15)
)
ciscoWanFeederMIB.setRevisions(
        ("2003-03-27 00:00",
         "2000-10-10 00:00",
         "2000-04-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwfMIBObjects_ObjectIdentity = ObjectIdentity
cwfMIBObjects = _CwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1)
)
_CwfFeeder_ObjectIdentity = ObjectIdentity
cwfFeeder = _CwfFeeder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1)
)
_CwfFeederTable_Object = MibTable
cwfFeederTable = _CwfFeederTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwfFeederTable.setStatus("current")
_CwfFeederEntry_Object = MibTableRow
cwfFeederEntry = _CwfFeederEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1)
)
cwfFeederEntry.setIndexNames(
    (0, "CISCO-WAN-FEEDER-MIB", "cwfFeederIfNum"),
)
if mibBuilder.loadTexts:
    cwfFeederEntry.setStatus("current")
_CwfFeederIfNum_Type = InterfaceIndex
_CwfFeederIfNum_Object = MibTableColumn
cwfFeederIfNum = _CwfFeederIfNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 1),
    _CwfFeederIfNum_Type()
)
cwfFeederIfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwfFeederIfNum.setStatus("current")
_CwfFeederName_Type = DisplayString
_CwfFeederName_Object = MibTableColumn
cwfFeederName = _CwfFeederName_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 2),
    _CwfFeederName_Type()
)
cwfFeederName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfFeederName.setStatus("current")
_CwfLanIP_Type = IpAddress
_CwfLanIP_Object = MibTableColumn
cwfLanIP = _CwfLanIP_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 3),
    _CwfLanIP_Type()
)
cwfLanIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfLanIP.setStatus("current")
_CwfNetIP_Type = IpAddress
_CwfNetIP_Object = MibTableColumn
cwfNetIP = _CwfNetIP_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 4),
    _CwfNetIP_Type()
)
cwfNetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfNetIP.setStatus("current")


class _CwfRemoteShelf_Type(Integer32):
    """Custom type cwfRemoteShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CwfRemoteShelf_Type.__name__ = "Integer32"
_CwfRemoteShelf_Object = MibTableColumn
cwfRemoteShelf = _CwfRemoteShelf_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 5),
    _CwfRemoteShelf_Type()
)
cwfRemoteShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfRemoteShelf.setStatus("current")


class _CwfRemoteSlot_Type(Integer32):
    """Custom type cwfRemoteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CwfRemoteSlot_Type.__name__ = "Integer32"
_CwfRemoteSlot_Object = MibTableColumn
cwfRemoteSlot = _CwfRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 6),
    _CwfRemoteSlot_Type()
)
cwfRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfRemoteSlot.setStatus("current")


class _CwfRemotePort_Type(Integer32):
    """Custom type cwfRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CwfRemotePort_Type.__name__ = "Integer32"
_CwfRemotePort_Object = MibTableColumn
cwfRemotePort = _CwfRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 7),
    _CwfRemotePort_Type()
)
cwfRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfRemotePort.setStatus("current")


class _CwfFeederType_Type(Integer32):
    """Custom type cwfFeederType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("fdrAPS", 7),
          ("fdrBASIS", 4),
          ("fdrBPX", 2),
          ("fdrIGX", 8),
          ("fdrIPX", 1),
          ("fdrIgxAF", 9),
          ("fdrIpxAF", 3),
          ("fdrNON", 12),
          ("fdrPAR", 11),
          ("fdrUNI", 6),
          ("fdrUNKNOWN", 5),
          ("fdrVSI", 10))
    )


_CwfFeederType_Type.__name__ = "Integer32"
_CwfFeederType_Object = MibTableColumn
cwfFeederType = _CwfFeederType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 8),
    _CwfFeederType_Type()
)
cwfFeederType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfFeederType.setStatus("current")


class _CwfModelNumber_Type(Integer32):
    """Custom type cwfModelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwfModelNumber_Type.__name__ = "Integer32"
_CwfModelNumber_Object = MibTableColumn
cwfModelNumber = _CwfModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 9),
    _CwfModelNumber_Type()
)
cwfModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfModelNumber.setStatus("current")


class _CwfLMIAdminStatus_Type(Integer32):
    """Custom type cwfLMIAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CwfLMIAdminStatus_Type.__name__ = "Integer32"
_CwfLMIAdminStatus_Object = MibTableColumn
cwfLMIAdminStatus = _CwfLMIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 10),
    _CwfLMIAdminStatus_Type()
)
cwfLMIAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwfLMIAdminStatus.setStatus("current")


class _CwfLMIOperStatus_Type(Integer32):
    """Custom type cwfLMIOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CwfLMIOperStatus_Type.__name__ = "Integer32"
_CwfLMIOperStatus_Object = MibTableColumn
cwfLMIOperStatus = _CwfLMIOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 11),
    _CwfLMIOperStatus_Type()
)
cwfLMIOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfLMIOperStatus.setStatus("current")


class _CwfFeederNodeAlarm_Type(Integer32):
    """Custom type cwfFeederNodeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("unknown", 5))
    )


_CwfFeederNodeAlarm_Type.__name__ = "Integer32"
_CwfFeederNodeAlarm_Object = MibTableColumn
cwfFeederNodeAlarm = _CwfFeederNodeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 12),
    _CwfFeederNodeAlarm_Type()
)
cwfFeederNodeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwfFeederNodeAlarm.setStatus("current")
_CwfFeederRowStatus_Type = RowStatus
_CwfFeederRowStatus_Object = MibTableColumn
cwfFeederRowStatus = _CwfFeederRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 13),
    _CwfFeederRowStatus_Type()
)
cwfFeederRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwfFeederRowStatus.setStatus("current")


class _CwfLMIType_Type(Integer32):
    """Custom type cwfLMIType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("feeder", 1),
          ("xLMI", 2))
    )


_CwfLMIType_Type.__name__ = "Integer32"
_CwfLMIType_Object = MibTableColumn
cwfLMIType = _CwfLMIType_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 1, 1, 1, 1, 14),
    _CwfLMIType_Type()
)
cwfLMIType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwfLMIType.setStatus("current")
_CwfMIBConformance_ObjectIdentity = ObjectIdentity
cwfMIBConformance = _CwfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3)
)
_CwfMIBCompliances_ObjectIdentity = ObjectIdentity
cwfMIBCompliances = _CwfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1)
)
_CwfMIBGroups_ObjectIdentity = ObjectIdentity
cwfMIBGroups = _CwfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2)
)

# Managed Objects groups

cwfFeederGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2, 1)
)
cwfFeederGroup.setObjects(
      *(("CISCO-WAN-FEEDER-MIB", "cwfFeederName"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLanIP"),
        ("CISCO-WAN-FEEDER-MIB", "cwfNetIP"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemoteShelf"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemoteSlot"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemotePort"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederType"),
        ("CISCO-WAN-FEEDER-MIB", "cwfModelNumber"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLMIAdminStatus"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLMIOperStatus"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederNodeAlarm"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederRowStatus"))
)
if mibBuilder.loadTexts:
    cwfFeederGroup.setStatus("deprecated")

cwfFeederGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 2, 2)
)
cwfFeederGroup2.setObjects(
      *(("CISCO-WAN-FEEDER-MIB", "cwfFeederName"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLanIP"),
        ("CISCO-WAN-FEEDER-MIB", "cwfNetIP"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemoteShelf"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemoteSlot"),
        ("CISCO-WAN-FEEDER-MIB", "cwfRemotePort"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederType"),
        ("CISCO-WAN-FEEDER-MIB", "cwfModelNumber"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLMIAdminStatus"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLMIOperStatus"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederNodeAlarm"),
        ("CISCO-WAN-FEEDER-MIB", "cwfFeederRowStatus"),
        ("CISCO-WAN-FEEDER-MIB", "cwfLMIType"))
)
if mibBuilder.loadTexts:
    cwfFeederGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cwfMIBCompliance.setStatus(
        "deprecated"
    )

cwfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cwfMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FEEDER-MIB",
    **{"ciscoWanFeederMIB": ciscoWanFeederMIB,
       "cwfMIBObjects": cwfMIBObjects,
       "cwfFeeder": cwfFeeder,
       "cwfFeederTable": cwfFeederTable,
       "cwfFeederEntry": cwfFeederEntry,
       "cwfFeederIfNum": cwfFeederIfNum,
       "cwfFeederName": cwfFeederName,
       "cwfLanIP": cwfLanIP,
       "cwfNetIP": cwfNetIP,
       "cwfRemoteShelf": cwfRemoteShelf,
       "cwfRemoteSlot": cwfRemoteSlot,
       "cwfRemotePort": cwfRemotePort,
       "cwfFeederType": cwfFeederType,
       "cwfModelNumber": cwfModelNumber,
       "cwfLMIAdminStatus": cwfLMIAdminStatus,
       "cwfLMIOperStatus": cwfLMIOperStatus,
       "cwfFeederNodeAlarm": cwfFeederNodeAlarm,
       "cwfFeederRowStatus": cwfFeederRowStatus,
       "cwfLMIType": cwfLMIType,
       "cwfMIBConformance": cwfMIBConformance,
       "cwfMIBCompliances": cwfMIBCompliances,
       "cwfMIBCompliance": cwfMIBCompliance,
       "cwfMIBCompliance2": cwfMIBCompliance2,
       "cwfMIBGroups": cwfMIBGroups,
       "cwfFeederGroup": cwfFeederGroup,
       "cwfFeederGroup2": cwfFeederGroup2}
)
