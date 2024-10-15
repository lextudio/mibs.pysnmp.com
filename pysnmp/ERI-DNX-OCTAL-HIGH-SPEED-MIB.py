# SNMP MIB module (ERI-DNX-OCTAL-HIGH-SPEED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-OCTAL-HIGH-SPEED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:26 2024
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

(ConnectionSpeed,
 DecisionType,
 FunctionSwitch,
 LinkCmdStatus,
 LinkPortAddress,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "ConnectionSpeed",
    "DecisionType",
    "FunctionSwitch",
    "LinkCmdStatus",
    "LinkPortAddress",
    "PortStatus",
    "devices",
    "trapSequence")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

eriDNXOctalHSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 6)
)
eriDNXOctalHSMIB.setRevisions(
        ("2003-02-05 00:00",
         "2002-05-13 00:00",
         "2002-03-11 00:00",
         "2001-08-01 00:00",
         "2001-06-25 00:00",
         "2001-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnxOHS_ObjectIdentity = ObjectIdentity
dnxOHS = _DnxOHS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5)
)
_DnxOHSEnterprise_ObjectIdentity = ObjectIdentity
dnxOHSEnterprise = _DnxOHSEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 0)
)
if mibBuilder.loadTexts:
    dnxOHSEnterprise.setStatus("current")
_OhsConfig_ObjectIdentity = ObjectIdentity
ohsConfig = _OhsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1)
)
_OHSConfigTable_Object = MibTable
oHSConfigTable = _OHSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    oHSConfigTable.setStatus("current")
_OHSConfigEntry_Object = MibTableRow
oHSConfigEntry = _OHSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1)
)
oHSConfigEntry.setIndexNames(
    (0, "ERI-DNX-OCTAL-HIGH-SPEED-MIB", "oHSCfgPortAddr"),
)
if mibBuilder.loadTexts:
    oHSConfigEntry.setStatus("current")
_OHSCfgPortAddr_Type = LinkPortAddress
_OHSCfgPortAddr_Object = MibTableColumn
oHSCfgPortAddr = _OHSCfgPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 1),
    _OHSCfgPortAddr_Type()
)
oHSCfgPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oHSCfgPortAddr.setStatus("current")
_OHSCfgResource_Type = Integer32
_OHSCfgResource_Object = MibTableColumn
oHSCfgResource = _OHSCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 2),
    _OHSCfgResource_Type()
)
oHSCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oHSCfgResource.setStatus("current")


class _OHSCfgPortName_Type(DisplayString):
    """Custom type oHSCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OHSCfgPortName_Type.__name__ = "DisplayString"
_OHSCfgPortName_Object = MibTableColumn
oHSCfgPortName = _OHSCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 3),
    _OHSCfgPortName_Type()
)
oHSCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgPortName.setStatus("current")
_OHSCfgStatus_Type = PortStatus
_OHSCfgStatus_Object = MibTableColumn
oHSCfgStatus = _OHSCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 4),
    _OHSCfgStatus_Type()
)
oHSCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgStatus.setStatus("current")


class _OHSCfgMode_Type(Integer32):
    """Custom type oHSCfgMode based on Integer32"""
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
        *(("ds0-A", 1),
          ("ds0-A-Special", 3),
          ("nxDs0", 0),
          ("nxDs0-Special", 2))
    )


_OHSCfgMode_Type.__name__ = "Integer32"
_OHSCfgMode_Object = MibTableColumn
oHSCfgMode = _OHSCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 5),
    _OHSCfgMode_Type()
)
oHSCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgMode.setStatus("current")
_OHSCfgSpeed_Type = ConnectionSpeed
_OHSCfgSpeed_Object = MibTableColumn
oHSCfgSpeed = _OHSCfgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 6),
    _OHSCfgSpeed_Type()
)
oHSCfgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oHSCfgSpeed.setStatus("obsolete")


class _OHSCfgType_Type(Integer32):
    """Custom type oHSCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("eia232", 2),
          ("eia422", 4),
          ("eia530", 13),
          ("eia530A", 15),
          ("ituV-35", 14),
          ("ituX-21", 16))
    )


_OHSCfgType_Type.__name__ = "Integer32"
_OHSCfgType_Object = MibTableColumn
oHSCfgType = _OHSCfgType_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 7),
    _OHSCfgType_Type()
)
oHSCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgType.setStatus("current")


class _OHSCfgData_Type(Integer32):
    """Custom type oHSCfgData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invert", 1),
          ("normal", 0))
    )


_OHSCfgData_Type.__name__ = "Integer32"
_OHSCfgData_Object = MibTableColumn
oHSCfgData = _OHSCfgData_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 8),
    _OHSCfgData_Type()
)
oHSCfgData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgData.setStatus("current")


class _OHSCfgClock_Type(Integer32):
    """Custom type oHSCfgClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invert", 1),
          ("normal", 0))
    )


_OHSCfgClock_Type.__name__ = "Integer32"
_OHSCfgClock_Object = MibTableColumn
oHSCfgClock = _OHSCfgClock_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 9),
    _OHSCfgClock_Type()
)
oHSCfgClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgClock.setStatus("current")
_OHSCfgNetLoop_Type = FunctionSwitch
_OHSCfgNetLoop_Object = MibTableColumn
oHSCfgNetLoop = _OHSCfgNetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 10),
    _OHSCfgNetLoop_Type()
)
oHSCfgNetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgNetLoop.setStatus("current")


class _OHSCfgTiming_Type(Integer32):
    """Custom type oHSCfgTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("int-ext", 1),
          ("internal", 0))
    )


_OHSCfgTiming_Type.__name__ = "Integer32"
_OHSCfgTiming_Object = MibTableColumn
oHSCfgTiming = _OHSCfgTiming_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 11),
    _OHSCfgTiming_Type()
)
oHSCfgTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgTiming.setStatus("current")


class _OHSCfgDcd_Type(Integer32):
    """Custom type oHSCfgDcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drop-carrier", 4),
          ("forced-off", 0),
          ("forced-on", 1),
          ("track-RTS", 2))
    )


_OHSCfgDcd_Type.__name__ = "Integer32"
_OHSCfgDcd_Object = MibTableColumn
oHSCfgDcd = _OHSCfgDcd_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 12),
    _OHSCfgDcd_Type()
)
oHSCfgDcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgDcd.setStatus("current")


class _OHSCfgDsr_Type(Integer32):
    """Custom type oHSCfgDsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced-off", 0),
          ("forced-on", 1),
          ("track-DTR", 2))
    )


_OHSCfgDsr_Type.__name__ = "Integer32"
_OHSCfgDsr_Object = MibTableColumn
oHSCfgDsr = _OHSCfgDsr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 13),
    _OHSCfgDsr_Type()
)
oHSCfgDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgDsr.setStatus("current")


class _OHSCfgCtsIndication_Type(Integer32):
    """Custom type oHSCfgCtsIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced-off", 0),
          ("forced-on", 1),
          ("track-RTS", 2))
    )


_OHSCfgCtsIndication_Type.__name__ = "Integer32"
_OHSCfgCtsIndication_Object = MibTableColumn
oHSCfgCtsIndication = _OHSCfgCtsIndication_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 14),
    _OHSCfgCtsIndication_Type()
)
oHSCfgCtsIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgCtsIndication.setStatus("current")
_OHSCfgDTELoop_Type = FunctionSwitch
_OHSCfgDTELoop_Object = MibTableColumn
oHSCfgDTELoop = _OHSCfgDTELoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 15),
    _OHSCfgDTELoop_Type()
)
oHSCfgDTELoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgDTELoop.setStatus("current")
_OHSCfgCmdStatus_Type = LinkCmdStatus
_OHSCfgCmdStatus_Object = MibTableColumn
oHSCfgCmdStatus = _OHSCfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 16),
    _OHSCfgCmdStatus_Type()
)
oHSCfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgCmdStatus.setStatus("current")
_OHSCfgClockEdgeErrs_Type = DecisionType
_OHSCfgClockEdgeErrs_Object = MibTableColumn
oHSCfgClockEdgeErrs = _OHSCfgClockEdgeErrs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 1, 1, 1, 17),
    _OHSCfgClockEdgeErrs_Type()
)
oHSCfgClockEdgeErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oHSCfgClockEdgeErrs.setStatus("current")
_OhsDiag_ObjectIdentity = ObjectIdentity
ohsDiag = _OhsDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 2)
)

# Managed Objects groups


# Notification objects

oHSConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 5, 0, 1)
)
oHSConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-OCTAL-HIGH-SPEED-MIB", "oHSCfgPortAddr"),
        ("ERI-DNX-OCTAL-HIGH-SPEED-MIB", "oHSCfgCmdStatus"))
)
if mibBuilder.loadTexts:
    oHSConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-OCTAL-HIGH-SPEED-MIB",
    **{"dnxOHS": dnxOHS,
       "dnxOHSEnterprise": dnxOHSEnterprise,
       "oHSConfigTrap": oHSConfigTrap,
       "ohsConfig": ohsConfig,
       "oHSConfigTable": oHSConfigTable,
       "oHSConfigEntry": oHSConfigEntry,
       "oHSCfgPortAddr": oHSCfgPortAddr,
       "oHSCfgResource": oHSCfgResource,
       "oHSCfgPortName": oHSCfgPortName,
       "oHSCfgStatus": oHSCfgStatus,
       "oHSCfgMode": oHSCfgMode,
       "oHSCfgSpeed": oHSCfgSpeed,
       "oHSCfgType": oHSCfgType,
       "oHSCfgData": oHSCfgData,
       "oHSCfgClock": oHSCfgClock,
       "oHSCfgNetLoop": oHSCfgNetLoop,
       "oHSCfgTiming": oHSCfgTiming,
       "oHSCfgDcd": oHSCfgDcd,
       "oHSCfgDsr": oHSCfgDsr,
       "oHSCfgCtsIndication": oHSCfgCtsIndication,
       "oHSCfgDTELoop": oHSCfgDTELoop,
       "oHSCfgCmdStatus": oHSCfgCmdStatus,
       "oHSCfgClockEdgeErrs": oHSCfgClockEdgeErrs,
       "ohsDiag": ohsDiag,
       "eriDNXOctalHSMIB": eriDNXOctalHSMIB}
)
