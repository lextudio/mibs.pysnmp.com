# SNMP MIB module (REMOTEACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REMOTEACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:52 2024
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

(rmon,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "rmon")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23)
)
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 19)
)


class _TftpFile_Type(DisplayString):
    """Custom type tftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpFile_Type.__name__ = "DisplayString"
_TftpFile_Object = MibScalar
tftpFile = _TftpFile_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 6),
    _TftpFile_Type()
)
tftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFile.setStatus("current")
_TftpServerIP_Type = IpAddress
_TftpServerIP_Object = MibScalar
tftpServerIP = _TftpServerIP_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 7),
    _TftpServerIP_Type()
)
tftpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIP.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("load", 2),
          ("store", 3))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 8),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("checksumerror", 5),
          ("generalerror", 3),
          ("incompatibleimage", 6),
          ("noresponsefromserver", 4),
          ("statusunknown", 2),
          ("success", 1),
          ("tftpaccessviolation", 8),
          ("tftpfilenotfound", 7))
    )


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 9),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")
_Sonix_ObjectIdentity = ObjectIdentity
sonix = _Sonix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559)
)
_SonixMibs_ObjectIdentity = ObjectIdentity
sonixMibs = _SonixMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1)
)
_RemoteaccessMib_ObjectIdentity = ObjectIdentity
remoteaccessMib = _RemoteaccessMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1)
)


class _Variant_Type(DisplayString):
    """Custom type variant based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Variant_Type.__name__ = "DisplayString"
_Variant_Object = MibTableColumn
variant = _Variant_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 1),
    _Variant_Type()
)
variant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    variant.setStatus("mandatory")


class _Version_Type(DisplayString):
    """Custom type version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Version_Type.__name__ = "DisplayString"
_Version_Object = MibTableColumn
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")


class _Unitname_Type(DisplayString):
    """Custom type unitname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_Unitname_Type.__name__ = "DisplayString"
_Unitname_Object = MibTableColumn
unitname = _Unitname_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 3),
    _Unitname_Type()
)
unitname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitname.setStatus("mandatory")


class _Save_Type(Integer32):
    """Custom type save based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Save_Type.__name__ = "Integer32"
_Save_Object = MibTableColumn
save = _Save_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 4),
    _Save_Type()
)
save.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    save.setStatus("mandatory")


class _Standard_Type(Integer32):
    """Custom type standard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Standard_Type.__name__ = "Integer32"
_Standard_Object = MibTableColumn
standard = _Standard_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 5),
    _Standard_Type()
)
standard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standard.setStatus("mandatory")


class _Saverequired_Type(Integer32):
    """Custom type saverequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Saverequired_Type.__name__ = "Integer32"
_Saverequired_Object = MibTableColumn
saverequired = _Saverequired_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 6),
    _Saverequired_Type()
)
saverequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saverequired.setStatus("mandatory")


class _Date_Type(DisplayString):
    """Custom type date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Date_Type.__name__ = "DisplayString"
_Date_Object = MibTableColumn
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 7),
    _Date_Type()
)
date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date.setStatus("mandatory")


class _Time_Type(DisplayString):
    """Custom type time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Time_Type.__name__ = "DisplayString"
_Time_Object = MibTableColumn
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 8),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("mandatory")


class _Dayoftheweek_Type(Integer32):
    """Custom type dayoftheweek based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_Dayoftheweek_Type.__name__ = "Integer32"
_Dayoftheweek_Object = MibTableColumn
dayoftheweek = _Dayoftheweek_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 9),
    _Dayoftheweek_Type()
)
dayoftheweek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dayoftheweek.setStatus("mandatory")
_Managertimeout_Type = Integer32
_Managertimeout_Object = MibTableColumn
managertimeout = _Managertimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 10),
    _Managertimeout_Type()
)
managertimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managertimeout.setStatus("mandatory")
_Unitipad_Type = IpAddress
_Unitipad_Object = MibTableColumn
unitipad = _Unitipad_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 11),
    _Unitipad_Type()
)
unitipad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitipad.setStatus("mandatory")
_Unitmacaddress_Type = MacAddress
_Unitmacaddress_Object = MibTableColumn
unitmacaddress = _Unitmacaddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 12),
    _Unitmacaddress_Type()
)
unitmacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitmacaddress.setStatus("mandatory")


class _Defaultalert_Type(Integer32):
    """Custom type defaultalert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beep", 2),
          ("disabled", 0),
          ("enabled", 1))
    )


_Defaultalert_Type.__name__ = "Integer32"
_Defaultalert_Object = MibTableColumn
defaultalert = _Defaultalert_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 13),
    _Defaultalert_Type()
)
defaultalert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultalert.setStatus("mandatory")


class _Incallalert_Type(Integer32):
    """Custom type incallalert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beep", 2),
          ("disabled", 0),
          ("enabled", 1))
    )


_Incallalert_Type.__name__ = "Integer32"
_Incallalert_Object = MibTableColumn
incallalert = _Incallalert_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 14),
    _Incallalert_Type()
)
incallalert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incallalert.setStatus("mandatory")


class _Publiccommunity_Type(DisplayString):
    """Custom type publiccommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Publiccommunity_Type.__name__ = "DisplayString"
_Publiccommunity_Object = MibTableColumn
publiccommunity = _Publiccommunity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 15),
    _Publiccommunity_Type()
)
publiccommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    publiccommunity.setStatus("mandatory")


class _Privatecommunity_Type(DisplayString):
    """Custom type privatecommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Privatecommunity_Type.__name__ = "DisplayString"
_Privatecommunity_Object = MibTableColumn
privatecommunity = _Privatecommunity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 16),
    _Privatecommunity_Type()
)
privatecommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privatecommunity.setStatus("mandatory")
_Trapaddress_Type = IpAddress
_Trapaddress_Object = MibTableColumn
trapaddress = _Trapaddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 17),
    _Trapaddress_Type()
)
trapaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapaddress.setStatus("mandatory")
_Trapport_Type = Integer32
_Trapport_Object = MibTableColumn
trapport = _Trapport_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 18),
    _Trapport_Type()
)
trapport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapport.setStatus("mandatory")


class _LcdManagerLock_Type(Integer32):
    """Custom type lcdManagerLock based on Integer32"""
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


_LcdManagerLock_Type.__name__ = "Integer32"
_LcdManagerLock_Object = MibTableColumn
lcdManagerLock = _LcdManagerLock_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 19),
    _LcdManagerLock_Type()
)
lcdManagerLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcdManagerLock.setStatus("mandatory")


class _LoopControl_Type(Integer32):
    """Custom type loopControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_LoopControl_Type.__name__ = "Integer32"
_LoopControl_Object = MibTableColumn
loopControl = _LoopControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 20),
    _LoopControl_Type()
)
loopControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopControl.setStatus("mandatory")
_Novelltimeout_Type = Integer32
_Novelltimeout_Object = MibTableColumn
novelltimeout = _Novelltimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 21),
    _Novelltimeout_Type()
)
novelltimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    novelltimeout.setStatus("mandatory")


class _TimeSinceReboot_Type(DisplayString):
    """Custom type timeSinceReboot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TimeSinceReboot_Type.__name__ = "DisplayString"
_TimeSinceReboot_Object = MibTableColumn
timeSinceReboot = _TimeSinceReboot_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 22),
    _TimeSinceReboot_Type()
)
timeSinceReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSinceReboot.setStatus("mandatory")
_PasswdsTable_Object = MibTable
passwdsTable = _PasswdsTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 23)
)
if mibBuilder.loadTexts:
    passwdsTable.setStatus("mandatory")
_PasswdsEntry_Object = MibTableRow
passwdsEntry = _PasswdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 23, 1)
)
passwdsEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "passwdsOld"),
)
if mibBuilder.loadTexts:
    passwdsEntry.setStatus("mandatory")
_PasswdsOld_Type = DisplayString
_PasswdsOld_Object = MibTableColumn
passwdsOld = _PasswdsOld_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 23, 1, 1),
    _PasswdsOld_Type()
)
passwdsOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwdsOld.setStatus("mandatory")
_PasswdsNew_Type = DisplayString
_PasswdsNew_Object = MibTableColumn
passwdsNew = _PasswdsNew_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 23, 1, 2),
    _PasswdsNew_Type()
)
passwdsNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passwdsNew.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25)
)
_Iprip_ObjectIdentity = ObjectIdentity
iprip = _Iprip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1)
)
_IpInRipRequests_Type = Counter32
_IpInRipRequests_Object = MibTableColumn
ipInRipRequests = _IpInRipRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 1),
    _IpInRipRequests_Type()
)
ipInRipRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInRipRequests.setStatus("mandatory")
_IpInRipResponses_Type = Counter32
_IpInRipResponses_Object = MibTableColumn
ipInRipResponses = _IpInRipResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 2),
    _IpInRipResponses_Type()
)
ipInRipResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInRipResponses.setStatus("mandatory")
_IpInRipErrors_Type = Counter32
_IpInRipErrors_Object = MibTableColumn
ipInRipErrors = _IpInRipErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 3),
    _IpInRipErrors_Type()
)
ipInRipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInRipErrors.setStatus("mandatory")
_IpInRipDiscards_Type = Counter32
_IpInRipDiscards_Object = MibTableColumn
ipInRipDiscards = _IpInRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 4),
    _IpInRipDiscards_Type()
)
ipInRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInRipDiscards.setStatus("mandatory")
_IpOutRipRequests_Type = Counter32
_IpOutRipRequests_Object = MibTableColumn
ipOutRipRequests = _IpOutRipRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 5),
    _IpOutRipRequests_Type()
)
ipOutRipRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRipRequests.setStatus("mandatory")
_IpOutRipResponses_Type = Counter32
_IpOutRipResponses_Object = MibTableColumn
ipOutRipResponses = _IpOutRipResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 6),
    _IpOutRipResponses_Type()
)
ipOutRipResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRipResponses.setStatus("mandatory")
_IpOutRipUpdates_Type = Counter32
_IpOutRipUpdates_Object = MibTableColumn
ipOutRipUpdates = _IpOutRipUpdates_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 7),
    _IpOutRipUpdates_Type()
)
ipOutRipUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRipUpdates.setStatus("mandatory")
_IpOutRipErrors_Type = Counter32
_IpOutRipErrors_Object = MibTableColumn
ipOutRipErrors = _IpOutRipErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 8),
    _IpOutRipErrors_Type()
)
ipOutRipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRipErrors.setStatus("mandatory")
_IpOutRipDiscards_Type = Counter32
_IpOutRipDiscards_Object = MibTableColumn
ipOutRipDiscards = _IpOutRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 9),
    _IpOutRipDiscards_Type()
)
ipOutRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRipDiscards.setStatus("mandatory")


class _IpRoutingProtocol_Type(Integer32):
    """Custom type ipRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("rip2", 2),
          ("ripExtended", 9),
          ("ripFixedMask", 8))
    )


_IpRoutingProtocol_Type.__name__ = "Integer32"
_IpRoutingProtocol_Object = MibTableColumn
ipRoutingProtocol = _IpRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 10),
    _IpRoutingProtocol_Type()
)
ipRoutingProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingProtocol.setStatus("mandatory")


class _IpRipLearning_Type(Integer32):
    """Custom type ipRipLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpRipLearning_Type.__name__ = "Integer32"
_IpRipLearning_Object = MibTableColumn
ipRipLearning = _IpRipLearning_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 11),
    _IpRipLearning_Type()
)
ipRipLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRipLearning.setStatus("mandatory")


class _IpRoutingAdvertise_Type(Integer32):
    """Custom type ipRoutingAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("lan", 3),
          ("none", 1))
    )


_IpRoutingAdvertise_Type.__name__ = "Integer32"
_IpRoutingAdvertise_Object = MibScalar
ipRoutingAdvertise = _IpRoutingAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 1, 12),
    _IpRoutingAdvertise_Type()
)
ipRoutingAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRoutingAdvertise.setStatus("mandatory")
_IpRouteTableCopy_Object = MibTable
ipRouteTableCopy = _IpRouteTableCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2)
)
if mibBuilder.loadTexts:
    ipRouteTableCopy.setStatus("mandatory")
_IpRouteEntryCopy_Object = MibTableRow
ipRouteEntryCopy = _IpRouteEntryCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1)
)
ipRouteEntryCopy.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipRouteDestCopy"),
)
if mibBuilder.loadTexts:
    ipRouteEntryCopy.setStatus("mandatory")
_IpRouteDestCopy_Type = IpAddress
_IpRouteDestCopy_Object = MibTableColumn
ipRouteDestCopy = _IpRouteDestCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 1),
    _IpRouteDestCopy_Type()
)
ipRouteDestCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteDestCopy.setStatus("mandatory")
_IpRouteIfIndexCopy_Type = Integer32
_IpRouteIfIndexCopy_Object = MibTableColumn
ipRouteIfIndexCopy = _IpRouteIfIndexCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 2),
    _IpRouteIfIndexCopy_Type()
)
ipRouteIfIndexCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteIfIndexCopy.setStatus("mandatory")
_IpRouteMetric1Copy_Type = Integer32
_IpRouteMetric1Copy_Object = MibTableColumn
ipRouteMetric1Copy = _IpRouteMetric1Copy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 3),
    _IpRouteMetric1Copy_Type()
)
ipRouteMetric1Copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric1Copy.setStatus("mandatory")
_IpRouteMetric2Copy_Type = Integer32
_IpRouteMetric2Copy_Object = MibTableColumn
ipRouteMetric2Copy = _IpRouteMetric2Copy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 4),
    _IpRouteMetric2Copy_Type()
)
ipRouteMetric2Copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric2Copy.setStatus("mandatory")
_IpRouteMetric3Copy_Type = Integer32
_IpRouteMetric3Copy_Object = MibTableColumn
ipRouteMetric3Copy = _IpRouteMetric3Copy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 5),
    _IpRouteMetric3Copy_Type()
)
ipRouteMetric3Copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric3Copy.setStatus("mandatory")
_IpRouteMetric4Copy_Type = Integer32
_IpRouteMetric4Copy_Object = MibTableColumn
ipRouteMetric4Copy = _IpRouteMetric4Copy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 6),
    _IpRouteMetric4Copy_Type()
)
ipRouteMetric4Copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric4Copy.setStatus("mandatory")
_IpRouteNextHopCopy_Type = IpAddress
_IpRouteNextHopCopy_Object = MibTableColumn
ipRouteNextHopCopy = _IpRouteNextHopCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 7),
    _IpRouteNextHopCopy_Type()
)
ipRouteNextHopCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHopCopy.setStatus("mandatory")


class _IpRouteTypeCopy_Type(Integer32):
    """Custom type ipRouteTypeCopy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_IpRouteTypeCopy_Type.__name__ = "Integer32"
_IpRouteTypeCopy_Object = MibTableColumn
ipRouteTypeCopy = _IpRouteTypeCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 8),
    _IpRouteTypeCopy_Type()
)
ipRouteTypeCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteTypeCopy.setStatus("mandatory")


class _IpRouteProtoCopy_Type(Integer32):
    """Custom type ipRouteProtoCopy based on Integer32"""
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
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpRouteProtoCopy_Type.__name__ = "Integer32"
_IpRouteProtoCopy_Object = MibTableColumn
ipRouteProtoCopy = _IpRouteProtoCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 9),
    _IpRouteProtoCopy_Type()
)
ipRouteProtoCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteProtoCopy.setStatus("mandatory")
_IpRouteAgeCopy_Type = Integer32
_IpRouteAgeCopy_Object = MibTableColumn
ipRouteAgeCopy = _IpRouteAgeCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 10),
    _IpRouteAgeCopy_Type()
)
ipRouteAgeCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteAgeCopy.setStatus("mandatory")
_IpRouteMaskCopy_Type = IpAddress
_IpRouteMaskCopy_Object = MibTableColumn
ipRouteMaskCopy = _IpRouteMaskCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 11),
    _IpRouteMaskCopy_Type()
)
ipRouteMaskCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMaskCopy.setStatus("mandatory")
_IpRouteMetric5Copy_Type = Integer32
_IpRouteMetric5Copy_Object = MibTableColumn
ipRouteMetric5Copy = _IpRouteMetric5Copy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 12),
    _IpRouteMetric5Copy_Type()
)
ipRouteMetric5Copy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric5Copy.setStatus("mandatory")
_IpRouteInfoCopy_Type = ObjectIdentifier
_IpRouteInfoCopy_Object = MibTableColumn
ipRouteInfoCopy = _IpRouteInfoCopy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 13),
    _IpRouteInfoCopy_Type()
)
ipRouteInfoCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfoCopy.setStatus("mandatory")
_IpRouteNextHopName_Type = DisplayString
_IpRouteNextHopName_Object = MibTableColumn
ipRouteNextHopName = _IpRouteNextHopName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 14),
    _IpRouteNextHopName_Type()
)
ipRouteNextHopName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHopName.setStatus("mandatory")


class _IpRouteAdvertise_Type(Integer32):
    """Custom type ipRouteAdvertise based on Integer32"""
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


_IpRouteAdvertise_Type.__name__ = "Integer32"
_IpRouteAdvertise_Object = MibTableColumn
ipRouteAdvertise = _IpRouteAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 25, 2, 1, 15),
    _IpRouteAdvertise_Type()
)
ipRouteAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteAdvertise.setStatus("mandatory")
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26)
)
_IpxInReceives_Type = Counter32
_IpxInReceives_Object = MibTableColumn
ipxInReceives = _IpxInReceives_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 1),
    _IpxInReceives_Type()
)
ipxInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInReceives.setStatus("mandatory")
_IpxInDelivers_Type = Counter32
_IpxInDelivers_Object = MibTableColumn
ipxInDelivers = _IpxInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 2),
    _IpxInDelivers_Type()
)
ipxInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInDelivers.setStatus("mandatory")
_IpxInDiscards_Type = Counter32
_IpxInDiscards_Object = MibTableColumn
ipxInDiscards = _IpxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 3),
    _IpxInDiscards_Type()
)
ipxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInDiscards.setStatus("mandatory")
_IpxInUnknownProtocols_Type = Counter32
_IpxInUnknownProtocols_Object = MibTableColumn
ipxInUnknownProtocols = _IpxInUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 4),
    _IpxInUnknownProtocols_Type()
)
ipxInUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInUnknownProtocols.setStatus("mandatory")
_IpxInHeaderErrors_Type = Counter32
_IpxInHeaderErrors_Object = MibTableColumn
ipxInHeaderErrors = _IpxInHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 5),
    _IpxInHeaderErrors_Type()
)
ipxInHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInHeaderErrors.setStatus("mandatory")
_IpxForwardDatagrams_Type = Counter32
_IpxForwardDatagrams_Object = MibTableColumn
ipxForwardDatagrams = _IpxForwardDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 6),
    _IpxForwardDatagrams_Type()
)
ipxForwardDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxForwardDatagrams.setStatus("mandatory")
_IpxOutRequests_Type = Counter32
_IpxOutRequests_Object = MibTableColumn
ipxOutRequests = _IpxOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 7),
    _IpxOutRequests_Type()
)
ipxOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRequests.setStatus("mandatory")
_IpxOutNoRoutes_Type = Counter32
_IpxOutNoRoutes_Object = MibTableColumn
ipxOutNoRoutes = _IpxOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 8),
    _IpxOutNoRoutes_Type()
)
ipxOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutNoRoutes.setStatus("mandatory")
_IpxOutDiscards_Type = Counter32
_IpxOutDiscards_Object = MibTableColumn
ipxOutDiscards = _IpxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 9),
    _IpxOutDiscards_Type()
)
ipxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutDiscards.setStatus("mandatory")


class _IpxForwarding_Type(Integer32):
    """Custom type ipxForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("not-forwarding", 1))
    )


_IpxForwarding_Type.__name__ = "Integer32"
_IpxForwarding_Object = MibScalar
ipxForwarding = _IpxForwarding_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 10),
    _IpxForwarding_Type()
)
ipxForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxForwarding.setStatus("mandatory")
_Ipxrip_ObjectIdentity = ObjectIdentity
ipxrip = _Ipxrip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11)
)
_IpxInRipRequests_Type = Counter32
_IpxInRipRequests_Object = MibTableColumn
ipxInRipRequests = _IpxInRipRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 1),
    _IpxInRipRequests_Type()
)
ipxInRipRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInRipRequests.setStatus("mandatory")
_IpxInRipResponses_Type = Counter32
_IpxInRipResponses_Object = MibTableColumn
ipxInRipResponses = _IpxInRipResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 2),
    _IpxInRipResponses_Type()
)
ipxInRipResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInRipResponses.setStatus("mandatory")
_IpxInRipErrors_Type = Counter32
_IpxInRipErrors_Object = MibTableColumn
ipxInRipErrors = _IpxInRipErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 3),
    _IpxInRipErrors_Type()
)
ipxInRipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInRipErrors.setStatus("mandatory")
_IpxInRipTimeouts_Type = Counter32
_IpxInRipTimeouts_Object = MibTableColumn
ipxInRipTimeouts = _IpxInRipTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 4),
    _IpxInRipTimeouts_Type()
)
ipxInRipTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInRipTimeouts.setStatus("mandatory")
_IpxInRipDiscards_Type = Counter32
_IpxInRipDiscards_Object = MibTableColumn
ipxInRipDiscards = _IpxInRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 5),
    _IpxInRipDiscards_Type()
)
ipxInRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInRipDiscards.setStatus("mandatory")
_IpxOutRipRequests_Type = Counter32
_IpxOutRipRequests_Object = MibTableColumn
ipxOutRipRequests = _IpxOutRipRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 6),
    _IpxOutRipRequests_Type()
)
ipxOutRipRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRipRequests.setStatus("mandatory")
_IpxOutRipResponses_Type = Counter32
_IpxOutRipResponses_Object = MibTableColumn
ipxOutRipResponses = _IpxOutRipResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 7),
    _IpxOutRipResponses_Type()
)
ipxOutRipResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRipResponses.setStatus("mandatory")
_IpxOutRipUpdates_Type = Counter32
_IpxOutRipUpdates_Object = MibTableColumn
ipxOutRipUpdates = _IpxOutRipUpdates_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 8),
    _IpxOutRipUpdates_Type()
)
ipxOutRipUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRipUpdates.setStatus("mandatory")
_IpxOutRipErrors_Type = Counter32
_IpxOutRipErrors_Object = MibTableColumn
ipxOutRipErrors = _IpxOutRipErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 9),
    _IpxOutRipErrors_Type()
)
ipxOutRipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRipErrors.setStatus("mandatory")
_IpxOutRipDiscards_Type = Counter32
_IpxOutRipDiscards_Object = MibTableColumn
ipxOutRipDiscards = _IpxOutRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 11, 10),
    _IpxOutRipDiscards_Type()
)
ipxOutRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutRipDiscards.setStatus("mandatory")
_Ipxrt_ObjectIdentity = ObjectIdentity
ipxrt = _Ipxrt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12)
)
_IpxRoutingTable_Object = MibTable
ipxRoutingTable = _IpxRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1)
)
if mibBuilder.loadTexts:
    ipxRoutingTable.setStatus("mandatory")
_IpxRoutingTableEntry_Object = MibTableRow
ipxRoutingTableEntry = _IpxRoutingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1)
)
ipxRoutingTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipxRouteTarget"),
)
if mibBuilder.loadTexts:
    ipxRoutingTableEntry.setStatus("mandatory")


class _IpxRouteTarget_Type(OctetString):
    """Custom type ipxRouteTarget based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRouteTarget_Type.__name__ = "OctetString"
_IpxRouteTarget_Object = MibTableColumn
ipxRouteTarget = _IpxRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 1),
    _IpxRouteTarget_Type()
)
ipxRouteTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRouteTarget.setStatus("mandatory")
_IpxRouteHopCount_Type = Integer32
_IpxRouteHopCount_Object = MibTableColumn
ipxRouteHopCount = _IpxRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 2),
    _IpxRouteHopCount_Type()
)
ipxRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteHopCount.setStatus("mandatory")
_IpxRouteTicks_Type = Integer32
_IpxRouteTicks_Object = MibTableColumn
ipxRouteTicks = _IpxRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 3),
    _IpxRouteTicks_Type()
)
ipxRouteTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteTicks.setStatus("mandatory")


class _IpxRouteNextHopNetwork_Type(OctetString):
    """Custom type ipxRouteNextHopNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRouteNextHopNetwork_Type.__name__ = "OctetString"
_IpxRouteNextHopNetwork_Object = MibTableColumn
ipxRouteNextHopNetwork = _IpxRouteNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 4),
    _IpxRouteNextHopNetwork_Type()
)
ipxRouteNextHopNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteNextHopNetwork.setStatus("mandatory")
_IpxRouteNextHopNode_Type = MacAddress
_IpxRouteNextHopNode_Object = MibTableColumn
ipxRouteNextHopNode = _IpxRouteNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 5),
    _IpxRouteNextHopNode_Type()
)
ipxRouteNextHopNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteNextHopNode.setStatus("mandatory")


class _IpxRouteType_Type(Integer32):
    """Custom type ipxRouteType based on Integer32"""
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
        *(("alternate", 3),
          ("autocall", 5),
          ("equal", 4),
          ("local", 2),
          ("permanent", 6),
          ("remote", 1))
    )


_IpxRouteType_Type.__name__ = "Integer32"
_IpxRouteType_Object = MibTableColumn
ipxRouteType = _IpxRouteType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 6),
    _IpxRouteType_Type()
)
ipxRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteType.setStatus("mandatory")
_IpxRoutePort_Type = DisplayString
_IpxRoutePort_Object = MibTableColumn
ipxRoutePort = _IpxRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 7),
    _IpxRoutePort_Type()
)
ipxRoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRoutePort.setStatus("mandatory")


class _IpxRouteLinkType_Type(Integer32):
    """Custom type ipxRouteLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("ppp", 1))
    )


_IpxRouteLinkType_Type.__name__ = "Integer32"
_IpxRouteLinkType_Object = MibTableColumn
ipxRouteLinkType = _IpxRouteLinkType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 8),
    _IpxRouteLinkType_Type()
)
ipxRouteLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteLinkType.setStatus("mandatory")


class _IpxRouteIpxType_Type(Integer32):
    """Custom type ipxRouteIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_IpxRouteIpxType_Type.__name__ = "Integer32"
_IpxRouteIpxType_Object = MibTableColumn
ipxRouteIpxType = _IpxRouteIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 9),
    _IpxRouteIpxType_Type()
)
ipxRouteIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteIpxType.setStatus("mandatory")
_IpxRouteLinkTicks_Type = Integer32
_IpxRouteLinkTicks_Object = MibTableColumn
ipxRouteLinkTicks = _IpxRouteLinkTicks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 10),
    _IpxRouteLinkTicks_Type()
)
ipxRouteLinkTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteLinkTicks.setStatus("mandatory")
_IpxRouteMlink_Type = DisplayString
_IpxRouteMlink_Object = MibTableColumn
ipxRouteMlink = _IpxRouteMlink_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 11),
    _IpxRouteMlink_Type()
)
ipxRouteMlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteMlink.setStatus("mandatory")


class _IpxRouteMode_Type(Integer32):
    """Custom type ipxRouteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_IpxRouteMode_Type.__name__ = "Integer32"
_IpxRouteMode_Object = MibTableColumn
ipxRouteMode = _IpxRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 12, 1, 1, 12),
    _IpxRouteMode_Type()
)
ipxRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouteMode.setStatus("mandatory")
_Ipxsap_ObjectIdentity = ObjectIdentity
ipxsap = _Ipxsap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13)
)
_IpxInSapRequests_Type = Counter32
_IpxInSapRequests_Object = MibTableColumn
ipxInSapRequests = _IpxInSapRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 1),
    _IpxInSapRequests_Type()
)
ipxInSapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInSapRequests.setStatus("mandatory")
_IpxInSapResponses_Type = Counter32
_IpxInSapResponses_Object = MibTableColumn
ipxInSapResponses = _IpxInSapResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 2),
    _IpxInSapResponses_Type()
)
ipxInSapResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInSapResponses.setStatus("mandatory")
_IpxInSapNoServers_Type = Counter32
_IpxInSapNoServers_Object = MibTableColumn
ipxInSapNoServers = _IpxInSapNoServers_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 3),
    _IpxInSapNoServers_Type()
)
ipxInSapNoServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInSapNoServers.setStatus("mandatory")
_IpxInSapErrors_Type = Counter32
_IpxInSapErrors_Object = MibTableColumn
ipxInSapErrors = _IpxInSapErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 4),
    _IpxInSapErrors_Type()
)
ipxInSapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInSapErrors.setStatus("mandatory")
_IpxInSapDiscards_Type = Counter32
_IpxInSapDiscards_Object = MibTableColumn
ipxInSapDiscards = _IpxInSapDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 5),
    _IpxInSapDiscards_Type()
)
ipxInSapDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxInSapDiscards.setStatus("mandatory")
_IpxOutSapRequests_Type = Counter32
_IpxOutSapRequests_Object = MibTableColumn
ipxOutSapRequests = _IpxOutSapRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 6),
    _IpxOutSapRequests_Type()
)
ipxOutSapRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutSapRequests.setStatus("mandatory")
_IpxOutSapResponses_Type = Counter32
_IpxOutSapResponses_Object = MibTableColumn
ipxOutSapResponses = _IpxOutSapResponses_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 7),
    _IpxOutSapResponses_Type()
)
ipxOutSapResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutSapResponses.setStatus("mandatory")
_IpxOutSapErrors_Type = Counter32
_IpxOutSapErrors_Object = MibTableColumn
ipxOutSapErrors = _IpxOutSapErrors_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 8),
    _IpxOutSapErrors_Type()
)
ipxOutSapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutSapErrors.setStatus("mandatory")
_IpxOutSapDiscards_Type = Counter32
_IpxOutSapDiscards_Object = MibTableColumn
ipxOutSapDiscards = _IpxOutSapDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 13, 9),
    _IpxOutSapDiscards_Type()
)
ipxOutSapDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxOutSapDiscards.setStatus("mandatory")
_Ipxsapt_ObjectIdentity = ObjectIdentity
ipxsapt = _Ipxsapt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14)
)
_IpxServicesTable_Object = MibTable
ipxServicesTable = _IpxServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1)
)
if mibBuilder.loadTexts:
    ipxServicesTable.setStatus("mandatory")
_IpxServicesTableEntry_Object = MibTableRow
ipxServicesTableEntry = _IpxServicesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1)
)
ipxServicesTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipxServiceNode"),
    (0, "REMOTEACCESS-MIB", "ipxServiceSocket"),
)
if mibBuilder.loadTexts:
    ipxServicesTableEntry.setStatus("mandatory")


class _IpxServiceNetwork_Type(OctetString):
    """Custom type ipxServiceNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxServiceNetwork_Type.__name__ = "OctetString"
_IpxServiceNetwork_Object = MibTableColumn
ipxServiceNetwork = _IpxServiceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 1),
    _IpxServiceNetwork_Type()
)
ipxServiceNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceNetwork.setStatus("mandatory")
_IpxServiceNode_Type = MacAddress
_IpxServiceNode_Object = MibTableColumn
ipxServiceNode = _IpxServiceNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 2),
    _IpxServiceNode_Type()
)
ipxServiceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServiceNode.setStatus("mandatory")
_IpxServiceSocket_Type = Integer32
_IpxServiceSocket_Object = MibTableColumn
ipxServiceSocket = _IpxServiceSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 3),
    _IpxServiceSocket_Type()
)
ipxServiceSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServiceSocket.setStatus("mandatory")
_IpxServiceName_Type = DisplayString
_IpxServiceName_Object = MibTableColumn
ipxServiceName = _IpxServiceName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 4),
    _IpxServiceName_Type()
)
ipxServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceName.setStatus("mandatory")
_IpxServiceType_Type = Integer32
_IpxServiceType_Object = MibTableColumn
ipxServiceType = _IpxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 5),
    _IpxServiceType_Type()
)
ipxServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceType.setStatus("mandatory")
_IpxServiceHopCount_Type = Integer32
_IpxServiceHopCount_Object = MibTableColumn
ipxServiceHopCount = _IpxServiceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 6),
    _IpxServiceHopCount_Type()
)
ipxServiceHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceHopCount.setStatus("mandatory")
_IpxServicePort_Type = DisplayString
_IpxServicePort_Object = MibTableColumn
ipxServicePort = _IpxServicePort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 7),
    _IpxServicePort_Type()
)
ipxServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServicePort.setStatus("mandatory")


class _IpxServiceNextHopNetwork_Type(OctetString):
    """Custom type ipxServiceNextHopNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxServiceNextHopNetwork_Type.__name__ = "OctetString"
_IpxServiceNextHopNetwork_Object = MibTableColumn
ipxServiceNextHopNetwork = _IpxServiceNextHopNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 8),
    _IpxServiceNextHopNetwork_Type()
)
ipxServiceNextHopNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceNextHopNetwork.setStatus("mandatory")
_IpxServiceNextHopNode_Type = MacAddress
_IpxServiceNextHopNode_Object = MibTableColumn
ipxServiceNextHopNode = _IpxServiceNextHopNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 9),
    _IpxServiceNextHopNode_Type()
)
ipxServiceNextHopNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceNextHopNode.setStatus("mandatory")


class _IpxServiceIpxType_Type(Integer32):
    """Custom type ipxServiceIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_IpxServiceIpxType_Type.__name__ = "Integer32"
_IpxServiceIpxType_Object = MibTableColumn
ipxServiceIpxType = _IpxServiceIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 10),
    _IpxServiceIpxType_Type()
)
ipxServiceIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceIpxType.setStatus("mandatory")


class _IpxServiceRTType_Type(Integer32):
    """Custom type ipxServiceRTType based on Integer32"""
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
        *(("alternate", 3),
          ("autocall", 5),
          ("equal", 4),
          ("local", 2),
          ("permanent", 6),
          ("remote", 1))
    )


_IpxServiceRTType_Type.__name__ = "Integer32"
_IpxServiceRTType_Object = MibTableColumn
ipxServiceRTType = _IpxServiceRTType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 11),
    _IpxServiceRTType_Type()
)
ipxServiceRTType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceRTType.setStatus("mandatory")


class _IpxServiceLinkType_Type(Integer32):
    """Custom type ipxServiceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("ppp", 1))
    )


_IpxServiceLinkType_Type.__name__ = "Integer32"
_IpxServiceLinkType_Object = MibTableColumn
ipxServiceLinkType = _IpxServiceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 12),
    _IpxServiceLinkType_Type()
)
ipxServiceLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceLinkType.setStatus("mandatory")
_IpxServiceMlink_Type = DisplayString
_IpxServiceMlink_Object = MibTableColumn
ipxServiceMlink = _IpxServiceMlink_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 13),
    _IpxServiceMlink_Type()
)
ipxServiceMlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceMlink.setStatus("mandatory")


class _IpxServiceMode_Type(Integer32):
    """Custom type ipxServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_IpxServiceMode_Type.__name__ = "Integer32"
_IpxServiceMode_Object = MibTableColumn
ipxServiceMode = _IpxServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 14, 1, 1, 14),
    _IpxServiceMode_Type()
)
ipxServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServiceMode.setStatus("mandatory")
_Ipxnear_ObjectIdentity = ObjectIdentity
ipxnear = _Ipxnear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15)
)


class _IpxNearest_Type(Integer32):
    """Custom type ipxNearest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_IpxNearest_Type.__name__ = "Integer32"
_IpxNearest_Object = MibScalar
ipxNearest = _IpxNearest_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 1),
    _IpxNearest_Type()
)
ipxNearest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNearest.setStatus("mandatory")
_IpxNearestTable_Object = MibTable
ipxNearestTable = _IpxNearestTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 2)
)
if mibBuilder.loadTexts:
    ipxNearestTable.setStatus("mandatory")
_IpxNearestTableEntry_Object = MibTableRow
ipxNearestTableEntry = _IpxNearestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 2, 1)
)
ipxNearestTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipxNearestIndex"),
)
if mibBuilder.loadTexts:
    ipxNearestTableEntry.setStatus("mandatory")
_IpxNearestIndex_Type = Integer32
_IpxNearestIndex_Object = MibTableColumn
ipxNearestIndex = _IpxNearestIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 2, 1, 1),
    _IpxNearestIndex_Type()
)
ipxNearestIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNearestIndex.setStatus("mandatory")
_IpxNearestServer_Type = DisplayString
_IpxNearestServer_Object = MibTableColumn
ipxNearestServer = _IpxNearestServer_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 2, 1, 2),
    _IpxNearestServer_Type()
)
ipxNearestServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNearestServer.setStatus("mandatory")


class _IpxNearestMode_Type(Integer32):
    """Custom type ipxNearestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_IpxNearestMode_Type.__name__ = "Integer32"
_IpxNearestMode_Object = MibTableColumn
ipxNearestMode = _IpxNearestMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 26, 15, 2, 1, 3),
    _IpxNearestMode_Type()
)
ipxNearestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxNearestMode.setStatus("mandatory")
_Pppext_ObjectIdentity = ObjectIdentity
pppext = _Pppext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27)
)
_PppExtLcpConfigTable_Object = MibTable
pppExtLcpConfigTable = _PppExtLcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1)
)
if mibBuilder.loadTexts:
    pppExtLcpConfigTable.setStatus("mandatory")
_PppExtLcpConfigTableEntry_Object = MibTableRow
pppExtLcpConfigTableEntry = _PppExtLcpConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1)
)
pppExtLcpConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppExtLcpConfigTableEntry.setStatus("mandatory")


class _PppExtLcpLocalProtocolCompression_Type(Integer32):
    """Custom type pppExtLcpLocalProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpLocalProtocolCompression_Type.__name__ = "Integer32"
_PppExtLcpLocalProtocolCompression_Object = MibTableColumn
pppExtLcpLocalProtocolCompression = _PppExtLcpLocalProtocolCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 1),
    _PppExtLcpLocalProtocolCompression_Type()
)
pppExtLcpLocalProtocolCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalProtocolCompression.setStatus("mandatory")


class _PppExtLcpLocalAddressCompression_Type(Integer32):
    """Custom type pppExtLcpLocalAddressCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpLocalAddressCompression_Type.__name__ = "Integer32"
_PppExtLcpLocalAddressCompression_Object = MibTableColumn
pppExtLcpLocalAddressCompression = _PppExtLcpLocalAddressCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 2),
    _PppExtLcpLocalAddressCompression_Type()
)
pppExtLcpLocalAddressCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalAddressCompression.setStatus("mandatory")
_PppExtLcpRemoteMRU_Type = Integer32
_PppExtLcpRemoteMRU_Object = MibTableColumn
pppExtLcpRemoteMRU = _PppExtLcpRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 3),
    _PppExtLcpRemoteMRU_Type()
)
pppExtLcpRemoteMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteMRU.setStatus("mandatory")


class _PppExtLcpRemoteProtocolCompression_Type(Integer32):
    """Custom type pppExtLcpRemoteProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpRemoteProtocolCompression_Type.__name__ = "Integer32"
_PppExtLcpRemoteProtocolCompression_Object = MibTableColumn
pppExtLcpRemoteProtocolCompression = _PppExtLcpRemoteProtocolCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 4),
    _PppExtLcpRemoteProtocolCompression_Type()
)
pppExtLcpRemoteProtocolCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteProtocolCompression.setStatus("mandatory")


class _PppExtLcpRemoteAddressCompression_Type(Integer32):
    """Custom type pppExtLcpRemoteAddressCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpRemoteAddressCompression_Type.__name__ = "Integer32"
_PppExtLcpRemoteAddressCompression_Object = MibTableColumn
pppExtLcpRemoteAddressCompression = _PppExtLcpRemoteAddressCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 5),
    _PppExtLcpRemoteAddressCompression_Type()
)
pppExtLcpRemoteAddressCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteAddressCompression.setStatus("mandatory")
_PppExtLcpMinimumRestartPeriod_Type = Integer32
_PppExtLcpMinimumRestartPeriod_Object = MibTableColumn
pppExtLcpMinimumRestartPeriod = _PppExtLcpMinimumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 6),
    _PppExtLcpMinimumRestartPeriod_Type()
)
pppExtLcpMinimumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpMinimumRestartPeriod.setStatus("mandatory")
_PppExtLcpMaximumRestartPeriod_Type = Integer32
_PppExtLcpMaximumRestartPeriod_Object = MibTableColumn
pppExtLcpMaximumRestartPeriod = _PppExtLcpMaximumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 7),
    _PppExtLcpMaximumRestartPeriod_Type()
)
pppExtLcpMaximumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpMaximumRestartPeriod.setStatus("mandatory")
_PppExtLcpMaximumTerminateRequests_Type = Integer32
_PppExtLcpMaximumTerminateRequests_Object = MibTableColumn
pppExtLcpMaximumTerminateRequests = _PppExtLcpMaximumTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 8),
    _PppExtLcpMaximumTerminateRequests_Type()
)
pppExtLcpMaximumTerminateRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpMaximumTerminateRequests.setStatus("mandatory")
_PppExtLcpMaximumConfigRequests_Type = Integer32
_PppExtLcpMaximumConfigRequests_Object = MibTableColumn
pppExtLcpMaximumConfigRequests = _PppExtLcpMaximumConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 9),
    _PppExtLcpMaximumConfigRequests_Type()
)
pppExtLcpMaximumConfigRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpMaximumConfigRequests.setStatus("mandatory")
_PppExtLcpMaximumConfigNaks_Type = Integer32
_PppExtLcpMaximumConfigNaks_Object = MibTableColumn
pppExtLcpMaximumConfigNaks = _PppExtLcpMaximumConfigNaks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 10),
    _PppExtLcpMaximumConfigNaks_Type()
)
pppExtLcpMaximumConfigNaks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpMaximumConfigNaks.setStatus("mandatory")
_PppExtLcpLocalMRU_Type = Integer32
_PppExtLcpLocalMRU_Object = MibTableColumn
pppExtLcpLocalMRU = _PppExtLcpLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 11),
    _PppExtLcpLocalMRU_Type()
)
pppExtLcpLocalMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalMRU.setStatus("mandatory")


class _PppExtLcpLocalMagic_Type(Integer32):
    """Custom type pppExtLcpLocalMagic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpLocalMagic_Type.__name__ = "Integer32"
_PppExtLcpLocalMagic_Object = MibTableColumn
pppExtLcpLocalMagic = _PppExtLcpLocalMagic_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 12),
    _PppExtLcpLocalMagic_Type()
)
pppExtLcpLocalMagic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalMagic.setStatus("mandatory")


class _PppExtLcpRemoteMagic_Type(Integer32):
    """Custom type pppExtLcpRemoteMagic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpRemoteMagic_Type.__name__ = "Integer32"
_PppExtLcpRemoteMagic_Object = MibTableColumn
pppExtLcpRemoteMagic = _PppExtLcpRemoteMagic_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 13),
    _PppExtLcpRemoteMagic_Type()
)
pppExtLcpRemoteMagic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteMagic.setStatus("mandatory")


class _PppExtLcpLocalMRUEnabled_Type(Integer32):
    """Custom type pppExtLcpLocalMRUEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpLocalMRUEnabled_Type.__name__ = "Integer32"
_PppExtLcpLocalMRUEnabled_Object = MibTableColumn
pppExtLcpLocalMRUEnabled = _PppExtLcpLocalMRUEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 14),
    _PppExtLcpLocalMRUEnabled_Type()
)
pppExtLcpLocalMRUEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalMRUEnabled.setStatus("mandatory")


class _PppExtLcpRemoteMRUEnabled_Type(Integer32):
    """Custom type pppExtLcpRemoteMRUEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpRemoteMRUEnabled_Type.__name__ = "Integer32"
_PppExtLcpRemoteMRUEnabled_Object = MibTableColumn
pppExtLcpRemoteMRUEnabled = _PppExtLcpRemoteMRUEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 15),
    _PppExtLcpRemoteMRUEnabled_Type()
)
pppExtLcpRemoteMRUEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteMRUEnabled.setStatus("mandatory")
_PppExtLcpLocalACCM_Type = Integer32
_PppExtLcpLocalACCM_Object = MibTableColumn
pppExtLcpLocalACCM = _PppExtLcpLocalACCM_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 16),
    _PppExtLcpLocalACCM_Type()
)
pppExtLcpLocalACCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalACCM.setStatus("mandatory")
_PppExtLcpRemoteACCM_Type = Integer32
_PppExtLcpRemoteACCM_Object = MibTableColumn
pppExtLcpRemoteACCM = _PppExtLcpRemoteACCM_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 17),
    _PppExtLcpRemoteACCM_Type()
)
pppExtLcpRemoteACCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteACCM.setStatus("mandatory")
_PppExtLcpLocalACCMEnabled_Type = Integer32
_PppExtLcpLocalACCMEnabled_Object = MibTableColumn
pppExtLcpLocalACCMEnabled = _PppExtLcpLocalACCMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 18),
    _PppExtLcpLocalACCMEnabled_Type()
)
pppExtLcpLocalACCMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalACCMEnabled.setStatus("mandatory")
_PppExtLcpRemoteACCMEnabled_Type = Integer32
_PppExtLcpRemoteACCMEnabled_Object = MibTableColumn
pppExtLcpRemoteACCMEnabled = _PppExtLcpRemoteACCMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 19),
    _PppExtLcpRemoteACCMEnabled_Type()
)
pppExtLcpRemoteACCMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteACCMEnabled.setStatus("mandatory")


class _PppExtLcpLocalPAPEnabled_Type(Integer32):
    """Custom type pppExtLcpLocalPAPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("incoming", 3))
    )


_PppExtLcpLocalPAPEnabled_Type.__name__ = "Integer32"
_PppExtLcpLocalPAPEnabled_Object = MibTableColumn
pppExtLcpLocalPAPEnabled = _PppExtLcpLocalPAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 20),
    _PppExtLcpLocalPAPEnabled_Type()
)
pppExtLcpLocalPAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalPAPEnabled.setStatus("mandatory")


class _PppExtLcpRemotePAPEnabled_Type(Integer32):
    """Custom type pppExtLcpRemotePAPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PppExtLcpRemotePAPEnabled_Type.__name__ = "Integer32"
_PppExtLcpRemotePAPEnabled_Object = MibTableColumn
pppExtLcpRemotePAPEnabled = _PppExtLcpRemotePAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 21),
    _PppExtLcpRemotePAPEnabled_Type()
)
pppExtLcpRemotePAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemotePAPEnabled.setStatus("mandatory")
_PppExtLcpLocalCHAPEnabled_Type = Integer32
_PppExtLcpLocalCHAPEnabled_Object = MibTableColumn
pppExtLcpLocalCHAPEnabled = _PppExtLcpLocalCHAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 22),
    _PppExtLcpLocalCHAPEnabled_Type()
)
pppExtLcpLocalCHAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpLocalCHAPEnabled.setStatus("mandatory")
_PppExtLcpRemoteCHAPEnabled_Type = Integer32
_PppExtLcpRemoteCHAPEnabled_Object = MibTableColumn
pppExtLcpRemoteCHAPEnabled = _PppExtLcpRemoteCHAPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 1, 1, 23),
    _PppExtLcpRemoteCHAPEnabled_Type()
)
pppExtLcpRemoteCHAPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLcpRemoteCHAPEnabled.setStatus("mandatory")
_PppEchoConfigTable_Object = MibTable
pppEchoConfigTable = _PppEchoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 2)
)
if mibBuilder.loadTexts:
    pppEchoConfigTable.setStatus("mandatory")
_PppEchoConfigTableEntry_Object = MibTableRow
pppEchoConfigTableEntry = _PppEchoConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 2, 1)
)
pppEchoConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppEchoConfigTableEntry.setStatus("mandatory")
_PppEchoPeriod_Type = Integer32
_PppEchoPeriod_Object = MibTableColumn
pppEchoPeriod = _PppEchoPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 2, 1, 1),
    _PppEchoPeriod_Type()
)
pppEchoPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEchoPeriod.setStatus("mandatory")
_PppEchoMaxNumberRetransmits_Type = Integer32
_PppEchoMaxNumberRetransmits_Object = MibTableColumn
pppEchoMaxNumberRetransmits = _PppEchoMaxNumberRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 2, 1, 2),
    _PppEchoMaxNumberRetransmits_Type()
)
pppEchoMaxNumberRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppEchoMaxNumberRetransmits.setStatus("mandatory")
_PppIpcpConfigTable_Object = MibTable
pppIpcpConfigTable = _PppIpcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3)
)
if mibBuilder.loadTexts:
    pppIpcpConfigTable.setStatus("mandatory")
_PppIpcpConfigTableEntry_Object = MibTableRow
pppIpcpConfigTableEntry = _PppIpcpConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1)
)
pppIpcpConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppIpcpConfigTableEntry.setStatus("mandatory")


class _IpcpLocalIPAddressNegotiation_Type(Integer32):
    """Custom type ipcpLocalIPAddressNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpcpLocalIPAddressNegotiation_Type.__name__ = "Integer32"
_IpcpLocalIPAddressNegotiation_Object = MibTableColumn
ipcpLocalIPAddressNegotiation = _IpcpLocalIPAddressNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 1),
    _IpcpLocalIPAddressNegotiation_Type()
)
ipcpLocalIPAddressNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpLocalIPAddressNegotiation.setStatus("mandatory")


class _IpcpRemoteIPAddressNegotiation_Type(Integer32):
    """Custom type ipcpRemoteIPAddressNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpcpRemoteIPAddressNegotiation_Type.__name__ = "Integer32"
_IpcpRemoteIPAddressNegotiation_Object = MibTableColumn
ipcpRemoteIPAddressNegotiation = _IpcpRemoteIPAddressNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 2),
    _IpcpRemoteIPAddressNegotiation_Type()
)
ipcpRemoteIPAddressNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpRemoteIPAddressNegotiation.setStatus("mandatory")


class _IpcpRemoteCompressionNegotiation_Type(Integer32):
    """Custom type ipcpRemoteCompressionNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("none", 1),
          ("van-jacobson", 2))
    )


_IpcpRemoteCompressionNegotiation_Type.__name__ = "Integer32"
_IpcpRemoteCompressionNegotiation_Object = MibTableColumn
ipcpRemoteCompressionNegotiation = _IpcpRemoteCompressionNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 3),
    _IpcpRemoteCompressionNegotiation_Type()
)
ipcpRemoteCompressionNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpRemoteCompressionNegotiation.setStatus("mandatory")
_IpcpMinimumRestartPeriod_Type = Integer32
_IpcpMinimumRestartPeriod_Object = MibTableColumn
ipcpMinimumRestartPeriod = _IpcpMinimumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 4),
    _IpcpMinimumRestartPeriod_Type()
)
ipcpMinimumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpMinimumRestartPeriod.setStatus("mandatory")
_IpcpMaximumRestartPeriod_Type = Integer32
_IpcpMaximumRestartPeriod_Object = MibTableColumn
ipcpMaximumRestartPeriod = _IpcpMaximumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 5),
    _IpcpMaximumRestartPeriod_Type()
)
ipcpMaximumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpMaximumRestartPeriod.setStatus("mandatory")
_IpcpMaximumTerminateRequests_Type = Integer32
_IpcpMaximumTerminateRequests_Object = MibTableColumn
ipcpMaximumTerminateRequests = _IpcpMaximumTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 6),
    _IpcpMaximumTerminateRequests_Type()
)
ipcpMaximumTerminateRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpMaximumTerminateRequests.setStatus("mandatory")
_IpcpMaximumConfigRequests_Type = Integer32
_IpcpMaximumConfigRequests_Object = MibTableColumn
ipcpMaximumConfigRequests = _IpcpMaximumConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 7),
    _IpcpMaximumConfigRequests_Type()
)
ipcpMaximumConfigRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpMaximumConfigRequests.setStatus("mandatory")
_IpcpMaximumConfigNaks_Type = Integer32
_IpcpMaximumConfigNaks_Object = MibTableColumn
ipcpMaximumConfigNaks = _IpcpMaximumConfigNaks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 8),
    _IpcpMaximumConfigNaks_Type()
)
ipcpMaximumConfigNaks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpMaximumConfigNaks.setStatus("mandatory")


class _IpcpLocalCompressionNegotiation_Type(Integer32):
    """Custom type ipcpLocalCompressionNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("none", 1),
          ("van-jacobson", 2))
    )


_IpcpLocalCompressionNegotiation_Type.__name__ = "Integer32"
_IpcpLocalCompressionNegotiation_Object = MibTableColumn
ipcpLocalCompressionNegotiation = _IpcpLocalCompressionNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 9),
    _IpcpLocalCompressionNegotiation_Type()
)
ipcpLocalCompressionNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpLocalCompressionNegotiation.setStatus("mandatory")


class _IpcpRfc1172Negotiation_Type(Integer32):
    """Custom type ipcpRfc1172Negotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpcpRfc1172Negotiation_Type.__name__ = "Integer32"
_IpcpRfc1172Negotiation_Object = MibTableColumn
ipcpRfc1172Negotiation = _IpcpRfc1172Negotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 3, 1, 10),
    _IpcpRfc1172Negotiation_Type()
)
ipcpRfc1172Negotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipcpRfc1172Negotiation.setStatus("mandatory")
_PppIpxcpConfigTable_Object = MibTable
pppIpxcpConfigTable = _PppIpxcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4)
)
if mibBuilder.loadTexts:
    pppIpxcpConfigTable.setStatus("mandatory")
_PppIpxcpConfigTableEntry_Object = MibTableRow
pppIpxcpConfigTableEntry = _PppIpxcpConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1)
)
pppIpxcpConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppIpxcpConfigTableEntry.setStatus("mandatory")


class _IpxcpLocalNetworkNumberNegotiation_Type(Integer32):
    """Custom type ipxcpLocalNetworkNumberNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpLocalNetworkNumberNegotiation_Type.__name__ = "Integer32"
_IpxcpLocalNetworkNumberNegotiation_Object = MibTableColumn
ipxcpLocalNetworkNumberNegotiation = _IpxcpLocalNetworkNumberNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 1),
    _IpxcpLocalNetworkNumberNegotiation_Type()
)
ipxcpLocalNetworkNumberNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpLocalNetworkNumberNegotiation.setStatus("mandatory")


class _IpxcpLocalNodeNumberNegotiation_Type(Integer32):
    """Custom type ipxcpLocalNodeNumberNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpLocalNodeNumberNegotiation_Type.__name__ = "Integer32"
_IpxcpLocalNodeNumberNegotiation_Object = MibTableColumn
ipxcpLocalNodeNumberNegotiation = _IpxcpLocalNodeNumberNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 2),
    _IpxcpLocalNodeNumberNegotiation_Type()
)
ipxcpLocalNodeNumberNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpLocalNodeNumberNegotiation.setStatus("mandatory")


class _IpxcpLocalRoutingProtocolNegotiation_Type(Integer32):
    """Custom type ipxcpLocalRoutingProtocolNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("default", 4),
          ("none", 1),
          ("rip-sap", 2))
    )


_IpxcpLocalRoutingProtocolNegotiation_Type.__name__ = "Integer32"
_IpxcpLocalRoutingProtocolNegotiation_Object = MibTableColumn
ipxcpLocalRoutingProtocolNegotiation = _IpxcpLocalRoutingProtocolNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 3),
    _IpxcpLocalRoutingProtocolNegotiation_Type()
)
ipxcpLocalRoutingProtocolNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpLocalRoutingProtocolNegotiation.setStatus("mandatory")


class _IpxcpLocalRouterNameNegotiation_Type(Integer32):
    """Custom type ipxcpLocalRouterNameNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpLocalRouterNameNegotiation_Type.__name__ = "Integer32"
_IpxcpLocalRouterNameNegotiation_Object = MibTableColumn
ipxcpLocalRouterNameNegotiation = _IpxcpLocalRouterNameNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 4),
    _IpxcpLocalRouterNameNegotiation_Type()
)
ipxcpLocalRouterNameNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpLocalRouterNameNegotiation.setStatus("mandatory")


class _IpxcpRemoteNetworkNumberNegotiation_Type(Integer32):
    """Custom type ipxcpRemoteNetworkNumberNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpRemoteNetworkNumberNegotiation_Type.__name__ = "Integer32"
_IpxcpRemoteNetworkNumberNegotiation_Object = MibTableColumn
ipxcpRemoteNetworkNumberNegotiation = _IpxcpRemoteNetworkNumberNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 5),
    _IpxcpRemoteNetworkNumberNegotiation_Type()
)
ipxcpRemoteNetworkNumberNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpRemoteNetworkNumberNegotiation.setStatus("mandatory")


class _IpxcpRemoteNodeNumberNegotiation_Type(Integer32):
    """Custom type ipxcpRemoteNodeNumberNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpRemoteNodeNumberNegotiation_Type.__name__ = "Integer32"
_IpxcpRemoteNodeNumberNegotiation_Object = MibTableColumn
ipxcpRemoteNodeNumberNegotiation = _IpxcpRemoteNodeNumberNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 6),
    _IpxcpRemoteNodeNumberNegotiation_Type()
)
ipxcpRemoteNodeNumberNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpRemoteNodeNumberNegotiation.setStatus("mandatory")


class _IpxcpRemoteRoutingProtocolNegotiation_Type(Integer32):
    """Custom type ipxcpRemoteRoutingProtocolNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("default", 4),
          ("none", 1),
          ("rip-sap", 2))
    )


_IpxcpRemoteRoutingProtocolNegotiation_Type.__name__ = "Integer32"
_IpxcpRemoteRoutingProtocolNegotiation_Object = MibTableColumn
ipxcpRemoteRoutingProtocolNegotiation = _IpxcpRemoteRoutingProtocolNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 7),
    _IpxcpRemoteRoutingProtocolNegotiation_Type()
)
ipxcpRemoteRoutingProtocolNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpRemoteRoutingProtocolNegotiation.setStatus("mandatory")


class _IpxcpRemoteRouterNameNegotiation_Type(Integer32):
    """Custom type ipxcpRemoteRouterNameNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpRemoteRouterNameNegotiation_Type.__name__ = "Integer32"
_IpxcpRemoteRouterNameNegotiation_Object = MibTableColumn
ipxcpRemoteRouterNameNegotiation = _IpxcpRemoteRouterNameNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 8),
    _IpxcpRemoteRouterNameNegotiation_Type()
)
ipxcpRemoteRouterNameNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpRemoteRouterNameNegotiation.setStatus("mandatory")


class _IpxcpConfigCompleteNegotiation_Type(Integer32):
    """Custom type ipxcpConfigCompleteNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpxcpConfigCompleteNegotiation_Type.__name__ = "Integer32"
_IpxcpConfigCompleteNegotiation_Object = MibTableColumn
ipxcpConfigCompleteNegotiation = _IpxcpConfigCompleteNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 9),
    _IpxcpConfigCompleteNegotiation_Type()
)
ipxcpConfigCompleteNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpConfigCompleteNegotiation.setStatus("mandatory")


class _IpxcpAdmin_Type(Integer32):
    """Custom type ipxcpAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("opened", 1))
    )


_IpxcpAdmin_Type.__name__ = "Integer32"
_IpxcpAdmin_Object = MibTableColumn
ipxcpAdmin = _IpxcpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 10),
    _IpxcpAdmin_Type()
)
ipxcpAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpAdmin.setStatus("mandatory")
_IpxcpMinimumRestartPeriod_Type = Integer32
_IpxcpMinimumRestartPeriod_Object = MibTableColumn
ipxcpMinimumRestartPeriod = _IpxcpMinimumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 11),
    _IpxcpMinimumRestartPeriod_Type()
)
ipxcpMinimumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpMinimumRestartPeriod.setStatus("mandatory")
_IpxcpMaximumRestartPeriod_Type = Integer32
_IpxcpMaximumRestartPeriod_Object = MibTableColumn
ipxcpMaximumRestartPeriod = _IpxcpMaximumRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 12),
    _IpxcpMaximumRestartPeriod_Type()
)
ipxcpMaximumRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpMaximumRestartPeriod.setStatus("mandatory")
_IpxcpMaximumTerminateRequests_Type = Integer32
_IpxcpMaximumTerminateRequests_Object = MibTableColumn
ipxcpMaximumTerminateRequests = _IpxcpMaximumTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 13),
    _IpxcpMaximumTerminateRequests_Type()
)
ipxcpMaximumTerminateRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpMaximumTerminateRequests.setStatus("mandatory")
_IpxcpMaximumConfigRequests_Type = Integer32
_IpxcpMaximumConfigRequests_Object = MibTableColumn
ipxcpMaximumConfigRequests = _IpxcpMaximumConfigRequests_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 14),
    _IpxcpMaximumConfigRequests_Type()
)
ipxcpMaximumConfigRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpMaximumConfigRequests.setStatus("mandatory")
_IpxcpMaximumConfigNaks_Type = Integer32
_IpxcpMaximumConfigNaks_Object = MibTableColumn
ipxcpMaximumConfigNaks = _IpxcpMaximumConfigNaks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 15),
    _IpxcpMaximumConfigNaks_Type()
)
ipxcpMaximumConfigNaks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpMaximumConfigNaks.setStatus("mandatory")
_IpxcpNodeNumber_Type = MacAddress
_IpxcpNodeNumber_Object = MibTableColumn
ipxcpNodeNumber = _IpxcpNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 4, 1, 16),
    _IpxcpNodeNumber_Type()
)
ipxcpNodeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxcpNodeNumber.setStatus("mandatory")
_PppExtConfigTable_Object = MibTable
pppExtConfigTable = _PppExtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5)
)
if mibBuilder.loadTexts:
    pppExtConfigTable.setStatus("mandatory")
_PppExtConfigTableEntry_Object = MibTableRow
pppExtConfigTableEntry = _PppExtConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5, 1)
)
pppExtConfigTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppExtConfigTableEntry.setStatus("mandatory")


class _PppExtLinkAuthentication_Type(Integer32):
    """Custom type pppExtLinkAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PppExtLinkAuthentication_Type.__name__ = "Integer32"
_PppExtLinkAuthentication_Object = MibTableColumn
pppExtLinkAuthentication = _PppExtLinkAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5, 1, 1),
    _PppExtLinkAuthentication_Type()
)
pppExtLinkAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtLinkAuthentication.setStatus("mandatory")


class _PppExtEnableIp_Type(Integer32):
    """Custom type pppExtEnableIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PppExtEnableIp_Type.__name__ = "Integer32"
_PppExtEnableIp_Object = MibTableColumn
pppExtEnableIp = _PppExtEnableIp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5, 1, 2),
    _PppExtEnableIp_Type()
)
pppExtEnableIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtEnableIp.setStatus("mandatory")


class _PppExtEnableIpx_Type(Integer32):
    """Custom type pppExtEnableIpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PppExtEnableIpx_Type.__name__ = "Integer32"
_PppExtEnableIpx_Object = MibTableColumn
pppExtEnableIpx = _PppExtEnableIpx_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5, 1, 3),
    _PppExtEnableIpx_Type()
)
pppExtEnableIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtEnableIpx.setStatus("mandatory")


class _PppExtHdlcLayer_Type(Integer32):
    """Custom type pppExtHdlcLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 2),
          ("synchronous", 1))
    )


_PppExtHdlcLayer_Type.__name__ = "Integer32"
_PppExtHdlcLayer_Object = MibTableColumn
pppExtHdlcLayer = _PppExtHdlcLayer_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 27, 5, 1, 4),
    _PppExtHdlcLayer_Type()
)
pppExtHdlcLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppExtHdlcLayer.setStatus("mandatory")
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28)
)
_IpFirewallStatusTable_Object = MibTable
ipFirewallStatusTable = _IpFirewallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 1)
)
if mibBuilder.loadTexts:
    ipFirewallStatusTable.setStatus("mandatory")
_IpFirewallStatusTableEntry_Object = MibTableRow
ipFirewallStatusTableEntry = _IpFirewallStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 1, 1)
)
ipFirewallStatusTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipFirewallStatusIndex"),
)
if mibBuilder.loadTexts:
    ipFirewallStatusTableEntry.setStatus("mandatory")


class _IpFirewallStatusIndex_Type(Integer32):
    """Custom type ipFirewallStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpFirewallStatusIndex_Type.__name__ = "Integer32"
_IpFirewallStatusIndex_Object = MibTableColumn
ipFirewallStatusIndex = _IpFirewallStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 1, 1, 1),
    _IpFirewallStatusIndex_Type()
)
ipFirewallStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFirewallStatusIndex.setStatus("mandatory")
_IpFirewallFilteredPackets_Type = Counter32
_IpFirewallFilteredPackets_Object = MibTableColumn
ipFirewallFilteredPackets = _IpFirewallFilteredPackets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 1, 1, 2),
    _IpFirewallFilteredPackets_Type()
)
ipFirewallFilteredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFirewallFilteredPackets.setStatus("mandatory")
_IpFirewallConfigTable_Object = MibTable
ipFirewallConfigTable = _IpFirewallConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2)
)
if mibBuilder.loadTexts:
    ipFirewallConfigTable.setStatus("mandatory")
_IpFirewallConfigTableEntry_Object = MibTableRow
ipFirewallConfigTableEntry = _IpFirewallConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1)
)
ipFirewallConfigTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipFirewallConfigIndex"),
)
if mibBuilder.loadTexts:
    ipFirewallConfigTableEntry.setStatus("mandatory")


class _IpFirewallConfigIndex_Type(Integer32):
    """Custom type ipFirewallConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpFirewallConfigIndex_Type.__name__ = "Integer32"
_IpFirewallConfigIndex_Object = MibTableColumn
ipFirewallConfigIndex = _IpFirewallConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 1),
    _IpFirewallConfigIndex_Type()
)
ipFirewallConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFirewallConfigIndex.setStatus("mandatory")
_IpFirewallSourceAddress_Type = IpAddress
_IpFirewallSourceAddress_Object = MibTableColumn
ipFirewallSourceAddress = _IpFirewallSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 2),
    _IpFirewallSourceAddress_Type()
)
ipFirewallSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallSourceAddress.setStatus("mandatory")
_IpFirewallSourceMask_Type = IpAddress
_IpFirewallSourceMask_Object = MibTableColumn
ipFirewallSourceMask = _IpFirewallSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 3),
    _IpFirewallSourceMask_Type()
)
ipFirewallSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallSourceMask.setStatus("mandatory")
_IpFirewallLowerSourcePort_Type = Integer32
_IpFirewallLowerSourcePort_Object = MibTableColumn
ipFirewallLowerSourcePort = _IpFirewallLowerSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 4),
    _IpFirewallLowerSourcePort_Type()
)
ipFirewallLowerSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallLowerSourcePort.setStatus("mandatory")
_IpFirewallHigherSourcePort_Type = Integer32
_IpFirewallHigherSourcePort_Object = MibTableColumn
ipFirewallHigherSourcePort = _IpFirewallHigherSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 5),
    _IpFirewallHigherSourcePort_Type()
)
ipFirewallHigherSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallHigherSourcePort.setStatus("mandatory")
_IpFirewallDestinationAddress_Type = IpAddress
_IpFirewallDestinationAddress_Object = MibTableColumn
ipFirewallDestinationAddress = _IpFirewallDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 6),
    _IpFirewallDestinationAddress_Type()
)
ipFirewallDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallDestinationAddress.setStatus("mandatory")
_IpFirewallDestinationMask_Type = IpAddress
_IpFirewallDestinationMask_Object = MibTableColumn
ipFirewallDestinationMask = _IpFirewallDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 7),
    _IpFirewallDestinationMask_Type()
)
ipFirewallDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallDestinationMask.setStatus("mandatory")
_IpFirewallLowerDestinationPort_Type = Integer32
_IpFirewallLowerDestinationPort_Object = MibTableColumn
ipFirewallLowerDestinationPort = _IpFirewallLowerDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 8),
    _IpFirewallLowerDestinationPort_Type()
)
ipFirewallLowerDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallLowerDestinationPort.setStatus("mandatory")
_IpFirewallHigherDestinationPort_Type = Integer32
_IpFirewallHigherDestinationPort_Object = MibTableColumn
ipFirewallHigherDestinationPort = _IpFirewallHigherDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 9),
    _IpFirewallHigherDestinationPort_Type()
)
ipFirewallHigherDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallHigherDestinationPort.setStatus("mandatory")
_IpFirewallRouterName_Type = DisplayString
_IpFirewallRouterName_Object = MibTableColumn
ipFirewallRouterName = _IpFirewallRouterName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 10),
    _IpFirewallRouterName_Type()
)
ipFirewallRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallRouterName.setStatus("mandatory")


class _IpFirewallMode_Type(Integer32):
    """Custom type ipFirewallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("append", 3),
          ("delete", 1),
          ("edit", 4),
          ("insert", 2))
    )


_IpFirewallMode_Type.__name__ = "Integer32"
_IpFirewallMode_Object = MibTableColumn
ipFirewallMode = _IpFirewallMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 11),
    _IpFirewallMode_Type()
)
ipFirewallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallMode.setStatus("mandatory")


class _IpFirewallType_Type(Integer32):
    """Custom type ipFirewallType based on Integer32"""
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
        *(("all", 2),
          ("icmp", 5),
          ("none", 1),
          ("tcp", 3),
          ("udp", 4))
    )


_IpFirewallType_Type.__name__ = "Integer32"
_IpFirewallType_Object = MibTableColumn
ipFirewallType = _IpFirewallType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 12),
    _IpFirewallType_Type()
)
ipFirewallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallType.setStatus("mandatory")


class _IpFirewallAction_Type(Integer32):
    """Custom type ipFirewallAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_IpFirewallAction_Type.__name__ = "Integer32"
_IpFirewallAction_Object = MibTableColumn
ipFirewallAction = _IpFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 13),
    _IpFirewallAction_Type()
)
ipFirewallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallAction.setStatus("mandatory")


class _IpFirewallBidir_Type(Integer32):
    """Custom type ipFirewallBidir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpFirewallBidir_Type.__name__ = "Integer32"
_IpFirewallBidir_Object = MibTableColumn
ipFirewallBidir = _IpFirewallBidir_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 14),
    _IpFirewallBidir_Type()
)
ipFirewallBidir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallBidir.setStatus("mandatory")


class _IpFirewallTcpsyn_Type(Integer32):
    """Custom type ipFirewallTcpsyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpFirewallTcpsyn_Type.__name__ = "Integer32"
_IpFirewallTcpsyn_Object = MibTableColumn
ipFirewallTcpsyn = _IpFirewallTcpsyn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 2, 1, 15),
    _IpFirewallTcpsyn_Type()
)
ipFirewallTcpsyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipFirewallTcpsyn.setStatus("mandatory")
_IpxFirewallStatusTable_Object = MibTable
ipxFirewallStatusTable = _IpxFirewallStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 3)
)
if mibBuilder.loadTexts:
    ipxFirewallStatusTable.setStatus("mandatory")
_IpxFirewallStatusTableEntry_Object = MibTableRow
ipxFirewallStatusTableEntry = _IpxFirewallStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 3, 1)
)
ipxFirewallStatusTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipxFirewallStatusIndex"),
)
if mibBuilder.loadTexts:
    ipxFirewallStatusTableEntry.setStatus("mandatory")


class _IpxFirewallStatusIndex_Type(Integer32):
    """Custom type ipxFirewallStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpxFirewallStatusIndex_Type.__name__ = "Integer32"
_IpxFirewallStatusIndex_Object = MibTableColumn
ipxFirewallStatusIndex = _IpxFirewallStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 3, 1, 1),
    _IpxFirewallStatusIndex_Type()
)
ipxFirewallStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxFirewallStatusIndex.setStatus("mandatory")
_IpxFirewallFilteredPackets_Type = Counter32
_IpxFirewallFilteredPackets_Object = MibTableColumn
ipxFirewallFilteredPackets = _IpxFirewallFilteredPackets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 3, 1, 2),
    _IpxFirewallFilteredPackets_Type()
)
ipxFirewallFilteredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxFirewallFilteredPackets.setStatus("mandatory")
_IpxFirewallConfigTable_Object = MibTable
ipxFirewallConfigTable = _IpxFirewallConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4)
)
if mibBuilder.loadTexts:
    ipxFirewallConfigTable.setStatus("mandatory")
_IpxFirewallConfigTableEntry_Object = MibTableRow
ipxFirewallConfigTableEntry = _IpxFirewallConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1)
)
ipxFirewallConfigTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "ipxFirewallConfigIndex"),
)
if mibBuilder.loadTexts:
    ipxFirewallConfigTableEntry.setStatus("mandatory")


class _IpxFirewallConfigIndex_Type(Integer32):
    """Custom type ipxFirewallConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpxFirewallConfigIndex_Type.__name__ = "Integer32"
_IpxFirewallConfigIndex_Object = MibTableColumn
ipxFirewallConfigIndex = _IpxFirewallConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 1),
    _IpxFirewallConfigIndex_Type()
)
ipxFirewallConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxFirewallConfigIndex.setStatus("mandatory")


class _IpxFirewallLowerSourceNetwork_Type(OctetString):
    """Custom type ipxFirewallLowerSourceNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxFirewallLowerSourceNetwork_Type.__name__ = "OctetString"
_IpxFirewallLowerSourceNetwork_Object = MibTableColumn
ipxFirewallLowerSourceNetwork = _IpxFirewallLowerSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 2),
    _IpxFirewallLowerSourceNetwork_Type()
)
ipxFirewallLowerSourceNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerSourceNetwork.setStatus("mandatory")


class _IpxFirewallHigherSourceNetwork_Type(OctetString):
    """Custom type ipxFirewallHigherSourceNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxFirewallHigherSourceNetwork_Type.__name__ = "OctetString"
_IpxFirewallHigherSourceNetwork_Object = MibTableColumn
ipxFirewallHigherSourceNetwork = _IpxFirewallHigherSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 3),
    _IpxFirewallHigherSourceNetwork_Type()
)
ipxFirewallHigherSourceNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherSourceNetwork.setStatus("mandatory")
_IpxFirewallLowerSourceNode_Type = MacAddress
_IpxFirewallLowerSourceNode_Object = MibTableColumn
ipxFirewallLowerSourceNode = _IpxFirewallLowerSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 4),
    _IpxFirewallLowerSourceNode_Type()
)
ipxFirewallLowerSourceNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerSourceNode.setStatus("mandatory")
_IpxFirewallHigherSourceNode_Type = MacAddress
_IpxFirewallHigherSourceNode_Object = MibTableColumn
ipxFirewallHigherSourceNode = _IpxFirewallHigherSourceNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 5),
    _IpxFirewallHigherSourceNode_Type()
)
ipxFirewallHigherSourceNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherSourceNode.setStatus("mandatory")


class _IpxFirewallLowerSourceSocket_Type(OctetString):
    """Custom type ipxFirewallLowerSourceSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxFirewallLowerSourceSocket_Type.__name__ = "OctetString"
_IpxFirewallLowerSourceSocket_Object = MibTableColumn
ipxFirewallLowerSourceSocket = _IpxFirewallLowerSourceSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 6),
    _IpxFirewallLowerSourceSocket_Type()
)
ipxFirewallLowerSourceSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerSourceSocket.setStatus("mandatory")


class _IpxFirewallHigherSourceSocket_Type(OctetString):
    """Custom type ipxFirewallHigherSourceSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxFirewallHigherSourceSocket_Type.__name__ = "OctetString"
_IpxFirewallHigherSourceSocket_Object = MibTableColumn
ipxFirewallHigherSourceSocket = _IpxFirewallHigherSourceSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 7),
    _IpxFirewallHigherSourceSocket_Type()
)
ipxFirewallHigherSourceSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherSourceSocket.setStatus("mandatory")


class _IpxFirewallLowerDestinationNetwork_Type(OctetString):
    """Custom type ipxFirewallLowerDestinationNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxFirewallLowerDestinationNetwork_Type.__name__ = "OctetString"
_IpxFirewallLowerDestinationNetwork_Object = MibTableColumn
ipxFirewallLowerDestinationNetwork = _IpxFirewallLowerDestinationNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 8),
    _IpxFirewallLowerDestinationNetwork_Type()
)
ipxFirewallLowerDestinationNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerDestinationNetwork.setStatus("mandatory")


class _IpxFirewallHigherDestinationNetwork_Type(OctetString):
    """Custom type ipxFirewallHigherDestinationNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxFirewallHigherDestinationNetwork_Type.__name__ = "OctetString"
_IpxFirewallHigherDestinationNetwork_Object = MibTableColumn
ipxFirewallHigherDestinationNetwork = _IpxFirewallHigherDestinationNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 9),
    _IpxFirewallHigherDestinationNetwork_Type()
)
ipxFirewallHigherDestinationNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherDestinationNetwork.setStatus("mandatory")
_IpxFirewallLowerDestinationNode_Type = MacAddress
_IpxFirewallLowerDestinationNode_Object = MibTableColumn
ipxFirewallLowerDestinationNode = _IpxFirewallLowerDestinationNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 10),
    _IpxFirewallLowerDestinationNode_Type()
)
ipxFirewallLowerDestinationNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerDestinationNode.setStatus("mandatory")
_IpxFirewallHigherDestinationNode_Type = MacAddress
_IpxFirewallHigherDestinationNode_Object = MibTableColumn
ipxFirewallHigherDestinationNode = _IpxFirewallHigherDestinationNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 11),
    _IpxFirewallHigherDestinationNode_Type()
)
ipxFirewallHigherDestinationNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherDestinationNode.setStatus("mandatory")


class _IpxFirewallLowerDestinationSocket_Type(OctetString):
    """Custom type ipxFirewallLowerDestinationSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxFirewallLowerDestinationSocket_Type.__name__ = "OctetString"
_IpxFirewallLowerDestinationSocket_Object = MibTableColumn
ipxFirewallLowerDestinationSocket = _IpxFirewallLowerDestinationSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 12),
    _IpxFirewallLowerDestinationSocket_Type()
)
ipxFirewallLowerDestinationSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallLowerDestinationSocket.setStatus("mandatory")


class _IpxFirewallHigherDestinationSocket_Type(OctetString):
    """Custom type ipxFirewallHigherDestinationSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxFirewallHigherDestinationSocket_Type.__name__ = "OctetString"
_IpxFirewallHigherDestinationSocket_Object = MibTableColumn
ipxFirewallHigherDestinationSocket = _IpxFirewallHigherDestinationSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 13),
    _IpxFirewallHigherDestinationSocket_Type()
)
ipxFirewallHigherDestinationSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallHigherDestinationSocket.setStatus("mandatory")
_IpxFirewallRouterName_Type = DisplayString
_IpxFirewallRouterName_Object = MibTableColumn
ipxFirewallRouterName = _IpxFirewallRouterName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 14),
    _IpxFirewallRouterName_Type()
)
ipxFirewallRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallRouterName.setStatus("mandatory")


class _IpxFirewallMode_Type(Integer32):
    """Custom type ipxFirewallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("append", 3),
          ("delete", 1),
          ("edit", 4),
          ("insert", 2))
    )


_IpxFirewallMode_Type.__name__ = "Integer32"
_IpxFirewallMode_Object = MibTableColumn
ipxFirewallMode = _IpxFirewallMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 15),
    _IpxFirewallMode_Type()
)
ipxFirewallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallMode.setStatus("mandatory")


class _IpxFirewallAction_Type(Integer32):
    """Custom type ipxFirewallAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_IpxFirewallAction_Type.__name__ = "Integer32"
_IpxFirewallAction_Object = MibTableColumn
ipxFirewallAction = _IpxFirewallAction_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 16),
    _IpxFirewallAction_Type()
)
ipxFirewallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallAction.setStatus("mandatory")


class _IpxFirewallBidir_Type(Integer32):
    """Custom type ipxFirewallBidir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IpxFirewallBidir_Type.__name__ = "Integer32"
_IpxFirewallBidir_Object = MibTableColumn
ipxFirewallBidir = _IpxFirewallBidir_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 28, 4, 1, 17),
    _IpxFirewallBidir_Type()
)
ipxFirewallBidir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxFirewallBidir.setStatus("mandatory")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29)
)
_UsercfgTable_Object = MibTable
usercfgTable = _UsercfgTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    usercfgTable.setStatus("mandatory")
_UsercfgEntry_Object = MibTableRow
usercfgEntry = _UsercfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1)
)
usercfgEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "usercfgIndex"),
)
if mibBuilder.loadTexts:
    usercfgEntry.setStatus("mandatory")


class _UsercfgIndex_Type(Integer32):
    """Custom type usercfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsercfgIndex_Type.__name__ = "Integer32"
_UsercfgIndex_Object = MibTableColumn
usercfgIndex = _UsercfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1, 1),
    _UsercfgIndex_Type()
)
usercfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usercfgIndex.setStatus("mandatory")


class _UsercfgName_Type(DisplayString):
    """Custom type usercfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsercfgName_Type.__name__ = "DisplayString"
_UsercfgName_Object = MibTableColumn
usercfgName = _UsercfgName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1, 2),
    _UsercfgName_Type()
)
usercfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usercfgName.setStatus("mandatory")
_UsercfgMac_Type = MacAddress
_UsercfgMac_Object = MibTableColumn
usercfgMac = _UsercfgMac_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1, 3),
    _UsercfgMac_Type()
)
usercfgMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usercfgMac.setStatus("mandatory")


class _UsercfgAllowed_Type(Integer32):
    """Custom type usercfgAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_UsercfgAllowed_Type.__name__ = "Integer32"
_UsercfgAllowed_Object = MibTableColumn
usercfgAllowed = _UsercfgAllowed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1, 4),
    _UsercfgAllowed_Type()
)
usercfgAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usercfgAllowed.setStatus("mandatory")


class _UsercfgMode_Type(Integer32):
    """Custom type usercfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_UsercfgMode_Type.__name__ = "Integer32"
_UsercfgMode_Object = MibTableColumn
usercfgMode = _UsercfgMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 29, 1, 1, 5),
    _UsercfgMode_Type()
)
usercfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usercfgMode.setStatus("mandatory")


class _SrcEnabled_Type(Integer32):
    """Custom type srcEnabled based on Integer32"""
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


_SrcEnabled_Type.__name__ = "Integer32"
_SrcEnabled_Object = MibScalar
srcEnabled = _SrcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 30),
    _SrcEnabled_Type()
)
srcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcEnabled.setStatus("mandatory")


class _SrcPriority_Type(Integer32):
    """Custom type srcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              128,
              200)
        )
    )
    namedValues = NamedValues(
        *(("primary", 50),
          ("secondary", 128),
          ("slave", 200))
    )


_SrcPriority_Type.__name__ = "Integer32"
_SrcPriority_Object = MibScalar
srcPriority = _SrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 31),
    _SrcPriority_Type()
)
srcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcPriority.setStatus("mandatory")
_Ipnat_ObjectIdentity = ObjectIdentity
ipnat = _Ipnat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32)
)


class _IpNatTranslate_Type(Integer32):
    """Custom type ipNatTranslate based on Integer32"""
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


_IpNatTranslate_Type.__name__ = "Integer32"
_IpNatTranslate_Object = MibScalar
ipNatTranslate = _IpNatTranslate_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 1),
    _IpNatTranslate_Type()
)
ipNatTranslate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatTranslate.setStatus("mandatory")
_IpNatIpAddress_Type = IpAddress
_IpNatIpAddress_Object = MibScalar
ipNatIpAddress = _IpNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 2),
    _IpNatIpAddress_Type()
)
ipNatIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatIpAddress.setStatus("mandatory")
_IpNatBogusNetwork_Type = IpAddress
_IpNatBogusNetwork_Object = MibScalar
ipNatBogusNetwork = _IpNatBogusNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 3),
    _IpNatBogusNetwork_Type()
)
ipNatBogusNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatBogusNetwork.setStatus("mandatory")
_IpNatBogusNetmask_Type = IpAddress
_IpNatBogusNetmask_Object = MibScalar
ipNatBogusNetmask = _IpNatBogusNetmask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 4),
    _IpNatBogusNetmask_Type()
)
ipNatBogusNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatBogusNetmask.setStatus("mandatory")
_IpNatTcpFinTimeout_Type = Integer32
_IpNatTcpFinTimeout_Object = MibScalar
ipNatTcpFinTimeout = _IpNatTcpFinTimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 5),
    _IpNatTcpFinTimeout_Type()
)
ipNatTcpFinTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatTcpFinTimeout.setStatus("mandatory")
_IpNatTcpInactiveTimeout_Type = Integer32
_IpNatTcpInactiveTimeout_Object = MibScalar
ipNatTcpInactiveTimeout = _IpNatTcpInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 6),
    _IpNatTcpInactiveTimeout_Type()
)
ipNatTcpInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatTcpInactiveTimeout.setStatus("mandatory")
_IpNatUdpTimeout_Type = Integer32
_IpNatUdpTimeout_Object = MibScalar
ipNatUdpTimeout = _IpNatUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 7),
    _IpNatUdpTimeout_Type()
)
ipNatUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatUdpTimeout.setStatus("mandatory")


class _IpNatMyself_Type(Integer32):
    """Custom type ipNatMyself based on Integer32"""
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


_IpNatMyself_Type.__name__ = "Integer32"
_IpNatMyself_Object = MibScalar
ipNatMyself = _IpNatMyself_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 32, 8),
    _IpNatMyself_Type()
)
ipNatMyself.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatMyself.setStatus("mandatory")
_Dhcpserver_ObjectIdentity = ObjectIdentity
dhcpserver = _Dhcpserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33)
)


class _DhcpAutoStatus_Type(Integer32):
    """Custom type dhcpAutoStatus based on Integer32"""
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


_DhcpAutoStatus_Type.__name__ = "Integer32"
_DhcpAutoStatus_Object = MibScalar
dhcpAutoStatus = _DhcpAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 1),
    _DhcpAutoStatus_Type()
)
dhcpAutoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoStatus.setStatus("mandatory")


class _DhcpAutoName_Type(DisplayString):
    """Custom type dhcpAutoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DhcpAutoName_Type.__name__ = "DisplayString"
_DhcpAutoName_Object = MibScalar
dhcpAutoName = _DhcpAutoName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 2),
    _DhcpAutoName_Type()
)
dhcpAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoName.setStatus("mandatory")


class _DhcpAutoDomain_Type(DisplayString):
    """Custom type dhcpAutoDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_DhcpAutoDomain_Type.__name__ = "DisplayString"
_DhcpAutoDomain_Object = MibScalar
dhcpAutoDomain = _DhcpAutoDomain_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 3),
    _DhcpAutoDomain_Type()
)
dhcpAutoDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoDomain.setStatus("mandatory")
_DhcpAutoSeedStart_Type = IpAddress
_DhcpAutoSeedStart_Object = MibScalar
dhcpAutoSeedStart = _DhcpAutoSeedStart_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 4),
    _DhcpAutoSeedStart_Type()
)
dhcpAutoSeedStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoSeedStart.setStatus("mandatory")
_DhcpAutoSeedEnd_Type = IpAddress
_DhcpAutoSeedEnd_Object = MibScalar
dhcpAutoSeedEnd = _DhcpAutoSeedEnd_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 5),
    _DhcpAutoSeedEnd_Type()
)
dhcpAutoSeedEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoSeedEnd.setStatus("mandatory")
_DhcpAutoMask_Type = IpAddress
_DhcpAutoMask_Object = MibScalar
dhcpAutoMask = _DhcpAutoMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 6),
    _DhcpAutoMask_Type()
)
dhcpAutoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoMask.setStatus("mandatory")
_DhcpAutoRouter_Type = IpAddress
_DhcpAutoRouter_Object = MibScalar
dhcpAutoRouter = _DhcpAutoRouter_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 7),
    _DhcpAutoRouter_Type()
)
dhcpAutoRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoRouter.setStatus("mandatory")
_DhcpWINSTable_Object = MibTable
dhcpWINSTable = _DhcpWINSTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 8)
)
if mibBuilder.loadTexts:
    dhcpWINSTable.setStatus("mandatory")
_DhcpWINSEntry_Object = MibTableRow
dhcpWINSEntry = _DhcpWINSEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 8, 1)
)
dhcpWINSEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "dhcpWINSIndex"),
)
if mibBuilder.loadTexts:
    dhcpWINSEntry.setStatus("mandatory")
_DhcpWINSIndex_Type = Integer32
_DhcpWINSIndex_Object = MibTableColumn
dhcpWINSIndex = _DhcpWINSIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 8, 1, 1),
    _DhcpWINSIndex_Type()
)
dhcpWINSIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpWINSIndex.setStatus("mandatory")
_DhcpWINSAddr_Type = IpAddress
_DhcpWINSAddr_Object = MibTableColumn
dhcpWINSAddr = _DhcpWINSAddr_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 8, 1, 2),
    _DhcpWINSAddr_Type()
)
dhcpWINSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpWINSAddr.setStatus("mandatory")
_DhcpDNSTable_Object = MibTable
dhcpDNSTable = _DhcpDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 9)
)
if mibBuilder.loadTexts:
    dhcpDNSTable.setStatus("mandatory")
_DhcpDNSEntry_Object = MibTableRow
dhcpDNSEntry = _DhcpDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 9, 1)
)
dhcpDNSEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "dhcpDNSIndex"),
)
if mibBuilder.loadTexts:
    dhcpDNSEntry.setStatus("mandatory")
_DhcpDNSIndex_Type = Integer32
_DhcpDNSIndex_Object = MibTableColumn
dhcpDNSIndex = _DhcpDNSIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 9, 1, 1),
    _DhcpDNSIndex_Type()
)
dhcpDNSIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDNSIndex.setStatus("mandatory")
_DhcpDNSAddr_Type = IpAddress
_DhcpDNSAddr_Object = MibTableColumn
dhcpDNSAddr = _DhcpDNSAddr_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 9, 1, 2),
    _DhcpDNSAddr_Type()
)
dhcpDNSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpDNSAddr.setStatus("mandatory")
_DhcpAutoLease_Type = Integer32
_DhcpAutoLease_Object = MibScalar
dhcpAutoLease = _DhcpAutoLease_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 10),
    _DhcpAutoLease_Type()
)
dhcpAutoLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpAutoLease.setStatus("mandatory")
_DhcpAstatTable_Object = MibTable
dhcpAstatTable = _DhcpAstatTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11)
)
if mibBuilder.loadTexts:
    dhcpAstatTable.setStatus("mandatory")
_DhcpAstatEntry_Object = MibTableRow
dhcpAstatEntry = _DhcpAstatEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1)
)
dhcpAstatEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "dhcpAstatIpAddr"),
)
if mibBuilder.loadTexts:
    dhcpAstatEntry.setStatus("mandatory")
_DhcpAstatIpAddr_Type = IpAddress
_DhcpAstatIpAddr_Object = MibTableColumn
dhcpAstatIpAddr = _DhcpAstatIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1, 1),
    _DhcpAstatIpAddr_Type()
)
dhcpAstatIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAstatIpAddr.setStatus("mandatory")


class _DhcpAstatIf_Type(Integer32):
    """Custom type dhcpAstatIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("unused", 0))
    )


_DhcpAstatIf_Type.__name__ = "Integer32"
_DhcpAstatIf_Object = MibTableColumn
dhcpAstatIf = _DhcpAstatIf_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1, 2),
    _DhcpAstatIf_Type()
)
dhcpAstatIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAstatIf.setStatus("mandatory")
_DhcpAstatHwAddr_Type = MacAddress
_DhcpAstatHwAddr_Object = MibTableColumn
dhcpAstatHwAddr = _DhcpAstatHwAddr_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1, 3),
    _DhcpAstatHwAddr_Type()
)
dhcpAstatHwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAstatHwAddr.setStatus("mandatory")
_DhcpAstatCID_Type = OctetString
_DhcpAstatCID_Object = MibTableColumn
dhcpAstatCID = _DhcpAstatCID_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1, 4),
    _DhcpAstatCID_Type()
)
dhcpAstatCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAstatCID.setStatus("mandatory")
_DhcpAstatLife_Type = Integer32
_DhcpAstatLife_Object = MibTableColumn
dhcpAstatLife = _DhcpAstatLife_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 33, 11, 1, 5),
    _DhcpAstatLife_Type()
)
dhcpAstatLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpAstatLife.setStatus("mandatory")
_PppAuthTable_Object = MibTable
pppAuthTable = _PppAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34)
)
if mibBuilder.loadTexts:
    pppAuthTable.setStatus("mandatory")
_PppAuthTableEntry_Object = MibTableRow
pppAuthTableEntry = _PppAuthTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1)
)
pppAuthTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "pppAuthIndex"),
)
if mibBuilder.loadTexts:
    pppAuthTableEntry.setStatus("mandatory")
_PppAuthIndex_Type = Integer32
_PppAuthIndex_Object = MibTableColumn
pppAuthIndex = _PppAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 1),
    _PppAuthIndex_Type()
)
pppAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppAuthIndex.setStatus("mandatory")


class _PppAuthName_Type(DisplayString):
    """Custom type pppAuthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PppAuthName_Type.__name__ = "DisplayString"
_PppAuthName_Object = MibTableColumn
pppAuthName = _PppAuthName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 2),
    _PppAuthName_Type()
)
pppAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthName.setStatus("mandatory")


class _PppAuthClass_Type(Integer32):
    """Custom type pppAuthClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_PppAuthClass_Type.__name__ = "Integer32"
_PppAuthClass_Object = MibTableColumn
pppAuthClass = _PppAuthClass_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 3),
    _PppAuthClass_Type()
)
pppAuthClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthClass.setStatus("mandatory")


class _PppAuthLocalId_Type(DisplayString):
    """Custom type pppAuthLocalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_PppAuthLocalId_Type.__name__ = "DisplayString"
_PppAuthLocalId_Object = MibTableColumn
pppAuthLocalId = _PppAuthLocalId_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 4),
    _PppAuthLocalId_Type()
)
pppAuthLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthLocalId.setStatus("mandatory")


class _PppAuthLocalPw_Type(DisplayString):
    """Custom type pppAuthLocalPw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PppAuthLocalPw_Type.__name__ = "DisplayString"
_PppAuthLocalPw_Object = MibTableColumn
pppAuthLocalPw = _PppAuthLocalPw_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 5),
    _PppAuthLocalPw_Type()
)
pppAuthLocalPw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthLocalPw.setStatus("mandatory")


class _PppAuthRemoteId_Type(DisplayString):
    """Custom type pppAuthRemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_PppAuthRemoteId_Type.__name__ = "DisplayString"
_PppAuthRemoteId_Object = MibTableColumn
pppAuthRemoteId = _PppAuthRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 6),
    _PppAuthRemoteId_Type()
)
pppAuthRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthRemoteId.setStatus("mandatory")


class _PppAuthRemotePw_Type(DisplayString):
    """Custom type pppAuthRemotePw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PppAuthRemotePw_Type.__name__ = "DisplayString"
_PppAuthRemotePw_Object = MibTableColumn
pppAuthRemotePw = _PppAuthRemotePw_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 7),
    _PppAuthRemotePw_Type()
)
pppAuthRemotePw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthRemotePw.setStatus("mandatory")


class _PppAuthRetryPeriod_Type(Integer32):
    """Custom type pppAuthRetryPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PppAuthRetryPeriod_Type.__name__ = "Integer32"
_PppAuthRetryPeriod_Object = MibTableColumn
pppAuthRetryPeriod = _PppAuthRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 8),
    _PppAuthRetryPeriod_Type()
)
pppAuthRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthRetryPeriod.setStatus("mandatory")


class _PppAuthRenegPeriod_Type(Integer32):
    """Custom type pppAuthRenegPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_PppAuthRenegPeriod_Type.__name__ = "Integer32"
_PppAuthRenegPeriod_Object = MibTableColumn
pppAuthRenegPeriod = _PppAuthRenegPeriod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 9),
    _PppAuthRenegPeriod_Type()
)
pppAuthRenegPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthRenegPeriod.setStatus("mandatory")


class _PppAuthRetryCount_Type(Integer32):
    """Custom type pppAuthRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_PppAuthRetryCount_Type.__name__ = "Integer32"
_PppAuthRetryCount_Object = MibTableColumn
pppAuthRetryCount = _PppAuthRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 10),
    _PppAuthRetryCount_Type()
)
pppAuthRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthRetryCount.setStatus("mandatory")


class _PppAuthMode_Type(Integer32):
    """Custom type pppAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_PppAuthMode_Type.__name__ = "Integer32"
_PppAuthMode_Object = MibTableColumn
pppAuthMode = _PppAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 34, 1, 11),
    _PppAuthMode_Type()
)
pppAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppAuthMode.setStatus("mandatory")
_Dnsproxy_ObjectIdentity = ObjectIdentity
dnsproxy = _Dnsproxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35)
)
_PrimaryDNSAddress_Type = IpAddress
_PrimaryDNSAddress_Object = MibScalar
primaryDNSAddress = _PrimaryDNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 1),
    _PrimaryDNSAddress_Type()
)
primaryDNSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryDNSAddress.setStatus("mandatory")
_SecondaryDNSAddress_Type = IpAddress
_SecondaryDNSAddress_Object = MibScalar
secondaryDNSAddress = _SecondaryDNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 2),
    _SecondaryDNSAddress_Type()
)
secondaryDNSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryDNSAddress.setStatus("mandatory")
_PrimaryNBNSAddress_Type = IpAddress
_PrimaryNBNSAddress_Object = MibScalar
primaryNBNSAddress = _PrimaryNBNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 3),
    _PrimaryNBNSAddress_Type()
)
primaryNBNSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryNBNSAddress.setStatus("mandatory")
_SecondaryNBNSAddress_Type = IpAddress
_SecondaryNBNSAddress_Object = MibScalar
secondaryNBNSAddress = _SecondaryNBNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 4),
    _SecondaryNBNSAddress_Type()
)
secondaryNBNSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryNBNSAddress.setStatus("mandatory")


class _DnsProxyActive_Type(Integer32):
    """Custom type dnsProxyActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DnsProxyActive_Type.__name__ = "Integer32"
_DnsProxyActive_Object = MibScalar
dnsProxyActive = _DnsProxyActive_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 5),
    _DnsProxyActive_Type()
)
dnsProxyActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProxyActive.setStatus("mandatory")


class _DnsCacheSize_Type(Integer32):
    """Custom type dnsCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_DnsCacheSize_Type.__name__ = "Integer32"
_DnsCacheSize_Object = MibScalar
dnsCacheSize = _DnsCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 6),
    _DnsCacheSize_Type()
)
dnsCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsCacheSize.setStatus("mandatory")
_DnsMaxServerTimeout_Type = Integer32
_DnsMaxServerTimeout_Object = MibScalar
dnsMaxServerTimeout = _DnsMaxServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 7),
    _DnsMaxServerTimeout_Type()
)
dnsMaxServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsMaxServerTimeout.setStatus("mandatory")
_DnsServerRetries_Type = Integer32
_DnsServerRetries_Object = MibScalar
dnsServerRetries = _DnsServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 8),
    _DnsServerRetries_Type()
)
dnsServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServerRetries.setStatus("mandatory")
_DnsDomainTable_Object = MibTable
dnsDomainTable = _DnsDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9)
)
if mibBuilder.loadTexts:
    dnsDomainTable.setStatus("mandatory")
_DnsDomainTableEntry_Object = MibTableRow
dnsDomainTableEntry = _DnsDomainTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1)
)
dnsDomainTableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "dnsDomainTableIndex"),
)
if mibBuilder.loadTexts:
    dnsDomainTableEntry.setStatus("mandatory")


class _DnsDomainTableIndex_Type(Integer32):
    """Custom type dnsDomainTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DnsDomainTableIndex_Type.__name__ = "Integer32"
_DnsDomainTableIndex_Object = MibTableColumn
dnsDomainTableIndex = _DnsDomainTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 1),
    _DnsDomainTableIndex_Type()
)
dnsDomainTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDomainTableIndex.setStatus("mandatory")


class _DnsDomainDomainName_Type(DisplayString):
    """Custom type dnsDomainDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DnsDomainDomainName_Type.__name__ = "DisplayString"
_DnsDomainDomainName_Object = MibTableColumn
dnsDomainDomainName = _DnsDomainDomainName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 2),
    _DnsDomainDomainName_Type()
)
dnsDomainDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainDomainName.setStatus("mandatory")


class _DnsDomainProfileIndex_Type(Integer32):
    """Custom type dnsDomainProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DnsDomainProfileIndex_Type.__name__ = "Integer32"
_DnsDomainProfileIndex_Object = MibTableColumn
dnsDomainProfileIndex = _DnsDomainProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 3),
    _DnsDomainProfileIndex_Type()
)
dnsDomainProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainProfileIndex.setStatus("mandatory")


class _DnsDomainRemoteServer_Type(DisplayString):
    """Custom type dnsDomainRemoteServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DnsDomainRemoteServer_Type.__name__ = "DisplayString"
_DnsDomainRemoteServer_Object = MibTableColumn
dnsDomainRemoteServer = _DnsDomainRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 4),
    _DnsDomainRemoteServer_Type()
)
dnsDomainRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainRemoteServer.setStatus("mandatory")
_DnsDomainPrimaryDNS_Type = IpAddress
_DnsDomainPrimaryDNS_Object = MibTableColumn
dnsDomainPrimaryDNS = _DnsDomainPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 5),
    _DnsDomainPrimaryDNS_Type()
)
dnsDomainPrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainPrimaryDNS.setStatus("mandatory")
_DnsDomainSecondaryDNS_Type = IpAddress
_DnsDomainSecondaryDNS_Object = MibTableColumn
dnsDomainSecondaryDNS = _DnsDomainSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 6),
    _DnsDomainSecondaryDNS_Type()
)
dnsDomainSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainSecondaryDNS.setStatus("mandatory")


class _DnsDomainMode_Type(Integer32):
    """Custom type dnsDomainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("append", 3),
          ("delete", 1),
          ("edit", 4),
          ("insert", 2))
    )


_DnsDomainMode_Type.__name__ = "Integer32"
_DnsDomainMode_Object = MibTableColumn
dnsDomainMode = _DnsDomainMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 9, 1, 7),
    _DnsDomainMode_Type()
)
dnsDomainMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainMode.setStatus("mandatory")
_DnsProfileTable_Object = MibTable
dnsProfileTable = _DnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10)
)
if mibBuilder.loadTexts:
    dnsProfileTable.setStatus("mandatory")
_DnsProfileEntry_Object = MibTableRow
dnsProfileEntry = _DnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1)
)
dnsProfileEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "dnsProfileIndex"),
)
if mibBuilder.loadTexts:
    dnsProfileEntry.setStatus("mandatory")


class _DnsProfileIndex_Type(Integer32):
    """Custom type dnsProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DnsProfileIndex_Type.__name__ = "Integer32"
_DnsProfileIndex_Object = MibTableColumn
dnsProfileIndex = _DnsProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 1),
    _DnsProfileIndex_Type()
)
dnsProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsProfileIndex.setStatus("mandatory")


class _DnsProfileName_Type(DisplayString):
    """Custom type dnsProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DnsProfileName_Type.__name__ = "DisplayString"
_DnsProfileName_Object = MibTableColumn
dnsProfileName = _DnsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 2),
    _DnsProfileName_Type()
)
dnsProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProfileName.setStatus("mandatory")


class _DnsProfileRemoteServer_Type(DisplayString):
    """Custom type dnsProfileRemoteServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DnsProfileRemoteServer_Type.__name__ = "DisplayString"
_DnsProfileRemoteServer_Object = MibTableColumn
dnsProfileRemoteServer = _DnsProfileRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 3),
    _DnsProfileRemoteServer_Type()
)
dnsProfileRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProfileRemoteServer.setStatus("mandatory")
_DnsProfilePrimaryDNS_Type = IpAddress
_DnsProfilePrimaryDNS_Object = MibTableColumn
dnsProfilePrimaryDNS = _DnsProfilePrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 4),
    _DnsProfilePrimaryDNS_Type()
)
dnsProfilePrimaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProfilePrimaryDNS.setStatus("mandatory")
_DnsProfileSecondaryDNS_Type = IpAddress
_DnsProfileSecondaryDNS_Object = MibTableColumn
dnsProfileSecondaryDNS = _DnsProfileSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 5),
    _DnsProfileSecondaryDNS_Type()
)
dnsProfileSecondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProfileSecondaryDNS.setStatus("mandatory")


class _DnsProfileMode_Type(Integer32):
    """Custom type dnsProfileMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 3),
          ("delete", 1),
          ("edit", 4))
    )


_DnsProfileMode_Type.__name__ = "Integer32"
_DnsProfileMode_Object = MibTableColumn
dnsProfileMode = _DnsProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 35, 10, 1, 6),
    _DnsProfileMode_Type()
)
dnsProfileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsProfileMode.setStatus("mandatory")
_Memoryusage_ObjectIdentity = ObjectIdentity
memoryusage = _Memoryusage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36)
)
_MemoryFree_Type = Integer32
_MemoryFree_Object = MibScalar
memoryFree = _MemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 1),
    _MemoryFree_Type()
)
memoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFree.setStatus("mandatory")
_MemoryTotal_Type = Integer32
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 2),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("mandatory")
_FragmentCount_Type = Integer32
_FragmentCount_Object = MibScalar
fragmentCount = _FragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 3),
    _FragmentCount_Type()
)
fragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentCount.setStatus("mandatory")
_FragmentLargest_Type = Integer32
_FragmentLargest_Object = MibScalar
fragmentLargest = _FragmentLargest_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 4),
    _FragmentLargest_Type()
)
fragmentLargest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fragmentLargest.setStatus("mandatory")
_Pool1size_Type = Integer32
_Pool1size_Object = MibScalar
pool1size = _Pool1size_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 5),
    _Pool1size_Type()
)
pool1size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pool1size.setStatus("mandatory")
_Pool2size_Type = Integer32
_Pool2size_Object = MibScalar
pool2size = _Pool2size_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 6),
    _Pool2size_Type()
)
pool2size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pool2size.setStatus("mandatory")
_Pool3size_Type = Integer32
_Pool3size_Object = MibScalar
pool3size = _Pool3size_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 7),
    _Pool3size_Type()
)
pool3size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pool3size.setStatus("mandatory")
_Pool4size_Type = Integer32
_Pool4size_Object = MibScalar
pool4size = _Pool4size_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 36, 8),
    _Pool4size_Type()
)
pool4size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pool4size.setStatus("mandatory")
_Traptable_Object = MibTable
traptable = _Traptable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37)
)
if mibBuilder.loadTexts:
    traptable.setStatus("mandatory")
_TraptableEntry_Object = MibTableRow
traptableEntry = _TraptableEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1)
)
traptableEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    traptableEntry.setStatus("mandatory")
_TrapIndex_Type = Integer32
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")
_TrapAddr_Type = IpAddress
_TrapAddr_Object = MibTableColumn
trapAddr = _TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 2),
    _TrapAddr_Type()
)
trapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAddr.setStatus("mandatory")
_TrapPort_Type = Integer32
_TrapPort_Object = MibTableColumn
trapPort = _TrapPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 3),
    _TrapPort_Type()
)
trapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapPort.setStatus("mandatory")


class _TrapLogFull_Type(Integer32):
    """Custom type trapLogFull based on Integer32"""
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


_TrapLogFull_Type.__name__ = "Integer32"
_TrapLogFull_Object = MibTableColumn
trapLogFull = _TrapLogFull_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 4),
    _TrapLogFull_Type()
)
trapLogFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLogFull.setStatus("mandatory")


class _TrapLogThreshold_Type(Integer32):
    """Custom type trapLogThreshold based on Integer32"""
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


_TrapLogThreshold_Type.__name__ = "Integer32"
_TrapLogThreshold_Object = MibTableColumn
trapLogThreshold = _TrapLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 5),
    _TrapLogThreshold_Type()
)
trapLogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLogThreshold.setStatus("mandatory")


class _TrapWarmStart_Type(Integer32):
    """Custom type trapWarmStart based on Integer32"""
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


_TrapWarmStart_Type.__name__ = "Integer32"
_TrapWarmStart_Object = MibTableColumn
trapWarmStart = _TrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 6),
    _TrapWarmStart_Type()
)
trapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapWarmStart.setStatus("mandatory")


class _TrapLinkDown_Type(Integer32):
    """Custom type trapLinkDown based on Integer32"""
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


_TrapLinkDown_Type.__name__ = "Integer32"
_TrapLinkDown_Object = MibTableColumn
trapLinkDown = _TrapLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 7),
    _TrapLinkDown_Type()
)
trapLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLinkDown.setStatus("mandatory")


class _TrapLinkUp_Type(Integer32):
    """Custom type trapLinkUp based on Integer32"""
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


_TrapLinkUp_Type.__name__ = "Integer32"
_TrapLinkUp_Object = MibTableColumn
trapLinkUp = _TrapLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 8),
    _TrapLinkUp_Type()
)
trapLinkUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLinkUp.setStatus("mandatory")


class _TrapVoiceDown_Type(Integer32):
    """Custom type trapVoiceDown based on Integer32"""
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


_TrapVoiceDown_Type.__name__ = "Integer32"
_TrapVoiceDown_Object = MibTableColumn
trapVoiceDown = _TrapVoiceDown_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 9),
    _TrapVoiceDown_Type()
)
trapVoiceDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVoiceDown.setStatus("mandatory")


class _TrapVoiceUp_Type(Integer32):
    """Custom type trapVoiceUp based on Integer32"""
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


_TrapVoiceUp_Type.__name__ = "Integer32"
_TrapVoiceUp_Object = MibTableColumn
trapVoiceUp = _TrapVoiceUp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 10),
    _TrapVoiceUp_Type()
)
trapVoiceUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVoiceUp.setStatus("mandatory")


class _TrapISDNDown_Type(Integer32):
    """Custom type trapISDNDown based on Integer32"""
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


_TrapISDNDown_Type.__name__ = "Integer32"
_TrapISDNDown_Object = MibTableColumn
trapISDNDown = _TrapISDNDown_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 11),
    _TrapISDNDown_Type()
)
trapISDNDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapISDNDown.setStatus("mandatory")


class _TrapISDNUp_Type(Integer32):
    """Custom type trapISDNUp based on Integer32"""
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


_TrapISDNUp_Type.__name__ = "Integer32"
_TrapISDNUp_Object = MibTableColumn
trapISDNUp = _TrapISDNUp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 12),
    _TrapISDNUp_Type()
)
trapISDNUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapISDNUp.setStatus("mandatory")


class _TrapAlarm_Type(Integer32):
    """Custom type trapAlarm based on Integer32"""
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


_TrapAlarm_Type.__name__ = "Integer32"
_TrapAlarm_Object = MibTableColumn
trapAlarm = _TrapAlarm_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 13),
    _TrapAlarm_Type()
)
trapAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAlarm.setStatus("mandatory")


class _TrapQ931Fail_Type(Integer32):
    """Custom type trapQ931Fail based on Integer32"""
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


_TrapQ931Fail_Type.__name__ = "Integer32"
_TrapQ931Fail_Object = MibTableColumn
trapQ931Fail = _TrapQ931Fail_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 14),
    _TrapQ931Fail_Type()
)
trapQ931Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapQ931Fail.setStatus("mandatory")


class _TrapDASS2Fail_Type(Integer32):
    """Custom type trapDASS2Fail based on Integer32"""
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


_TrapDASS2Fail_Type.__name__ = "Integer32"
_TrapDASS2Fail_Object = MibTableColumn
trapDASS2Fail = _TrapDASS2Fail_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 15),
    _TrapDASS2Fail_Type()
)
trapDASS2Fail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDASS2Fail.setStatus("mandatory")


class _TrapBriFail_Type(Integer32):
    """Custom type trapBriFail based on Integer32"""
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


_TrapBriFail_Type.__name__ = "Integer32"
_TrapBriFail_Object = MibTableColumn
trapBriFail = _TrapBriFail_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 16),
    _TrapBriFail_Type()
)
trapBriFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapBriFail.setStatus("mandatory")


class _TrapLoginAuth_Type(Integer32):
    """Custom type trapLoginAuth based on Integer32"""
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


_TrapLoginAuth_Type.__name__ = "Integer32"
_TrapLoginAuth_Object = MibTableColumn
trapLoginAuth = _TrapLoginAuth_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 37, 1, 17),
    _TrapLoginAuth_Type()
)
trapLoginAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapLoginAuth.setStatus("mandatory")
_PatTable_Object = MibTable
patTable = _PatTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38)
)
if mibBuilder.loadTexts:
    patTable.setStatus("mandatory")
_PatEntry_Object = MibTableRow
patEntry = _PatEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1)
)
patEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "patIndex"),
)
if mibBuilder.loadTexts:
    patEntry.setStatus("mandatory")


class _PatIndex_Type(Integer32):
    """Custom type patIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PatIndex_Type.__name__ = "Integer32"
_PatIndex_Object = MibTableColumn
patIndex = _PatIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1, 1),
    _PatIndex_Type()
)
patIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    patIndex.setStatus("mandatory")
_PatPort_Type = Integer32
_PatPort_Object = MibTableColumn
patPort = _PatPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1, 2),
    _PatPort_Type()
)
patPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patPort.setStatus("mandatory")
_PatInternalIP_Type = IpAddress
_PatInternalIP_Object = MibTableColumn
patInternalIP = _PatInternalIP_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1, 3),
    _PatInternalIP_Type()
)
patInternalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patInternalIP.setStatus("mandatory")
_PatInternalPort_Type = Integer32
_PatInternalPort_Object = MibTableColumn
patInternalPort = _PatInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1, 4),
    _PatInternalPort_Type()
)
patInternalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patInternalPort.setStatus("mandatory")


class _PatMode_Type(Integer32):
    """Custom type patMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_PatMode_Type.__name__ = "Integer32"
_PatMode_Object = MibTableColumn
patMode = _PatMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 38, 1, 5),
    _PatMode_Type()
)
patMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patMode.setStatus("mandatory")
_TpadLanPort_Type = Integer32
_TpadLanPort_Object = MibScalar
tpadLanPort = _TpadLanPort_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 1, 39),
    _TpadLanPort_Type()
)
tpadLanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpadLanPort.setStatus("mandatory")
_Ports_ObjectIdentity = ObjectIdentity
ports = _Ports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2)
)
_PortsTable_Object = MibTable
portsTable = _PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portsTable.setStatus("mandatory")
_PortsEntry_Object = MibTableRow
portsEntry = _PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1)
)
portsEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portsIndex"),
)
if mibBuilder.loadTexts:
    portsEntry.setStatus("mandatory")
_PortsIndex_Type = Integer32
_PortsIndex_Object = MibTableColumn
portsIndex = _PortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 1),
    _PortsIndex_Type()
)
portsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsIndex.setStatus("mandatory")
_PortsName_Type = DisplayString
_PortsName_Object = MibTableColumn
portsName = _PortsName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 2),
    _PortsName_Type()
)
portsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsName.setStatus("mandatory")


class _PortsType_Type(Integer32):
    """Custom type portsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("ethernet", 5),
          ("hdlc", 3),
          ("none", 0),
          ("ppp", 4),
          ("repeater", 7),
          ("slip", 9),
          ("slipMMIauto", 10),
          ("ta", 6),
          ("tpad", 11),
          ("voice", 8))
    )


_PortsType_Type.__name__ = "Integer32"
_PortsType_Object = MibTableColumn
portsType = _PortsType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 3),
    _PortsType_Type()
)
portsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsType.setStatus("mandatory")


class _PortsPhys_Type(Integer32):
    """Custom type portsPhys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("analogue", 8),
          ("aui", 5),
          ("isdn", 4),
          ("none", 0),
          ("tenBase2", 6),
          ("tenBaseT", 7),
          ("v24", 3),
          ("v35", 1),
          ("x21", 2))
    )


_PortsPhys_Type.__name__ = "Integer32"
_PortsPhys_Object = MibTableColumn
portsPhys = _PortsPhys_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 4),
    _PortsPhys_Type()
)
portsPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsPhys.setStatus("mandatory")
_PortsTxutil_Type = Integer32
_PortsTxutil_Object = MibTableColumn
portsTxutil = _PortsTxutil_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 5),
    _PortsTxutil_Type()
)
portsTxutil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsTxutil.setStatus("mandatory")
_PortsRxutil_Type = Integer32
_PortsRxutil_Object = MibTableColumn
portsRxutil = _PortsRxutil_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 6),
    _PortsRxutil_Type()
)
portsRxutil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsRxutil.setStatus("mandatory")
_PortsCompress_Type = Integer32
_PortsCompress_Object = MibTableColumn
portsCompress = _PortsCompress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 7),
    _PortsCompress_Type()
)
portsCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsCompress.setStatus("mandatory")


class _PortsState_Type(Integer32):
    """Custom type portsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notApplicable", 0),
          ("up", 1))
    )


_PortsState_Type.__name__ = "Integer32"
_PortsState_Object = MibTableColumn
portsState = _PortsState_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 8),
    _PortsState_Type()
)
portsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsState.setStatus("mandatory")
_PortsRxoctets_Type = Counter32
_PortsRxoctets_Object = MibTableColumn
portsRxoctets = _PortsRxoctets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 9),
    _PortsRxoctets_Type()
)
portsRxoctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsRxoctets.setStatus("mandatory")
_PortsTxoctets_Type = Counter32
_PortsTxoctets_Object = MibTableColumn
portsTxoctets = _PortsTxoctets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 10),
    _PortsTxoctets_Type()
)
portsTxoctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsTxoctets.setStatus("mandatory")
_PortsRxpackets_Type = Counter32
_PortsRxpackets_Object = MibTableColumn
portsRxpackets = _PortsRxpackets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 11),
    _PortsRxpackets_Type()
)
portsRxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsRxpackets.setStatus("mandatory")
_PortsTxpackets_Type = Counter32
_PortsTxpackets_Object = MibTableColumn
portsTxpackets = _PortsTxpackets_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 12),
    _PortsTxpackets_Type()
)
portsTxpackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsTxpackets.setStatus("mandatory")
_PortsRxerrs_Type = Counter32
_PortsRxerrs_Object = MibTableColumn
portsRxerrs = _PortsRxerrs_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 13),
    _PortsRxerrs_Type()
)
portsRxerrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsRxerrs.setStatus("mandatory")
_PortsTxerrs_Type = Counter32
_PortsTxerrs_Object = MibTableColumn
portsTxerrs = _PortsTxerrs_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 1, 1, 14),
    _PortsTxerrs_Type()
)
portsTxerrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsTxerrs.setStatus("mandatory")
_PortslanTable_Object = MibTable
portslanTable = _PortslanTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    portslanTable.setStatus("mandatory")
_PortslanEntry_Object = MibTableRow
portslanEntry = _PortslanEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1)
)
portslanEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portslanIndex"),
)
if mibBuilder.loadTexts:
    portslanEntry.setStatus("mandatory")
_PortslanIndex_Type = Integer32
_PortslanIndex_Object = MibTableColumn
portslanIndex = _PortslanIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 1),
    _PortslanIndex_Type()
)
portslanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portslanIndex.setStatus("mandatory")


class _PortslanName_Type(DisplayString):
    """Custom type portslanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortslanName_Type.__name__ = "DisplayString"
_PortslanName_Object = MibTableColumn
portslanName = _PortslanName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 2),
    _PortslanName_Type()
)
portslanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanName.setStatus("mandatory")
_PortslanPriority_Type = Integer32
_PortslanPriority_Object = MibTableColumn
portslanPriority = _PortslanPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 3),
    _PortslanPriority_Type()
)
portslanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanPriority.setStatus("mandatory")
_PortslanLinespeed_Type = Integer32
_PortslanLinespeed_Object = MibTableColumn
portslanLinespeed = _PortslanLinespeed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 4),
    _PortslanLinespeed_Type()
)
portslanLinespeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanLinespeed.setStatus("mandatory")
_PortslanIpAddress_Type = IpAddress
_PortslanIpAddress_Object = MibTableColumn
portslanIpAddress = _PortslanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 5),
    _PortslanIpAddress_Type()
)
portslanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanIpAddress.setStatus("mandatory")
_PortslanIpMask_Type = IpAddress
_PortslanIpMask_Object = MibTableColumn
portslanIpMask = _PortslanIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 6),
    _PortslanIpMask_Type()
)
portslanIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanIpMask.setStatus("mandatory")
_PortslanIpMetric_Type = Integer32
_PortslanIpMetric_Object = MibTableColumn
portslanIpMetric = _PortslanIpMetric_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 7),
    _PortslanIpMetric_Type()
)
portslanIpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanIpMetric.setStatus("mandatory")


class _PortslanIpxNetwork_Type(OctetString):
    """Custom type portslanIpxNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PortslanIpxNetwork_Type.__name__ = "OctetString"
_PortslanIpxNetwork_Object = MibTableColumn
portslanIpxNetwork = _PortslanIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 8),
    _PortslanIpxNetwork_Type()
)
portslanIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanIpxNetwork.setStatus("mandatory")


class _PortslanIpxType_Type(Integer32):
    """Custom type portslanIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_PortslanIpxType_Type.__name__ = "Integer32"
_PortslanIpxType_Object = MibTableColumn
portslanIpxType = _PortslanIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 2, 1, 9),
    _PortslanIpxType_Type()
)
portslanIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portslanIpxType.setStatus("mandatory")
_PortshdlcTable_Object = MibTable
portshdlcTable = _PortshdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    portshdlcTable.setStatus("mandatory")
_PortshdlcEntry_Object = MibTableRow
portshdlcEntry = _PortshdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1)
)
portshdlcEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portshdlcIndex"),
)
if mibBuilder.loadTexts:
    portshdlcEntry.setStatus("mandatory")
_PortshdlcIndex_Type = Integer32
_PortshdlcIndex_Object = MibTableColumn
portshdlcIndex = _PortshdlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 1),
    _PortshdlcIndex_Type()
)
portshdlcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portshdlcIndex.setStatus("mandatory")


class _PortshdlcName_Type(DisplayString):
    """Custom type portshdlcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortshdlcName_Type.__name__ = "DisplayString"
_PortshdlcName_Object = MibTableColumn
portshdlcName = _PortshdlcName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 2),
    _PortshdlcName_Type()
)
portshdlcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcName.setStatus("mandatory")
_PortshdlcPriority_Type = Integer32
_PortshdlcPriority_Object = MibTableColumn
portshdlcPriority = _PortshdlcPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 3),
    _PortshdlcPriority_Type()
)
portshdlcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcPriority.setStatus("mandatory")
_PortshdlcLinespeed_Type = Integer32
_PortshdlcLinespeed_Object = MibTableColumn
portshdlcLinespeed = _PortshdlcLinespeed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 4),
    _PortshdlcLinespeed_Type()
)
portshdlcLinespeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcLinespeed.setStatus("mandatory")


class _PortshdlcCompression_Type(Integer32):
    """Custom type portshdlcCompression based on Integer32"""
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
        *(("disabled", 0),
          ("lzStandard", 1),
          ("lzWhite", 2),
          ("stac", 3))
    )


_PortshdlcCompression_Type.__name__ = "Integer32"
_PortshdlcCompression_Object = MibTableColumn
portshdlcCompression = _PortshdlcCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 5),
    _PortshdlcCompression_Type()
)
portshdlcCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcCompression.setStatus("mandatory")


class _PortshdlcScramble_Type(Integer32):
    """Custom type portshdlcScramble based on Integer32"""
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


_PortshdlcScramble_Type.__name__ = "Integer32"
_PortshdlcScramble_Object = MibTableColumn
portshdlcScramble = _PortshdlcScramble_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 6),
    _PortshdlcScramble_Type()
)
portshdlcScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcScramble.setStatus("mandatory")


class _PortshdlcBackupdemand_Type(Integer32):
    """Custom type portshdlcBackupdemand based on Integer32"""
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
        *(("backup", 1),
          ("both", 3),
          ("demand", 2),
          ("none", 0))
    )


_PortshdlcBackupdemand_Type.__name__ = "Integer32"
_PortshdlcBackupdemand_Object = MibTableColumn
portshdlcBackupdemand = _PortshdlcBackupdemand_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 7),
    _PortshdlcBackupdemand_Type()
)
portshdlcBackupdemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcBackupdemand.setStatus("mandatory")
_PortshdlcDemandthresh_Type = Integer32
_PortshdlcDemandthresh_Object = MibTableColumn
portshdlcDemandthresh = _PortshdlcDemandthresh_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 8),
    _PortshdlcDemandthresh_Type()
)
portshdlcDemandthresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcDemandthresh.setStatus("mandatory")
_PortshdlcDemandperiod_Type = Integer32
_PortshdlcDemandperiod_Object = MibTableColumn
portshdlcDemandperiod = _PortshdlcDemandperiod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 9),
    _PortshdlcDemandperiod_Type()
)
portshdlcDemandperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcDemandperiod.setStatus("mandatory")
_PortshdlcIdlethresh_Type = Integer32
_PortshdlcIdlethresh_Object = MibTableColumn
portshdlcIdlethresh = _PortshdlcIdlethresh_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 10),
    _PortshdlcIdlethresh_Type()
)
portshdlcIdlethresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIdlethresh.setStatus("mandatory")
_PortshdlcIdleperiod_Type = Integer32
_PortshdlcIdleperiod_Object = MibTableColumn
portshdlcIdleperiod = _PortshdlcIdleperiod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 11),
    _PortshdlcIdleperiod_Type()
)
portshdlcIdleperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIdleperiod.setStatus("mandatory")


class _PortshdlcBackupalert_Type(Integer32):
    """Custom type portshdlcBackupalert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beep", 2),
          ("disabled", 0),
          ("enabled", 1))
    )


_PortshdlcBackupalert_Type.__name__ = "Integer32"
_PortshdlcBackupalert_Object = MibTableColumn
portshdlcBackupalert = _PortshdlcBackupalert_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 12),
    _PortshdlcBackupalert_Type()
)
portshdlcBackupalert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcBackupalert.setStatus("mandatory")


class _PortshdlcDemandpriority_Type(Integer32):
    """Custom type portshdlcDemandpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortshdlcDemandpriority_Type.__name__ = "Integer32"
_PortshdlcDemandpriority_Object = MibTableColumn
portshdlcDemandpriority = _PortshdlcDemandpriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 13),
    _PortshdlcDemandpriority_Type()
)
portshdlcDemandpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcDemandpriority.setStatus("mandatory")


class _PortshdlcBackuppriority_Type(Integer32):
    """Custom type portshdlcBackuppriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortshdlcBackuppriority_Type.__name__ = "Integer32"
_PortshdlcBackuppriority_Object = MibTableColumn
portshdlcBackuppriority = _PortshdlcBackuppriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 14),
    _PortshdlcBackuppriority_Type()
)
portshdlcBackuppriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcBackuppriority.setStatus("mandatory")


class _PortshdlcBackupnumber_Type(DisplayString):
    """Custom type portshdlcBackupnumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_PortshdlcBackupnumber_Type.__name__ = "DisplayString"
_PortshdlcBackupnumber_Object = MibTableColumn
portshdlcBackupnumber = _PortshdlcBackupnumber_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 15),
    _PortshdlcBackupnumber_Type()
)
portshdlcBackupnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcBackupnumber.setStatus("mandatory")
_PortshdlcBackupMac_Type = MacAddress
_PortshdlcBackupMac_Object = MibTableColumn
portshdlcBackupMac = _PortshdlcBackupMac_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 16),
    _PortshdlcBackupMac_Type()
)
portshdlcBackupMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcBackupMac.setStatus("mandatory")
_PortshdlcIpAddress_Type = IpAddress
_PortshdlcIpAddress_Object = MibTableColumn
portshdlcIpAddress = _PortshdlcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 17),
    _PortshdlcIpAddress_Type()
)
portshdlcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIpAddress.setStatus("mandatory")
_PortshdlcIpMask_Type = IpAddress
_PortshdlcIpMask_Object = MibTableColumn
portshdlcIpMask = _PortshdlcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 18),
    _PortshdlcIpMask_Type()
)
portshdlcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIpMask.setStatus("mandatory")
_PortshdlcIpMetric_Type = Integer32
_PortshdlcIpMetric_Object = MibTableColumn
portshdlcIpMetric = _PortshdlcIpMetric_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 19),
    _PortshdlcIpMetric_Type()
)
portshdlcIpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIpMetric.setStatus("mandatory")


class _PortshdlcIpxNetwork_Type(OctetString):
    """Custom type portshdlcIpxNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PortshdlcIpxNetwork_Type.__name__ = "OctetString"
_PortshdlcIpxNetwork_Object = MibTableColumn
portshdlcIpxNetwork = _PortshdlcIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 20),
    _PortshdlcIpxNetwork_Type()
)
portshdlcIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIpxNetwork.setStatus("mandatory")


class _PortshdlcIpxType_Type(Integer32):
    """Custom type portshdlcIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_PortshdlcIpxType_Type.__name__ = "Integer32"
_PortshdlcIpxType_Object = MibTableColumn
portshdlcIpxType = _PortshdlcIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 3, 1, 21),
    _PortshdlcIpxType_Type()
)
portshdlcIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portshdlcIpxType.setStatus("mandatory")
_PortspppTable_Object = MibTable
portspppTable = _PortspppTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    portspppTable.setStatus("mandatory")
_PortspppEntry_Object = MibTableRow
portspppEntry = _PortspppEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1)
)
portspppEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portspppIndex"),
)
if mibBuilder.loadTexts:
    portspppEntry.setStatus("mandatory")
_PortspppIndex_Type = Integer32
_PortspppIndex_Object = MibTableColumn
portspppIndex = _PortspppIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 1),
    _PortspppIndex_Type()
)
portspppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portspppIndex.setStatus("mandatory")


class _PortspppName_Type(DisplayString):
    """Custom type portspppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortspppName_Type.__name__ = "DisplayString"
_PortspppName_Object = MibTableColumn
portspppName = _PortspppName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 2),
    _PortspppName_Type()
)
portspppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppName.setStatus("mandatory")
_PortspppPriority_Type = Integer32
_PortspppPriority_Object = MibTableColumn
portspppPriority = _PortspppPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 3),
    _PortspppPriority_Type()
)
portspppPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppPriority.setStatus("mandatory")
_PortspppLinespeed_Type = Integer32
_PortspppLinespeed_Object = MibTableColumn
portspppLinespeed = _PortspppLinespeed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 4),
    _PortspppLinespeed_Type()
)
portspppLinespeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppLinespeed.setStatus("mandatory")
_PortspppIpAddress_Type = IpAddress
_PortspppIpAddress_Object = MibTableColumn
portspppIpAddress = _PortspppIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 5),
    _PortspppIpAddress_Type()
)
portspppIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIpAddress.setStatus("mandatory")
_PortspppIpMask_Type = IpAddress
_PortspppIpMask_Object = MibTableColumn
portspppIpMask = _PortspppIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 6),
    _PortspppIpMask_Type()
)
portspppIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIpMask.setStatus("mandatory")
_PortspppIpMetric_Type = Integer32
_PortspppIpMetric_Object = MibTableColumn
portspppIpMetric = _PortspppIpMetric_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 7),
    _PortspppIpMetric_Type()
)
portspppIpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIpMetric.setStatus("mandatory")


class _PortspppIpxNetwork_Type(OctetString):
    """Custom type portspppIpxNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PortspppIpxNetwork_Type.__name__ = "OctetString"
_PortspppIpxNetwork_Object = MibTableColumn
portspppIpxNetwork = _PortspppIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 8),
    _PortspppIpxNetwork_Type()
)
portspppIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIpxNetwork.setStatus("mandatory")


class _PortspppIpxType_Type(Integer32):
    """Custom type portspppIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_PortspppIpxType_Type.__name__ = "Integer32"
_PortspppIpxType_Object = MibTableColumn
portspppIpxType = _PortspppIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 9),
    _PortspppIpxType_Type()
)
portspppIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIpxType.setStatus("mandatory")


class _PortspppBaud_Type(Integer32):
    """Custom type portspppBaud based on Integer32"""
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
        *(("bd1200", 1),
          ("bd19200", 5),
          ("bd2400", 2),
          ("bd38400", 6),
          ("bd4800", 3),
          ("bd9600", 4))
    )


_PortspppBaud_Type.__name__ = "Integer32"
_PortspppBaud_Object = MibTableColumn
portspppBaud = _PortspppBaud_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 10),
    _PortspppBaud_Type()
)
portspppBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppBaud.setStatus("mandatory")


class _PortspppDataBits_Type(Integer32):
    """Custom type portspppDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data-7-bits", 7),
          ("data-8-bits", 8))
    )


_PortspppDataBits_Type.__name__ = "Integer32"
_PortspppDataBits_Object = MibTableColumn
portspppDataBits = _PortspppDataBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 11),
    _PortspppDataBits_Type()
)
portspppDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppDataBits.setStatus("mandatory")


class _PortspppStopBits_Type(Integer32):
    """Custom type portspppStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-1-bits", 1),
          ("data-2-bits", 2))
    )


_PortspppStopBits_Type.__name__ = "Integer32"
_PortspppStopBits_Object = MibTableColumn
portspppStopBits = _PortspppStopBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 12),
    _PortspppStopBits_Type()
)
portspppStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppStopBits.setStatus("mandatory")


class _PortspppFlowControl_Type(Integer32):
    """Custom type portspppFlowControl based on Integer32"""
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
        *(("halfxon", 3),
          ("none", 5),
          ("rts", 1),
          ("rts-on-tx", 4),
          ("xon", 2))
    )


_PortspppFlowControl_Type.__name__ = "Integer32"
_PortspppFlowControl_Object = MibTableColumn
portspppFlowControl = _PortspppFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 13),
    _PortspppFlowControl_Type()
)
portspppFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppFlowControl.setStatus("mandatory")


class _PortspppTxParity_Type(Integer32):
    """Custom type portspppTxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortspppTxParity_Type.__name__ = "Integer32"
_PortspppTxParity_Object = MibTableColumn
portspppTxParity = _PortspppTxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 14),
    _PortspppTxParity_Type()
)
portspppTxParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppTxParity.setStatus("mandatory")


class _PortspppRxParity_Type(Integer32):
    """Custom type portspppRxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortspppRxParity_Type.__name__ = "Integer32"
_PortspppRxParity_Object = MibTableColumn
portspppRxParity = _PortspppRxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 15),
    _PortspppRxParity_Type()
)
portspppRxParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppRxParity.setStatus("mandatory")


class _PortspppRemoteUnit_Type(Integer32):
    """Custom type portspppRemoteUnit based on Integer32"""
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
        *(("any", 1),
          ("ascend", 4),
          ("cisco", 3),
          ("r3com", 2),
          ("spider", 5))
    )


_PortspppRemoteUnit_Type.__name__ = "Integer32"
_PortspppRemoteUnit_Object = MibTableColumn
portspppRemoteUnit = _PortspppRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 16),
    _PortspppRemoteUnit_Type()
)
portspppRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppRemoteUnit.setStatus("mandatory")
_PortspppIPRemoteAddress_Type = IpAddress
_PortspppIPRemoteAddress_Object = MibTableColumn
portspppIPRemoteAddress = _PortspppIPRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 4, 1, 17),
    _PortspppIPRemoteAddress_Type()
)
portspppIPRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portspppIPRemoteAddress.setStatus("mandatory")
_PortstaTable_Object = MibTable
portstaTable = _PortstaTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    portstaTable.setStatus("mandatory")
_PortstaEntry_Object = MibTableRow
portstaEntry = _PortstaEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1)
)
portstaEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portstaIndex"),
)
if mibBuilder.loadTexts:
    portstaEntry.setStatus("mandatory")
_PortstaIndex_Type = Integer32
_PortstaIndex_Object = MibTableColumn
portstaIndex = _PortstaIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 1),
    _PortstaIndex_Type()
)
portstaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstaIndex.setStatus("mandatory")


class _PortstaName_Type(DisplayString):
    """Custom type portstaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortstaName_Type.__name__ = "DisplayString"
_PortstaName_Object = MibTableColumn
portstaName = _PortstaName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 2),
    _PortstaName_Type()
)
portstaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaName.setStatus("mandatory")
_PortstaPriority_Type = Integer32
_PortstaPriority_Object = MibTableColumn
portstaPriority = _PortstaPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 3),
    _PortstaPriority_Type()
)
portstaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaPriority.setStatus("mandatory")
_PortstaLinespeed_Type = Integer32
_PortstaLinespeed_Object = MibTableColumn
portstaLinespeed = _PortstaLinespeed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 4),
    _PortstaLinespeed_Type()
)
portstaLinespeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaLinespeed.setStatus("mandatory")


class _PortstaCompression_Type(Integer32):
    """Custom type portstaCompression based on Integer32"""
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
        *(("disabled", 0),
          ("lzStandard", 1),
          ("lzWhite", 2),
          ("stac", 3))
    )


_PortstaCompression_Type.__name__ = "Integer32"
_PortstaCompression_Object = MibTableColumn
portstaCompression = _PortstaCompression_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 5),
    _PortstaCompression_Type()
)
portstaCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaCompression.setStatus("mandatory")


class _PortstaScramble_Type(Integer32):
    """Custom type portstaScramble based on Integer32"""
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


_PortstaScramble_Type.__name__ = "Integer32"
_PortstaScramble_Object = MibTableColumn
portstaScramble = _PortstaScramble_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 6),
    _PortstaScramble_Type()
)
portstaScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaScramble.setStatus("mandatory")


class _PortstaDemand_Type(Integer32):
    """Custom type portstaDemand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 2))
    )


_PortstaDemand_Type.__name__ = "Integer32"
_PortstaDemand_Object = MibTableColumn
portstaDemand = _PortstaDemand_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 7),
    _PortstaDemand_Type()
)
portstaDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaDemand.setStatus("mandatory")
_PortstaDemandthresh_Type = Integer32
_PortstaDemandthresh_Object = MibTableColumn
portstaDemandthresh = _PortstaDemandthresh_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 8),
    _PortstaDemandthresh_Type()
)
portstaDemandthresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaDemandthresh.setStatus("mandatory")
_PortstaDemandperiod_Type = Integer32
_PortstaDemandperiod_Object = MibTableColumn
portstaDemandperiod = _PortstaDemandperiod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 9),
    _PortstaDemandperiod_Type()
)
portstaDemandperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaDemandperiod.setStatus("mandatory")
_PortstaIdlethresh_Type = Integer32
_PortstaIdlethresh_Object = MibTableColumn
portstaIdlethresh = _PortstaIdlethresh_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 10),
    _PortstaIdlethresh_Type()
)
portstaIdlethresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaIdlethresh.setStatus("mandatory")
_PortstaIdleperiod_Type = Integer32
_PortstaIdleperiod_Object = MibTableColumn
portstaIdleperiod = _PortstaIdleperiod_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 11),
    _PortstaIdleperiod_Type()
)
portstaIdleperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaIdleperiod.setStatus("mandatory")


class _PortstaDemandpriority_Type(Integer32):
    """Custom type portstaDemandpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortstaDemandpriority_Type.__name__ = "Integer32"
_PortstaDemandpriority_Object = MibTableColumn
portstaDemandpriority = _PortstaDemandpriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 13),
    _PortstaDemandpriority_Type()
)
portstaDemandpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaDemandpriority.setStatus("mandatory")


class _PortstaDialtimeout_Type(Integer32):
    """Custom type portstaDialtimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortstaDialtimeout_Type.__name__ = "Integer32"
_PortstaDialtimeout_Object = MibTableColumn
portstaDialtimeout = _PortstaDialtimeout_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 17),
    _PortstaDialtimeout_Type()
)
portstaDialtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaDialtimeout.setStatus("mandatory")


class _PortstaAtzstring_Type(DisplayString):
    """Custom type portstaAtzstring based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_PortstaAtzstring_Type.__name__ = "DisplayString"
_PortstaAtzstring_Object = MibTableColumn
portstaAtzstring = _PortstaAtzstring_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 18),
    _PortstaAtzstring_Type()
)
portstaAtzstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaAtzstring.setStatus("mandatory")


class _PortstaSpidstring_Type(DisplayString):
    """Custom type portstaSpidstring based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_PortstaSpidstring_Type.__name__ = "DisplayString"
_PortstaSpidstring_Object = MibTableColumn
portstaSpidstring = _PortstaSpidstring_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 5, 1, 19),
    _PortstaSpidstring_Type()
)
portstaSpidstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstaSpidstring.setStatus("mandatory")
_PortsslipTable_Object = MibTable
portsslipTable = _PortsslipTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    portsslipTable.setStatus("mandatory")
_PortsslipEntry_Object = MibTableRow
portsslipEntry = _PortsslipEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1)
)
portsslipEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portsslipIndex"),
)
if mibBuilder.loadTexts:
    portsslipEntry.setStatus("mandatory")
_PortsslipIndex_Type = Integer32
_PortsslipIndex_Object = MibTableColumn
portsslipIndex = _PortsslipIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 1),
    _PortsslipIndex_Type()
)
portsslipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsslipIndex.setStatus("mandatory")


class _PortsslipName_Type(DisplayString):
    """Custom type portsslipName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortsslipName_Type.__name__ = "DisplayString"
_PortsslipName_Object = MibTableColumn
portsslipName = _PortsslipName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 2),
    _PortsslipName_Type()
)
portsslipName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipName.setStatus("mandatory")
_PortsslipPriority_Type = Integer32
_PortsslipPriority_Object = MibTableColumn
portsslipPriority = _PortsslipPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 3),
    _PortsslipPriority_Type()
)
portsslipPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipPriority.setStatus("mandatory")
_PortsslipLinespeed_Type = Integer32
_PortsslipLinespeed_Object = MibTableColumn
portsslipLinespeed = _PortsslipLinespeed_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 4),
    _PortsslipLinespeed_Type()
)
portsslipLinespeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipLinespeed.setStatus("mandatory")
_PortsslipIpAddress_Type = IpAddress
_PortsslipIpAddress_Object = MibTableColumn
portsslipIpAddress = _PortsslipIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 5),
    _PortsslipIpAddress_Type()
)
portsslipIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipIpAddress.setStatus("mandatory")
_PortsslipIpMask_Type = IpAddress
_PortsslipIpMask_Object = MibTableColumn
portsslipIpMask = _PortsslipIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 6),
    _PortsslipIpMask_Type()
)
portsslipIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipIpMask.setStatus("mandatory")
_PortsslipIpMetric_Type = Integer32
_PortsslipIpMetric_Object = MibTableColumn
portsslipIpMetric = _PortsslipIpMetric_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 7),
    _PortsslipIpMetric_Type()
)
portsslipIpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipIpMetric.setStatus("mandatory")


class _PortsslipBaud_Type(Integer32):
    """Custom type portsslipBaud based on Integer32"""
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
        *(("bd1200", 1),
          ("bd19200", 5),
          ("bd2400", 2),
          ("bd38400", 6),
          ("bd4800", 3),
          ("bd9600", 4))
    )


_PortsslipBaud_Type.__name__ = "Integer32"
_PortsslipBaud_Object = MibTableColumn
portsslipBaud = _PortsslipBaud_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 8),
    _PortsslipBaud_Type()
)
portsslipBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipBaud.setStatus("mandatory")


class _PortsslipDataBits_Type(Integer32):
    """Custom type portsslipDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data-7-bits", 7),
          ("data-8-bits", 8))
    )


_PortsslipDataBits_Type.__name__ = "Integer32"
_PortsslipDataBits_Object = MibTableColumn
portsslipDataBits = _PortsslipDataBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 9),
    _PortsslipDataBits_Type()
)
portsslipDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsslipDataBits.setStatus("mandatory")


class _PortsslipStopBits_Type(Integer32):
    """Custom type portsslipStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-1-bits", 1),
          ("data-2-bits", 2))
    )


_PortsslipStopBits_Type.__name__ = "Integer32"
_PortsslipStopBits_Object = MibTableColumn
portsslipStopBits = _PortsslipStopBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 10),
    _PortsslipStopBits_Type()
)
portsslipStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipStopBits.setStatus("mandatory")


class _PortsslipFlowControl_Type(Integer32):
    """Custom type portsslipFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 5),
          ("rts", 1),
          ("rts-on-tx", 4))
    )


_PortsslipFlowControl_Type.__name__ = "Integer32"
_PortsslipFlowControl_Object = MibTableColumn
portsslipFlowControl = _PortsslipFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 11),
    _PortsslipFlowControl_Type()
)
portsslipFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipFlowControl.setStatus("mandatory")


class _PortsslipTxParity_Type(Integer32):
    """Custom type portsslipTxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortsslipTxParity_Type.__name__ = "Integer32"
_PortsslipTxParity_Object = MibTableColumn
portsslipTxParity = _PortsslipTxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 12),
    _PortsslipTxParity_Type()
)
portsslipTxParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsslipTxParity.setStatus("mandatory")


class _PortsslipRxParity_Type(Integer32):
    """Custom type portsslipRxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortsslipRxParity_Type.__name__ = "Integer32"
_PortsslipRxParity_Object = MibTableColumn
portsslipRxParity = _PortsslipRxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 13),
    _PortsslipRxParity_Type()
)
portsslipRxParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsslipRxParity.setStatus("mandatory")
_PortsslipMTU_Type = Integer32
_PortsslipMTU_Object = MibTableColumn
portsslipMTU = _PortsslipMTU_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 14),
    _PortsslipMTU_Type()
)
portsslipMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipMTU.setStatus("mandatory")


class _PortsslipRIPPrivate_Type(Integer32):
    """Custom type portsslipRIPPrivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_PortsslipRIPPrivate_Type.__name__ = "Integer32"
_PortsslipRIPPrivate_Object = MibTableColumn
portsslipRIPPrivate = _PortsslipRIPPrivate_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 15),
    _PortsslipRIPPrivate_Type()
)
portsslipRIPPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipRIPPrivate.setStatus("mandatory")
_PortsslipIPRemoteAddress_Type = IpAddress
_PortsslipIPRemoteAddress_Object = MibTableColumn
portsslipIPRemoteAddress = _PortsslipIPRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 6, 1, 16),
    _PortsslipIPRemoteAddress_Type()
)
portsslipIPRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsslipIPRemoteAddress.setStatus("mandatory")
_PortsasyncTable_Object = MibTable
portsasyncTable = _PortsasyncTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    portsasyncTable.setStatus("mandatory")
_PortsasyncEntry_Object = MibTableRow
portsasyncEntry = _PortsasyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1)
)
portsasyncEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portsasyncIndex"),
)
if mibBuilder.loadTexts:
    portsasyncEntry.setStatus("mandatory")
_PortsasyncIndex_Type = Integer32
_PortsasyncIndex_Object = MibTableColumn
portsasyncIndex = _PortsasyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 1),
    _PortsasyncIndex_Type()
)
portsasyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsasyncIndex.setStatus("mandatory")


class _PortsasyncName_Type(DisplayString):
    """Custom type portsasyncName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortsasyncName_Type.__name__ = "DisplayString"
_PortsasyncName_Object = MibTableColumn
portsasyncName = _PortsasyncName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 2),
    _PortsasyncName_Type()
)
portsasyncName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncName.setStatus("mandatory")


class _PortsasyncBaud_Type(Integer32):
    """Custom type portsasyncBaud based on Integer32"""
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
        *(("bd1200", 1),
          ("bd19200", 5),
          ("bd2400", 2),
          ("bd38400", 6),
          ("bd4800", 3),
          ("bd9600", 4))
    )


_PortsasyncBaud_Type.__name__ = "Integer32"
_PortsasyncBaud_Object = MibTableColumn
portsasyncBaud = _PortsasyncBaud_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 3),
    _PortsasyncBaud_Type()
)
portsasyncBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncBaud.setStatus("mandatory")


class _PortsasyncDataBits_Type(Integer32):
    """Custom type portsasyncDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data-7-bits", 7),
          ("data-8-bits", 8))
    )


_PortsasyncDataBits_Type.__name__ = "Integer32"
_PortsasyncDataBits_Object = MibTableColumn
portsasyncDataBits = _PortsasyncDataBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 4),
    _PortsasyncDataBits_Type()
)
portsasyncDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncDataBits.setStatus("mandatory")


class _PortsasyncStopBits_Type(Integer32):
    """Custom type portsasyncStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-1-bits", 1),
          ("data-2-bits", 2))
    )


_PortsasyncStopBits_Type.__name__ = "Integer32"
_PortsasyncStopBits_Object = MibTableColumn
portsasyncStopBits = _PortsasyncStopBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 5),
    _PortsasyncStopBits_Type()
)
portsasyncStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncStopBits.setStatus("mandatory")


class _PortsasyncFlowControl_Type(Integer32):
    """Custom type portsasyncFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("both", 6),
          ("none", 5),
          ("rtscts", 1),
          ("xonxoff", 2))
    )


_PortsasyncFlowControl_Type.__name__ = "Integer32"
_PortsasyncFlowControl_Object = MibTableColumn
portsasyncFlowControl = _PortsasyncFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 6),
    _PortsasyncFlowControl_Type()
)
portsasyncFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncFlowControl.setStatus("mandatory")


class _PortsasyncTxParity_Type(Integer32):
    """Custom type portsasyncTxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortsasyncTxParity_Type.__name__ = "Integer32"
_PortsasyncTxParity_Object = MibTableColumn
portsasyncTxParity = _PortsasyncTxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 7),
    _PortsasyncTxParity_Type()
)
portsasyncTxParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncTxParity.setStatus("mandatory")


class _PortsasyncRxParity_Type(Integer32):
    """Custom type portsasyncRxParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortsasyncRxParity_Type.__name__ = "Integer32"
_PortsasyncRxParity_Object = MibTableColumn
portsasyncRxParity = _PortsasyncRxParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 7, 1, 8),
    _PortsasyncRxParity_Type()
)
portsasyncRxParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsasyncRxParity.setStatus("mandatory")
_PortsvoiceTable_Object = MibTable
portsvoiceTable = _PortsvoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    portsvoiceTable.setStatus("mandatory")
_PortsvoiceEntry_Object = MibTableRow
portsvoiceEntry = _PortsvoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1)
)
portsvoiceEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portsvoiceIndex"),
)
if mibBuilder.loadTexts:
    portsvoiceEntry.setStatus("mandatory")
_PortsvoiceIndex_Type = Integer32
_PortsvoiceIndex_Object = MibTableColumn
portsvoiceIndex = _PortsvoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1, 1),
    _PortsvoiceIndex_Type()
)
portsvoiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsvoiceIndex.setStatus("mandatory")


class _PortsvoiceName_Type(DisplayString):
    """Custom type portsvoiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortsvoiceName_Type.__name__ = "DisplayString"
_PortsvoiceName_Object = MibTableColumn
portsvoiceName = _PortsvoiceName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1, 2),
    _PortsvoiceName_Type()
)
portsvoiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsvoiceName.setStatus("mandatory")


class _PortsvoiceCallsPermitted_Type(Integer32):
    """Custom type portsvoiceCallsPermitted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("inout", 0),
          ("out", 2))
    )


_PortsvoiceCallsPermitted_Type.__name__ = "Integer32"
_PortsvoiceCallsPermitted_Object = MibTableColumn
portsvoiceCallsPermitted = _PortsvoiceCallsPermitted_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1, 3),
    _PortsvoiceCallsPermitted_Type()
)
portsvoiceCallsPermitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsvoiceCallsPermitted.setStatus("mandatory")


class _PortsvoiceEncoding_Type(Integer32):
    """Custom type portsvoiceEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 0),
          ("ulaw", 1))
    )


_PortsvoiceEncoding_Type.__name__ = "Integer32"
_PortsvoiceEncoding_Object = MibTableColumn
portsvoiceEncoding = _PortsvoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1, 4),
    _PortsvoiceEncoding_Type()
)
portsvoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsvoiceEncoding.setStatus("mandatory")


class _PortsvoiceDialMode_Type(Integer32):
    """Custom type portsvoiceDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 1),
          ("overlap", 0))
    )


_PortsvoiceDialMode_Type.__name__ = "Integer32"
_PortsvoiceDialMode_Object = MibTableColumn
portsvoiceDialMode = _PortsvoiceDialMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 8, 1, 5),
    _PortsvoiceDialMode_Type()
)
portsvoiceDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsvoiceDialMode.setStatus("mandatory")
_PortstpadTable_Object = MibTable
portstpadTable = _PortstpadTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    portstpadTable.setStatus("mandatory")
_PortstpadEntry_Object = MibTableRow
portstpadEntry = _PortstpadEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1)
)
portstpadEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "portstpadIndex"),
)
if mibBuilder.loadTexts:
    portstpadEntry.setStatus("mandatory")
_PortstpadIndex_Type = Integer32
_PortstpadIndex_Object = MibTableColumn
portstpadIndex = _PortstpadIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 1),
    _PortstpadIndex_Type()
)
portstpadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portstpadIndex.setStatus("mandatory")


class _PortstpadName_Type(DisplayString):
    """Custom type portstpadName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_PortstpadName_Type.__name__ = "DisplayString"
_PortstpadName_Object = MibTableColumn
portstpadName = _PortstpadName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 2),
    _PortstpadName_Type()
)
portstpadName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadName.setStatus("mandatory")


class _PortstpadBaud_Type(Integer32):
    """Custom type portstpadBaud based on Integer32"""
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
        *(("bd1200", 1),
          ("bd19200", 5),
          ("bd2400", 2),
          ("bd38400", 6),
          ("bd4800", 3),
          ("bd57600", 7),
          ("bd9600", 4))
    )


_PortstpadBaud_Type.__name__ = "Integer32"
_PortstpadBaud_Object = MibTableColumn
portstpadBaud = _PortstpadBaud_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 3),
    _PortstpadBaud_Type()
)
portstpadBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadBaud.setStatus("mandatory")


class _PortstpadDataBits_Type(Integer32):
    """Custom type portstpadDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data-7-bits", 7),
          ("data-8-bits", 8))
    )


_PortstpadDataBits_Type.__name__ = "Integer32"
_PortstpadDataBits_Object = MibTableColumn
portstpadDataBits = _PortstpadDataBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 4),
    _PortstpadDataBits_Type()
)
portstpadDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadDataBits.setStatus("mandatory")


class _PortstpadStopBits_Type(Integer32):
    """Custom type portstpadStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-1-bits", 1),
          ("data-2-bits", 2))
    )


_PortstpadStopBits_Type.__name__ = "Integer32"
_PortstpadStopBits_Object = MibTableColumn
portstpadStopBits = _PortstpadStopBits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 5),
    _PortstpadStopBits_Type()
)
portstpadStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadStopBits.setStatus("mandatory")


class _PortstpadParity_Type(Integer32):
    """Custom type portstpadParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_PortstpadParity_Type.__name__ = "Integer32"
_PortstpadParity_Object = MibTableColumn
portstpadParity = _PortstpadParity_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 6),
    _PortstpadParity_Type()
)
portstpadParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadParity.setStatus("mandatory")


class _PortstpadTxFlowControl_Type(Integer32):
    """Custom type portstpadTxFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("both", 6),
          ("none", 5),
          ("rtscts", 1),
          ("xonxoff", 2))
    )


_PortstpadTxFlowControl_Type.__name__ = "Integer32"
_PortstpadTxFlowControl_Object = MibTableColumn
portstpadTxFlowControl = _PortstpadTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 7),
    _PortstpadTxFlowControl_Type()
)
portstpadTxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadTxFlowControl.setStatus("mandatory")


class _PortstpadRxFlowControl_Type(Integer32):
    """Custom type portstpadRxFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("both", 6),
          ("none", 5),
          ("rtscts", 1),
          ("xonxoff", 2))
    )


_PortstpadRxFlowControl_Type.__name__ = "Integer32"
_PortstpadRxFlowControl_Object = MibTableColumn
portstpadRxFlowControl = _PortstpadRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 8),
    _PortstpadRxFlowControl_Type()
)
portstpadRxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadRxFlowControl.setStatus("mandatory")
_PortstpadX25MinLCN_Type = Integer32
_PortstpadX25MinLCN_Object = MibTableColumn
portstpadX25MinLCN = _PortstpadX25MinLCN_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 9),
    _PortstpadX25MinLCN_Type()
)
portstpadX25MinLCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadX25MinLCN.setStatus("mandatory")
_PortstpadX25MaxLCN_Type = Integer32
_PortstpadX25MaxLCN_Object = MibTableColumn
portstpadX25MaxLCN = _PortstpadX25MaxLCN_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 2, 9, 1, 10),
    _PortstpadX25MaxLCN_Type()
)
portstpadX25MaxLCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portstpadX25MaxLCN.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3)
)
_Mlink_ObjectIdentity = ObjectIdentity
mlink = _Mlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1)
)
_MlinkTable_Object = MibTable
mlinkTable = _MlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mlinkTable.setStatus("mandatory")
_MlinkEntry_Object = MibTableRow
mlinkEntry = _MlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1)
)
mlinkEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "mlinkIndex"),
)
if mibBuilder.loadTexts:
    mlinkEntry.setStatus("mandatory")
_MlinkIndex_Type = Integer32
_MlinkIndex_Object = MibTableColumn
mlinkIndex = _MlinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 1),
    _MlinkIndex_Type()
)
mlinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkIndex.setStatus("mandatory")


class _MlinkName_Type(DisplayString):
    """Custom type mlinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_MlinkName_Type.__name__ = "DisplayString"
_MlinkName_Object = MibTableColumn
mlinkName = _MlinkName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 2),
    _MlinkName_Type()
)
mlinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkName.setStatus("mandatory")
_MlinkNumberOfPorts_Type = Integer32
_MlinkNumberOfPorts_Object = MibTableColumn
mlinkNumberOfPorts = _MlinkNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 3),
    _MlinkNumberOfPorts_Type()
)
mlinkNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkNumberOfPorts.setStatus("mandatory")
_MlinkInFrames_Type = Counter32
_MlinkInFrames_Object = MibTableColumn
mlinkInFrames = _MlinkInFrames_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 4),
    _MlinkInFrames_Type()
)
mlinkInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkInFrames.setStatus("mandatory")
_MlinkOutFrames_Type = Counter32
_MlinkOutFrames_Object = MibTableColumn
mlinkOutFrames = _MlinkOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 5),
    _MlinkOutFrames_Type()
)
mlinkOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkOutFrames.setStatus("mandatory")
_MlinkInDiscards_Type = Counter32
_MlinkInDiscards_Object = MibTableColumn
mlinkInDiscards = _MlinkInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 6),
    _MlinkInDiscards_Type()
)
mlinkInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkInDiscards.setStatus("mandatory")


class _MlinkState_Type(Integer32):
    """Custom type mlinkState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_MlinkState_Type.__name__ = "Integer32"
_MlinkState_Object = MibTableColumn
mlinkState = _MlinkState_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 1, 1, 1, 7),
    _MlinkState_Type()
)
mlinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlinkState.setStatus("mandatory")
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1)
)
filterEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "filterDest"),
    (0, "REMOTEACCESS-MIB", "filterSource"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")


class _FilterDest_Type(OctetString):
    """Custom type filterDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FilterDest_Type.__name__ = "OctetString"
_FilterDest_Object = MibTableColumn
filterDest = _FilterDest_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 1),
    _FilterDest_Type()
)
filterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDest.setStatus("mandatory")


class _FilterSource_Type(OctetString):
    """Custom type filterSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FilterSource_Type.__name__ = "OctetString"
_FilterSource_Object = MibTableColumn
filterSource = _FilterSource_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 2),
    _FilterSource_Type()
)
filterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterSource.setStatus("mandatory")


class _FilterPrimary_Type(Integer32):
    """Custom type filterPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FilterPrimary_Type.__name__ = "Integer32"
_FilterPrimary_Object = MibTableColumn
filterPrimary = _FilterPrimary_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 3),
    _FilterPrimary_Type()
)
filterPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPrimary.setStatus("mandatory")


class _FilterType_Type(Integer32):
    """Custom type filterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("learned", 2),
          ("permanent", 1))
    )


_FilterType_Type.__name__ = "Integer32"
_FilterType_Object = MibTableColumn
filterType = _FilterType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 4),
    _FilterType_Type()
)
filterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterType.setStatus("mandatory")
_FilterRoute_Type = DisplayString
_FilterRoute_Object = MibTableColumn
filterRoute = _FilterRoute_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 5),
    _FilterRoute_Type()
)
filterRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterRoute.setStatus("mandatory")
_FilterPacketcount_Type = Integer32
_FilterPacketcount_Object = MibTableColumn
filterPacketcount = _FilterPacketcount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 6),
    _FilterPacketcount_Type()
)
filterPacketcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPacketcount.setStatus("mandatory")
_FilterBytecount_Type = Integer32
_FilterBytecount_Object = MibTableColumn
filterBytecount = _FilterBytecount_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 1, 1, 7),
    _FilterBytecount_Type()
)
filterBytecount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterBytecount.setStatus("mandatory")
_FiltertypeTable_Object = MibTable
filtertypeTable = _FiltertypeTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    filtertypeTable.setStatus("mandatory")
_FiltertypeEntry_Object = MibTableRow
filtertypeEntry = _FiltertypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2, 1)
)
filtertypeEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "filtertypeIndex"),
)
if mibBuilder.loadTexts:
    filtertypeEntry.setStatus("mandatory")
_FiltertypeIndex_Type = Integer32
_FiltertypeIndex_Object = MibTableColumn
filtertypeIndex = _FiltertypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2, 1, 1),
    _FiltertypeIndex_Type()
)
filtertypeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filtertypeIndex.setStatus("mandatory")


class _FiltertypeClass_Type(Integer32):
    """Custom type filtertypeClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee", 0))
    )


_FiltertypeClass_Type.__name__ = "Integer32"
_FiltertypeClass_Object = MibTableColumn
filtertypeClass = _FiltertypeClass_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2, 1, 2),
    _FiltertypeClass_Type()
)
filtertypeClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filtertypeClass.setStatus("mandatory")
_FiltertypeLsap_Type = Integer32
_FiltertypeLsap_Object = MibTableColumn
filtertypeLsap = _FiltertypeLsap_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2, 1, 3),
    _FiltertypeLsap_Type()
)
filtertypeLsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filtertypeLsap.setStatus("mandatory")


class _FiltertypeMode_Type(Integer32):
    """Custom type filtertypeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 0))
    )


_FiltertypeMode_Type.__name__ = "Integer32"
_FiltertypeMode_Object = MibTableColumn
filtertypeMode = _FiltertypeMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 2, 1, 4),
    _FiltertypeMode_Type()
)
filtertypeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filtertypeMode.setStatus("mandatory")


class _FilterAgingtime_Type(Integer32):
    """Custom type filterAgingtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterAgingtime_Type.__name__ = "Integer32"
_FilterAgingtime_Object = MibTableColumn
filterAgingtime = _FilterAgingtime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 3),
    _FilterAgingtime_Type()
)
filterAgingtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterAgingtime.setStatus("mandatory")


class _FilterLearning_Type(Integer32):
    """Custom type filterLearning based on Integer32"""
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


_FilterLearning_Type.__name__ = "Integer32"
_FilterLearning_Object = MibTableColumn
filterLearning = _FilterLearning_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 4),
    _FilterLearning_Type()
)
filterLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterLearning.setStatus("mandatory")


class _FilterActiononmatch_Type(Integer32):
    """Custom type filterActiononmatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reject", 0))
    )


_FilterActiononmatch_Type.__name__ = "Integer32"
_FilterActiononmatch_Object = MibTableColumn
filterActiononmatch = _FilterActiononmatch_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 5),
    _FilterActiononmatch_Type()
)
filterActiononmatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActiononmatch.setStatus("mandatory")


class _FilterFiltermcast_Type(Integer32):
    """Custom type filterFiltermcast based on Integer32"""
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


_FilterFiltermcast_Type.__name__ = "Integer32"
_FilterFiltermcast_Object = MibTableColumn
filterFiltermcast = _FilterFiltermcast_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 6),
    _FilterFiltermcast_Type()
)
filterFiltermcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterFiltermcast.setStatus("mandatory")


class _FilterTypematching_Type(Integer32):
    """Custom type filterTypematching based on Integer32"""
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


_FilterTypematching_Type.__name__ = "Integer32"
_FilterTypematching_Object = MibTableColumn
filterTypematching = _FilterTypematching_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 7),
    _FilterTypematching_Type()
)
filterTypematching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTypematching.setStatus("mandatory")


class _FilterTypematchaction_Type(Integer32):
    """Custom type filterTypematchaction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reject", 0))
    )


_FilterTypematchaction_Type.__name__ = "Integer32"
_FilterTypematchaction_Object = MibTableColumn
filterTypematchaction = _FilterTypematchaction_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 8),
    _FilterTypematchaction_Type()
)
filterTypematchaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterTypematchaction.setStatus("mandatory")


class _FilterLearnsourceonmcast_Type(Integer32):
    """Custom type filterLearnsourceonmcast based on Integer32"""
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


_FilterLearnsourceonmcast_Type.__name__ = "Integer32"
_FilterLearnsourceonmcast_Object = MibTableColumn
filterLearnsourceonmcast = _FilterLearnsourceonmcast_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 9),
    _FilterLearnsourceonmcast_Type()
)
filterLearnsourceonmcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterLearnsourceonmcast.setStatus("mandatory")


class _FilterFlushall_Type(Integer32):
    """Custom type filterFlushall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FilterFlushall_Type.__name__ = "Integer32"
_FilterFlushall_Object = MibTableColumn
filterFlushall = _FilterFlushall_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 10),
    _FilterFlushall_Type()
)
filterFlushall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterFlushall.setStatus("mandatory")


class _FilterLearnnovell_Type(Integer32):
    """Custom type filterLearnnovell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FilterLearnnovell_Type.__name__ = "Integer32"
_FilterLearnnovell_Object = MibTableColumn
filterLearnnovell = _FilterLearnnovell_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 11),
    _FilterLearnnovell_Type()
)
filterLearnnovell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterLearnnovell.setStatus("mandatory")


class _FilterLearnbridging_Type(Integer32):
    """Custom type filterLearnbridging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FilterLearnbridging_Type.__name__ = "Integer32"
_FilterLearnbridging_Object = MibScalar
filterLearnbridging = _FilterLearnbridging_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 2, 12),
    _FilterLearnbridging_Type()
)
filterLearnbridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterLearnbridging.setStatus("mandatory")
_Authorised_ObjectIdentity = ObjectIdentity
authorised = _Authorised_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3)
)
_AuthorisedTable_Object = MibTable
authorisedTable = _AuthorisedTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    authorisedTable.setStatus("mandatory")
_AuthorisedEntry_Object = MibTableRow
authorisedEntry = _AuthorisedEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3, 1, 1)
)
authorisedEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "authorisedIndex"),
)
if mibBuilder.loadTexts:
    authorisedEntry.setStatus("mandatory")


class _AuthorisedIndex_Type(OctetString):
    """Custom type authorisedIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AuthorisedIndex_Type.__name__ = "OctetString"
_AuthorisedIndex_Object = MibTableColumn
authorisedIndex = _AuthorisedIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3, 1, 1, 1),
    _AuthorisedIndex_Type()
)
authorisedIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorisedIndex.setStatus("mandatory")


class _AuthorisedAddress_Type(OctetString):
    """Custom type authorisedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AuthorisedAddress_Type.__name__ = "OctetString"
_AuthorisedAddress_Object = MibTableColumn
authorisedAddress = _AuthorisedAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3, 1, 1, 2),
    _AuthorisedAddress_Type()
)
authorisedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorisedAddress.setStatus("mandatory")


class _AuthorisedMode_Type(Integer32):
    """Custom type authorisedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 0))
    )


_AuthorisedMode_Type.__name__ = "Integer32"
_AuthorisedMode_Object = MibTableColumn
authorisedMode = _AuthorisedMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 3, 1, 1, 3),
    _AuthorisedMode_Type()
)
authorisedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorisedMode.setStatus("mandatory")
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4)
)
_Autocall_ObjectIdentity = ObjectIdentity
autocall = _Autocall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1)
)
_AutocallMacTable_Object = MibTable
autocallMacTable = _AutocallMacTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    autocallMacTable.setStatus("mandatory")
_AutocallMacEntry_Object = MibTableRow
autocallMacEntry = _AutocallMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1)
)
autocallMacEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallMacIndex"),
)
if mibBuilder.loadTexts:
    autocallMacEntry.setStatus("mandatory")


class _AutocallMacIndex_Type(OctetString):
    """Custom type autocallMacIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallMacIndex_Type.__name__ = "OctetString"
_AutocallMacIndex_Object = MibTableColumn
autocallMacIndex = _AutocallMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 1),
    _AutocallMacIndex_Type()
)
autocallMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallMacIndex.setStatus("mandatory")


class _AutocallMacDefault_Type(Integer32):
    """Custom type autocallMacDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallMacDefault_Type.__name__ = "Integer32"
_AutocallMacDefault_Object = MibTableColumn
autocallMacDefault = _AutocallMacDefault_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 2),
    _AutocallMacDefault_Type()
)
autocallMacDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacDefault.setStatus("mandatory")


class _AutocallMacBumpable_Type(Integer32):
    """Custom type autocallMacBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallMacBumpable_Type.__name__ = "Integer32"
_AutocallMacBumpable_Object = MibTableColumn
autocallMacBumpable = _AutocallMacBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 3),
    _AutocallMacBumpable_Type()
)
autocallMacBumpable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacBumpable.setStatus("mandatory")
_AutocallMacIdle_Type = Integer32
_AutocallMacIdle_Object = MibTableColumn
autocallMacIdle = _AutocallMacIdle_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 4),
    _AutocallMacIdle_Type()
)
autocallMacIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacIdle.setStatus("mandatory")


class _AutocallMacIdleThreshold_Type(Integer32):
    """Custom type autocallMacIdleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AutocallMacIdleThreshold_Type.__name__ = "Integer32"
_AutocallMacIdleThreshold_Object = MibTableColumn
autocallMacIdleThreshold = _AutocallMacIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 5),
    _AutocallMacIdleThreshold_Type()
)
autocallMacIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacIdleThreshold.setStatus("mandatory")
_AutocallMacAddress_Type = MacAddress
_AutocallMacAddress_Object = MibTableColumn
autocallMacAddress = _AutocallMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 6),
    _AutocallMacAddress_Type()
)
autocallMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacAddress.setStatus("mandatory")


class _AutocallMacIsdn_Type(DisplayString):
    """Custom type autocallMacIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallMacIsdn_Type.__name__ = "DisplayString"
_AutocallMacIsdn_Object = MibTableColumn
autocallMacIsdn = _AutocallMacIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 7),
    _AutocallMacIsdn_Type()
)
autocallMacIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacIsdn.setStatus("mandatory")


class _AutocallMacMode_Type(Integer32):
    """Custom type autocallMacMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallMacMode_Type.__name__ = "Integer32"
_AutocallMacMode_Object = MibTableColumn
autocallMacMode = _AutocallMacMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 2, 1, 8),
    _AutocallMacMode_Type()
)
autocallMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallMacMode.setStatus("mandatory")
_AutocallIpTable_Object = MibTable
autocallIpTable = _AutocallIpTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    autocallIpTable.setStatus("mandatory")
_AutocallIpEntry_Object = MibTableRow
autocallIpEntry = _AutocallIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1)
)
autocallIpEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallIpIndex"),
)
if mibBuilder.loadTexts:
    autocallIpEntry.setStatus("mandatory")


class _AutocallIpIndex_Type(OctetString):
    """Custom type autocallIpIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpIndex_Type.__name__ = "OctetString"
_AutocallIpIndex_Object = MibTableColumn
autocallIpIndex = _AutocallIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 1),
    _AutocallIpIndex_Type()
)
autocallIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallIpIndex.setStatus("mandatory")


class _AutocallIpBumpable_Type(Integer32):
    """Custom type autocallIpBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpBumpable_Type.__name__ = "Integer32"
_AutocallIpBumpable_Object = MibTableColumn
autocallIpBumpable = _AutocallIpBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 2),
    _AutocallIpBumpable_Type()
)
autocallIpBumpable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpBumpable.setStatus("mandatory")
_AutocallIpIdle_Type = Integer32
_AutocallIpIdle_Object = MibTableColumn
autocallIpIdle = _AutocallIpIdle_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 3),
    _AutocallIpIdle_Type()
)
autocallIpIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpIdle.setStatus("mandatory")


class _AutocallIpIdleThreshold_Type(Integer32):
    """Custom type autocallIpIdleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AutocallIpIdleThreshold_Type.__name__ = "Integer32"
_AutocallIpIdleThreshold_Object = MibTableColumn
autocallIpIdleThreshold = _AutocallIpIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 4),
    _AutocallIpIdleThreshold_Type()
)
autocallIpIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpIdleThreshold.setStatus("mandatory")
_AutocallIpAddress_Type = IpAddress
_AutocallIpAddress_Object = MibTableColumn
autocallIpAddress = _AutocallIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 5),
    _AutocallIpAddress_Type()
)
autocallIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpAddress.setStatus("mandatory")
_AutocallIpMask_Type = IpAddress
_AutocallIpMask_Object = MibTableColumn
autocallIpMask = _AutocallIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 6),
    _AutocallIpMask_Type()
)
autocallIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpMask.setStatus("mandatory")


class _AutocallIpInverse_Type(Integer32):
    """Custom type autocallIpInverse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpInverse_Type.__name__ = "Integer32"
_AutocallIpInverse_Object = MibTableColumn
autocallIpInverse = _AutocallIpInverse_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 7),
    _AutocallIpInverse_Type()
)
autocallIpInverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpInverse.setStatus("mandatory")


class _AutocallIpIsdn_Type(DisplayString):
    """Custom type autocallIpIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallIpIsdn_Type.__name__ = "DisplayString"
_AutocallIpIsdn_Object = MibTableColumn
autocallIpIsdn = _AutocallIpIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 8),
    _AutocallIpIsdn_Type()
)
autocallIpIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpIsdn.setStatus("mandatory")


class _AutocallIpMode_Type(Integer32):
    """Custom type autocallIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallIpMode_Type.__name__ = "Integer32"
_AutocallIpMode_Object = MibTableColumn
autocallIpMode = _AutocallIpMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 3, 1, 9),
    _AutocallIpMode_Type()
)
autocallIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpMode.setStatus("mandatory")
_AutocallIpxSapTable_Object = MibTable
autocallIpxSapTable = _AutocallIpxSapTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    autocallIpxSapTable.setStatus("mandatory")
_AutocallIpxSapEntry_Object = MibTableRow
autocallIpxSapEntry = _AutocallIpxSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1)
)
autocallIpxSapEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallIpxSapIndex"),
)
if mibBuilder.loadTexts:
    autocallIpxSapEntry.setStatus("mandatory")


class _AutocallIpxSapIndex_Type(OctetString):
    """Custom type autocallIpxSapIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpxSapIndex_Type.__name__ = "OctetString"
_AutocallIpxSapIndex_Object = MibTableColumn
autocallIpxSapIndex = _AutocallIpxSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 1),
    _AutocallIpxSapIndex_Type()
)
autocallIpxSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallIpxSapIndex.setStatus("mandatory")


class _AutocallIpxSapServer_Type(DisplayString):
    """Custom type autocallIpxSapServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_AutocallIpxSapServer_Type.__name__ = "DisplayString"
_AutocallIpxSapServer_Object = MibTableColumn
autocallIpxSapServer = _AutocallIpxSapServer_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 2),
    _AutocallIpxSapServer_Type()
)
autocallIpxSapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapServer.setStatus("mandatory")


class _AutocallIpxSapNetwork_Type(OctetString):
    """Custom type autocallIpxSapNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AutocallIpxSapNetwork_Type.__name__ = "OctetString"
_AutocallIpxSapNetwork_Object = MibTableColumn
autocallIpxSapNetwork = _AutocallIpxSapNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 3),
    _AutocallIpxSapNetwork_Type()
)
autocallIpxSapNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapNetwork.setStatus("mandatory")
_AutocallIpxSapNode_Type = MacAddress
_AutocallIpxSapNode_Object = MibTableColumn
autocallIpxSapNode = _AutocallIpxSapNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 4),
    _AutocallIpxSapNode_Type()
)
autocallIpxSapNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapNode.setStatus("mandatory")


class _AutocallIpxSapSocket_Type(OctetString):
    """Custom type autocallIpxSapSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpxSapSocket_Type.__name__ = "OctetString"
_AutocallIpxSapSocket_Object = MibTableColumn
autocallIpxSapSocket = _AutocallIpxSapSocket_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 5),
    _AutocallIpxSapSocket_Type()
)
autocallIpxSapSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapSocket.setStatus("mandatory")


class _AutocallIpxSapService_Type(OctetString):
    """Custom type autocallIpxSapService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpxSapService_Type.__name__ = "OctetString"
_AutocallIpxSapService_Object = MibTableColumn
autocallIpxSapService = _AutocallIpxSapService_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 6),
    _AutocallIpxSapService_Type()
)
autocallIpxSapService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapService.setStatus("mandatory")


class _AutocallIpxSapHops_Type(Integer32):
    """Custom type autocallIpxSapHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AutocallIpxSapHops_Type.__name__ = "Integer32"
_AutocallIpxSapHops_Object = MibTableColumn
autocallIpxSapHops = _AutocallIpxSapHops_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 7),
    _AutocallIpxSapHops_Type()
)
autocallIpxSapHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapHops.setStatus("mandatory")


class _AutocallIpxSapIsdn_Type(DisplayString):
    """Custom type autocallIpxSapIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallIpxSapIsdn_Type.__name__ = "DisplayString"
_AutocallIpxSapIsdn_Object = MibTableColumn
autocallIpxSapIsdn = _AutocallIpxSapIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 8),
    _AutocallIpxSapIsdn_Type()
)
autocallIpxSapIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapIsdn.setStatus("mandatory")


class _AutocallIpxSapFrameType_Type(Integer32):
    """Custom type autocallIpxSapFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("etherII", 1),
          ("ieee8022", 2),
          ("ieee8023", 3),
          ("snap", 4))
    )


_AutocallIpxSapFrameType_Type.__name__ = "Integer32"
_AutocallIpxSapFrameType_Object = MibTableColumn
autocallIpxSapFrameType = _AutocallIpxSapFrameType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 9),
    _AutocallIpxSapFrameType_Type()
)
autocallIpxSapFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapFrameType.setStatus("mandatory")


class _AutocallIpxSapDirectNetwork_Type(OctetString):
    """Custom type autocallIpxSapDirectNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AutocallIpxSapDirectNetwork_Type.__name__ = "OctetString"
_AutocallIpxSapDirectNetwork_Object = MibTableColumn
autocallIpxSapDirectNetwork = _AutocallIpxSapDirectNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 10),
    _AutocallIpxSapDirectNetwork_Type()
)
autocallIpxSapDirectNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapDirectNetwork.setStatus("mandatory")
_AutocallIpxSapRouterMac_Type = MacAddress
_AutocallIpxSapRouterMac_Object = MibTableColumn
autocallIpxSapRouterMac = _AutocallIpxSapRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 11),
    _AutocallIpxSapRouterMac_Type()
)
autocallIpxSapRouterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapRouterMac.setStatus("mandatory")


class _AutocallIpxSapNearest_Type(Integer32):
    """Custom type autocallIpxSapNearest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxSapNearest_Type.__name__ = "Integer32"
_AutocallIpxSapNearest_Object = MibTableColumn
autocallIpxSapNearest = _AutocallIpxSapNearest_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 12),
    _AutocallIpxSapNearest_Type()
)
autocallIpxSapNearest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapNearest.setStatus("mandatory")


class _AutocallIpxSapPpp_Type(Integer32):
    """Custom type autocallIpxSapPpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxSapPpp_Type.__name__ = "Integer32"
_AutocallIpxSapPpp_Object = MibTableColumn
autocallIpxSapPpp = _AutocallIpxSapPpp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 13),
    _AutocallIpxSapPpp_Type()
)
autocallIpxSapPpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapPpp.setStatus("mandatory")


class _AutocallIpxSapIsdnType_Type(Integer32):
    """Custom type autocallIpxSapIsdnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 2),
          ("sync", 1))
    )


_AutocallIpxSapIsdnType_Type.__name__ = "Integer32"
_AutocallIpxSapIsdnType_Object = MibTableColumn
autocallIpxSapIsdnType = _AutocallIpxSapIsdnType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 14),
    _AutocallIpxSapIsdnType_Type()
)
autocallIpxSapIsdnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapIsdnType.setStatus("mandatory")


class _AutocallIpxSapMode_Type(Integer32):
    """Custom type autocallIpxSapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallIpxSapMode_Type.__name__ = "Integer32"
_AutocallIpxSapMode_Object = MibTableColumn
autocallIpxSapMode = _AutocallIpxSapMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 4, 1, 15),
    _AutocallIpxSapMode_Type()
)
autocallIpxSapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxSapMode.setStatus("mandatory")
_AutocallIpxTable_Object = MibTable
autocallIpxTable = _AutocallIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    autocallIpxTable.setStatus("mandatory")
_AutocallIpxEntry_Object = MibTableRow
autocallIpxEntry = _AutocallIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1)
)
autocallIpxEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallIpxIndex"),
)
if mibBuilder.loadTexts:
    autocallIpxEntry.setStatus("mandatory")


class _AutocallIpxIndex_Type(OctetString):
    """Custom type autocallIpxIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpxIndex_Type.__name__ = "OctetString"
_AutocallIpxIndex_Object = MibTableColumn
autocallIpxIndex = _AutocallIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 1),
    _AutocallIpxIndex_Type()
)
autocallIpxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallIpxIndex.setStatus("mandatory")


class _AutocallIpxNetwork_Type(OctetString):
    """Custom type autocallIpxNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AutocallIpxNetwork_Type.__name__ = "OctetString"
_AutocallIpxNetwork_Object = MibTableColumn
autocallIpxNetwork = _AutocallIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 2),
    _AutocallIpxNetwork_Type()
)
autocallIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxNetwork.setStatus("mandatory")
_AutocallIpxNode_Type = MacAddress
_AutocallIpxNode_Object = MibTableColumn
autocallIpxNode = _AutocallIpxNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 3),
    _AutocallIpxNode_Type()
)
autocallIpxNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxNode.setStatus("mandatory")


class _AutocallIpxPacketType_Type(OctetString):
    """Custom type autocallIpxPacketType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_AutocallIpxPacketType_Type.__name__ = "OctetString"
_AutocallIpxPacketType_Object = MibTableColumn
autocallIpxPacketType = _AutocallIpxPacketType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 4),
    _AutocallIpxPacketType_Type()
)
autocallIpxPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxPacketType.setStatus("mandatory")


class _AutocallIpxTransportControl_Type(Integer32):
    """Custom type autocallIpxTransportControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AutocallIpxTransportControl_Type.__name__ = "Integer32"
_AutocallIpxTransportControl_Object = MibTableColumn
autocallIpxTransportControl = _AutocallIpxTransportControl_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 5),
    _AutocallIpxTransportControl_Type()
)
autocallIpxTransportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxTransportControl.setStatus("mandatory")


class _AutocallIpxIsdn_Type(DisplayString):
    """Custom type autocallIpxIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallIpxIsdn_Type.__name__ = "DisplayString"
_AutocallIpxIsdn_Object = MibTableColumn
autocallIpxIsdn = _AutocallIpxIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 6),
    _AutocallIpxIsdn_Type()
)
autocallIpxIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxIsdn.setStatus("mandatory")


class _AutocallIpxBumpable_Type(Integer32):
    """Custom type autocallIpxBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxBumpable_Type.__name__ = "Integer32"
_AutocallIpxBumpable_Object = MibTableColumn
autocallIpxBumpable = _AutocallIpxBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 7),
    _AutocallIpxBumpable_Type()
)
autocallIpxBumpable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxBumpable.setStatus("mandatory")
_AutocallIpxIdle_Type = Integer32
_AutocallIpxIdle_Object = MibTableColumn
autocallIpxIdle = _AutocallIpxIdle_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 8),
    _AutocallIpxIdle_Type()
)
autocallIpxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxIdle.setStatus("mandatory")


class _AutocallIpxIdleThreshold_Type(Integer32):
    """Custom type autocallIpxIdleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AutocallIpxIdleThreshold_Type.__name__ = "Integer32"
_AutocallIpxIdleThreshold_Object = MibTableColumn
autocallIpxIdleThreshold = _AutocallIpxIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 9),
    _AutocallIpxIdleThreshold_Type()
)
autocallIpxIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxIdleThreshold.setStatus("mandatory")


class _AutocallIpxDefault_Type(Integer32):
    """Custom type autocallIpxDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxDefault_Type.__name__ = "Integer32"
_AutocallIpxDefault_Object = MibTableColumn
autocallIpxDefault = _AutocallIpxDefault_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 10),
    _AutocallIpxDefault_Type()
)
autocallIpxDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxDefault.setStatus("mandatory")


class _AutocallIpxFrameType_Type(Integer32):
    """Custom type autocallIpxFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("etherII", 1),
          ("ieee8022", 2),
          ("ieee8023", 3),
          ("snap", 4))
    )


_AutocallIpxFrameType_Type.__name__ = "Integer32"
_AutocallIpxFrameType_Object = MibTableColumn
autocallIpxFrameType = _AutocallIpxFrameType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 11),
    _AutocallIpxFrameType_Type()
)
autocallIpxFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxFrameType.setStatus("mandatory")


class _AutocallIpxPpp_Type(Integer32):
    """Custom type autocallIpxPpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxPpp_Type.__name__ = "Integer32"
_AutocallIpxPpp_Object = MibTableColumn
autocallIpxPpp = _AutocallIpxPpp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 12),
    _AutocallIpxPpp_Type()
)
autocallIpxPpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxPpp.setStatus("mandatory")


class _AutocallIpxIsdnType_Type(Integer32):
    """Custom type autocallIpxIsdnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 2),
          ("sync", 1))
    )


_AutocallIpxIsdnType_Type.__name__ = "Integer32"
_AutocallIpxIsdnType_Object = MibTableColumn
autocallIpxIsdnType = _AutocallIpxIsdnType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 13),
    _AutocallIpxIsdnType_Type()
)
autocallIpxIsdnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxIsdnType.setStatus("mandatory")


class _AutocallIpxMode_Type(Integer32):
    """Custom type autocallIpxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallIpxMode_Type.__name__ = "Integer32"
_AutocallIpxMode_Object = MibTableColumn
autocallIpxMode = _AutocallIpxMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 5, 1, 14),
    _AutocallIpxMode_Type()
)
autocallIpxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxMode.setStatus("mandatory")
_AutocallIpxRipTable_Object = MibTable
autocallIpxRipTable = _AutocallIpxRipTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    autocallIpxRipTable.setStatus("mandatory")
_AutocallIpxRipEntry_Object = MibTableRow
autocallIpxRipEntry = _AutocallIpxRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1)
)
autocallIpxRipEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallIpxRipIndex"),
)
if mibBuilder.loadTexts:
    autocallIpxRipEntry.setStatus("mandatory")


class _AutocallIpxRipIndex_Type(OctetString):
    """Custom type autocallIpxRipIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallIpxRipIndex_Type.__name__ = "OctetString"
_AutocallIpxRipIndex_Object = MibTableColumn
autocallIpxRipIndex = _AutocallIpxRipIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 1),
    _AutocallIpxRipIndex_Type()
)
autocallIpxRipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallIpxRipIndex.setStatus("mandatory")


class _AutocallIpxRipNetwork_Type(OctetString):
    """Custom type autocallIpxRipNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AutocallIpxRipNetwork_Type.__name__ = "OctetString"
_AutocallIpxRipNetwork_Object = MibTableColumn
autocallIpxRipNetwork = _AutocallIpxRipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 2),
    _AutocallIpxRipNetwork_Type()
)
autocallIpxRipNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipNetwork.setStatus("mandatory")


class _AutocallIpxRipHops_Type(Integer32):
    """Custom type autocallIpxRipHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AutocallIpxRipHops_Type.__name__ = "Integer32"
_AutocallIpxRipHops_Object = MibTableColumn
autocallIpxRipHops = _AutocallIpxRipHops_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 3),
    _AutocallIpxRipHops_Type()
)
autocallIpxRipHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipHops.setStatus("mandatory")
_AutocallIpxRipTicks_Type = Integer32
_AutocallIpxRipTicks_Object = MibTableColumn
autocallIpxRipTicks = _AutocallIpxRipTicks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 4),
    _AutocallIpxRipTicks_Type()
)
autocallIpxRipTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipTicks.setStatus("mandatory")
_AutocallIpxRipNode_Type = MacAddress
_AutocallIpxRipNode_Object = MibTableColumn
autocallIpxRipNode = _AutocallIpxRipNode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 5),
    _AutocallIpxRipNode_Type()
)
autocallIpxRipNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipNode.setStatus("mandatory")


class _AutocallIpxRipIsdn_Type(DisplayString):
    """Custom type autocallIpxRipIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallIpxRipIsdn_Type.__name__ = "DisplayString"
_AutocallIpxRipIsdn_Object = MibTableColumn
autocallIpxRipIsdn = _AutocallIpxRipIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 6),
    _AutocallIpxRipIsdn_Type()
)
autocallIpxRipIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipIsdn.setStatus("mandatory")


class _AutocallIpxRipFrameType_Type(Integer32):
    """Custom type autocallIpxRipFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("etherII", 1),
          ("ieee8022", 2),
          ("ieee8023", 3),
          ("snap", 4))
    )


_AutocallIpxRipFrameType_Type.__name__ = "Integer32"
_AutocallIpxRipFrameType_Object = MibTableColumn
autocallIpxRipFrameType = _AutocallIpxRipFrameType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 7),
    _AutocallIpxRipFrameType_Type()
)
autocallIpxRipFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipFrameType.setStatus("mandatory")


class _AutocallIpxRipDirectNetwork_Type(OctetString):
    """Custom type autocallIpxRipDirectNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AutocallIpxRipDirectNetwork_Type.__name__ = "OctetString"
_AutocallIpxRipDirectNetwork_Object = MibTableColumn
autocallIpxRipDirectNetwork = _AutocallIpxRipDirectNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 8),
    _AutocallIpxRipDirectNetwork_Type()
)
autocallIpxRipDirectNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipDirectNetwork.setStatus("mandatory")
_AutocallIpxRipRouterMac_Type = MacAddress
_AutocallIpxRipRouterMac_Object = MibTableColumn
autocallIpxRipRouterMac = _AutocallIpxRipRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 9),
    _AutocallIpxRipRouterMac_Type()
)
autocallIpxRipRouterMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipRouterMac.setStatus("mandatory")
_AutocallIpxRipLinkTicks_Type = Integer32
_AutocallIpxRipLinkTicks_Object = MibTableColumn
autocallIpxRipLinkTicks = _AutocallIpxRipLinkTicks_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 10),
    _AutocallIpxRipLinkTicks_Type()
)
autocallIpxRipLinkTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipLinkTicks.setStatus("mandatory")


class _AutocallIpxRipPpp_Type(Integer32):
    """Custom type autocallIpxRipPpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallIpxRipPpp_Type.__name__ = "Integer32"
_AutocallIpxRipPpp_Object = MibTableColumn
autocallIpxRipPpp = _AutocallIpxRipPpp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 11),
    _AutocallIpxRipPpp_Type()
)
autocallIpxRipPpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipPpp.setStatus("mandatory")


class _AutocallIpxRipIsdnType_Type(Integer32):
    """Custom type autocallIpxRipIsdnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 2),
          ("sync", 1))
    )


_AutocallIpxRipIsdnType_Type.__name__ = "Integer32"
_AutocallIpxRipIsdnType_Object = MibTableColumn
autocallIpxRipIsdnType = _AutocallIpxRipIsdnType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 12),
    _AutocallIpxRipIsdnType_Type()
)
autocallIpxRipIsdnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipIsdnType.setStatus("mandatory")


class _AutocallIpxRipMode_Type(Integer32):
    """Custom type autocallIpxRipMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallIpxRipMode_Type.__name__ = "Integer32"
_AutocallIpxRipMode_Object = MibTableColumn
autocallIpxRipMode = _AutocallIpxRipMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 6, 1, 13),
    _AutocallIpxRipMode_Type()
)
autocallIpxRipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallIpxRipMode.setStatus("mandatory")
_AutocallDialTable_Object = MibTable
autocallDialTable = _AutocallDialTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    autocallDialTable.setStatus("mandatory")
_AutocallDialEntry_Object = MibTableRow
autocallDialEntry = _AutocallDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1)
)
autocallDialEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "autocallDialIndex"),
)
if mibBuilder.loadTexts:
    autocallDialEntry.setStatus("mandatory")


class _AutocallDialIndex_Type(OctetString):
    """Custom type autocallDialIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AutocallDialIndex_Type.__name__ = "OctetString"
_AutocallDialIndex_Object = MibTableColumn
autocallDialIndex = _AutocallDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 1),
    _AutocallDialIndex_Type()
)
autocallDialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autocallDialIndex.setStatus("mandatory")


class _AutocallDialCli_Type(DisplayString):
    """Custom type autocallDialCli based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallDialCli_Type.__name__ = "DisplayString"
_AutocallDialCli_Object = MibTableColumn
autocallDialCli = _AutocallDialCli_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 2),
    _AutocallDialCli_Type()
)
autocallDialCli.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialCli.setStatus("mandatory")


class _AutocallDialIsdn_Type(DisplayString):
    """Custom type autocallDialIsdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AutocallDialIsdn_Type.__name__ = "DisplayString"
_AutocallDialIsdn_Object = MibTableColumn
autocallDialIsdn = _AutocallDialIsdn_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 3),
    _AutocallDialIsdn_Type()
)
autocallDialIsdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialIsdn.setStatus("mandatory")


class _AutocallDialBumpable_Type(Integer32):
    """Custom type autocallDialBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AutocallDialBumpable_Type.__name__ = "Integer32"
_AutocallDialBumpable_Object = MibTableColumn
autocallDialBumpable = _AutocallDialBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 4),
    _AutocallDialBumpable_Type()
)
autocallDialBumpable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialBumpable.setStatus("mandatory")
_AutocallDialIdle_Type = Integer32
_AutocallDialIdle_Object = MibTableColumn
autocallDialIdle = _AutocallDialIdle_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 5),
    _AutocallDialIdle_Type()
)
autocallDialIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialIdle.setStatus("mandatory")


class _AutocallDialIdleThreshold_Type(Integer32):
    """Custom type autocallDialIdleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AutocallDialIdleThreshold_Type.__name__ = "Integer32"
_AutocallDialIdleThreshold_Object = MibTableColumn
autocallDialIdleThreshold = _AutocallDialIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 6),
    _AutocallDialIdleThreshold_Type()
)
autocallDialIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialIdleThreshold.setStatus("mandatory")


class _AutocallDialMode_Type(Integer32):
    """Custom type autocallDialMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 4))
    )


_AutocallDialMode_Type.__name__ = "Integer32"
_AutocallDialMode_Object = MibTableColumn
autocallDialMode = _AutocallDialMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 1, 7, 1, 7),
    _AutocallDialMode_Type()
)
autocallDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autocallDialMode.setStatus("mandatory")
_Isdnbands_ObjectIdentity = ObjectIdentity
isdnbands = _Isdnbands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2)
)
_IsdnbandsTable_Object = MibTable
isdnbandsTable = _IsdnbandsTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    isdnbandsTable.setStatus("mandatory")
_IsdnbandsEntry_Object = MibTableRow
isdnbandsEntry = _IsdnbandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1)
)
isdnbandsEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnbandsIndex"),
)
if mibBuilder.loadTexts:
    isdnbandsEntry.setStatus("mandatory")
_IsdnbandsIndex_Type = Integer32
_IsdnbandsIndex_Object = MibTableColumn
isdnbandsIndex = _IsdnbandsIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 1),
    _IsdnbandsIndex_Type()
)
isdnbandsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsIndex.setStatus("mandatory")


class _IsdnbandsName_Type(DisplayString):
    """Custom type isdnbandsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IsdnbandsName_Type.__name__ = "DisplayString"
_IsdnbandsName_Object = MibTableColumn
isdnbandsName = _IsdnbandsName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 2),
    _IsdnbandsName_Type()
)
isdnbandsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsName.setStatus("mandatory")


class _IsdnbandsStarttime_Type(Integer32):
    """Custom type isdnbandsStarttime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_IsdnbandsStarttime_Type.__name__ = "Integer32"
_IsdnbandsStarttime_Object = MibTableColumn
isdnbandsStarttime = _IsdnbandsStarttime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 3),
    _IsdnbandsStarttime_Type()
)
isdnbandsStarttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsStarttime.setStatus("mandatory")


class _IsdnbandsEndtime_Type(Integer32):
    """Custom type isdnbandsEndtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_IsdnbandsEndtime_Type.__name__ = "Integer32"
_IsdnbandsEndtime_Object = MibTableColumn
isdnbandsEndtime = _IsdnbandsEndtime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 4),
    _IsdnbandsEndtime_Type()
)
isdnbandsEndtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsEndtime.setStatus("mandatory")
_IsdnbandsDays_Type = DisplayString
_IsdnbandsDays_Object = MibTableColumn
isdnbandsDays = _IsdnbandsDays_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 5),
    _IsdnbandsDays_Type()
)
isdnbandsDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsDays.setStatus("mandatory")


class _IsdnbandsAllowbackup_Type(Integer32):
    """Custom type isdnbandsAllowbackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnbandsAllowbackup_Type.__name__ = "Integer32"
_IsdnbandsAllowbackup_Object = MibTableColumn
isdnbandsAllowbackup = _IsdnbandsAllowbackup_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 6),
    _IsdnbandsAllowbackup_Type()
)
isdnbandsAllowbackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsAllowbackup.setStatus("mandatory")


class _IsdnbandsAllowdemand_Type(Integer32):
    """Custom type isdnbandsAllowdemand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnbandsAllowdemand_Type.__name__ = "Integer32"
_IsdnbandsAllowdemand_Object = MibTableColumn
isdnbandsAllowdemand = _IsdnbandsAllowdemand_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 7),
    _IsdnbandsAllowdemand_Type()
)
isdnbandsAllowdemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsAllowdemand.setStatus("mandatory")


class _IsdnbandsAllowautocall_Type(Integer32):
    """Custom type isdnbandsAllowautocall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnbandsAllowautocall_Type.__name__ = "Integer32"
_IsdnbandsAllowautocall_Object = MibTableColumn
isdnbandsAllowautocall = _IsdnbandsAllowautocall_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 8),
    _IsdnbandsAllowautocall_Type()
)
isdnbandsAllowautocall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsAllowautocall.setStatus("mandatory")


class _IsdnbandsAllowlist_Type(Integer32):
    """Custom type isdnbandsAllowlist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnbandsAllowlist_Type.__name__ = "Integer32"
_IsdnbandsAllowlist_Object = MibTableColumn
isdnbandsAllowlist = _IsdnbandsAllowlist_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 9),
    _IsdnbandsAllowlist_Type()
)
isdnbandsAllowlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsAllowlist.setStatus("mandatory")


class _IsdnbandsMode_Type(Integer32):
    """Custom type isdnbandsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 0))
    )


_IsdnbandsMode_Type.__name__ = "Integer32"
_IsdnbandsMode_Object = MibTableColumn
isdnbandsMode = _IsdnbandsMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 1, 1, 12),
    _IsdnbandsMode_Type()
)
isdnbandsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsMode.setStatus("mandatory")
_IsdnbandsBridgeListTable_Object = MibTable
isdnbandsBridgeListTable = _IsdnbandsBridgeListTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    isdnbandsBridgeListTable.setStatus("mandatory")
_IsdnbandsBridgeListEntry_Object = MibTableRow
isdnbandsBridgeListEntry = _IsdnbandsBridgeListEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 2, 1)
)
isdnbandsBridgeListEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnbandsBridgeListIndex"),
)
if mibBuilder.loadTexts:
    isdnbandsBridgeListEntry.setStatus("mandatory")
_IsdnbandsBridgeListIndex_Type = Integer32
_IsdnbandsBridgeListIndex_Object = MibTableColumn
isdnbandsBridgeListIndex = _IsdnbandsBridgeListIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 2, 1, 1),
    _IsdnbandsBridgeListIndex_Type()
)
isdnbandsBridgeListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsBridgeListIndex.setStatus("mandatory")


class _IsdnbandsBridgeListBandName_Type(DisplayString):
    """Custom type isdnbandsBridgeListBandName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IsdnbandsBridgeListBandName_Type.__name__ = "DisplayString"
_IsdnbandsBridgeListBandName_Object = MibTableColumn
isdnbandsBridgeListBandName = _IsdnbandsBridgeListBandName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 2, 1, 2),
    _IsdnbandsBridgeListBandName_Type()
)
isdnbandsBridgeListBandName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsBridgeListBandName.setStatus("mandatory")


class _IsdnbandsBridgeListBridgeName_Type(DisplayString):
    """Custom type isdnbandsBridgeListBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IsdnbandsBridgeListBridgeName_Type.__name__ = "DisplayString"
_IsdnbandsBridgeListBridgeName_Object = MibTableColumn
isdnbandsBridgeListBridgeName = _IsdnbandsBridgeListBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 2, 2, 1, 3),
    _IsdnbandsBridgeListBridgeName_Type()
)
isdnbandsBridgeListBridgeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnbandsBridgeListBridgeName.setStatus("mandatory")
_Isdnnumbers_ObjectIdentity = ObjectIdentity
isdnnumbers = _Isdnnumbers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3)
)
_IsdnnumbersTable_Object = MibTable
isdnnumbersTable = _IsdnnumbersTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    isdnnumbersTable.setStatus("mandatory")
_IsdnnumbersEntry_Object = MibTableRow
isdnnumbersEntry = _IsdnnumbersEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1)
)
isdnnumbersEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnnumbersIndex"),
)
if mibBuilder.loadTexts:
    isdnnumbersEntry.setStatus("mandatory")


class _IsdnnumbersIndex_Type(OctetString):
    """Custom type isdnnumbersIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IsdnnumbersIndex_Type.__name__ = "OctetString"
_IsdnnumbersIndex_Object = MibTableColumn
isdnnumbersIndex = _IsdnnumbersIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 1),
    _IsdnnumbersIndex_Type()
)
isdnnumbersIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIndex.setStatus("mandatory")


class _IsdnnumbersName_Type(DisplayString):
    """Custom type isdnnumbersName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IsdnnumbersName_Type.__name__ = "DisplayString"
_IsdnnumbersName_Object = MibTableColumn
isdnnumbersName = _IsdnnumbersName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 2),
    _IsdnnumbersName_Type()
)
isdnnumbersName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersName.setStatus("mandatory")


class _IsdnnumbersNumber1_Type(DisplayString):
    """Custom type isdnnumbersNumber1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnnumbersNumber1_Type.__name__ = "DisplayString"
_IsdnnumbersNumber1_Object = MibTableColumn
isdnnumbersNumber1 = _IsdnnumbersNumber1_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 3),
    _IsdnnumbersNumber1_Type()
)
isdnnumbersNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersNumber1.setStatus("mandatory")


class _IsdnnumbersNumber2_Type(DisplayString):
    """Custom type isdnnumbersNumber2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnnumbersNumber2_Type.__name__ = "DisplayString"
_IsdnnumbersNumber2_Object = MibTableColumn
isdnnumbersNumber2 = _IsdnnumbersNumber2_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 4),
    _IsdnnumbersNumber2_Type()
)
isdnnumbersNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersNumber2.setStatus("mandatory")


class _IsdnnumbersNumber3_Type(DisplayString):
    """Custom type isdnnumbersNumber3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnnumbersNumber3_Type.__name__ = "DisplayString"
_IsdnnumbersNumber3_Object = MibTableColumn
isdnnumbersNumber3 = _IsdnnumbersNumber3_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 5),
    _IsdnnumbersNumber3_Type()
)
isdnnumbersNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersNumber3.setStatus("mandatory")


class _IsdnnumbersNumber4_Type(DisplayString):
    """Custom type isdnnumbersNumber4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnnumbersNumber4_Type.__name__ = "DisplayString"
_IsdnnumbersNumber4_Object = MibTableColumn
isdnnumbersNumber4 = _IsdnnumbersNumber4_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 6),
    _IsdnnumbersNumber4_Type()
)
isdnnumbersNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnnumbersNumber4.setStatus("mandatory")


class _IsdnnumbersCall_Type(Integer32):
    """Custom type isdnnumbersCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 2),
          ("false", 0),
          ("request", 1))
    )


_IsdnnumbersCall_Type.__name__ = "Integer32"
_IsdnnumbersCall_Object = MibTableColumn
isdnnumbersCall = _IsdnnumbersCall_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 7),
    _IsdnnumbersCall_Type()
)
isdnnumbersCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersCall.setStatus("mandatory")


class _IsdnnumbersTesttime_Type(Integer32):
    """Custom type isdnnumbersTesttime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_IsdnnumbersTesttime_Type.__name__ = "Integer32"
_IsdnnumbersTesttime_Object = MibTableColumn
isdnnumbersTesttime = _IsdnnumbersTesttime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 8),
    _IsdnnumbersTesttime_Type()
)
isdnnumbersTesttime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersTesttime.setStatus("mandatory")
_IsdnnumbersDays_Type = DisplayString
_IsdnnumbersDays_Object = MibTableColumn
isdnnumbersDays = _IsdnnumbersDays_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 9),
    _IsdnnumbersDays_Type()
)
isdnnumbersDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersDays.setStatus("mandatory")
_IsdnnumbersLasttest_Type = DisplayString
_IsdnnumbersLasttest_Object = MibTableColumn
isdnnumbersLasttest = _IsdnnumbersLasttest_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 10),
    _IsdnnumbersLasttest_Type()
)
isdnnumbersLasttest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnnumbersLasttest.setStatus("mandatory")
_IsdnnumbersIpAddress_Type = IpAddress
_IsdnnumbersIpAddress_Object = MibTableColumn
isdnnumbersIpAddress = _IsdnnumbersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 11),
    _IsdnnumbersIpAddress_Type()
)
isdnnumbersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIpAddress.setStatus("mandatory")
_IsdnnumbersIpMask_Type = IpAddress
_IsdnnumbersIpMask_Object = MibTableColumn
isdnnumbersIpMask = _IsdnnumbersIpMask_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 12),
    _IsdnnumbersIpMask_Type()
)
isdnnumbersIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIpMask.setStatus("mandatory")
_IsdnnumbersIpMetric_Type = Integer32
_IsdnnumbersIpMetric_Object = MibTableColumn
isdnnumbersIpMetric = _IsdnnumbersIpMetric_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 13),
    _IsdnnumbersIpMetric_Type()
)
isdnnumbersIpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIpMetric.setStatus("mandatory")


class _IsdnnumbersIpxNetwork_Type(OctetString):
    """Custom type isdnnumbersIpxNetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IsdnnumbersIpxNetwork_Type.__name__ = "OctetString"
_IsdnnumbersIpxNetwork_Object = MibTableColumn
isdnnumbersIpxNetwork = _IsdnnumbersIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 14),
    _IsdnnumbersIpxNetwork_Type()
)
isdnnumbersIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIpxNetwork.setStatus("mandatory")


class _IsdnnumbersIpxType_Type(Integer32):
    """Custom type isdnnumbersIpxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee802dot2", 2),
          ("novell802dot3", 3),
          ("snap", 4))
    )


_IsdnnumbersIpxType_Type.__name__ = "Integer32"
_IsdnnumbersIpxType_Object = MibTableColumn
isdnnumbersIpxType = _IsdnnumbersIpxType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 15),
    _IsdnnumbersIpxType_Type()
)
isdnnumbersIpxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersIpxType.setStatus("mandatory")


class _IsdnnumbersPpp_Type(Integer32):
    """Custom type isdnnumbersPpp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_IsdnnumbersPpp_Type.__name__ = "Integer32"
_IsdnnumbersPpp_Object = MibTableColumn
isdnnumbersPpp = _IsdnnumbersPpp_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 16),
    _IsdnnumbersPpp_Type()
)
isdnnumbersPpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersPpp.setStatus("mandatory")
_IsdnnumbersRemoteIpAddress_Type = IpAddress
_IsdnnumbersRemoteIpAddress_Object = MibTableColumn
isdnnumbersRemoteIpAddress = _IsdnnumbersRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 17),
    _IsdnnumbersRemoteIpAddress_Type()
)
isdnnumbersRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersRemoteIpAddress.setStatus("mandatory")


class _IsdnnumbersRemoteUnitType_Type(Integer32):
    """Custom type isdnnumbersRemoteUnitType based on Integer32"""
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
        *(("any", 1),
          ("ascend", 4),
          ("cisco", 3),
          ("n3com", 2),
          ("spider", 5))
    )


_IsdnnumbersRemoteUnitType_Type.__name__ = "Integer32"
_IsdnnumbersRemoteUnitType_Object = MibTableColumn
isdnnumbersRemoteUnitType = _IsdnnumbersRemoteUnitType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 18),
    _IsdnnumbersRemoteUnitType_Type()
)
isdnnumbersRemoteUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersRemoteUnitType.setStatus("mandatory")


class _IsdnnumbersHdlcType_Type(Integer32):
    """Custom type isdnnumbersHdlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lapb", 2),
          ("synchronous", 1))
    )


_IsdnnumbersHdlcType_Type.__name__ = "Integer32"
_IsdnnumbersHdlcType_Object = MibTableColumn
isdnnumbersHdlcType = _IsdnnumbersHdlcType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 19),
    _IsdnnumbersHdlcType_Type()
)
isdnnumbersHdlcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersHdlcType.setStatus("mandatory")


class _IsdnnumbersPppAuthentication_Type(Integer32):
    """Custom type isdnnumbersPppAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_IsdnnumbersPppAuthentication_Type.__name__ = "Integer32"
_IsdnnumbersPppAuthentication_Object = MibTableColumn
isdnnumbersPppAuthentication = _IsdnnumbersPppAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 20),
    _IsdnnumbersPppAuthentication_Type()
)
isdnnumbersPppAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnnumbersPppAuthentication.setStatus("mandatory")
_IsdnnumbersMaxCircuits_Type = Integer32
_IsdnnumbersMaxCircuits_Object = MibTableColumn
isdnnumbersMaxCircuits = _IsdnnumbersMaxCircuits_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 21),
    _IsdnnumbersMaxCircuits_Type()
)
isdnnumbersMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersMaxCircuits.setStatus("mandatory")


class _IsdnnumbersMPEnable_Type(Integer32):
    """Custom type isdnnumbersMPEnable based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-bacp", 4),
          ("enabled-short", 3),
          ("enabled-short-bacp", 5))
    )


_IsdnnumbersMPEnable_Type.__name__ = "Integer32"
_IsdnnumbersMPEnable_Object = MibTableColumn
isdnnumbersMPEnable = _IsdnnumbersMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 22),
    _IsdnnumbersMPEnable_Type()
)
isdnnumbersMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersMPEnable.setStatus("mandatory")


class _IsdnnumbersLearntED_Type(DisplayString):
    """Custom type isdnnumbersLearntED based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IsdnnumbersLearntED_Type.__name__ = "DisplayString"
_IsdnnumbersLearntED_Object = MibTableColumn
isdnnumbersLearntED = _IsdnnumbersLearntED_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 23),
    _IsdnnumbersLearntED_Type()
)
isdnnumbersLearntED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnnumbersLearntED.setStatus("mandatory")


class _IsdnnumbersMode_Type(Integer32):
    """Custom type isdnnumbersMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 0))
    )


_IsdnnumbersMode_Type.__name__ = "Integer32"
_IsdnnumbersMode_Object = MibTableColumn
isdnnumbersMode = _IsdnnumbersMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 24),
    _IsdnnumbersMode_Type()
)
isdnnumbersMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersMode.setStatus("mandatory")


class _IsdnnumbersCallType1_Type(Integer32):
    """Custom type isdnnumbersCallType1 based on Integer32"""
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
        *(("restricted", 1),
          ("speech", 3),
          ("unrestricted", 0),
          ("v110", 2))
    )


_IsdnnumbersCallType1_Type.__name__ = "Integer32"
_IsdnnumbersCallType1_Object = MibTableColumn
isdnnumbersCallType1 = _IsdnnumbersCallType1_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 25),
    _IsdnnumbersCallType1_Type()
)
isdnnumbersCallType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersCallType1.setStatus("mandatory")


class _IsdnnumbersCallType2_Type(Integer32):
    """Custom type isdnnumbersCallType2 based on Integer32"""
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
        *(("restricted", 1),
          ("speech", 3),
          ("unrestricted", 0),
          ("v110", 2))
    )


_IsdnnumbersCallType2_Type.__name__ = "Integer32"
_IsdnnumbersCallType2_Object = MibTableColumn
isdnnumbersCallType2 = _IsdnnumbersCallType2_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 26),
    _IsdnnumbersCallType2_Type()
)
isdnnumbersCallType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersCallType2.setStatus("mandatory")


class _IsdnnumbersCallType3_Type(Integer32):
    """Custom type isdnnumbersCallType3 based on Integer32"""
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
        *(("restricted", 1),
          ("speech", 3),
          ("unrestricted", 0),
          ("v110", 2))
    )


_IsdnnumbersCallType3_Type.__name__ = "Integer32"
_IsdnnumbersCallType3_Object = MibTableColumn
isdnnumbersCallType3 = _IsdnnumbersCallType3_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 27),
    _IsdnnumbersCallType3_Type()
)
isdnnumbersCallType3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersCallType3.setStatus("mandatory")


class _IsdnnumbersCallType4_Type(Integer32):
    """Custom type isdnnumbersCallType4 based on Integer32"""
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
        *(("restricted", 1),
          ("speech", 3),
          ("unrestricted", 0),
          ("v110", 2))
    )


_IsdnnumbersCallType4_Type.__name__ = "Integer32"
_IsdnnumbersCallType4_Object = MibTableColumn
isdnnumbersCallType4 = _IsdnnumbersCallType4_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 3, 1, 1, 28),
    _IsdnnumbersCallType4_Type()
)
isdnnumbersCallType4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnnumbersCallType4.setStatus("mandatory")
_Isdnports_ObjectIdentity = ObjectIdentity
isdnports = _Isdnports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4)
)
_IsdnportsTable_Object = MibTable
isdnportsTable = _IsdnportsTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    isdnportsTable.setStatus("mandatory")
_IsdnportsEntry_Object = MibTableRow
isdnportsEntry = _IsdnportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1)
)
isdnportsEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnportsIndex"),
)
if mibBuilder.loadTexts:
    isdnportsEntry.setStatus("mandatory")
_IsdnportsIndex_Type = Integer32
_IsdnportsIndex_Object = MibTableColumn
isdnportsIndex = _IsdnportsIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 1),
    _IsdnportsIndex_Type()
)
isdnportsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsIndex.setStatus("mandatory")


class _IsdnportsDestination_Type(DisplayString):
    """Custom type isdnportsDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnportsDestination_Type.__name__ = "DisplayString"
_IsdnportsDestination_Object = MibTableColumn
isdnportsDestination = _IsdnportsDestination_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 2),
    _IsdnportsDestination_Type()
)
isdnportsDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsDestination.setStatus("mandatory")


class _IsdnportsState_Type(Integer32):
    """Custom type isdnportsState based on Integer32"""
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
        *(("answered", 5),
          ("answering", 4),
          ("calling", 1),
          ("connected", 3),
          ("idle", 0),
          ("ringing", 2))
    )


_IsdnportsState_Type.__name__ = "Integer32"
_IsdnportsState_Object = MibTableColumn
isdnportsState = _IsdnportsState_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 3),
    _IsdnportsState_Type()
)
isdnportsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsState.setStatus("mandatory")
_IsdnportsConnTime_Type = TimeTicks
_IsdnportsConnTime_Object = MibTableColumn
isdnportsConnTime = _IsdnportsConnTime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 4),
    _IsdnportsConnTime_Type()
)
isdnportsConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsConnTime.setStatus("mandatory")


class _IsdnportsBackup_Type(Integer32):
    """Custom type isdnportsBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnportsBackup_Type.__name__ = "Integer32"
_IsdnportsBackup_Object = MibTableColumn
isdnportsBackup = _IsdnportsBackup_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 5),
    _IsdnportsBackup_Type()
)
isdnportsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsBackup.setStatus("mandatory")


class _IsdnportsDemand_Type(Integer32):
    """Custom type isdnportsDemand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnportsDemand_Type.__name__ = "Integer32"
_IsdnportsDemand_Object = MibTableColumn
isdnportsDemand = _IsdnportsDemand_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 6),
    _IsdnportsDemand_Type()
)
isdnportsDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsDemand.setStatus("mandatory")


class _IsdnportsBumpable_Type(Integer32):
    """Custom type isdnportsBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_IsdnportsBumpable_Type.__name__ = "Integer32"
_IsdnportsBumpable_Object = MibTableColumn
isdnportsBumpable = _IsdnportsBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 7),
    _IsdnportsBumpable_Type()
)
isdnportsBumpable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsBumpable.setStatus("mandatory")


class _IsdnportsAlert_Type(Integer32):
    """Custom type isdnportsAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("beep", 2),
          ("none", 0))
    )


_IsdnportsAlert_Type.__name__ = "Integer32"
_IsdnportsAlert_Object = MibTableColumn
isdnportsAlert = _IsdnportsAlert_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 8),
    _IsdnportsAlert_Type()
)
isdnportsAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsAlert.setStatus("mandatory")
_IsdnportsPriority_Type = Integer32
_IsdnportsPriority_Object = MibTableColumn
isdnportsPriority = _IsdnportsPriority_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 9),
    _IsdnportsPriority_Type()
)
isdnportsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsPriority.setStatus("mandatory")
_IsdnportsSourceMac_Type = MacAddress
_IsdnportsSourceMac_Object = MibTableColumn
isdnportsSourceMac = _IsdnportsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 4, 1, 1, 10),
    _IsdnportsSourceMac_Type()
)
isdnportsSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnportsSourceMac.setStatus("mandatory")
_Isdnhistory_ObjectIdentity = ObjectIdentity
isdnhistory = _Isdnhistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5)
)
_IsdnhistoryTable_Object = MibTable
isdnhistoryTable = _IsdnhistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1)
)
if mibBuilder.loadTexts:
    isdnhistoryTable.setStatus("mandatory")
_IsdnhistoryEntry_Object = MibTableRow
isdnhistoryEntry = _IsdnhistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1)
)
isdnhistoryEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnhistoryIndex"),
)
if mibBuilder.loadTexts:
    isdnhistoryEntry.setStatus("mandatory")
_IsdnhistoryIndex_Type = Integer32
_IsdnhistoryIndex_Object = MibTableColumn
isdnhistoryIndex = _IsdnhistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1, 1),
    _IsdnhistoryIndex_Type()
)
isdnhistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnhistoryIndex.setStatus("mandatory")


class _IsdnhistoryDestination_Type(DisplayString):
    """Custom type isdnhistoryDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_IsdnhistoryDestination_Type.__name__ = "DisplayString"
_IsdnhistoryDestination_Object = MibTableColumn
isdnhistoryDestination = _IsdnhistoryDestination_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1, 2),
    _IsdnhistoryDestination_Type()
)
isdnhistoryDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnhistoryDestination.setStatus("mandatory")
_IsdnhistoryTotalTime_Type = TimeTicks
_IsdnhistoryTotalTime_Object = MibTableColumn
isdnhistoryTotalTime = _IsdnhistoryTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1, 3),
    _IsdnhistoryTotalTime_Type()
)
isdnhistoryTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnhistoryTotalTime.setStatus("mandatory")
_IsdnhistoryTotalCalls_Type = Integer32
_IsdnhistoryTotalCalls_Object = MibTableColumn
isdnhistoryTotalCalls = _IsdnhistoryTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1, 4),
    _IsdnhistoryTotalCalls_Type()
)
isdnhistoryTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnhistoryTotalCalls.setStatus("mandatory")
_IsdnhistoryFailedCalls_Type = Integer32
_IsdnhistoryFailedCalls_Object = MibTableColumn
isdnhistoryFailedCalls = _IsdnhistoryFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 5, 1, 1, 5),
    _IsdnhistoryFailedCalls_Type()
)
isdnhistoryFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnhistoryFailedCalls.setStatus("mandatory")
_Isdncla_ObjectIdentity = ObjectIdentity
isdncla = _Isdncla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6)
)
_IsdnCliTable_Object = MibTable
isdnCliTable = _IsdnCliTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6, 1)
)
if mibBuilder.loadTexts:
    isdnCliTable.setStatus("mandatory")
_IsdnCliEntry_Object = MibTableRow
isdnCliEntry = _IsdnCliEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6, 1, 1)
)
isdnCliEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnCliIndex"),
)
if mibBuilder.loadTexts:
    isdnCliEntry.setStatus("mandatory")
_IsdnCliIndex_Type = Integer32
_IsdnCliIndex_Object = MibTableColumn
isdnCliIndex = _IsdnCliIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6, 1, 1, 1),
    _IsdnCliIndex_Type()
)
isdnCliIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCliIndex.setStatus("mandatory")
_IsdnCliNumber_Type = DisplayString
_IsdnCliNumber_Object = MibTableColumn
isdnCliNumber = _IsdnCliNumber_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6, 1, 1, 2),
    _IsdnCliNumber_Type()
)
isdnCliNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCliNumber.setStatus("mandatory")


class _IsdnCliMode_Type(Integer32):
    """Custom type isdnCliMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("edit", 0))
    )


_IsdnCliMode_Type.__name__ = "Integer32"
_IsdnCliMode_Object = MibTableColumn
isdnCliMode = _IsdnCliMode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 6, 1, 1, 3),
    _IsdnCliMode_Type()
)
isdnCliMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCliMode.setStatus("mandatory")
_Isdnlists_ObjectIdentity = ObjectIdentity
isdnlists = _Isdnlists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7)
)
_IsdnlistsTable_Object = MibTable
isdnlistsTable = _IsdnlistsTable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    isdnlistsTable.setStatus("mandatory")
_IsdnlistsEntry_Object = MibTableRow
isdnlistsEntry = _IsdnlistsEntry_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7, 1, 1)
)
isdnlistsEntry.setIndexNames(
    (0, "REMOTEACCESS-MIB", "isdnlistsIndex"),
)
if mibBuilder.loadTexts:
    isdnlistsEntry.setStatus("mandatory")
_IsdnlistsIndex_Type = Integer32
_IsdnlistsIndex_Object = MibTableColumn
isdnlistsIndex = _IsdnlistsIndex_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7, 1, 1, 1),
    _IsdnlistsIndex_Type()
)
isdnlistsIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnlistsIndex.setStatus("mandatory")


class _IsdnlistsBand_Type(DisplayString):
    """Custom type isdnlistsBand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_IsdnlistsBand_Type.__name__ = "DisplayString"
_IsdnlistsBand_Object = MibTableColumn
isdnlistsBand = _IsdnlistsBand_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7, 1, 1, 2),
    _IsdnlistsBand_Type()
)
isdnlistsBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnlistsBand.setStatus("mandatory")


class _IsdnlistsName_Type(DisplayString):
    """Custom type isdnlistsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IsdnlistsName_Type.__name__ = "DisplayString"
_IsdnlistsName_Object = MibTableColumn
isdnlistsName = _IsdnlistsName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 7, 1, 1, 3),
    _IsdnlistsName_Type()
)
isdnlistsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnlistsName.setStatus("mandatory")
_IsdnParams_ObjectIdentity = ObjectIdentity
isdnParams = _IsdnParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8)
)


class _IsdnParamsNetworkType_Type(Integer32):
    """Custom type isdnParamsNetworkType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("att5essCustom", 3),
          ("australia", 5),
          ("etsi", 1),
          ("germany1tr6", 4),
          ("germanyD64S", 7),
          ("italy", 6),
          ("japan-ins64", 9),
          ("nationalIsdn1", 2),
          ("usa-dms100", 8))
    )


_IsdnParamsNetworkType_Type.__name__ = "Integer32"
_IsdnParamsNetworkType_Object = MibTableColumn
isdnParamsNetworkType = _IsdnParamsNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 1),
    _IsdnParamsNetworkType_Type()
)
isdnParamsNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsNetworkType.setStatus("mandatory")


class _IsdnParamsSpid1_Type(DisplayString):
    """Custom type isdnParamsSpid1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSpid1_Type.__name__ = "DisplayString"
_IsdnParamsSpid1_Object = MibTableColumn
isdnParamsSpid1 = _IsdnParamsSpid1_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 2),
    _IsdnParamsSpid1_Type()
)
isdnParamsSpid1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSpid1.setStatus("mandatory")


class _IsdnParamsSpid2_Type(DisplayString):
    """Custom type isdnParamsSpid2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSpid2_Type.__name__ = "DisplayString"
_IsdnParamsSpid2_Object = MibTableColumn
isdnParamsSpid2 = _IsdnParamsSpid2_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 3),
    _IsdnParamsSpid2_Type()
)
isdnParamsSpid2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSpid2.setStatus("mandatory")


class _IsdnParamsSpid3_Type(DisplayString):
    """Custom type isdnParamsSpid3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSpid3_Type.__name__ = "DisplayString"
_IsdnParamsSpid3_Object = MibTableColumn
isdnParamsSpid3 = _IsdnParamsSpid3_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 4),
    _IsdnParamsSpid3_Type()
)
isdnParamsSpid3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSpid3.setStatus("mandatory")


class _IsdnParamsSpid4_Type(DisplayString):
    """Custom type isdnParamsSpid4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSpid4_Type.__name__ = "DisplayString"
_IsdnParamsSpid4_Object = MibTableColumn
isdnParamsSpid4 = _IsdnParamsSpid4_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 5),
    _IsdnParamsSpid4_Type()
)
isdnParamsSpid4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSpid4.setStatus("mandatory")


class _IsdnParamsDirectoryNumber1_Type(DisplayString):
    """Custom type isdnParamsDirectoryNumber1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsDirectoryNumber1_Type.__name__ = "DisplayString"
_IsdnParamsDirectoryNumber1_Object = MibTableColumn
isdnParamsDirectoryNumber1 = _IsdnParamsDirectoryNumber1_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 6),
    _IsdnParamsDirectoryNumber1_Type()
)
isdnParamsDirectoryNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsDirectoryNumber1.setStatus("mandatory")


class _IsdnParamsDirectoryNumber2_Type(DisplayString):
    """Custom type isdnParamsDirectoryNumber2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsDirectoryNumber2_Type.__name__ = "DisplayString"
_IsdnParamsDirectoryNumber2_Object = MibTableColumn
isdnParamsDirectoryNumber2 = _IsdnParamsDirectoryNumber2_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 7),
    _IsdnParamsDirectoryNumber2_Type()
)
isdnParamsDirectoryNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsDirectoryNumber2.setStatus("mandatory")


class _IsdnParamsDirectoryNumber3_Type(DisplayString):
    """Custom type isdnParamsDirectoryNumber3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsDirectoryNumber3_Type.__name__ = "DisplayString"
_IsdnParamsDirectoryNumber3_Object = MibTableColumn
isdnParamsDirectoryNumber3 = _IsdnParamsDirectoryNumber3_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 8),
    _IsdnParamsDirectoryNumber3_Type()
)
isdnParamsDirectoryNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsDirectoryNumber3.setStatus("mandatory")


class _IsdnParamsDirectoryNumber4_Type(DisplayString):
    """Custom type isdnParamsDirectoryNumber4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsDirectoryNumber4_Type.__name__ = "DisplayString"
_IsdnParamsDirectoryNumber4_Object = MibTableColumn
isdnParamsDirectoryNumber4 = _IsdnParamsDirectoryNumber4_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 9),
    _IsdnParamsDirectoryNumber4_Type()
)
isdnParamsDirectoryNumber4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsDirectoryNumber4.setStatus("mandatory")


class _IsdnParamsReportBusy_Type(Integer32):
    """Custom type isdnParamsReportBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_IsdnParamsReportBusy_Type.__name__ = "Integer32"
_IsdnParamsReportBusy_Object = MibTableColumn
isdnParamsReportBusy = _IsdnParamsReportBusy_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 10),
    _IsdnParamsReportBusy_Type()
)
isdnParamsReportBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsReportBusy.setStatus("mandatory")


class _IsdnParamsIncomingDov_Type(Integer32):
    """Custom type isdnParamsIncomingDov based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("disable", 1))
    )


_IsdnParamsIncomingDov_Type.__name__ = "Integer32"
_IsdnParamsIncomingDov_Object = MibTableColumn
isdnParamsIncomingDov = _IsdnParamsIncomingDov_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 11),
    _IsdnParamsIncomingDov_Type()
)
isdnParamsIncomingDov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsIncomingDov.setStatus("mandatory")
_IsdnParamsMaxCallTime_Type = Integer32
_IsdnParamsMaxCallTime_Object = MibTableColumn
isdnParamsMaxCallTime = _IsdnParamsMaxCallTime_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 12),
    _IsdnParamsMaxCallTime_Type()
)
isdnParamsMaxCallTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsMaxCallTime.setStatus("mandatory")
_IsdnParamsMsn_ObjectIdentity = ObjectIdentity
isdnParamsMsn = _IsdnParamsMsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 13)
)


class _IsdnParamsMsnLan_Type(DisplayString):
    """Custom type isdnParamsMsnLan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsMsnLan_Type.__name__ = "DisplayString"
_IsdnParamsMsnLan_Object = MibTableColumn
isdnParamsMsnLan = _IsdnParamsMsnLan_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 13, 1),
    _IsdnParamsMsnLan_Type()
)
isdnParamsMsnLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsMsnLan.setStatus("mandatory")


class _IsdnParamsMsnVoice_Type(DisplayString):
    """Custom type isdnParamsMsnVoice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsMsnVoice_Type.__name__ = "DisplayString"
_IsdnParamsMsnVoice_Object = MibTableColumn
isdnParamsMsnVoice = _IsdnParamsMsnVoice_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 13, 2),
    _IsdnParamsMsnVoice_Type()
)
isdnParamsMsnVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsMsnVoice.setStatus("mandatory")


class _IsdnParamsMsnCheck_Type(Integer32):
    """Custom type isdnParamsMsnCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_IsdnParamsMsnCheck_Type.__name__ = "Integer32"
_IsdnParamsMsnCheck_Object = MibTableColumn
isdnParamsMsnCheck = _IsdnParamsMsnCheck_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 13, 3),
    _IsdnParamsMsnCheck_Type()
)
isdnParamsMsnCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsMsnCheck.setStatus("mandatory")


class _IsdnParamsMsnSend_Type(Integer32):
    """Custom type isdnParamsMsnSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_IsdnParamsMsnSend_Type.__name__ = "Integer32"
_IsdnParamsMsnSend_Object = MibTableColumn
isdnParamsMsnSend = _IsdnParamsMsnSend_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 13, 4),
    _IsdnParamsMsnSend_Type()
)
isdnParamsMsnSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsMsnSend.setStatus("mandatory")
_IsdnParamsSubAddr_ObjectIdentity = ObjectIdentity
isdnParamsSubAddr = _IsdnParamsSubAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14)
)


class _IsdnParamsSubAddrLan_Type(DisplayString):
    """Custom type isdnParamsSubAddrLan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSubAddrLan_Type.__name__ = "DisplayString"
_IsdnParamsSubAddrLan_Object = MibTableColumn
isdnParamsSubAddrLan = _IsdnParamsSubAddrLan_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14, 1),
    _IsdnParamsSubAddrLan_Type()
)
isdnParamsSubAddrLan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSubAddrLan.setStatus("mandatory")


class _IsdnParamsSubAddrVoice_Type(DisplayString):
    """Custom type isdnParamsSubAddrVoice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_IsdnParamsSubAddrVoice_Type.__name__ = "DisplayString"
_IsdnParamsSubAddrVoice_Object = MibTableColumn
isdnParamsSubAddrVoice = _IsdnParamsSubAddrVoice_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14, 2),
    _IsdnParamsSubAddrVoice_Type()
)
isdnParamsSubAddrVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSubAddrVoice.setStatus("mandatory")


class _IsdnParamsSubAddrCheck_Type(Integer32):
    """Custom type isdnParamsSubAddrCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_IsdnParamsSubAddrCheck_Type.__name__ = "Integer32"
_IsdnParamsSubAddrCheck_Object = MibTableColumn
isdnParamsSubAddrCheck = _IsdnParamsSubAddrCheck_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14, 3),
    _IsdnParamsSubAddrCheck_Type()
)
isdnParamsSubAddrCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSubAddrCheck.setStatus("mandatory")


class _IsdnParamsSubAddrSend_Type(Integer32):
    """Custom type isdnParamsSubAddrSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_IsdnParamsSubAddrSend_Type.__name__ = "Integer32"
_IsdnParamsSubAddrSend_Object = MibTableColumn
isdnParamsSubAddrSend = _IsdnParamsSubAddrSend_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14, 4),
    _IsdnParamsSubAddrSend_Type()
)
isdnParamsSubAddrSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSubAddrSend.setStatus("mandatory")


class _IsdnParamsSubAddrType_Type(Integer32):
    """Custom type isdnParamsSubAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nsap", 1),
          ("user", 2))
    )


_IsdnParamsSubAddrType_Type.__name__ = "Integer32"
_IsdnParamsSubAddrType_Object = MibTableColumn
isdnParamsSubAddrType = _IsdnParamsSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 14, 5),
    _IsdnParamsSubAddrType_Type()
)
isdnParamsSubAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsSubAddrType.setStatus("mandatory")
_IsdnParamsTokenValue_Type = Integer32
_IsdnParamsTokenValue_Object = MibTableColumn
isdnParamsTokenValue = _IsdnParamsTokenValue_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 15),
    _IsdnParamsTokenValue_Type()
)
isdnParamsTokenValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsTokenValue.setStatus("mandatory")


class _IsdnParamsTokenRefill_Type(Integer32):
    """Custom type isdnParamsTokenRefill based on Integer32"""
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
        *(("auto", 2),
          ("disable", 0),
          ("manual", 1),
          ("refill", 3))
    )


_IsdnParamsTokenRefill_Type.__name__ = "Integer32"
_IsdnParamsTokenRefill_Object = MibTableColumn
isdnParamsTokenRefill = _IsdnParamsTokenRefill_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 16),
    _IsdnParamsTokenRefill_Type()
)
isdnParamsTokenRefill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnParamsTokenRefill.setStatus("mandatory")
_IsdnParamsTokenRemain_Type = Integer32
_IsdnParamsTokenRemain_Object = MibTableColumn
isdnParamsTokenRemain = _IsdnParamsTokenRemain_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 8, 17),
    _IsdnParamsTokenRemain_Type()
)
isdnParamsTokenRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnParamsTokenRemain.setStatus("mandatory")
_Bootp_ObjectIdentity = ObjectIdentity
bootp = _Bootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9)
)


class _BootpActive_Type(Integer32):
    """Custom type bootpActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BootpActive_Type.__name__ = "Integer32"
_BootpActive_Object = MibScalar
bootpActive = _BootpActive_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 1),
    _BootpActive_Type()
)
bootpActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpActive.setStatus("mandatory")


class _BootpBumpable_Type(Integer32):
    """Custom type bootpBumpable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_BootpBumpable_Type.__name__ = "Integer32"
_BootpBumpable_Object = MibScalar
bootpBumpable = _BootpBumpable_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 2),
    _BootpBumpable_Type()
)
bootpBumpable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpBumpable.setStatus("mandatory")
_BootpIdle_Type = Integer32
_BootpIdle_Object = MibScalar
bootpIdle = _BootpIdle_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 3),
    _BootpIdle_Type()
)
bootpIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIdle.setStatus("mandatory")


class _BootpIdleThreshold_Type(Integer32):
    """Custom type bootpIdleThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BootpIdleThreshold_Type.__name__ = "Integer32"
_BootpIdleThreshold_Object = MibScalar
bootpIdleThreshold = _BootpIdleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 4),
    _BootpIdleThreshold_Type()
)
bootpIdleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIdleThreshold.setStatus("mandatory")


class _BootpIsdnName_Type(DisplayString):
    """Custom type bootpIsdnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_BootpIsdnName_Type.__name__ = "DisplayString"
_BootpIsdnName_Object = MibScalar
bootpIsdnName = _BootpIsdnName_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 5),
    _BootpIsdnName_Type()
)
bootpIsdnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIsdnName.setStatus("mandatory")
_BootpAddress_Type = IpAddress
_BootpAddress_Object = MibScalar
bootpAddress = _BootpAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 6),
    _BootpAddress_Type()
)
bootpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpAddress.setStatus("mandatory")


class _BootpDelaySecs_Type(Integer32):
    """Custom type bootpDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_BootpDelaySecs_Type.__name__ = "Integer32"
_BootpDelaySecs_Object = MibScalar
bootpDelaySecs = _BootpDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 7),
    _BootpDelaySecs_Type()
)
bootpDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpDelaySecs.setStatus("mandatory")


class _DhcpProxyActive_Type(Integer32):
    """Custom type dhcpProxyActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_DhcpProxyActive_Type.__name__ = "Integer32"
_DhcpProxyActive_Object = MibScalar
dhcpProxyActive = _DhcpProxyActive_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 8),
    _DhcpProxyActive_Type()
)
dhcpProxyActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpProxyActive.setStatus("mandatory")
_ReferenceAddress_Type = IpAddress
_ReferenceAddress_Object = MibScalar
referenceAddress = _ReferenceAddress_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 9),
    _ReferenceAddress_Type()
)
referenceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    referenceAddress.setStatus("mandatory")
_MinPoolSize_Type = Integer32
_MinPoolSize_Object = MibScalar
minPoolSize = _MinPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 3, 4, 9, 10),
    _MinPoolSize_Type()
)
minPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minPoolSize.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 1)
)


class _AlarmCode_Type(Integer32):
    """Custom type alarmCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("failed", 1)
    )


_AlarmCode_Type.__name__ = "Integer32"
_AlarmCode_Object = MibScalar
alarmCode = _AlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 1, 1),
    _AlarmCode_Type()
)
alarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCode.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 1, 2),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("mandatory")
_IsdnFailCause_ObjectIdentity = ObjectIdentity
isdnFailCause = _IsdnFailCause_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 2)
)
_IsdnFailDestination_Type = DisplayString
_IsdnFailDestination_Object = MibScalar
isdnFailDestination = _IsdnFailDestination_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 2, 1),
    _IsdnFailDestination_Type()
)
isdnFailDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnFailDestination.setStatus("mandatory")


class _Q931FailCauseCode_Type(Integer32):
    """Custom type q931FailCauseCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              17,
              18,
              19,
              21,
              22,
              27,
              38,
              41,
              42,
              84,
              86,
              88,
              145)
        )
    )
    namedValues = NamedValues(
        *(("callIdentityInUse", 84),
          ("callRejected", 21),
          ("destinationOutOfOrder", 27),
          ("dlFailureLineBroken", 145),
          ("incompatibleDestination", 88),
          ("networkOutOfOrder", 38),
          ("noAnswerFromUser", 19),
          ("noUserResponding", 18),
          ("normalCallClearing", 16),
          ("numberChanged", 22),
          ("requestedCallIdentityCleared", 86),
          ("switchingEquipmentCongestion", 42),
          ("temporaryFailure", 41),
          ("unallocatedNumber", 1),
          ("userBusy", 17))
    )


_Q931FailCauseCode_Type.__name__ = "Integer32"
_Q931FailCauseCode_Object = MibScalar
q931FailCauseCode = _Q931FailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 2, 2),
    _Q931FailCauseCode_Type()
)
q931FailCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    q931FailCauseCode.setStatus("mandatory")


class _Dass2FailCauseCode_Type(Integer32):
    """Custom type dass2FailCauseCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              30,
              31,
              32,
              45,
              46,
              48)
        )
    )
    namedValues = NamedValues(
        *(("accessBarred", 11),
          ("cleared2", 2),
          ("cleared48", 48),
          ("lineOutOfService", 9),
          ("networkBusy", 7),
          ("noReply", 31),
          ("numberBusy", 8),
          ("numberIncomplete", 1),
          ("numberUnobtainable0", 0),
          ("numberUnobtainable10", 10),
          ("numberUnobtainable3", 3),
          ("numberUnobtainable30", 30),
          ("numberUnobtainable4", 4),
          ("serviceTermination", 32),
          ("terminalUnavailable45", 45),
          ("terminalUnavailable46", 46),
          ("userHasChangedNumber", 5))
    )


_Dass2FailCauseCode_Type.__name__ = "Integer32"
_Dass2FailCauseCode_Object = MibScalar
dass2FailCauseCode = _Dass2FailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 2, 3),
    _Dass2FailCauseCode_Type()
)
dass2FailCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dass2FailCauseCode.setStatus("mandatory")
_BriFailCauseCode_Type = Integer32
_BriFailCauseCode_Object = MibScalar
briFailCauseCode = _BriFailCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 2, 4),
    _BriFailCauseCode_Type()
)
briFailCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briFailCauseCode.setStatus("mandatory")
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 3)
)


class _RadiusReplyCode_Type(Integer32):
    """Custom type radiusReplyCode based on Integer32"""
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
        *(("radauthnoresponse", 1),
          ("radauthreadonly", 2),
          ("radauthreadwrite", 3),
          ("radauthreject", 0))
    )


_RadiusReplyCode_Type.__name__ = "Integer32"
_RadiusReplyCode_Object = MibScalar
radiusReplyCode = _RadiusReplyCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 3, 1),
    _RadiusReplyCode_Type()
)
radiusReplyCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusReplyCode.setStatus("mandatory")
_RadiusUsername_Type = DisplayString
_RadiusUsername_Object = MibScalar
radiusUsername = _RadiusUsername_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 3, 2),
    _RadiusUsername_Type()
)
radiusUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusUsername.setStatus("mandatory")
_Login_ObjectIdentity = ObjectIdentity
login = _Login_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 4)
)


class _LoginCode_Type(Integer32):
    """Custom type loginCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authok", 1),
          ("authreject", 0))
    )


_LoginCode_Type.__name__ = "Integer32"
_LoginCode_Object = MibScalar
loginCode = _LoginCode_Object(
    (1, 3, 6, 1, 4, 1, 559, 1, 2, 4, 4, 1),
    _LoginCode_Type()
)
loginCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginCode.setStatus("mandatory")
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2)
)
_RegArpeggio_ObjectIdentity = ObjectIdentity
regArpeggio = _RegArpeggio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10)
)
_ArpStandard_ObjectIdentity = ObjectIdentity
arpStandard = _ArpStandard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 1)
)
_ArpFocus_ObjectIdentity = ObjectIdentity
arpFocus = _ArpFocus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 2)
)
_ArpOffice_ObjectIdentity = ObjectIdentity
arpOffice = _ArpOffice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 3)
)
_ArpPlus_ObjectIdentity = ObjectIdentity
arpPlus = _ArpPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 4)
)
_ArpMultiLan_ObjectIdentity = ObjectIdentity
arpMultiLan = _ArpMultiLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 5)
)
_ArpLite_ObjectIdentity = ObjectIdentity
arpLite = _ArpLite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 6)
)
_ArpPlusRPrimary_ObjectIdentity = ObjectIdentity
arpPlusRPrimary = _ArpPlusRPrimary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 7)
)
_ArpPlusRBasic_ObjectIdentity = ObjectIdentity
arpPlusRBasic = _ArpPlusRBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 10, 8)
)
_OfficeConnect_ObjectIdentity = ObjectIdentity
officeConnect = _OfficeConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13)
)
_OfficeConnectRemote510s_ObjectIdentity = ObjectIdentity
officeConnectRemote510s = _OfficeConnectRemote510s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 1)
)
_OfficeConnectRemote520s_ObjectIdentity = ObjectIdentity
officeConnectRemote520s = _OfficeConnectRemote520s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 2)
)
_OfficeConnectRemote530s_ObjectIdentity = ObjectIdentity
officeConnectRemote530s = _OfficeConnectRemote530s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 3)
)
_OfficeConnectRemote510u_ObjectIdentity = ObjectIdentity
officeConnectRemote510u = _OfficeConnectRemote510u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 4)
)
_OfficeConnectRemote520u_ObjectIdentity = ObjectIdentity
officeConnectRemote520u = _OfficeConnectRemote520u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 5)
)
_OfficeConnectRemote530u_ObjectIdentity = ObjectIdentity
officeConnectRemote530u = _OfficeConnectRemote530u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 6)
)
_OfficeConnectRemote531s_ObjectIdentity = ObjectIdentity
officeConnectRemote531s = _OfficeConnectRemote531s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 7)
)
_OfficeConnectRemote531u_ObjectIdentity = ObjectIdentity
officeConnectRemote531u = _OfficeConnectRemote531u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 13, 8)
)
_AccessBuilder_ObjectIdentity = ObjectIdentity
accessBuilder = _AccessBuilder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14)
)
_AccessBuilderRemoteUser400s_ObjectIdentity = ObjectIdentity
accessBuilderRemoteUser400s = _AccessBuilderRemoteUser400s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 1)
)
_AccessBuilderRemoteUser400u_ObjectIdentity = ObjectIdentity
accessBuilderRemoteUser400u = _AccessBuilderRemoteUser400u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 2)
)
_AccessBuilderInternet400s_ObjectIdentity = ObjectIdentity
accessBuilderInternet400s = _AccessBuilderInternet400s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 3)
)
_AccessBuilderInternet400u_ObjectIdentity = ObjectIdentity
accessBuilderInternet400u = _AccessBuilderInternet400u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 4)
)
_AccessBuilderRemoteOffice500_ObjectIdentity = ObjectIdentity
accessBuilderRemoteOffice500 = _AccessBuilderRemoteOffice500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 5)
)
_AccessBuilderRemoteOffice600_ObjectIdentity = ObjectIdentity
accessBuilderRemoteOffice600 = _AccessBuilderRemoteOffice600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 6)
)
_AccessBuilderRemoteOffice700_ObjectIdentity = ObjectIdentity
accessBuilderRemoteOffice700 = _AccessBuilderRemoteOffice700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 7)
)
_AccessBuilder7000BriBridgeRouter_ObjectIdentity = ObjectIdentity
accessBuilder7000BriBridgeRouter = _AccessBuilder7000BriBridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 8)
)
_AccessBuilder7000PriBridgeRouter_ObjectIdentity = ObjectIdentity
accessBuilder7000PriBridgeRouter = _AccessBuilder7000PriBridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 14, 9)
)
_ServiceConnect2000_ObjectIdentity = ObjectIdentity
serviceConnect2000 = _ServiceConnect2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 15)
)
_ServiceConnect2000Base_ObjectIdentity = ObjectIdentity
serviceConnect2000Base = _ServiceConnect2000Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 15, 1)
)
_ServiceConnect2000BaseBri_ObjectIdentity = ObjectIdentity
serviceConnect2000BaseBri = _ServiceConnect2000BaseBri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 15, 1, 1)
)
_ServiceConnect2000BasePri_ObjectIdentity = ObjectIdentity
serviceConnect2000BasePri = _ServiceConnect2000BasePri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 2, 15, 1, 2)
)
_CscmInfo_ObjectIdentity = ObjectIdentity
cscmInfo = _CscmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 559, 3)
)


class _CscmEventNumber_Type(Integer32):
    """Custom type cscmEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100,
              101,
              102,
              103,
              104,
              105,
              1000,
              1001,
              1016,
              1017,
              1018,
              1019,
              1021,
              1022,
              1027,
              1038,
              1041,
              1042,
              1084,
              1086,
              1088,
              1145,
              1200,
              1201,
              1202,
              1203,
              1204,
              1205,
              1207,
              1208,
              1209,
              1210,
              1211,
              1230,
              1231,
              1232,
              1245,
              1246,
              1248)
        )
    )
    namedValues = NamedValues(
        *(("dailyThresholdExceeded", 102),
          ("dass2accessBarred", 1211),
          ("dass2cleared2", 1202),
          ("dass2cleared48", 1248),
          ("dass2lineOutOfService", 1209),
          ("dass2networkBusy", 1207),
          ("dass2noReply", 1231),
          ("dass2numberBusy", 1208),
          ("dass2numberIncomplete", 1201),
          ("dass2numberUnobtainable0", 1200),
          ("dass2numberUnobtainable10", 1210),
          ("dass2numberUnobtainable3", 1203),
          ("dass2numberUnobtainable30", 1230),
          ("dass2numberUnobtainable4", 1204),
          ("dass2serviceTermination", 1232),
          ("dass2terminalUnavailable45", 1245),
          ("dass2terminalUnavailable46", 1246),
          ("dass2userHasChangedNumber", 1205),
          ("hourlyThresholdExceeded", 103),
          ("isdnConnection", 3),
          ("isdnDisconnection", 4),
          ("linkDown", 2),
          ("linkUp", 1),
          ("maxCallLengthExceeded", 104),
          ("pollFailure", 100),
          ("pollSuccess", 101),
          ("q931callIdentityInUse", 1084),
          ("q931callRejected", 1021),
          ("q931destinationOutOfOrder", 1027),
          ("q931dlFailureLineBroken", 1145),
          ("q931failure1000", 1000),
          ("q931incompatibleDestination", 1088),
          ("q931networkOutOfOrder", 1038),
          ("q931noAnswerFromUser", 1019),
          ("q931noUserResponding", 1018),
          ("q931normalCallClearing", 1016),
          ("q931numberChanged", 1022),
          ("q931requestedCallIdentityCleared", 1086),
          ("q931switchingEquipmentCongestion", 1042),
          ("q931temporaryFailure", 1041),
          ("q931unallocatedNumber", 1001),
          ("q931userBusy", 1017),
          ("testPollFailure", 105))
    )


_CscmEventNumber_Type.__name__ = "Integer32"
_CscmEventNumber_Object = MibScalar
cscmEventNumber = _CscmEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 559, 3, 1),
    _CscmEventNumber_Type()
)
cscmEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscmEventNumber.setStatus("mandatory")
_CscmOriginatingIP_Type = IpAddress
_CscmOriginatingIP_Object = MibScalar
cscmOriginatingIP = _CscmOriginatingIP_Object(
    (1, 3, 6, 1, 4, 1, 559, 3, 2),
    _CscmOriginatingIP_Type()
)
cscmOriginatingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscmOriginatingIP.setStatus("mandatory")
_CscmTrapDetail_Type = DisplayString
_CscmTrapDetail_Object = MibScalar
cscmTrapDetail = _CscmTrapDetail_Object(
    (1, 3, 6, 1, 4, 1, 559, 3, 3),
    _CscmTrapDetail_Type()
)
cscmTrapDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cscmTrapDetail.setStatus("mandatory")

# Managed Objects groups


# Notification objects

isdnTestCallEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 1)
)
isdnTestCallEvent.setObjects(
      *(("REMOTEACCESS-MIB", "alarmCode"),
        ("REMOTEACCESS-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    isdnTestCallEvent.setStatus(
        ""
    )

isdnLinkDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 2)
)
isdnLinkDownEvent.setObjects(
      *(("REMOTEACCESS-MIB", "portsIndex"),
        ("REMOTEACCESS-MIB", "portsName"),
        ("REMOTEACCESS-MIB", "isdnportsState"),
        ("REMOTEACCESS-MIB", "isdnportsConnTime"))
)
if mibBuilder.loadTexts:
    isdnLinkDownEvent.setStatus(
        ""
    )

isdnLinkUpEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 3)
)
isdnLinkUpEvent.setObjects(
      *(("REMOTEACCESS-MIB", "portsIndex"),
        ("REMOTEACCESS-MIB", "portsName"),
        ("REMOTEACCESS-MIB", "isdnportsState"))
)
if mibBuilder.loadTexts:
    isdnLinkUpEvent.setStatus(
        ""
    )

q931FailCauseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 6)
)
q931FailCauseEvent.setObjects(
      *(("REMOTEACCESS-MIB", "portsIndex"),
        ("REMOTEACCESS-MIB", "isdnFailDestination"),
        ("REMOTEACCESS-MIB", "q931FailCauseCode"))
)
if mibBuilder.loadTexts:
    q931FailCauseEvent.setStatus(
        ""
    )

dass2FailCauseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 7)
)
dass2FailCauseEvent.setObjects(
      *(("REMOTEACCESS-MIB", "portsIndex"),
        ("REMOTEACCESS-MIB", "isdnFailDestination"),
        ("REMOTEACCESS-MIB", "dass2FailCauseCode"))
)
if mibBuilder.loadTexts:
    dass2FailCauseEvent.setStatus(
        ""
    )

briFailCauseEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 8)
)
briFailCauseEvent.setObjects(
      *(("REMOTEACCESS-MIB", "portsIndex"),
        ("REMOTEACCESS-MIB", "isdnFailDestination"),
        ("REMOTEACCESS-MIB", "briFailCauseCode"),
        ("REMOTEACCESS-MIB", "isdnParamsNetworkType"))
)
if mibBuilder.loadTexts:
    briFailCauseEvent.setStatus(
        ""
    )

radiusTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 20)
)
radiusTrapEvent.setObjects(
      *(("REMOTEACCESS-MIB", "radiusReplyCode"),
        ("REMOTEACCESS-MIB", "radiusUsername"))
)
if mibBuilder.loadTexts:
    radiusTrapEvent.setStatus(
        ""
    )

loginTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 21)
)
loginTrapEvent.setObjects(
    ("REMOTEACCESS-MIB", "loginCode")
)
if mibBuilder.loadTexts:
    loginTrapEvent.setStatus(
        ""
    )

cscmTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 559, 0, 100)
)
cscmTrapEvent.setObjects(
      *(("REMOTEACCESS-MIB", "cscmEventNumber"),
        ("REMOTEACCESS-MIB", "cscmOriginatingIP"),
        ("REMOTEACCESS-MIB", "cscmTrapDetail"))
)
if mibBuilder.loadTexts:
    cscmTrapEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REMOTEACCESS-MIB",
    **{"MacAddress": MacAddress,
       "EntryStatus": EntryStatus,
       "ppp": ppp,
       "tftp": tftp,
       "tftpFile": tftpFile,
       "tftpServerIP": tftpServerIP,
       "tftpAction": tftpAction,
       "tftpStatus": tftpStatus,
       "sonix": sonix,
       "isdnTestCallEvent": isdnTestCallEvent,
       "isdnLinkDownEvent": isdnLinkDownEvent,
       "isdnLinkUpEvent": isdnLinkUpEvent,
       "q931FailCauseEvent": q931FailCauseEvent,
       "dass2FailCauseEvent": dass2FailCauseEvent,
       "briFailCauseEvent": briFailCauseEvent,
       "radiusTrapEvent": radiusTrapEvent,
       "loginTrapEvent": loginTrapEvent,
       "cscmTrapEvent": cscmTrapEvent,
       "sonixMibs": sonixMibs,
       "remoteaccessMib": remoteaccessMib,
       "system": system,
       "variant": variant,
       "version": version,
       "unitname": unitname,
       "save": save,
       "standard": standard,
       "saverequired": saverequired,
       "date": date,
       "time": time,
       "dayoftheweek": dayoftheweek,
       "managertimeout": managertimeout,
       "unitipad": unitipad,
       "unitmacaddress": unitmacaddress,
       "defaultalert": defaultalert,
       "incallalert": incallalert,
       "publiccommunity": publiccommunity,
       "privatecommunity": privatecommunity,
       "trapaddress": trapaddress,
       "trapport": trapport,
       "lcdManagerLock": lcdManagerLock,
       "loopControl": loopControl,
       "novelltimeout": novelltimeout,
       "timeSinceReboot": timeSinceReboot,
       "passwdsTable": passwdsTable,
       "passwdsEntry": passwdsEntry,
       "passwdsOld": passwdsOld,
       "passwdsNew": passwdsNew,
       "ip": ip,
       "iprip": iprip,
       "ipInRipRequests": ipInRipRequests,
       "ipInRipResponses": ipInRipResponses,
       "ipInRipErrors": ipInRipErrors,
       "ipInRipDiscards": ipInRipDiscards,
       "ipOutRipRequests": ipOutRipRequests,
       "ipOutRipResponses": ipOutRipResponses,
       "ipOutRipUpdates": ipOutRipUpdates,
       "ipOutRipErrors": ipOutRipErrors,
       "ipOutRipDiscards": ipOutRipDiscards,
       "ipRoutingProtocol": ipRoutingProtocol,
       "ipRipLearning": ipRipLearning,
       "ipRoutingAdvertise": ipRoutingAdvertise,
       "ipRouteTableCopy": ipRouteTableCopy,
       "ipRouteEntryCopy": ipRouteEntryCopy,
       "ipRouteDestCopy": ipRouteDestCopy,
       "ipRouteIfIndexCopy": ipRouteIfIndexCopy,
       "ipRouteMetric1Copy": ipRouteMetric1Copy,
       "ipRouteMetric2Copy": ipRouteMetric2Copy,
       "ipRouteMetric3Copy": ipRouteMetric3Copy,
       "ipRouteMetric4Copy": ipRouteMetric4Copy,
       "ipRouteNextHopCopy": ipRouteNextHopCopy,
       "ipRouteTypeCopy": ipRouteTypeCopy,
       "ipRouteProtoCopy": ipRouteProtoCopy,
       "ipRouteAgeCopy": ipRouteAgeCopy,
       "ipRouteMaskCopy": ipRouteMaskCopy,
       "ipRouteMetric5Copy": ipRouteMetric5Copy,
       "ipRouteInfoCopy": ipRouteInfoCopy,
       "ipRouteNextHopName": ipRouteNextHopName,
       "ipRouteAdvertise": ipRouteAdvertise,
       "ipx": ipx,
       "ipxInReceives": ipxInReceives,
       "ipxInDelivers": ipxInDelivers,
       "ipxInDiscards": ipxInDiscards,
       "ipxInUnknownProtocols": ipxInUnknownProtocols,
       "ipxInHeaderErrors": ipxInHeaderErrors,
       "ipxForwardDatagrams": ipxForwardDatagrams,
       "ipxOutRequests": ipxOutRequests,
       "ipxOutNoRoutes": ipxOutNoRoutes,
       "ipxOutDiscards": ipxOutDiscards,
       "ipxForwarding": ipxForwarding,
       "ipxrip": ipxrip,
       "ipxInRipRequests": ipxInRipRequests,
       "ipxInRipResponses": ipxInRipResponses,
       "ipxInRipErrors": ipxInRipErrors,
       "ipxInRipTimeouts": ipxInRipTimeouts,
       "ipxInRipDiscards": ipxInRipDiscards,
       "ipxOutRipRequests": ipxOutRipRequests,
       "ipxOutRipResponses": ipxOutRipResponses,
       "ipxOutRipUpdates": ipxOutRipUpdates,
       "ipxOutRipErrors": ipxOutRipErrors,
       "ipxOutRipDiscards": ipxOutRipDiscards,
       "ipxrt": ipxrt,
       "ipxRoutingTable": ipxRoutingTable,
       "ipxRoutingTableEntry": ipxRoutingTableEntry,
       "ipxRouteTarget": ipxRouteTarget,
       "ipxRouteHopCount": ipxRouteHopCount,
       "ipxRouteTicks": ipxRouteTicks,
       "ipxRouteNextHopNetwork": ipxRouteNextHopNetwork,
       "ipxRouteNextHopNode": ipxRouteNextHopNode,
       "ipxRouteType": ipxRouteType,
       "ipxRoutePort": ipxRoutePort,
       "ipxRouteLinkType": ipxRouteLinkType,
       "ipxRouteIpxType": ipxRouteIpxType,
       "ipxRouteLinkTicks": ipxRouteLinkTicks,
       "ipxRouteMlink": ipxRouteMlink,
       "ipxRouteMode": ipxRouteMode,
       "ipxsap": ipxsap,
       "ipxInSapRequests": ipxInSapRequests,
       "ipxInSapResponses": ipxInSapResponses,
       "ipxInSapNoServers": ipxInSapNoServers,
       "ipxInSapErrors": ipxInSapErrors,
       "ipxInSapDiscards": ipxInSapDiscards,
       "ipxOutSapRequests": ipxOutSapRequests,
       "ipxOutSapResponses": ipxOutSapResponses,
       "ipxOutSapErrors": ipxOutSapErrors,
       "ipxOutSapDiscards": ipxOutSapDiscards,
       "ipxsapt": ipxsapt,
       "ipxServicesTable": ipxServicesTable,
       "ipxServicesTableEntry": ipxServicesTableEntry,
       "ipxServiceNetwork": ipxServiceNetwork,
       "ipxServiceNode": ipxServiceNode,
       "ipxServiceSocket": ipxServiceSocket,
       "ipxServiceName": ipxServiceName,
       "ipxServiceType": ipxServiceType,
       "ipxServiceHopCount": ipxServiceHopCount,
       "ipxServicePort": ipxServicePort,
       "ipxServiceNextHopNetwork": ipxServiceNextHopNetwork,
       "ipxServiceNextHopNode": ipxServiceNextHopNode,
       "ipxServiceIpxType": ipxServiceIpxType,
       "ipxServiceRTType": ipxServiceRTType,
       "ipxServiceLinkType": ipxServiceLinkType,
       "ipxServiceMlink": ipxServiceMlink,
       "ipxServiceMode": ipxServiceMode,
       "ipxnear": ipxnear,
       "ipxNearest": ipxNearest,
       "ipxNearestTable": ipxNearestTable,
       "ipxNearestTableEntry": ipxNearestTableEntry,
       "ipxNearestIndex": ipxNearestIndex,
       "ipxNearestServer": ipxNearestServer,
       "ipxNearestMode": ipxNearestMode,
       "pppext": pppext,
       "pppExtLcpConfigTable": pppExtLcpConfigTable,
       "pppExtLcpConfigTableEntry": pppExtLcpConfigTableEntry,
       "pppExtLcpLocalProtocolCompression": pppExtLcpLocalProtocolCompression,
       "pppExtLcpLocalAddressCompression": pppExtLcpLocalAddressCompression,
       "pppExtLcpRemoteMRU": pppExtLcpRemoteMRU,
       "pppExtLcpRemoteProtocolCompression": pppExtLcpRemoteProtocolCompression,
       "pppExtLcpRemoteAddressCompression": pppExtLcpRemoteAddressCompression,
       "pppExtLcpMinimumRestartPeriod": pppExtLcpMinimumRestartPeriod,
       "pppExtLcpMaximumRestartPeriod": pppExtLcpMaximumRestartPeriod,
       "pppExtLcpMaximumTerminateRequests": pppExtLcpMaximumTerminateRequests,
       "pppExtLcpMaximumConfigRequests": pppExtLcpMaximumConfigRequests,
       "pppExtLcpMaximumConfigNaks": pppExtLcpMaximumConfigNaks,
       "pppExtLcpLocalMRU": pppExtLcpLocalMRU,
       "pppExtLcpLocalMagic": pppExtLcpLocalMagic,
       "pppExtLcpRemoteMagic": pppExtLcpRemoteMagic,
       "pppExtLcpLocalMRUEnabled": pppExtLcpLocalMRUEnabled,
       "pppExtLcpRemoteMRUEnabled": pppExtLcpRemoteMRUEnabled,
       "pppExtLcpLocalACCM": pppExtLcpLocalACCM,
       "pppExtLcpRemoteACCM": pppExtLcpRemoteACCM,
       "pppExtLcpLocalACCMEnabled": pppExtLcpLocalACCMEnabled,
       "pppExtLcpRemoteACCMEnabled": pppExtLcpRemoteACCMEnabled,
       "pppExtLcpLocalPAPEnabled": pppExtLcpLocalPAPEnabled,
       "pppExtLcpRemotePAPEnabled": pppExtLcpRemotePAPEnabled,
       "pppExtLcpLocalCHAPEnabled": pppExtLcpLocalCHAPEnabled,
       "pppExtLcpRemoteCHAPEnabled": pppExtLcpRemoteCHAPEnabled,
       "pppEchoConfigTable": pppEchoConfigTable,
       "pppEchoConfigTableEntry": pppEchoConfigTableEntry,
       "pppEchoPeriod": pppEchoPeriod,
       "pppEchoMaxNumberRetransmits": pppEchoMaxNumberRetransmits,
       "pppIpcpConfigTable": pppIpcpConfigTable,
       "pppIpcpConfigTableEntry": pppIpcpConfigTableEntry,
       "ipcpLocalIPAddressNegotiation": ipcpLocalIPAddressNegotiation,
       "ipcpRemoteIPAddressNegotiation": ipcpRemoteIPAddressNegotiation,
       "ipcpRemoteCompressionNegotiation": ipcpRemoteCompressionNegotiation,
       "ipcpMinimumRestartPeriod": ipcpMinimumRestartPeriod,
       "ipcpMaximumRestartPeriod": ipcpMaximumRestartPeriod,
       "ipcpMaximumTerminateRequests": ipcpMaximumTerminateRequests,
       "ipcpMaximumConfigRequests": ipcpMaximumConfigRequests,
       "ipcpMaximumConfigNaks": ipcpMaximumConfigNaks,
       "ipcpLocalCompressionNegotiation": ipcpLocalCompressionNegotiation,
       "ipcpRfc1172Negotiation": ipcpRfc1172Negotiation,
       "pppIpxcpConfigTable": pppIpxcpConfigTable,
       "pppIpxcpConfigTableEntry": pppIpxcpConfigTableEntry,
       "ipxcpLocalNetworkNumberNegotiation": ipxcpLocalNetworkNumberNegotiation,
       "ipxcpLocalNodeNumberNegotiation": ipxcpLocalNodeNumberNegotiation,
       "ipxcpLocalRoutingProtocolNegotiation": ipxcpLocalRoutingProtocolNegotiation,
       "ipxcpLocalRouterNameNegotiation": ipxcpLocalRouterNameNegotiation,
       "ipxcpRemoteNetworkNumberNegotiation": ipxcpRemoteNetworkNumberNegotiation,
       "ipxcpRemoteNodeNumberNegotiation": ipxcpRemoteNodeNumberNegotiation,
       "ipxcpRemoteRoutingProtocolNegotiation": ipxcpRemoteRoutingProtocolNegotiation,
       "ipxcpRemoteRouterNameNegotiation": ipxcpRemoteRouterNameNegotiation,
       "ipxcpConfigCompleteNegotiation": ipxcpConfigCompleteNegotiation,
       "ipxcpAdmin": ipxcpAdmin,
       "ipxcpMinimumRestartPeriod": ipxcpMinimumRestartPeriod,
       "ipxcpMaximumRestartPeriod": ipxcpMaximumRestartPeriod,
       "ipxcpMaximumTerminateRequests": ipxcpMaximumTerminateRequests,
       "ipxcpMaximumConfigRequests": ipxcpMaximumConfigRequests,
       "ipxcpMaximumConfigNaks": ipxcpMaximumConfigNaks,
       "ipxcpNodeNumber": ipxcpNodeNumber,
       "pppExtConfigTable": pppExtConfigTable,
       "pppExtConfigTableEntry": pppExtConfigTableEntry,
       "pppExtLinkAuthentication": pppExtLinkAuthentication,
       "pppExtEnableIp": pppExtEnableIp,
       "pppExtEnableIpx": pppExtEnableIpx,
       "pppExtHdlcLayer": pppExtHdlcLayer,
       "firewall": firewall,
       "ipFirewallStatusTable": ipFirewallStatusTable,
       "ipFirewallStatusTableEntry": ipFirewallStatusTableEntry,
       "ipFirewallStatusIndex": ipFirewallStatusIndex,
       "ipFirewallFilteredPackets": ipFirewallFilteredPackets,
       "ipFirewallConfigTable": ipFirewallConfigTable,
       "ipFirewallConfigTableEntry": ipFirewallConfigTableEntry,
       "ipFirewallConfigIndex": ipFirewallConfigIndex,
       "ipFirewallSourceAddress": ipFirewallSourceAddress,
       "ipFirewallSourceMask": ipFirewallSourceMask,
       "ipFirewallLowerSourcePort": ipFirewallLowerSourcePort,
       "ipFirewallHigherSourcePort": ipFirewallHigherSourcePort,
       "ipFirewallDestinationAddress": ipFirewallDestinationAddress,
       "ipFirewallDestinationMask": ipFirewallDestinationMask,
       "ipFirewallLowerDestinationPort": ipFirewallLowerDestinationPort,
       "ipFirewallHigherDestinationPort": ipFirewallHigherDestinationPort,
       "ipFirewallRouterName": ipFirewallRouterName,
       "ipFirewallMode": ipFirewallMode,
       "ipFirewallType": ipFirewallType,
       "ipFirewallAction": ipFirewallAction,
       "ipFirewallBidir": ipFirewallBidir,
       "ipFirewallTcpsyn": ipFirewallTcpsyn,
       "ipxFirewallStatusTable": ipxFirewallStatusTable,
       "ipxFirewallStatusTableEntry": ipxFirewallStatusTableEntry,
       "ipxFirewallStatusIndex": ipxFirewallStatusIndex,
       "ipxFirewallFilteredPackets": ipxFirewallFilteredPackets,
       "ipxFirewallConfigTable": ipxFirewallConfigTable,
       "ipxFirewallConfigTableEntry": ipxFirewallConfigTableEntry,
       "ipxFirewallConfigIndex": ipxFirewallConfigIndex,
       "ipxFirewallLowerSourceNetwork": ipxFirewallLowerSourceNetwork,
       "ipxFirewallHigherSourceNetwork": ipxFirewallHigherSourceNetwork,
       "ipxFirewallLowerSourceNode": ipxFirewallLowerSourceNode,
       "ipxFirewallHigherSourceNode": ipxFirewallHigherSourceNode,
       "ipxFirewallLowerSourceSocket": ipxFirewallLowerSourceSocket,
       "ipxFirewallHigherSourceSocket": ipxFirewallHigherSourceSocket,
       "ipxFirewallLowerDestinationNetwork": ipxFirewallLowerDestinationNetwork,
       "ipxFirewallHigherDestinationNetwork": ipxFirewallHigherDestinationNetwork,
       "ipxFirewallLowerDestinationNode": ipxFirewallLowerDestinationNode,
       "ipxFirewallHigherDestinationNode": ipxFirewallHigherDestinationNode,
       "ipxFirewallLowerDestinationSocket": ipxFirewallLowerDestinationSocket,
       "ipxFirewallHigherDestinationSocket": ipxFirewallHigherDestinationSocket,
       "ipxFirewallRouterName": ipxFirewallRouterName,
       "ipxFirewallMode": ipxFirewallMode,
       "ipxFirewallAction": ipxFirewallAction,
       "ipxFirewallBidir": ipxFirewallBidir,
       "users": users,
       "usercfgTable": usercfgTable,
       "usercfgEntry": usercfgEntry,
       "usercfgIndex": usercfgIndex,
       "usercfgName": usercfgName,
       "usercfgMac": usercfgMac,
       "usercfgAllowed": usercfgAllowed,
       "usercfgMode": usercfgMode,
       "srcEnabled": srcEnabled,
       "srcPriority": srcPriority,
       "ipnat": ipnat,
       "ipNatTranslate": ipNatTranslate,
       "ipNatIpAddress": ipNatIpAddress,
       "ipNatBogusNetwork": ipNatBogusNetwork,
       "ipNatBogusNetmask": ipNatBogusNetmask,
       "ipNatTcpFinTimeout": ipNatTcpFinTimeout,
       "ipNatTcpInactiveTimeout": ipNatTcpInactiveTimeout,
       "ipNatUdpTimeout": ipNatUdpTimeout,
       "ipNatMyself": ipNatMyself,
       "dhcpserver": dhcpserver,
       "dhcpAutoStatus": dhcpAutoStatus,
       "dhcpAutoName": dhcpAutoName,
       "dhcpAutoDomain": dhcpAutoDomain,
       "dhcpAutoSeedStart": dhcpAutoSeedStart,
       "dhcpAutoSeedEnd": dhcpAutoSeedEnd,
       "dhcpAutoMask": dhcpAutoMask,
       "dhcpAutoRouter": dhcpAutoRouter,
       "dhcpWINSTable": dhcpWINSTable,
       "dhcpWINSEntry": dhcpWINSEntry,
       "dhcpWINSIndex": dhcpWINSIndex,
       "dhcpWINSAddr": dhcpWINSAddr,
       "dhcpDNSTable": dhcpDNSTable,
       "dhcpDNSEntry": dhcpDNSEntry,
       "dhcpDNSIndex": dhcpDNSIndex,
       "dhcpDNSAddr": dhcpDNSAddr,
       "dhcpAutoLease": dhcpAutoLease,
       "dhcpAstatTable": dhcpAstatTable,
       "dhcpAstatEntry": dhcpAstatEntry,
       "dhcpAstatIpAddr": dhcpAstatIpAddr,
       "dhcpAstatIf": dhcpAstatIf,
       "dhcpAstatHwAddr": dhcpAstatHwAddr,
       "dhcpAstatCID": dhcpAstatCID,
       "dhcpAstatLife": dhcpAstatLife,
       "pppAuthTable": pppAuthTable,
       "pppAuthTableEntry": pppAuthTableEntry,
       "pppAuthIndex": pppAuthIndex,
       "pppAuthName": pppAuthName,
       "pppAuthClass": pppAuthClass,
       "pppAuthLocalId": pppAuthLocalId,
       "pppAuthLocalPw": pppAuthLocalPw,
       "pppAuthRemoteId": pppAuthRemoteId,
       "pppAuthRemotePw": pppAuthRemotePw,
       "pppAuthRetryPeriod": pppAuthRetryPeriod,
       "pppAuthRenegPeriod": pppAuthRenegPeriod,
       "pppAuthRetryCount": pppAuthRetryCount,
       "pppAuthMode": pppAuthMode,
       "dnsproxy": dnsproxy,
       "primaryDNSAddress": primaryDNSAddress,
       "secondaryDNSAddress": secondaryDNSAddress,
       "primaryNBNSAddress": primaryNBNSAddress,
       "secondaryNBNSAddress": secondaryNBNSAddress,
       "dnsProxyActive": dnsProxyActive,
       "dnsCacheSize": dnsCacheSize,
       "dnsMaxServerTimeout": dnsMaxServerTimeout,
       "dnsServerRetries": dnsServerRetries,
       "dnsDomainTable": dnsDomainTable,
       "dnsDomainTableEntry": dnsDomainTableEntry,
       "dnsDomainTableIndex": dnsDomainTableIndex,
       "dnsDomainDomainName": dnsDomainDomainName,
       "dnsDomainProfileIndex": dnsDomainProfileIndex,
       "dnsDomainRemoteServer": dnsDomainRemoteServer,
       "dnsDomainPrimaryDNS": dnsDomainPrimaryDNS,
       "dnsDomainSecondaryDNS": dnsDomainSecondaryDNS,
       "dnsDomainMode": dnsDomainMode,
       "dnsProfileTable": dnsProfileTable,
       "dnsProfileEntry": dnsProfileEntry,
       "dnsProfileIndex": dnsProfileIndex,
       "dnsProfileName": dnsProfileName,
       "dnsProfileRemoteServer": dnsProfileRemoteServer,
       "dnsProfilePrimaryDNS": dnsProfilePrimaryDNS,
       "dnsProfileSecondaryDNS": dnsProfileSecondaryDNS,
       "dnsProfileMode": dnsProfileMode,
       "memoryusage": memoryusage,
       "memoryFree": memoryFree,
       "memoryTotal": memoryTotal,
       "fragmentCount": fragmentCount,
       "fragmentLargest": fragmentLargest,
       "pool1size": pool1size,
       "pool2size": pool2size,
       "pool3size": pool3size,
       "pool4size": pool4size,
       "traptable": traptable,
       "traptableEntry": traptableEntry,
       "trapIndex": trapIndex,
       "trapAddr": trapAddr,
       "trapPort": trapPort,
       "trapLogFull": trapLogFull,
       "trapLogThreshold": trapLogThreshold,
       "trapWarmStart": trapWarmStart,
       "trapLinkDown": trapLinkDown,
       "trapLinkUp": trapLinkUp,
       "trapVoiceDown": trapVoiceDown,
       "trapVoiceUp": trapVoiceUp,
       "trapISDNDown": trapISDNDown,
       "trapISDNUp": trapISDNUp,
       "trapAlarm": trapAlarm,
       "trapQ931Fail": trapQ931Fail,
       "trapDASS2Fail": trapDASS2Fail,
       "trapBriFail": trapBriFail,
       "trapLoginAuth": trapLoginAuth,
       "patTable": patTable,
       "patEntry": patEntry,
       "patIndex": patIndex,
       "patPort": patPort,
       "patInternalIP": patInternalIP,
       "patInternalPort": patInternalPort,
       "patMode": patMode,
       "tpadLanPort": tpadLanPort,
       "ports": ports,
       "portsTable": portsTable,
       "portsEntry": portsEntry,
       "portsIndex": portsIndex,
       "portsName": portsName,
       "portsType": portsType,
       "portsPhys": portsPhys,
       "portsTxutil": portsTxutil,
       "portsRxutil": portsRxutil,
       "portsCompress": portsCompress,
       "portsState": portsState,
       "portsRxoctets": portsRxoctets,
       "portsTxoctets": portsTxoctets,
       "portsRxpackets": portsRxpackets,
       "portsTxpackets": portsTxpackets,
       "portsRxerrs": portsRxerrs,
       "portsTxerrs": portsTxerrs,
       "portslanTable": portslanTable,
       "portslanEntry": portslanEntry,
       "portslanIndex": portslanIndex,
       "portslanName": portslanName,
       "portslanPriority": portslanPriority,
       "portslanLinespeed": portslanLinespeed,
       "portslanIpAddress": portslanIpAddress,
       "portslanIpMask": portslanIpMask,
       "portslanIpMetric": portslanIpMetric,
       "portslanIpxNetwork": portslanIpxNetwork,
       "portslanIpxType": portslanIpxType,
       "portshdlcTable": portshdlcTable,
       "portshdlcEntry": portshdlcEntry,
       "portshdlcIndex": portshdlcIndex,
       "portshdlcName": portshdlcName,
       "portshdlcPriority": portshdlcPriority,
       "portshdlcLinespeed": portshdlcLinespeed,
       "portshdlcCompression": portshdlcCompression,
       "portshdlcScramble": portshdlcScramble,
       "portshdlcBackupdemand": portshdlcBackupdemand,
       "portshdlcDemandthresh": portshdlcDemandthresh,
       "portshdlcDemandperiod": portshdlcDemandperiod,
       "portshdlcIdlethresh": portshdlcIdlethresh,
       "portshdlcIdleperiod": portshdlcIdleperiod,
       "portshdlcBackupalert": portshdlcBackupalert,
       "portshdlcDemandpriority": portshdlcDemandpriority,
       "portshdlcBackuppriority": portshdlcBackuppriority,
       "portshdlcBackupnumber": portshdlcBackupnumber,
       "portshdlcBackupMac": portshdlcBackupMac,
       "portshdlcIpAddress": portshdlcIpAddress,
       "portshdlcIpMask": portshdlcIpMask,
       "portshdlcIpMetric": portshdlcIpMetric,
       "portshdlcIpxNetwork": portshdlcIpxNetwork,
       "portshdlcIpxType": portshdlcIpxType,
       "portspppTable": portspppTable,
       "portspppEntry": portspppEntry,
       "portspppIndex": portspppIndex,
       "portspppName": portspppName,
       "portspppPriority": portspppPriority,
       "portspppLinespeed": portspppLinespeed,
       "portspppIpAddress": portspppIpAddress,
       "portspppIpMask": portspppIpMask,
       "portspppIpMetric": portspppIpMetric,
       "portspppIpxNetwork": portspppIpxNetwork,
       "portspppIpxType": portspppIpxType,
       "portspppBaud": portspppBaud,
       "portspppDataBits": portspppDataBits,
       "portspppStopBits": portspppStopBits,
       "portspppFlowControl": portspppFlowControl,
       "portspppTxParity": portspppTxParity,
       "portspppRxParity": portspppRxParity,
       "portspppRemoteUnit": portspppRemoteUnit,
       "portspppIPRemoteAddress": portspppIPRemoteAddress,
       "portstaTable": portstaTable,
       "portstaEntry": portstaEntry,
       "portstaIndex": portstaIndex,
       "portstaName": portstaName,
       "portstaPriority": portstaPriority,
       "portstaLinespeed": portstaLinespeed,
       "portstaCompression": portstaCompression,
       "portstaScramble": portstaScramble,
       "portstaDemand": portstaDemand,
       "portstaDemandthresh": portstaDemandthresh,
       "portstaDemandperiod": portstaDemandperiod,
       "portstaIdlethresh": portstaIdlethresh,
       "portstaIdleperiod": portstaIdleperiod,
       "portstaDemandpriority": portstaDemandpriority,
       "portstaDialtimeout": portstaDialtimeout,
       "portstaAtzstring": portstaAtzstring,
       "portstaSpidstring": portstaSpidstring,
       "portsslipTable": portsslipTable,
       "portsslipEntry": portsslipEntry,
       "portsslipIndex": portsslipIndex,
       "portsslipName": portsslipName,
       "portsslipPriority": portsslipPriority,
       "portsslipLinespeed": portsslipLinespeed,
       "portsslipIpAddress": portsslipIpAddress,
       "portsslipIpMask": portsslipIpMask,
       "portsslipIpMetric": portsslipIpMetric,
       "portsslipBaud": portsslipBaud,
       "portsslipDataBits": portsslipDataBits,
       "portsslipStopBits": portsslipStopBits,
       "portsslipFlowControl": portsslipFlowControl,
       "portsslipTxParity": portsslipTxParity,
       "portsslipRxParity": portsslipRxParity,
       "portsslipMTU": portsslipMTU,
       "portsslipRIPPrivate": portsslipRIPPrivate,
       "portsslipIPRemoteAddress": portsslipIPRemoteAddress,
       "portsasyncTable": portsasyncTable,
       "portsasyncEntry": portsasyncEntry,
       "portsasyncIndex": portsasyncIndex,
       "portsasyncName": portsasyncName,
       "portsasyncBaud": portsasyncBaud,
       "portsasyncDataBits": portsasyncDataBits,
       "portsasyncStopBits": portsasyncStopBits,
       "portsasyncFlowControl": portsasyncFlowControl,
       "portsasyncTxParity": portsasyncTxParity,
       "portsasyncRxParity": portsasyncRxParity,
       "portsvoiceTable": portsvoiceTable,
       "portsvoiceEntry": portsvoiceEntry,
       "portsvoiceIndex": portsvoiceIndex,
       "portsvoiceName": portsvoiceName,
       "portsvoiceCallsPermitted": portsvoiceCallsPermitted,
       "portsvoiceEncoding": portsvoiceEncoding,
       "portsvoiceDialMode": portsvoiceDialMode,
       "portstpadTable": portstpadTable,
       "portstpadEntry": portstpadEntry,
       "portstpadIndex": portstpadIndex,
       "portstpadName": portstpadName,
       "portstpadBaud": portstpadBaud,
       "portstpadDataBits": portstpadDataBits,
       "portstpadStopBits": portstpadStopBits,
       "portstpadParity": portstpadParity,
       "portstpadTxFlowControl": portstpadTxFlowControl,
       "portstpadRxFlowControl": portstpadRxFlowControl,
       "portstpadX25MinLCN": portstpadX25MinLCN,
       "portstpadX25MaxLCN": portstpadX25MaxLCN,
       "bridge": bridge,
       "mlink": mlink,
       "mlinkTable": mlinkTable,
       "mlinkEntry": mlinkEntry,
       "mlinkIndex": mlinkIndex,
       "mlinkName": mlinkName,
       "mlinkNumberOfPorts": mlinkNumberOfPorts,
       "mlinkInFrames": mlinkInFrames,
       "mlinkOutFrames": mlinkOutFrames,
       "mlinkInDiscards": mlinkInDiscards,
       "mlinkState": mlinkState,
       "filter": filter,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterDest": filterDest,
       "filterSource": filterSource,
       "filterPrimary": filterPrimary,
       "filterType": filterType,
       "filterRoute": filterRoute,
       "filterPacketcount": filterPacketcount,
       "filterBytecount": filterBytecount,
       "filtertypeTable": filtertypeTable,
       "filtertypeEntry": filtertypeEntry,
       "filtertypeIndex": filtertypeIndex,
       "filtertypeClass": filtertypeClass,
       "filtertypeLsap": filtertypeLsap,
       "filtertypeMode": filtertypeMode,
       "filterAgingtime": filterAgingtime,
       "filterLearning": filterLearning,
       "filterActiononmatch": filterActiononmatch,
       "filterFiltermcast": filterFiltermcast,
       "filterTypematching": filterTypematching,
       "filterTypematchaction": filterTypematchaction,
       "filterLearnsourceonmcast": filterLearnsourceonmcast,
       "filterFlushall": filterFlushall,
       "filterLearnnovell": filterLearnnovell,
       "filterLearnbridging": filterLearnbridging,
       "authorised": authorised,
       "authorisedTable": authorisedTable,
       "authorisedEntry": authorisedEntry,
       "authorisedIndex": authorisedIndex,
       "authorisedAddress": authorisedAddress,
       "authorisedMode": authorisedMode,
       "isdn": isdn,
       "autocall": autocall,
       "autocallMacTable": autocallMacTable,
       "autocallMacEntry": autocallMacEntry,
       "autocallMacIndex": autocallMacIndex,
       "autocallMacDefault": autocallMacDefault,
       "autocallMacBumpable": autocallMacBumpable,
       "autocallMacIdle": autocallMacIdle,
       "autocallMacIdleThreshold": autocallMacIdleThreshold,
       "autocallMacAddress": autocallMacAddress,
       "autocallMacIsdn": autocallMacIsdn,
       "autocallMacMode": autocallMacMode,
       "autocallIpTable": autocallIpTable,
       "autocallIpEntry": autocallIpEntry,
       "autocallIpIndex": autocallIpIndex,
       "autocallIpBumpable": autocallIpBumpable,
       "autocallIpIdle": autocallIpIdle,
       "autocallIpIdleThreshold": autocallIpIdleThreshold,
       "autocallIpAddress": autocallIpAddress,
       "autocallIpMask": autocallIpMask,
       "autocallIpInverse": autocallIpInverse,
       "autocallIpIsdn": autocallIpIsdn,
       "autocallIpMode": autocallIpMode,
       "autocallIpxSapTable": autocallIpxSapTable,
       "autocallIpxSapEntry": autocallIpxSapEntry,
       "autocallIpxSapIndex": autocallIpxSapIndex,
       "autocallIpxSapServer": autocallIpxSapServer,
       "autocallIpxSapNetwork": autocallIpxSapNetwork,
       "autocallIpxSapNode": autocallIpxSapNode,
       "autocallIpxSapSocket": autocallIpxSapSocket,
       "autocallIpxSapService": autocallIpxSapService,
       "autocallIpxSapHops": autocallIpxSapHops,
       "autocallIpxSapIsdn": autocallIpxSapIsdn,
       "autocallIpxSapFrameType": autocallIpxSapFrameType,
       "autocallIpxSapDirectNetwork": autocallIpxSapDirectNetwork,
       "autocallIpxSapRouterMac": autocallIpxSapRouterMac,
       "autocallIpxSapNearest": autocallIpxSapNearest,
       "autocallIpxSapPpp": autocallIpxSapPpp,
       "autocallIpxSapIsdnType": autocallIpxSapIsdnType,
       "autocallIpxSapMode": autocallIpxSapMode,
       "autocallIpxTable": autocallIpxTable,
       "autocallIpxEntry": autocallIpxEntry,
       "autocallIpxIndex": autocallIpxIndex,
       "autocallIpxNetwork": autocallIpxNetwork,
       "autocallIpxNode": autocallIpxNode,
       "autocallIpxPacketType": autocallIpxPacketType,
       "autocallIpxTransportControl": autocallIpxTransportControl,
       "autocallIpxIsdn": autocallIpxIsdn,
       "autocallIpxBumpable": autocallIpxBumpable,
       "autocallIpxIdle": autocallIpxIdle,
       "autocallIpxIdleThreshold": autocallIpxIdleThreshold,
       "autocallIpxDefault": autocallIpxDefault,
       "autocallIpxFrameType": autocallIpxFrameType,
       "autocallIpxPpp": autocallIpxPpp,
       "autocallIpxIsdnType": autocallIpxIsdnType,
       "autocallIpxMode": autocallIpxMode,
       "autocallIpxRipTable": autocallIpxRipTable,
       "autocallIpxRipEntry": autocallIpxRipEntry,
       "autocallIpxRipIndex": autocallIpxRipIndex,
       "autocallIpxRipNetwork": autocallIpxRipNetwork,
       "autocallIpxRipHops": autocallIpxRipHops,
       "autocallIpxRipTicks": autocallIpxRipTicks,
       "autocallIpxRipNode": autocallIpxRipNode,
       "autocallIpxRipIsdn": autocallIpxRipIsdn,
       "autocallIpxRipFrameType": autocallIpxRipFrameType,
       "autocallIpxRipDirectNetwork": autocallIpxRipDirectNetwork,
       "autocallIpxRipRouterMac": autocallIpxRipRouterMac,
       "autocallIpxRipLinkTicks": autocallIpxRipLinkTicks,
       "autocallIpxRipPpp": autocallIpxRipPpp,
       "autocallIpxRipIsdnType": autocallIpxRipIsdnType,
       "autocallIpxRipMode": autocallIpxRipMode,
       "autocallDialTable": autocallDialTable,
       "autocallDialEntry": autocallDialEntry,
       "autocallDialIndex": autocallDialIndex,
       "autocallDialCli": autocallDialCli,
       "autocallDialIsdn": autocallDialIsdn,
       "autocallDialBumpable": autocallDialBumpable,
       "autocallDialIdle": autocallDialIdle,
       "autocallDialIdleThreshold": autocallDialIdleThreshold,
       "autocallDialMode": autocallDialMode,
       "isdnbands": isdnbands,
       "isdnbandsTable": isdnbandsTable,
       "isdnbandsEntry": isdnbandsEntry,
       "isdnbandsIndex": isdnbandsIndex,
       "isdnbandsName": isdnbandsName,
       "isdnbandsStarttime": isdnbandsStarttime,
       "isdnbandsEndtime": isdnbandsEndtime,
       "isdnbandsDays": isdnbandsDays,
       "isdnbandsAllowbackup": isdnbandsAllowbackup,
       "isdnbandsAllowdemand": isdnbandsAllowdemand,
       "isdnbandsAllowautocall": isdnbandsAllowautocall,
       "isdnbandsAllowlist": isdnbandsAllowlist,
       "isdnbandsMode": isdnbandsMode,
       "isdnbandsBridgeListTable": isdnbandsBridgeListTable,
       "isdnbandsBridgeListEntry": isdnbandsBridgeListEntry,
       "isdnbandsBridgeListIndex": isdnbandsBridgeListIndex,
       "isdnbandsBridgeListBandName": isdnbandsBridgeListBandName,
       "isdnbandsBridgeListBridgeName": isdnbandsBridgeListBridgeName,
       "isdnnumbers": isdnnumbers,
       "isdnnumbersTable": isdnnumbersTable,
       "isdnnumbersEntry": isdnnumbersEntry,
       "isdnnumbersIndex": isdnnumbersIndex,
       "isdnnumbersName": isdnnumbersName,
       "isdnnumbersNumber1": isdnnumbersNumber1,
       "isdnnumbersNumber2": isdnnumbersNumber2,
       "isdnnumbersNumber3": isdnnumbersNumber3,
       "isdnnumbersNumber4": isdnnumbersNumber4,
       "isdnnumbersCall": isdnnumbersCall,
       "isdnnumbersTesttime": isdnnumbersTesttime,
       "isdnnumbersDays": isdnnumbersDays,
       "isdnnumbersLasttest": isdnnumbersLasttest,
       "isdnnumbersIpAddress": isdnnumbersIpAddress,
       "isdnnumbersIpMask": isdnnumbersIpMask,
       "isdnnumbersIpMetric": isdnnumbersIpMetric,
       "isdnnumbersIpxNetwork": isdnnumbersIpxNetwork,
       "isdnnumbersIpxType": isdnnumbersIpxType,
       "isdnnumbersPpp": isdnnumbersPpp,
       "isdnnumbersRemoteIpAddress": isdnnumbersRemoteIpAddress,
       "isdnnumbersRemoteUnitType": isdnnumbersRemoteUnitType,
       "isdnnumbersHdlcType": isdnnumbersHdlcType,
       "isdnnumbersPppAuthentication": isdnnumbersPppAuthentication,
       "isdnnumbersMaxCircuits": isdnnumbersMaxCircuits,
       "isdnnumbersMPEnable": isdnnumbersMPEnable,
       "isdnnumbersLearntED": isdnnumbersLearntED,
       "isdnnumbersMode": isdnnumbersMode,
       "isdnnumbersCallType1": isdnnumbersCallType1,
       "isdnnumbersCallType2": isdnnumbersCallType2,
       "isdnnumbersCallType3": isdnnumbersCallType3,
       "isdnnumbersCallType4": isdnnumbersCallType4,
       "isdnports": isdnports,
       "isdnportsTable": isdnportsTable,
       "isdnportsEntry": isdnportsEntry,
       "isdnportsIndex": isdnportsIndex,
       "isdnportsDestination": isdnportsDestination,
       "isdnportsState": isdnportsState,
       "isdnportsConnTime": isdnportsConnTime,
       "isdnportsBackup": isdnportsBackup,
       "isdnportsDemand": isdnportsDemand,
       "isdnportsBumpable": isdnportsBumpable,
       "isdnportsAlert": isdnportsAlert,
       "isdnportsPriority": isdnportsPriority,
       "isdnportsSourceMac": isdnportsSourceMac,
       "isdnhistory": isdnhistory,
       "isdnhistoryTable": isdnhistoryTable,
       "isdnhistoryEntry": isdnhistoryEntry,
       "isdnhistoryIndex": isdnhistoryIndex,
       "isdnhistoryDestination": isdnhistoryDestination,
       "isdnhistoryTotalTime": isdnhistoryTotalTime,
       "isdnhistoryTotalCalls": isdnhistoryTotalCalls,
       "isdnhistoryFailedCalls": isdnhistoryFailedCalls,
       "isdncla": isdncla,
       "isdnCliTable": isdnCliTable,
       "isdnCliEntry": isdnCliEntry,
       "isdnCliIndex": isdnCliIndex,
       "isdnCliNumber": isdnCliNumber,
       "isdnCliMode": isdnCliMode,
       "isdnlists": isdnlists,
       "isdnlistsTable": isdnlistsTable,
       "isdnlistsEntry": isdnlistsEntry,
       "isdnlistsIndex": isdnlistsIndex,
       "isdnlistsBand": isdnlistsBand,
       "isdnlistsName": isdnlistsName,
       "isdnParams": isdnParams,
       "isdnParamsNetworkType": isdnParamsNetworkType,
       "isdnParamsSpid1": isdnParamsSpid1,
       "isdnParamsSpid2": isdnParamsSpid2,
       "isdnParamsSpid3": isdnParamsSpid3,
       "isdnParamsSpid4": isdnParamsSpid4,
       "isdnParamsDirectoryNumber1": isdnParamsDirectoryNumber1,
       "isdnParamsDirectoryNumber2": isdnParamsDirectoryNumber2,
       "isdnParamsDirectoryNumber3": isdnParamsDirectoryNumber3,
       "isdnParamsDirectoryNumber4": isdnParamsDirectoryNumber4,
       "isdnParamsReportBusy": isdnParamsReportBusy,
       "isdnParamsIncomingDov": isdnParamsIncomingDov,
       "isdnParamsMaxCallTime": isdnParamsMaxCallTime,
       "isdnParamsMsn": isdnParamsMsn,
       "isdnParamsMsnLan": isdnParamsMsnLan,
       "isdnParamsMsnVoice": isdnParamsMsnVoice,
       "isdnParamsMsnCheck": isdnParamsMsnCheck,
       "isdnParamsMsnSend": isdnParamsMsnSend,
       "isdnParamsSubAddr": isdnParamsSubAddr,
       "isdnParamsSubAddrLan": isdnParamsSubAddrLan,
       "isdnParamsSubAddrVoice": isdnParamsSubAddrVoice,
       "isdnParamsSubAddrCheck": isdnParamsSubAddrCheck,
       "isdnParamsSubAddrSend": isdnParamsSubAddrSend,
       "isdnParamsSubAddrType": isdnParamsSubAddrType,
       "isdnParamsTokenValue": isdnParamsTokenValue,
       "isdnParamsTokenRefill": isdnParamsTokenRefill,
       "isdnParamsTokenRemain": isdnParamsTokenRemain,
       "bootp": bootp,
       "bootpActive": bootpActive,
       "bootpBumpable": bootpBumpable,
       "bootpIdle": bootpIdle,
       "bootpIdleThreshold": bootpIdleThreshold,
       "bootpIsdnName": bootpIsdnName,
       "bootpAddress": bootpAddress,
       "bootpDelaySecs": bootpDelaySecs,
       "dhcpProxyActive": dhcpProxyActive,
       "referenceAddress": referenceAddress,
       "minPoolSize": minPoolSize,
       "traps": traps,
       "alarms": alarms,
       "alarmCode": alarmCode,
       "alarmText": alarmText,
       "isdnFailCause": isdnFailCause,
       "isdnFailDestination": isdnFailDestination,
       "q931FailCauseCode": q931FailCauseCode,
       "dass2FailCauseCode": dass2FailCauseCode,
       "briFailCauseCode": briFailCauseCode,
       "radius": radius,
       "radiusReplyCode": radiusReplyCode,
       "radiusUsername": radiusUsername,
       "login": login,
       "loginCode": loginCode,
       "registration": registration,
       "regArpeggio": regArpeggio,
       "arpStandard": arpStandard,
       "arpFocus": arpFocus,
       "arpOffice": arpOffice,
       "arpPlus": arpPlus,
       "arpMultiLan": arpMultiLan,
       "arpLite": arpLite,
       "arpPlusRPrimary": arpPlusRPrimary,
       "arpPlusRBasic": arpPlusRBasic,
       "officeConnect": officeConnect,
       "officeConnectRemote510s": officeConnectRemote510s,
       "officeConnectRemote520s": officeConnectRemote520s,
       "officeConnectRemote530s": officeConnectRemote530s,
       "officeConnectRemote510u": officeConnectRemote510u,
       "officeConnectRemote520u": officeConnectRemote520u,
       "officeConnectRemote530u": officeConnectRemote530u,
       "officeConnectRemote531s": officeConnectRemote531s,
       "officeConnectRemote531u": officeConnectRemote531u,
       "accessBuilder": accessBuilder,
       "accessBuilderRemoteUser400s": accessBuilderRemoteUser400s,
       "accessBuilderRemoteUser400u": accessBuilderRemoteUser400u,
       "accessBuilderInternet400s": accessBuilderInternet400s,
       "accessBuilderInternet400u": accessBuilderInternet400u,
       "accessBuilderRemoteOffice500": accessBuilderRemoteOffice500,
       "accessBuilderRemoteOffice600": accessBuilderRemoteOffice600,
       "accessBuilderRemoteOffice700": accessBuilderRemoteOffice700,
       "accessBuilder7000BriBridgeRouter": accessBuilder7000BriBridgeRouter,
       "accessBuilder7000PriBridgeRouter": accessBuilder7000PriBridgeRouter,
       "serviceConnect2000": serviceConnect2000,
       "serviceConnect2000Base": serviceConnect2000Base,
       "serviceConnect2000BaseBri": serviceConnect2000BaseBri,
       "serviceConnect2000BasePri": serviceConnect2000BasePri,
       "cscmInfo": cscmInfo,
       "cscmEventNumber": cscmEventNumber,
       "cscmOriginatingIP": cscmOriginatingIP,
       "cscmTrapDetail": cscmTrapDetail}
)
