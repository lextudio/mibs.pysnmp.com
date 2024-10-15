# SNMP MIB module (EICON-SDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-SDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:49 2024
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


# Types definitions



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("other", 1),
          ("ready", 3))
    )





class AdminState(Integer32):
    """Custom type AdminState based on Integer32"""
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
        *(("dump", 3),
          ("invalid", 5),
          ("start", 1),
          ("stop", 2),
          ("test", 4))
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class LinkRef(Integer32):
    """Custom type LinkRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )





class StationAddr(Integer32):
    """Custom type StationAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Sdlc_ObjectIdentity = ObjectIdentity
sdlc = _Sdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2)
)
_SdlcCfgTable_Object = MibTable
sdlcCfgTable = _SdlcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sdlcCfgTable.setStatus("mandatory")
_SdlcCfgEntry_Object = MibTableRow
sdlcCfgEntry = _SdlcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1)
)
sdlcCfgEntry.setIndexNames(
    (0, "EICON-SDLC-MIB", "sdlcCfgPortRef"),
)
if mibBuilder.loadTexts:
    sdlcCfgEntry.setStatus("mandatory")
_SdlcCfgPortRef_Type = PortRef
_SdlcCfgPortRef_Object = MibTableColumn
sdlcCfgPortRef = _SdlcCfgPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 1),
    _SdlcCfgPortRef_Type()
)
sdlcCfgPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgPortRef.setStatus("mandatory")


class _SdlcCfgMaxLinkStation_Type(LinkRef):
    """Custom type sdlcCfgMaxLinkStation based on LinkRef"""
    defaultValue = 9


_SdlcCfgMaxLinkStation_Object = MibTableColumn
sdlcCfgMaxLinkStation = _SdlcCfgMaxLinkStation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 2),
    _SdlcCfgMaxLinkStation_Type()
)
sdlcCfgMaxLinkStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgMaxLinkStation.setStatus("mandatory")


class _SdlcCfgT1_Type(Integer32):
    """Custom type sdlcCfgT1 based on Integer32"""
    defaultValue = 2900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SdlcCfgT1_Type.__name__ = "Integer32"
_SdlcCfgT1_Object = MibTableColumn
sdlcCfgT1 = _SdlcCfgT1_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 3),
    _SdlcCfgT1_Type()
)
sdlcCfgT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgT1.setStatus("mandatory")


class _SdlcCfgT2_Type(Integer32):
    """Custom type sdlcCfgT2 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SdlcCfgT2_Type.__name__ = "Integer32"
_SdlcCfgT2_Object = MibTableColumn
sdlcCfgT2 = _SdlcCfgT2_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 4),
    _SdlcCfgT2_Type()
)
sdlcCfgT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgT2.setStatus("mandatory")


class _SdlcCfgT3_Type(Integer32):
    """Custom type sdlcCfgT3 based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_SdlcCfgT3_Type.__name__ = "Integer32"
_SdlcCfgT3_Object = MibTableColumn
sdlcCfgT3 = _SdlcCfgT3_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 5),
    _SdlcCfgT3_Type()
)
sdlcCfgT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgT3.setStatus("mandatory")


class _SdlcCfgT4_Type(Integer32):
    """Custom type sdlcCfgT4 based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_SdlcCfgT4_Type.__name__ = "Integer32"
_SdlcCfgT4_Object = MibTableColumn
sdlcCfgT4 = _SdlcCfgT4_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 6),
    _SdlcCfgT4_Type()
)
sdlcCfgT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgT4.setStatus("mandatory")


class _SdlcCfgMaxFrameSz_Type(Integer32):
    """Custom type sdlcCfgMaxFrameSz based on Integer32"""
    defaultValue = 267

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(267, 8203),
    )


_SdlcCfgMaxFrameSz_Type.__name__ = "Integer32"
_SdlcCfgMaxFrameSz_Object = MibTableColumn
sdlcCfgMaxFrameSz = _SdlcCfgMaxFrameSz_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 7),
    _SdlcCfgMaxFrameSz_Type()
)
sdlcCfgMaxFrameSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgMaxFrameSz.setStatus("mandatory")


class _SdlcCfgMaxRetryCount_Type(Integer32):
    """Custom type sdlcCfgMaxRetryCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SdlcCfgMaxRetryCount_Type.__name__ = "Integer32"
_SdlcCfgMaxRetryCount_Object = MibTableColumn
sdlcCfgMaxRetryCount = _SdlcCfgMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 8),
    _SdlcCfgMaxRetryCount_Type()
)
sdlcCfgMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgMaxRetryCount.setStatus("mandatory")


class _SdlcCfgMaxWindowSz_Type(Integer32):
    """Custom type sdlcCfgMaxWindowSz based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_SdlcCfgMaxWindowSz_Type.__name__ = "Integer32"
_SdlcCfgMaxWindowSz_Object = MibTableColumn
sdlcCfgMaxWindowSz = _SdlcCfgMaxWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 1, 1, 9),
    _SdlcCfgMaxWindowSz_Type()
)
sdlcCfgMaxWindowSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCfgMaxWindowSz.setStatus("mandatory")
_SdlcInfoTable_Object = MibTable
sdlcInfoTable = _SdlcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    sdlcInfoTable.setStatus("mandatory")
_SdlcInfoEntry_Object = MibTableRow
sdlcInfoEntry = _SdlcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1)
)
sdlcInfoEntry.setIndexNames(
    (0, "EICON-SDLC-MIB", "sdlcInfoPortRef"),
)
if mibBuilder.loadTexts:
    sdlcInfoEntry.setStatus("mandatory")
_SdlcInfoPortRef_Type = PortRef
_SdlcInfoPortRef_Object = MibTableColumn
sdlcInfoPortRef = _SdlcInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 1),
    _SdlcInfoPortRef_Type()
)
sdlcInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoPortRef.setStatus("mandatory")
_SdlcInfoAdminStatusCtr_Type = AdminState
_SdlcInfoAdminStatusCtr_Object = MibTableColumn
sdlcInfoAdminStatusCtr = _SdlcInfoAdminStatusCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 2),
    _SdlcInfoAdminStatusCtr_Type()
)
sdlcInfoAdminStatusCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcInfoAdminStatusCtr.setStatus("mandatory")
_SdlcInfoOperStatus_Type = OperState
_SdlcInfoOperStatus_Object = MibTableColumn
sdlcInfoOperStatus = _SdlcInfoOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 3),
    _SdlcInfoOperStatus_Type()
)
sdlcInfoOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoOperStatus.setStatus("mandatory")


class _SdlcInfoDial_Type(Integer32):
    """Custom type sdlcInfoDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial-up", 2),
          ("leased", 1))
    )


_SdlcInfoDial_Type.__name__ = "Integer32"
_SdlcInfoDial_Object = MibTableColumn
sdlcInfoDial = _SdlcInfoDial_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 4),
    _SdlcInfoDial_Type()
)
sdlcInfoDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoDial.setStatus("mandatory")


class _SdlcInfoDuplex_Type(Integer32):
    """Custom type sdlcInfoDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_SdlcInfoDuplex_Type.__name__ = "Integer32"
_SdlcInfoDuplex_Object = MibTableColumn
sdlcInfoDuplex = _SdlcInfoDuplex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 5),
    _SdlcInfoDuplex_Type()
)
sdlcInfoDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoDuplex.setStatus("mandatory")
_SdlcInfoMaxFrameSz_Type = Integer32
_SdlcInfoMaxFrameSz_Object = MibTableColumn
sdlcInfoMaxFrameSz = _SdlcInfoMaxFrameSz_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 6),
    _SdlcInfoMaxFrameSz_Type()
)
sdlcInfoMaxFrameSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoMaxFrameSz.setStatus("mandatory")
_SdlcInfoMaxRetryCount_Type = Integer32
_SdlcInfoMaxRetryCount_Object = MibTableColumn
sdlcInfoMaxRetryCount = _SdlcInfoMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 7),
    _SdlcInfoMaxRetryCount_Type()
)
sdlcInfoMaxRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoMaxRetryCount.setStatus("mandatory")
_SdlcInfoMaxWindowSz_Type = Integer32
_SdlcInfoMaxWindowSz_Object = MibTableColumn
sdlcInfoMaxWindowSz = _SdlcInfoMaxWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 8),
    _SdlcInfoMaxWindowSz_Type()
)
sdlcInfoMaxWindowSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoMaxWindowSz.setStatus("mandatory")
_SdlcInfoMaxLinkStation_Type = Integer32
_SdlcInfoMaxLinkStation_Object = MibTableColumn
sdlcInfoMaxLinkStation = _SdlcInfoMaxLinkStation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 9),
    _SdlcInfoMaxLinkStation_Type()
)
sdlcInfoMaxLinkStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoMaxLinkStation.setStatus("mandatory")
_SdlcInfoNbStationInUse_Type = Integer32
_SdlcInfoNbStationInUse_Object = MibTableColumn
sdlcInfoNbStationInUse = _SdlcInfoNbStationInUse_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 10),
    _SdlcInfoNbStationInUse_Type()
)
sdlcInfoNbStationInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoNbStationInUse.setStatus("mandatory")
_SdlcInfoStartTime_Type = TimeTicks
_SdlcInfoStartTime_Object = MibTableColumn
sdlcInfoStartTime = _SdlcInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 11),
    _SdlcInfoStartTime_Type()
)
sdlcInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoStartTime.setStatus("mandatory")
_SdlcInfoModemTime_Type = TimeTicks
_SdlcInfoModemTime_Object = MibTableColumn
sdlcInfoModemTime = _SdlcInfoModemTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 2, 1, 12),
    _SdlcInfoModemTime_Type()
)
sdlcInfoModemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcInfoModemTime.setStatus("mandatory")
_SdlcLinkInfoTable_Object = MibTable
sdlcLinkInfoTable = _SdlcLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    sdlcLinkInfoTable.setStatus("mandatory")
_SdlcLinkInfoEntry_Object = MibTableRow
sdlcLinkInfoEntry = _SdlcLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1)
)
sdlcLinkInfoEntry.setIndexNames(
    (0, "EICON-SDLC-MIB", "sdlcLinkInfoPortRef"),
    (0, "EICON-SDLC-MIB", "sdlcLinkInfoStationAddr"),
)
if mibBuilder.loadTexts:
    sdlcLinkInfoEntry.setStatus("mandatory")
_SdlcLinkInfoPortRef_Type = PortRef
_SdlcLinkInfoPortRef_Object = MibTableColumn
sdlcLinkInfoPortRef = _SdlcLinkInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 1),
    _SdlcLinkInfoPortRef_Type()
)
sdlcLinkInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoPortRef.setStatus("mandatory")
_SdlcLinkInfoStationAddr_Type = StationAddr
_SdlcLinkInfoStationAddr_Object = MibTableColumn
sdlcLinkInfoStationAddr = _SdlcLinkInfoStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 2),
    _SdlcLinkInfoStationAddr_Type()
)
sdlcLinkInfoStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoStationAddr.setStatus("mandatory")
_SdlcLinkInfoAdminStatusCtr_Type = AdminState
_SdlcLinkInfoAdminStatusCtr_Object = MibTableColumn
sdlcLinkInfoAdminStatusCtr = _SdlcLinkInfoAdminStatusCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 3),
    _SdlcLinkInfoAdminStatusCtr_Type()
)
sdlcLinkInfoAdminStatusCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdlcLinkInfoAdminStatusCtr.setStatus("mandatory")


class _SdlcLinkInfoProtocolState_Type(Integer32):
    """Custom type sdlcLinkInfoProtocolState based on Integer32"""
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
        *(("closed", 1),
          ("closing", 2),
          ("opened", 4),
          ("opening", 3),
          ("resetting", 5),
          ("wait-open", 7),
          ("wait-reset", 6),
          ("xid-recv", 9),
          ("xid-send", 8))
    )


_SdlcLinkInfoProtocolState_Type.__name__ = "Integer32"
_SdlcLinkInfoProtocolState_Object = MibTableColumn
sdlcLinkInfoProtocolState = _SdlcLinkInfoProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 4),
    _SdlcLinkInfoProtocolState_Type()
)
sdlcLinkInfoProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoProtocolState.setStatus("mandatory")


class _SdlcLinkInfoUserState_Type(Integer32):
    """Custom type sdlcLinkInfoUserState based on Integer32"""
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
        *(("closed", 1),
          ("closing", 2),
          ("opened", 4),
          ("opening", 3),
          ("other", 5))
    )


_SdlcLinkInfoUserState_Type.__name__ = "Integer32"
_SdlcLinkInfoUserState_Object = MibTableColumn
sdlcLinkInfoUserState = _SdlcLinkInfoUserState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 5),
    _SdlcLinkInfoUserState_Type()
)
sdlcLinkInfoUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoUserState.setStatus("mandatory")


class _SdlcLinkInfoStationType_Type(Integer32):
    """Custom type sdlcLinkInfoStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiable", 3),
          ("primary", 2),
          ("secondary", 1))
    )


_SdlcLinkInfoStationType_Type.__name__ = "Integer32"
_SdlcLinkInfoStationType_Object = MibTableColumn
sdlcLinkInfoStationType = _SdlcLinkInfoStationType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 6),
    _SdlcLinkInfoStationType_Type()
)
sdlcLinkInfoStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoStationType.setStatus("mandatory")
_SdlcLinkInfoStartTime_Type = TimeTicks
_SdlcLinkInfoStartTime_Object = MibTableColumn
sdlcLinkInfoStartTime = _SdlcLinkInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 7),
    _SdlcLinkInfoStartTime_Type()
)
sdlcLinkInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoStartTime.setStatus("mandatory")
_SdlcLinkInfoChangeTime_Type = TimeTicks
_SdlcLinkInfoChangeTime_Object = MibTableColumn
sdlcLinkInfoChangeTime = _SdlcLinkInfoChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 8),
    _SdlcLinkInfoChangeTime_Type()
)
sdlcLinkInfoChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoChangeTime.setStatus("mandatory")
_SdlcLinkInfoDataTime_Type = TimeTicks
_SdlcLinkInfoDataTime_Object = MibTableColumn
sdlcLinkInfoDataTime = _SdlcLinkInfoDataTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 9),
    _SdlcLinkInfoDataTime_Type()
)
sdlcLinkInfoDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoDataTime.setStatus("mandatory")
_SdlcLinkInfoMaxOut_Type = Integer32
_SdlcLinkInfoMaxOut_Object = MibTableColumn
sdlcLinkInfoMaxOut = _SdlcLinkInfoMaxOut_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 10),
    _SdlcLinkInfoMaxOut_Type()
)
sdlcLinkInfoMaxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoMaxOut.setStatus("mandatory")
_SdlcLinkInfoMaxIn_Type = Integer32
_SdlcLinkInfoMaxIn_Object = MibTableColumn
sdlcLinkInfoMaxIn = _SdlcLinkInfoMaxIn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 11),
    _SdlcLinkInfoMaxIn_Type()
)
sdlcLinkInfoMaxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoMaxIn.setStatus("mandatory")
_SdlcLinkInfoMaxData_Type = Integer32
_SdlcLinkInfoMaxData_Object = MibTableColumn
sdlcLinkInfoMaxData = _SdlcLinkInfoMaxData_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 12),
    _SdlcLinkInfoMaxData_Type()
)
sdlcLinkInfoMaxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoMaxData.setStatus("mandatory")
_SdlcLinkInfoLocalBusy_Type = Integer32
_SdlcLinkInfoLocalBusy_Object = MibTableColumn
sdlcLinkInfoLocalBusy = _SdlcLinkInfoLocalBusy_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 13),
    _SdlcLinkInfoLocalBusy_Type()
)
sdlcLinkInfoLocalBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoLocalBusy.setStatus("mandatory")
_SdlcLinkInfoRemoteBusy_Type = Integer32
_SdlcLinkInfoRemoteBusy_Object = MibTableColumn
sdlcLinkInfoRemoteBusy = _SdlcLinkInfoRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 14),
    _SdlcLinkInfoRemoteBusy_Type()
)
sdlcLinkInfoRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoRemoteBusy.setStatus("mandatory")
_SdlcLinkInfoNS_Type = Integer32
_SdlcLinkInfoNS_Object = MibTableColumn
sdlcLinkInfoNS = _SdlcLinkInfoNS_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 15),
    _SdlcLinkInfoNS_Type()
)
sdlcLinkInfoNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoNS.setStatus("mandatory")
_SdlcLinkInfoNR_Type = Integer32
_SdlcLinkInfoNR_Object = MibTableColumn
sdlcLinkInfoNR = _SdlcLinkInfoNR_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 16),
    _SdlcLinkInfoNR_Type()
)
sdlcLinkInfoNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoNR.setStatus("mandatory")
_SdlcLinkInfoLNR_Type = Integer32
_SdlcLinkInfoLNR_Object = MibTableColumn
sdlcLinkInfoLNR = _SdlcLinkInfoLNR_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 3, 1, 17),
    _SdlcLinkInfoLNR_Type()
)
sdlcLinkInfoLNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkInfoLNR.setStatus("mandatory")
_SdlcCountTable_Object = MibTable
sdlcCountTable = _SdlcCountTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    sdlcCountTable.setStatus("mandatory")
_SdlcCountEntry_Object = MibTableRow
sdlcCountEntry = _SdlcCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1)
)
sdlcCountEntry.setIndexNames(
    (0, "EICON-SDLC-MIB", "sdlcCountPortRef"),
)
if mibBuilder.loadTexts:
    sdlcCountEntry.setStatus("mandatory")
_SdlcCountPortRef_Type = PortRef
_SdlcCountPortRef_Object = MibTableColumn
sdlcCountPortRef = _SdlcCountPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 1),
    _SdlcCountPortRef_Type()
)
sdlcCountPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountPortRef.setStatus("mandatory")
_SdlcCountT1expires_Type = Counter32
_SdlcCountT1expires_Object = MibTableColumn
sdlcCountT1expires = _SdlcCountT1expires_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 2),
    _SdlcCountT1expires_Type()
)
sdlcCountT1expires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountT1expires.setStatus("mandatory")
_SdlcCountRetransmis_Type = Counter32
_SdlcCountRetransmis_Object = MibTableColumn
sdlcCountRetransmis = _SdlcCountRetransmis_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 3),
    _SdlcCountRetransmis_Type()
)
sdlcCountRetransmis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRetransmis.setStatus("mandatory")
_SdlcCountSNRMTxs_Type = Counter32
_SdlcCountSNRMTxs_Object = MibTableColumn
sdlcCountSNRMTxs = _SdlcCountSNRMTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 4),
    _SdlcCountSNRMTxs_Type()
)
sdlcCountSNRMTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountSNRMTxs.setStatus("mandatory")
_SdlcCountSNRMRxs_Type = Counter32
_SdlcCountSNRMRxs_Object = MibTableColumn
sdlcCountSNRMRxs = _SdlcCountSNRMRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 5),
    _SdlcCountSNRMRxs_Type()
)
sdlcCountSNRMRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountSNRMRxs.setStatus("mandatory")
_SdlcCountDISCTxs_Type = Counter32
_SdlcCountDISCTxs_Object = MibTableColumn
sdlcCountDISCTxs = _SdlcCountDISCTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 6),
    _SdlcCountDISCTxs_Type()
)
sdlcCountDISCTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountDISCTxs.setStatus("mandatory")
_SdlcCountDISCRxs_Type = Counter32
_SdlcCountDISCRxs_Object = MibTableColumn
sdlcCountDISCRxs = _SdlcCountDISCRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 7),
    _SdlcCountDISCRxs_Type()
)
sdlcCountDISCRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountDISCRxs.setStatus("mandatory")
_SdlcCountUAsTxs_Type = Counter32
_SdlcCountUAsTxs_Object = MibTableColumn
sdlcCountUAsTxs = _SdlcCountUAsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 8),
    _SdlcCountUAsTxs_Type()
)
sdlcCountUAsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountUAsTxs.setStatus("mandatory")
_SdlcCountUAsRxs_Type = Counter32
_SdlcCountUAsRxs_Object = MibTableColumn
sdlcCountUAsRxs = _SdlcCountUAsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 9),
    _SdlcCountUAsRxs_Type()
)
sdlcCountUAsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountUAsRxs.setStatus("mandatory")
_SdlcCountDMsTxs_Type = Counter32
_SdlcCountDMsTxs_Object = MibTableColumn
sdlcCountDMsTxs = _SdlcCountDMsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 10),
    _SdlcCountDMsTxs_Type()
)
sdlcCountDMsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountDMsTxs.setStatus("mandatory")
_SdlcCountDMsRxs_Type = Counter32
_SdlcCountDMsRxs_Object = MibTableColumn
sdlcCountDMsRxs = _SdlcCountDMsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 11),
    _SdlcCountDMsRxs_Type()
)
sdlcCountDMsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountDMsRxs.setStatus("mandatory")
_SdlcCountFRMRsTxs_Type = Counter32
_SdlcCountFRMRsTxs_Object = MibTableColumn
sdlcCountFRMRsTxs = _SdlcCountFRMRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 12),
    _SdlcCountFRMRsTxs_Type()
)
sdlcCountFRMRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountFRMRsTxs.setStatus("mandatory")
_SdlcCountFRMRsRxs_Type = Counter32
_SdlcCountFRMRsRxs_Object = MibTableColumn
sdlcCountFRMRsRxs = _SdlcCountFRMRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 13),
    _SdlcCountFRMRsRxs_Type()
)
sdlcCountFRMRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountFRMRsRxs.setStatus("mandatory")
_SdlcCountXIDsTxs_Type = Counter32
_SdlcCountXIDsTxs_Object = MibTableColumn
sdlcCountXIDsTxs = _SdlcCountXIDsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 14),
    _SdlcCountXIDsTxs_Type()
)
sdlcCountXIDsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountXIDsTxs.setStatus("mandatory")
_SdlcCountXIDsRxs_Type = Counter32
_SdlcCountXIDsRxs_Object = MibTableColumn
sdlcCountXIDsRxs = _SdlcCountXIDsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 15),
    _SdlcCountXIDsRxs_Type()
)
sdlcCountXIDsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountXIDsRxs.setStatus("mandatory")
_SdlcCountINFOsTxs_Type = Counter32
_SdlcCountINFOsTxs_Object = MibTableColumn
sdlcCountINFOsTxs = _SdlcCountINFOsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 16),
    _SdlcCountINFOsTxs_Type()
)
sdlcCountINFOsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountINFOsTxs.setStatus("mandatory")
_SdlcCountINFOsRxs_Type = Counter32
_SdlcCountINFOsRxs_Object = MibTableColumn
sdlcCountINFOsRxs = _SdlcCountINFOsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 17),
    _SdlcCountINFOsRxs_Type()
)
sdlcCountINFOsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountINFOsRxs.setStatus("mandatory")
_SdlcCountRRsTxs_Type = Counter32
_SdlcCountRRsTxs_Object = MibTableColumn
sdlcCountRRsTxs = _SdlcCountRRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 18),
    _SdlcCountRRsTxs_Type()
)
sdlcCountRRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRRsTxs.setStatus("mandatory")
_SdlcCountRRsRxs_Type = Counter32
_SdlcCountRRsRxs_Object = MibTableColumn
sdlcCountRRsRxs = _SdlcCountRRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 19),
    _SdlcCountRRsRxs_Type()
)
sdlcCountRRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRRsRxs.setStatus("mandatory")
_SdlcCountRNRsTxs_Type = Counter32
_SdlcCountRNRsTxs_Object = MibTableColumn
sdlcCountRNRsTxs = _SdlcCountRNRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 20),
    _SdlcCountRNRsTxs_Type()
)
sdlcCountRNRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRNRsTxs.setStatus("mandatory")
_SdlcCountRNRsRxs_Type = Counter32
_SdlcCountRNRsRxs_Object = MibTableColumn
sdlcCountRNRsRxs = _SdlcCountRNRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 21),
    _SdlcCountRNRsRxs_Type()
)
sdlcCountRNRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRNRsRxs.setStatus("mandatory")
_SdlcCountREJsTxs_Type = Counter32
_SdlcCountREJsTxs_Object = MibTableColumn
sdlcCountREJsTxs = _SdlcCountREJsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 22),
    _SdlcCountREJsTxs_Type()
)
sdlcCountREJsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountREJsTxs.setStatus("mandatory")
_SdlcCountREJsRxs_Type = Counter32
_SdlcCountREJsRxs_Object = MibTableColumn
sdlcCountREJsRxs = _SdlcCountREJsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 23),
    _SdlcCountREJsRxs_Type()
)
sdlcCountREJsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountREJsRxs.setStatus("mandatory")
_SdlcCountTestTxs_Type = Counter32
_SdlcCountTestTxs_Object = MibTableColumn
sdlcCountTestTxs = _SdlcCountTestTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 24),
    _SdlcCountTestTxs_Type()
)
sdlcCountTestTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountTestTxs.setStatus("mandatory")
_SdlcCountTestRxs_Type = Counter32
_SdlcCountTestRxs_Object = MibTableColumn
sdlcCountTestRxs = _SdlcCountTestRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 25),
    _SdlcCountTestRxs_Type()
)
sdlcCountTestRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountTestRxs.setStatus("mandatory")
_SdlcCountBadFcsTxs_Type = Counter32
_SdlcCountBadFcsTxs_Object = MibTableColumn
sdlcCountBadFcsTxs = _SdlcCountBadFcsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 26),
    _SdlcCountBadFcsTxs_Type()
)
sdlcCountBadFcsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountBadFcsTxs.setStatus("mandatory")
_SdlcCountBadFcsRxs_Type = Counter32
_SdlcCountBadFcsRxs_Object = MibTableColumn
sdlcCountBadFcsRxs = _SdlcCountBadFcsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 27),
    _SdlcCountBadFcsRxs_Type()
)
sdlcCountBadFcsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountBadFcsRxs.setStatus("mandatory")
_SdlcCountAbortTxs_Type = Counter32
_SdlcCountAbortTxs_Object = MibTableColumn
sdlcCountAbortTxs = _SdlcCountAbortTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 28),
    _SdlcCountAbortTxs_Type()
)
sdlcCountAbortTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountAbortTxs.setStatus("mandatory")
_SdlcCountAbortRxs_Type = Counter32
_SdlcCountAbortRxs_Object = MibTableColumn
sdlcCountAbortRxs = _SdlcCountAbortRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 29),
    _SdlcCountAbortRxs_Type()
)
sdlcCountAbortRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountAbortRxs.setStatus("mandatory")
_SdlcCountTxUnderRs_Type = Counter32
_SdlcCountTxUnderRs_Object = MibTableColumn
sdlcCountTxUnderRs = _SdlcCountTxUnderRs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 30),
    _SdlcCountTxUnderRs_Type()
)
sdlcCountTxUnderRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountTxUnderRs.setStatus("mandatory")
_SdlcCountRxOverRs_Type = Counter32
_SdlcCountRxOverRs_Object = MibTableColumn
sdlcCountRxOverRs = _SdlcCountRxOverRs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 31),
    _SdlcCountRxOverRs_Type()
)
sdlcCountRxOverRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountRxOverRs.setStatus("mandatory")
_SdlcCountUnknowTxs_Type = Counter32
_SdlcCountUnknowTxs_Object = MibTableColumn
sdlcCountUnknowTxs = _SdlcCountUnknowTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 32),
    _SdlcCountUnknowTxs_Type()
)
sdlcCountUnknowTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountUnknowTxs.setStatus("mandatory")
_SdlcCountUnknowRxs_Type = Counter32
_SdlcCountUnknowRxs_Object = MibTableColumn
sdlcCountUnknowRxs = _SdlcCountUnknowRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 4, 1, 33),
    _SdlcCountUnknowRxs_Type()
)
sdlcCountUnknowRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcCountUnknowRxs.setStatus("mandatory")
_SdlcLinkCountTable_Object = MibTable
sdlcLinkCountTable = _SdlcLinkCountTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    sdlcLinkCountTable.setStatus("mandatory")
_SdlcLinkCountEntry_Object = MibTableRow
sdlcLinkCountEntry = _SdlcLinkCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1)
)
sdlcLinkCountEntry.setIndexNames(
    (0, "EICON-SDLC-MIB", "sdlcLinkCountPortRef"),
    (0, "EICON-SDLC-MIB", "sdlcLinkCountStationRef"),
)
if mibBuilder.loadTexts:
    sdlcLinkCountEntry.setStatus("mandatory")
_SdlcLinkCountPortRef_Type = PortRef
_SdlcLinkCountPortRef_Object = MibTableColumn
sdlcLinkCountPortRef = _SdlcLinkCountPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 1),
    _SdlcLinkCountPortRef_Type()
)
sdlcLinkCountPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountPortRef.setStatus("mandatory")
_SdlcLinkCountStationRef_Type = StationAddr
_SdlcLinkCountStationRef_Object = MibTableColumn
sdlcLinkCountStationRef = _SdlcLinkCountStationRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 2),
    _SdlcLinkCountStationRef_Type()
)
sdlcLinkCountStationRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountStationRef.setStatus("mandatory")
_SdlcLinkCountT1expires_Type = Counter32
_SdlcLinkCountT1expires_Object = MibTableColumn
sdlcLinkCountT1expires = _SdlcLinkCountT1expires_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 3),
    _SdlcLinkCountT1expires_Type()
)
sdlcLinkCountT1expires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountT1expires.setStatus("mandatory")
_SdlcLinkCountRetransmis_Type = Counter32
_SdlcLinkCountRetransmis_Object = MibTableColumn
sdlcLinkCountRetransmis = _SdlcLinkCountRetransmis_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 4),
    _SdlcLinkCountRetransmis_Type()
)
sdlcLinkCountRetransmis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountRetransmis.setStatus("mandatory")
_SdlcLinkCountSNRMTxs_Type = Counter32
_SdlcLinkCountSNRMTxs_Object = MibTableColumn
sdlcLinkCountSNRMTxs = _SdlcLinkCountSNRMTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 5),
    _SdlcLinkCountSNRMTxs_Type()
)
sdlcLinkCountSNRMTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountSNRMTxs.setStatus("mandatory")
_SdlcLinkCountSNRMRxs_Type = Counter32
_SdlcLinkCountSNRMRxs_Object = MibTableColumn
sdlcLinkCountSNRMRxs = _SdlcLinkCountSNRMRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 6),
    _SdlcLinkCountSNRMRxs_Type()
)
sdlcLinkCountSNRMRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountSNRMRxs.setStatus("mandatory")
_SdlcLinkCountDISCTxs_Type = Counter32
_SdlcLinkCountDISCTxs_Object = MibTableColumn
sdlcLinkCountDISCTxs = _SdlcLinkCountDISCTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 7),
    _SdlcLinkCountDISCTxs_Type()
)
sdlcLinkCountDISCTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountDISCTxs.setStatus("mandatory")
_SdlcLinkCountDISCRxs_Type = Counter32
_SdlcLinkCountDISCRxs_Object = MibTableColumn
sdlcLinkCountDISCRxs = _SdlcLinkCountDISCRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 8),
    _SdlcLinkCountDISCRxs_Type()
)
sdlcLinkCountDISCRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountDISCRxs.setStatus("mandatory")
_SdlcLinkCountUAsTxs_Type = Counter32
_SdlcLinkCountUAsTxs_Object = MibTableColumn
sdlcLinkCountUAsTxs = _SdlcLinkCountUAsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 9),
    _SdlcLinkCountUAsTxs_Type()
)
sdlcLinkCountUAsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountUAsTxs.setStatus("mandatory")
_SdlcLinkCountUAsRxs_Type = Counter32
_SdlcLinkCountUAsRxs_Object = MibTableColumn
sdlcLinkCountUAsRxs = _SdlcLinkCountUAsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 10),
    _SdlcLinkCountUAsRxs_Type()
)
sdlcLinkCountUAsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountUAsRxs.setStatus("mandatory")
_SdlcLinkCountDMsTxs_Type = Counter32
_SdlcLinkCountDMsTxs_Object = MibTableColumn
sdlcLinkCountDMsTxs = _SdlcLinkCountDMsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 11),
    _SdlcLinkCountDMsTxs_Type()
)
sdlcLinkCountDMsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountDMsTxs.setStatus("mandatory")
_SdlcLinkCountDMsRxs_Type = Counter32
_SdlcLinkCountDMsRxs_Object = MibTableColumn
sdlcLinkCountDMsRxs = _SdlcLinkCountDMsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 12),
    _SdlcLinkCountDMsRxs_Type()
)
sdlcLinkCountDMsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountDMsRxs.setStatus("mandatory")
_SdlcLinkCountFRMRsTxs_Type = Counter32
_SdlcLinkCountFRMRsTxs_Object = MibTableColumn
sdlcLinkCountFRMRsTxs = _SdlcLinkCountFRMRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 13),
    _SdlcLinkCountFRMRsTxs_Type()
)
sdlcLinkCountFRMRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountFRMRsTxs.setStatus("mandatory")
_SdlcLinkCountFRMRsRxs_Type = Counter32
_SdlcLinkCountFRMRsRxs_Object = MibTableColumn
sdlcLinkCountFRMRsRxs = _SdlcLinkCountFRMRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 14),
    _SdlcLinkCountFRMRsRxs_Type()
)
sdlcLinkCountFRMRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountFRMRsRxs.setStatus("mandatory")
_SdlcLinkCountXIDsTxs_Type = Counter32
_SdlcLinkCountXIDsTxs_Object = MibTableColumn
sdlcLinkCountXIDsTxs = _SdlcLinkCountXIDsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 15),
    _SdlcLinkCountXIDsTxs_Type()
)
sdlcLinkCountXIDsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountXIDsTxs.setStatus("mandatory")
_SdlcLinkCountXIDsRxs_Type = Counter32
_SdlcLinkCountXIDsRxs_Object = MibTableColumn
sdlcLinkCountXIDsRxs = _SdlcLinkCountXIDsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 16),
    _SdlcLinkCountXIDsRxs_Type()
)
sdlcLinkCountXIDsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountXIDsRxs.setStatus("mandatory")
_SdlcLinkCountINFOsTxs_Type = Counter32
_SdlcLinkCountINFOsTxs_Object = MibTableColumn
sdlcLinkCountINFOsTxs = _SdlcLinkCountINFOsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 17),
    _SdlcLinkCountINFOsTxs_Type()
)
sdlcLinkCountINFOsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountINFOsTxs.setStatus("mandatory")
_SdlcLinkCountINFOsRxs_Type = Counter32
_SdlcLinkCountINFOsRxs_Object = MibTableColumn
sdlcLinkCountINFOsRxs = _SdlcLinkCountINFOsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 18),
    _SdlcLinkCountINFOsRxs_Type()
)
sdlcLinkCountINFOsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountINFOsRxs.setStatus("mandatory")
_SdlcLinkCountRRsTxs_Type = Counter32
_SdlcLinkCountRRsTxs_Object = MibTableColumn
sdlcLinkCountRRsTxs = _SdlcLinkCountRRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 19),
    _SdlcLinkCountRRsTxs_Type()
)
sdlcLinkCountRRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountRRsTxs.setStatus("mandatory")
_SdlcLinkCountRRsRxs_Type = Counter32
_SdlcLinkCountRRsRxs_Object = MibTableColumn
sdlcLinkCountRRsRxs = _SdlcLinkCountRRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 21),
    _SdlcLinkCountRRsRxs_Type()
)
sdlcLinkCountRRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountRRsRxs.setStatus("mandatory")
_SdlcLinkCountRNRsTxs_Type = Counter32
_SdlcLinkCountRNRsTxs_Object = MibTableColumn
sdlcLinkCountRNRsTxs = _SdlcLinkCountRNRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 22),
    _SdlcLinkCountRNRsTxs_Type()
)
sdlcLinkCountRNRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountRNRsTxs.setStatus("mandatory")
_SdlcLinkCountRNRsRxs_Type = Counter32
_SdlcLinkCountRNRsRxs_Object = MibTableColumn
sdlcLinkCountRNRsRxs = _SdlcLinkCountRNRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 23),
    _SdlcLinkCountRNRsRxs_Type()
)
sdlcLinkCountRNRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountRNRsRxs.setStatus("mandatory")
_SdlcLinkCountREJsTxs_Type = Counter32
_SdlcLinkCountREJsTxs_Object = MibTableColumn
sdlcLinkCountREJsTxs = _SdlcLinkCountREJsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 24),
    _SdlcLinkCountREJsTxs_Type()
)
sdlcLinkCountREJsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountREJsTxs.setStatus("mandatory")
_SdlcLinkCountREJsRxs_Type = Counter32
_SdlcLinkCountREJsRxs_Object = MibTableColumn
sdlcLinkCountREJsRxs = _SdlcLinkCountREJsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 25),
    _SdlcLinkCountREJsRxs_Type()
)
sdlcLinkCountREJsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountREJsRxs.setStatus("mandatory")
_SdlcLinkCountTestTxs_Type = Counter32
_SdlcLinkCountTestTxs_Object = MibTableColumn
sdlcLinkCountTestTxs = _SdlcLinkCountTestTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 26),
    _SdlcLinkCountTestTxs_Type()
)
sdlcLinkCountTestTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountTestTxs.setStatus("mandatory")
_SdlcLinkCountTestRxs_Type = Counter32
_SdlcLinkCountTestRxs_Object = MibTableColumn
sdlcLinkCountTestRxs = _SdlcLinkCountTestRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 2, 5, 1, 27),
    _SdlcLinkCountTestRxs_Type()
)
sdlcLinkCountTestRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdlcLinkCountTestRxs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-SDLC-MIB",
    **{"OperState": OperState,
       "AdminState": AdminState,
       "PortRef": PortRef,
       "LinkRef": LinkRef,
       "StationAddr": StationAddr,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "sdlc": sdlc,
       "sdlcCfgTable": sdlcCfgTable,
       "sdlcCfgEntry": sdlcCfgEntry,
       "sdlcCfgPortRef": sdlcCfgPortRef,
       "sdlcCfgMaxLinkStation": sdlcCfgMaxLinkStation,
       "sdlcCfgT1": sdlcCfgT1,
       "sdlcCfgT2": sdlcCfgT2,
       "sdlcCfgT3": sdlcCfgT3,
       "sdlcCfgT4": sdlcCfgT4,
       "sdlcCfgMaxFrameSz": sdlcCfgMaxFrameSz,
       "sdlcCfgMaxRetryCount": sdlcCfgMaxRetryCount,
       "sdlcCfgMaxWindowSz": sdlcCfgMaxWindowSz,
       "sdlcInfoTable": sdlcInfoTable,
       "sdlcInfoEntry": sdlcInfoEntry,
       "sdlcInfoPortRef": sdlcInfoPortRef,
       "sdlcInfoAdminStatusCtr": sdlcInfoAdminStatusCtr,
       "sdlcInfoOperStatus": sdlcInfoOperStatus,
       "sdlcInfoDial": sdlcInfoDial,
       "sdlcInfoDuplex": sdlcInfoDuplex,
       "sdlcInfoMaxFrameSz": sdlcInfoMaxFrameSz,
       "sdlcInfoMaxRetryCount": sdlcInfoMaxRetryCount,
       "sdlcInfoMaxWindowSz": sdlcInfoMaxWindowSz,
       "sdlcInfoMaxLinkStation": sdlcInfoMaxLinkStation,
       "sdlcInfoNbStationInUse": sdlcInfoNbStationInUse,
       "sdlcInfoStartTime": sdlcInfoStartTime,
       "sdlcInfoModemTime": sdlcInfoModemTime,
       "sdlcLinkInfoTable": sdlcLinkInfoTable,
       "sdlcLinkInfoEntry": sdlcLinkInfoEntry,
       "sdlcLinkInfoPortRef": sdlcLinkInfoPortRef,
       "sdlcLinkInfoStationAddr": sdlcLinkInfoStationAddr,
       "sdlcLinkInfoAdminStatusCtr": sdlcLinkInfoAdminStatusCtr,
       "sdlcLinkInfoProtocolState": sdlcLinkInfoProtocolState,
       "sdlcLinkInfoUserState": sdlcLinkInfoUserState,
       "sdlcLinkInfoStationType": sdlcLinkInfoStationType,
       "sdlcLinkInfoStartTime": sdlcLinkInfoStartTime,
       "sdlcLinkInfoChangeTime": sdlcLinkInfoChangeTime,
       "sdlcLinkInfoDataTime": sdlcLinkInfoDataTime,
       "sdlcLinkInfoMaxOut": sdlcLinkInfoMaxOut,
       "sdlcLinkInfoMaxIn": sdlcLinkInfoMaxIn,
       "sdlcLinkInfoMaxData": sdlcLinkInfoMaxData,
       "sdlcLinkInfoLocalBusy": sdlcLinkInfoLocalBusy,
       "sdlcLinkInfoRemoteBusy": sdlcLinkInfoRemoteBusy,
       "sdlcLinkInfoNS": sdlcLinkInfoNS,
       "sdlcLinkInfoNR": sdlcLinkInfoNR,
       "sdlcLinkInfoLNR": sdlcLinkInfoLNR,
       "sdlcCountTable": sdlcCountTable,
       "sdlcCountEntry": sdlcCountEntry,
       "sdlcCountPortRef": sdlcCountPortRef,
       "sdlcCountT1expires": sdlcCountT1expires,
       "sdlcCountRetransmis": sdlcCountRetransmis,
       "sdlcCountSNRMTxs": sdlcCountSNRMTxs,
       "sdlcCountSNRMRxs": sdlcCountSNRMRxs,
       "sdlcCountDISCTxs": sdlcCountDISCTxs,
       "sdlcCountDISCRxs": sdlcCountDISCRxs,
       "sdlcCountUAsTxs": sdlcCountUAsTxs,
       "sdlcCountUAsRxs": sdlcCountUAsRxs,
       "sdlcCountDMsTxs": sdlcCountDMsTxs,
       "sdlcCountDMsRxs": sdlcCountDMsRxs,
       "sdlcCountFRMRsTxs": sdlcCountFRMRsTxs,
       "sdlcCountFRMRsRxs": sdlcCountFRMRsRxs,
       "sdlcCountXIDsTxs": sdlcCountXIDsTxs,
       "sdlcCountXIDsRxs": sdlcCountXIDsRxs,
       "sdlcCountINFOsTxs": sdlcCountINFOsTxs,
       "sdlcCountINFOsRxs": sdlcCountINFOsRxs,
       "sdlcCountRRsTxs": sdlcCountRRsTxs,
       "sdlcCountRRsRxs": sdlcCountRRsRxs,
       "sdlcCountRNRsTxs": sdlcCountRNRsTxs,
       "sdlcCountRNRsRxs": sdlcCountRNRsRxs,
       "sdlcCountREJsTxs": sdlcCountREJsTxs,
       "sdlcCountREJsRxs": sdlcCountREJsRxs,
       "sdlcCountTestTxs": sdlcCountTestTxs,
       "sdlcCountTestRxs": sdlcCountTestRxs,
       "sdlcCountBadFcsTxs": sdlcCountBadFcsTxs,
       "sdlcCountBadFcsRxs": sdlcCountBadFcsRxs,
       "sdlcCountAbortTxs": sdlcCountAbortTxs,
       "sdlcCountAbortRxs": sdlcCountAbortRxs,
       "sdlcCountTxUnderRs": sdlcCountTxUnderRs,
       "sdlcCountRxOverRs": sdlcCountRxOverRs,
       "sdlcCountUnknowTxs": sdlcCountUnknowTxs,
       "sdlcCountUnknowRxs": sdlcCountUnknowRxs,
       "sdlcLinkCountTable": sdlcLinkCountTable,
       "sdlcLinkCountEntry": sdlcLinkCountEntry,
       "sdlcLinkCountPortRef": sdlcLinkCountPortRef,
       "sdlcLinkCountStationRef": sdlcLinkCountStationRef,
       "sdlcLinkCountT1expires": sdlcLinkCountT1expires,
       "sdlcLinkCountRetransmis": sdlcLinkCountRetransmis,
       "sdlcLinkCountSNRMTxs": sdlcLinkCountSNRMTxs,
       "sdlcLinkCountSNRMRxs": sdlcLinkCountSNRMRxs,
       "sdlcLinkCountDISCTxs": sdlcLinkCountDISCTxs,
       "sdlcLinkCountDISCRxs": sdlcLinkCountDISCRxs,
       "sdlcLinkCountUAsTxs": sdlcLinkCountUAsTxs,
       "sdlcLinkCountUAsRxs": sdlcLinkCountUAsRxs,
       "sdlcLinkCountDMsTxs": sdlcLinkCountDMsTxs,
       "sdlcLinkCountDMsRxs": sdlcLinkCountDMsRxs,
       "sdlcLinkCountFRMRsTxs": sdlcLinkCountFRMRsTxs,
       "sdlcLinkCountFRMRsRxs": sdlcLinkCountFRMRsRxs,
       "sdlcLinkCountXIDsTxs": sdlcLinkCountXIDsTxs,
       "sdlcLinkCountXIDsRxs": sdlcLinkCountXIDsRxs,
       "sdlcLinkCountINFOsTxs": sdlcLinkCountINFOsTxs,
       "sdlcLinkCountINFOsRxs": sdlcLinkCountINFOsRxs,
       "sdlcLinkCountRRsTxs": sdlcLinkCountRRsTxs,
       "sdlcLinkCountRRsRxs": sdlcLinkCountRRsRxs,
       "sdlcLinkCountRNRsTxs": sdlcLinkCountRNRsTxs,
       "sdlcLinkCountRNRsRxs": sdlcLinkCountRNRsRxs,
       "sdlcLinkCountREJsTxs": sdlcLinkCountREJsTxs,
       "sdlcLinkCountREJsRxs": sdlcLinkCountREJsRxs,
       "sdlcLinkCountTestTxs": sdlcLinkCountTestTxs,
       "sdlcLinkCountTestRxs": sdlcLinkCountTestRxs}
)
