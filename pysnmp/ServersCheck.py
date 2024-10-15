# SNMP MIB module (ServersCheck) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ServersCheck
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Serverscheck_ObjectIdentity = ObjectIdentity
serverscheck = _Serverscheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 1)
)
_Productname_Type = DisplayString
_Productname_Object = MibScalar
productname = _Productname_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 1),
    _Productname_Type()
)
productname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productname.setStatus("mandatory")
_Productversion_Type = DisplayString
_Productversion_Object = MibScalar
productversion = _Productversion_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 2),
    _Productversion_Type()
)
productversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productversion.setStatus("mandatory")
_Productdate_Type = DisplayString
_Productdate_Object = MibScalar
productdate = _Productdate_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 3),
    _Productdate_Type()
)
productdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productdate.setStatus("mandatory")
_Productusername_Type = DisplayString
_Productusername_Object = MibScalar
productusername = _Productusername_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 4),
    _Productusername_Type()
)
productusername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productusername.setStatus("mandatory")
_Productuserloc_Type = DisplayString
_Productuserloc_Object = MibScalar
productuserloc = _Productuserloc_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 5),
    _Productuserloc_Type()
)
productuserloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productuserloc.setStatus("mandatory")
_Productnetip_Type = IpAddress
_Productnetip_Object = MibScalar
productnetip = _Productnetip_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 6),
    _Productnetip_Type()
)
productnetip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetip.setStatus("mandatory")
_Productnetgateway_Type = IpAddress
_Productnetgateway_Object = MibScalar
productnetgateway = _Productnetgateway_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 7),
    _Productnetgateway_Type()
)
productnetgateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetgateway.setStatus("mandatory")
_Productnetpridns_Type = IpAddress
_Productnetpridns_Object = MibScalar
productnetpridns = _Productnetpridns_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 8),
    _Productnetpridns_Type()
)
productnetpridns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetpridns.setStatus("mandatory")
_Productnetsecdns_Type = IpAddress
_Productnetsecdns_Object = MibScalar
productnetsecdns = _Productnetsecdns_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 9),
    _Productnetsecdns_Type()
)
productnetsecdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetsecdns.setStatus("mandatory")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 2)
)
_Traps_Object = MibTable
traps = _Traps_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1)
)
if mibBuilder.loadTexts:
    traps.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1)
)
trapEntry.setIndexNames(
    (0, "ServersCheck", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("mandatory")


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibTableColumn
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 2),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("mandatory")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 3),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("mandatory")
_TrapCommunity_Type = DisplayString
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 3)
)
_Sensor1name_Type = DisplayString
_Sensor1name_Object = MibScalar
sensor1name = _Sensor1name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 1),
    _Sensor1name_Type()
)
sensor1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1name.setStatus("mandatory")
_Sensor1Value_Type = DisplayString
_Sensor1Value_Object = MibScalar
sensor1Value = _Sensor1Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 2),
    _Sensor1Value_Type()
)
sensor1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1Value.setStatus("mandatory")
_Sensor1LastErrMsg_Type = DisplayString
_Sensor1LastErrMsg_Object = MibScalar
sensor1LastErrMsg = _Sensor1LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 3),
    _Sensor1LastErrMsg_Type()
)
sensor1LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1LastErrMsg.setStatus("mandatory")
_Sensor1LastErrTime_Type = DisplayString
_Sensor1LastErrTime_Object = MibScalar
sensor1LastErrTime = _Sensor1LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 4),
    _Sensor1LastErrTime_Type()
)
sensor1LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1LastErrTime.setStatus("mandatory")
_Sensor2name_Type = DisplayString
_Sensor2name_Object = MibScalar
sensor2name = _Sensor2name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 5),
    _Sensor2name_Type()
)
sensor2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2name.setStatus("mandatory")
_Sensor2Value_Type = DisplayString
_Sensor2Value_Object = MibScalar
sensor2Value = _Sensor2Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 6),
    _Sensor2Value_Type()
)
sensor2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2Value.setStatus("mandatory")
_Sensor2LastErrMsg_Type = DisplayString
_Sensor2LastErrMsg_Object = MibScalar
sensor2LastErrMsg = _Sensor2LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 7),
    _Sensor2LastErrMsg_Type()
)
sensor2LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2LastErrMsg.setStatus("mandatory")
_Sensor2LastErrTime_Type = DisplayString
_Sensor2LastErrTime_Object = MibScalar
sensor2LastErrTime = _Sensor2LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 8),
    _Sensor2LastErrTime_Type()
)
sensor2LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2LastErrTime.setStatus("mandatory")
_Sensor3name_Type = DisplayString
_Sensor3name_Object = MibScalar
sensor3name = _Sensor3name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 9),
    _Sensor3name_Type()
)
sensor3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3name.setStatus("mandatory")
_Sensor3Value_Type = DisplayString
_Sensor3Value_Object = MibScalar
sensor3Value = _Sensor3Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 10),
    _Sensor3Value_Type()
)
sensor3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3Value.setStatus("mandatory")
_Sensor3LastErrMsg_Type = DisplayString
_Sensor3LastErrMsg_Object = MibScalar
sensor3LastErrMsg = _Sensor3LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 11),
    _Sensor3LastErrMsg_Type()
)
sensor3LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3LastErrMsg.setStatus("mandatory")
_Sensor3LastErrTime_Type = DisplayString
_Sensor3LastErrTime_Object = MibScalar
sensor3LastErrTime = _Sensor3LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 12),
    _Sensor3LastErrTime_Type()
)
sensor3LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3LastErrTime.setStatus("mandatory")
_Sensor4name_Type = DisplayString
_Sensor4name_Object = MibScalar
sensor4name = _Sensor4name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 13),
    _Sensor4name_Type()
)
sensor4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4name.setStatus("mandatory")
_Sensor4Value_Type = DisplayString
_Sensor4Value_Object = MibScalar
sensor4Value = _Sensor4Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 14),
    _Sensor4Value_Type()
)
sensor4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4Value.setStatus("mandatory")
_Sensor4LastErrMsg_Type = DisplayString
_Sensor4LastErrMsg_Object = MibScalar
sensor4LastErrMsg = _Sensor4LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 15),
    _Sensor4LastErrMsg_Type()
)
sensor4LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4LastErrMsg.setStatus("mandatory")
_Sensor4LastErrTime_Type = DisplayString
_Sensor4LastErrTime_Object = MibScalar
sensor4LastErrTime = _Sensor4LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 16),
    _Sensor4LastErrTime_Type()
)
sensor4LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4LastErrTime.setStatus("mandatory")
_Sensor5name_Type = DisplayString
_Sensor5name_Object = MibScalar
sensor5name = _Sensor5name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 17),
    _Sensor5name_Type()
)
sensor5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5name.setStatus("mandatory")
_Sensor5Value_Type = DisplayString
_Sensor5Value_Object = MibScalar
sensor5Value = _Sensor5Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 18),
    _Sensor5Value_Type()
)
sensor5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5Value.setStatus("mandatory")
_Sensor5LastErrMsg_Type = DisplayString
_Sensor5LastErrMsg_Object = MibScalar
sensor5LastErrMsg = _Sensor5LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 19),
    _Sensor5LastErrMsg_Type()
)
sensor5LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5LastErrMsg.setStatus("mandatory")
_Sensor5LastErrTime_Type = DisplayString
_Sensor5LastErrTime_Object = MibScalar
sensor5LastErrTime = _Sensor5LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 20),
    _Sensor5LastErrTime_Type()
)
sensor5LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5LastErrTime.setStatus("mandatory")
_Trapalerts_ObjectIdentity = ObjectIdentity
trapalerts = _Trapalerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 4)
)
_Sensor1TrapErrMsg_Type = OctetString
_Sensor1TrapErrMsg_Object = MibScalar
sensor1TrapErrMsg = _Sensor1TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 1),
    _Sensor1TrapErrMsg_Type()
)
sensor1TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1TrapErrMsg.setStatus("mandatory")
_Sensor2TrapErrMsg_Type = OctetString
_Sensor2TrapErrMsg_Object = MibScalar
sensor2TrapErrMsg = _Sensor2TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 2),
    _Sensor2TrapErrMsg_Type()
)
sensor2TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2TrapErrMsg.setStatus("mandatory")
_Sensor3TrapErrMsg_Type = OctetString
_Sensor3TrapErrMsg_Object = MibScalar
sensor3TrapErrMsg = _Sensor3TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 3),
    _Sensor3TrapErrMsg_Type()
)
sensor3TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3TrapErrMsg.setStatus("mandatory")
_Sensor4TrapErrMsg_Type = OctetString
_Sensor4TrapErrMsg_Object = MibScalar
sensor4TrapErrMsg = _Sensor4TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 4),
    _Sensor4TrapErrMsg_Type()
)
sensor4TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4TrapErrMsg.setStatus("mandatory")
_Sensor6TrapErrMsg_Type = OctetString
_Sensor6TrapErrMsg_Object = MibScalar
sensor6TrapErrMsg = _Sensor6TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 4),
    _Sensor6TrapErrMsg_Type()
)
sensor6TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6TrapErrMsg.setStatus("mandatory")
_Sensor5TrapErrMsg_Type = OctetString
_Sensor5TrapErrMsg_Object = MibScalar
sensor5TrapErrMsg = _Sensor5TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 5),
    _Sensor5TrapErrMsg_Type()
)
sensor5TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5TrapErrMsg.setStatus("mandatory")
_Iotrapalerts_ObjectIdentity = ObjectIdentity
iotrapalerts = _Iotrapalerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 5)
)
_IosensorINPUT1trapErrMsg_Type = OctetString
_IosensorINPUT1trapErrMsg_Object = MibScalar
iosensorINPUT1trapErrMsg = _IosensorINPUT1trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 1),
    _IosensorINPUT1trapErrMsg_Type()
)
iosensorINPUT1trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT1trapErrMsg.setStatus("mandatory")
_IosensorINPUT2trapErrMsg_Type = OctetString
_IosensorINPUT2trapErrMsg_Object = MibScalar
iosensorINPUT2trapErrMsg = _IosensorINPUT2trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 2),
    _IosensorINPUT2trapErrMsg_Type()
)
iosensorINPUT2trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT2trapErrMsg.setStatus("mandatory")
_IosensorINPUT3trapErrMsg_Type = OctetString
_IosensorINPUT3trapErrMsg_Object = MibScalar
iosensorINPUT3trapErrMsg = _IosensorINPUT3trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 3),
    _IosensorINPUT3trapErrMsg_Type()
)
iosensorINPUT3trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT3trapErrMsg.setStatus("mandatory")
_IosensorINPUT4trapErrMsg_Type = OctetString
_IosensorINPUT4trapErrMsg_Object = MibScalar
iosensorINPUT4trapErrMsg = _IosensorINPUT4trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 4),
    _IosensorINPUT4trapErrMsg_Type()
)
iosensorINPUT4trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT4trapErrMsg.setStatus("mandatory")
_IosensorINPUT5trapErrMsg_Type = OctetString
_IosensorINPUT5trapErrMsg_Object = MibScalar
iosensorINPUT5trapErrMsg = _IosensorINPUT5trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 5),
    _IosensorINPUT5trapErrMsg_Type()
)
iosensorINPUT5trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT5trapErrMsg.setStatus("mandatory")
_IosensorINPUT6trapErrMsg_Type = OctetString
_IosensorINPUT6trapErrMsg_Object = MibScalar
iosensorINPUT6trapErrMsg = _IosensorINPUT6trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 6),
    _IosensorINPUT6trapErrMsg_Type()
)
iosensorINPUT6trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT6trapErrMsg.setStatus("mandatory")
_IosensorINPUT7trapErrMsg_Type = OctetString
_IosensorINPUT7trapErrMsg_Object = MibScalar
iosensorINPUT7trapErrMsg = _IosensorINPUT7trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 7),
    _IosensorINPUT7trapErrMsg_Type()
)
iosensorINPUT7trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT7trapErrMsg.setStatus("mandatory")
_IosensorINPUT8trapErrMsg_Type = OctetString
_IosensorINPUT8trapErrMsg_Object = MibScalar
iosensorINPUT8trapErrMsg = _IosensorINPUT8trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 8),
    _IosensorINPUT8trapErrMsg_Type()
)
iosensorINPUT8trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT8trapErrMsg.setStatus("mandatory")
_IosensorINPUT9trapErrMsg_Type = OctetString
_IosensorINPUT9trapErrMsg_Object = MibScalar
iosensorINPUT9trapErrMsg = _IosensorINPUT9trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 9),
    _IosensorINPUT9trapErrMsg_Type()
)
iosensorINPUT9trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT9trapErrMsg.setStatus("mandatory")
_IosensorINPUT10trapErrMsg_Type = OctetString
_IosensorINPUT10trapErrMsg_Object = MibScalar
iosensorINPUT10trapErrMsg = _IosensorINPUT10trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 10),
    _IosensorINPUT10trapErrMsg_Type()
)
iosensorINPUT10trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT10trapErrMsg.setStatus("mandatory")
_IosensorINPUT11trapErrMsg_Type = OctetString
_IosensorINPUT11trapErrMsg_Object = MibScalar
iosensorINPUT11trapErrMsg = _IosensorINPUT11trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 11),
    _IosensorINPUT11trapErrMsg_Type()
)
iosensorINPUT11trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT11trapErrMsg.setStatus("mandatory")
_IosensorINPUT12trapErrMsg_Type = OctetString
_IosensorINPUT12trapErrMsg_Object = MibScalar
iosensorINPUT12trapErrMsg = _IosensorINPUT12trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 12),
    _IosensorINPUT12trapErrMsg_Type()
)
iosensorINPUT12trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT12trapErrMsg.setStatus("mandatory")
_IosensorINPUT13trapErrMsg_Type = OctetString
_IosensorINPUT13trapErrMsg_Object = MibScalar
iosensorINPUT13trapErrMsg = _IosensorINPUT13trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 13),
    _IosensorINPUT13trapErrMsg_Type()
)
iosensorINPUT13trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT13trapErrMsg.setStatus("mandatory")
_IosensorINPUT14trapErrMsg_Type = OctetString
_IosensorINPUT14trapErrMsg_Object = MibScalar
iosensorINPUT14trapErrMsg = _IosensorINPUT14trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 14),
    _IosensorINPUT14trapErrMsg_Type()
)
iosensorINPUT14trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT14trapErrMsg.setStatus("mandatory")
_IosensorINPUT15trapErrMsg_Type = OctetString
_IosensorINPUT15trapErrMsg_Object = MibScalar
iosensorINPUT15trapErrMsg = _IosensorINPUT15trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 15),
    _IosensorINPUT15trapErrMsg_Type()
)
iosensorINPUT15trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT15trapErrMsg.setStatus("mandatory")
_IosensorINPUT16trapErrMsg_Type = OctetString
_IosensorINPUT16trapErrMsg_Object = MibScalar
iosensorINPUT16trapErrMsg = _IosensorINPUT16trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 16),
    _IosensorINPUT16trapErrMsg_Type()
)
iosensorINPUT16trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT16trapErrMsg.setStatus("mandatory")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 6)
)
_Input1name_Type = DisplayString
_Input1name_Object = MibScalar
input1name = _Input1name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 1),
    _Input1name_Type()
)
input1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1name.setStatus("mandatory")
_Input1Value_Type = DisplayString
_Input1Value_Object = MibScalar
input1Value = _Input1Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 2),
    _Input1Value_Type()
)
input1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1Value.setStatus("mandatory")
_Input1LastErrMsg_Type = DisplayString
_Input1LastErrMsg_Object = MibScalar
input1LastErrMsg = _Input1LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 3),
    _Input1LastErrMsg_Type()
)
input1LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1LastErrMsg.setStatus("mandatory")
_Input2name_Type = DisplayString
_Input2name_Object = MibScalar
input2name = _Input2name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 4),
    _Input2name_Type()
)
input2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2name.setStatus("mandatory")
_Input2Value_Type = DisplayString
_Input2Value_Object = MibScalar
input2Value = _Input2Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 5),
    _Input2Value_Type()
)
input2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2Value.setStatus("mandatory")
_Input2LastErrMsg_Type = DisplayString
_Input2LastErrMsg_Object = MibScalar
input2LastErrMsg = _Input2LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 6),
    _Input2LastErrMsg_Type()
)
input2LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2LastErrMsg.setStatus("mandatory")
_Input3name_Type = DisplayString
_Input3name_Object = MibScalar
input3name = _Input3name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 7),
    _Input3name_Type()
)
input3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3name.setStatus("mandatory")
_Input3Value_Type = DisplayString
_Input3Value_Object = MibScalar
input3Value = _Input3Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 8),
    _Input3Value_Type()
)
input3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3Value.setStatus("mandatory")
_Input3LastErrMsg_Type = DisplayString
_Input3LastErrMsg_Object = MibScalar
input3LastErrMsg = _Input3LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 9),
    _Input3LastErrMsg_Type()
)
input3LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3LastErrMsg.setStatus("mandatory")
_Input4name_Type = DisplayString
_Input4name_Object = MibScalar
input4name = _Input4name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 10),
    _Input4name_Type()
)
input4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4name.setStatus("mandatory")
_Input4Value_Type = DisplayString
_Input4Value_Object = MibScalar
input4Value = _Input4Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 11),
    _Input4Value_Type()
)
input4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4Value.setStatus("mandatory")
_Input4LastErrMsg_Type = DisplayString
_Input4LastErrMsg_Object = MibScalar
input4LastErrMsg = _Input4LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 12),
    _Input4LastErrMsg_Type()
)
input4LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4LastErrMsg.setStatus("mandatory")
_Input5name_Type = DisplayString
_Input5name_Object = MibScalar
input5name = _Input5name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 13),
    _Input5name_Type()
)
input5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5name.setStatus("mandatory")
_Input5Value_Type = DisplayString
_Input5Value_Object = MibScalar
input5Value = _Input5Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 14),
    _Input5Value_Type()
)
input5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5Value.setStatus("mandatory")
_Input5LastErrMsg_Type = DisplayString
_Input5LastErrMsg_Object = MibScalar
input5LastErrMsg = _Input5LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 15),
    _Input5LastErrMsg_Type()
)
input5LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5LastErrMsg.setStatus("mandatory")
_Input6name_Type = DisplayString
_Input6name_Object = MibScalar
input6name = _Input6name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 16),
    _Input6name_Type()
)
input6name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6name.setStatus("mandatory")
_Input6Value_Type = DisplayString
_Input6Value_Object = MibScalar
input6Value = _Input6Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 17),
    _Input6Value_Type()
)
input6Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6Value.setStatus("mandatory")
_Input6LastErrMsg_Type = DisplayString
_Input6LastErrMsg_Object = MibScalar
input6LastErrMsg = _Input6LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 18),
    _Input6LastErrMsg_Type()
)
input6LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6LastErrMsg.setStatus("mandatory")
_Input7name_Type = DisplayString
_Input7name_Object = MibScalar
input7name = _Input7name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 19),
    _Input7name_Type()
)
input7name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7name.setStatus("mandatory")
_Input7Value_Type = DisplayString
_Input7Value_Object = MibScalar
input7Value = _Input7Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 20),
    _Input7Value_Type()
)
input7Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7Value.setStatus("mandatory")
_Input7LastErrMsg_Type = DisplayString
_Input7LastErrMsg_Object = MibScalar
input7LastErrMsg = _Input7LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 21),
    _Input7LastErrMsg_Type()
)
input7LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7LastErrMsg.setStatus("mandatory")
_Input8name_Type = DisplayString
_Input8name_Object = MibScalar
input8name = _Input8name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 22),
    _Input8name_Type()
)
input8name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8name.setStatus("mandatory")
_Input8Value_Type = DisplayString
_Input8Value_Object = MibScalar
input8Value = _Input8Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 23),
    _Input8Value_Type()
)
input8Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8Value.setStatus("mandatory")
_Input8LastErrMsg_Type = DisplayString
_Input8LastErrMsg_Object = MibScalar
input8LastErrMsg = _Input8LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 24),
    _Input8LastErrMsg_Type()
)
input8LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8LastErrMsg.setStatus("mandatory")
_Input9name_Type = DisplayString
_Input9name_Object = MibScalar
input9name = _Input9name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 25),
    _Input9name_Type()
)
input9name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9name.setStatus("mandatory")
_Input9Value_Type = DisplayString
_Input9Value_Object = MibScalar
input9Value = _Input9Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 26),
    _Input9Value_Type()
)
input9Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9Value.setStatus("mandatory")
_Input9LastErrMsg_Type = DisplayString
_Input9LastErrMsg_Object = MibScalar
input9LastErrMsg = _Input9LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 27),
    _Input9LastErrMsg_Type()
)
input9LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9LastErrMsg.setStatus("mandatory")
_Input10name_Type = DisplayString
_Input10name_Object = MibScalar
input10name = _Input10name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 28),
    _Input10name_Type()
)
input10name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10name.setStatus("mandatory")
_Input10Value_Type = DisplayString
_Input10Value_Object = MibScalar
input10Value = _Input10Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 29),
    _Input10Value_Type()
)
input10Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10Value.setStatus("mandatory")
_Input10LastErrMsg_Type = DisplayString
_Input10LastErrMsg_Object = MibScalar
input10LastErrMsg = _Input10LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 30),
    _Input10LastErrMsg_Type()
)
input10LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10LastErrMsg.setStatus("mandatory")
_Input11name_Type = DisplayString
_Input11name_Object = MibScalar
input11name = _Input11name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 31),
    _Input11name_Type()
)
input11name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11name.setStatus("mandatory")
_Input11Value_Type = DisplayString
_Input11Value_Object = MibScalar
input11Value = _Input11Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 32),
    _Input11Value_Type()
)
input11Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11Value.setStatus("mandatory")
_Input11LastErrMsg_Type = DisplayString
_Input11LastErrMsg_Object = MibScalar
input11LastErrMsg = _Input11LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 33),
    _Input11LastErrMsg_Type()
)
input11LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11LastErrMsg.setStatus("mandatory")
_Input12name_Type = DisplayString
_Input12name_Object = MibScalar
input12name = _Input12name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 34),
    _Input12name_Type()
)
input12name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12name.setStatus("mandatory")
_Input12Value_Type = DisplayString
_Input12Value_Object = MibScalar
input12Value = _Input12Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 35),
    _Input12Value_Type()
)
input12Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12Value.setStatus("mandatory")
_Input12LastErrMsg_Type = DisplayString
_Input12LastErrMsg_Object = MibScalar
input12LastErrMsg = _Input12LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 36),
    _Input12LastErrMsg_Type()
)
input12LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12LastErrMsg.setStatus("mandatory")
_Input13name_Type = DisplayString
_Input13name_Object = MibScalar
input13name = _Input13name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 37),
    _Input13name_Type()
)
input13name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13name.setStatus("mandatory")
_Input13Value_Type = DisplayString
_Input13Value_Object = MibScalar
input13Value = _Input13Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 38),
    _Input13Value_Type()
)
input13Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13Value.setStatus("mandatory")
_Input13LastErrMsg_Type = DisplayString
_Input13LastErrMsg_Object = MibScalar
input13LastErrMsg = _Input13LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 39),
    _Input13LastErrMsg_Type()
)
input13LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13LastErrMsg.setStatus("mandatory")
_Input14name_Type = DisplayString
_Input14name_Object = MibScalar
input14name = _Input14name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 40),
    _Input14name_Type()
)
input14name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14name.setStatus("mandatory")
_Input14Value_Type = DisplayString
_Input14Value_Object = MibScalar
input14Value = _Input14Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 41),
    _Input14Value_Type()
)
input14Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14Value.setStatus("mandatory")
_Input14LastErrMsg_Type = DisplayString
_Input14LastErrMsg_Object = MibScalar
input14LastErrMsg = _Input14LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 42),
    _Input14LastErrMsg_Type()
)
input14LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14LastErrMsg.setStatus("mandatory")
_Input15name_Type = DisplayString
_Input15name_Object = MibScalar
input15name = _Input15name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 43),
    _Input15name_Type()
)
input15name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15name.setStatus("mandatory")
_Input15Value_Type = DisplayString
_Input15Value_Object = MibScalar
input15Value = _Input15Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 44),
    _Input15Value_Type()
)
input15Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15Value.setStatus("mandatory")
_Input15LastErrMsg_Type = DisplayString
_Input15LastErrMsg_Object = MibScalar
input15LastErrMsg = _Input15LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 45),
    _Input15LastErrMsg_Type()
)
input15LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15LastErrMsg.setStatus("mandatory")
_Input16name_Type = DisplayString
_Input16name_Object = MibScalar
input16name = _Input16name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 46),
    _Input16name_Type()
)
input16name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16name.setStatus("mandatory")
_Input16Value_Type = DisplayString
_Input16Value_Object = MibScalar
input16Value = _Input16Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 47),
    _Input16Value_Type()
)
input16Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16Value.setStatus("mandatory")
_Input16LastErrMsg_Type = DisplayString
_Input16LastErrMsg_Object = MibScalar
input16LastErrMsg = _Input16LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 48),
    _Input16LastErrMsg_Type()
)
input16LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16LastErrMsg.setStatus("mandatory")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 7)
)
_Output1State_Type = DisplayString
_Output1State_Object = MibScalar
output1State = _Output1State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 1),
    _Output1State_Type()
)
output1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output1State.setStatus("mandatory")
_Output2State_Type = DisplayString
_Output2State_Object = MibScalar
output2State = _Output2State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 2),
    _Output2State_Type()
)
output2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output2State.setStatus("mandatory")
_Output3State_Type = DisplayString
_Output3State_Object = MibScalar
output3State = _Output3State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 3),
    _Output3State_Type()
)
output3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output3State.setStatus("mandatory")
_Output4State_Type = DisplayString
_Output4State_Object = MibScalar
output4State = _Output4State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 4),
    _Output4State_Type()
)
output4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output4State.setStatus("mandatory")

# Managed Objects groups


# Notification objects

iosensorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 0, 0)
)
iosensorAlert.setObjects(
      *(("ServersCheck", "iosensorINPUT1trapErrMsg"),
        ("ServersCheck", "iosensorINPUT2trapErrMsg"),
        ("ServersCheck", "iosensorINPUT3trapErrMsg"),
        ("ServersCheck", "iosensorINPUT4trapErrMsg"),
        ("ServersCheck", "iosensorINPUT5trapErrMsg"),
        ("ServersCheck", "iosensorINPUT6trapErrMsg"),
        ("ServersCheck", "iosensorINPUT7trapErrMsg"),
        ("ServersCheck", "iosensorINPUT8trapErrMsg"),
        ("ServersCheck", "iosensorINPUT9trapErrMsg"),
        ("ServersCheck", "iosensorINPUT10trapErrMsg"),
        ("ServersCheck", "iosensorINPUT11trapErrMsg"),
        ("ServersCheck", "iosensorINPUT12trapErrMsg"),
        ("ServersCheck", "iosensorINPUT13trapErrMsg"),
        ("ServersCheck", "iosensorINPUT14trapErrMsg"),
        ("ServersCheck", "iosensorINPUT15trapErrMsg"),
        ("ServersCheck", "iosensorINPUT16trapErrMsg"))
)
if mibBuilder.loadTexts:
    iosensorAlert.setStatus(
        ""
    )

sensorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 0, 1)
)
sensorAlert.setObjects(
      *(("ServersCheck", "sensor1TrapErrMsg"),
        ("ServersCheck", "sensor2TrapErrMsg"),
        ("ServersCheck", "sensor3TrapErrMsg"),
        ("ServersCheck", "sensor4TrapErrMsg"),
        ("ServersCheck", "sensor5TrapErrMsg"),
        ("ServersCheck", "sensor6TrapErrMsg"))
)
if mibBuilder.loadTexts:
    sensorAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ServersCheck",
    **{"serverscheck": serverscheck,
       "iosensorAlert": iosensorAlert,
       "sensorAlert": sensorAlert,
       "product": product,
       "productname": productname,
       "productversion": productversion,
       "productdate": productdate,
       "productusername": productusername,
       "productuserloc": productuserloc,
       "productnetip": productnetip,
       "productnetgateway": productnetgateway,
       "productnetpridns": productnetpridns,
       "productnetsecdns": productnetsecdns,
       "setup": setup,
       "traps": traps,
       "trapEntry": trapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "control": control,
       "sensor1name": sensor1name,
       "sensor1Value": sensor1Value,
       "sensor1LastErrMsg": sensor1LastErrMsg,
       "sensor1LastErrTime": sensor1LastErrTime,
       "sensor2name": sensor2name,
       "sensor2Value": sensor2Value,
       "sensor2LastErrMsg": sensor2LastErrMsg,
       "sensor2LastErrTime": sensor2LastErrTime,
       "sensor3name": sensor3name,
       "sensor3Value": sensor3Value,
       "sensor3LastErrMsg": sensor3LastErrMsg,
       "sensor3LastErrTime": sensor3LastErrTime,
       "sensor4name": sensor4name,
       "sensor4Value": sensor4Value,
       "sensor4LastErrMsg": sensor4LastErrMsg,
       "sensor4LastErrTime": sensor4LastErrTime,
       "sensor5name": sensor5name,
       "sensor5Value": sensor5Value,
       "sensor5LastErrMsg": sensor5LastErrMsg,
       "sensor5LastErrTime": sensor5LastErrTime,
       "trapalerts": trapalerts,
       "sensor1TrapErrMsg": sensor1TrapErrMsg,
       "sensor2TrapErrMsg": sensor2TrapErrMsg,
       "sensor3TrapErrMsg": sensor3TrapErrMsg,
       "sensor4TrapErrMsg": sensor4TrapErrMsg,
       "sensor6TrapErrMsg": sensor6TrapErrMsg,
       "sensor5TrapErrMsg": sensor5TrapErrMsg,
       "iotrapalerts": iotrapalerts,
       "iosensorINPUT1trapErrMsg": iosensorINPUT1trapErrMsg,
       "iosensorINPUT2trapErrMsg": iosensorINPUT2trapErrMsg,
       "iosensorINPUT3trapErrMsg": iosensorINPUT3trapErrMsg,
       "iosensorINPUT4trapErrMsg": iosensorINPUT4trapErrMsg,
       "iosensorINPUT5trapErrMsg": iosensorINPUT5trapErrMsg,
       "iosensorINPUT6trapErrMsg": iosensorINPUT6trapErrMsg,
       "iosensorINPUT7trapErrMsg": iosensorINPUT7trapErrMsg,
       "iosensorINPUT8trapErrMsg": iosensorINPUT8trapErrMsg,
       "iosensorINPUT9trapErrMsg": iosensorINPUT9trapErrMsg,
       "iosensorINPUT10trapErrMsg": iosensorINPUT10trapErrMsg,
       "iosensorINPUT11trapErrMsg": iosensorINPUT11trapErrMsg,
       "iosensorINPUT12trapErrMsg": iosensorINPUT12trapErrMsg,
       "iosensorINPUT13trapErrMsg": iosensorINPUT13trapErrMsg,
       "iosensorINPUT14trapErrMsg": iosensorINPUT14trapErrMsg,
       "iosensorINPUT15trapErrMsg": iosensorINPUT15trapErrMsg,
       "iosensorINPUT16trapErrMsg": iosensorINPUT16trapErrMsg,
       "input": input,
       "input1name": input1name,
       "input1Value": input1Value,
       "input1LastErrMsg": input1LastErrMsg,
       "input2name": input2name,
       "input2Value": input2Value,
       "input2LastErrMsg": input2LastErrMsg,
       "input3name": input3name,
       "input3Value": input3Value,
       "input3LastErrMsg": input3LastErrMsg,
       "input4name": input4name,
       "input4Value": input4Value,
       "input4LastErrMsg": input4LastErrMsg,
       "input5name": input5name,
       "input5Value": input5Value,
       "input5LastErrMsg": input5LastErrMsg,
       "input6name": input6name,
       "input6Value": input6Value,
       "input6LastErrMsg": input6LastErrMsg,
       "input7name": input7name,
       "input7Value": input7Value,
       "input7LastErrMsg": input7LastErrMsg,
       "input8name": input8name,
       "input8Value": input8Value,
       "input8LastErrMsg": input8LastErrMsg,
       "input9name": input9name,
       "input9Value": input9Value,
       "input9LastErrMsg": input9LastErrMsg,
       "input10name": input10name,
       "input10Value": input10Value,
       "input10LastErrMsg": input10LastErrMsg,
       "input11name": input11name,
       "input11Value": input11Value,
       "input11LastErrMsg": input11LastErrMsg,
       "input12name": input12name,
       "input12Value": input12Value,
       "input12LastErrMsg": input12LastErrMsg,
       "input13name": input13name,
       "input13Value": input13Value,
       "input13LastErrMsg": input13LastErrMsg,
       "input14name": input14name,
       "input14Value": input14Value,
       "input14LastErrMsg": input14LastErrMsg,
       "input15name": input15name,
       "input15Value": input15Value,
       "input15LastErrMsg": input15LastErrMsg,
       "input16name": input16name,
       "input16Value": input16Value,
       "input16LastErrMsg": input16LastErrMsg,
       "output": output,
       "output1State": output1State,
       "output2State": output2State,
       "output3State": output3State,
       "output4State": output4State}
)
