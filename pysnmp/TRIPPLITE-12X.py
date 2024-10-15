# SNMP MIB module (TRIPPLITE-12X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRIPPLITE-12X
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:47 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")

(tripplite,) = mibBuilder.importSymbols(
    "TRIPPLITE",
    "tripplite")

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY

tlPowerAlert = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 850, 90)
)
tlPowerAlert.setRevisions(
        ("2015-07-29 00:00",
         "2014-10-17 09:30",
         "2014-09-18 10:00",
         "2014-08-06 08:30",
         "2014-05-08 08:30",
         "2014-04-09 10:00",
         "2013-10-30 13:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TlEnumerations_ObjectIdentity = ObjectIdentity
tlEnumerations = _TlEnumerations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2)
)
_TlOperatingSystems_ObjectIdentity = ObjectIdentity
tlOperatingSystems = _TlOperatingSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1)
)
_Hpux9_ObjectIdentity = ObjectIdentity
hpux9 = _Hpux9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 1)
)
_Sunos4_ObjectIdentity = ObjectIdentity
sunos4 = _Sunos4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 2)
)
_Solaris_ObjectIdentity = ObjectIdentity
solaris = _Solaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 3)
)
_Osf_ObjectIdentity = ObjectIdentity
osf = _Osf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 4)
)
_Ultrix_ObjectIdentity = ObjectIdentity
ultrix = _Ultrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 5)
)
_Hpux10_ObjectIdentity = ObjectIdentity
hpux10 = _Hpux10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 6)
)
_Netbsd1_ObjectIdentity = ObjectIdentity
netbsd1 = _Netbsd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 7)
)
_Freebsd_ObjectIdentity = ObjectIdentity
freebsd = _Freebsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 8)
)
_Irix_ObjectIdentity = ObjectIdentity
irix = _Irix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 9)
)
_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 10)
)
_Bsdi_ObjectIdentity = ObjectIdentity
bsdi = _Bsdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 11)
)
_Openbsd_ObjectIdentity = ObjectIdentity
openbsd = _Openbsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 12)
)
_Win32_ObjectIdentity = ObjectIdentity
win32 = _Win32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 13)
)
_Hpux11_ObjectIdentity = ObjectIdentity
hpux11 = _Hpux11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 14)
)
_Win9x_ObjectIdentity = ObjectIdentity
win9x = _Win9x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 50)
)
_Winnt_ObjectIdentity = ObjectIdentity
winnt = _Winnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 51)
)
_Solspark_ObjectIdentity = ObjectIdentity
solspark = _Solspark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 52)
)
_Solintel_ObjectIdentity = ObjectIdentity
solintel = _Solintel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 53)
)
_Aix_ObjectIdentity = ObjectIdentity
aix = _Aix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 54)
)
_Sco_ObjectIdentity = ObjectIdentity
sco = _Sco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 55)
)
_Osx_ObjectIdentity = ObjectIdentity
osx = _Osx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 56)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 2, 1, 255)
)
_TlConformance_ObjectIdentity = ObjectIdentity
tlConformance = _TlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20)
)
_TlCompliances_ObjectIdentity = ObjectIdentity
tlCompliances = _TlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 1)
)
_TlGroups_ObjectIdentity = ObjectIdentity
tlGroups = _TlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2)
)
_TlSubsetGroups_ObjectIdentity = ObjectIdentity
tlSubsetGroups = _TlSubsetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 1)
)
_TlBasicGroups_ObjectIdentity = ObjectIdentity
tlBasicGroups = _TlBasicGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 2)
)
_TlFullGroups_ObjectIdentity = ObjectIdentity
tlFullGroups = _TlFullGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3)
)
_TlUpsFullGroups_ObjectIdentity = ObjectIdentity
tlUpsFullGroups = _TlUpsFullGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100)
)
_TlUpsFullAlarmGroup_ObjectIdentity = ObjectIdentity
tlUpsFullAlarmGroup = _TlUpsFullAlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 6)
)
_TlPASystem_ObjectIdentity = ObjectIdentity
tlPASystem = _TlPASystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 90, 1)
)
_TlPAContacts_ObjectIdentity = ObjectIdentity
tlPAContacts = _TlPAContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1)
)
_TlPAEmailContacts_ObjectIdentity = ObjectIdentity
tlPAEmailContacts = _TlPAEmailContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1)
)
_TlPANumberOfEmailContacts_Type = NonNegativeInteger
_TlPANumberOfEmailContacts_Object = MibScalar
tlPANumberOfEmailContacts = _TlPANumberOfEmailContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 1),
    _TlPANumberOfEmailContacts_Type()
)
tlPANumberOfEmailContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlPANumberOfEmailContacts.setStatus("current")
_TlPAEmailContactsTable_Object = MibTable
tlPAEmailContactsTable = _TlPAEmailContactsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tlPAEmailContactsTable.setStatus("current")
_TlPAEmailContactEntry_Object = MibTableRow
tlPAEmailContactEntry = _TlPAEmailContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2, 1)
)
tlPAEmailContactEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlPAEmailContactIndex"),
)
if mibBuilder.loadTexts:
    tlPAEmailContactEntry.setStatus("current")
_TlPAEmailContactIndex_Type = PositiveInteger
_TlPAEmailContactIndex_Object = MibTableColumn
tlPAEmailContactIndex = _TlPAEmailContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2, 1, 1),
    _TlPAEmailContactIndex_Type()
)
tlPAEmailContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlPAEmailContactIndex.setStatus("current")
_TlPAEmailContactRowStatus_Type = RowStatus
_TlPAEmailContactRowStatus_Object = MibTableColumn
tlPAEmailContactRowStatus = _TlPAEmailContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2, 1, 2),
    _TlPAEmailContactRowStatus_Type()
)
tlPAEmailContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPAEmailContactRowStatus.setStatus("current")
_TlPAEmailContactName_Type = DisplayString
_TlPAEmailContactName_Object = MibTableColumn
tlPAEmailContactName = _TlPAEmailContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2, 1, 3),
    _TlPAEmailContactName_Type()
)
tlPAEmailContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPAEmailContactName.setStatus("current")
_TlPAEmailContactAddress_Type = DisplayString
_TlPAEmailContactAddress_Object = MibTableColumn
tlPAEmailContactAddress = _TlPAEmailContactAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 1, 2, 1, 4),
    _TlPAEmailContactAddress_Type()
)
tlPAEmailContactAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPAEmailContactAddress.setStatus("current")
_TlPASnmpContacts_ObjectIdentity = ObjectIdentity
tlPASnmpContacts = _TlPASnmpContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2)
)
_TlPANumberOfSnmpContacts_Type = NonNegativeInteger
_TlPANumberOfSnmpContacts_Object = MibScalar
tlPANumberOfSnmpContacts = _TlPANumberOfSnmpContacts_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 1),
    _TlPANumberOfSnmpContacts_Type()
)
tlPANumberOfSnmpContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlPANumberOfSnmpContacts.setStatus("current")
_TlPASnmpContactsTable_Object = MibTable
tlPASnmpContactsTable = _TlPASnmpContactsTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tlPASnmpContactsTable.setStatus("current")
_TlPASnmpContactEntry_Object = MibTableRow
tlPASnmpContactEntry = _TlPASnmpContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1)
)
tlPASnmpContactEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlPASnmpContactIndex"),
)
if mibBuilder.loadTexts:
    tlPASnmpContactEntry.setStatus("current")
_TlPASnmpContactIndex_Type = PositiveInteger
_TlPASnmpContactIndex_Object = MibTableColumn
tlPASnmpContactIndex = _TlPASnmpContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 1),
    _TlPASnmpContactIndex_Type()
)
tlPASnmpContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlPASnmpContactIndex.setStatus("current")
_TlPASnmpContactRowStatus_Type = RowStatus
_TlPASnmpContactRowStatus_Object = MibTableColumn
tlPASnmpContactRowStatus = _TlPASnmpContactRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 2),
    _TlPASnmpContactRowStatus_Type()
)
tlPASnmpContactRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactRowStatus.setStatus("current")
_TlPASnmpContactName_Type = DisplayString
_TlPASnmpContactName_Object = MibTableColumn
tlPASnmpContactName = _TlPASnmpContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 3),
    _TlPASnmpContactName_Type()
)
tlPASnmpContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactName.setStatus("current")
_TlPASnmpContactIpAddress_Type = DisplayString
_TlPASnmpContactIpAddress_Object = MibTableColumn
tlPASnmpContactIpAddress = _TlPASnmpContactIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 4),
    _TlPASnmpContactIpAddress_Type()
)
tlPASnmpContactIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactIpAddress.setStatus("current")
_TlPASnmpContactPort_Type = PositiveInteger
_TlPASnmpContactPort_Object = MibTableColumn
tlPASnmpContactPort = _TlPASnmpContactPort_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 5),
    _TlPASnmpContactPort_Type()
)
tlPASnmpContactPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactPort.setStatus("current")


class _TlPASnmpContactSnmpVersion_Type(Integer32):
    """Custom type tlPASnmpContactSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2),
          ("snmpv3", 3))
    )


_TlPASnmpContactSnmpVersion_Type.__name__ = "Integer32"
_TlPASnmpContactSnmpVersion_Object = MibTableColumn
tlPASnmpContactSnmpVersion = _TlPASnmpContactSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 6),
    _TlPASnmpContactSnmpVersion_Type()
)
tlPASnmpContactSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactSnmpVersion.setStatus("current")
_TlPASnmpContactSecurityName_Type = DisplayString
_TlPASnmpContactSecurityName_Object = MibTableColumn
tlPASnmpContactSecurityName = _TlPASnmpContactSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 7),
    _TlPASnmpContactSecurityName_Type()
)
tlPASnmpContactSecurityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactSecurityName.setStatus("current")
_TlPASnmpContactPrivPassword_Type = DisplayString
_TlPASnmpContactPrivPassword_Object = MibTableColumn
tlPASnmpContactPrivPassword = _TlPASnmpContactPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 8),
    _TlPASnmpContactPrivPassword_Type()
)
tlPASnmpContactPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactPrivPassword.setStatus("current")
_TlPASnmpContactAuthPassword_Type = DisplayString
_TlPASnmpContactAuthPassword_Object = MibTableColumn
tlPASnmpContactAuthPassword = _TlPASnmpContactAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 850, 90, 1, 1, 2, 2, 1, 9),
    _TlPASnmpContactAuthPassword_Type()
)
tlPASnmpContactAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlPASnmpContactAuthPassword.setStatus("current")
_TlUPS_ObjectIdentity = ObjectIdentity
tlUPS = _TlUPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100)
)
_TlUpsObjects_ObjectIdentity = ObjectIdentity
tlUpsObjects = _TlUpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1)
)
_TlUpsIdent_ObjectIdentity = ObjectIdentity
tlUpsIdent = _TlUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1)
)
_TlUpsIdentUpsSoftwareChecksum_Type = Integer32
_TlUpsIdentUpsSoftwareChecksum_Object = MibScalar
tlUpsIdentUpsSoftwareChecksum = _TlUpsIdentUpsSoftwareChecksum_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 1),
    _TlUpsIdentUpsSoftwareChecksum_Type()
)
tlUpsIdentUpsSoftwareChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsIdentUpsSoftwareChecksum.setStatus("current")
_TlUpsIdentSerialNum_Type = DisplayString
_TlUpsIdentSerialNum_Object = MibScalar
tlUpsIdentSerialNum = _TlUpsIdentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 2),
    _TlUpsIdentSerialNum_Type()
)
tlUpsIdentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsIdentSerialNum.setStatus("current")


class _TlUpsIdentID_Type(Integer32):
    """Custom type tlUpsIdentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TlUpsIdentID_Type.__name__ = "Integer32"
_TlUpsIdentID_Object = MibScalar
tlUpsIdentID = _TlUpsIdentID_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 3),
    _TlUpsIdentID_Type()
)
tlUpsIdentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsIdentID.setStatus("current")
_TlUpsSnmpCardSerialNum_Type = DisplayString
_TlUpsSnmpCardSerialNum_Object = MibScalar
tlUpsSnmpCardSerialNum = _TlUpsSnmpCardSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 4),
    _TlUpsSnmpCardSerialNum_Type()
)
tlUpsSnmpCardSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsSnmpCardSerialNum.setStatus("current")


class _TlUpsSelectedDeviceID_Type(Integer32):
    """Custom type tlUpsSelectedDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TlUpsSelectedDeviceID_Type.__name__ = "Integer32"
_TlUpsSelectedDeviceID_Object = MibScalar
tlUpsSelectedDeviceID = _TlUpsSelectedDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 5),
    _TlUpsSelectedDeviceID_Type()
)
tlUpsSelectedDeviceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsSelectedDeviceID.setStatus("current")
_TlUpsLocation_Type = DisplayString
_TlUpsLocation_Object = MibScalar
tlUpsLocation = _TlUpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 1, 6),
    _TlUpsLocation_Type()
)
tlUpsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsLocation.setStatus("current")
_TlUpsBattery_ObjectIdentity = ObjectIdentity
tlUpsBattery = _TlUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 2)
)
_TlUpsBatteryAge_Type = DisplayString
_TlUpsBatteryAge_Object = MibScalar
tlUpsBatteryAge = _TlUpsBatteryAge_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 2, 1),
    _TlUpsBatteryAge_Type()
)
tlUpsBatteryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsBatteryAge.setStatus("current")
_TlUpsTemperatureF_Type = Integer32
_TlUpsTemperatureF_Object = MibScalar
tlUpsTemperatureF = _TlUpsTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 2, 2),
    _TlUpsTemperatureF_Type()
)
tlUpsTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsTemperatureF.setStatus("current")
_TlUpsExternalBatteryAge_Type = DisplayString
_TlUpsExternalBatteryAge_Object = MibScalar
tlUpsExternalBatteryAge = _TlUpsExternalBatteryAge_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 2, 3),
    _TlUpsExternalBatteryAge_Type()
)
tlUpsExternalBatteryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsExternalBatteryAge.setStatus("current")
_TlUpsInput_ObjectIdentity = ObjectIdentity
tlUpsInput = _TlUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3)
)
_TlUpsInputNumVoltages_Type = NonNegativeInteger
_TlUpsInputNumVoltages_Object = MibScalar
tlUpsInputNumVoltages = _TlUpsInputNumVoltages_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 1),
    _TlUpsInputNumVoltages_Type()
)
tlUpsInputNumVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputNumVoltages.setStatus("current")
_TlUpsInputVoltageTable_Object = MibTable
tlUpsInputVoltageTable = _TlUpsInputVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tlUpsInputVoltageTable.setStatus("current")
_TlUpsInputVoltageEntry_Object = MibTableRow
tlUpsInputVoltageEntry = _TlUpsInputVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 2, 1)
)
tlUpsInputVoltageEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlUpsInputVoltageIndex"),
)
if mibBuilder.loadTexts:
    tlUpsInputVoltageEntry.setStatus("current")
_TlUpsInputVoltageIndex_Type = PositiveInteger
_TlUpsInputVoltageIndex_Object = MibTableColumn
tlUpsInputVoltageIndex = _TlUpsInputVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 2, 1, 1),
    _TlUpsInputVoltageIndex_Type()
)
tlUpsInputVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlUpsInputVoltageIndex.setStatus("current")


class _TlUpsInputVoltageType_Type(Integer32):
    """Custom type tlUpsInputVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("phaseToNeutral", 0),
          ("phaseToPhase", 1))
    )


_TlUpsInputVoltageType_Type.__name__ = "Integer32"
_TlUpsInputVoltageType_Object = MibTableColumn
tlUpsInputVoltageType = _TlUpsInputVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 2, 1, 2),
    _TlUpsInputVoltageType_Type()
)
tlUpsInputVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputVoltageType.setStatus("current")
_TlUpsInputVoltage_Type = NonNegativeInteger
_TlUpsInputVoltage_Object = MibTableColumn
tlUpsInputVoltage = _TlUpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 2, 1, 3),
    _TlUpsInputVoltage_Type()
)
tlUpsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsInputVoltage.setUnits("RMS Volts")


class _TlUpsInputSourceSelect_Type(Integer32):
    """Custom type tlUpsInputSourceSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 0),
          ("inputSourceB", 1))
    )


_TlUpsInputSourceSelect_Type.__name__ = "Integer32"
_TlUpsInputSourceSelect_Object = MibScalar
tlUpsInputSourceSelect = _TlUpsInputSourceSelect_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 3),
    _TlUpsInputSourceSelect_Type()
)
tlUpsInputSourceSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsInputSourceSelect.setStatus("current")
_TlUpsPhaseImbalance_Type = Integer32
_TlUpsPhaseImbalance_Object = MibScalar
tlUpsPhaseImbalance = _TlUpsPhaseImbalance_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 4),
    _TlUpsPhaseImbalance_Type()
)
tlUpsPhaseImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsPhaseImbalance.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsPhaseImbalance.setUnits("Percent")


class _TlUpsInputSourceAvailability_Type(Integer32):
    """Custom type tlUpsInputSourceAvailability based on Integer32"""
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
        *(("inputSourceA", 1),
          ("inputSourceAB", 3),
          ("inputSourceB", 2),
          ("none", 0))
    )


_TlUpsInputSourceAvailability_Type.__name__ = "Integer32"
_TlUpsInputSourceAvailability_Object = MibScalar
tlUpsInputSourceAvailability = _TlUpsInputSourceAvailability_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 5),
    _TlUpsInputSourceAvailability_Type()
)
tlUpsInputSourceAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputSourceAvailability.setStatus("current")


class _TlUpsInputSourceInUse_Type(Integer32):
    """Custom type tlUpsInputSourceInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inputSourceA", 0),
          ("inputSourceB", 1))
    )


_TlUpsInputSourceInUse_Type.__name__ = "Integer32"
_TlUpsInputSourceInUse_Object = MibScalar
tlUpsInputSourceInUse = _TlUpsInputSourceInUse_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 6),
    _TlUpsInputSourceInUse_Type()
)
tlUpsInputSourceInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputSourceInUse.setStatus("current")
_TlUpsInputSourceTransitionCount_Type = PositiveInteger
_TlUpsInputSourceTransitionCount_Object = MibScalar
tlUpsInputSourceTransitionCount = _TlUpsInputSourceTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 3, 7),
    _TlUpsInputSourceTransitionCount_Type()
)
tlUpsInputSourceTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsInputSourceTransitionCount.setStatus("current")
_TlUpsOutput_ObjectIdentity = ObjectIdentity
tlUpsOutput = _TlUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4)
)
_TlUpsOutputPowerTotal_Type = PositiveInteger
_TlUpsOutputPowerTotal_Object = MibScalar
tlUpsOutputPowerTotal = _TlUpsOutputPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 5),
    _TlUpsOutputPowerTotal_Type()
)
tlUpsOutputPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputPowerTotal.setStatus("current")
_TlUpsOutputCircuits_Type = NonNegativeInteger
_TlUpsOutputCircuits_Object = MibScalar
tlUpsOutputCircuits = _TlUpsOutputCircuits_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 6),
    _TlUpsOutputCircuits_Type()
)
tlUpsOutputCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuits.setStatus("current")
_TlUpsOutputCircuitTable_Object = MibTable
tlUpsOutputCircuitTable = _TlUpsOutputCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tlUpsOutputCircuitTable.setStatus("current")
_TlUpsOutputCircuitEntry_Object = MibTableRow
tlUpsOutputCircuitEntry = _TlUpsOutputCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1)
)
tlUpsOutputCircuitEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlUpsOutputCircuitIndex"),
)
if mibBuilder.loadTexts:
    tlUpsOutputCircuitEntry.setStatus("current")
_TlUpsOutputCircuitIndex_Type = PositiveInteger
_TlUpsOutputCircuitIndex_Object = MibTableColumn
tlUpsOutputCircuitIndex = _TlUpsOutputCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 1),
    _TlUpsOutputCircuitIndex_Type()
)
tlUpsOutputCircuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitIndex.setStatus("current")


class _TlUpsOutputCircuitStatus_Type(Integer32):
    """Custom type tlUpsOutputCircuitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_TlUpsOutputCircuitStatus_Type.__name__ = "Integer32"
_TlUpsOutputCircuitStatus_Object = MibTableColumn
tlUpsOutputCircuitStatus = _TlUpsOutputCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 2),
    _TlUpsOutputCircuitStatus_Type()
)
tlUpsOutputCircuitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitStatus.setStatus("current")
_TlUpsOutputCircuitLoadCurrent_Type = NonNegativeInteger
_TlUpsOutputCircuitLoadCurrent_Object = MibTableColumn
tlUpsOutputCircuitLoadCurrent = _TlUpsOutputCircuitLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 3),
    _TlUpsOutputCircuitLoadCurrent_Type()
)
tlUpsOutputCircuitLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitLoadCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitLoadCurrent.setUnits("0.1 Amperes")
_TlUpsOutputCircuitVoltage_Type = NonNegativeInteger
_TlUpsOutputCircuitVoltage_Object = MibTableColumn
tlUpsOutputCircuitVoltage = _TlUpsOutputCircuitVoltage_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 4),
    _TlUpsOutputCircuitVoltage_Type()
)
tlUpsOutputCircuitVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitVoltage.setUnits("0.1 Volts")
_TlUpsOutputCircuitPower_Type = NonNegativeInteger
_TlUpsOutputCircuitPower_Object = MibTableColumn
tlUpsOutputCircuitPower = _TlUpsOutputCircuitPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 5),
    _TlUpsOutputCircuitPower_Type()
)
tlUpsOutputCircuitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitPower.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitPower.setUnits("Watts")
_TlUpsOutputCircuitPowerFactor_Type = NonNegativeInteger
_TlUpsOutputCircuitPowerFactor_Object = MibTableColumn
tlUpsOutputCircuitPowerFactor = _TlUpsOutputCircuitPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 7, 1, 6),
    _TlUpsOutputCircuitPowerFactor_Type()
)
tlUpsOutputCircuitPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsOutputCircuitPowerFactor.setUnits("Percent")
_TlUpsAggregatePowerFactor_Type = PositiveInteger
_TlUpsAggregatePowerFactor_Object = MibScalar
tlUpsAggregatePowerFactor = _TlUpsAggregatePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 4, 8),
    _TlUpsAggregatePowerFactor_Type()
)
tlUpsAggregatePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAggregatePowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsAggregatePowerFactor.setUnits("0.1 Watts")
_TlUpsAlarm_ObjectIdentity = ObjectIdentity
tlUpsAlarm = _TlUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6)
)
_TlUpsAlarmsPresent_Type = Gauge32
_TlUpsAlarmsPresent_Object = MibScalar
tlUpsAlarmsPresent = _TlUpsAlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 1),
    _TlUpsAlarmsPresent_Type()
)
tlUpsAlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmsPresent.setStatus("current")
_TlUpsAlarmTable_Object = MibTable
tlUpsAlarmTable = _TlUpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tlUpsAlarmTable.setStatus("current")
_TlUpsAlarmEntry_Object = MibTableRow
tlUpsAlarmEntry = _TlUpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1)
)
tlUpsAlarmEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlUpsAlarmId"),
)
if mibBuilder.loadTexts:
    tlUpsAlarmEntry.setStatus("current")
_TlUpsAlarmId_Type = PositiveInteger
_TlUpsAlarmId_Object = MibTableColumn
tlUpsAlarmId = _TlUpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 1),
    _TlUpsAlarmId_Type()
)
tlUpsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmId.setStatus("current")
_TlUpsAlarmDescr_Type = AutonomousType
_TlUpsAlarmDescr_Object = MibTableColumn
tlUpsAlarmDescr = _TlUpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 2),
    _TlUpsAlarmDescr_Type()
)
tlUpsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDescr.setStatus("current")
_TlUpsAlarmTime_Type = TimeStamp
_TlUpsAlarmTime_Object = MibTableColumn
tlUpsAlarmTime = _TlUpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 3),
    _TlUpsAlarmTime_Type()
)
tlUpsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmTime.setStatus("current")
_TlUpsAlarmDetail_Type = DisplayString
_TlUpsAlarmDetail_Object = MibTableColumn
tlUpsAlarmDetail = _TlUpsAlarmDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 4),
    _TlUpsAlarmDetail_Type()
)
tlUpsAlarmDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDetail.setStatus("current")
_TlUpsAlarmDeviceId_Type = PositiveInteger
_TlUpsAlarmDeviceId_Object = MibTableColumn
tlUpsAlarmDeviceId = _TlUpsAlarmDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 5),
    _TlUpsAlarmDeviceId_Type()
)
tlUpsAlarmDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDeviceId.setStatus("current")
_TlUpsAlarmDeviceName_Type = DisplayString
_TlUpsAlarmDeviceName_Object = MibTableColumn
tlUpsAlarmDeviceName = _TlUpsAlarmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 6),
    _TlUpsAlarmDeviceName_Type()
)
tlUpsAlarmDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDeviceName.setStatus("current")
_TlUpsAlarmLocation_Type = DisplayString
_TlUpsAlarmLocation_Object = MibTableColumn
tlUpsAlarmLocation = _TlUpsAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 7),
    _TlUpsAlarmLocation_Type()
)
tlUpsAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmLocation.setStatus("current")


class _TlUpsAlarmGroup_Type(Integer32):
    """Custom type tlUpsAlarmGroup based on Integer32"""
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
        *(("critical", 1),
          ("custom", 6),
          ("info", 3),
          ("offline", 5),
          ("status", 4),
          ("warning", 2))
    )


_TlUpsAlarmGroup_Type.__name__ = "Integer32"
_TlUpsAlarmGroup_Object = MibTableColumn
tlUpsAlarmGroup = _TlUpsAlarmGroup_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 8),
    _TlUpsAlarmGroup_Type()
)
tlUpsAlarmGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmGroup.setStatus("current")
_TlUpsAlarmIp_Type = IpAddress
_TlUpsAlarmIp_Object = MibTableColumn
tlUpsAlarmIp = _TlUpsAlarmIp_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 9),
    _TlUpsAlarmIp_Type()
)
tlUpsAlarmIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmIp.setStatus("current")
_TlUpsAlarmMac_Type = DisplayString
_TlUpsAlarmMac_Object = MibTableColumn
tlUpsAlarmMac = _TlUpsAlarmMac_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 2, 1, 10),
    _TlUpsAlarmMac_Type()
)
tlUpsAlarmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmMac.setStatus("current")
_TlUpsWellKnownAlarms_ObjectIdentity = ObjectIdentity
tlUpsWellKnownAlarms = _TlUpsWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3)
)
_TlUpsAlarmPrimaryPowerOutage_ObjectIdentity = ObjectIdentity
tlUpsAlarmPrimaryPowerOutage = _TlUpsAlarmPrimaryPowerOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tlUpsAlarmPrimaryPowerOutage.setStatus("current")
_TlUpsAlarmSecondaryPowerOutage_ObjectIdentity = ObjectIdentity
tlUpsAlarmSecondaryPowerOutage = _TlUpsAlarmSecondaryPowerOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    tlUpsAlarmSecondaryPowerOutage.setStatus("current")
_TlUpsAlarmLoadLevelAboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmLoadLevelAboveThreshold = _TlUpsAlarmLoadLevelAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    tlUpsAlarmLoadLevelAboveThreshold.setStatus("current")
_TlUpsAlarmOutputCurrentChanged_ObjectIdentity = ObjectIdentity
tlUpsAlarmOutputCurrentChanged = _TlUpsAlarmOutputCurrentChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOutputCurrentChanged.setStatus("current")
_TlUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmBatteryAgeAboveThreshold = _TlUpsAlarmBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBatteryAgeAboveThreshold.setStatus("current")
_TlUpsAlarmLoadOff_ObjectIdentity = ObjectIdentity
tlUpsAlarmLoadOff = _TlUpsAlarmLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 6)
)
if mibBuilder.loadTexts:
    tlUpsAlarmLoadOff.setStatus("current")
_TlUpsAlarmUserDefined_ObjectIdentity = ObjectIdentity
tlUpsAlarmUserDefined = _TlUpsAlarmUserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 7)
)
if mibBuilder.loadTexts:
    tlUpsAlarmUserDefined.setStatus("current")
_TlUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmBatteryBad = _TlUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 8)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBatteryBad.setStatus("current")
_TlUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
tlUpsAlarmOnBattery = _TlUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 9)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOnBattery.setStatus("current")
_TlUpsAlarmLowBattery_ObjectIdentity = ObjectIdentity
tlUpsAlarmLowBattery = _TlUpsAlarmLowBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 10)
)
if mibBuilder.loadTexts:
    tlUpsAlarmLowBattery.setStatus("current")
_TlUpsAlarmDepletedBattery_ObjectIdentity = ObjectIdentity
tlUpsAlarmDepletedBattery = _TlUpsAlarmDepletedBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 11)
)
if mibBuilder.loadTexts:
    tlUpsAlarmDepletedBattery.setStatus("current")
_TlUpsAlarmTempBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmTempBad = _TlUpsAlarmTempBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 12)
)
if mibBuilder.loadTexts:
    tlUpsAlarmTempBad.setStatus("current")
_TlUpsAlarmInputBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmInputBad = _TlUpsAlarmInputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 13)
)
if mibBuilder.loadTexts:
    tlUpsAlarmInputBad.setStatus("current")
_TlUpsAlarmOutputBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmOutputBad = _TlUpsAlarmOutputBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 14)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOutputBad.setStatus("current")
_TlUpsAlarmOutputOverload_ObjectIdentity = ObjectIdentity
tlUpsAlarmOutputOverload = _TlUpsAlarmOutputOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 15)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOutputOverload.setStatus("current")
_TlUpsAlarmOnBypass_ObjectIdentity = ObjectIdentity
tlUpsAlarmOnBypass = _TlUpsAlarmOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 16)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOnBypass.setStatus("current")
_TlUpsAlarmBypassBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmBypassBad = _TlUpsAlarmBypassBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 17)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBypassBad.setStatus("current")
_TlUpsAlarmOutputOffAsRequested_ObjectIdentity = ObjectIdentity
tlUpsAlarmOutputOffAsRequested = _TlUpsAlarmOutputOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 18)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOutputOffAsRequested.setStatus("current")
_TlUpsAlarmUpsOffAsRequested_ObjectIdentity = ObjectIdentity
tlUpsAlarmUpsOffAsRequested = _TlUpsAlarmUpsOffAsRequested_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 19)
)
if mibBuilder.loadTexts:
    tlUpsAlarmUpsOffAsRequested.setStatus("current")
_TlUpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
tlUpsAlarmChargerFailed = _TlUpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 20)
)
if mibBuilder.loadTexts:
    tlUpsAlarmChargerFailed.setStatus("current")
_TlUpsAlarmUpsOutputOff_ObjectIdentity = ObjectIdentity
tlUpsAlarmUpsOutputOff = _TlUpsAlarmUpsOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 21)
)
if mibBuilder.loadTexts:
    tlUpsAlarmUpsOutputOff.setStatus("current")
_TlUpsAlarmUpsSystemOff_ObjectIdentity = ObjectIdentity
tlUpsAlarmUpsSystemOff = _TlUpsAlarmUpsSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 22)
)
if mibBuilder.loadTexts:
    tlUpsAlarmUpsSystemOff.setStatus("current")
_TlUpsAlarmFanFailure_ObjectIdentity = ObjectIdentity
tlUpsAlarmFanFailure = _TlUpsAlarmFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 23)
)
if mibBuilder.loadTexts:
    tlUpsAlarmFanFailure.setStatus("current")
_TlUpsAlarmFuseFailure_ObjectIdentity = ObjectIdentity
tlUpsAlarmFuseFailure = _TlUpsAlarmFuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 24)
)
if mibBuilder.loadTexts:
    tlUpsAlarmFuseFailure.setStatus("current")
_TlUpsAlarmGeneralFault_ObjectIdentity = ObjectIdentity
tlUpsAlarmGeneralFault = _TlUpsAlarmGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 25)
)
if mibBuilder.loadTexts:
    tlUpsAlarmGeneralFault.setStatus("current")
_TlUpsAlarmDiagnosticTestFailed_ObjectIdentity = ObjectIdentity
tlUpsAlarmDiagnosticTestFailed = _TlUpsAlarmDiagnosticTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 26)
)
if mibBuilder.loadTexts:
    tlUpsAlarmDiagnosticTestFailed.setStatus("current")
_TlUpsAlarmCommunicationsLost_ObjectIdentity = ObjectIdentity
tlUpsAlarmCommunicationsLost = _TlUpsAlarmCommunicationsLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 27)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCommunicationsLost.setStatus("current")
_TlUpsAlarmAwaitingPower_ObjectIdentity = ObjectIdentity
tlUpsAlarmAwaitingPower = _TlUpsAlarmAwaitingPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 28)
)
if mibBuilder.loadTexts:
    tlUpsAlarmAwaitingPower.setStatus("current")
_TlUpsAlarmShutdownPending_ObjectIdentity = ObjectIdentity
tlUpsAlarmShutdownPending = _TlUpsAlarmShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 29)
)
if mibBuilder.loadTexts:
    tlUpsAlarmShutdownPending.setStatus("current")
_TlUpsAlarmShutdownImminent_ObjectIdentity = ObjectIdentity
tlUpsAlarmShutdownImminent = _TlUpsAlarmShutdownImminent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 30)
)
if mibBuilder.loadTexts:
    tlUpsAlarmShutdownImminent.setStatus("current")
_TlUpsAlarmTestInProgress_ObjectIdentity = ObjectIdentity
tlUpsAlarmTestInProgress = _TlUpsAlarmTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 31)
)
if mibBuilder.loadTexts:
    tlUpsAlarmTestInProgress.setStatus("current")
_TlUpsAlarmCircuitBreaker1Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker1Open = _TlUpsAlarmCircuitBreaker1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 32)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker1Open.setStatus("current")
_TlUpsAlarmCircuitBreaker2Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker2Open = _TlUpsAlarmCircuitBreaker2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 33)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker2Open.setStatus("current")
_TlUpsAlarmCircuitBreaker3Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker3Open = _TlUpsAlarmCircuitBreaker3Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 34)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker3Open.setStatus("current")
_TlUpsAlarmCircuitBreaker4Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker4Open = _TlUpsAlarmCircuitBreaker4Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 35)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker4Open.setStatus("current")
_TlUpsAlarmCircuitBreaker5Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker5Open = _TlUpsAlarmCircuitBreaker5Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 36)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker5Open.setStatus("current")
_TlUpsAlarmCircuitBreaker6Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker6Open = _TlUpsAlarmCircuitBreaker6Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 37)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker6Open.setStatus("current")
_TlUpsAlarmCircuitBreaker7Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker7Open = _TlUpsAlarmCircuitBreaker7Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 38)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker7Open.setStatus("current")
_TlUpsAlarmCircuitBreaker8Open_ObjectIdentity = ObjectIdentity
tlUpsAlarmCircuitBreaker8Open = _TlUpsAlarmCircuitBreaker8Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 39)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCircuitBreaker8Open.setStatus("current")
_TlUpsAlarmCurrent1AboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmCurrent1AboveThreshold = _TlUpsAlarmCurrent1AboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 40)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCurrent1AboveThreshold.setStatus("current")
_TlUpsAlarmCurrent2AboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmCurrent2AboveThreshold = _TlUpsAlarmCurrent2AboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 41)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCurrent2AboveThreshold.setStatus("current")
_TlUpsAlarmCurrent3AboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmCurrent3AboveThreshold = _TlUpsAlarmCurrent3AboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 42)
)
if mibBuilder.loadTexts:
    tlUpsAlarmCurrent3AboveThreshold.setStatus("current")
_TlUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity = ObjectIdentity
tlUpsAlarmRuntimeBelowWarningLevel = _TlUpsAlarmRuntimeBelowWarningLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 43)
)
if mibBuilder.loadTexts:
    tlUpsAlarmRuntimeBelowWarningLevel.setStatus("current")
_TlUpsAlarmBusStartVoltageLow_ObjectIdentity = ObjectIdentity
tlUpsAlarmBusStartVoltageLow = _TlUpsAlarmBusStartVoltageLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 44)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBusStartVoltageLow.setStatus("current")
_TlUpsAlarmBusOverVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmBusOverVoltage = _TlUpsAlarmBusOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 45)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBusOverVoltage.setStatus("current")
_TlUpsAlarmBusUnderVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmBusUnderVoltage = _TlUpsAlarmBusUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 46)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBusUnderVoltage.setStatus("current")
_TlUpsAlarmBusVoltageUnbalanced_ObjectIdentity = ObjectIdentity
tlUpsAlarmBusVoltageUnbalanced = _TlUpsAlarmBusVoltageUnbalanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 47)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBusVoltageUnbalanced.setStatus("current")
_TlUpsAlarmInverterSoftStartBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmInverterSoftStartBad = _TlUpsAlarmInverterSoftStartBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 48)
)
if mibBuilder.loadTexts:
    tlUpsAlarmInverterSoftStartBad.setStatus("current")
_TlUpsAlarmInverterOverVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmInverterOverVoltage = _TlUpsAlarmInverterOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 49)
)
if mibBuilder.loadTexts:
    tlUpsAlarmInverterOverVoltage.setStatus("current")
_TlUpsAlarmInverterUnderVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmInverterUnderVoltage = _TlUpsAlarmInverterUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 50)
)
if mibBuilder.loadTexts:
    tlUpsAlarmInverterUnderVoltage.setStatus("current")
_TlUpsAlarmInverterCircuitBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmInverterCircuitBad = _TlUpsAlarmInverterCircuitBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 51)
)
if mibBuilder.loadTexts:
    tlUpsAlarmInverterCircuitBad.setStatus("current")
_TlUpsAlarmBatteryOverVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmBatteryOverVoltage = _TlUpsAlarmBatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 52)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBatteryOverVoltage.setStatus("current")
_TlUpsAlarmBatteryUnderVoltage_ObjectIdentity = ObjectIdentity
tlUpsAlarmBatteryUnderVoltage = _TlUpsAlarmBatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 53)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBatteryUnderVoltage.setStatus("current")
_TlUpsAlarmSiteWiringFault_ObjectIdentity = ObjectIdentity
tlUpsAlarmSiteWiringFault = _TlUpsAlarmSiteWiringFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 54)
)
if mibBuilder.loadTexts:
    tlUpsAlarmSiteWiringFault.setStatus("current")
_TlUpsAlarmOverTemperatureProtection_ObjectIdentity = ObjectIdentity
tlUpsAlarmOverTemperatureProtection = _TlUpsAlarmOverTemperatureProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 55)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOverTemperatureProtection.setStatus("current")
_TlUpsAlarmOverCharged_ObjectIdentity = ObjectIdentity
tlUpsAlarmOverCharged = _TlUpsAlarmOverCharged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 56)
)
if mibBuilder.loadTexts:
    tlUpsAlarmOverCharged.setStatus("current")
_TlUpsAlarmEPOActive_ObjectIdentity = ObjectIdentity
tlUpsAlarmEPOActive = _TlUpsAlarmEPOActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 57)
)
if mibBuilder.loadTexts:
    tlUpsAlarmEPOActive.setStatus("current")
_TlUpsAlarmBypassFrequencyBad_ObjectIdentity = ObjectIdentity
tlUpsAlarmBypassFrequencyBad = _TlUpsAlarmBypassFrequencyBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 58)
)
if mibBuilder.loadTexts:
    tlUpsAlarmBypassFrequencyBad.setStatus("current")
_TlUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmExternalSmartBatteryAgeAboveThreshold = _TlUpsAlarmExternalSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 59)
)
if mibBuilder.loadTexts:
    tlUpsAlarmExternalSmartBatteryAgeAboveThreshold.setStatus("current")
_TlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity = ObjectIdentity
tlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold = _TlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 60)
)
if mibBuilder.loadTexts:
    tlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold.setStatus("current")
_TlUpsAlarmSmartBatteryCommLost_ObjectIdentity = ObjectIdentity
tlUpsAlarmSmartBatteryCommLost = _TlUpsAlarmSmartBatteryCommLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 61)
)
if mibBuilder.loadTexts:
    tlUpsAlarmSmartBatteryCommLost.setStatus("current")
_TlUpsAlarmSourceAOutage_ObjectIdentity = ObjectIdentity
tlUpsAlarmSourceAOutage = _TlUpsAlarmSourceAOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 62)
)
if mibBuilder.loadTexts:
    tlUpsAlarmSourceAOutage.setStatus("current")
_TlUpsAlarmSourceBOutage_ObjectIdentity = ObjectIdentity
tlUpsAlarmSourceBOutage = _TlUpsAlarmSourceBOutage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 63)
)
if mibBuilder.loadTexts:
    tlUpsAlarmSourceBOutage.setStatus("current")
_TlUpsAlarmWatchdogReset_ObjectIdentity = ObjectIdentity
tlUpsAlarmWatchdogReset = _TlUpsAlarmWatchdogReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 3, 64)
)
if mibBuilder.loadTexts:
    tlUpsAlarmWatchdogReset.setStatus("current")
_TlUpsAlarmDevName_Type = DisplayString
_TlUpsAlarmDevName_Object = MibScalar
tlUpsAlarmDevName = _TlUpsAlarmDevName_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 7),
    _TlUpsAlarmDevName_Type()
)
tlUpsAlarmDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDevName.setStatus("deprecated")
_TlUpsAlarmDevLocation_Type = DisplayString
_TlUpsAlarmDevLocation_Object = MibScalar
tlUpsAlarmDevLocation = _TlUpsAlarmDevLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 8),
    _TlUpsAlarmDevLocation_Type()
)
tlUpsAlarmDevLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmDevLocation.setStatus("deprecated")
_TlUpsAlarmCategory_Type = Integer32
_TlUpsAlarmCategory_Object = MibScalar
tlUpsAlarmCategory = _TlUpsAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 6, 9),
    _TlUpsAlarmCategory_Type()
)
tlUpsAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsAlarmCategory.setStatus("deprecated")
_TlUpsTest_ObjectIdentity = ObjectIdentity
tlUpsTest = _TlUpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 7)
)
_TlUpsTestDate_Type = DisplayString
_TlUpsTestDate_Object = MibScalar
tlUpsTestDate = _TlUpsTestDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 7, 1),
    _TlUpsTestDate_Type()
)
tlUpsTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsTestDate.setStatus("current")
_TlUpsTestResultsDetail_Type = DisplayString
_TlUpsTestResultsDetail_Object = MibScalar
tlUpsTestResultsDetail = _TlUpsTestResultsDetail_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 7, 2),
    _TlUpsTestResultsDetail_Type()
)
tlUpsTestResultsDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsTestResultsDetail.setStatus("current")
_TlUpsControl_ObjectIdentity = ObjectIdentity
tlUpsControl = _TlUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8)
)
_TlUpsWatchdogSupported_Type = TruthValue
_TlUpsWatchdogSupported_Object = MibScalar
tlUpsWatchdogSupported = _TlUpsWatchdogSupported_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 1),
    _TlUpsWatchdogSupported_Type()
)
tlUpsWatchdogSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsWatchdogSupported.setStatus("current")
_TlUpsWatchdogSecsBeforeReboot_Type = NonNegativeInteger
_TlUpsWatchdogSecsBeforeReboot_Object = MibScalar
tlUpsWatchdogSecsBeforeReboot = _TlUpsWatchdogSecsBeforeReboot_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 2),
    _TlUpsWatchdogSecsBeforeReboot_Type()
)
tlUpsWatchdogSecsBeforeReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsWatchdogSecsBeforeReboot.setStatus("current")
_TlUpsWellKnownControls_ObjectIdentity = ObjectIdentity
tlUpsWellKnownControls = _TlUpsWellKnownControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3)
)
_TlUpsControlSelfTest_Type = TruthValue
_TlUpsControlSelfTest_Object = MibScalar
tlUpsControlSelfTest = _TlUpsControlSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3, 1),
    _TlUpsControlSelfTest_Type()
)
tlUpsControlSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsControlSelfTest.setStatus("current")
_TlUpsControlRamp_Type = TruthValue
_TlUpsControlRamp_Object = MibScalar
tlUpsControlRamp = _TlUpsControlRamp_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3, 2),
    _TlUpsControlRamp_Type()
)
tlUpsControlRamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsControlRamp.setStatus("current")
_TlUpsControlShed_Type = TruthValue
_TlUpsControlShed_Object = MibScalar
tlUpsControlShed = _TlUpsControlShed_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3, 3),
    _TlUpsControlShed_Type()
)
tlUpsControlShed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsControlShed.setStatus("current")
_TlUpsControlUpsOn_Type = TruthValue
_TlUpsControlUpsOn_Object = MibScalar
tlUpsControlUpsOn = _TlUpsControlUpsOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3, 4),
    _TlUpsControlUpsOn_Type()
)
tlUpsControlUpsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsControlUpsOn.setStatus("current")
_TlUpsControlUpsOff_Type = TruthValue
_TlUpsControlUpsOff_Object = MibScalar
tlUpsControlUpsOff = _TlUpsControlUpsOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 8, 3, 5),
    _TlUpsControlUpsOff_Type()
)
tlUpsControlUpsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsControlUpsOff.setStatus("current")
_TlUpsConfig_ObjectIdentity = ObjectIdentity
tlUpsConfig = _TlUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 9)
)
_TlUpsConfigBattReplDate_Type = DisplayString
_TlUpsConfigBattReplDate_Object = MibScalar
tlUpsConfigBattReplDate = _TlUpsConfigBattReplDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 9, 1),
    _TlUpsConfigBattReplDate_Type()
)
tlUpsConfigBattReplDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsConfigBattReplDate.setStatus("current")


class _TlUpsConfigDisplayUnits_Type(Integer32):
    """Custom type tlUpsConfigDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("english", 0),
          ("metric", 1))
    )


_TlUpsConfigDisplayUnits_Type.__name__ = "Integer32"
_TlUpsConfigDisplayUnits_Object = MibScalar
tlUpsConfigDisplayUnits = _TlUpsConfigDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 9, 4),
    _TlUpsConfigDisplayUnits_Type()
)
tlUpsConfigDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsConfigDisplayUnits.setStatus("current")
_TlUpsConfigExternalBattReplDate_Type = DisplayString
_TlUpsConfigExternalBattReplDate_Object = MibScalar
tlUpsConfigExternalBattReplDate = _TlUpsConfigExternalBattReplDate_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 9, 5),
    _TlUpsConfigExternalBattReplDate_Type()
)
tlUpsConfigExternalBattReplDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsConfigExternalBattReplDate.setStatus("current")
_TlUpsOutlet_ObjectIdentity = ObjectIdentity
tlUpsOutlet = _TlUpsOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10)
)
_TlUpsOutletNumOutlets_Type = NonNegativeInteger
_TlUpsOutletNumOutlets_Object = MibScalar
tlUpsOutletNumOutlets = _TlUpsOutletNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 1),
    _TlUpsOutletNumOutlets_Type()
)
tlUpsOutletNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletNumOutlets.setStatus("current")
_TlUpsOutletTable_Object = MibTable
tlUpsOutletTable = _TlUpsOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tlUpsOutletTable.setStatus("current")
_TlUpsOutletEntry_Object = MibTableRow
tlUpsOutletEntry = _TlUpsOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1)
)
tlUpsOutletEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlUpsOutletIndex"),
)
if mibBuilder.loadTexts:
    tlUpsOutletEntry.setStatus("current")
_TlUpsOutletIndex_Type = PositiveInteger
_TlUpsOutletIndex_Object = MibTableColumn
tlUpsOutletIndex = _TlUpsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 1),
    _TlUpsOutletIndex_Type()
)
tlUpsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletIndex.setStatus("current")


class _TlUpsOutletState_Type(Integer32):
    """Custom type tlUpsOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlUpsOutletState_Type.__name__ = "Integer32"
_TlUpsOutletState_Object = MibTableColumn
tlUpsOutletState = _TlUpsOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 2),
    _TlUpsOutletState_Type()
)
tlUpsOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletState.setStatus("current")
_TlUpsOutletType_Type = Integer32
_TlUpsOutletType_Object = MibTableColumn
tlUpsOutletType = _TlUpsOutletType_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 3),
    _TlUpsOutletType_Type()
)
tlUpsOutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletType.setStatus("current")


class _TlUpsOutletControl_Type(Integer32):
    """Custom type tlUpsOutletControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlUpsOutletControl_Type.__name__ = "Integer32"
_TlUpsOutletControl_Object = MibTableColumn
tlUpsOutletControl = _TlUpsOutletControl_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 4),
    _TlUpsOutletControl_Type()
)
tlUpsOutletControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletControl.setStatus("current")
_TlUpsOutletName_Type = DisplayString
_TlUpsOutletName_Object = MibTableColumn
tlUpsOutletName = _TlUpsOutletName_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 5),
    _TlUpsOutletName_Type()
)
tlUpsOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletName.setStatus("current")


class _TlUpsOutletRampAction_Type(Integer32):
    """Custom type tlUpsOutletRampAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOff", 0),
          ("turnOnAfterDelay", 1))
    )


_TlUpsOutletRampAction_Type.__name__ = "Integer32"
_TlUpsOutletRampAction_Object = MibTableColumn
tlUpsOutletRampAction = _TlUpsOutletRampAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 6),
    _TlUpsOutletRampAction_Type()
)
tlUpsOutletRampAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletRampAction.setStatus("current")


class _TlUpsOutletRampDataType_Type(Integer32):
    """Custom type tlUpsOutletRampDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("delayInSeconds", 0)
    )


_TlUpsOutletRampDataType_Type.__name__ = "Integer32"
_TlUpsOutletRampDataType_Object = MibTableColumn
tlUpsOutletRampDataType = _TlUpsOutletRampDataType_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 7),
    _TlUpsOutletRampDataType_Type()
)
tlUpsOutletRampDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletRampDataType.setStatus("current")
_TlUpsOutletRampData_Type = Integer32
_TlUpsOutletRampData_Object = MibTableColumn
tlUpsOutletRampData = _TlUpsOutletRampData_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 8),
    _TlUpsOutletRampData_Type()
)
tlUpsOutletRampData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletRampData.setStatus("current")


class _TlUpsOutletShedAction_Type(Integer32):
    """Custom type tlUpsOutletShedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remainOn", 0),
          ("turnOffAfterDelay", 1))
    )


_TlUpsOutletShedAction_Type.__name__ = "Integer32"
_TlUpsOutletShedAction_Object = MibTableColumn
tlUpsOutletShedAction = _TlUpsOutletShedAction_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 9),
    _TlUpsOutletShedAction_Type()
)
tlUpsOutletShedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletShedAction.setStatus("current")


class _TlUpsOutletShedDataType_Type(Integer32):
    """Custom type tlUpsOutletShedDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("delayInSeconds", 0)
    )


_TlUpsOutletShedDataType_Type.__name__ = "Integer32"
_TlUpsOutletShedDataType_Object = MibTableColumn
tlUpsOutletShedDataType = _TlUpsOutletShedDataType_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 10),
    _TlUpsOutletShedDataType_Type()
)
tlUpsOutletShedDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletShedDataType.setStatus("current")
_TlUpsOutletShedData_Type = Integer32
_TlUpsOutletShedData_Object = MibTableColumn
tlUpsOutletShedData = _TlUpsOutletShedData_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 11),
    _TlUpsOutletShedData_Type()
)
tlUpsOutletShedData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletShedData.setStatus("current")
_TlUpsOutletGroupNdx_Type = Integer32
_TlUpsOutletGroupNdx_Object = MibTableColumn
tlUpsOutletGroupNdx = _TlUpsOutletGroupNdx_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 12),
    _TlUpsOutletGroupNdx_Type()
)
tlUpsOutletGroupNdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletGroupNdx.setStatus("current")
_TlUpsOutletCurrent_Type = PositiveInteger
_TlUpsOutletCurrent_Object = MibTableColumn
tlUpsOutletCurrent = _TlUpsOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 13),
    _TlUpsOutletCurrent_Type()
)
tlUpsOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tlUpsOutletCurrent.setUnits("0.1 RMS Amp")
_TlUpsOutletPower_Type = PositiveInteger
_TlUpsOutletPower_Object = MibTableColumn
tlUpsOutletPower = _TlUpsOutletPower_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 10, 2, 1, 14),
    _TlUpsOutletPower_Type()
)
tlUpsOutletPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletPower.setStatus("current")
_TlUpsOutletGroup_ObjectIdentity = ObjectIdentity
tlUpsOutletGroup = _TlUpsOutletGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11)
)
_TlUpsOutletNumOutletGroups_Type = NonNegativeInteger
_TlUpsOutletNumOutletGroups_Object = MibScalar
tlUpsOutletNumOutletGroups = _TlUpsOutletNumOutletGroups_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 1),
    _TlUpsOutletNumOutletGroups_Type()
)
tlUpsOutletNumOutletGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletNumOutletGroups.setStatus("current")
_TlUpsOutletGroupTable_Object = MibTable
tlUpsOutletGroupTable = _TlUpsOutletGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2)
)
if mibBuilder.loadTexts:
    tlUpsOutletGroupTable.setStatus("current")
_TlUpsOutletGroupEntry_Object = MibTableRow
tlUpsOutletGroupEntry = _TlUpsOutletGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1)
)
tlUpsOutletGroupEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlUpsOutletGroupIndex"),
)
if mibBuilder.loadTexts:
    tlUpsOutletGroupEntry.setStatus("current")
_TlUpsOutletGroupIndex_Type = PositiveInteger
_TlUpsOutletGroupIndex_Object = MibTableColumn
tlUpsOutletGroupIndex = _TlUpsOutletGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 1),
    _TlUpsOutletGroupIndex_Type()
)
tlUpsOutletGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletGroupIndex.setStatus("current")
_TlUpsOutletGroupRowStatus_Type = RowStatus
_TlUpsOutletGroupRowStatus_Object = MibTableColumn
tlUpsOutletGroupRowStatus = _TlUpsOutletGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 2),
    _TlUpsOutletGroupRowStatus_Type()
)
tlUpsOutletGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletGroupRowStatus.setStatus("current")
_TlUpsOutletGroupName_Type = DisplayString
_TlUpsOutletGroupName_Object = MibTableColumn
tlUpsOutletGroupName = _TlUpsOutletGroupName_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 3),
    _TlUpsOutletGroupName_Type()
)
tlUpsOutletGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletGroupName.setStatus("current")
_TlUpsOutletGroupDesc_Type = DisplayString
_TlUpsOutletGroupDesc_Object = MibTableColumn
tlUpsOutletGroupDesc = _TlUpsOutletGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 4),
    _TlUpsOutletGroupDesc_Type()
)
tlUpsOutletGroupDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletGroupDesc.setStatus("current")


class _TlUpsOutletGroupState_Type(Integer32):
    """Custom type tlUpsOutletGroupState based on Integer32"""
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
        *(("mixed", 3),
          ("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlUpsOutletGroupState_Type.__name__ = "Integer32"
_TlUpsOutletGroupState_Object = MibTableColumn
tlUpsOutletGroupState = _TlUpsOutletGroupState_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 5),
    _TlUpsOutletGroupState_Type()
)
tlUpsOutletGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsOutletGroupState.setStatus("current")


class _TlUpsOutletGroupControl_Type(Integer32):
    """Custom type tlUpsOutletGroupControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 3),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlUpsOutletGroupControl_Type.__name__ = "Integer32"
_TlUpsOutletGroupControl_Object = MibTableColumn
tlUpsOutletGroupControl = _TlUpsOutletGroupControl_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 11, 2, 1, 6),
    _TlUpsOutletGroupControl_Type()
)
tlUpsOutletGroupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsOutletGroupControl.setStatus("current")
_TlUpsMainOutlet_ObjectIdentity = ObjectIdentity
tlUpsMainOutlet = _TlUpsMainOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 12)
)


class _TlUpsMainOutletState_Type(Integer32):
    """Custom type tlUpsMainOutletState based on Integer32"""
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
        *(("mixed", 3),
          ("off", 1),
          ("on", 2),
          ("unknown", 0))
    )


_TlUpsMainOutletState_Type.__name__ = "Integer32"
_TlUpsMainOutletState_Object = MibScalar
tlUpsMainOutletState = _TlUpsMainOutletState_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 12, 1),
    _TlUpsMainOutletState_Type()
)
tlUpsMainOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsMainOutletState.setStatus("current")
_TlUpsMainOutletControllable_Type = TruthValue
_TlUpsMainOutletControllable_Object = MibScalar
tlUpsMainOutletControllable = _TlUpsMainOutletControllable_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 12, 2),
    _TlUpsMainOutletControllable_Type()
)
tlUpsMainOutletControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsMainOutletControllable.setStatus("current")


class _TlUpsMainOutletControl_Type(Integer32):
    """Custom type tlUpsMainOutletControl based on Integer32"""
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
        *(("cycle", 3),
          ("idle", 0),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_TlUpsMainOutletControl_Type.__name__ = "Integer32"
_TlUpsMainOutletControl_Object = MibScalar
tlUpsMainOutletControl = _TlUpsMainOutletControl_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 12, 3),
    _TlUpsMainOutletControl_Type()
)
tlUpsMainOutletControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlUpsMainOutletControl.setStatus("current")
_TlUpsEnvironment_ObjectIdentity = ObjectIdentity
tlUpsEnvironment = _TlUpsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 13)
)
_TlUpsTemperature_Type = Integer32
_TlUpsTemperature_Object = MibScalar
tlUpsTemperature = _TlUpsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 850, 100, 1, 13, 1),
    _TlUpsTemperature_Type()
)
tlUpsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlUpsTemperature.setStatus("current")
_TlUpsTraps_ObjectIdentity = ObjectIdentity
tlUpsTraps = _TlUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 100, 2)
)
_TlEnviroSense_ObjectIdentity = ObjectIdentity
tlEnviroSense = _TlEnviroSense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 101)
)
_TlEnvEnvironment_ObjectIdentity = ObjectIdentity
tlEnvEnvironment = _TlEnvEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 101, 1)
)
_TlEnvTemperatureData_ObjectIdentity = ObjectIdentity
tlEnvTemperatureData = _TlEnvTemperatureData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1)
)
_TlEnvTemperatureC_Type = Integer32
_TlEnvTemperatureC_Object = MibScalar
tlEnvTemperatureC = _TlEnvTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1, 1),
    _TlEnvTemperatureC_Type()
)
tlEnvTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvTemperatureC.setStatus("current")
_TlEnvTemperatureF_Type = Integer32
_TlEnvTemperatureF_Object = MibScalar
tlEnvTemperatureF = _TlEnvTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1, 2),
    _TlEnvTemperatureF_Type()
)
tlEnvTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvTemperatureF.setStatus("current")
_TlEnvTemperatureLowLimit_Type = Integer32
_TlEnvTemperatureLowLimit_Object = MibScalar
tlEnvTemperatureLowLimit = _TlEnvTemperatureLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1, 3),
    _TlEnvTemperatureLowLimit_Type()
)
tlEnvTemperatureLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvTemperatureLowLimit.setStatus("current")
_TlEnvTemperatureHighLimit_Type = Integer32
_TlEnvTemperatureHighLimit_Object = MibScalar
tlEnvTemperatureHighLimit = _TlEnvTemperatureHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1, 4),
    _TlEnvTemperatureHighLimit_Type()
)
tlEnvTemperatureHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvTemperatureHighLimit.setStatus("current")
_TlEnvTemperatureInAlarm_Type = TruthValue
_TlEnvTemperatureInAlarm_Object = MibScalar
tlEnvTemperatureInAlarm = _TlEnvTemperatureInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 1, 5),
    _TlEnvTemperatureInAlarm_Type()
)
tlEnvTemperatureInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvTemperatureInAlarm.setStatus("current")
_TlEnvHumidityData_ObjectIdentity = ObjectIdentity
tlEnvHumidityData = _TlEnvHumidityData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 2)
)
_TlEnvHumidity_Type = Integer32
_TlEnvHumidity_Object = MibScalar
tlEnvHumidity = _TlEnvHumidity_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 2, 1),
    _TlEnvHumidity_Type()
)
tlEnvHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvHumidity.setStatus("current")
_TlEnvHumidityLowLimit_Type = Integer32
_TlEnvHumidityLowLimit_Object = MibScalar
tlEnvHumidityLowLimit = _TlEnvHumidityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 2, 2),
    _TlEnvHumidityLowLimit_Type()
)
tlEnvHumidityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvHumidityLowLimit.setStatus("current")
_TlEnvHumidityHighLimit_Type = Integer32
_TlEnvHumidityHighLimit_Object = MibScalar
tlEnvHumidityHighLimit = _TlEnvHumidityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 2, 3),
    _TlEnvHumidityHighLimit_Type()
)
tlEnvHumidityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvHumidityHighLimit.setStatus("current")
_TlEnvHumidityInAlarm_Type = TruthValue
_TlEnvHumidityInAlarm_Object = MibScalar
tlEnvHumidityInAlarm = _TlEnvHumidityInAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 1, 2, 4),
    _TlEnvHumidityInAlarm_Type()
)
tlEnvHumidityInAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvHumidityInAlarm.setStatus("current")
_TlEnvContacts_ObjectIdentity = ObjectIdentity
tlEnvContacts = _TlEnvContacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 101, 2)
)
_TlEnvContactTable_Object = MibTable
tlEnvContactTable = _TlEnvContactTable_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1)
)
if mibBuilder.loadTexts:
    tlEnvContactTable.setStatus("current")
_TlEnvContactEntry_Object = MibTableRow
tlEnvContactEntry = _TlEnvContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1, 1)
)
tlEnvContactEntry.setIndexNames(
    (0, "TRIPPLITE-12X", "tlEnvContactIndex"),
)
if mibBuilder.loadTexts:
    tlEnvContactEntry.setStatus("current")
_TlEnvContactIndex_Type = PositiveInteger
_TlEnvContactIndex_Object = MibTableColumn
tlEnvContactIndex = _TlEnvContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1, 1, 1),
    _TlEnvContactIndex_Type()
)
tlEnvContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvContactIndex.setStatus("current")
_TlEnvContactName_Type = DisplayString
_TlEnvContactName_Object = MibTableColumn
tlEnvContactName = _TlEnvContactName_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1, 1, 2),
    _TlEnvContactName_Type()
)
tlEnvContactName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvContactName.setStatus("current")


class _TlEnvContactStatus_Type(Integer32):
    """Custom type tlEnvContactStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("normal", 0))
    )


_TlEnvContactStatus_Type.__name__ = "Integer32"
_TlEnvContactStatus_Object = MibTableColumn
tlEnvContactStatus = _TlEnvContactStatus_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1, 1, 3),
    _TlEnvContactStatus_Type()
)
tlEnvContactStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlEnvContactStatus.setStatus("current")


class _TlEnvContactConfig_Type(Integer32):
    """Custom type tlEnvContactConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normallyClosed", 1),
          ("normallyOpen", 0))
    )


_TlEnvContactConfig_Type.__name__ = "Integer32"
_TlEnvContactConfig_Object = MibTableColumn
tlEnvContactConfig = _TlEnvContactConfig_Object(
    (1, 3, 6, 1, 4, 1, 850, 101, 2, 1, 1, 4),
    _TlEnvContactConfig_Type()
)
tlEnvContactConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlEnvContactConfig.setStatus("current")
_TlCooling_ObjectIdentity = ObjectIdentity
tlCooling = _TlCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103)
)
_TlCoolingEnvironment_ObjectIdentity = ObjectIdentity
tlCoolingEnvironment = _TlCoolingEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1)
)
_TlCoolingIdent_ObjectIdentity = ObjectIdentity
tlCoolingIdent = _TlCoolingIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1)
)
_TlCoolingModel_Type = DisplayString
_TlCoolingModel_Object = MibScalar
tlCoolingModel = _TlCoolingModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 1),
    _TlCoolingModel_Type()
)
tlCoolingModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingModel.setStatus("current")
_TlCoolingManufacturer_Type = DisplayString
_TlCoolingManufacturer_Object = MibScalar
tlCoolingManufacturer = _TlCoolingManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 2),
    _TlCoolingManufacturer_Type()
)
tlCoolingManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingManufacturer.setStatus("current")
_TlCoolingSerialNumber_Type = DisplayString
_TlCoolingSerialNumber_Object = MibScalar
tlCoolingSerialNumber = _TlCoolingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 3),
    _TlCoolingSerialNumber_Type()
)
tlCoolingSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingSerialNumber.setStatus("current")
_TlCoolingFirmwareVersion_Type = DisplayString
_TlCoolingFirmwareVersion_Object = MibScalar
tlCoolingFirmwareVersion = _TlCoolingFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 4),
    _TlCoolingFirmwareVersion_Type()
)
tlCoolingFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingFirmwareVersion.setStatus("current")
_TlCoolingHostSoftwareVersion_Type = DisplayString
_TlCoolingHostSoftwareVersion_Object = MibScalar
tlCoolingHostSoftwareVersion = _TlCoolingHostSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 5),
    _TlCoolingHostSoftwareVersion_Type()
)
tlCoolingHostSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingHostSoftwareVersion.setStatus("current")
_TlCoolingName_Type = DisplayString
_TlCoolingName_Object = MibScalar
tlCoolingName = _TlCoolingName_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 6),
    _TlCoolingName_Type()
)
tlCoolingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingName.setStatus("current")
_TlCoolingLocation_Type = DisplayString
_TlCoolingLocation_Object = MibScalar
tlCoolingLocation = _TlCoolingLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 1, 7),
    _TlCoolingLocation_Type()
)
tlCoolingLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingLocation.setStatus("current")
_TlCoolingStatus_ObjectIdentity = ObjectIdentity
tlCoolingStatus = _TlCoolingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2)
)
_TlCoolingCondOutletTemp_Type = Integer32
_TlCoolingCondOutletTemp_Object = MibScalar
tlCoolingCondOutletTemp = _TlCoolingCondOutletTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 1),
    _TlCoolingCondOutletTemp_Type()
)
tlCoolingCondOutletTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCondOutletTemp.setStatus("current")
_TlCoolingCondInletTemp_Type = Integer32
_TlCoolingCondInletTemp_Object = MibScalar
tlCoolingCondInletTemp = _TlCoolingCondInletTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 2),
    _TlCoolingCondInletTemp_Type()
)
tlCoolingCondInletTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCondInletTemp.setStatus("current")
_TlCoolingRefrigerantTemp_Type = Integer32
_TlCoolingRefrigerantTemp_Object = MibScalar
tlCoolingRefrigerantTemp = _TlCoolingRefrigerantTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 3),
    _TlCoolingRefrigerantTemp_Type()
)
tlCoolingRefrigerantTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingRefrigerantTemp.setStatus("current")
_TlCoolingEvapSurfaceTemp_Type = Integer32
_TlCoolingEvapSurfaceTemp_Object = MibScalar
tlCoolingEvapSurfaceTemp = _TlCoolingEvapSurfaceTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 4),
    _TlCoolingEvapSurfaceTemp_Type()
)
tlCoolingEvapSurfaceTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingEvapSurfaceTemp.setStatus("current")
_TlCoolingSuctionPressure_Type = Integer32
_TlCoolingSuctionPressure_Object = MibScalar
tlCoolingSuctionPressure = _TlCoolingSuctionPressure_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 5),
    _TlCoolingSuctionPressure_Type()
)
tlCoolingSuctionPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingSuctionPressure.setStatus("current")
_TlCoolingDischargePressure_Type = Integer32
_TlCoolingDischargePressure_Object = MibScalar
tlCoolingDischargePressure = _TlCoolingDischargePressure_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 6),
    _TlCoolingDischargePressure_Type()
)
tlCoolingDischargePressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingDischargePressure.setStatus("current")


class _TlCoolingEvapFanSpeed_Type(Integer32):
    """Custom type tlCoolingEvapFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hi", 5),
          ("low", 1),
          ("med", 3),
          ("medHi", 4),
          ("medLow", 2),
          ("off", 0))
    )


_TlCoolingEvapFanSpeed_Type.__name__ = "Integer32"
_TlCoolingEvapFanSpeed_Object = MibScalar
tlCoolingEvapFanSpeed = _TlCoolingEvapFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 7),
    _TlCoolingEvapFanSpeed_Type()
)
tlCoolingEvapFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingEvapFanSpeed.setStatus("current")


class _TlCoolingCondFanSpeed_Type(Integer32):
    """Custom type tlCoolingCondFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hi", 2),
          ("low", 1),
          ("off", 0))
    )


_TlCoolingCondFanSpeed_Type.__name__ = "Integer32"
_TlCoolingCondFanSpeed_Object = MibScalar
tlCoolingCondFanSpeed = _TlCoolingCondFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 8),
    _TlCoolingCondFanSpeed_Type()
)
tlCoolingCondFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCondFanSpeed.setStatus("current")
_TlCoolingCompFrequency_Type = Integer32
_TlCoolingCompFrequency_Object = MibScalar
tlCoolingCompFrequency = _TlCoolingCompFrequency_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 9),
    _TlCoolingCompFrequency_Type()
)
tlCoolingCompFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCompFrequency.setStatus("current")
_TlCoolingEEVPercentage_Type = Integer32
_TlCoolingEEVPercentage_Object = MibScalar
tlCoolingEEVPercentage = _TlCoolingEEVPercentage_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 10),
    _TlCoolingEEVPercentage_Type()
)
tlCoolingEEVPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingEEVPercentage.setStatus("current")
_TlCoolingUnitCurrent_Type = Integer32
_TlCoolingUnitCurrent_Object = MibScalar
tlCoolingUnitCurrent = _TlCoolingUnitCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 11),
    _TlCoolingUnitCurrent_Type()
)
tlCoolingUnitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingUnitCurrent.setStatus("current")
_TlCoolingFanCurrent_Type = Integer32
_TlCoolingFanCurrent_Object = MibScalar
tlCoolingFanCurrent = _TlCoolingFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 12),
    _TlCoolingFanCurrent_Type()
)
tlCoolingFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingFanCurrent.setStatus("current")
_TlCoolingCompCurrent_Type = Integer32
_TlCoolingCompCurrent_Object = MibScalar
tlCoolingCompCurrent = _TlCoolingCompCurrent_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 13),
    _TlCoolingCompCurrent_Type()
)
tlCoolingCompCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCompCurrent.setStatus("current")
_TlCoolingReturnAirTemp_Type = Integer32
_TlCoolingReturnAirTemp_Object = MibScalar
tlCoolingReturnAirTemp = _TlCoolingReturnAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 14),
    _TlCoolingReturnAirTemp_Type()
)
tlCoolingReturnAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingReturnAirTemp.setStatus("current")
_TlCoolingSuctionTemp_Type = Integer32
_TlCoolingSuctionTemp_Object = MibScalar
tlCoolingSuctionTemp = _TlCoolingSuctionTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 15),
    _TlCoolingSuctionTemp_Type()
)
tlCoolingSuctionTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingSuctionTemp.setStatus("current")
_TlCoolingSupplyAirTemp_Type = Integer32
_TlCoolingSupplyAirTemp_Object = MibScalar
tlCoolingSupplyAirTemp = _TlCoolingSupplyAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 2, 16),
    _TlCoolingSupplyAirTemp_Type()
)
tlCoolingSupplyAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingSupplyAirTemp.setStatus("current")
_TlCoolingRunTimes_ObjectIdentity = ObjectIdentity
tlCoolingRunTimes = _TlCoolingRunTimes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3)
)
_TlCoolingAirFilterRunHours_Type = Integer32
_TlCoolingAirFilterRunHours_Object = MibScalar
tlCoolingAirFilterRunHours = _TlCoolingAirFilterRunHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 1),
    _TlCoolingAirFilterRunHours_Type()
)
tlCoolingAirFilterRunHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingAirFilterRunHours.setStatus("current")
_TlCoolingEvapFanRunDays_Type = Integer32
_TlCoolingEvapFanRunDays_Object = MibScalar
tlCoolingEvapFanRunDays = _TlCoolingEvapFanRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 2),
    _TlCoolingEvapFanRunDays_Type()
)
tlCoolingEvapFanRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingEvapFanRunDays.setStatus("current")
_TlCoolingCondFanRunDays_Type = Integer32
_TlCoolingCondFanRunDays_Object = MibScalar
tlCoolingCondFanRunDays = _TlCoolingCondFanRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 3),
    _TlCoolingCondFanRunDays_Type()
)
tlCoolingCondFanRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCondFanRunDays.setStatus("current")
_TlCoolingCompressorRunDays_Type = Integer32
_TlCoolingCompressorRunDays_Object = MibScalar
tlCoolingCompressorRunDays = _TlCoolingCompressorRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 4),
    _TlCoolingCompressorRunDays_Type()
)
tlCoolingCompressorRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCompressorRunDays.setStatus("current")
_TlCoolingCondPumpRunDays_Type = Integer32
_TlCoolingCondPumpRunDays_Object = MibScalar
tlCoolingCondPumpRunDays = _TlCoolingCondPumpRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 5),
    _TlCoolingCondPumpRunDays_Type()
)
tlCoolingCondPumpRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingCondPumpRunDays.setStatus("current")
_TlCoolingAtomizerRunDays_Type = Integer32
_TlCoolingAtomizerRunDays_Object = MibScalar
tlCoolingAtomizerRunDays = _TlCoolingAtomizerRunDays_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 3, 6),
    _TlCoolingAtomizerRunDays_Type()
)
tlCoolingAtomizerRunDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlCoolingAtomizerRunDays.setStatus("current")
_TlCoolingConfig_ObjectIdentity = ObjectIdentity
tlCoolingConfig = _TlCoolingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4)
)


class _TlCoolingOnOff_Type(Integer32):
    """Custom type tlCoolingOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOffUnit", 0),
          ("turnOnUnit", 1))
    )


_TlCoolingOnOff_Type.__name__ = "Integer32"
_TlCoolingOnOff_Object = MibScalar
tlCoolingOnOff = _TlCoolingOnOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 1),
    _TlCoolingOnOff_Type()
)
tlCoolingOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingOnOff.setStatus("current")
_TlCoolingSetPointTemp_Type = Integer32
_TlCoolingSetPointTemp_Object = MibScalar
tlCoolingSetPointTemp = _TlCoolingSetPointTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 2),
    _TlCoolingSetPointTemp_Type()
)
tlCoolingSetPointTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingSetPointTemp.setStatus("current")


class _TlCoolingAutoStart_Type(Integer32):
    """Custom type tlCoolingAutoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlCoolingAutoStart_Type.__name__ = "Integer32"
_TlCoolingAutoStart_Object = MibScalar
tlCoolingAutoStart = _TlCoolingAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 3),
    _TlCoolingAutoStart_Type()
)
tlCoolingAutoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingAutoStart.setStatus("current")


class _TlCoolingFanSpeedOverride_Type(Integer32):
    """Custom type tlCoolingFanSpeedOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("autoFanSpeed", 0),
          ("hi", 5),
          ("low", 1),
          ("med", 3),
          ("medHi", 4),
          ("medLow", 2))
    )


_TlCoolingFanSpeedOverride_Type.__name__ = "Integer32"
_TlCoolingFanSpeedOverride_Object = MibScalar
tlCoolingFanSpeedOverride = _TlCoolingFanSpeedOverride_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 4),
    _TlCoolingFanSpeedOverride_Type()
)
tlCoolingFanSpeedOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingFanSpeedOverride.setStatus("current")


class _TlCoolingControlType_Type(Integer32):
    """Custom type tlCoolingControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remoteTemperature", 1),
          ("returnAirTemp", 0))
    )


_TlCoolingControlType_Type.__name__ = "Integer32"
_TlCoolingControlType_Object = MibScalar
tlCoolingControlType = _TlCoolingControlType_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 5),
    _TlCoolingControlType_Type()
)
tlCoolingControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingControlType.setStatus("current")
_TlCoolingCurrentRemoteTemp_Type = Integer32
_TlCoolingCurrentRemoteTemp_Object = MibScalar
tlCoolingCurrentRemoteTemp = _TlCoolingCurrentRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 6),
    _TlCoolingCurrentRemoteTemp_Type()
)
tlCoolingCurrentRemoteTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingCurrentRemoteTemp.setStatus("current")


class _TlCoolingDisplayUnits_Type(Integer32):
    """Custom type tlCoolingDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("metric", 0))
    )


_TlCoolingDisplayUnits_Type.__name__ = "Integer32"
_TlCoolingDisplayUnits_Object = MibScalar
tlCoolingDisplayUnits = _TlCoolingDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 7),
    _TlCoolingDisplayUnits_Type()
)
tlCoolingDisplayUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingDisplayUnits.setStatus("current")


class _TlCoolingBeepOnKey_Type(Integer32):
    """Custom type tlCoolingBeepOnKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("beepOn", 1),
          ("noBeep", 0))
    )


_TlCoolingBeepOnKey_Type.__name__ = "Integer32"
_TlCoolingBeepOnKey_Object = MibScalar
tlCoolingBeepOnKey = _TlCoolingBeepOnKey_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 8),
    _TlCoolingBeepOnKey_Type()
)
tlCoolingBeepOnKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingBeepOnKey.setStatus("current")


class _TlCoolingOutputRelaySource_Type(Integer32):
    """Custom type tlCoolingOutputRelaySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allAlarmsAndWarnings", 1),
          ("criticalAlarmsOnly", 2),
          ("disabled", 0))
    )


_TlCoolingOutputRelaySource_Type.__name__ = "Integer32"
_TlCoolingOutputRelaySource_Object = MibScalar
tlCoolingOutputRelaySource = _TlCoolingOutputRelaySource_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 9),
    _TlCoolingOutputRelaySource_Type()
)
tlCoolingOutputRelaySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingOutputRelaySource.setStatus("current")


class _TlCoolingOffOnLeak_Type(Integer32):
    """Custom type tlCoolingOffOnLeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 1),
          ("turnOff", 0))
    )


_TlCoolingOffOnLeak_Type.__name__ = "Integer32"
_TlCoolingOffOnLeak_Object = MibScalar
tlCoolingOffOnLeak = _TlCoolingOffOnLeak_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 10),
    _TlCoolingOffOnLeak_Type()
)
tlCoolingOffOnLeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingOffOnLeak.setStatus("current")


class _TlCoolingOffOnInputContact_Type(Integer32):
    """Custom type tlCoolingOffOnInputContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnly", 1),
          ("turnOff", 0))
    )


_TlCoolingOffOnInputContact_Type.__name__ = "Integer32"
_TlCoolingOffOnInputContact_Object = MibScalar
tlCoolingOffOnInputContact = _TlCoolingOffOnInputContact_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 11),
    _TlCoolingOffOnInputContact_Type()
)
tlCoolingOffOnInputContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingOffOnInputContact.setStatus("current")


class _TlCoolingInputContactType_Type(Integer32):
    """Custom type tlCoolingInputContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ncRelay", 0),
          ("noRelay", 1))
    )


_TlCoolingInputContactType_Type.__name__ = "Integer32"
_TlCoolingInputContactType_Object = MibScalar
tlCoolingInputContactType = _TlCoolingInputContactType_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 12),
    _TlCoolingInputContactType_Type()
)
tlCoolingInputContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingInputContactType.setStatus("current")


class _TlCoolingOutputRelayDefault_Type(Integer32):
    """Custom type tlCoolingOutputRelayDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nc", 0),
          ("no", 1))
    )


_TlCoolingOutputRelayDefault_Type.__name__ = "Integer32"
_TlCoolingOutputRelayDefault_Object = MibScalar
tlCoolingOutputRelayDefault = _TlCoolingOutputRelayDefault_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 13),
    _TlCoolingOutputRelayDefault_Type()
)
tlCoolingOutputRelayDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingOutputRelayDefault.setStatus("current")
_TlCoolingAirFilterInterval_Type = Integer32
_TlCoolingAirFilterInterval_Object = MibScalar
tlCoolingAirFilterInterval = _TlCoolingAirFilterInterval_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 14),
    _TlCoolingAirFilterInterval_Type()
)
tlCoolingAirFilterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingAirFilterInterval.setStatus("current")


class _TlCoolingWaterLeakContactType_Type(Integer32):
    """Custom type tlCoolingWaterLeakContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ncRelay", 1),
          ("noRelay", 0))
    )


_TlCoolingWaterLeakContactType_Type.__name__ = "Integer32"
_TlCoolingWaterLeakContactType_Object = MibScalar
tlCoolingWaterLeakContactType = _TlCoolingWaterLeakContactType_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 4, 15),
    _TlCoolingWaterLeakContactType_Type()
)
tlCoolingWaterLeakContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingWaterLeakContactType.setStatus("current")
_TlCoolingThresholds_ObjectIdentity = ObjectIdentity
tlCoolingThresholds = _TlCoolingThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5)
)
_TlCoolingMaxAirFilterRunHours_Type = Integer32
_TlCoolingMaxAirFilterRunHours_Object = MibScalar
tlCoolingMaxAirFilterRunHours = _TlCoolingMaxAirFilterRunHours_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 1),
    _TlCoolingMaxAirFilterRunHours_Type()
)
tlCoolingMaxAirFilterRunHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingMaxAirFilterRunHours.setStatus("current")


class _TlCoolingEnableAirFilterAlarm_Type(Integer32):
    """Custom type tlCoolingEnableAirFilterAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TlCoolingEnableAirFilterAlarm_Type.__name__ = "Integer32"
_TlCoolingEnableAirFilterAlarm_Object = MibScalar
tlCoolingEnableAirFilterAlarm = _TlCoolingEnableAirFilterAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 2),
    _TlCoolingEnableAirFilterAlarm_Type()
)
tlCoolingEnableAirFilterAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingEnableAirFilterAlarm.setStatus("current")
_TlCoolingMaxSupplyTemp_Type = Integer32
_TlCoolingMaxSupplyTemp_Object = MibScalar
tlCoolingMaxSupplyTemp = _TlCoolingMaxSupplyTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 3),
    _TlCoolingMaxSupplyTemp_Type()
)
tlCoolingMaxSupplyTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingMaxSupplyTemp.setStatus("current")
_TlCoolingMinSupplyTemp_Type = Integer32
_TlCoolingMinSupplyTemp_Object = MibScalar
tlCoolingMinSupplyTemp = _TlCoolingMinSupplyTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 4),
    _TlCoolingMinSupplyTemp_Type()
)
tlCoolingMinSupplyTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingMinSupplyTemp.setStatus("current")
_TlCoolingTempDiffAlarm_Type = Integer32
_TlCoolingTempDiffAlarm_Object = MibScalar
tlCoolingTempDiffAlarm = _TlCoolingTempDiffAlarm_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 5),
    _TlCoolingTempDiffAlarm_Type()
)
tlCoolingTempDiffAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingTempDiffAlarm.setStatus("current")
_TlCoolingMaxReturnAirTemp_Type = Integer32
_TlCoolingMaxReturnAirTemp_Object = MibScalar
tlCoolingMaxReturnAirTemp = _TlCoolingMaxReturnAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 103, 1, 5, 6),
    _TlCoolingMaxReturnAirTemp_Type()
)
tlCoolingMaxReturnAirTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlCoolingMaxReturnAirTemp.setStatus("current")
_TlCoolingAlarm_ObjectIdentity = ObjectIdentity
tlCoolingAlarm = _TlCoolingAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6)
)
_TlCoolingWellKnownAlarms_ObjectIdentity = ObjectIdentity
tlCoolingWellKnownAlarms = _TlCoolingWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3)
)
_TlCoolingSupplyAirSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingSupplyAirSensorFault = _TlCoolingSupplyAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tlCoolingSupplyAirSensorFault.setStatus("current")
_TlCoolingReturnAirSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingReturnAirSensorFault = _TlCoolingReturnAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 2)
)
if mibBuilder.loadTexts:
    tlCoolingReturnAirSensorFault.setStatus("current")
_TlCoolingCondenserInletAirSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingCondenserInletAirSensorFault = _TlCoolingCondenserInletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 3)
)
if mibBuilder.loadTexts:
    tlCoolingCondenserInletAirSensorFault.setStatus("current")
_TlCoolingCondenserOutletAirSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingCondenserOutletAirSensorFault = _TlCoolingCondenserOutletAirSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 4)
)
if mibBuilder.loadTexts:
    tlCoolingCondenserOutletAirSensorFault.setStatus("current")
_TlCoolingSuctionTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingSuctionTemperatureSensorFault = _TlCoolingSuctionTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 5)
)
if mibBuilder.loadTexts:
    tlCoolingSuctionTemperatureSensorFault.setStatus("current")
_TlCoolingEvaporatorTemperatureSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingEvaporatorTemperatureSensorFault = _TlCoolingEvaporatorTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 6)
)
if mibBuilder.loadTexts:
    tlCoolingEvaporatorTemperatureSensorFault.setStatus("current")
_TlCoolingAirFilterClogged_ObjectIdentity = ObjectIdentity
tlCoolingAirFilterClogged = _TlCoolingAirFilterClogged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 7)
)
if mibBuilder.loadTexts:
    tlCoolingAirFilterClogged.setStatus("current")
_TlCoolingAirFilterRunHoursViolation_ObjectIdentity = ObjectIdentity
tlCoolingAirFilterRunHoursViolation = _TlCoolingAirFilterRunHoursViolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 8)
)
if mibBuilder.loadTexts:
    tlCoolingAirFilterRunHoursViolation.setStatus("current")
_TlCoolingSuctionPressureSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingSuctionPressureSensorFault = _TlCoolingSuctionPressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 9)
)
if mibBuilder.loadTexts:
    tlCoolingSuctionPressureSensorFault.setStatus("current")
_TlCoolingInverterCommunicationsFault_ObjectIdentity = ObjectIdentity
tlCoolingInverterCommunicationsFault = _TlCoolingInverterCommunicationsFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 10)
)
if mibBuilder.loadTexts:
    tlCoolingInverterCommunicationsFault.setStatus("current")
_TlCoolingRemoteShutdownViaInputContact_ObjectIdentity = ObjectIdentity
tlCoolingRemoteShutdownViaInputContact = _TlCoolingRemoteShutdownViaInputContact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 11)
)
if mibBuilder.loadTexts:
    tlCoolingRemoteShutdownViaInputContact.setStatus("current")
_TlCoolingCondensatePumpFault_ObjectIdentity = ObjectIdentity
tlCoolingCondensatePumpFault = _TlCoolingCondensatePumpFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 12)
)
if mibBuilder.loadTexts:
    tlCoolingCondensatePumpFault.setStatus("current")
_TlCoolingLowRefrigerantStartupFault_ObjectIdentity = ObjectIdentity
tlCoolingLowRefrigerantStartupFault = _TlCoolingLowRefrigerantStartupFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 13)
)
if mibBuilder.loadTexts:
    tlCoolingLowRefrigerantStartupFault.setStatus("current")
_TlCoolingCondenserFanFault_ObjectIdentity = ObjectIdentity
tlCoolingCondenserFanFault = _TlCoolingCondenserFanFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 14)
)
if mibBuilder.loadTexts:
    tlCoolingCondenserFanFault.setStatus("current")
_TlCoolingCondenserFailure_ObjectIdentity = ObjectIdentity
tlCoolingCondenserFailure = _TlCoolingCondenserFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 15)
)
if mibBuilder.loadTexts:
    tlCoolingCondenserFailure.setStatus("current")
_TlCoolingEvaporatorCoolingFailure_ObjectIdentity = ObjectIdentity
tlCoolingEvaporatorCoolingFailure = _TlCoolingEvaporatorCoolingFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 16)
)
if mibBuilder.loadTexts:
    tlCoolingEvaporatorCoolingFailure.setStatus("current")
_TlCoolingReturnAirTempHigh_ObjectIdentity = ObjectIdentity
tlCoolingReturnAirTempHigh = _TlCoolingReturnAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 17)
)
if mibBuilder.loadTexts:
    tlCoolingReturnAirTempHigh.setStatus("current")
_TlCoolingSupplyAirTempHigh_ObjectIdentity = ObjectIdentity
tlCoolingSupplyAirTempHigh = _TlCoolingSupplyAirTempHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 18)
)
if mibBuilder.loadTexts:
    tlCoolingSupplyAirTempHigh.setStatus("current")
_TlCoolingEvaporatorFailure_ObjectIdentity = ObjectIdentity
tlCoolingEvaporatorFailure = _TlCoolingEvaporatorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 19)
)
if mibBuilder.loadTexts:
    tlCoolingEvaporatorFailure.setStatus("current")
_TlCoolingEvaporatorFreezeUp_ObjectIdentity = ObjectIdentity
tlCoolingEvaporatorFreezeUp = _TlCoolingEvaporatorFreezeUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 20)
)
if mibBuilder.loadTexts:
    tlCoolingEvaporatorFreezeUp.setStatus("current")
_TlCoolingDischargePressureHigh_ObjectIdentity = ObjectIdentity
tlCoolingDischargePressureHigh = _TlCoolingDischargePressureHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 21)
)
if mibBuilder.loadTexts:
    tlCoolingDischargePressureHigh.setStatus("current")
_TlCoolingPressureGaugeFailure_ObjectIdentity = ObjectIdentity
tlCoolingPressureGaugeFailure = _TlCoolingPressureGaugeFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 22)
)
if mibBuilder.loadTexts:
    tlCoolingPressureGaugeFailure.setStatus("current")
_TlCoolingDischargePressurePersistentHigh_ObjectIdentity = ObjectIdentity
tlCoolingDischargePressurePersistentHigh = _TlCoolingDischargePressurePersistentHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 23)
)
if mibBuilder.loadTexts:
    tlCoolingDischargePressurePersistentHigh.setStatus("current")
_TlCoolingSuctionPressureLowStartFailure_ObjectIdentity = ObjectIdentity
tlCoolingSuctionPressureLowStartFailure = _TlCoolingSuctionPressureLowStartFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 24)
)
if mibBuilder.loadTexts:
    tlCoolingSuctionPressureLowStartFailure.setStatus("current")
_TlCoolingSuctionPressureLow_ObjectIdentity = ObjectIdentity
tlCoolingSuctionPressureLow = _TlCoolingSuctionPressureLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 25)
)
if mibBuilder.loadTexts:
    tlCoolingSuctionPressureLow.setStatus("current")
_TlCoolingSuctionPressurePersistentLow_ObjectIdentity = ObjectIdentity
tlCoolingSuctionPressurePersistentLow = _TlCoolingSuctionPressurePersistentLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 26)
)
if mibBuilder.loadTexts:
    tlCoolingSuctionPressurePersistentLow.setStatus("current")
_TlCoolingStartupLinePressureImbalance_ObjectIdentity = ObjectIdentity
tlCoolingStartupLinePressureImbalance = _TlCoolingStartupLinePressureImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 27)
)
if mibBuilder.loadTexts:
    tlCoolingStartupLinePressureImbalance.setStatus("current")
_TlCoolingCompressorFailure_ObjectIdentity = ObjectIdentity
tlCoolingCompressorFailure = _TlCoolingCompressorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 28)
)
if mibBuilder.loadTexts:
    tlCoolingCompressorFailure.setStatus("current")
_TlCoolingCurrentLimit_ObjectIdentity = ObjectIdentity
tlCoolingCurrentLimit = _TlCoolingCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 29)
)
if mibBuilder.loadTexts:
    tlCoolingCurrentLimit.setStatus("current")
_TlCoolingWaterLeak_ObjectIdentity = ObjectIdentity
tlCoolingWaterLeak = _TlCoolingWaterLeak_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 30)
)
if mibBuilder.loadTexts:
    tlCoolingWaterLeak.setStatus("current")
_TlCoolingFanUnderCurrent_ObjectIdentity = ObjectIdentity
tlCoolingFanUnderCurrent = _TlCoolingFanUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 31)
)
if mibBuilder.loadTexts:
    tlCoolingFanUnderCurrent.setStatus("current")
_TlCoolingFanOverCurrent_ObjectIdentity = ObjectIdentity
tlCoolingFanOverCurrent = _TlCoolingFanOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 32)
)
if mibBuilder.loadTexts:
    tlCoolingFanOverCurrent.setStatus("current")
_TlCoolingDischargePressureSensorFault_ObjectIdentity = ObjectIdentity
tlCoolingDischargePressureSensorFault = _TlCoolingDischargePressureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 33)
)
if mibBuilder.loadTexts:
    tlCoolingDischargePressureSensorFault.setStatus("current")
_TlCoolingWaterFull_ObjectIdentity = ObjectIdentity
tlCoolingWaterFull = _TlCoolingWaterFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 34)
)
if mibBuilder.loadTexts:
    tlCoolingWaterFull.setStatus("current")
_TlCoolingAutoCoolingOn_ObjectIdentity = ObjectIdentity
tlCoolingAutoCoolingOn = _TlCoolingAutoCoolingOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 35)
)
if mibBuilder.loadTexts:
    tlCoolingAutoCoolingOn.setStatus("current")
_TlCoolingPowerButtonPressed_ObjectIdentity = ObjectIdentity
tlCoolingPowerButtonPressed = _TlCoolingPowerButtonPressed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 36)
)
if mibBuilder.loadTexts:
    tlCoolingPowerButtonPressed.setStatus("current")
_TlCoolingDisconnectedFromDevice_ObjectIdentity = ObjectIdentity
tlCoolingDisconnectedFromDevice = _TlCoolingDisconnectedFromDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 103, 6, 3, 37)
)
if mibBuilder.loadTexts:
    tlCoolingDisconnectedFromDevice.setStatus("current")
_TlSrCoolNet_ObjectIdentity = ObjectIdentity
tlSrCoolNet = _TlSrCoolNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104)
)
_TlSrCoolNetData_ObjectIdentity = ObjectIdentity
tlSrCoolNetData = _TlSrCoolNetData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 1)
)
_TlSrCoolNetIdent_ObjectIdentity = ObjectIdentity
tlSrCoolNetIdent = _TlSrCoolNetIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1)
)
_TlSrCoolNetModel_Type = DisplayString
_TlSrCoolNetModel_Object = MibScalar
tlSrCoolNetModel = _TlSrCoolNetModel_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 1),
    _TlSrCoolNetModel_Type()
)
tlSrCoolNetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetModel.setStatus("current")
_TlSrCoolNetManufacturer_Type = DisplayString
_TlSrCoolNetManufacturer_Object = MibScalar
tlSrCoolNetManufacturer = _TlSrCoolNetManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 2),
    _TlSrCoolNetManufacturer_Type()
)
tlSrCoolNetManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetManufacturer.setStatus("current")
_TlSrCoolNetSerialNumber_Type = DisplayString
_TlSrCoolNetSerialNumber_Object = MibScalar
tlSrCoolNetSerialNumber = _TlSrCoolNetSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 3),
    _TlSrCoolNetSerialNumber_Type()
)
tlSrCoolNetSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetSerialNumber.setStatus("current")
_TlSrCoolNetHostSoftwareVersion_Type = DisplayString
_TlSrCoolNetHostSoftwareVersion_Object = MibScalar
tlSrCoolNetHostSoftwareVersion = _TlSrCoolNetHostSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 4),
    _TlSrCoolNetHostSoftwareVersion_Type()
)
tlSrCoolNetHostSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetHostSoftwareVersion.setStatus("current")
_TlSrCoolNetName_Type = DisplayString
_TlSrCoolNetName_Object = MibScalar
tlSrCoolNetName = _TlSrCoolNetName_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 5),
    _TlSrCoolNetName_Type()
)
tlSrCoolNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetName.setStatus("current")
_TlSrCoolNetLocation_Type = DisplayString
_TlSrCoolNetLocation_Object = MibScalar
tlSrCoolNetLocation = _TlSrCoolNetLocation_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 1, 6),
    _TlSrCoolNetLocation_Type()
)
tlSrCoolNetLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetLocation.setStatus("current")
_TlSrCoolNetStatus_ObjectIdentity = ObjectIdentity
tlSrCoolNetStatus = _TlSrCoolNetStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2)
)


class _TlSrCoolNetMode_Type(Integer32):
    """Custom type tlSrCoolNetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cooling", 2),
          ("defrost", 5),
          ("dehumidifying", 4),
          ("idle", 1),
          ("notconnected", 6),
          ("off", 0),
          ("unknown", 3))
    )


_TlSrCoolNetMode_Type.__name__ = "Integer32"
_TlSrCoolNetMode_Object = MibScalar
tlSrCoolNetMode = _TlSrCoolNetMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 1),
    _TlSrCoolNetMode_Type()
)
tlSrCoolNetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetMode.setStatus("current")


class _TlSrCoolNetFanSpeed_Type(Integer32):
    """Custom type tlSrCoolNetFanSpeed based on Integer32"""
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
        *(("hi", 3),
          ("low", 1),
          ("med", 2),
          ("off", 0))
    )


_TlSrCoolNetFanSpeed_Type.__name__ = "Integer32"
_TlSrCoolNetFanSpeed_Object = MibScalar
tlSrCoolNetFanSpeed = _TlSrCoolNetFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 2),
    _TlSrCoolNetFanSpeed_Type()
)
tlSrCoolNetFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetFanSpeed.setStatus("current")
_TlSrCoolNetReturnAirTemp_Type = Integer32
_TlSrCoolNetReturnAirTemp_Object = MibScalar
tlSrCoolNetReturnAirTemp = _TlSrCoolNetReturnAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 3),
    _TlSrCoolNetReturnAirTemp_Type()
)
tlSrCoolNetReturnAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetReturnAirTemp.setStatus("current")


class _TlSrCoolNetWaterFull_Type(Integer32):
    """Custom type tlSrCoolNetWaterFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("waterFull", 1),
          ("waterNotFull", 0))
    )


_TlSrCoolNetWaterFull_Type.__name__ = "Integer32"
_TlSrCoolNetWaterFull_Object = MibScalar
tlSrCoolNetWaterFull = _TlSrCoolNetWaterFull_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 4),
    _TlSrCoolNetWaterFull_Type()
)
tlSrCoolNetWaterFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetWaterFull.setStatus("current")
_TlSrCoolNetCurrentRemoteTemp_Type = Integer32
_TlSrCoolNetCurrentRemoteTemp_Object = MibScalar
tlSrCoolNetCurrentRemoteTemp = _TlSrCoolNetCurrentRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 5),
    _TlSrCoolNetCurrentRemoteTemp_Type()
)
tlSrCoolNetCurrentRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetCurrentRemoteTemp.setStatus("current")


class _TlSrCoolNetDisplayUnits_Type(Integer32):
    """Custom type tlSrCoolNetDisplayUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("metric", 0))
    )


_TlSrCoolNetDisplayUnits_Type.__name__ = "Integer32"
_TlSrCoolNetDisplayUnits_Object = MibScalar
tlSrCoolNetDisplayUnits = _TlSrCoolNetDisplayUnits_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 2, 6),
    _TlSrCoolNetDisplayUnits_Type()
)
tlSrCoolNetDisplayUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlSrCoolNetDisplayUnits.setStatus("current")
_TlSrCoolNetConfig_ObjectIdentity = ObjectIdentity
tlSrCoolNetConfig = _TlSrCoolNetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3)
)


class _TlSrCoolNetOnOff_Type(Integer32):
    """Custom type tlSrCoolNetOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("turnOffUnit", 0),
          ("turnOnUnit", 1))
    )


_TlSrCoolNetOnOff_Type.__name__ = "Integer32"
_TlSrCoolNetOnOff_Object = MibScalar
tlSrCoolNetOnOff = _TlSrCoolNetOnOff_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 1),
    _TlSrCoolNetOnOff_Type()
)
tlSrCoolNetOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetOnOff.setStatus("current")


class _TlSrCoolSetMode_Type(Integer32):
    """Custom type tlSrCoolSetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cooling", 0),
          ("dehumidifying", 1))
    )


_TlSrCoolSetMode_Type.__name__ = "Integer32"
_TlSrCoolSetMode_Object = MibScalar
tlSrCoolSetMode = _TlSrCoolSetMode_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 2),
    _TlSrCoolSetMode_Type()
)
tlSrCoolSetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolSetMode.setStatus("current")
_TlSrCoolNetSetPointTemp_Type = Integer32
_TlSrCoolNetSetPointTemp_Object = MibScalar
tlSrCoolNetSetPointTemp = _TlSrCoolNetSetPointTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 3),
    _TlSrCoolNetSetPointTemp_Type()
)
tlSrCoolNetSetPointTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetSetPointTemp.setStatus("current")
_TlSrCoolNetRemoteSetPointTemp_Type = Integer32
_TlSrCoolNetRemoteSetPointTemp_Object = MibScalar
tlSrCoolNetRemoteSetPointTemp = _TlSrCoolNetRemoteSetPointTemp_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 4),
    _TlSrCoolNetRemoteSetPointTemp_Type()
)
tlSrCoolNetRemoteSetPointTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetRemoteSetPointTemp.setStatus("current")


class _TlSrCoolNetFanSpeedSetting_Type(Integer32):
    """Custom type tlSrCoolNetFanSpeedSetting based on Integer32"""
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
        *(("auto", 0),
          ("high", 3),
          ("low", 1),
          ("med", 2))
    )


_TlSrCoolNetFanSpeedSetting_Type.__name__ = "Integer32"
_TlSrCoolNetFanSpeedSetting_Object = MibScalar
tlSrCoolNetFanSpeedSetting = _TlSrCoolNetFanSpeedSetting_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 5),
    _TlSrCoolNetFanSpeedSetting_Type()
)
tlSrCoolNetFanSpeedSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetFanSpeedSetting.setStatus("current")


class _TlSrCoolNetRemoteSetpointEnable_Type(Integer32):
    """Custom type tlSrCoolNetRemoteSetpointEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TlSrCoolNetRemoteSetpointEnable_Type.__name__ = "Integer32"
_TlSrCoolNetRemoteSetpointEnable_Object = MibScalar
tlSrCoolNetRemoteSetpointEnable = _TlSrCoolNetRemoteSetpointEnable_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 6),
    _TlSrCoolNetRemoteSetpointEnable_Type()
)
tlSrCoolNetRemoteSetpointEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetRemoteSetpointEnable.setStatus("current")


class _TlSrCoolNetFanAlwaysOn_Type(Integer32):
    """Custom type tlSrCoolNetFanAlwaysOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TlSrCoolNetFanAlwaysOn_Type.__name__ = "Integer32"
_TlSrCoolNetFanAlwaysOn_Object = MibScalar
tlSrCoolNetFanAlwaysOn = _TlSrCoolNetFanAlwaysOn_Object(
    (1, 3, 6, 1, 4, 1, 850, 104, 1, 3, 7),
    _TlSrCoolNetFanAlwaysOn_Type()
)
tlSrCoolNetFanAlwaysOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlSrCoolNetFanAlwaysOn.setStatus("current")
_TlSrCoolNetAlarm_ObjectIdentity = ObjectIdentity
tlSrCoolNetAlarm = _TlSrCoolNetAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 2)
)
_TlSrCoolNetWellKnownAlarms_ObjectIdentity = ObjectIdentity
tlSrCoolNetWellKnownAlarms = _TlSrCoolNetWellKnownAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 2, 1)
)
_TlSrCoolNetWaterFullAlarm_ObjectIdentity = ObjectIdentity
tlSrCoolNetWaterFullAlarm = _TlSrCoolNetWaterFullAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 850, 104, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tlSrCoolNetWaterFullAlarm.setStatus("current")

# Managed Objects groups

tlUpsFullIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 1)
)
tlUpsFullIdentGroup.setObjects(
      *(("TRIPPLITE-12X", "tlUpsIdentUpsSoftwareChecksum"),
        ("TRIPPLITE-12X", "tlUpsIdentSerialNum"),
        ("TRIPPLITE-12X", "tlUpsIdentID"),
        ("TRIPPLITE-12X", "tlUpsSelectedDeviceID"))
)
if mibBuilder.loadTexts:
    tlUpsFullIdentGroup.setStatus("current")

tlUpsFullBatteryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 2)
)
tlUpsFullBatteryGroup.setObjects(
      *(("TRIPPLITE-12X", "tlUpsBatteryAge"),
        ("TRIPPLITE-12X", "tlUpsTemperatureF"))
)
if mibBuilder.loadTexts:
    tlUpsFullBatteryGroup.setStatus("current")

tlUpsFullAlarmObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 6, 1)
)
tlUpsFullAlarmObjsGroup.setObjects(
      *(("TRIPPLITE-12X", "tlUpsAlarmDevName"),
        ("TRIPPLITE-12X", "tlUpsAlarmDevLocation"),
        ("TRIPPLITE-12X", "tlUpsAlarmCategory"))
)
if mibBuilder.loadTexts:
    tlUpsFullAlarmObjsGroup.setStatus("current")

tlUpsFullTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 7)
)
tlUpsFullTestGroup.setObjects(
      *(("TRIPPLITE-12X", "tlUpsTestDate"),
        ("TRIPPLITE-12X", "tlUpsTestResultsDetail"))
)
if mibBuilder.loadTexts:
    tlUpsFullTestGroup.setStatus("current")

tlUpsFullControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 8)
)
tlUpsFullControlGroup.setObjects(
      *(("TRIPPLITE-12X", "tlUpsWatchdogSupported"),
        ("TRIPPLITE-12X", "tlUpsWatchdogSecsBeforeReboot"))
)
if mibBuilder.loadTexts:
    tlUpsFullControlGroup.setStatus("current")

tlUpsFullConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 9)
)
tlUpsFullConfigGroup.setObjects(
    ("TRIPPLITE-12X", "tlUpsConfigBattReplDate")
)
if mibBuilder.loadTexts:
    tlUpsFullConfigGroup.setStatus("current")

tlUpsFullOutletGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 850, 20, 2, 3, 100, 10)
)
tlUpsFullOutletGroup.setObjects(
    ("TRIPPLITE-12X", "tlUpsOutletNumOutlets")
)
if mibBuilder.loadTexts:
    tlUpsFullOutletGroup.setStatus("current")


# Notification objects

tlUpsTrapAlarmEntryAddedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 0, 3)
)
tlUpsTrapAlarmEntryAddedV1.setObjects(
      *(("TRIPPLITE-12X", "tlUpsAlarmId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDescr"),
        ("TRIPPLITE-12X", "tlUpsAlarmDetail"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceName"),
        ("TRIPPLITE-12X", "tlUpsAlarmLocation"),
        ("TRIPPLITE-12X", "tlUpsAlarmGroup"))
)
if mibBuilder.loadTexts:
    tlUpsTrapAlarmEntryAddedV1.setStatus(
        ""
    )

tlUpsTrapAlarmEntryRemovedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 0, 4)
)
tlUpsTrapAlarmEntryRemovedV1.setObjects(
      *(("TRIPPLITE-12X", "tlUpsAlarmId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDescr"),
        ("TRIPPLITE-12X", "tlUpsAlarmDetail"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceName"),
        ("TRIPPLITE-12X", "tlUpsAlarmLocation"),
        ("TRIPPLITE-12X", "tlUpsAlarmGroup"))
)
if mibBuilder.loadTexts:
    tlUpsTrapAlarmEntryRemovedV1.setStatus(
        ""
    )

tlUpsTrapAlarmEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 3)
)
tlUpsTrapAlarmEntryAdded.setObjects(
      *(("TRIPPLITE-12X", "tlUpsAlarmId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDescr"),
        ("TRIPPLITE-12X", "tlUpsAlarmDetail"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceName"),
        ("TRIPPLITE-12X", "tlUpsAlarmLocation"),
        ("TRIPPLITE-12X", "tlUpsAlarmGroup"))
)
if mibBuilder.loadTexts:
    tlUpsTrapAlarmEntryAdded.setStatus(
        "current"
    )

tlUpsTrapAlarmEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 4)
)
tlUpsTrapAlarmEntryRemoved.setObjects(
      *(("TRIPPLITE-12X", "tlUpsAlarmId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDescr"),
        ("TRIPPLITE-12X", "tlUpsAlarmDetail"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceId"),
        ("TRIPPLITE-12X", "tlUpsAlarmDeviceName"),
        ("TRIPPLITE-12X", "tlUpsAlarmLocation"),
        ("TRIPPLITE-12X", "tlUpsAlarmGroup"))
)
if mibBuilder.loadTexts:
    tlUpsTrapAlarmEntryRemoved.setStatus(
        "current"
    )

tlUpsTrapSystemStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 5)
)
if mibBuilder.loadTexts:
    tlUpsTrapSystemStartup.setStatus(
        "current"
    )

tlUpsTrapSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 850, 100, 2, 6)
)
if mibBuilder.loadTexts:
    tlUpsTrapSystemShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIPPLITE-12X",
    **{"tlEnumerations": tlEnumerations,
       "tlOperatingSystems": tlOperatingSystems,
       "hpux9": hpux9,
       "sunos4": sunos4,
       "solaris": solaris,
       "osf": osf,
       "ultrix": ultrix,
       "hpux10": hpux10,
       "netbsd1": netbsd1,
       "freebsd": freebsd,
       "irix": irix,
       "linux": linux,
       "bsdi": bsdi,
       "openbsd": openbsd,
       "win32": win32,
       "hpux11": hpux11,
       "win9x": win9x,
       "winnt": winnt,
       "solspark": solspark,
       "solintel": solintel,
       "aix": aix,
       "sco": sco,
       "osx": osx,
       "unknown": unknown,
       "tlConformance": tlConformance,
       "tlCompliances": tlCompliances,
       "tlGroups": tlGroups,
       "tlSubsetGroups": tlSubsetGroups,
       "tlBasicGroups": tlBasicGroups,
       "tlFullGroups": tlFullGroups,
       "tlUpsFullGroups": tlUpsFullGroups,
       "tlUpsFullIdentGroup": tlUpsFullIdentGroup,
       "tlUpsFullBatteryGroup": tlUpsFullBatteryGroup,
       "tlUpsFullAlarmGroup": tlUpsFullAlarmGroup,
       "tlUpsFullAlarmObjsGroup": tlUpsFullAlarmObjsGroup,
       "tlUpsFullTestGroup": tlUpsFullTestGroup,
       "tlUpsFullControlGroup": tlUpsFullControlGroup,
       "tlUpsFullConfigGroup": tlUpsFullConfigGroup,
       "tlUpsFullOutletGroup": tlUpsFullOutletGroup,
       "tlPowerAlert": tlPowerAlert,
       "tlPASystem": tlPASystem,
       "tlPAContacts": tlPAContacts,
       "tlPAEmailContacts": tlPAEmailContacts,
       "tlPANumberOfEmailContacts": tlPANumberOfEmailContacts,
       "tlPAEmailContactsTable": tlPAEmailContactsTable,
       "tlPAEmailContactEntry": tlPAEmailContactEntry,
       "tlPAEmailContactIndex": tlPAEmailContactIndex,
       "tlPAEmailContactRowStatus": tlPAEmailContactRowStatus,
       "tlPAEmailContactName": tlPAEmailContactName,
       "tlPAEmailContactAddress": tlPAEmailContactAddress,
       "tlPASnmpContacts": tlPASnmpContacts,
       "tlPANumberOfSnmpContacts": tlPANumberOfSnmpContacts,
       "tlPASnmpContactsTable": tlPASnmpContactsTable,
       "tlPASnmpContactEntry": tlPASnmpContactEntry,
       "tlPASnmpContactIndex": tlPASnmpContactIndex,
       "tlPASnmpContactRowStatus": tlPASnmpContactRowStatus,
       "tlPASnmpContactName": tlPASnmpContactName,
       "tlPASnmpContactIpAddress": tlPASnmpContactIpAddress,
       "tlPASnmpContactPort": tlPASnmpContactPort,
       "tlPASnmpContactSnmpVersion": tlPASnmpContactSnmpVersion,
       "tlPASnmpContactSecurityName": tlPASnmpContactSecurityName,
       "tlPASnmpContactPrivPassword": tlPASnmpContactPrivPassword,
       "tlPASnmpContactAuthPassword": tlPASnmpContactAuthPassword,
       "tlUPS": tlUPS,
       "tlUpsObjects": tlUpsObjects,
       "tlUpsIdent": tlUpsIdent,
       "tlUpsIdentUpsSoftwareChecksum": tlUpsIdentUpsSoftwareChecksum,
       "tlUpsIdentSerialNum": tlUpsIdentSerialNum,
       "tlUpsIdentID": tlUpsIdentID,
       "tlUpsSnmpCardSerialNum": tlUpsSnmpCardSerialNum,
       "tlUpsSelectedDeviceID": tlUpsSelectedDeviceID,
       "tlUpsLocation": tlUpsLocation,
       "tlUpsBattery": tlUpsBattery,
       "tlUpsBatteryAge": tlUpsBatteryAge,
       "tlUpsTemperatureF": tlUpsTemperatureF,
       "tlUpsExternalBatteryAge": tlUpsExternalBatteryAge,
       "tlUpsInput": tlUpsInput,
       "tlUpsInputNumVoltages": tlUpsInputNumVoltages,
       "tlUpsInputVoltageTable": tlUpsInputVoltageTable,
       "tlUpsInputVoltageEntry": tlUpsInputVoltageEntry,
       "tlUpsInputVoltageIndex": tlUpsInputVoltageIndex,
       "tlUpsInputVoltageType": tlUpsInputVoltageType,
       "tlUpsInputVoltage": tlUpsInputVoltage,
       "tlUpsInputSourceSelect": tlUpsInputSourceSelect,
       "tlUpsPhaseImbalance": tlUpsPhaseImbalance,
       "tlUpsInputSourceAvailability": tlUpsInputSourceAvailability,
       "tlUpsInputSourceInUse": tlUpsInputSourceInUse,
       "tlUpsInputSourceTransitionCount": tlUpsInputSourceTransitionCount,
       "tlUpsOutput": tlUpsOutput,
       "tlUpsOutputPowerTotal": tlUpsOutputPowerTotal,
       "tlUpsOutputCircuits": tlUpsOutputCircuits,
       "tlUpsOutputCircuitTable": tlUpsOutputCircuitTable,
       "tlUpsOutputCircuitEntry": tlUpsOutputCircuitEntry,
       "tlUpsOutputCircuitIndex": tlUpsOutputCircuitIndex,
       "tlUpsOutputCircuitStatus": tlUpsOutputCircuitStatus,
       "tlUpsOutputCircuitLoadCurrent": tlUpsOutputCircuitLoadCurrent,
       "tlUpsOutputCircuitVoltage": tlUpsOutputCircuitVoltage,
       "tlUpsOutputCircuitPower": tlUpsOutputCircuitPower,
       "tlUpsOutputCircuitPowerFactor": tlUpsOutputCircuitPowerFactor,
       "tlUpsAggregatePowerFactor": tlUpsAggregatePowerFactor,
       "tlUpsAlarm": tlUpsAlarm,
       "tlUpsAlarmsPresent": tlUpsAlarmsPresent,
       "tlUpsAlarmTable": tlUpsAlarmTable,
       "tlUpsAlarmEntry": tlUpsAlarmEntry,
       "tlUpsAlarmId": tlUpsAlarmId,
       "tlUpsAlarmDescr": tlUpsAlarmDescr,
       "tlUpsAlarmTime": tlUpsAlarmTime,
       "tlUpsAlarmDetail": tlUpsAlarmDetail,
       "tlUpsAlarmDeviceId": tlUpsAlarmDeviceId,
       "tlUpsAlarmDeviceName": tlUpsAlarmDeviceName,
       "tlUpsAlarmLocation": tlUpsAlarmLocation,
       "tlUpsAlarmGroup": tlUpsAlarmGroup,
       "tlUpsAlarmIp": tlUpsAlarmIp,
       "tlUpsAlarmMac": tlUpsAlarmMac,
       "tlUpsWellKnownAlarms": tlUpsWellKnownAlarms,
       "tlUpsAlarmPrimaryPowerOutage": tlUpsAlarmPrimaryPowerOutage,
       "tlUpsAlarmSecondaryPowerOutage": tlUpsAlarmSecondaryPowerOutage,
       "tlUpsAlarmLoadLevelAboveThreshold": tlUpsAlarmLoadLevelAboveThreshold,
       "tlUpsAlarmOutputCurrentChanged": tlUpsAlarmOutputCurrentChanged,
       "tlUpsAlarmBatteryAgeAboveThreshold": tlUpsAlarmBatteryAgeAboveThreshold,
       "tlUpsAlarmLoadOff": tlUpsAlarmLoadOff,
       "tlUpsAlarmUserDefined": tlUpsAlarmUserDefined,
       "tlUpsAlarmBatteryBad": tlUpsAlarmBatteryBad,
       "tlUpsAlarmOnBattery": tlUpsAlarmOnBattery,
       "tlUpsAlarmLowBattery": tlUpsAlarmLowBattery,
       "tlUpsAlarmDepletedBattery": tlUpsAlarmDepletedBattery,
       "tlUpsAlarmTempBad": tlUpsAlarmTempBad,
       "tlUpsAlarmInputBad": tlUpsAlarmInputBad,
       "tlUpsAlarmOutputBad": tlUpsAlarmOutputBad,
       "tlUpsAlarmOutputOverload": tlUpsAlarmOutputOverload,
       "tlUpsAlarmOnBypass": tlUpsAlarmOnBypass,
       "tlUpsAlarmBypassBad": tlUpsAlarmBypassBad,
       "tlUpsAlarmOutputOffAsRequested": tlUpsAlarmOutputOffAsRequested,
       "tlUpsAlarmUpsOffAsRequested": tlUpsAlarmUpsOffAsRequested,
       "tlUpsAlarmChargerFailed": tlUpsAlarmChargerFailed,
       "tlUpsAlarmUpsOutputOff": tlUpsAlarmUpsOutputOff,
       "tlUpsAlarmUpsSystemOff": tlUpsAlarmUpsSystemOff,
       "tlUpsAlarmFanFailure": tlUpsAlarmFanFailure,
       "tlUpsAlarmFuseFailure": tlUpsAlarmFuseFailure,
       "tlUpsAlarmGeneralFault": tlUpsAlarmGeneralFault,
       "tlUpsAlarmDiagnosticTestFailed": tlUpsAlarmDiagnosticTestFailed,
       "tlUpsAlarmCommunicationsLost": tlUpsAlarmCommunicationsLost,
       "tlUpsAlarmAwaitingPower": tlUpsAlarmAwaitingPower,
       "tlUpsAlarmShutdownPending": tlUpsAlarmShutdownPending,
       "tlUpsAlarmShutdownImminent": tlUpsAlarmShutdownImminent,
       "tlUpsAlarmTestInProgress": tlUpsAlarmTestInProgress,
       "tlUpsAlarmCircuitBreaker1Open": tlUpsAlarmCircuitBreaker1Open,
       "tlUpsAlarmCircuitBreaker2Open": tlUpsAlarmCircuitBreaker2Open,
       "tlUpsAlarmCircuitBreaker3Open": tlUpsAlarmCircuitBreaker3Open,
       "tlUpsAlarmCircuitBreaker4Open": tlUpsAlarmCircuitBreaker4Open,
       "tlUpsAlarmCircuitBreaker5Open": tlUpsAlarmCircuitBreaker5Open,
       "tlUpsAlarmCircuitBreaker6Open": tlUpsAlarmCircuitBreaker6Open,
       "tlUpsAlarmCircuitBreaker7Open": tlUpsAlarmCircuitBreaker7Open,
       "tlUpsAlarmCircuitBreaker8Open": tlUpsAlarmCircuitBreaker8Open,
       "tlUpsAlarmCurrent1AboveThreshold": tlUpsAlarmCurrent1AboveThreshold,
       "tlUpsAlarmCurrent2AboveThreshold": tlUpsAlarmCurrent2AboveThreshold,
       "tlUpsAlarmCurrent3AboveThreshold": tlUpsAlarmCurrent3AboveThreshold,
       "tlUpsAlarmRuntimeBelowWarningLevel": tlUpsAlarmRuntimeBelowWarningLevel,
       "tlUpsAlarmBusStartVoltageLow": tlUpsAlarmBusStartVoltageLow,
       "tlUpsAlarmBusOverVoltage": tlUpsAlarmBusOverVoltage,
       "tlUpsAlarmBusUnderVoltage": tlUpsAlarmBusUnderVoltage,
       "tlUpsAlarmBusVoltageUnbalanced": tlUpsAlarmBusVoltageUnbalanced,
       "tlUpsAlarmInverterSoftStartBad": tlUpsAlarmInverterSoftStartBad,
       "tlUpsAlarmInverterOverVoltage": tlUpsAlarmInverterOverVoltage,
       "tlUpsAlarmInverterUnderVoltage": tlUpsAlarmInverterUnderVoltage,
       "tlUpsAlarmInverterCircuitBad": tlUpsAlarmInverterCircuitBad,
       "tlUpsAlarmBatteryOverVoltage": tlUpsAlarmBatteryOverVoltage,
       "tlUpsAlarmBatteryUnderVoltage": tlUpsAlarmBatteryUnderVoltage,
       "tlUpsAlarmSiteWiringFault": tlUpsAlarmSiteWiringFault,
       "tlUpsAlarmOverTemperatureProtection": tlUpsAlarmOverTemperatureProtection,
       "tlUpsAlarmOverCharged": tlUpsAlarmOverCharged,
       "tlUpsAlarmEPOActive": tlUpsAlarmEPOActive,
       "tlUpsAlarmBypassFrequencyBad": tlUpsAlarmBypassFrequencyBad,
       "tlUpsAlarmExternalSmartBatteryAgeAboveThreshold": tlUpsAlarmExternalSmartBatteryAgeAboveThreshold,
       "tlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold": tlUpsAlarmExternalNonSmartBatteryAgeAboveThreshold,
       "tlUpsAlarmSmartBatteryCommLost": tlUpsAlarmSmartBatteryCommLost,
       "tlUpsAlarmSourceAOutage": tlUpsAlarmSourceAOutage,
       "tlUpsAlarmSourceBOutage": tlUpsAlarmSourceBOutage,
       "tlUpsAlarmWatchdogReset": tlUpsAlarmWatchdogReset,
       "tlUpsAlarmDevName": tlUpsAlarmDevName,
       "tlUpsAlarmDevLocation": tlUpsAlarmDevLocation,
       "tlUpsAlarmCategory": tlUpsAlarmCategory,
       "tlUpsTest": tlUpsTest,
       "tlUpsTestDate": tlUpsTestDate,
       "tlUpsTestResultsDetail": tlUpsTestResultsDetail,
       "tlUpsControl": tlUpsControl,
       "tlUpsWatchdogSupported": tlUpsWatchdogSupported,
       "tlUpsWatchdogSecsBeforeReboot": tlUpsWatchdogSecsBeforeReboot,
       "tlUpsWellKnownControls": tlUpsWellKnownControls,
       "tlUpsControlSelfTest": tlUpsControlSelfTest,
       "tlUpsControlRamp": tlUpsControlRamp,
       "tlUpsControlShed": tlUpsControlShed,
       "tlUpsControlUpsOn": tlUpsControlUpsOn,
       "tlUpsControlUpsOff": tlUpsControlUpsOff,
       "tlUpsConfig": tlUpsConfig,
       "tlUpsConfigBattReplDate": tlUpsConfigBattReplDate,
       "tlUpsConfigDisplayUnits": tlUpsConfigDisplayUnits,
       "tlUpsConfigExternalBattReplDate": tlUpsConfigExternalBattReplDate,
       "tlUpsOutlet": tlUpsOutlet,
       "tlUpsOutletNumOutlets": tlUpsOutletNumOutlets,
       "tlUpsOutletTable": tlUpsOutletTable,
       "tlUpsOutletEntry": tlUpsOutletEntry,
       "tlUpsOutletIndex": tlUpsOutletIndex,
       "tlUpsOutletState": tlUpsOutletState,
       "tlUpsOutletType": tlUpsOutletType,
       "tlUpsOutletControl": tlUpsOutletControl,
       "tlUpsOutletName": tlUpsOutletName,
       "tlUpsOutletRampAction": tlUpsOutletRampAction,
       "tlUpsOutletRampDataType": tlUpsOutletRampDataType,
       "tlUpsOutletRampData": tlUpsOutletRampData,
       "tlUpsOutletShedAction": tlUpsOutletShedAction,
       "tlUpsOutletShedDataType": tlUpsOutletShedDataType,
       "tlUpsOutletShedData": tlUpsOutletShedData,
       "tlUpsOutletGroupNdx": tlUpsOutletGroupNdx,
       "tlUpsOutletCurrent": tlUpsOutletCurrent,
       "tlUpsOutletPower": tlUpsOutletPower,
       "tlUpsOutletGroup": tlUpsOutletGroup,
       "tlUpsOutletNumOutletGroups": tlUpsOutletNumOutletGroups,
       "tlUpsOutletGroupTable": tlUpsOutletGroupTable,
       "tlUpsOutletGroupEntry": tlUpsOutletGroupEntry,
       "tlUpsOutletGroupIndex": tlUpsOutletGroupIndex,
       "tlUpsOutletGroupRowStatus": tlUpsOutletGroupRowStatus,
       "tlUpsOutletGroupName": tlUpsOutletGroupName,
       "tlUpsOutletGroupDesc": tlUpsOutletGroupDesc,
       "tlUpsOutletGroupState": tlUpsOutletGroupState,
       "tlUpsOutletGroupControl": tlUpsOutletGroupControl,
       "tlUpsMainOutlet": tlUpsMainOutlet,
       "tlUpsMainOutletState": tlUpsMainOutletState,
       "tlUpsMainOutletControllable": tlUpsMainOutletControllable,
       "tlUpsMainOutletControl": tlUpsMainOutletControl,
       "tlUpsEnvironment": tlUpsEnvironment,
       "tlUpsTemperature": tlUpsTemperature,
       "tlUpsTraps": tlUpsTraps,
       "tlUpsTrapAlarmEntryAddedV1": tlUpsTrapAlarmEntryAddedV1,
       "tlUpsTrapAlarmEntryRemovedV1": tlUpsTrapAlarmEntryRemovedV1,
       "tlUpsTrapAlarmEntryAdded": tlUpsTrapAlarmEntryAdded,
       "tlUpsTrapAlarmEntryRemoved": tlUpsTrapAlarmEntryRemoved,
       "tlUpsTrapSystemStartup": tlUpsTrapSystemStartup,
       "tlUpsTrapSystemShutdown": tlUpsTrapSystemShutdown,
       "tlEnviroSense": tlEnviroSense,
       "tlEnvEnvironment": tlEnvEnvironment,
       "tlEnvTemperatureData": tlEnvTemperatureData,
       "tlEnvTemperatureC": tlEnvTemperatureC,
       "tlEnvTemperatureF": tlEnvTemperatureF,
       "tlEnvTemperatureLowLimit": tlEnvTemperatureLowLimit,
       "tlEnvTemperatureHighLimit": tlEnvTemperatureHighLimit,
       "tlEnvTemperatureInAlarm": tlEnvTemperatureInAlarm,
       "tlEnvHumidityData": tlEnvHumidityData,
       "tlEnvHumidity": tlEnvHumidity,
       "tlEnvHumidityLowLimit": tlEnvHumidityLowLimit,
       "tlEnvHumidityHighLimit": tlEnvHumidityHighLimit,
       "tlEnvHumidityInAlarm": tlEnvHumidityInAlarm,
       "tlEnvContacts": tlEnvContacts,
       "tlEnvContactTable": tlEnvContactTable,
       "tlEnvContactEntry": tlEnvContactEntry,
       "tlEnvContactIndex": tlEnvContactIndex,
       "tlEnvContactName": tlEnvContactName,
       "tlEnvContactStatus": tlEnvContactStatus,
       "tlEnvContactConfig": tlEnvContactConfig,
       "tlCooling": tlCooling,
       "tlCoolingEnvironment": tlCoolingEnvironment,
       "tlCoolingIdent": tlCoolingIdent,
       "tlCoolingModel": tlCoolingModel,
       "tlCoolingManufacturer": tlCoolingManufacturer,
       "tlCoolingSerialNumber": tlCoolingSerialNumber,
       "tlCoolingFirmwareVersion": tlCoolingFirmwareVersion,
       "tlCoolingHostSoftwareVersion": tlCoolingHostSoftwareVersion,
       "tlCoolingName": tlCoolingName,
       "tlCoolingLocation": tlCoolingLocation,
       "tlCoolingStatus": tlCoolingStatus,
       "tlCoolingCondOutletTemp": tlCoolingCondOutletTemp,
       "tlCoolingCondInletTemp": tlCoolingCondInletTemp,
       "tlCoolingRefrigerantTemp": tlCoolingRefrigerantTemp,
       "tlCoolingEvapSurfaceTemp": tlCoolingEvapSurfaceTemp,
       "tlCoolingSuctionPressure": tlCoolingSuctionPressure,
       "tlCoolingDischargePressure": tlCoolingDischargePressure,
       "tlCoolingEvapFanSpeed": tlCoolingEvapFanSpeed,
       "tlCoolingCondFanSpeed": tlCoolingCondFanSpeed,
       "tlCoolingCompFrequency": tlCoolingCompFrequency,
       "tlCoolingEEVPercentage": tlCoolingEEVPercentage,
       "tlCoolingUnitCurrent": tlCoolingUnitCurrent,
       "tlCoolingFanCurrent": tlCoolingFanCurrent,
       "tlCoolingCompCurrent": tlCoolingCompCurrent,
       "tlCoolingReturnAirTemp": tlCoolingReturnAirTemp,
       "tlCoolingSuctionTemp": tlCoolingSuctionTemp,
       "tlCoolingSupplyAirTemp": tlCoolingSupplyAirTemp,
       "tlCoolingRunTimes": tlCoolingRunTimes,
       "tlCoolingAirFilterRunHours": tlCoolingAirFilterRunHours,
       "tlCoolingEvapFanRunDays": tlCoolingEvapFanRunDays,
       "tlCoolingCondFanRunDays": tlCoolingCondFanRunDays,
       "tlCoolingCompressorRunDays": tlCoolingCompressorRunDays,
       "tlCoolingCondPumpRunDays": tlCoolingCondPumpRunDays,
       "tlCoolingAtomizerRunDays": tlCoolingAtomizerRunDays,
       "tlCoolingConfig": tlCoolingConfig,
       "tlCoolingOnOff": tlCoolingOnOff,
       "tlCoolingSetPointTemp": tlCoolingSetPointTemp,
       "tlCoolingAutoStart": tlCoolingAutoStart,
       "tlCoolingFanSpeedOverride": tlCoolingFanSpeedOverride,
       "tlCoolingControlType": tlCoolingControlType,
       "tlCoolingCurrentRemoteTemp": tlCoolingCurrentRemoteTemp,
       "tlCoolingDisplayUnits": tlCoolingDisplayUnits,
       "tlCoolingBeepOnKey": tlCoolingBeepOnKey,
       "tlCoolingOutputRelaySource": tlCoolingOutputRelaySource,
       "tlCoolingOffOnLeak": tlCoolingOffOnLeak,
       "tlCoolingOffOnInputContact": tlCoolingOffOnInputContact,
       "tlCoolingInputContactType": tlCoolingInputContactType,
       "tlCoolingOutputRelayDefault": tlCoolingOutputRelayDefault,
       "tlCoolingAirFilterInterval": tlCoolingAirFilterInterval,
       "tlCoolingWaterLeakContactType": tlCoolingWaterLeakContactType,
       "tlCoolingThresholds": tlCoolingThresholds,
       "tlCoolingMaxAirFilterRunHours": tlCoolingMaxAirFilterRunHours,
       "tlCoolingEnableAirFilterAlarm": tlCoolingEnableAirFilterAlarm,
       "tlCoolingMaxSupplyTemp": tlCoolingMaxSupplyTemp,
       "tlCoolingMinSupplyTemp": tlCoolingMinSupplyTemp,
       "tlCoolingTempDiffAlarm": tlCoolingTempDiffAlarm,
       "tlCoolingMaxReturnAirTemp": tlCoolingMaxReturnAirTemp,
       "tlCoolingAlarm": tlCoolingAlarm,
       "tlCoolingWellKnownAlarms": tlCoolingWellKnownAlarms,
       "tlCoolingSupplyAirSensorFault": tlCoolingSupplyAirSensorFault,
       "tlCoolingReturnAirSensorFault": tlCoolingReturnAirSensorFault,
       "tlCoolingCondenserInletAirSensorFault": tlCoolingCondenserInletAirSensorFault,
       "tlCoolingCondenserOutletAirSensorFault": tlCoolingCondenserOutletAirSensorFault,
       "tlCoolingSuctionTemperatureSensorFault": tlCoolingSuctionTemperatureSensorFault,
       "tlCoolingEvaporatorTemperatureSensorFault": tlCoolingEvaporatorTemperatureSensorFault,
       "tlCoolingAirFilterClogged": tlCoolingAirFilterClogged,
       "tlCoolingAirFilterRunHoursViolation": tlCoolingAirFilterRunHoursViolation,
       "tlCoolingSuctionPressureSensorFault": tlCoolingSuctionPressureSensorFault,
       "tlCoolingInverterCommunicationsFault": tlCoolingInverterCommunicationsFault,
       "tlCoolingRemoteShutdownViaInputContact": tlCoolingRemoteShutdownViaInputContact,
       "tlCoolingCondensatePumpFault": tlCoolingCondensatePumpFault,
       "tlCoolingLowRefrigerantStartupFault": tlCoolingLowRefrigerantStartupFault,
       "tlCoolingCondenserFanFault": tlCoolingCondenserFanFault,
       "tlCoolingCondenserFailure": tlCoolingCondenserFailure,
       "tlCoolingEvaporatorCoolingFailure": tlCoolingEvaporatorCoolingFailure,
       "tlCoolingReturnAirTempHigh": tlCoolingReturnAirTempHigh,
       "tlCoolingSupplyAirTempHigh": tlCoolingSupplyAirTempHigh,
       "tlCoolingEvaporatorFailure": tlCoolingEvaporatorFailure,
       "tlCoolingEvaporatorFreezeUp": tlCoolingEvaporatorFreezeUp,
       "tlCoolingDischargePressureHigh": tlCoolingDischargePressureHigh,
       "tlCoolingPressureGaugeFailure": tlCoolingPressureGaugeFailure,
       "tlCoolingDischargePressurePersistentHigh": tlCoolingDischargePressurePersistentHigh,
       "tlCoolingSuctionPressureLowStartFailure": tlCoolingSuctionPressureLowStartFailure,
       "tlCoolingSuctionPressureLow": tlCoolingSuctionPressureLow,
       "tlCoolingSuctionPressurePersistentLow": tlCoolingSuctionPressurePersistentLow,
       "tlCoolingStartupLinePressureImbalance": tlCoolingStartupLinePressureImbalance,
       "tlCoolingCompressorFailure": tlCoolingCompressorFailure,
       "tlCoolingCurrentLimit": tlCoolingCurrentLimit,
       "tlCoolingWaterLeak": tlCoolingWaterLeak,
       "tlCoolingFanUnderCurrent": tlCoolingFanUnderCurrent,
       "tlCoolingFanOverCurrent": tlCoolingFanOverCurrent,
       "tlCoolingDischargePressureSensorFault": tlCoolingDischargePressureSensorFault,
       "tlCoolingWaterFull": tlCoolingWaterFull,
       "tlCoolingAutoCoolingOn": tlCoolingAutoCoolingOn,
       "tlCoolingPowerButtonPressed": tlCoolingPowerButtonPressed,
       "tlCoolingDisconnectedFromDevice": tlCoolingDisconnectedFromDevice,
       "tlSrCoolNet": tlSrCoolNet,
       "tlSrCoolNetData": tlSrCoolNetData,
       "tlSrCoolNetIdent": tlSrCoolNetIdent,
       "tlSrCoolNetModel": tlSrCoolNetModel,
       "tlSrCoolNetManufacturer": tlSrCoolNetManufacturer,
       "tlSrCoolNetSerialNumber": tlSrCoolNetSerialNumber,
       "tlSrCoolNetHostSoftwareVersion": tlSrCoolNetHostSoftwareVersion,
       "tlSrCoolNetName": tlSrCoolNetName,
       "tlSrCoolNetLocation": tlSrCoolNetLocation,
       "tlSrCoolNetStatus": tlSrCoolNetStatus,
       "tlSrCoolNetMode": tlSrCoolNetMode,
       "tlSrCoolNetFanSpeed": tlSrCoolNetFanSpeed,
       "tlSrCoolNetReturnAirTemp": tlSrCoolNetReturnAirTemp,
       "tlSrCoolNetWaterFull": tlSrCoolNetWaterFull,
       "tlSrCoolNetCurrentRemoteTemp": tlSrCoolNetCurrentRemoteTemp,
       "tlSrCoolNetDisplayUnits": tlSrCoolNetDisplayUnits,
       "tlSrCoolNetConfig": tlSrCoolNetConfig,
       "tlSrCoolNetOnOff": tlSrCoolNetOnOff,
       "tlSrCoolSetMode": tlSrCoolSetMode,
       "tlSrCoolNetSetPointTemp": tlSrCoolNetSetPointTemp,
       "tlSrCoolNetRemoteSetPointTemp": tlSrCoolNetRemoteSetPointTemp,
       "tlSrCoolNetFanSpeedSetting": tlSrCoolNetFanSpeedSetting,
       "tlSrCoolNetRemoteSetpointEnable": tlSrCoolNetRemoteSetpointEnable,
       "tlSrCoolNetFanAlwaysOn": tlSrCoolNetFanAlwaysOn,
       "tlSrCoolNetAlarm": tlSrCoolNetAlarm,
       "tlSrCoolNetWellKnownAlarms": tlSrCoolNetWellKnownAlarms,
       "tlSrCoolNetWaterFullAlarm": tlSrCoolNetWaterFullAlarm}
)
