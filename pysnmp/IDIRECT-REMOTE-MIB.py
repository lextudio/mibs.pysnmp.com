# SNMP MIB module (IDIRECT-REMOTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IDIRECT-REMOTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:05 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

iDirectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13732)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IDirectObjects_ObjectIdentity = ObjectIdentity
iDirectObjects = _IDirectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1)
)
_Netmodem_ObjectIdentity = ObjectIdentity
netmodem = _Netmodem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1)
)


class _NetModemEntries_Type(Unsigned32):
    """Custom type netModemEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NetModemEntries_Type.__name__ = "Unsigned32"
_NetModemEntries_Object = MibScalar
netModemEntries = _NetModemEntries_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 0),
    _NetModemEntries_Type()
)
netModemEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netModemEntries.setStatus("current")
_NetModemTable_Object = MibTable
netModemTable = _NetModemTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1)
)
if mibBuilder.loadTexts:
    netModemTable.setStatus("current")
_NetModemEntry_Object = MibTableRow
netModemEntry = _NetModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1)
)
netModemEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "netdid"),
)
if mibBuilder.loadTexts:
    netModemEntry.setStatus("current")


class _Netdid_Type(Unsigned32):
    """Custom type netdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Netdid_Type.__name__ = "Unsigned32"
_Netdid_Object = MibTableColumn
netdid = _Netdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 1),
    _Netdid_Type()
)
netdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netdid.setStatus("current")


class _Nmppid_Type(Unsigned32):
    """Custom type nmppid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nmppid_Type.__name__ = "Unsigned32"
_Nmppid_Object = MibTableColumn
nmppid = _Nmppid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 2),
    _Nmppid_Type()
)
nmppid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmppid.setStatus("current")


class _Networkid_Type(Unsigned32):
    """Custom type networkid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Networkid_Type.__name__ = "Unsigned32"
_Networkid_Object = MibTableColumn
networkid = _Networkid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 3),
    _Networkid_Type()
)
networkid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkid.setStatus("current")


class _Nmteleportid_Type(Unsigned32):
    """Custom type nmteleportid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nmteleportid_Type.__name__ = "Unsigned32"
_Nmteleportid_Object = MibTableColumn
nmteleportid = _Nmteleportid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 4),
    _Nmteleportid_Type()
)
nmteleportid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmteleportid.setStatus("current")


class _Nmid_Type(Unsigned32):
    """Custom type nmid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Nmid_Type.__name__ = "Unsigned32"
_Nmid_Object = MibTableColumn
nmid = _Nmid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 5),
    _Nmid_Type()
)
nmid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmid.setStatus("current")


class _Inroutegroupid_Type(Unsigned32):
    """Custom type inroutegroupid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Inroutegroupid_Type.__name__ = "Unsigned32"
_Inroutegroupid_Object = MibTableColumn
inroutegroupid = _Inroutegroupid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 6),
    _Inroutegroupid_Type()
)
inroutegroupid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inroutegroupid.setStatus("current")


class _Nmname_Type(DisplayString):
    """Custom type nmname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Nmname_Type.__name__ = "DisplayString"
_Nmname_Object = MibTableColumn
nmname = _Nmname_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 7),
    _Nmname_Type()
)
nmname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmname.setStatus("current")


class _Ethipadr_Type(DisplayString):
    """Custom type ethipadr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ethipadr_Type.__name__ = "DisplayString"
_Ethipadr_Object = MibTableColumn
ethipadr = _Ethipadr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 8),
    _Ethipadr_Type()
)
ethipadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethipadr.setStatus("current")


class _Dcmslotnum_Type(Unsigned32):
    """Custom type dcmslotnum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dcmslotnum_Type.__name__ = "Unsigned32"
_Dcmslotnum_Object = MibTableColumn
dcmslotnum = _Dcmslotnum_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 9),
    _Dcmslotnum_Type()
)
dcmslotnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcmslotnum.setStatus("current")


class _Chassid_Type(Unsigned32):
    """Custom type chassid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Chassid_Type.__name__ = "Unsigned32"
_Chassid_Object = MibTableColumn
chassid = _Chassid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 10),
    _Chassid_Type()
)
chassid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassid.setStatus("current")


class _Typeid_Type(Integer32):
    """Custom type typeid based on Integer32"""
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
        *(("fsRepeater", 5),
          ("remote", 3),
          ("rxHub", 1),
          ("standby", 4),
          ("standbyFsRepeater", 6),
          ("txHub", 0),
          ("txRxHub", 2))
    )


_Typeid_Type.__name__ = "Integer32"
_Typeid_Object = MibTableColumn
typeid = _Typeid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 11),
    _Typeid_Type()
)
typeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    typeid.setStatus("current")


class _Nmstate_Type(Integer32):
    """Custom type nmstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("offline", 4),
          ("red", 2),
          ("yellow", 1),
          ("yellowRed", 3))
    )


_Nmstate_Type.__name__ = "Integer32"
_Nmstate_Object = MibTableColumn
nmstate = _Nmstate_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 12),
    _Nmstate_Type()
)
nmstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstate.setStatus("current")


class _Nmwarnings_Type(DisplayString):
    """Custom type nmwarnings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Nmwarnings_Type.__name__ = "DisplayString"
_Nmwarnings_Object = MibTableColumn
nmwarnings = _Nmwarnings_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 13),
    _Nmwarnings_Type()
)
nmwarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmwarnings.setStatus("current")


class _Nmalarms_Type(DisplayString):
    """Custom type nmalarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Nmalarms_Type.__name__ = "DisplayString"
_Nmalarms_Object = MibTableColumn
nmalarms = _Nmalarms_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 14),
    _Nmalarms_Type()
)
nmalarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmalarms.setStatus("current")


class _Nmstatus_Type(DisplayString):
    """Custom type nmstatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Nmstatus_Type.__name__ = "DisplayString"
_Nmstatus_Object = MibTableColumn
nmstatus = _Nmstatus_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 15),
    _Nmstatus_Type()
)
nmstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmstatus.setStatus("current")


class _Geoloc_Type(DisplayString):
    """Custom type geoloc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Geoloc_Type.__name__ = "DisplayString"
_Geoloc_Object = MibTableColumn
geoloc = _Geoloc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 1, 1, 1, 16),
    _Geoloc_Type()
)
geoloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    geoloc.setStatus("current")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2)
)


class _ChassisEntries_Type(Unsigned32):
    """Custom type chassisEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChassisEntries_Type.__name__ = "Unsigned32"
_ChassisEntries_Object = MibScalar
chassisEntries = _ChassisEntries_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 0),
    _ChassisEntries_Type()
)
chassisEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisEntries.setStatus("current")
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "chassisid"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")


class _Chassisid_Type(Unsigned32):
    """Custom type chassisid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Chassisid_Type.__name__ = "Unsigned32"
_Chassisid_Object = MibTableColumn
chassisid = _Chassisid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1, 1),
    _Chassisid_Type()
)
chassisid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisid.setStatus("current")


class _Chassisname_Type(DisplayString):
    """Custom type chassisname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chassisname_Type.__name__ = "DisplayString"
_Chassisname_Object = MibTableColumn
chassisname = _Chassisname_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1, 2),
    _Chassisname_Type()
)
chassisname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisname.setStatus("current")


class _Chstate_Type(Integer32):
    """Custom type chstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("offline", 4),
          ("red", 2),
          ("yellow", 1),
          ("yellowRed", 3))
    )


_Chstate_Type.__name__ = "Integer32"
_Chstate_Object = MibTableColumn
chstate = _Chstate_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1, 3),
    _Chstate_Type()
)
chstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chstate.setStatus("current")


class _Chwarnings_Type(DisplayString):
    """Custom type chwarnings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chwarnings_Type.__name__ = "DisplayString"
_Chwarnings_Object = MibTableColumn
chwarnings = _Chwarnings_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1, 4),
    _Chwarnings_Type()
)
chwarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chwarnings.setStatus("current")


class _Chalarms_Type(DisplayString):
    """Custom type chalarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Chalarms_Type.__name__ = "DisplayString"
_Chalarms_Object = MibTableColumn
chalarms = _Chalarms_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 2, 1, 1, 5),
    _Chalarms_Type()
)
chalarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chalarms.setStatus("current")
_Pp_ObjectIdentity = ObjectIdentity
pp = _Pp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3)
)


class _PpEntries_Type(Unsigned32):
    """Custom type ppEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PpEntries_Type.__name__ = "Unsigned32"
_PpEntries_Object = MibScalar
ppEntries = _PpEntries_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 0),
    _PpEntries_Type()
)
ppEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppEntries.setStatus("current")
_PpTable_Object = MibTable
ppTable = _PpTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ppTable.setStatus("current")
_PpEntry_Object = MibTableRow
ppEntry = _PpEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1)
)
ppEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "ppid"),
)
if mibBuilder.loadTexts:
    ppEntry.setStatus("current")


class _Ppid_Type(Unsigned32):
    """Custom type ppid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ppid_Type.__name__ = "Unsigned32"
_Ppid_Object = MibTableColumn
ppid = _Ppid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 1),
    _Ppid_Type()
)
ppid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppid.setStatus("current")


class _Ppname_Type(DisplayString):
    """Custom type ppname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ppname_Type.__name__ = "DisplayString"
_Ppname_Object = MibTableColumn
ppname = _Ppname_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 2),
    _Ppname_Type()
)
ppname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppname.setStatus("current")


class _Ppteleportid_Type(Unsigned32):
    """Custom type ppteleportid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ppteleportid_Type.__name__ = "Unsigned32"
_Ppteleportid_Object = MibTableColumn
ppteleportid = _Ppteleportid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 3),
    _Ppteleportid_Type()
)
ppteleportid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppteleportid.setStatus("current")


class _Ppstate_Type(Integer32):
    """Custom type ppstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("offline", 4),
          ("red", 2),
          ("yellow", 1),
          ("yellowRed", 3))
    )


_Ppstate_Type.__name__ = "Integer32"
_Ppstate_Object = MibTableColumn
ppstate = _Ppstate_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 4),
    _Ppstate_Type()
)
ppstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppstate.setStatus("current")


class _Ppwarnings_Type(DisplayString):
    """Custom type ppwarnings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ppwarnings_Type.__name__ = "DisplayString"
_Ppwarnings_Object = MibTableColumn
ppwarnings = _Ppwarnings_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 5),
    _Ppwarnings_Type()
)
ppwarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppwarnings.setStatus("current")


class _Ppalarms_Type(DisplayString):
    """Custom type ppalarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ppalarms_Type.__name__ = "DisplayString"
_Ppalarms_Object = MibTableColumn
ppalarms = _Ppalarms_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 3, 1, 1, 6),
    _Ppalarms_Type()
)
ppalarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ppalarms.setStatus("current")
_Idirectstats_ObjectIdentity = ObjectIdentity
idirectstats = _Idirectstats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4)
)
_IpstatsTable_Object = MibTable
ipstatsTable = _IpstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipstatsTable.setStatus("current")
_IpstatsEntry_Object = MibTableRow
ipstatsEntry = _IpstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1)
)
ipstatsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "nmdid"),
)
if mibBuilder.loadTexts:
    ipstatsEntry.setStatus("current")


class _Nmdid_Type(Unsigned32):
    """Custom type nmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Nmdid_Type.__name__ = "Unsigned32"
_Nmdid_Object = MibTableColumn
nmdid = _Nmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 1),
    _Nmdid_Type()
)
nmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmdid.setStatus("current")
_Rxtcp_Type = Counter64
_Rxtcp_Object = MibTableColumn
rxtcp = _Rxtcp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 2),
    _Rxtcp_Type()
)
rxtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxtcp.setStatus("current")
_Rxudp_Type = Counter64
_Rxudp_Object = MibTableColumn
rxudp = _Rxudp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 3),
    _Rxudp_Type()
)
rxudp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxudp.setStatus("current")
_Rxicmp_Type = Counter64
_Rxicmp_Object = MibTableColumn
rxicmp = _Rxicmp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 4),
    _Rxicmp_Type()
)
rxicmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxicmp.setStatus("current")
_Rxigmp_Type = Counter64
_Rxigmp_Object = MibTableColumn
rxigmp = _Rxigmp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 5),
    _Rxigmp_Type()
)
rxigmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxigmp.setStatus("current")
_Rxhttp_Type = Counter64
_Rxhttp_Object = MibTableColumn
rxhttp = _Rxhttp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 6),
    _Rxhttp_Type()
)
rxhttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxhttp.setStatus("current")
_Rxother_Type = Counter64
_Rxother_Object = MibTableColumn
rxother = _Rxother_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 7),
    _Rxother_Type()
)
rxother.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxother.setStatus("current")
_Txtcp_Type = Counter64
_Txtcp_Object = MibTableColumn
txtcp = _Txtcp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 8),
    _Txtcp_Type()
)
txtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txtcp.setStatus("current")
_Txudp_Type = Counter64
_Txudp_Object = MibTableColumn
txudp = _Txudp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 9),
    _Txudp_Type()
)
txudp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txudp.setStatus("current")
_Txicmp_Type = Counter64
_Txicmp_Object = MibTableColumn
txicmp = _Txicmp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 10),
    _Txicmp_Type()
)
txicmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txicmp.setStatus("current")
_Txigmp_Type = Counter64
_Txigmp_Object = MibTableColumn
txigmp = _Txigmp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 11),
    _Txigmp_Type()
)
txigmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txigmp.setStatus("current")
_Txhttp_Type = Counter64
_Txhttp_Object = MibTableColumn
txhttp = _Txhttp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 12),
    _Txhttp_Type()
)
txhttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txhttp.setStatus("current")
_Txother_Type = Counter64
_Txother_Object = MibTableColumn
txother = _Txother_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 13),
    _Txother_Type()
)
txother.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txother.setStatus("current")


class _Ipstatstime_Type(DisplayString):
    """Custom type ipstatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ipstatstime_Type.__name__ = "DisplayString"
_Ipstatstime_Object = MibTableColumn
ipstatstime = _Ipstatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 1, 1, 14),
    _Ipstatstime_Type()
)
ipstatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstatstime.setStatus("current")
_OtastatsTable_Object = MibTable
otastatsTable = _OtastatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2)
)
if mibBuilder.loadTexts:
    otastatsTable.setStatus("current")
_OtastatsEntry_Object = MibTableRow
otastatsEntry = _OtastatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1)
)
otastatsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "otanmdid"),
)
if mibBuilder.loadTexts:
    otastatsEntry.setStatus("current")


class _Otanmdid_Type(Unsigned32):
    """Custom type otanmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Otanmdid_Type.__name__ = "Unsigned32"
_Otanmdid_Object = MibTableColumn
otanmdid = _Otanmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 1),
    _Otanmdid_Type()
)
otanmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otanmdid.setStatus("current")


class _Otamode_Type(DisplayString):
    """Custom type otamode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Otamode_Type.__name__ = "DisplayString"
_Otamode_Object = MibTableColumn
otamode = _Otamode_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 2),
    _Otamode_Type()
)
otamode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otamode.setStatus("current")
_DownstreamreliableBytes_Type = Counter64
_DownstreamreliableBytes_Object = MibTableColumn
downstreamreliableBytes = _DownstreamreliableBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 3),
    _DownstreamreliableBytes_Type()
)
downstreamreliableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreamreliableBytes.setStatus("current")
_DownstreamunreliableBytes_Type = Counter64
_DownstreamunreliableBytes_Object = MibTableColumn
downstreamunreliableBytes = _DownstreamunreliableBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 4),
    _DownstreamunreliableBytes_Type()
)
downstreamunreliableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreamunreliableBytes.setStatus("current")
_DownstreamoverheadBytes_Type = Counter64
_DownstreamoverheadBytes_Object = MibTableColumn
downstreamoverheadBytes = _DownstreamoverheadBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 5),
    _DownstreamoverheadBytes_Type()
)
downstreamoverheadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreamoverheadBytes.setStatus("current")
_DownstreammulticastBytes_Type = Counter64
_DownstreammulticastBytes_Object = MibTableColumn
downstreammulticastBytes = _DownstreammulticastBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 6),
    _DownstreammulticastBytes_Type()
)
downstreammulticastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreammulticastBytes.setStatus("current")
_DownstreambroadcastBytes_Type = Counter64
_DownstreambroadcastBytes_Object = MibTableColumn
downstreambroadcastBytes = _DownstreambroadcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 7),
    _DownstreambroadcastBytes_Type()
)
downstreambroadcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreambroadcastBytes.setStatus("current")
_DownstreammulticastSymbols_Type = Counter64
_DownstreammulticastSymbols_Object = MibTableColumn
downstreammulticastSymbols = _DownstreammulticastSymbols_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 8),
    _DownstreammulticastSymbols_Type()
)
downstreammulticastSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreammulticastSymbols.setStatus("current")
_DownstreambroadcastSymbols_Type = Counter64
_DownstreambroadcastSymbols_Object = MibTableColumn
downstreambroadcastSymbols = _DownstreambroadcastSymbols_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 9),
    _DownstreambroadcastSymbols_Type()
)
downstreambroadcastSymbols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreambroadcastSymbols.setStatus("current")
_DownstreamtotalKiloBytes_Type = Counter64
_DownstreamtotalKiloBytes_Object = MibTableColumn
downstreamtotalKiloBytes = _DownstreamtotalKiloBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 10),
    _DownstreamtotalKiloBytes_Type()
)
downstreamtotalKiloBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downstreamtotalKiloBytes.setStatus("current")
_UpstreamreliableBytes_Type = Counter64
_UpstreamreliableBytes_Object = MibTableColumn
upstreamreliableBytes = _UpstreamreliableBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 11),
    _UpstreamreliableBytes_Type()
)
upstreamreliableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upstreamreliableBytes.setStatus("current")
_UpstreamunreliableBytes_Type = Counter64
_UpstreamunreliableBytes_Object = MibTableColumn
upstreamunreliableBytes = _UpstreamunreliableBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 12),
    _UpstreamunreliableBytes_Type()
)
upstreamunreliableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upstreamunreliableBytes.setStatus("current")
_UpstreamoverheadBytes_Type = Counter64
_UpstreamoverheadBytes_Object = MibTableColumn
upstreamoverheadBytes = _UpstreamoverheadBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 13),
    _UpstreamoverheadBytes_Type()
)
upstreamoverheadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upstreamoverheadBytes.setStatus("current")
_UpstreamtotalKiloBytes_Type = Counter64
_UpstreamtotalKiloBytes_Object = MibTableColumn
upstreamtotalKiloBytes = _UpstreamtotalKiloBytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 14),
    _UpstreamtotalKiloBytes_Type()
)
upstreamtotalKiloBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upstreamtotalKiloBytes.setStatus("current")


class _Otastatstime_Type(DisplayString):
    """Custom type otastatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Otastatstime_Type.__name__ = "DisplayString"
_Otastatstime_Object = MibTableColumn
otastatstime = _Otastatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 2, 1, 15),
    _Otastatstime_Type()
)
otastatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otastatstime.setStatus("current")
_RemotestatusTable_Object = MibTable
remotestatusTable = _RemotestatusTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3)
)
if mibBuilder.loadTexts:
    remotestatusTable.setStatus("current")
_RemotestatusEntry_Object = MibTableRow
remotestatusEntry = _RemotestatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1)
)
remotestatusEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "rsnmdid"),
)
if mibBuilder.loadTexts:
    remotestatusEntry.setStatus("current")


class _Rsnmdid_Type(Unsigned32):
    """Custom type rsnmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Rsnmdid_Type.__name__ = "Unsigned32"
_Rsnmdid_Object = MibTableColumn
rsnmdid = _Rsnmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 1),
    _Rsnmdid_Type()
)
rsnmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsnmdid.setStatus("current")


class _Downsnr_Type(DisplayString):
    """Custom type downsnr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Downsnr_Type.__name__ = "DisplayString"
_Downsnr_Object = MibTableColumn
downsnr = _Downsnr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 2),
    _Downsnr_Type()
)
downsnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downsnr.setStatus("current")


class _Rstxpower_Type(DisplayString):
    """Custom type rstxpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rstxpower_Type.__name__ = "DisplayString"
_Rstxpower_Object = MibTableColumn
rstxpower = _Rstxpower_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 3),
    _Rstxpower_Type()
)
rstxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstxpower.setStatus("current")


class _Rsrxpower_Type(DisplayString):
    """Custom type rsrxpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rsrxpower_Type.__name__ = "DisplayString"
_Rsrxpower_Object = MibTableColumn
rsrxpower = _Rsrxpower_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 4),
    _Rsrxpower_Type()
)
rsrxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsrxpower.setStatus("current")


class _Digitalrxgain_Type(DisplayString):
    """Custom type digitalrxgain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Digitalrxgain_Type.__name__ = "DisplayString"
_Digitalrxgain_Object = MibTableColumn
digitalrxgain = _Digitalrxgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 5),
    _Digitalrxgain_Type()
)
digitalrxgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalrxgain.setStatus("current")
_Flldac_Type = Integer32
_Flldac_Object = MibTableColumn
flldac = _Flldac_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 6),
    _Flldac_Type()
)
flldac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flldac.setStatus("current")
_Rxcof_Type = Integer32
_Rxcof_Object = MibTableColumn
rxcof = _Rxcof_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 7),
    _Rxcof_Type()
)
rxcof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxcof.setStatus("current")


class _Rstemp_Type(DisplayString):
    """Custom type rstemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rstemp_Type.__name__ = "DisplayString"
_Rstemp_Object = MibTableColumn
rstemp = _Rstemp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 8),
    _Rstemp_Type()
)
rstemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstemp.setStatus("current")
_Tdmlost_Type = Counter32
_Tdmlost_Object = MibTableColumn
tdmlost = _Tdmlost_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 9),
    _Tdmlost_Type()
)
tdmlost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmlost.setStatus("current")
_Scpcerrors_Type = Counter32
_Scpcerrors_Object = MibTableColumn
scpcerrors = _Scpcerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 10),
    _Scpcerrors_Type()
)
scpcerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpcerrors.setStatus("current")
_Rstimeticks_Type = TimeTicks
_Rstimeticks_Object = MibTableColumn
rstimeticks = _Rstimeticks_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 11),
    _Rstimeticks_Type()
)
rstimeticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstimeticks.setStatus("current")


class _Lanport_Type(DisplayString):
    """Custom type lanport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Lanport_Type.__name__ = "DisplayString"
_Lanport_Object = MibTableColumn
lanport = _Lanport_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 12),
    _Lanport_Type()
)
lanport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanport.setStatus("current")


class _Ethmode_Type(DisplayString):
    """Custom type ethmode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ethmode_Type.__name__ = "DisplayString"
_Ethmode_Object = MibTableColumn
ethmode = _Ethmode_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 13),
    _Ethmode_Type()
)
ethmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethmode.setStatus("current")


class _Ethspeed_Type(DisplayString):
    """Custom type ethspeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ethspeed_Type.__name__ = "DisplayString"
_Ethspeed_Object = MibTableColumn
ethspeed = _Ethspeed_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 14),
    _Ethspeed_Type()
)
ethspeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethspeed.setStatus("current")


class _Ethautonegotiate_Type(DisplayString):
    """Custom type ethautonegotiate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ethautonegotiate_Type.__name__ = "DisplayString"
_Ethautonegotiate_Object = MibTableColumn
ethautonegotiate = _Ethautonegotiate_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 15),
    _Ethautonegotiate_Type()
)
ethautonegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethautonegotiate.setStatus("current")


class _Telnetsession_Type(DisplayString):
    """Custom type telnetsession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Telnetsession_Type.__name__ = "DisplayString"
_Telnetsession_Object = MibTableColumn
telnetsession = _Telnetsession_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 16),
    _Telnetsession_Type()
)
telnetsession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetsession.setStatus("current")


class _Isitesession_Type(DisplayString):
    """Custom type isitesession based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Isitesession_Type.__name__ = "DisplayString"
_Isitesession_Object = MibTableColumn
isitesession = _Isitesession_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 17),
    _Isitesession_Type()
)
isitesession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isitesession.setStatus("current")


class _Inmesh_Type(DisplayString):
    """Custom type inmesh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Inmesh_Type.__name__ = "DisplayString"
_Inmesh_Object = MibTableColumn
inmesh = _Inmesh_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 18),
    _Inmesh_Type()
)
inmesh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inmesh.setStatus("current")
_Fastfadecorr_Type = Counter32
_Fastfadecorr_Object = MibTableColumn
fastfadecorr = _Fastfadecorr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 19),
    _Fastfadecorr_Type()
)
fastfadecorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastfadecorr.setStatus("current")
_Crc8error_Type = Counter32
_Crc8error_Object = MibTableColumn
crc8error = _Crc8error_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 20),
    _Crc8error_Type()
)
crc8error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crc8error.setStatus("current")
_Crc32error_Type = Counter32
_Crc32error_Object = MibTableColumn
crc32error = _Crc32error_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 21),
    _Crc32error_Type()
)
crc32error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crc32error.setStatus("current")
_Ncrlost_Type = Counter32
_Ncrlost_Object = MibTableColumn
ncrlost = _Ncrlost_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 22),
    _Ncrlost_Type()
)
ncrlost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncrlost.setStatus("current")
_Plsynclost_Type = Counter32
_Plsynclost_Object = MibTableColumn
plsynclost = _Plsynclost_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 23),
    _Plsynclost_Type()
)
plsynclost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsynclost.setStatus("current")
_Clockdeltacnt_Type = Counter32
_Clockdeltacnt_Object = MibTableColumn
clockdeltacnt = _Clockdeltacnt_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 24),
    _Clockdeltacnt_Type()
)
clockdeltacnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockdeltacnt.setStatus("current")
_Digitalagcgain_Type = Counter32
_Digitalagcgain_Object = MibTableColumn
digitalagcgain = _Digitalagcgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 25),
    _Digitalagcgain_Type()
)
digitalagcgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalagcgain.setStatus("current")
_Tuneragcgain_Type = Counter32
_Tuneragcgain_Object = MibTableColumn
tuneragcgain = _Tuneragcgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 26),
    _Tuneragcgain_Type()
)
tuneragcgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuneragcgain.setStatus("current")
_Fooffset_Type = Counter32
_Fooffset_Object = MibTableColumn
fooffset = _Fooffset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 27),
    _Fooffset_Type()
)
fooffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fooffset.setStatus("current")
_Tdmacrcerrors_Type = Counter32
_Tdmacrcerrors_Object = MibTableColumn
tdmacrcerrors = _Tdmacrcerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 28),
    _Tdmacrcerrors_Type()
)
tdmacrcerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmacrcerrors.setStatus("current")


class _Tdmasnrcal_Type(DisplayString):
    """Custom type tdmasnrcal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Tdmasnrcal_Type.__name__ = "DisplayString"
_Tdmasnrcal_Object = MibTableColumn
tdmasnrcal = _Tdmasnrcal_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 29),
    _Tdmasnrcal_Type()
)
tdmasnrcal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmasnrcal.setStatus("current")
_Tdmasymoffset_Type = Counter32
_Tdmasymoffset_Object = MibTableColumn
tdmasymoffset = _Tdmasymoffset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 30),
    _Tdmasymoffset_Type()
)
tdmasymoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmasymoffset.setStatus("current")
_Tdmafreqoffset_Type = Counter32
_Tdmafreqoffset_Object = MibTableColumn
tdmafreqoffset = _Tdmafreqoffset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 31),
    _Tdmafreqoffset_Type()
)
tdmafreqoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmafreqoffset.setStatus("current")
_Rxreliable_Type = Counter32
_Rxreliable_Object = MibTableColumn
rxreliable = _Rxreliable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 32),
    _Rxreliable_Type()
)
rxreliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxreliable.setStatus("current")
_Rxunreliable_Type = Counter32
_Rxunreliable_Object = MibTableColumn
rxunreliable = _Rxunreliable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 33),
    _Rxunreliable_Type()
)
rxunreliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxunreliable.setStatus("current")
_Rxoob_Type = Counter32
_Rxoob_Object = MibTableColumn
rxoob = _Rxoob_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 34),
    _Rxoob_Type()
)
rxoob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxoob.setStatus("current")
_Txreliable_Type = Counter32
_Txreliable_Object = MibTableColumn
txreliable = _Txreliable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 35),
    _Txreliable_Type()
)
txreliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txreliable.setStatus("current")
_Txunreliable_Type = Counter32
_Txunreliable_Object = MibTableColumn
txunreliable = _Txunreliable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 36),
    _Txunreliable_Type()
)
txunreliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txunreliable.setStatus("current")
_Txoob_Type = Counter32
_Txoob_Object = MibTableColumn
txoob = _Txoob_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 37),
    _Txoob_Type()
)
txoob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txoob.setStatus("current")


class _Remotestatstime_Type(DisplayString):
    """Custom type remotestatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Remotestatstime_Type.__name__ = "DisplayString"
_Remotestatstime_Object = MibTableColumn
remotestatstime = _Remotestatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 3, 1, 38),
    _Remotestatstime_Type()
)
remotestatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotestatstime.setStatus("current")
_RemoteucpTable_Object = MibTable
remoteucpTable = _RemoteucpTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4)
)
if mibBuilder.loadTexts:
    remoteucpTable.setStatus("current")
_RemoteucpEntry_Object = MibTableRow
remoteucpEntry = _RemoteucpEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1)
)
remoteucpEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "ucpnmdid"),
)
if mibBuilder.loadTexts:
    remoteucpEntry.setStatus("current")


class _Ucpnmdid_Type(Unsigned32):
    """Custom type ucpnmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Ucpnmdid_Type.__name__ = "Unsigned32"
_Ucpnmdid_Object = MibTableColumn
ucpnmdid = _Ucpnmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 1),
    _Ucpnmdid_Type()
)
ucpnmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucpnmdid.setStatus("current")


class _Upsnr_Type(DisplayString):
    """Custom type upsnr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Upsnr_Type.__name__ = "DisplayString"
_Upsnr_Object = MibTableColumn
upsnr = _Upsnr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 2),
    _Upsnr_Type()
)
upsnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsnr.setStatus("current")


class _Poweradjustment_Type(DisplayString):
    """Custom type poweradjustment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Poweradjustment_Type.__name__ = "DisplayString"
_Poweradjustment_Object = MibTableColumn
poweradjustment = _Poweradjustment_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 3),
    _Poweradjustment_Type()
)
poweradjustment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poweradjustment.setStatus("current")
_Symboloffset_Type = Integer32
_Symboloffset_Object = MibTableColumn
symboloffset = _Symboloffset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 4),
    _Symboloffset_Type()
)
symboloffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    symboloffset.setStatus("current")
_Frequencyoffset_Type = Integer32
_Frequencyoffset_Object = MibTableColumn
frequencyoffset = _Frequencyoffset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 5),
    _Frequencyoffset_Type()
)
frequencyoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyoffset.setStatus("current")


class _Scpcsnrcal_Type(DisplayString):
    """Custom type scpcsnrcal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Scpcsnrcal_Type.__name__ = "DisplayString"
_Scpcsnrcal_Object = MibTableColumn
scpcsnrcal = _Scpcsnrcal_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 6),
    _Scpcsnrcal_Type()
)
scpcsnrcal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpcsnrcal.setStatus("current")


class _Ucpstatstime_Type(DisplayString):
    """Custom type ucpstatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ucpstatstime_Type.__name__ = "DisplayString"
_Ucpstatstime_Object = MibTableColumn
ucpstatstime = _Ucpstatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 4, 1, 7),
    _Ucpstatstime_Type()
)
ucpstatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ucpstatstime.setStatus("current")
_LatencystatsTable_Object = MibTable
latencystatsTable = _LatencystatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5)
)
if mibBuilder.loadTexts:
    latencystatsTable.setStatus("current")
_LatencystatsEntry_Object = MibTableRow
latencystatsEntry = _LatencystatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1)
)
latencystatsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "latnmdid"),
)
if mibBuilder.loadTexts:
    latencystatsEntry.setStatus("current")


class _Latnmdid_Type(Unsigned32):
    """Custom type latnmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Latnmdid_Type.__name__ = "Unsigned32"
_Latnmdid_Object = MibTableColumn
latnmdid = _Latnmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 1),
    _Latnmdid_Type()
)
latnmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latnmdid.setStatus("current")


class _Latnmname_Type(DisplayString):
    """Custom type latnmname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Latnmname_Type.__name__ = "DisplayString"
_Latnmname_Object = MibTableColumn
latnmname = _Latnmname_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 2),
    _Latnmname_Type()
)
latnmname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latnmname.setStatus("current")
_Latnmsn_Type = Unsigned32
_Latnmsn_Object = MibTableColumn
latnmsn = _Latnmsn_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 3),
    _Latnmsn_Type()
)
latnmsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latnmsn.setStatus("current")


class _Mgmtipaddress_Type(DisplayString):
    """Custom type mgmtipaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mgmtipaddress_Type.__name__ = "DisplayString"
_Mgmtipaddress_Object = MibTableColumn
mgmtipaddress = _Mgmtipaddress_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 4),
    _Mgmtipaddress_Type()
)
mgmtipaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtipaddress.setStatus("current")


class _Latencyvalue_Type(DisplayString):
    """Custom type latencyvalue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Latencyvalue_Type.__name__ = "DisplayString"
_Latencyvalue_Object = MibTableColumn
latencyvalue = _Latencyvalue_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 5),
    _Latencyvalue_Type()
)
latencyvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyvalue.setStatus("current")


class _Networkname_Type(DisplayString):
    """Custom type networkname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Networkname_Type.__name__ = "DisplayString"
_Networkname_Object = MibTableColumn
networkname = _Networkname_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 6),
    _Networkname_Type()
)
networkname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkname.setStatus("current")


class _Latstatstime_Type(DisplayString):
    """Custom type latstatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Latstatstime_Type.__name__ = "DisplayString"
_Latstatstime_Object = MibTableColumn
latstatstime = _Latstatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 5, 1, 7),
    _Latstatstime_Type()
)
latstatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latstatstime.setStatus("current")
_HubstatsTable_Object = MibTable
hubstatsTable = _HubstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hubstatsTable.setStatus("current")
_HubstatsEntry_Object = MibTableRow
hubstatsEntry = _HubstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1)
)
hubstatsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "linecarddid"),
)
if mibBuilder.loadTexts:
    hubstatsEntry.setStatus("current")


class _Linecarddid_Type(Unsigned32):
    """Custom type linecarddid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Linecarddid_Type.__name__ = "Unsigned32"
_Linecarddid_Object = MibTableColumn
linecarddid = _Linecarddid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 1),
    _Linecarddid_Type()
)
linecarddid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecarddid.setStatus("current")
_Linecardsn_Type = Unsigned32
_Linecardsn_Object = MibTableColumn
linecardsn = _Linecardsn_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 2),
    _Linecardsn_Type()
)
linecardsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linecardsn.setStatus("current")
_Txattempts_Type = Counter32
_Txattempts_Object = MibTableColumn
txattempts = _Txattempts_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 3),
    _Txattempts_Type()
)
txattempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txattempts.setStatus("current")
_Txbytes_Type = Counter32
_Txbytes_Object = MibTableColumn
txbytes = _Txbytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 4),
    _Txbytes_Type()
)
txbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txbytes.setStatus("current")
_Txerrors_Type = Counter32
_Txerrors_Object = MibTableColumn
txerrors = _Txerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 5),
    _Txerrors_Type()
)
txerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txerrors.setStatus("current")
_Acqcrcerrors_Type = Counter32
_Acqcrcerrors_Object = MibTableColumn
acqcrcerrors = _Acqcrcerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 6),
    _Acqcrcerrors_Type()
)
acqcrcerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqcrcerrors.setStatus("current")
_Trafficcrcerrors_Type = Counter32
_Trafficcrcerrors_Object = MibTableColumn
trafficcrcerrors = _Trafficcrcerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 7),
    _Trafficcrcerrors_Type()
)
trafficcrcerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficcrcerrors.setStatus("current")
_Bursts_Type = Counter32
_Bursts_Object = MibTableColumn
bursts = _Bursts_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 8),
    _Bursts_Type()
)
bursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bursts.setStatus("current")
_Rxbytes_Type = Counter32
_Rxbytes_Object = MibTableColumn
rxbytes = _Rxbytes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 9),
    _Rxbytes_Type()
)
rxbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxbytes.setStatus("current")


class _Rxpower_Type(DisplayString):
    """Custom type rxpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rxpower_Type.__name__ = "DisplayString"
_Rxpower_Object = MibTableColumn
rxpower = _Rxpower_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 10),
    _Rxpower_Type()
)
rxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxpower.setStatus("current")
_Dmareset_Type = Counter32
_Dmareset_Object = MibTableColumn
dmareset = _Dmareset_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 11),
    _Dmareset_Type()
)
dmareset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmareset.setStatus("current")
_Tunnelrxerrors_Type = Counter32
_Tunnelrxerrors_Object = MibTableColumn
tunnelrxerrors = _Tunnelrxerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 12),
    _Tunnelrxerrors_Type()
)
tunnelrxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelrxerrors.setStatus("current")
_Tunneltxerrors_Type = Counter32
_Tunneltxerrors_Object = MibTableColumn
tunneltxerrors = _Tunneltxerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 13),
    _Tunneltxerrors_Type()
)
tunneltxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunneltxerrors.setStatus("current")


class _Txpower_Type(DisplayString):
    """Custom type txpower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Txpower_Type.__name__ = "DisplayString"
_Txpower_Object = MibTableColumn
txpower = _Txpower_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 14),
    _Txpower_Type()
)
txpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txpower.setStatus("current")


class _Temp_Type(DisplayString):
    """Custom type temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Temp_Type.__name__ = "DisplayString"
_Temp_Object = MibTableColumn
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 15),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("current")
_Timeticks_Type = TimeTicks
_Timeticks_Object = MibTableColumn
timeticks = _Timeticks_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 16),
    _Timeticks_Type()
)
timeticks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeticks.setStatus("current")
_Agcgain_Type = Counter32
_Agcgain_Object = MibTableColumn
agcgain = _Agcgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 17),
    _Agcgain_Type()
)
agcgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agcgain.setStatus("current")
_Mcagcgain_Type = Counter32
_Mcagcgain_Object = MibTableColumn
mcagcgain = _Mcagcgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 18),
    _Mcagcgain_Type()
)
mcagcgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcagcgain.setStatus("current")


class _Gige_Type(DisplayString):
    """Custom type gige based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Gige_Type.__name__ = "DisplayString"
_Gige_Object = MibTableColumn
gige = _Gige_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 19),
    _Gige_Type()
)
gige.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gige.setStatus("current")
_Bufoverflow_Type = Counter32
_Bufoverflow_Object = MibTableColumn
bufoverflow = _Bufoverflow_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 20),
    _Bufoverflow_Type()
)
bufoverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufoverflow.setStatus("current")
_Fegacdacval_Type = Counter32
_Fegacdacval_Object = MibTableColumn
fegacdacval = _Fegacdacval_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 21),
    _Fegacdacval_Type()
)
fegacdacval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fegacdacval.setStatus("current")
_Gigetxerrors_Type = Counter32
_Gigetxerrors_Object = MibTableColumn
gigetxerrors = _Gigetxerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 22),
    _Gigetxerrors_Type()
)
gigetxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigetxerrors.setStatus("current")
_Gigerxerrors_Type = Counter32
_Gigerxerrors_Object = MibTableColumn
gigerxerrors = _Gigerxerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 23),
    _Gigerxerrors_Type()
)
gigerxerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gigerxerrors.setStatus("current")
_Scpcrxgain_Type = Counter32
_Scpcrxgain_Object = MibTableColumn
scpcrxgain = _Scpcrxgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 24),
    _Scpcrxgain_Type()
)
scpcrxgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpcrxgain.setStatus("current")
_Scpcrxcof_Type = Counter32
_Scpcrxcof_Object = MibTableColumn
scpcrxcof = _Scpcrxcof_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 25),
    _Scpcrxcof_Type()
)
scpcrxcof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpcrxcof.setStatus("current")
_Scpclockstat_Type = Counter32
_Scpclockstat_Object = MibTableColumn
scpclockstat = _Scpclockstat_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 26),
    _Scpclockstat_Type()
)
scpclockstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpclockstat.setStatus("current")
_Scpclockcntr_Type = Counter32
_Scpclockcntr_Object = MibTableColumn
scpclockcntr = _Scpclockcntr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 27),
    _Scpclockcntr_Type()
)
scpclockcntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpclockcntr.setStatus("current")
_Tdmaagcerrors_Type = Counter32
_Tdmaagcerrors_Object = MibTableColumn
tdmaagcerrors = _Tdmaagcerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 28),
    _Tdmaagcerrors_Type()
)
tdmaagcerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmaagcerrors.setStatus("current")
_Tdmatrafficerrors_Type = Counter32
_Tdmatrafficerrors_Object = MibTableColumn
tdmatrafficerrors = _Tdmatrafficerrors_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 29),
    _Tdmatrafficerrors_Type()
)
tdmatrafficerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmatrafficerrors.setStatus("current")
_Tdmabursts_Type = Counter32
_Tdmabursts_Object = MibTableColumn
tdmabursts = _Tdmabursts_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 30),
    _Tdmabursts_Type()
)
tdmabursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmabursts.setStatus("current")
_Tdmabytesrx_Type = Counter32
_Tdmabytesrx_Object = MibTableColumn
tdmabytesrx = _Tdmabytesrx_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 31),
    _Tdmabytesrx_Type()
)
tdmabytesrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmabytesrx.setStatus("current")
_Tdmarxgain_Type = Counter32
_Tdmarxgain_Object = MibTableColumn
tdmarxgain = _Tdmarxgain_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 32),
    _Tdmarxgain_Type()
)
tdmarxgain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdmarxgain.setStatus("current")


class _Hubstatstime_Type(DisplayString):
    """Custom type hubstatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hubstatstime_Type.__name__ = "DisplayString"
_Hubstatstime_Object = MibTableColumn
hubstatstime = _Hubstatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 6, 1, 33),
    _Hubstatstime_Type()
)
hubstatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubstatstime.setStatus("current")
_ResetAllStatTables_Type = Unsigned32
_ResetAllStatTables_Object = MibScalar
resetAllStatTables = _ResetAllStatTables_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 7),
    _ResetAllStatTables_Type()
)
resetAllStatTables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllStatTables.setStatus("current")


class _StatsStartTime_Type(DisplayString):
    """Custom type statsStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StatsStartTime_Type.__name__ = "DisplayString"
_StatsStartTime_Object = MibScalar
statsStartTime = _StatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 8),
    _StatsStartTime_Type()
)
statsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsStartTime.setStatus("current")
_DvbS2statsTable_Object = MibTable
dvbS2statsTable = _DvbS2statsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9)
)
if mibBuilder.loadTexts:
    dvbS2statsTable.setStatus("current")
_DvbS2statsEntry_Object = MibTableRow
dvbS2statsEntry = _DvbS2statsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1)
)
dvbS2statsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "dvbnmdid"),
)
if mibBuilder.loadTexts:
    dvbS2statsEntry.setStatus("current")


class _Dvbnmdid_Type(Unsigned32):
    """Custom type dvbnmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dvbnmdid_Type.__name__ = "Unsigned32"
_Dvbnmdid_Object = MibTableColumn
dvbnmdid = _Dvbnmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 1),
    _Dvbnmdid_Type()
)
dvbnmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbnmdid.setStatus("current")


class _Clearskymc_Type(DisplayString):
    """Custom type clearskymc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Clearskymc_Type.__name__ = "DisplayString"
_Clearskymc_Object = MibTableColumn
clearskymc = _Clearskymc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 2),
    _Clearskymc_Type()
)
clearskymc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearskymc.setStatus("current")


class _Minmc_Type(DisplayString):
    """Custom type minmc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Minmc_Type.__name__ = "DisplayString"
_Minmc_Object = MibTableColumn
minmc = _Minmc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 3),
    _Minmc_Type()
)
minmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minmc.setStatus("current")


class _Maxmc_Type(DisplayString):
    """Custom type maxmc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Maxmc_Type.__name__ = "DisplayString"
_Maxmc_Object = MibTableColumn
maxmc = _Maxmc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 4),
    _Maxmc_Type()
)
maxmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxmc.setStatus("current")


class _Currentmc_Type(Unsigned32):
    """Custom type currentmc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Currentmc_Type.__name__ = "Unsigned32"
_Currentmc_Object = MibTableColumn
currentmc = _Currentmc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 5),
    _Currentmc_Type()
)
currentmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentmc.setStatus("current")


class _Availablemc_Type(Unsigned32):
    """Custom type availablemc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Availablemc_Type.__name__ = "Unsigned32"
_Availablemc_Object = MibTableColumn
availablemc = _Availablemc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 6),
    _Availablemc_Type()
)
availablemc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availablemc.setStatus("current")


class _Currentsnr_Type(Unsigned32):
    """Custom type currentsnr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Currentsnr_Type.__name__ = "Unsigned32"
_Currentsnr_Object = MibTableColumn
currentsnr = _Currentsnr_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 7),
    _Currentsnr_Type()
)
currentsnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentsnr.setStatus("current")


class _Bytesmc01_Type(Unsigned32):
    """Custom type bytesmc01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc01_Type.__name__ = "Unsigned32"
_Bytesmc01_Object = MibTableColumn
bytesmc01 = _Bytesmc01_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 8),
    _Bytesmc01_Type()
)
bytesmc01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc01.setStatus("current")


class _Bytesmc02_Type(Unsigned32):
    """Custom type bytesmc02 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc02_Type.__name__ = "Unsigned32"
_Bytesmc02_Object = MibTableColumn
bytesmc02 = _Bytesmc02_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 9),
    _Bytesmc02_Type()
)
bytesmc02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc02.setStatus("current")


class _Bytesmc03_Type(Unsigned32):
    """Custom type bytesmc03 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc03_Type.__name__ = "Unsigned32"
_Bytesmc03_Object = MibTableColumn
bytesmc03 = _Bytesmc03_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 10),
    _Bytesmc03_Type()
)
bytesmc03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc03.setStatus("current")


class _Bytesmc04_Type(Unsigned32):
    """Custom type bytesmc04 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc04_Type.__name__ = "Unsigned32"
_Bytesmc04_Object = MibTableColumn
bytesmc04 = _Bytesmc04_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 11),
    _Bytesmc04_Type()
)
bytesmc04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc04.setStatus("current")


class _Bytesmc05_Type(Unsigned32):
    """Custom type bytesmc05 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc05_Type.__name__ = "Unsigned32"
_Bytesmc05_Object = MibTableColumn
bytesmc05 = _Bytesmc05_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 12),
    _Bytesmc05_Type()
)
bytesmc05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc05.setStatus("current")


class _Bytesmc06_Type(Unsigned32):
    """Custom type bytesmc06 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc06_Type.__name__ = "Unsigned32"
_Bytesmc06_Object = MibTableColumn
bytesmc06 = _Bytesmc06_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 13),
    _Bytesmc06_Type()
)
bytesmc06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc06.setStatus("current")


class _Bytesmc07_Type(Unsigned32):
    """Custom type bytesmc07 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc07_Type.__name__ = "Unsigned32"
_Bytesmc07_Object = MibTableColumn
bytesmc07 = _Bytesmc07_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 14),
    _Bytesmc07_Type()
)
bytesmc07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc07.setStatus("current")


class _Bytesmc08_Type(Unsigned32):
    """Custom type bytesmc08 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc08_Type.__name__ = "Unsigned32"
_Bytesmc08_Object = MibTableColumn
bytesmc08 = _Bytesmc08_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 15),
    _Bytesmc08_Type()
)
bytesmc08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc08.setStatus("current")


class _Bytesmc09_Type(Unsigned32):
    """Custom type bytesmc09 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc09_Type.__name__ = "Unsigned32"
_Bytesmc09_Object = MibTableColumn
bytesmc09 = _Bytesmc09_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 16),
    _Bytesmc09_Type()
)
bytesmc09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc09.setStatus("current")


class _Bytesmc10_Type(Unsigned32):
    """Custom type bytesmc10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc10_Type.__name__ = "Unsigned32"
_Bytesmc10_Object = MibTableColumn
bytesmc10 = _Bytesmc10_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 17),
    _Bytesmc10_Type()
)
bytesmc10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc10.setStatus("current")


class _Bytesmc11_Type(Unsigned32):
    """Custom type bytesmc11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc11_Type.__name__ = "Unsigned32"
_Bytesmc11_Object = MibTableColumn
bytesmc11 = _Bytesmc11_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 18),
    _Bytesmc11_Type()
)
bytesmc11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc11.setStatus("current")


class _Bytesmc12_Type(Unsigned32):
    """Custom type bytesmc12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc12_Type.__name__ = "Unsigned32"
_Bytesmc12_Object = MibTableColumn
bytesmc12 = _Bytesmc12_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 19),
    _Bytesmc12_Type()
)
bytesmc12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc12.setStatus("current")


class _Bytesmc13_Type(Unsigned32):
    """Custom type bytesmc13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc13_Type.__name__ = "Unsigned32"
_Bytesmc13_Object = MibTableColumn
bytesmc13 = _Bytesmc13_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 20),
    _Bytesmc13_Type()
)
bytesmc13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc13.setStatus("current")


class _Bytesmc14_Type(Unsigned32):
    """Custom type bytesmc14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc14_Type.__name__ = "Unsigned32"
_Bytesmc14_Object = MibTableColumn
bytesmc14 = _Bytesmc14_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 21),
    _Bytesmc14_Type()
)
bytesmc14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc14.setStatus("current")


class _Bytesmc15_Type(Unsigned32):
    """Custom type bytesmc15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc15_Type.__name__ = "Unsigned32"
_Bytesmc15_Object = MibTableColumn
bytesmc15 = _Bytesmc15_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 22),
    _Bytesmc15_Type()
)
bytesmc15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc15.setStatus("current")


class _Bytesmc16_Type(Unsigned32):
    """Custom type bytesmc16 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc16_Type.__name__ = "Unsigned32"
_Bytesmc16_Object = MibTableColumn
bytesmc16 = _Bytesmc16_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 23),
    _Bytesmc16_Type()
)
bytesmc16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc16.setStatus("current")


class _Bytesmc17_Type(Unsigned32):
    """Custom type bytesmc17 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc17_Type.__name__ = "Unsigned32"
_Bytesmc17_Object = MibTableColumn
bytesmc17 = _Bytesmc17_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 24),
    _Bytesmc17_Type()
)
bytesmc17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc17.setStatus("current")


class _Bytesmc18_Type(Unsigned32):
    """Custom type bytesmc18 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc18_Type.__name__ = "Unsigned32"
_Bytesmc18_Object = MibTableColumn
bytesmc18 = _Bytesmc18_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 25),
    _Bytesmc18_Type()
)
bytesmc18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc18.setStatus("current")


class _Bytesmc19_Type(Unsigned32):
    """Custom type bytesmc19 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc19_Type.__name__ = "Unsigned32"
_Bytesmc19_Object = MibTableColumn
bytesmc19 = _Bytesmc19_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 26),
    _Bytesmc19_Type()
)
bytesmc19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc19.setStatus("current")


class _Bytesmc20_Type(Unsigned32):
    """Custom type bytesmc20 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc20_Type.__name__ = "Unsigned32"
_Bytesmc20_Object = MibTableColumn
bytesmc20 = _Bytesmc20_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 27),
    _Bytesmc20_Type()
)
bytesmc20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc20.setStatus("current")


class _Bytesmc21_Type(Unsigned32):
    """Custom type bytesmc21 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc21_Type.__name__ = "Unsigned32"
_Bytesmc21_Object = MibTableColumn
bytesmc21 = _Bytesmc21_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 28),
    _Bytesmc21_Type()
)
bytesmc21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc21.setStatus("current")


class _Bytesmc22_Type(Unsigned32):
    """Custom type bytesmc22 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc22_Type.__name__ = "Unsigned32"
_Bytesmc22_Object = MibTableColumn
bytesmc22 = _Bytesmc22_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 29),
    _Bytesmc22_Type()
)
bytesmc22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc22.setStatus("current")


class _Bytesmc23_Type(Unsigned32):
    """Custom type bytesmc23 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc23_Type.__name__ = "Unsigned32"
_Bytesmc23_Object = MibTableColumn
bytesmc23 = _Bytesmc23_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 30),
    _Bytesmc23_Type()
)
bytesmc23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc23.setStatus("current")


class _Bytesmc24_Type(Unsigned32):
    """Custom type bytesmc24 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc24_Type.__name__ = "Unsigned32"
_Bytesmc24_Object = MibTableColumn
bytesmc24 = _Bytesmc24_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 31),
    _Bytesmc24_Type()
)
bytesmc24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc24.setStatus("current")


class _Bytesmc25_Type(Unsigned32):
    """Custom type bytesmc25 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc25_Type.__name__ = "Unsigned32"
_Bytesmc25_Object = MibTableColumn
bytesmc25 = _Bytesmc25_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 32),
    _Bytesmc25_Type()
)
bytesmc25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc25.setStatus("current")


class _Bytesmc26_Type(Unsigned32):
    """Custom type bytesmc26 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc26_Type.__name__ = "Unsigned32"
_Bytesmc26_Object = MibTableColumn
bytesmc26 = _Bytesmc26_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 33),
    _Bytesmc26_Type()
)
bytesmc26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc26.setStatus("current")


class _Bytesmc27_Type(Unsigned32):
    """Custom type bytesmc27 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc27_Type.__name__ = "Unsigned32"
_Bytesmc27_Object = MibTableColumn
bytesmc27 = _Bytesmc27_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 34),
    _Bytesmc27_Type()
)
bytesmc27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc27.setStatus("current")


class _Bytesmc28_Type(Unsigned32):
    """Custom type bytesmc28 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Bytesmc28_Type.__name__ = "Unsigned32"
_Bytesmc28_Object = MibTableColumn
bytesmc28 = _Bytesmc28_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 35),
    _Bytesmc28_Type()
)
bytesmc28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmc28.setStatus("current")


class _BytesmcTOT_Type(Unsigned32):
    """Custom type bytesmcTOT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_BytesmcTOT_Type.__name__ = "Unsigned32"
_BytesmcTOT_Object = MibTableColumn
bytesmcTOT = _BytesmcTOT_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 36),
    _BytesmcTOT_Type()
)
bytesmcTOT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesmcTOT.setStatus("current")


class _DvbS2statstime_Type(DisplayString):
    """Custom type dvbS2statstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DvbS2statstime_Type.__name__ = "DisplayString"
_DvbS2statstime_Object = MibTableColumn
dvbS2statstime = _DvbS2statstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 9, 1, 37),
    _DvbS2statstime_Type()
)
dvbS2statstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbS2statstime.setStatus("current")
_HubS2statsTable_Object = MibTable
hubS2statsTable = _HubS2statsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10)
)
if mibBuilder.loadTexts:
    hubS2statsTable.setStatus("current")
_HubS2statsEntry_Object = MibTableRow
hubS2statsEntry = _HubS2statsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1)
)
hubS2statsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "dvbhubdid"),
)
if mibBuilder.loadTexts:
    hubS2statsEntry.setStatus("current")


class _Dvbhubdid_Type(Unsigned32):
    """Custom type dvbhubdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dvbhubdid_Type.__name__ = "Unsigned32"
_Dvbhubdid_Object = MibTableColumn
dvbhubdid = _Dvbhubdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 1),
    _Dvbhubdid_Type()
)
dvbhubdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbhubdid.setStatus("current")


class _Udprxhigh_Type(Unsigned32):
    """Custom type udprxhigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Udprxhigh_Type.__name__ = "Unsigned32"
_Udprxhigh_Object = MibTableColumn
udprxhigh = _Udprxhigh_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 2),
    _Udprxhigh_Type()
)
udprxhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udprxhigh.setStatus("current")


class _Udprxlow_Type(Unsigned32):
    """Custom type udprxlow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Udprxlow_Type.__name__ = "Unsigned32"
_Udprxlow_Object = MibTableColumn
udprxlow = _Udprxlow_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 3),
    _Udprxlow_Type()
)
udprxlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udprxlow.setStatus("current")


class _Dummyframes_Type(Unsigned32):
    """Custom type dummyframes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Dummyframes_Type.__name__ = "Unsigned32"
_Dummyframes_Object = MibTableColumn
dummyframes = _Dummyframes_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 4),
    _Dummyframes_Type()
)
dummyframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dummyframes.setStatus("current")


class _Hubbytesmc01_Type(Unsigned32):
    """Custom type hubbytesmc01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc01_Type.__name__ = "Unsigned32"
_Hubbytesmc01_Object = MibTableColumn
hubbytesmc01 = _Hubbytesmc01_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 5),
    _Hubbytesmc01_Type()
)
hubbytesmc01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc01.setStatus("current")


class _Hubbytesmc02_Type(Unsigned32):
    """Custom type hubbytesmc02 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc02_Type.__name__ = "Unsigned32"
_Hubbytesmc02_Object = MibTableColumn
hubbytesmc02 = _Hubbytesmc02_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 6),
    _Hubbytesmc02_Type()
)
hubbytesmc02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc02.setStatus("current")


class _Hubbytesmc03_Type(Unsigned32):
    """Custom type hubbytesmc03 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc03_Type.__name__ = "Unsigned32"
_Hubbytesmc03_Object = MibTableColumn
hubbytesmc03 = _Hubbytesmc03_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 7),
    _Hubbytesmc03_Type()
)
hubbytesmc03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc03.setStatus("current")


class _Hubbytesmc04_Type(Unsigned32):
    """Custom type hubbytesmc04 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc04_Type.__name__ = "Unsigned32"
_Hubbytesmc04_Object = MibTableColumn
hubbytesmc04 = _Hubbytesmc04_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 8),
    _Hubbytesmc04_Type()
)
hubbytesmc04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc04.setStatus("current")


class _Hubbytesmc05_Type(Unsigned32):
    """Custom type hubbytesmc05 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc05_Type.__name__ = "Unsigned32"
_Hubbytesmc05_Object = MibTableColumn
hubbytesmc05 = _Hubbytesmc05_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 9),
    _Hubbytesmc05_Type()
)
hubbytesmc05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc05.setStatus("current")


class _Hubbytesmc06_Type(Unsigned32):
    """Custom type hubbytesmc06 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc06_Type.__name__ = "Unsigned32"
_Hubbytesmc06_Object = MibTableColumn
hubbytesmc06 = _Hubbytesmc06_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 10),
    _Hubbytesmc06_Type()
)
hubbytesmc06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc06.setStatus("current")


class _Hubbytesmc07_Type(Unsigned32):
    """Custom type hubbytesmc07 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc07_Type.__name__ = "Unsigned32"
_Hubbytesmc07_Object = MibTableColumn
hubbytesmc07 = _Hubbytesmc07_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 11),
    _Hubbytesmc07_Type()
)
hubbytesmc07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc07.setStatus("current")


class _Hubbytesmc08_Type(Unsigned32):
    """Custom type hubbytesmc08 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc08_Type.__name__ = "Unsigned32"
_Hubbytesmc08_Object = MibTableColumn
hubbytesmc08 = _Hubbytesmc08_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 12),
    _Hubbytesmc08_Type()
)
hubbytesmc08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc08.setStatus("current")


class _Hubbytesmc09_Type(Unsigned32):
    """Custom type hubbytesmc09 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc09_Type.__name__ = "Unsigned32"
_Hubbytesmc09_Object = MibTableColumn
hubbytesmc09 = _Hubbytesmc09_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 13),
    _Hubbytesmc09_Type()
)
hubbytesmc09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc09.setStatus("current")


class _Hubbytesmc10_Type(Unsigned32):
    """Custom type hubbytesmc10 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc10_Type.__name__ = "Unsigned32"
_Hubbytesmc10_Object = MibTableColumn
hubbytesmc10 = _Hubbytesmc10_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 14),
    _Hubbytesmc10_Type()
)
hubbytesmc10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc10.setStatus("current")


class _Hubbytesmc11_Type(Unsigned32):
    """Custom type hubbytesmc11 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc11_Type.__name__ = "Unsigned32"
_Hubbytesmc11_Object = MibTableColumn
hubbytesmc11 = _Hubbytesmc11_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 15),
    _Hubbytesmc11_Type()
)
hubbytesmc11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc11.setStatus("current")


class _Hubbytesmc12_Type(Unsigned32):
    """Custom type hubbytesmc12 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc12_Type.__name__ = "Unsigned32"
_Hubbytesmc12_Object = MibTableColumn
hubbytesmc12 = _Hubbytesmc12_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 16),
    _Hubbytesmc12_Type()
)
hubbytesmc12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc12.setStatus("current")


class _Hubbytesmc13_Type(Unsigned32):
    """Custom type hubbytesmc13 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc13_Type.__name__ = "Unsigned32"
_Hubbytesmc13_Object = MibTableColumn
hubbytesmc13 = _Hubbytesmc13_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 17),
    _Hubbytesmc13_Type()
)
hubbytesmc13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc13.setStatus("current")


class _Hubbytesmc14_Type(Unsigned32):
    """Custom type hubbytesmc14 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc14_Type.__name__ = "Unsigned32"
_Hubbytesmc14_Object = MibTableColumn
hubbytesmc14 = _Hubbytesmc14_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 18),
    _Hubbytesmc14_Type()
)
hubbytesmc14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc14.setStatus("current")


class _Hubbytesmc15_Type(Unsigned32):
    """Custom type hubbytesmc15 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc15_Type.__name__ = "Unsigned32"
_Hubbytesmc15_Object = MibTableColumn
hubbytesmc15 = _Hubbytesmc15_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 19),
    _Hubbytesmc15_Type()
)
hubbytesmc15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc15.setStatus("current")


class _Hubbytesmc16_Type(Unsigned32):
    """Custom type hubbytesmc16 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc16_Type.__name__ = "Unsigned32"
_Hubbytesmc16_Object = MibTableColumn
hubbytesmc16 = _Hubbytesmc16_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 20),
    _Hubbytesmc16_Type()
)
hubbytesmc16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc16.setStatus("current")


class _Hubbytesmc17_Type(Unsigned32):
    """Custom type hubbytesmc17 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc17_Type.__name__ = "Unsigned32"
_Hubbytesmc17_Object = MibTableColumn
hubbytesmc17 = _Hubbytesmc17_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 21),
    _Hubbytesmc17_Type()
)
hubbytesmc17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc17.setStatus("current")


class _Hubbytesmc18_Type(Unsigned32):
    """Custom type hubbytesmc18 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc18_Type.__name__ = "Unsigned32"
_Hubbytesmc18_Object = MibTableColumn
hubbytesmc18 = _Hubbytesmc18_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 22),
    _Hubbytesmc18_Type()
)
hubbytesmc18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc18.setStatus("current")


class _Hubbytesmc19_Type(Unsigned32):
    """Custom type hubbytesmc19 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc19_Type.__name__ = "Unsigned32"
_Hubbytesmc19_Object = MibTableColumn
hubbytesmc19 = _Hubbytesmc19_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 23),
    _Hubbytesmc19_Type()
)
hubbytesmc19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc19.setStatus("current")


class _Hubbytesmc20_Type(Unsigned32):
    """Custom type hubbytesmc20 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc20_Type.__name__ = "Unsigned32"
_Hubbytesmc20_Object = MibTableColumn
hubbytesmc20 = _Hubbytesmc20_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 24),
    _Hubbytesmc20_Type()
)
hubbytesmc20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc20.setStatus("current")


class _Hubbytesmc21_Type(Unsigned32):
    """Custom type hubbytesmc21 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc21_Type.__name__ = "Unsigned32"
_Hubbytesmc21_Object = MibTableColumn
hubbytesmc21 = _Hubbytesmc21_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 25),
    _Hubbytesmc21_Type()
)
hubbytesmc21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc21.setStatus("current")


class _Hubbytesmc22_Type(Unsigned32):
    """Custom type hubbytesmc22 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc22_Type.__name__ = "Unsigned32"
_Hubbytesmc22_Object = MibTableColumn
hubbytesmc22 = _Hubbytesmc22_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 26),
    _Hubbytesmc22_Type()
)
hubbytesmc22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc22.setStatus("current")


class _Hubbytesmc23_Type(Unsigned32):
    """Custom type hubbytesmc23 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc23_Type.__name__ = "Unsigned32"
_Hubbytesmc23_Object = MibTableColumn
hubbytesmc23 = _Hubbytesmc23_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 27),
    _Hubbytesmc23_Type()
)
hubbytesmc23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc23.setStatus("current")


class _Hubbytesmc24_Type(Unsigned32):
    """Custom type hubbytesmc24 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc24_Type.__name__ = "Unsigned32"
_Hubbytesmc24_Object = MibTableColumn
hubbytesmc24 = _Hubbytesmc24_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 28),
    _Hubbytesmc24_Type()
)
hubbytesmc24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc24.setStatus("current")


class _Hubbytesmc25_Type(Unsigned32):
    """Custom type hubbytesmc25 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc25_Type.__name__ = "Unsigned32"
_Hubbytesmc25_Object = MibTableColumn
hubbytesmc25 = _Hubbytesmc25_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 29),
    _Hubbytesmc25_Type()
)
hubbytesmc25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc25.setStatus("current")


class _Hubbytesmc26_Type(Unsigned32):
    """Custom type hubbytesmc26 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc26_Type.__name__ = "Unsigned32"
_Hubbytesmc26_Object = MibTableColumn
hubbytesmc26 = _Hubbytesmc26_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 30),
    _Hubbytesmc26_Type()
)
hubbytesmc26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc26.setStatus("current")


class _Hubbytesmc27_Type(Unsigned32):
    """Custom type hubbytesmc27 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc27_Type.__name__ = "Unsigned32"
_Hubbytesmc27_Object = MibTableColumn
hubbytesmc27 = _Hubbytesmc27_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 31),
    _Hubbytesmc27_Type()
)
hubbytesmc27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc27.setStatus("current")


class _Hubbytesmc28_Type(Unsigned32):
    """Custom type hubbytesmc28 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hubbytesmc28_Type.__name__ = "Unsigned32"
_Hubbytesmc28_Object = MibTableColumn
hubbytesmc28 = _Hubbytesmc28_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 32),
    _Hubbytesmc28_Type()
)
hubbytesmc28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmc28.setStatus("current")


class _HubbytesmcTOT_Type(Unsigned32):
    """Custom type hubbytesmcTOT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HubbytesmcTOT_Type.__name__ = "Unsigned32"
_HubbytesmcTOT_Object = MibTableColumn
hubbytesmcTOT = _HubbytesmcTOT_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 33),
    _HubbytesmcTOT_Type()
)
hubbytesmcTOT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubbytesmcTOT.setStatus("current")


class _Hubs2statstime_Type(DisplayString):
    """Custom type hubs2statstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hubs2statstime_Type.__name__ = "DisplayString"
_Hubs2statstime_Object = MibTableColumn
hubs2statstime = _Hubs2statstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 10, 1, 34),
    _Hubs2statstime_Type()
)
hubs2statstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubs2statstime.setStatus("current")
_RxstatsTable_Object = MibTable
rxstatsTable = _RxstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11)
)
if mibBuilder.loadTexts:
    rxstatsTable.setStatus("current")
_RxstatsEntry_Object = MibTableRow
rxstatsEntry = _RxstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1)
)
rxstatsEntry.setIndexNames(
    (0, "IDIRECT-REMOTE-MIB", "rxnmdid"),
)
if mibBuilder.loadTexts:
    rxstatsEntry.setStatus("current")


class _Rxnmdid_Type(Unsigned32):
    """Custom type rxnmdid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Rxnmdid_Type.__name__ = "Unsigned32"
_Rxnmdid_Object = MibTableColumn
rxnmdid = _Rxnmdid_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 1),
    _Rxnmdid_Type()
)
rxnmdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxnmdid.setStatus("current")


class _Rxstatstype_Type(DisplayString):
    """Custom type rxstatstype based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rxstatstype_Type.__name__ = "DisplayString"
_Rxstatstype_Object = MibTableColumn
rxstatstype = _Rxstatstype_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 2),
    _Rxstatstype_Type()
)
rxstatstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstatstype.setStatus("current")
_Tacqbursts_Type = Counter64
_Tacqbursts_Object = MibTableColumn
tacqbursts = _Tacqbursts_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 3),
    _Tacqbursts_Type()
)
tacqbursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacqbursts.setStatus("current")
_Tacqcrc_Type = Counter64
_Tacqcrc_Object = MibTableColumn
tacqcrc = _Tacqcrc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 4),
    _Tacqcrc_Type()
)
tacqcrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacqcrc.setStatus("current")
_Tacqmissing_Type = Counter64
_Tacqmissing_Object = MibTableColumn
tacqmissing = _Tacqmissing_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 5),
    _Tacqmissing_Type()
)
tacqmissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacqmissing.setStatus("current")
_Tacqmismatch_Type = Counter64
_Tacqmismatch_Object = MibTableColumn
tacqmismatch = _Tacqmismatch_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 6),
    _Tacqmismatch_Type()
)
tacqmismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacqmismatch.setStatus("current")
_Tdatabursts_Type = Counter64
_Tdatabursts_Object = MibTableColumn
tdatabursts = _Tdatabursts_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 7),
    _Tdatabursts_Type()
)
tdatabursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdatabursts.setStatus("current")
_Tdatacrc_Type = Counter64
_Tdatacrc_Object = MibTableColumn
tdatacrc = _Tdatacrc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 8),
    _Tdatacrc_Type()
)
tdatacrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdatacrc.setStatus("current")
_Tdatamissing_Type = Counter64
_Tdatamissing_Object = MibTableColumn
tdatamissing = _Tdatamissing_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 9),
    _Tdatamissing_Type()
)
tdatamissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdatamissing.setStatus("current")
_Tdatamismatch_Type = Counter64
_Tdatamismatch_Object = MibTableColumn
tdatamismatch = _Tdatamismatch_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 10),
    _Tdatamismatch_Type()
)
tdatamismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdatamismatch.setStatus("current")
_Tkeepalive_Type = Counter64
_Tkeepalive_Object = MibTableColumn
tkeepalive = _Tkeepalive_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 11),
    _Tkeepalive_Type()
)
tkeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tkeepalive.setStatus("current")
_Sdatapackets_Type = Counter64
_Sdatapackets_Object = MibTableColumn
sdatapackets = _Sdatapackets_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 12),
    _Sdatapackets_Type()
)
sdatapackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdatapackets.setStatus("current")
_Shdlcerror_Type = Counter64
_Shdlcerror_Object = MibTableColumn
shdlcerror = _Shdlcerror_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 13),
    _Shdlcerror_Type()
)
shdlcerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdlcerror.setStatus("current")
_Sdatamismatch_Type = Counter64
_Sdatamismatch_Object = MibTableColumn
sdatamismatch = _Sdatamismatch_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 14),
    _Sdatamismatch_Type()
)
sdatamismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdatamismatch.setStatus("current")
_Skeepalive_Type = Counter64
_Skeepalive_Object = MibTableColumn
skeepalive = _Skeepalive_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 15),
    _Skeepalive_Type()
)
skeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    skeepalive.setStatus("current")


class _Rxstatstime_Type(DisplayString):
    """Custom type rxstatstime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Rxstatstime_Type.__name__ = "DisplayString"
_Rxstatstime_Object = MibTableColumn
rxstatstime = _Rxstatstime_Object(
    (1, 3, 6, 1, 4, 1, 13732, 1, 4, 11, 1, 16),
    _Rxstatstime_Type()
)
rxstatstime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxstatstime.setStatus("current")
_MibGroups_ObjectIdentity = ObjectIdentity
mibGroups = _MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5)
)
_IDirectTraps_ObjectIdentity = ObjectIdentity
iDirectTraps = _IDirectTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 99)
)
_Nmtraps_ObjectIdentity = ObjectIdentity
nmtraps = _Nmtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1)
)
_Chtraps_ObjectIdentity = ObjectIdentity
chtraps = _Chtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2)
)
_Pptraps_ObjectIdentity = ObjectIdentity
pptraps = _Pptraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13732, 99, 3)
)


class _Trap_rem_ip_Type(DisplayString):
    """Custom type trap_rem_ip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Trap_rem_ip_Type.__name__ = "DisplayString"
_Trap_rem_ip_Object = MibScalar
trap_rem_ip = _Trap_rem_ip_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 94),
    _Trap_rem_ip_Type()
)
trap_rem_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_rem_ip.setStatus("current")


class _Trap_rem_desc_Type(DisplayString):
    """Custom type trap_rem_desc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Trap_rem_desc_Type.__name__ = "DisplayString"
_Trap_rem_desc_Object = MibScalar
trap_rem_desc = _Trap_rem_desc_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 95),
    _Trap_rem_desc_Type()
)
trap_rem_desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_rem_desc.setStatus("current")
_Trap_sn_id_Type = Integer32
_Trap_sn_id_Object = MibScalar
trap_sn_id = _Trap_sn_id_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 96),
    _Trap_sn_id_Type()
)
trap_sn_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_sn_id.setStatus("current")
_Trap_rem_id_Type = Integer32
_Trap_rem_id_Object = MibScalar
trap_rem_id = _Trap_rem_id_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 97),
    _Trap_rem_id_Type()
)
trap_rem_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_rem_id.setStatus("current")


class _Trap_str_Type(DisplayString):
    """Custom type trap_str based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Trap_str_Type.__name__ = "DisplayString"
_Trap_str_Object = MibScalar
trap_str = _Trap_str_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 98),
    _Trap_str_Type()
)
trap_str.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_str.setStatus("current")


class _Trap_level_Type(Integer32):
    """Custom type trap_level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("cleared", 2),
          ("offline", 3),
          ("unknown", 4),
          ("warning", 0))
    )


_Trap_level_Type.__name__ = "Integer32"
_Trap_level_Object = MibScalar
trap_level = _Trap_level_Object(
    (1, 3, 6, 1, 4, 1, 13732, 99, 99),
    _Trap_level_Type()
)
trap_level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trap_level.setStatus("current")

# Managed Objects groups

chassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 1)
)
chassisGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "chassisid"),
        ("IDIRECT-REMOTE-MIB", "chassisname"),
        ("IDIRECT-REMOTE-MIB", "chstate"),
        ("IDIRECT-REMOTE-MIB", "chwarnings"),
        ("IDIRECT-REMOTE-MIB", "chalarms"),
        ("IDIRECT-REMOTE-MIB", "chassisEntries"))
)
if mibBuilder.loadTexts:
    chassisGroup.setStatus("current")

ppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 2)
)
ppGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "ppid"),
        ("IDIRECT-REMOTE-MIB", "ppteleportid"),
        ("IDIRECT-REMOTE-MIB", "ppname"),
        ("IDIRECT-REMOTE-MIB", "ppstate"),
        ("IDIRECT-REMOTE-MIB", "ppwarnings"),
        ("IDIRECT-REMOTE-MIB", "ppalarms"),
        ("IDIRECT-REMOTE-MIB", "ppEntries"))
)
if mibBuilder.loadTexts:
    ppGroup.setStatus("current")

netModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 3)
)
netModemGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "netdid"),
        ("IDIRECT-REMOTE-MIB", "nmppid"),
        ("IDIRECT-REMOTE-MIB", "networkid"),
        ("IDIRECT-REMOTE-MIB", "nmteleportid"),
        ("IDIRECT-REMOTE-MIB", "nmid"),
        ("IDIRECT-REMOTE-MIB", "inroutegroupid"),
        ("IDIRECT-REMOTE-MIB", "nmname"),
        ("IDIRECT-REMOTE-MIB", "ethipadr"),
        ("IDIRECT-REMOTE-MIB", "dcmslotnum"),
        ("IDIRECT-REMOTE-MIB", "chassid"),
        ("IDIRECT-REMOTE-MIB", "typeid"),
        ("IDIRECT-REMOTE-MIB", "nmstate"),
        ("IDIRECT-REMOTE-MIB", "nmwarnings"),
        ("IDIRECT-REMOTE-MIB", "nmalarms"),
        ("IDIRECT-REMOTE-MIB", "nmstatus"),
        ("IDIRECT-REMOTE-MIB", "geoloc"),
        ("IDIRECT-REMOTE-MIB", "netModemEntries"))
)
if mibBuilder.loadTexts:
    netModemGroup.setStatus("current")

ipStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 4)
)
ipStatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "nmdid"),
        ("IDIRECT-REMOTE-MIB", "rxtcp"),
        ("IDIRECT-REMOTE-MIB", "rxudp"),
        ("IDIRECT-REMOTE-MIB", "rxicmp"),
        ("IDIRECT-REMOTE-MIB", "rxigmp"),
        ("IDIRECT-REMOTE-MIB", "rxhttp"),
        ("IDIRECT-REMOTE-MIB", "rxother"),
        ("IDIRECT-REMOTE-MIB", "txtcp"),
        ("IDIRECT-REMOTE-MIB", "txudp"),
        ("IDIRECT-REMOTE-MIB", "txicmp"),
        ("IDIRECT-REMOTE-MIB", "txigmp"),
        ("IDIRECT-REMOTE-MIB", "txhttp"),
        ("IDIRECT-REMOTE-MIB", "txother"),
        ("IDIRECT-REMOTE-MIB", "ipstatstime"))
)
if mibBuilder.loadTexts:
    ipStatsGroup.setStatus("current")

otaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 5)
)
otaStatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "otanmdid"),
        ("IDIRECT-REMOTE-MIB", "otamode"),
        ("IDIRECT-REMOTE-MIB", "downstreamreliableBytes"),
        ("IDIRECT-REMOTE-MIB", "downstreamunreliableBytes"),
        ("IDIRECT-REMOTE-MIB", "downstreamoverheadBytes"),
        ("IDIRECT-REMOTE-MIB", "downstreammulticastBytes"),
        ("IDIRECT-REMOTE-MIB", "downstreambroadcastBytes"),
        ("IDIRECT-REMOTE-MIB", "downstreammulticastSymbols"),
        ("IDIRECT-REMOTE-MIB", "downstreambroadcastSymbols"),
        ("IDIRECT-REMOTE-MIB", "downstreamtotalKiloBytes"),
        ("IDIRECT-REMOTE-MIB", "upstreamreliableBytes"),
        ("IDIRECT-REMOTE-MIB", "upstreamunreliableBytes"),
        ("IDIRECT-REMOTE-MIB", "upstreamoverheadBytes"),
        ("IDIRECT-REMOTE-MIB", "upstreamtotalKiloBytes"),
        ("IDIRECT-REMOTE-MIB", "otastatstime"))
)
if mibBuilder.loadTexts:
    otaStatsGroup.setStatus("current")

remoteucpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 6)
)
remoteucpGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "ucpnmdid"),
        ("IDIRECT-REMOTE-MIB", "upsnr"),
        ("IDIRECT-REMOTE-MIB", "poweradjustment"),
        ("IDIRECT-REMOTE-MIB", "symboloffset"),
        ("IDIRECT-REMOTE-MIB", "frequencyoffset"),
        ("IDIRECT-REMOTE-MIB", "scpcsnrcal"),
        ("IDIRECT-REMOTE-MIB", "ucpstatstime"))
)
if mibBuilder.loadTexts:
    remoteucpGroup.setStatus("current")

latencyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 7)
)
latencyStatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "latnmdid"),
        ("IDIRECT-REMOTE-MIB", "latnmname"),
        ("IDIRECT-REMOTE-MIB", "latnmsn"),
        ("IDIRECT-REMOTE-MIB", "mgmtipaddress"),
        ("IDIRECT-REMOTE-MIB", "latencyvalue"),
        ("IDIRECT-REMOTE-MIB", "networkname"),
        ("IDIRECT-REMOTE-MIB", "latstatstime"))
)
if mibBuilder.loadTexts:
    latencyStatsGroup.setStatus("current")

hubStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 8)
)
hubStatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "linecarddid"),
        ("IDIRECT-REMOTE-MIB", "linecardsn"),
        ("IDIRECT-REMOTE-MIB", "txattempts"),
        ("IDIRECT-REMOTE-MIB", "txbytes"),
        ("IDIRECT-REMOTE-MIB", "txerrors"),
        ("IDIRECT-REMOTE-MIB", "acqcrcerrors"),
        ("IDIRECT-REMOTE-MIB", "trafficcrcerrors"),
        ("IDIRECT-REMOTE-MIB", "bursts"),
        ("IDIRECT-REMOTE-MIB", "rxbytes"),
        ("IDIRECT-REMOTE-MIB", "rxpower"),
        ("IDIRECT-REMOTE-MIB", "dmareset"),
        ("IDIRECT-REMOTE-MIB", "tunnelrxerrors"),
        ("IDIRECT-REMOTE-MIB", "tunneltxerrors"),
        ("IDIRECT-REMOTE-MIB", "txpower"),
        ("IDIRECT-REMOTE-MIB", "temp"),
        ("IDIRECT-REMOTE-MIB", "timeticks"),
        ("IDIRECT-REMOTE-MIB", "agcgain"),
        ("IDIRECT-REMOTE-MIB", "mcagcgain"),
        ("IDIRECT-REMOTE-MIB", "gige"),
        ("IDIRECT-REMOTE-MIB", "bufoverflow"),
        ("IDIRECT-REMOTE-MIB", "fegacdacval"),
        ("IDIRECT-REMOTE-MIB", "gigetxerrors"),
        ("IDIRECT-REMOTE-MIB", "gigerxerrors"),
        ("IDIRECT-REMOTE-MIB", "scpcrxgain"),
        ("IDIRECT-REMOTE-MIB", "scpcrxcof"),
        ("IDIRECT-REMOTE-MIB", "scpclockstat"),
        ("IDIRECT-REMOTE-MIB", "scpclockcntr"),
        ("IDIRECT-REMOTE-MIB", "tdmaagcerrors"),
        ("IDIRECT-REMOTE-MIB", "tdmatrafficerrors"),
        ("IDIRECT-REMOTE-MIB", "tdmabursts"),
        ("IDIRECT-REMOTE-MIB", "tdmabytesrx"),
        ("IDIRECT-REMOTE-MIB", "tdmarxgain"),
        ("IDIRECT-REMOTE-MIB", "hubstatstime"))
)
if mibBuilder.loadTexts:
    hubStatsGroup.setStatus("current")

remotestatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 9)
)
remotestatusGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "rsnmdid"),
        ("IDIRECT-REMOTE-MIB", "downsnr"),
        ("IDIRECT-REMOTE-MIB", "rstxpower"),
        ("IDIRECT-REMOTE-MIB", "rsrxpower"),
        ("IDIRECT-REMOTE-MIB", "digitalrxgain"),
        ("IDIRECT-REMOTE-MIB", "flldac"),
        ("IDIRECT-REMOTE-MIB", "rxcof"),
        ("IDIRECT-REMOTE-MIB", "rstemp"),
        ("IDIRECT-REMOTE-MIB", "tdmlost"),
        ("IDIRECT-REMOTE-MIB", "scpcerrors"),
        ("IDIRECT-REMOTE-MIB", "rstimeticks"),
        ("IDIRECT-REMOTE-MIB", "lanport"),
        ("IDIRECT-REMOTE-MIB", "ethmode"),
        ("IDIRECT-REMOTE-MIB", "ethspeed"),
        ("IDIRECT-REMOTE-MIB", "ethautonegotiate"),
        ("IDIRECT-REMOTE-MIB", "telnetsession"),
        ("IDIRECT-REMOTE-MIB", "isitesession"),
        ("IDIRECT-REMOTE-MIB", "inmesh"),
        ("IDIRECT-REMOTE-MIB", "fastfadecorr"),
        ("IDIRECT-REMOTE-MIB", "crc8error"),
        ("IDIRECT-REMOTE-MIB", "crc32error"),
        ("IDIRECT-REMOTE-MIB", "ncrlost"),
        ("IDIRECT-REMOTE-MIB", "plsynclost"),
        ("IDIRECT-REMOTE-MIB", "clockdeltacnt"),
        ("IDIRECT-REMOTE-MIB", "digitalagcgain"),
        ("IDIRECT-REMOTE-MIB", "tuneragcgain"),
        ("IDIRECT-REMOTE-MIB", "fooffset"),
        ("IDIRECT-REMOTE-MIB", "tdmacrcerrors"),
        ("IDIRECT-REMOTE-MIB", "tdmasnrcal"),
        ("IDIRECT-REMOTE-MIB", "tdmasymoffset"),
        ("IDIRECT-REMOTE-MIB", "tdmafreqoffset"),
        ("IDIRECT-REMOTE-MIB", "rxreliable"),
        ("IDIRECT-REMOTE-MIB", "rxunreliable"),
        ("IDIRECT-REMOTE-MIB", "rxoob"),
        ("IDIRECT-REMOTE-MIB", "txreliable"),
        ("IDIRECT-REMOTE-MIB", "txunreliable"),
        ("IDIRECT-REMOTE-MIB", "txoob"),
        ("IDIRECT-REMOTE-MIB", "remotestatstime"))
)
if mibBuilder.loadTexts:
    remotestatusGroup.setStatus("current")

commonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 13)
)
commonGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "resetAllStatTables"),
        ("IDIRECT-REMOTE-MIB", "statsStartTime"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_desc"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_level"))
)
if mibBuilder.loadTexts:
    commonGroup.setStatus("current")

hubs2StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 14)
)
hubs2StatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "dvbhubdid"),
        ("IDIRECT-REMOTE-MIB", "udprxhigh"),
        ("IDIRECT-REMOTE-MIB", "udprxlow"),
        ("IDIRECT-REMOTE-MIB", "dummyframes"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc01"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc02"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc03"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc04"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc05"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc06"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc07"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc08"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc09"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc10"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc11"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc12"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc13"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc14"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc15"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc16"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc17"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc18"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc19"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc20"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc21"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc22"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc23"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc24"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc25"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc26"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc27"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmc28"),
        ("IDIRECT-REMOTE-MIB", "hubbytesmcTOT"),
        ("IDIRECT-REMOTE-MIB", "hubs2statstime"))
)
if mibBuilder.loadTexts:
    hubs2StatsGroup.setStatus("current")

rmts2StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 15)
)
rmts2StatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "dvbnmdid"),
        ("IDIRECT-REMOTE-MIB", "clearskymc"),
        ("IDIRECT-REMOTE-MIB", "minmc"),
        ("IDIRECT-REMOTE-MIB", "maxmc"),
        ("IDIRECT-REMOTE-MIB", "currentmc"),
        ("IDIRECT-REMOTE-MIB", "availablemc"),
        ("IDIRECT-REMOTE-MIB", "currentsnr"),
        ("IDIRECT-REMOTE-MIB", "bytesmc01"),
        ("IDIRECT-REMOTE-MIB", "bytesmc02"),
        ("IDIRECT-REMOTE-MIB", "bytesmc03"),
        ("IDIRECT-REMOTE-MIB", "bytesmc04"),
        ("IDIRECT-REMOTE-MIB", "bytesmc05"),
        ("IDIRECT-REMOTE-MIB", "bytesmc06"),
        ("IDIRECT-REMOTE-MIB", "bytesmc07"),
        ("IDIRECT-REMOTE-MIB", "bytesmc08"),
        ("IDIRECT-REMOTE-MIB", "bytesmc09"),
        ("IDIRECT-REMOTE-MIB", "bytesmc10"),
        ("IDIRECT-REMOTE-MIB", "bytesmc11"),
        ("IDIRECT-REMOTE-MIB", "bytesmc12"),
        ("IDIRECT-REMOTE-MIB", "bytesmc13"),
        ("IDIRECT-REMOTE-MIB", "bytesmc14"),
        ("IDIRECT-REMOTE-MIB", "bytesmc15"),
        ("IDIRECT-REMOTE-MIB", "bytesmc16"),
        ("IDIRECT-REMOTE-MIB", "bytesmc17"),
        ("IDIRECT-REMOTE-MIB", "bytesmc18"),
        ("IDIRECT-REMOTE-MIB", "bytesmc19"),
        ("IDIRECT-REMOTE-MIB", "bytesmc20"),
        ("IDIRECT-REMOTE-MIB", "bytesmc21"),
        ("IDIRECT-REMOTE-MIB", "bytesmc22"),
        ("IDIRECT-REMOTE-MIB", "bytesmc23"),
        ("IDIRECT-REMOTE-MIB", "bytesmc24"),
        ("IDIRECT-REMOTE-MIB", "bytesmc25"),
        ("IDIRECT-REMOTE-MIB", "bytesmc26"),
        ("IDIRECT-REMOTE-MIB", "bytesmc27"),
        ("IDIRECT-REMOTE-MIB", "bytesmc28"),
        ("IDIRECT-REMOTE-MIB", "bytesmcTOT"),
        ("IDIRECT-REMOTE-MIB", "dvbS2statstime"))
)
if mibBuilder.loadTexts:
    rmts2StatsGroup.setStatus("current")

rxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 16)
)
rxStatsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "rxnmdid"),
        ("IDIRECT-REMOTE-MIB", "rxstatstype"),
        ("IDIRECT-REMOTE-MIB", "tacqbursts"),
        ("IDIRECT-REMOTE-MIB", "tacqcrc"),
        ("IDIRECT-REMOTE-MIB", "tacqmissing"),
        ("IDIRECT-REMOTE-MIB", "tacqmismatch"),
        ("IDIRECT-REMOTE-MIB", "tdatabursts"),
        ("IDIRECT-REMOTE-MIB", "tdatacrc"),
        ("IDIRECT-REMOTE-MIB", "tdatamissing"),
        ("IDIRECT-REMOTE-MIB", "tdatamismatch"),
        ("IDIRECT-REMOTE-MIB", "tkeepalive"),
        ("IDIRECT-REMOTE-MIB", "sdatapackets"),
        ("IDIRECT-REMOTE-MIB", "shdlcerror"),
        ("IDIRECT-REMOTE-MIB", "sdatamismatch"),
        ("IDIRECT-REMOTE-MIB", "skeepalive"),
        ("IDIRECT-REMOTE-MIB", "rxstatstime"))
)
if mibBuilder.loadTexts:
    rxStatsGroup.setStatus("current")


# Notification objects

snmpProxyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 1)
)
if mibBuilder.loadTexts:
    snmpProxyStart.setStatus(
        "current"
    )

snmpProxyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 2)
)
if mibBuilder.loadTexts:
    snmpProxyStop.setStatus(
        "current"
    )

upstreamSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 3)
)
upstreamSNR.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    upstreamSNR.setStatus(
        "current"
    )

downstreamSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 4)
)
downstreamSNR.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    downstreamSNR.setStatus(
        "current"
    )

tempLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 5)
)
tempLimit.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    tempLimit.setStatus(
        "current"
    )

acqHubModemCRC = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 6)
)
acqHubModemCRC.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    acqHubModemCRC.setStatus(
        "current"
    )

trafficHubModemCRC = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 7)
)
trafficHubModemCRC.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    trafficHubModemCRC.setStatus(
        "current"
    )

latency = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 8)
)
latency.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    latency.setStatus(
        "current"
    )

symbolOffset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 9)
)
symbolOffset.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    symbolOffset.setStatus(
        "current"
    )

ethernetUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 10)
)
ethernetUnplugged.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    ethernetUnplugged.setStatus(
        "current"
    )

ucpLostContact = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 11)
)
ucpLostContact.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    ucpLostContact.setStatus(
        "current"
    )

llDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 12)
)
llDown.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    llDown.setStatus(
        "current"
    )

ucpOutOfNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 13)
)
ucpOutOfNetwork.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    ucpOutOfNetwork.setStatus(
        "current"
    )

latTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 14)
)
latTimeout.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    latTimeout.setStatus(
        "current"
    )

lackHubStats = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 16)
)
lackHubStats.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    lackHubStats.setStatus(
        "current"
    )

remoteOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 17)
)
remoteOffline.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    remoteOffline.setStatus(
        "current"
    )

rxOverflowFramesHubModem = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 18)
)
rxOverflowFramesHubModem.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rxOverflowFramesHubModem.setStatus(
        "current"
    )

downstreamPpsOverdrive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 19)
)
downstreamPpsOverdrive.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    downstreamPpsOverdrive.setStatus(
        "current"
    )

backplaneLost10Mhz = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 20)
)
backplaneLost10Mhz.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    backplaneLost10Mhz.setStatus(
        "current"
    )

calibratedTxPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 21)
)
calibratedTxPower.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    calibratedTxPower.setStatus(
        "current"
    )

txFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 22)
)
txFrequency.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    txFrequency.setStatus(
        "current"
    )

mobileLostGps = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 23)
)
mobileLostGps.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    mobileLostGps.setStatus(
        "current"
    )

scpcRxErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 24)
)
scpcRxErrors.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    scpcRxErrors.setStatus(
        "current"
    )

fllDacErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 25)
)
fllDacErrors.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    fllDacErrors.setStatus(
        "current"
    )

lcFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 26)
)
lcFailure.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    lcFailure.setStatus(
        "current"
    )

meshError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 27)
)
meshError.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshError.setStatus(
        "current"
    )

meshTdmLockLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 28)
)
meshTdmLockLost.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshTdmLockLost.setStatus(
        "current"
    )

meshHubRxScpcSnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 29)
)
meshHubRxScpcSnr.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshHubRxScpcSnr.setStatus(
        "current"
    )

meshHubRxTdmaSnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 30)
)
meshHubRxTdmaSnr.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshHubRxTdmaSnr.setStatus(
        "current"
    )

lineCardAGCOutOFRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 31)
)
lineCardAGCOutOFRange.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    lineCardAGCOutOFRange.setStatus(
        "current"
    )

meshRmtRxScpcSnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 32)
)
meshRmtRxScpcSnr.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshRmtRxScpcSnr.setStatus(
        "current"
    )

meshRmtRxTDMASnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 33)
)
meshRmtRxTDMASnr.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    meshRmtRxTDMASnr.setStatus(
        "current"
    )

remoteAgcOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 34)
)
remoteAgcOutOfRange.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    remoteAgcOutOfRange.setStatus(
        "current"
    )

reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 35)
)
reset.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    reset.setStatus(
        "current"
    )

unready = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 36)
)
unready.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    unready.setStatus(
        "current"
    )

flash = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 37)
)
flash.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    flash.setStatus(
        "current"
    )

activationStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 38)
)
activationStatus.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    activationStatus.setStatus(
        "current"
    )

elsewhereError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 39)
)
elsewhereError.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    elsewhereError.setStatus(
        "current"
    )

fanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 40)
)
fanAlarm.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    fanAlarm.setStatus(
        "current"
    )

backplaneLostSOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 41)
)
backplaneLostSOF.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    backplaneLostSOF.setStatus(
        "current"
    )

rmtMAXTxPwr = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 42)
)
rmtMAXTxPwr.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmtMAXTxPwr.setStatus(
        "current"
    )

bladeCPUHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 43)
)
bladeCPUHigh.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    bladeCPUHigh.setStatus(
        "current"
    )

rmtSleep = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 44)
)
rmtSleep.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmtSleep.setStatus(
        "current"
    )

hubTenMHzAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 45)
)
hubTenMHzAlarm.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    hubTenMHzAlarm.setStatus(
        "current"
    )

gigeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 46)
)
gigeFailed.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    gigeFailed.setStatus(
        "current"
    )

gigeHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 47)
)
gigeHealth.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    gigeHealth.setStatus(
        "current"
    )

rxOnly = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 48)
)
rxOnly.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rxOnly.setStatus(
        "current"
    )

crc8Errors = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 49)
)
crc8Errors.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    crc8Errors.setStatus(
        "current"
    )

crc32Errors = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 50)
)
crc32Errors.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    crc32Errors.setStatus(
        "current"
    )

ravenFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 51)
)
ravenFailed.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    ravenFailed.setStatus(
        "current"
    )

bladeNoEncLic = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 52)
)
bladeNoEncLic.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"))
)
if mibBuilder.loadTexts:
    bladeNoEncLic.setStatus(
        "current"
    )

rmtAcqBurst = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 53)
)
rmtAcqBurst.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"))
)
if mibBuilder.loadTexts:
    rmtAcqBurst.setStatus(
        "current"
    )

rmtCAWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 54)
)
rmtCAWillExpire.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"))
)
if mibBuilder.loadTexts:
    rmtCAWillExpire.setStatus(
        "current"
    )

rmtCAExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 55)
)
rmtCAExpired.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"))
)
if mibBuilder.loadTexts:
    rmtCAExpired.setStatus(
        "current"
    )

rmtCAInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 56)
)
rmtCAInvalid.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"))
)
if mibBuilder.loadTexts:
    rmtCAInvalid.setStatus(
        "current"
    )

rmttxTDMAAcqCrc = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 57)
)
rmttxTDMAAcqCrc.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxTDMAAcqCrc.setStatus(
        "current"
    )

rmttxTDMADataCrc = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 58)
)
rmttxTDMADataCrc.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxTDMADataCrc.setStatus(
        "current"
    )

rmttxTDMAAcqMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 59)
)
rmttxTDMAAcqMismatch.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxTDMAAcqMismatch.setStatus(
        "current"
    )

rmttxTDMADataMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 60)
)
rmttxTDMADataMismatch.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxTDMADataMismatch.setStatus(
        "current"
    )

rmttxTDMADataMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 61)
)
rmttxTDMADataMissing.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxTDMADataMissing.setStatus(
        "current"
    )

rmttxSCPCLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 62)
)
rmttxSCPCLostLock.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxSCPCLostLock.setStatus(
        "current"
    )

rmttxSCPCHdlcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 63)
)
rmttxSCPCHdlcError.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxSCPCHdlcError.setStatus(
        "current"
    )

rmttxSCPCDataMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 64)
)
rmttxSCPCDataMismatch.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmttxSCPCDataMismatch.setStatus(
        "current"
    )

rmtStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 65)
)
rmtStatusChange.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmtStatusChange.setStatus(
        "current"
    )

triStateIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 66)
)
triStateIdle.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    triStateIdle.setStatus(
        "current"
    )

triStateDormant = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 67)
)
triStateDormant.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    triStateDormant.setStatus(
        "current"
    )

rmtMCFPDecryptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 1, 68)
)
rmtMCFPDecryptFail.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"),
        ("IDIRECT-REMOTE-MIB", "trap_sn_id"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_ip"))
)
if mibBuilder.loadTexts:
    rmtMCFPDecryptFail.setStatus(
        "current"
    )

powerAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 1)
)
powerAlarm1.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    powerAlarm1.setStatus(
        "current"
    )

powerAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 2)
)
powerAlarm2.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    powerAlarm2.setStatus(
        "current"
    )

powerAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 3)
)
powerAlarm3.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    powerAlarm3.setStatus(
        "current"
    )

fanAlarmChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 4)
)
fanAlarmChassis.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    fanAlarmChassis.setStatus(
        "current"
    )

chassisDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 5)
)
chassisDown.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    chassisDown.setStatus(
        "current"
    )

rcmAAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 6)
)
rcmAAlarm.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    rcmAAlarm.setStatus(
        "current"
    )

rcmBAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 7)
)
rcmBAlarm.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    rcmBAlarm.setStatus(
        "current"
    )

lostChassisConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 8)
)
lostChassisConnection.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    lostChassisConnection.setStatus(
        "current"
    )

microChassisOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 9)
)
microChassisOverTemp.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microChassisOverTemp.setStatus(
        "current"
    )

microRCMANotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 10)
)
microRCMANotPresent.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microRCMANotPresent.setStatus(
        "current"
    )

microRCMAFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 11)
)
microRCMAFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microRCMAFault.setStatus(
        "current"
    )

microRCMBNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 12)
)
microRCMBNotPresent.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microRCMBNotPresent.setStatus(
        "current"
    )

microRCMBFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 13)
)
microRCMBFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microRCMBFault.setStatus(
        "current"
    )

microPwrAlarmABad = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 14)
)
microPwrAlarmABad.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microPwrAlarmABad.setStatus(
        "current"
    )

microPwrAlarmAOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 15)
)
microPwrAlarmAOverTemp.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microPwrAlarmAOverTemp.setStatus(
        "current"
    )

microPwrAlarmBBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 16)
)
microPwrAlarmBBad.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microPwrAlarmBBad.setStatus(
        "current"
    )

microPwrAlarmBOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 17)
)
microPwrAlarmBOverTemp.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microPwrAlarmBOverTemp.setStatus(
        "current"
    )

microFSMNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 18)
)
microFSMNotPresent.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microFSMNotPresent.setStatus(
        "current"
    )

microFSMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 19)
)
microFSMFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microFSMFault.setStatus(
        "current"
    )

microFSMFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 20)
)
microFSMFanFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microFSMFanFault.setStatus(
        "current"
    )

microIFMNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 21)
)
microIFMNotPresent.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microIFMNotPresent.setStatus(
        "current"
    )

microIFMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 22)
)
microIFMFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microIFMFault.setStatus(
        "current"
    )

microAlarmDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 23)
)
microAlarmDisabled.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microAlarmDisabled.setStatus(
        "current"
    )

microOPMAFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 24)
)
microOPMAFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microOPMAFault.setStatus(
        "current"
    )

microOPMBFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 2, 25)
)
microOPMBFault.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    microOPMBFault.setStatus(
        "current"
    )

ppStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 13732, 99, 3, 1)
)
ppStateTrap.setObjects(
      *(("IDIRECT-REMOTE-MIB", "trap_level"),
        ("IDIRECT-REMOTE-MIB", "trap_str"),
        ("IDIRECT-REMOTE-MIB", "trap_rem_id"))
)
if mibBuilder.loadTexts:
    ppStateTrap.setStatus(
        "current"
    )


# Notifications groups

netmodemNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 10)
)
netmodemNotificationsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "snmpProxyStart"),
        ("IDIRECT-REMOTE-MIB", "snmpProxyStop"),
        ("IDIRECT-REMOTE-MIB", "upstreamSNR"),
        ("IDIRECT-REMOTE-MIB", "downstreamSNR"),
        ("IDIRECT-REMOTE-MIB", "tempLimit"),
        ("IDIRECT-REMOTE-MIB", "acqHubModemCRC"),
        ("IDIRECT-REMOTE-MIB", "trafficHubModemCRC"),
        ("IDIRECT-REMOTE-MIB", "latency"),
        ("IDIRECT-REMOTE-MIB", "symbolOffset"),
        ("IDIRECT-REMOTE-MIB", "ethernetUnplugged"),
        ("IDIRECT-REMOTE-MIB", "ucpLostContact"),
        ("IDIRECT-REMOTE-MIB", "llDown"),
        ("IDIRECT-REMOTE-MIB", "ucpOutOfNetwork"),
        ("IDIRECT-REMOTE-MIB", "latTimeout"),
        ("IDIRECT-REMOTE-MIB", "lackHubStats"),
        ("IDIRECT-REMOTE-MIB", "remoteOffline"),
        ("IDIRECT-REMOTE-MIB", "rxOverflowFramesHubModem"),
        ("IDIRECT-REMOTE-MIB", "downstreamPpsOverdrive"),
        ("IDIRECT-REMOTE-MIB", "backplaneLost10Mhz"),
        ("IDIRECT-REMOTE-MIB", "calibratedTxPower"),
        ("IDIRECT-REMOTE-MIB", "txFrequency"),
        ("IDIRECT-REMOTE-MIB", "mobileLostGps"),
        ("IDIRECT-REMOTE-MIB", "scpcRxErrors"),
        ("IDIRECT-REMOTE-MIB", "fllDacErrors"),
        ("IDIRECT-REMOTE-MIB", "lcFailure"),
        ("IDIRECT-REMOTE-MIB", "meshError"),
        ("IDIRECT-REMOTE-MIB", "meshTdmLockLost"),
        ("IDIRECT-REMOTE-MIB", "meshHubRxScpcSnr"),
        ("IDIRECT-REMOTE-MIB", "meshHubRxTdmaSnr"),
        ("IDIRECT-REMOTE-MIB", "lineCardAGCOutOFRange"),
        ("IDIRECT-REMOTE-MIB", "meshRmtRxScpcSnr"),
        ("IDIRECT-REMOTE-MIB", "meshRmtRxTDMASnr"),
        ("IDIRECT-REMOTE-MIB", "remoteAgcOutOfRange"),
        ("IDIRECT-REMOTE-MIB", "reset"),
        ("IDIRECT-REMOTE-MIB", "unready"),
        ("IDIRECT-REMOTE-MIB", "flash"),
        ("IDIRECT-REMOTE-MIB", "activationStatus"),
        ("IDIRECT-REMOTE-MIB", "elsewhereError"),
        ("IDIRECT-REMOTE-MIB", "fanAlarm"),
        ("IDIRECT-REMOTE-MIB", "backplaneLostSOF"),
        ("IDIRECT-REMOTE-MIB", "rmtMAXTxPwr"),
        ("IDIRECT-REMOTE-MIB", "bladeCPUHigh"),
        ("IDIRECT-REMOTE-MIB", "rmtSleep"),
        ("IDIRECT-REMOTE-MIB", "hubTenMHzAlarm"),
        ("IDIRECT-REMOTE-MIB", "gigeFailed"),
        ("IDIRECT-REMOTE-MIB", "gigeHealth"),
        ("IDIRECT-REMOTE-MIB", "rxOnly"),
        ("IDIRECT-REMOTE-MIB", "crc8Errors"),
        ("IDIRECT-REMOTE-MIB", "crc32Errors"),
        ("IDIRECT-REMOTE-MIB", "ravenFailed"),
        ("IDIRECT-REMOTE-MIB", "rmttxTDMAAcqCrc"),
        ("IDIRECT-REMOTE-MIB", "rmttxTDMADataCrc"),
        ("IDIRECT-REMOTE-MIB", "rmttxTDMAAcqMismatch"),
        ("IDIRECT-REMOTE-MIB", "rmttxTDMADataMismatch"),
        ("IDIRECT-REMOTE-MIB", "rmttxTDMADataMissing"),
        ("IDIRECT-REMOTE-MIB", "rmttxSCPCLostLock"),
        ("IDIRECT-REMOTE-MIB", "rmttxSCPCHdlcError"),
        ("IDIRECT-REMOTE-MIB", "rmttxSCPCDataMismatch"),
        ("IDIRECT-REMOTE-MIB", "rmtStatusChange"),
        ("IDIRECT-REMOTE-MIB", "triStateDormant"),
        ("IDIRECT-REMOTE-MIB", "triStateDormant"),
        ("IDIRECT-REMOTE-MIB", "rmtMCFPDecryptFail"))
)
if mibBuilder.loadTexts:
    netmodemNotificationsGroup.setStatus(
        "current"
    )

chassisNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 11)
)
chassisNotificationsGroup.setObjects(
      *(("IDIRECT-REMOTE-MIB", "powerAlarm1"),
        ("IDIRECT-REMOTE-MIB", "powerAlarm2"),
        ("IDIRECT-REMOTE-MIB", "powerAlarm3"),
        ("IDIRECT-REMOTE-MIB", "fanAlarmChassis"),
        ("IDIRECT-REMOTE-MIB", "chassisDown"),
        ("IDIRECT-REMOTE-MIB", "rcmAAlarm"),
        ("IDIRECT-REMOTE-MIB", "rcmBAlarm"))
)
if mibBuilder.loadTexts:
    chassisNotificationsGroup.setStatus(
        "current"
    )

ppNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13732, 1, 5, 12)
)
ppNotificationsGroup.setObjects(
    ("IDIRECT-REMOTE-MIB", "ppStateTrap")
)
if mibBuilder.loadTexts:
    ppNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IDIRECT-REMOTE-MIB",
    **{"iDirectMIB": iDirectMIB,
       "iDirectObjects": iDirectObjects,
       "netmodem": netmodem,
       "netModemEntries": netModemEntries,
       "netModemTable": netModemTable,
       "netModemEntry": netModemEntry,
       "netdid": netdid,
       "nmppid": nmppid,
       "networkid": networkid,
       "nmteleportid": nmteleportid,
       "nmid": nmid,
       "inroutegroupid": inroutegroupid,
       "nmname": nmname,
       "ethipadr": ethipadr,
       "dcmslotnum": dcmslotnum,
       "chassid": chassid,
       "typeid": typeid,
       "nmstate": nmstate,
       "nmwarnings": nmwarnings,
       "nmalarms": nmalarms,
       "nmstatus": nmstatus,
       "geoloc": geoloc,
       "chassis": chassis,
       "chassisEntries": chassisEntries,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisid": chassisid,
       "chassisname": chassisname,
       "chstate": chstate,
       "chwarnings": chwarnings,
       "chalarms": chalarms,
       "pp": pp,
       "ppEntries": ppEntries,
       "ppTable": ppTable,
       "ppEntry": ppEntry,
       "ppid": ppid,
       "ppname": ppname,
       "ppteleportid": ppteleportid,
       "ppstate": ppstate,
       "ppwarnings": ppwarnings,
       "ppalarms": ppalarms,
       "idirectstats": idirectstats,
       "ipstatsTable": ipstatsTable,
       "ipstatsEntry": ipstatsEntry,
       "nmdid": nmdid,
       "rxtcp": rxtcp,
       "rxudp": rxudp,
       "rxicmp": rxicmp,
       "rxigmp": rxigmp,
       "rxhttp": rxhttp,
       "rxother": rxother,
       "txtcp": txtcp,
       "txudp": txudp,
       "txicmp": txicmp,
       "txigmp": txigmp,
       "txhttp": txhttp,
       "txother": txother,
       "ipstatstime": ipstatstime,
       "otastatsTable": otastatsTable,
       "otastatsEntry": otastatsEntry,
       "otanmdid": otanmdid,
       "otamode": otamode,
       "downstreamreliableBytes": downstreamreliableBytes,
       "downstreamunreliableBytes": downstreamunreliableBytes,
       "downstreamoverheadBytes": downstreamoverheadBytes,
       "downstreammulticastBytes": downstreammulticastBytes,
       "downstreambroadcastBytes": downstreambroadcastBytes,
       "downstreammulticastSymbols": downstreammulticastSymbols,
       "downstreambroadcastSymbols": downstreambroadcastSymbols,
       "downstreamtotalKiloBytes": downstreamtotalKiloBytes,
       "upstreamreliableBytes": upstreamreliableBytes,
       "upstreamunreliableBytes": upstreamunreliableBytes,
       "upstreamoverheadBytes": upstreamoverheadBytes,
       "upstreamtotalKiloBytes": upstreamtotalKiloBytes,
       "otastatstime": otastatstime,
       "remotestatusTable": remotestatusTable,
       "remotestatusEntry": remotestatusEntry,
       "rsnmdid": rsnmdid,
       "downsnr": downsnr,
       "rstxpower": rstxpower,
       "rsrxpower": rsrxpower,
       "digitalrxgain": digitalrxgain,
       "flldac": flldac,
       "rxcof": rxcof,
       "rstemp": rstemp,
       "tdmlost": tdmlost,
       "scpcerrors": scpcerrors,
       "rstimeticks": rstimeticks,
       "lanport": lanport,
       "ethmode": ethmode,
       "ethspeed": ethspeed,
       "ethautonegotiate": ethautonegotiate,
       "telnetsession": telnetsession,
       "isitesession": isitesession,
       "inmesh": inmesh,
       "fastfadecorr": fastfadecorr,
       "crc8error": crc8error,
       "crc32error": crc32error,
       "ncrlost": ncrlost,
       "plsynclost": plsynclost,
       "clockdeltacnt": clockdeltacnt,
       "digitalagcgain": digitalagcgain,
       "tuneragcgain": tuneragcgain,
       "fooffset": fooffset,
       "tdmacrcerrors": tdmacrcerrors,
       "tdmasnrcal": tdmasnrcal,
       "tdmasymoffset": tdmasymoffset,
       "tdmafreqoffset": tdmafreqoffset,
       "rxreliable": rxreliable,
       "rxunreliable": rxunreliable,
       "rxoob": rxoob,
       "txreliable": txreliable,
       "txunreliable": txunreliable,
       "txoob": txoob,
       "remotestatstime": remotestatstime,
       "remoteucpTable": remoteucpTable,
       "remoteucpEntry": remoteucpEntry,
       "ucpnmdid": ucpnmdid,
       "upsnr": upsnr,
       "poweradjustment": poweradjustment,
       "symboloffset": symboloffset,
       "frequencyoffset": frequencyoffset,
       "scpcsnrcal": scpcsnrcal,
       "ucpstatstime": ucpstatstime,
       "latencystatsTable": latencystatsTable,
       "latencystatsEntry": latencystatsEntry,
       "latnmdid": latnmdid,
       "latnmname": latnmname,
       "latnmsn": latnmsn,
       "mgmtipaddress": mgmtipaddress,
       "latencyvalue": latencyvalue,
       "networkname": networkname,
       "latstatstime": latstatstime,
       "hubstatsTable": hubstatsTable,
       "hubstatsEntry": hubstatsEntry,
       "linecarddid": linecarddid,
       "linecardsn": linecardsn,
       "txattempts": txattempts,
       "txbytes": txbytes,
       "txerrors": txerrors,
       "acqcrcerrors": acqcrcerrors,
       "trafficcrcerrors": trafficcrcerrors,
       "bursts": bursts,
       "rxbytes": rxbytes,
       "rxpower": rxpower,
       "dmareset": dmareset,
       "tunnelrxerrors": tunnelrxerrors,
       "tunneltxerrors": tunneltxerrors,
       "txpower": txpower,
       "temp": temp,
       "timeticks": timeticks,
       "agcgain": agcgain,
       "mcagcgain": mcagcgain,
       "gige": gige,
       "bufoverflow": bufoverflow,
       "fegacdacval": fegacdacval,
       "gigetxerrors": gigetxerrors,
       "gigerxerrors": gigerxerrors,
       "scpcrxgain": scpcrxgain,
       "scpcrxcof": scpcrxcof,
       "scpclockstat": scpclockstat,
       "scpclockcntr": scpclockcntr,
       "tdmaagcerrors": tdmaagcerrors,
       "tdmatrafficerrors": tdmatrafficerrors,
       "tdmabursts": tdmabursts,
       "tdmabytesrx": tdmabytesrx,
       "tdmarxgain": tdmarxgain,
       "hubstatstime": hubstatstime,
       "resetAllStatTables": resetAllStatTables,
       "statsStartTime": statsStartTime,
       "dvbS2statsTable": dvbS2statsTable,
       "dvbS2statsEntry": dvbS2statsEntry,
       "dvbnmdid": dvbnmdid,
       "clearskymc": clearskymc,
       "minmc": minmc,
       "maxmc": maxmc,
       "currentmc": currentmc,
       "availablemc": availablemc,
       "currentsnr": currentsnr,
       "bytesmc01": bytesmc01,
       "bytesmc02": bytesmc02,
       "bytesmc03": bytesmc03,
       "bytesmc04": bytesmc04,
       "bytesmc05": bytesmc05,
       "bytesmc06": bytesmc06,
       "bytesmc07": bytesmc07,
       "bytesmc08": bytesmc08,
       "bytesmc09": bytesmc09,
       "bytesmc10": bytesmc10,
       "bytesmc11": bytesmc11,
       "bytesmc12": bytesmc12,
       "bytesmc13": bytesmc13,
       "bytesmc14": bytesmc14,
       "bytesmc15": bytesmc15,
       "bytesmc16": bytesmc16,
       "bytesmc17": bytesmc17,
       "bytesmc18": bytesmc18,
       "bytesmc19": bytesmc19,
       "bytesmc20": bytesmc20,
       "bytesmc21": bytesmc21,
       "bytesmc22": bytesmc22,
       "bytesmc23": bytesmc23,
       "bytesmc24": bytesmc24,
       "bytesmc25": bytesmc25,
       "bytesmc26": bytesmc26,
       "bytesmc27": bytesmc27,
       "bytesmc28": bytesmc28,
       "bytesmcTOT": bytesmcTOT,
       "dvbS2statstime": dvbS2statstime,
       "hubS2statsTable": hubS2statsTable,
       "hubS2statsEntry": hubS2statsEntry,
       "dvbhubdid": dvbhubdid,
       "udprxhigh": udprxhigh,
       "udprxlow": udprxlow,
       "dummyframes": dummyframes,
       "hubbytesmc01": hubbytesmc01,
       "hubbytesmc02": hubbytesmc02,
       "hubbytesmc03": hubbytesmc03,
       "hubbytesmc04": hubbytesmc04,
       "hubbytesmc05": hubbytesmc05,
       "hubbytesmc06": hubbytesmc06,
       "hubbytesmc07": hubbytesmc07,
       "hubbytesmc08": hubbytesmc08,
       "hubbytesmc09": hubbytesmc09,
       "hubbytesmc10": hubbytesmc10,
       "hubbytesmc11": hubbytesmc11,
       "hubbytesmc12": hubbytesmc12,
       "hubbytesmc13": hubbytesmc13,
       "hubbytesmc14": hubbytesmc14,
       "hubbytesmc15": hubbytesmc15,
       "hubbytesmc16": hubbytesmc16,
       "hubbytesmc17": hubbytesmc17,
       "hubbytesmc18": hubbytesmc18,
       "hubbytesmc19": hubbytesmc19,
       "hubbytesmc20": hubbytesmc20,
       "hubbytesmc21": hubbytesmc21,
       "hubbytesmc22": hubbytesmc22,
       "hubbytesmc23": hubbytesmc23,
       "hubbytesmc24": hubbytesmc24,
       "hubbytesmc25": hubbytesmc25,
       "hubbytesmc26": hubbytesmc26,
       "hubbytesmc27": hubbytesmc27,
       "hubbytesmc28": hubbytesmc28,
       "hubbytesmcTOT": hubbytesmcTOT,
       "hubs2statstime": hubs2statstime,
       "rxstatsTable": rxstatsTable,
       "rxstatsEntry": rxstatsEntry,
       "rxnmdid": rxnmdid,
       "rxstatstype": rxstatstype,
       "tacqbursts": tacqbursts,
       "tacqcrc": tacqcrc,
       "tacqmissing": tacqmissing,
       "tacqmismatch": tacqmismatch,
       "tdatabursts": tdatabursts,
       "tdatacrc": tdatacrc,
       "tdatamissing": tdatamissing,
       "tdatamismatch": tdatamismatch,
       "tkeepalive": tkeepalive,
       "sdatapackets": sdatapackets,
       "shdlcerror": shdlcerror,
       "sdatamismatch": sdatamismatch,
       "skeepalive": skeepalive,
       "rxstatstime": rxstatstime,
       "mibGroups": mibGroups,
       "chassisGroup": chassisGroup,
       "ppGroup": ppGroup,
       "netModemGroup": netModemGroup,
       "ipStatsGroup": ipStatsGroup,
       "otaStatsGroup": otaStatsGroup,
       "remoteucpGroup": remoteucpGroup,
       "latencyStatsGroup": latencyStatsGroup,
       "hubStatsGroup": hubStatsGroup,
       "remotestatusGroup": remotestatusGroup,
       "netmodemNotificationsGroup": netmodemNotificationsGroup,
       "chassisNotificationsGroup": chassisNotificationsGroup,
       "ppNotificationsGroup": ppNotificationsGroup,
       "commonGroup": commonGroup,
       "hubs2StatsGroup": hubs2StatsGroup,
       "rmts2StatsGroup": rmts2StatsGroup,
       "rxStatsGroup": rxStatsGroup,
       "iDirectTraps": iDirectTraps,
       "nmtraps": nmtraps,
       "snmpProxyStart": snmpProxyStart,
       "snmpProxyStop": snmpProxyStop,
       "upstreamSNR": upstreamSNR,
       "downstreamSNR": downstreamSNR,
       "tempLimit": tempLimit,
       "acqHubModemCRC": acqHubModemCRC,
       "trafficHubModemCRC": trafficHubModemCRC,
       "latency": latency,
       "symbolOffset": symbolOffset,
       "ethernetUnplugged": ethernetUnplugged,
       "ucpLostContact": ucpLostContact,
       "llDown": llDown,
       "ucpOutOfNetwork": ucpOutOfNetwork,
       "latTimeout": latTimeout,
       "lackHubStats": lackHubStats,
       "remoteOffline": remoteOffline,
       "rxOverflowFramesHubModem": rxOverflowFramesHubModem,
       "downstreamPpsOverdrive": downstreamPpsOverdrive,
       "backplaneLost10Mhz": backplaneLost10Mhz,
       "calibratedTxPower": calibratedTxPower,
       "txFrequency": txFrequency,
       "mobileLostGps": mobileLostGps,
       "scpcRxErrors": scpcRxErrors,
       "fllDacErrors": fllDacErrors,
       "lcFailure": lcFailure,
       "meshError": meshError,
       "meshTdmLockLost": meshTdmLockLost,
       "meshHubRxScpcSnr": meshHubRxScpcSnr,
       "meshHubRxTdmaSnr": meshHubRxTdmaSnr,
       "lineCardAGCOutOFRange": lineCardAGCOutOFRange,
       "meshRmtRxScpcSnr": meshRmtRxScpcSnr,
       "meshRmtRxTDMASnr": meshRmtRxTDMASnr,
       "remoteAgcOutOfRange": remoteAgcOutOfRange,
       "reset": reset,
       "unready": unready,
       "flash": flash,
       "activationStatus": activationStatus,
       "elsewhereError": elsewhereError,
       "fanAlarm": fanAlarm,
       "backplaneLostSOF": backplaneLostSOF,
       "rmtMAXTxPwr": rmtMAXTxPwr,
       "bladeCPUHigh": bladeCPUHigh,
       "rmtSleep": rmtSleep,
       "hubTenMHzAlarm": hubTenMHzAlarm,
       "gigeFailed": gigeFailed,
       "gigeHealth": gigeHealth,
       "rxOnly": rxOnly,
       "crc8Errors": crc8Errors,
       "crc32Errors": crc32Errors,
       "ravenFailed": ravenFailed,
       "bladeNoEncLic": bladeNoEncLic,
       "rmtAcqBurst": rmtAcqBurst,
       "rmtCAWillExpire": rmtCAWillExpire,
       "rmtCAExpired": rmtCAExpired,
       "rmtCAInvalid": rmtCAInvalid,
       "rmttxTDMAAcqCrc": rmttxTDMAAcqCrc,
       "rmttxTDMADataCrc": rmttxTDMADataCrc,
       "rmttxTDMAAcqMismatch": rmttxTDMAAcqMismatch,
       "rmttxTDMADataMismatch": rmttxTDMADataMismatch,
       "rmttxTDMADataMissing": rmttxTDMADataMissing,
       "rmttxSCPCLostLock": rmttxSCPCLostLock,
       "rmttxSCPCHdlcError": rmttxSCPCHdlcError,
       "rmttxSCPCDataMismatch": rmttxSCPCDataMismatch,
       "rmtStatusChange": rmtStatusChange,
       "triStateIdle": triStateIdle,
       "triStateDormant": triStateDormant,
       "rmtMCFPDecryptFail": rmtMCFPDecryptFail,
       "chtraps": chtraps,
       "powerAlarm1": powerAlarm1,
       "powerAlarm2": powerAlarm2,
       "powerAlarm3": powerAlarm3,
       "fanAlarmChassis": fanAlarmChassis,
       "chassisDown": chassisDown,
       "rcmAAlarm": rcmAAlarm,
       "rcmBAlarm": rcmBAlarm,
       "lostChassisConnection": lostChassisConnection,
       "microChassisOverTemp": microChassisOverTemp,
       "microRCMANotPresent": microRCMANotPresent,
       "microRCMAFault": microRCMAFault,
       "microRCMBNotPresent": microRCMBNotPresent,
       "microRCMBFault": microRCMBFault,
       "microPwrAlarmABad": microPwrAlarmABad,
       "microPwrAlarmAOverTemp": microPwrAlarmAOverTemp,
       "microPwrAlarmBBad": microPwrAlarmBBad,
       "microPwrAlarmBOverTemp": microPwrAlarmBOverTemp,
       "microFSMNotPresent": microFSMNotPresent,
       "microFSMFault": microFSMFault,
       "microFSMFanFault": microFSMFanFault,
       "microIFMNotPresent": microIFMNotPresent,
       "microIFMFault": microIFMFault,
       "microAlarmDisabled": microAlarmDisabled,
       "microOPMAFault": microOPMAFault,
       "microOPMBFault": microOPMBFault,
       "pptraps": pptraps,
       "ppStateTrap": ppStateTrap,
       "trap-rem-ip": trap_rem_ip,
       "trap-rem-desc": trap_rem_desc,
       "trap-sn-id": trap_sn_id,
       "trap-rem-id": trap_rem_id,
       "trap-str": trap_str,
       "trap-level": trap_level}
)
