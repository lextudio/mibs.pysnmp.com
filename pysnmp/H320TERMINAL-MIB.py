# SNMP MIB module (H320TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H320TERMINAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:40 2024
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

(IsdnSignalingProtocol,) = mibBuilder.importSymbols(
    "ISDN-MIB",
    "IsdnSignalingProtocol")

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
 experimental,
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
    "experimental",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h320TerminalMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 320, 3)
)
h320TerminalMIB.setRevisions(
        ("1998-08-01 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LineRates(Integer32, TextualConvention):
    status = "current"


class VideoFormats(Integer32, TextualConvention):
    status = "current"


class AudioTypes(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("current")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 2),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysContact.setStatus("current")


class _Syst35CountryCode_Type(Integer32):
    """Custom type syst35CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Syst35CountryCode_Type.__name__ = "Integer32"
_Syst35CountryCode_Object = MibScalar
syst35CountryCode = _Syst35CountryCode_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 3),
    _Syst35CountryCode_Type()
)
syst35CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syst35CountryCode.setStatus("current")


class _Syst35CountryCodeExtention_Type(Integer32):
    """Custom type syst35CountryCodeExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Syst35CountryCodeExtention_Type.__name__ = "Integer32"
_Syst35CountryCodeExtention_Object = MibScalar
syst35CountryCodeExtention = _Syst35CountryCodeExtention_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 4),
    _Syst35CountryCodeExtention_Type()
)
syst35CountryCodeExtention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syst35CountryCodeExtention.setStatus("current")


class _Syst35ManufacturerCode_Type(Integer32):
    """Custom type syst35ManufacturerCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Syst35ManufacturerCode_Type.__name__ = "Integer32"
_Syst35ManufacturerCode_Object = MibScalar
syst35ManufacturerCode = _Syst35ManufacturerCode_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 5),
    _Syst35ManufacturerCode_Type()
)
syst35ManufacturerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syst35ManufacturerCode.setStatus("current")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_SysH320TerminalUptime_Type = TimeTicks
_SysH320TerminalUptime_Object = MibScalar
sysH320TerminalUptime = _SysH320TerminalUptime_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 7),
    _SysH320TerminalUptime_Type()
)
sysH320TerminalUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysH320TerminalUptime.setStatus("current")
_SysH320TerminalLocalTime_Type = DateAndTime
_SysH320TerminalLocalTime_Object = MibScalar
sysH320TerminalLocalTime = _SysH320TerminalLocalTime_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 8),
    _SysH320TerminalLocalTime_Type()
)
sysH320TerminalLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysH320TerminalLocalTime.setStatus("current")


class _SysH320TerminalDiagnostics_Type(Integer32):
    """Custom type sysH320TerminalDiagnostics based on Integer32"""
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
        *(("hardwareFault", 3),
          ("noResults", 1),
          ("passed", 2),
          ("softwareFault", 4))
    )


_SysH320TerminalDiagnostics_Type.__name__ = "Integer32"
_SysH320TerminalDiagnostics_Object = MibScalar
sysH320TerminalDiagnostics = _SysH320TerminalDiagnostics_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 9),
    _SysH320TerminalDiagnostics_Type()
)
sysH320TerminalDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysH320TerminalDiagnostics.setStatus("current")


class _SysH320TerminalStatus_Type(Integer32):
    """Custom type sysH320TerminalStatus based on Integer32"""
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
        *(("callHangUp", 3),
          ("callSetup", 1),
          ("callinProgress", 2),
          ("idle", 4))
    )


_SysH320TerminalStatus_Type.__name__ = "Integer32"
_SysH320TerminalStatus_Object = MibScalar
sysH320TerminalStatus = _SysH320TerminalStatus_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 10),
    _SysH320TerminalStatus_Type()
)
sysH320TerminalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysH320TerminalStatus.setStatus("current")
_SysH320TerminalIfType_Type = Integer32
_SysH320TerminalIfType_Object = MibScalar
sysH320TerminalIfType = _SysH320TerminalIfType_Object(
    (1, 3, 6, 1, 3, 320, 3, 1, 11),
    _SysH320TerminalIfType_Type()
)
sysH320TerminalIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysH320TerminalIfType.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 2)
)


class _ConfigH320TerminalSiteName_Type(DisplayString):
    """Custom type configH320TerminalSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigH320TerminalSiteName_Type.__name__ = "DisplayString"
_ConfigH320TerminalSiteName_Object = MibScalar
configH320TerminalSiteName = _ConfigH320TerminalSiteName_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 1),
    _ConfigH320TerminalSiteName_Type()
)
configH320TerminalSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320TerminalSiteName.setStatus("current")


class _ConfigH320TerminalVideoSystem_Type(Integer32):
    """Custom type configH320TerminalVideoSystem based on Integer32"""
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
        *(("ntsc", 1),
          ("others", 4),
          ("pal", 2),
          ("secam", 3))
    )


_ConfigH320TerminalVideoSystem_Type.__name__ = "Integer32"
_ConfigH320TerminalVideoSystem_Object = MibScalar
configH320TerminalVideoSystem = _ConfigH320TerminalVideoSystem_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 2),
    _ConfigH320TerminalVideoSystem_Type()
)
configH320TerminalVideoSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320TerminalVideoSystem.setStatus("current")
_ConfigH320TerminalIPAddress_Type = IpAddress
_ConfigH320TerminalIPAddress_Object = MibScalar
configH320TerminalIPAddress = _ConfigH320TerminalIPAddress_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 3),
    _ConfigH320TerminalIPAddress_Type()
)
configH320TerminalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320TerminalIPAddress.setStatus("current")
_ConfigH320ISDNSwitchType_Type = IsdnSignalingProtocol
_ConfigH320ISDNSwitchType_Object = MibScalar
configH320ISDNSwitchType = _ConfigH320ISDNSwitchType_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 4),
    _ConfigH320ISDNSwitchType_Type()
)
configH320ISDNSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320ISDNSwitchType.setStatus("current")
_ConfigH320ISDNAddrNumber_Type = Integer32
_ConfigH320ISDNAddrNumber_Object = MibScalar
configH320ISDNAddrNumber = _ConfigH320ISDNAddrNumber_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 5),
    _ConfigH320ISDNAddrNumber_Type()
)
configH320ISDNAddrNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320ISDNAddrNumber.setStatus("current")
_ConfigISDNAddrTable_Object = MibTable
configISDNAddrTable = _ConfigISDNAddrTable_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 6)
)
if mibBuilder.loadTexts:
    configISDNAddrTable.setStatus("current")
_ConfigISDNAddrEntry_Object = MibTableRow
configISDNAddrEntry = _ConfigISDNAddrEntry_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 6, 1)
)
configISDNAddrEntry.setIndexNames(
    (0, "H320TERMINAL-MIB", "configH320AddrIndex"),
)
if mibBuilder.loadTexts:
    configISDNAddrEntry.setStatus("current")


class _ConfigH320AddrIndex_Type(Integer32):
    """Custom type configH320AddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ConfigH320AddrIndex_Type.__name__ = "Integer32"
_ConfigH320AddrIndex_Object = MibTableColumn
configH320AddrIndex = _ConfigH320AddrIndex_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 6, 1, 1),
    _ConfigH320AddrIndex_Type()
)
configH320AddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configH320AddrIndex.setStatus("current")


class _ConfigH320ISDNAddress_Type(DisplayString):
    """Custom type configH320ISDNAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigH320ISDNAddress_Type.__name__ = "DisplayString"
_ConfigH320ISDNAddress_Object = MibTableColumn
configH320ISDNAddress = _ConfigH320ISDNAddress_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 6, 1, 2),
    _ConfigH320ISDNAddress_Type()
)
configH320ISDNAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320ISDNAddress.setStatus("current")


class _ConfigH320ISDNSPID_Type(DisplayString):
    """Custom type configH320ISDNSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigH320ISDNSPID_Type.__name__ = "DisplayString"
_ConfigH320ISDNSPID_Object = MibTableColumn
configH320ISDNSPID = _ConfigH320ISDNSPID_Object(
    (1, 3, 6, 1, 3, 320, 3, 2, 6, 1, 3),
    _ConfigH320ISDNSPID_Type()
)
configH320ISDNSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configH320ISDNSPID.setStatus("current")
_CallSites_ObjectIdentity = ObjectIdentity
callSites = _CallSites_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 3)
)
_H320CallSiteNumber_Type = Integer32
_H320CallSiteNumber_Object = MibScalar
h320CallSiteNumber = _H320CallSiteNumber_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 1),
    _H320CallSiteNumber_Type()
)
h320CallSiteNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h320CallSiteNumber.setStatus("current")


class _H320XferNextIndex_Type(Integer32):
    """Custom type h320XferNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H320XferNextIndex_Type.__name__ = "Integer32"
_H320XferNextIndex_Object = MibScalar
h320XferNextIndex = _H320XferNextIndex_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 2),
    _H320XferNextIndex_Type()
)
h320XferNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320XferNextIndex.setStatus("current")
_H320CallSiteTable_Object = MibTable
h320CallSiteTable = _H320CallSiteTable_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3)
)
if mibBuilder.loadTexts:
    h320CallSiteTable.setStatus("current")
_H320CallSiteEntry_Object = MibTableRow
h320CallSiteEntry = _H320CallSiteEntry_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1)
)
h320CallSiteEntry.setIndexNames(
    (0, "H320TERMINAL-MIB", "h320SiteIndex"),
)
if mibBuilder.loadTexts:
    h320CallSiteEntry.setStatus("current")


class _H320SiteIndex_Type(Integer32):
    """Custom type h320SiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H320SiteIndex_Type.__name__ = "Integer32"
_H320SiteIndex_Object = MibTableColumn
h320SiteIndex = _H320SiteIndex_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 1),
    _H320SiteIndex_Type()
)
h320SiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h320SiteIndex.setStatus("current")


class _H320SiteName_Type(DisplayString):
    """Custom type h320SiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H320SiteName_Type.__name__ = "DisplayString"
_H320SiteName_Object = MibTableColumn
h320SiteName = _H320SiteName_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 2),
    _H320SiteName_Type()
)
h320SiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320SiteName.setStatus("current")
_H320SiteIfType_Type = Integer32
_H320SiteIfType_Object = MibTableColumn
h320SiteIfType = _H320SiteIfType_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 3),
    _H320SiteIfType_Type()
)
h320SiteIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320SiteIfType.setStatus("current")
_H320SiteLineRate_Type = LineRates
_H320SiteLineRate_Object = MibTableColumn
h320SiteLineRate = _H320SiteLineRate_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 4),
    _H320SiteLineRate_Type()
)
h320SiteLineRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320SiteLineRate.setStatus("current")


class _H320CallMode_Type(Integer32):
    """Custom type h320CallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 2),
          ("manualConfig", 1))
    )


_H320CallMode_Type.__name__ = "Integer32"
_H320CallMode_Object = MibTableColumn
h320CallMode = _H320CallMode_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 5),
    _H320CallMode_Type()
)
h320CallMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320CallMode.setStatus("current")
_H320VideoMode_Type = VideoFormats
_H320VideoMode_Object = MibTableColumn
h320VideoMode = _H320VideoMode_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 6),
    _H320VideoMode_Type()
)
h320VideoMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320VideoMode.setStatus("current")
_H320AudioMode_Type = AudioTypes
_H320AudioMode_Object = MibTableColumn
h320AudioMode = _H320AudioMode_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 7),
    _H320AudioMode_Type()
)
h320AudioMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320AudioMode.setStatus("current")
_H320ISDNAddrNumber_Type = Integer32
_H320ISDNAddrNumber_Object = MibTableColumn
h320ISDNAddrNumber = _H320ISDNAddrNumber_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 8),
    _H320ISDNAddrNumber_Type()
)
h320ISDNAddrNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320ISDNAddrNumber.setStatus("current")
_H320SiteRowStatus_Type = RowStatus
_H320SiteRowStatus_Object = MibTableColumn
h320SiteRowStatus = _H320SiteRowStatus_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 3, 1, 9),
    _H320SiteRowStatus_Type()
)
h320SiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320SiteRowStatus.setStatus("current")
_H320ISDNAddrTable_Object = MibTable
h320ISDNAddrTable = _H320ISDNAddrTable_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 4)
)
if mibBuilder.loadTexts:
    h320ISDNAddrTable.setStatus("current")
_H320ISDNAddrEntry_Object = MibTableRow
h320ISDNAddrEntry = _H320ISDNAddrEntry_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 4, 1)
)
h320ISDNAddrEntry.setIndexNames(
    (0, "H320TERMINAL-MIB", "h320SiteIndex"),
    (0, "H320TERMINAL-MIB", "h320AddrIndex"),
)
if mibBuilder.loadTexts:
    h320ISDNAddrEntry.setStatus("current")


class _H320AddrIndex_Type(Unsigned32):
    """Custom type h320AddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_H320AddrIndex_Type.__name__ = "Unsigned32"
_H320AddrIndex_Object = MibTableColumn
h320AddrIndex = _H320AddrIndex_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 4, 1, 1),
    _H320AddrIndex_Type()
)
h320AddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h320AddrIndex.setStatus("current")


class _H320ISDNAddress_Type(DisplayString):
    """Custom type h320ISDNAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H320ISDNAddress_Type.__name__ = "DisplayString"
_H320ISDNAddress_Object = MibTableColumn
h320ISDNAddress = _H320ISDNAddress_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 4, 1, 2),
    _H320ISDNAddress_Type()
)
h320ISDNAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320ISDNAddress.setStatus("current")
_H320AddrRowStatus_Type = RowStatus
_H320AddrRowStatus_Object = MibTableColumn
h320AddrRowStatus = _H320AddrRowStatus_Object(
    (1, 3, 6, 1, 3, 320, 3, 3, 4, 1, 3),
    _H320AddrRowStatus_Type()
)
h320AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h320AddrRowStatus.setStatus("current")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 4)
)


class _ControlH320TerminalAdmin_Type(Integer32):
    """Custom type controlH320TerminalAdmin based on Integer32"""
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
        *(("diagnose", 3),
          ("reset", 2),
          ("run", 1),
          ("stop", 4))
    )


_ControlH320TerminalAdmin_Type.__name__ = "Integer32"
_ControlH320TerminalAdmin_Object = MibScalar
controlH320TerminalAdmin = _ControlH320TerminalAdmin_Object(
    (1, 3, 6, 1, 3, 320, 3, 4, 1),
    _ControlH320TerminalAdmin_Type()
)
controlH320TerminalAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlH320TerminalAdmin.setStatus("current")
_ControlH320TerminalCallSetUp_Type = Integer32
_ControlH320TerminalCallSetUp_Object = MibScalar
controlH320TerminalCallSetUp = _ControlH320TerminalCallSetUp_Object(
    (1, 3, 6, 1, 3, 320, 3, 4, 2),
    _ControlH320TerminalCallSetUp_Type()
)
controlH320TerminalCallSetUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlH320TerminalCallSetUp.setStatus("current")
_ControlH320TerminalCallHangup_Type = Integer32
_ControlH320TerminalCallHangup_Object = MibScalar
controlH320TerminalCallHangup = _ControlH320TerminalCallHangup_Object(
    (1, 3, 6, 1, 3, 320, 3, 4, 3),
    _ControlH320TerminalCallHangup_Type()
)
controlH320TerminalCallHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlH320TerminalCallHangup.setStatus("current")


class _ControlH320EnableLocalLoopback_Type(Integer32):
    """Custom type controlH320EnableLocalLoopback based on Integer32"""
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


_ControlH320EnableLocalLoopback_Type.__name__ = "Integer32"
_ControlH320EnableLocalLoopback_Object = MibScalar
controlH320EnableLocalLoopback = _ControlH320EnableLocalLoopback_Object(
    (1, 3, 6, 1, 3, 320, 3, 4, 4),
    _ControlH320EnableLocalLoopback_Type()
)
controlH320EnableLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlH320EnableLocalLoopback.setStatus("current")


class _ControlH320EnableRemoteLoopback_Type(Integer32):
    """Custom type controlH320EnableRemoteLoopback based on Integer32"""
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


_ControlH320EnableRemoteLoopback_Type.__name__ = "Integer32"
_ControlH320EnableRemoteLoopback_Object = MibScalar
controlH320EnableRemoteLoopback = _ControlH320EnableRemoteLoopback_Object(
    (1, 3, 6, 1, 3, 320, 3, 4, 5),
    _ControlH320EnableRemoteLoopback_Type()
)
controlH320EnableRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlH320EnableRemoteLoopback.setStatus("current")
_H320TerminalMIBConfs_ObjectIdentity = ObjectIdentity
h320TerminalMIBConfs = _H320TerminalMIBConfs_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 5)
)
_H320TerminalMIIBGroups_ObjectIdentity = ObjectIdentity
h320TerminalMIIBGroups = _H320TerminalMIIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 5, 1)
)
_H320TerminalMIBCompl_ObjectIdentity = ObjectIdentity
h320TerminalMIBCompl = _H320TerminalMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 3, 320, 3, 5, 2)
)

# Managed Objects groups

h320TerminalDesrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 320, 3, 5, 1, 1)
)
h320TerminalDesrGroup.setObjects(
      *(("H320TERMINAL-MIB", "sysDescr"),
        ("H320TERMINAL-MIB", "sysContact"),
        ("H320TERMINAL-MIB", "syst35CountryCode"),
        ("H320TERMINAL-MIB", "syst35CountryCodeExtention"),
        ("H320TERMINAL-MIB", "syst35ManufacturerCode"),
        ("H320TERMINAL-MIB", "sysLocation"),
        ("H320TERMINAL-MIB", "sysH320TerminalUptime"),
        ("H320TERMINAL-MIB", "sysH320TerminalLocalTime"),
        ("H320TERMINAL-MIB", "sysH320TerminalDiagnostics"),
        ("H320TERMINAL-MIB", "sysH320TerminalStatus"),
        ("H320TERMINAL-MIB", "sysH320TerminalIfType"))
)
if mibBuilder.loadTexts:
    h320TerminalDesrGroup.setStatus("current")

h320TerminalConfgGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 320, 3, 5, 1, 2)
)
h320TerminalConfgGroup.setObjects(
      *(("H320TERMINAL-MIB", "configH320TerminalSiteName"),
        ("H320TERMINAL-MIB", "configH320TerminalVideoSystem"),
        ("H320TERMINAL-MIB", "configH320TerminalIPAddress"),
        ("H320TERMINAL-MIB", "configH320ISDNSwitchType"),
        ("H320TERMINAL-MIB", "configH320ISDNAddrNumber"),
        ("H320TERMINAL-MIB", "configH320ISDNAddress"),
        ("H320TERMINAL-MIB", "configH320ISDNSPID"))
)
if mibBuilder.loadTexts:
    h320TerminalConfgGroup.setStatus("current")

h320TerminalCallSitesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 320, 3, 5, 1, 3)
)
h320TerminalCallSitesGroup.setObjects(
      *(("H320TERMINAL-MIB", "h320CallSiteNumber"),
        ("H320TERMINAL-MIB", "h320XferNextIndex"),
        ("H320TERMINAL-MIB", "h320SiteName"),
        ("H320TERMINAL-MIB", "h320SiteIfType"),
        ("H320TERMINAL-MIB", "h320SiteLineRate"),
        ("H320TERMINAL-MIB", "h320CallMode"),
        ("H320TERMINAL-MIB", "h320VideoMode"),
        ("H320TERMINAL-MIB", "h320AudioMode"),
        ("H320TERMINAL-MIB", "h320ISDNAddrNumber"),
        ("H320TERMINAL-MIB", "h320SiteRowStatus"),
        ("H320TERMINAL-MIB", "h320ISDNAddress"),
        ("H320TERMINAL-MIB", "h320AddrRowStatus"))
)
if mibBuilder.loadTexts:
    h320TerminalCallSitesGroup.setStatus("current")

h320TerminalControlGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 320, 3, 5, 1, 4)
)
h320TerminalControlGroup.setObjects(
      *(("H320TERMINAL-MIB", "controlH320TerminalAdmin"),
        ("H320TERMINAL-MIB", "controlH320TerminalCallSetUp"),
        ("H320TERMINAL-MIB", "controlH320TerminalCallHangup"),
        ("H320TERMINAL-MIB", "controlH320EnableLocalLoopback"),
        ("H320TERMINAL-MIB", "controlH320EnableRemoteLoopback"))
)
if mibBuilder.loadTexts:
    h320TerminalControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h320TErminalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 320, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    h320TErminalCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H320TERMINAL-MIB",
    **{"LineRates": LineRates,
       "VideoFormats": VideoFormats,
       "AudioTypes": AudioTypes,
       "h320TerminalMIB": h320TerminalMIB,
       "system": system,
       "sysDescr": sysDescr,
       "sysContact": sysContact,
       "syst35CountryCode": syst35CountryCode,
       "syst35CountryCodeExtention": syst35CountryCodeExtention,
       "syst35ManufacturerCode": syst35ManufacturerCode,
       "sysLocation": sysLocation,
       "sysH320TerminalUptime": sysH320TerminalUptime,
       "sysH320TerminalLocalTime": sysH320TerminalLocalTime,
       "sysH320TerminalDiagnostics": sysH320TerminalDiagnostics,
       "sysH320TerminalStatus": sysH320TerminalStatus,
       "sysH320TerminalIfType": sysH320TerminalIfType,
       "configuration": configuration,
       "configH320TerminalSiteName": configH320TerminalSiteName,
       "configH320TerminalVideoSystem": configH320TerminalVideoSystem,
       "configH320TerminalIPAddress": configH320TerminalIPAddress,
       "configH320ISDNSwitchType": configH320ISDNSwitchType,
       "configH320ISDNAddrNumber": configH320ISDNAddrNumber,
       "configISDNAddrTable": configISDNAddrTable,
       "configISDNAddrEntry": configISDNAddrEntry,
       "configH320AddrIndex": configH320AddrIndex,
       "configH320ISDNAddress": configH320ISDNAddress,
       "configH320ISDNSPID": configH320ISDNSPID,
       "callSites": callSites,
       "h320CallSiteNumber": h320CallSiteNumber,
       "h320XferNextIndex": h320XferNextIndex,
       "h320CallSiteTable": h320CallSiteTable,
       "h320CallSiteEntry": h320CallSiteEntry,
       "h320SiteIndex": h320SiteIndex,
       "h320SiteName": h320SiteName,
       "h320SiteIfType": h320SiteIfType,
       "h320SiteLineRate": h320SiteLineRate,
       "h320CallMode": h320CallMode,
       "h320VideoMode": h320VideoMode,
       "h320AudioMode": h320AudioMode,
       "h320ISDNAddrNumber": h320ISDNAddrNumber,
       "h320SiteRowStatus": h320SiteRowStatus,
       "h320ISDNAddrTable": h320ISDNAddrTable,
       "h320ISDNAddrEntry": h320ISDNAddrEntry,
       "h320AddrIndex": h320AddrIndex,
       "h320ISDNAddress": h320ISDNAddress,
       "h320AddrRowStatus": h320AddrRowStatus,
       "control": control,
       "controlH320TerminalAdmin": controlH320TerminalAdmin,
       "controlH320TerminalCallSetUp": controlH320TerminalCallSetUp,
       "controlH320TerminalCallHangup": controlH320TerminalCallHangup,
       "controlH320EnableLocalLoopback": controlH320EnableLocalLoopback,
       "controlH320EnableRemoteLoopback": controlH320EnableRemoteLoopback,
       "h320TerminalMIBConfs": h320TerminalMIBConfs,
       "h320TerminalMIIBGroups": h320TerminalMIIBGroups,
       "h320TerminalDesrGroup": h320TerminalDesrGroup,
       "h320TerminalConfgGroup": h320TerminalConfgGroup,
       "h320TerminalCallSitesGroup": h320TerminalCallSitesGroup,
       "h320TerminalControlGroup": h320TerminalControlGroup,
       "h320TerminalMIBCompl": h320TerminalMIBCompl,
       "h320TErminalCompliance": h320TErminalCompliance}
)
