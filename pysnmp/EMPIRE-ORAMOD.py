# SNMP MIB module (EMPIRE-ORAMOD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMPIRE-ORAMOD
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:28 2024
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

_Empire_ObjectIdentity = ObjectIdentity
empire = _Empire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546)
)
_Applications_ObjectIdentity = ObjectIdentity
applications = _Applications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16)
)
_Oracledb_ObjectIdentity = ObjectIdentity
oracledb = _Oracledb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4)
)
_OraModVersion_Type = DisplayString
_OraModVersion_Object = MibScalar
oraModVersion = _OraModVersion_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 1),
    _OraModVersion_Type()
)
oraModVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraModVersion.setStatus("mandatory")


class _OraModMode_Type(Integer32):
    """Custom type oraModMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMode", 1),
          ("restrictedMode", 2))
    )


_OraModMode_Type.__name__ = "Integer32"
_OraModMode_Object = MibScalar
oraModMode = _OraModMode_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 2),
    _OraModMode_Type()
)
oraModMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraModMode.setStatus("mandatory")
_OraFlag_Type = DisplayString
_OraFlag_Object = MibScalar
oraFlag = _OraFlag_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 3),
    _OraFlag_Type()
)
oraFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraFlag.setStatus("mandatory")
_OramodCfg_ObjectIdentity = ObjectIdentity
oramodCfg = _OramodCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10)
)
_OramodDbCfg_ObjectIdentity = ObjectIdentity
oramodDbCfg = _OramodDbCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1)
)
_OramodDbCfgTable_Object = MibTable
oramodDbCfgTable = _OramodDbCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1)
)
if mibBuilder.loadTexts:
    oramodDbCfgTable.setStatus("mandatory")
_OramodDbCfgEntry_Object = MibTableRow
oramodDbCfgEntry = _OramodDbCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1)
)
oramodDbCfgEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodDbCfgSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodDbCfgEntry.setStatus("mandatory")


class _OramodDbCfgSIDINDX_Type(Integer32):
    """Custom type oramodDbCfgSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgSIDINDX_Type.__name__ = "Integer32"
_OramodDbCfgSIDINDX_Object = MibTableColumn
oramodDbCfgSIDINDX = _OramodDbCfgSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 1),
    _OramodDbCfgSIDINDX_Type()
)
oramodDbCfgSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgSIDINDX.setStatus("mandatory")
_OramodDbCfgSID_Type = DisplayString
_OramodDbCfgSID_Object = MibTableColumn
oramodDbCfgSID = _OramodDbCfgSID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 2),
    _OramodDbCfgSID_Type()
)
oramodDbCfgSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgSID.setStatus("mandatory")
_OramodDbCfgVERSION_Type = DisplayString
_OramodDbCfgVERSION_Object = MibTableColumn
oramodDbCfgVERSION = _OramodDbCfgVERSION_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 3),
    _OramodDbCfgVERSION_Type()
)
oramodDbCfgVERSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgVERSION.setStatus("mandatory")
_OramodDbCfgHOME_Type = DisplayString
_OramodDbCfgHOME_Object = MibTableColumn
oramodDbCfgHOME = _OramodDbCfgHOME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 4),
    _OramodDbCfgHOME_Type()
)
oramodDbCfgHOME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgHOME.setStatus("mandatory")
_OramodDbCfgBASE_Type = DisplayString
_OramodDbCfgBASE_Object = MibTableColumn
oramodDbCfgBASE = _OramodDbCfgBASE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 5),
    _OramodDbCfgBASE_Type()
)
oramodDbCfgBASE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgBASE.setStatus("mandatory")
_OramodDbCfgID_Type = Integer32
_OramodDbCfgID_Object = MibTableColumn
oramodDbCfgID = _OramodDbCfgID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 6),
    _OramodDbCfgID_Type()
)
oramodDbCfgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgID.setStatus("mandatory")
_OramodDbCfgCRTDT_Type = DisplayString
_OramodDbCfgCRTDT_Object = MibTableColumn
oramodDbCfgCRTDT = _OramodDbCfgCRTDT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 7),
    _OramodDbCfgCRTDT_Type()
)
oramodDbCfgCRTDT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgCRTDT.setStatus("mandatory")
_OramodDbCfgLOGMODE_Type = DisplayString
_OramodDbCfgLOGMODE_Object = MibTableColumn
oramodDbCfgLOGMODE = _OramodDbCfgLOGMODE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 8),
    _OramodDbCfgLOGMODE_Type()
)
oramodDbCfgLOGMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgLOGMODE.setStatus("mandatory")
_OramodDbCfgCTRLFILETYPE_Type = DisplayString
_OramodDbCfgCTRLFILETYPE_Object = MibTableColumn
oramodDbCfgCTRLFILETYPE = _OramodDbCfgCTRLFILETYPE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 9),
    _OramodDbCfgCTRLFILETYPE_Type()
)
oramodDbCfgCTRLFILETYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgCTRLFILETYPE.setStatus("mandatory")
_OramodDbCfgOPENMODE_Type = DisplayString
_OramodDbCfgOPENMODE_Object = MibTableColumn
oramodDbCfgOPENMODE = _OramodDbCfgOPENMODE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 10),
    _OramodDbCfgOPENMODE_Type()
)
oramodDbCfgOPENMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgOPENMODE.setStatus("mandatory")


class _OramodDbCfgMAXPROCESS_Type(Integer32):
    """Custom type oramodDbCfgMAXPROCESS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgMAXPROCESS_Type.__name__ = "Integer32"
_OramodDbCfgMAXPROCESS_Object = MibTableColumn
oramodDbCfgMAXPROCESS = _OramodDbCfgMAXPROCESS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 11),
    _OramodDbCfgMAXPROCESS_Type()
)
oramodDbCfgMAXPROCESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgMAXPROCESS.setStatus("mandatory")


class _OramodDbCfgMAXSESSION_Type(Integer32):
    """Custom type oramodDbCfgMAXSESSION based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgMAXSESSION_Type.__name__ = "Integer32"
_OramodDbCfgMAXSESSION_Object = MibTableColumn
oramodDbCfgMAXSESSION = _OramodDbCfgMAXSESSION_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 12),
    _OramodDbCfgMAXSESSION_Type()
)
oramodDbCfgMAXSESSION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgMAXSESSION.setStatus("mandatory")
_OramodDbCfgTIMEDSTATISTICS_Type = DisplayString
_OramodDbCfgTIMEDSTATISTICS_Object = MibTableColumn
oramodDbCfgTIMEDSTATISTICS = _OramodDbCfgTIMEDSTATISTICS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 13),
    _OramodDbCfgTIMEDSTATISTICS_Type()
)
oramodDbCfgTIMEDSTATISTICS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgTIMEDSTATISTICS.setStatus("mandatory")


class _OramodDbCfgCPUCNT_Type(Integer32):
    """Custom type oramodDbCfgCPUCNT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgCPUCNT_Type.__name__ = "Integer32"
_OramodDbCfgCPUCNT_Object = MibTableColumn
oramodDbCfgCPUCNT = _OramodDbCfgCPUCNT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 14),
    _OramodDbCfgCPUCNT_Type()
)
oramodDbCfgCPUCNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgCPUCNT.setStatus("mandatory")


class _OramodDbCfgSHAREDPOOLSIZE_Type(Integer32):
    """Custom type oramodDbCfgSHAREDPOOLSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgSHAREDPOOLSIZE_Type.__name__ = "Integer32"
_OramodDbCfgSHAREDPOOLSIZE_Object = MibTableColumn
oramodDbCfgSHAREDPOOLSIZE = _OramodDbCfgSHAREDPOOLSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 15),
    _OramodDbCfgSHAREDPOOLSIZE_Type()
)
oramodDbCfgSHAREDPOOLSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgSHAREDPOOLSIZE.setStatus("mandatory")


class _OramodDbCfgSHAREDPOOLRSSIZE_Type(Integer32):
    """Custom type oramodDbCfgSHAREDPOOLRSSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgSHAREDPOOLRSSIZE_Type.__name__ = "Integer32"
_OramodDbCfgSHAREDPOOLRSSIZE_Object = MibTableColumn
oramodDbCfgSHAREDPOOLRSSIZE = _OramodDbCfgSHAREDPOOLRSSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 16),
    _OramodDbCfgSHAREDPOOLRSSIZE_Type()
)
oramodDbCfgSHAREDPOOLRSSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgSHAREDPOOLRSSIZE.setStatus("mandatory")


class _OramodDbCfgLARGEPOOLSIZE_Type(Integer32):
    """Custom type oramodDbCfgLARGEPOOLSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgLARGEPOOLSIZE_Type.__name__ = "Integer32"
_OramodDbCfgLARGEPOOLSIZE_Object = MibTableColumn
oramodDbCfgLARGEPOOLSIZE = _OramodDbCfgLARGEPOOLSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 17),
    _OramodDbCfgLARGEPOOLSIZE_Type()
)
oramodDbCfgLARGEPOOLSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgLARGEPOOLSIZE.setStatus("mandatory")


class _OramodDbCfgJAVAPOOLSIZE_Type(Integer32):
    """Custom type oramodDbCfgJAVAPOOLSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgJAVAPOOLSIZE_Type.__name__ = "Integer32"
_OramodDbCfgJAVAPOOLSIZE_Object = MibTableColumn
oramodDbCfgJAVAPOOLSIZE = _OramodDbCfgJAVAPOOLSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 18),
    _OramodDbCfgJAVAPOOLSIZE_Type()
)
oramodDbCfgJAVAPOOLSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgJAVAPOOLSIZE.setStatus("mandatory")
_OramodDbCfgCNTRLFILES_Type = DisplayString
_OramodDbCfgCNTRLFILES_Object = MibTableColumn
oramodDbCfgCNTRLFILES = _OramodDbCfgCNTRLFILES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 19),
    _OramodDbCfgCNTRLFILES_Type()
)
oramodDbCfgCNTRLFILES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgCNTRLFILES.setStatus("mandatory")


class _OramodDbCfgDBBLKBUFF_Type(Integer32):
    """Custom type oramodDbCfgDBBLKBUFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgDBBLKBUFF_Type.__name__ = "Integer32"
_OramodDbCfgDBBLKBUFF_Object = MibTableColumn
oramodDbCfgDBBLKBUFF = _OramodDbCfgDBBLKBUFF_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 20),
    _OramodDbCfgDBBLKBUFF_Type()
)
oramodDbCfgDBBLKBUFF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgDBBLKBUFF.setStatus("mandatory")


class _OramodDbCfgDBBLKSIZE_Type(Integer32):
    """Custom type oramodDbCfgDBBLKSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 8192),
    )


_OramodDbCfgDBBLKSIZE_Type.__name__ = "Integer32"
_OramodDbCfgDBBLKSIZE_Object = MibTableColumn
oramodDbCfgDBBLKSIZE = _OramodDbCfgDBBLKSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 21),
    _OramodDbCfgDBBLKSIZE_Type()
)
oramodDbCfgDBBLKSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgDBBLKSIZE.setStatus("mandatory")


class _OramodDbCfgCKPTINTRVL_Type(Integer32):
    """Custom type oramodDbCfgCKPTINTRVL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgCKPTINTRVL_Type.__name__ = "Integer32"
_OramodDbCfgCKPTINTRVL_Object = MibTableColumn
oramodDbCfgCKPTINTRVL = _OramodDbCfgCKPTINTRVL_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 22),
    _OramodDbCfgCKPTINTRVL_Type()
)
oramodDbCfgCKPTINTRVL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgCKPTINTRVL.setStatus("mandatory")


class _OramodDbCfgDBFILES_Type(Integer32):
    """Custom type oramodDbCfgDBFILES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgDBFILES_Type.__name__ = "Integer32"
_OramodDbCfgDBFILES_Object = MibTableColumn
oramodDbCfgDBFILES = _OramodDbCfgDBFILES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 23),
    _OramodDbCfgDBFILES_Type()
)
oramodDbCfgDBFILES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgDBFILES.setStatus("mandatory")


class _OramodDbCfgSORTAREASIZE_Type(Integer32):
    """Custom type oramodDbCfgSORTAREASIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgSORTAREASIZE_Type.__name__ = "Integer32"
_OramodDbCfgSORTAREASIZE_Object = MibTableColumn
oramodDbCfgSORTAREASIZE = _OramodDbCfgSORTAREASIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 24),
    _OramodDbCfgSORTAREASIZE_Type()
)
oramodDbCfgSORTAREASIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgSORTAREASIZE.setStatus("mandatory")


class _OramodDbCfgOPENCURSORS_Type(Integer32):
    """Custom type oramodDbCfgOPENCURSORS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgOPENCURSORS_Type.__name__ = "Integer32"
_OramodDbCfgOPENCURSORS_Object = MibTableColumn
oramodDbCfgOPENCURSORS = _OramodDbCfgOPENCURSORS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 25),
    _OramodDbCfgOPENCURSORS_Type()
)
oramodDbCfgOPENCURSORS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgOPENCURSORS.setStatus("mandatory")


class _OramodDbCfgTRNSACTNS_Type(Integer32):
    """Custom type oramodDbCfgTRNSACTNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgTRNSACTNS_Type.__name__ = "Integer32"
_OramodDbCfgTRNSACTNS_Object = MibTableColumn
oramodDbCfgTRNSACTNS = _OramodDbCfgTRNSACTNS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 26),
    _OramodDbCfgTRNSACTNS_Type()
)
oramodDbCfgTRNSACTNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgTRNSACTNS.setStatus("mandatory")


class _OramodDbCfgTRNSACTNSPERSEG_Type(Integer32):
    """Custom type oramodDbCfgTRNSACTNSPERSEG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodDbCfgTRNSACTNSPERSEG_Type.__name__ = "Integer32"
_OramodDbCfgTRNSACTNSPERSEG_Object = MibTableColumn
oramodDbCfgTRNSACTNSPERSEG = _OramodDbCfgTRNSACTNSPERSEG_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 27),
    _OramodDbCfgTRNSACTNSPERSEG_Type()
)
oramodDbCfgTRNSACTNSPERSEG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgTRNSACTNSPERSEG.setStatus("mandatory")


class _OramodDbCfgMAXROLLSEG_Type(Integer32):
    """Custom type oramodDbCfgMAXROLLSEG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_OramodDbCfgMAXROLLSEG_Type.__name__ = "Integer32"
_OramodDbCfgMAXROLLSEG_Object = MibTableColumn
oramodDbCfgMAXROLLSEG = _OramodDbCfgMAXROLLSEG_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 1, 1, 1, 28),
    _OramodDbCfgMAXROLLSEG_Type()
)
oramodDbCfgMAXROLLSEG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodDbCfgMAXROLLSEG.setStatus("mandatory")
_OramodCfgDf_ObjectIdentity = ObjectIdentity
oramodCfgDf = _OramodCfgDf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2)
)
_OramodCfgDfTable_Object = MibTable
oramodCfgDfTable = _OramodCfgDfTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1)
)
if mibBuilder.loadTexts:
    oramodCfgDfTable.setStatus("mandatory")
_OramodCfgDfEntry_Object = MibTableRow
oramodCfgDfEntry = _OramodCfgDfEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1)
)
oramodCfgDfEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodCfgDfSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodCfgDfFILENUM"),
)
if mibBuilder.loadTexts:
    oramodCfgDfEntry.setStatus("mandatory")


class _OramodCfgDfSIDINDX_Type(Integer32):
    """Custom type oramodCfgDfSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfSIDINDX_Type.__name__ = "Integer32"
_OramodCfgDfSIDINDX_Object = MibTableColumn
oramodCfgDfSIDINDX = _OramodCfgDfSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 1),
    _OramodCfgDfSIDINDX_Type()
)
oramodCfgDfSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfSIDINDX.setStatus("mandatory")
_OramodCfgDfFILENUM_Type = Integer32
_OramodCfgDfFILENUM_Object = MibTableColumn
oramodCfgDfFILENUM = _OramodCfgDfFILENUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 2),
    _OramodCfgDfFILENUM_Type()
)
oramodCfgDfFILENUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfFILENUM.setStatus("mandatory")
_OramodCfgDfSTATUS_Type = DisplayString
_OramodCfgDfSTATUS_Object = MibTableColumn
oramodCfgDfSTATUS = _OramodCfgDfSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 3),
    _OramodCfgDfSTATUS_Type()
)
oramodCfgDfSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfSTATUS.setStatus("mandatory")
_OramodCfgDfENABLED_Type = DisplayString
_OramodCfgDfENABLED_Object = MibTableColumn
oramodCfgDfENABLED = _OramodCfgDfENABLED_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 4),
    _OramodCfgDfENABLED_Type()
)
oramodCfgDfENABLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfENABLED.setStatus("mandatory")


class _OramodCfgDfUNRCVRBLECHG_Type(Integer32):
    """Custom type oramodCfgDfUNRCVRBLECHG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfUNRCVRBLECHG_Type.__name__ = "Integer32"
_OramodCfgDfUNRCVRBLECHG_Object = MibTableColumn
oramodCfgDfUNRCVRBLECHG = _OramodCfgDfUNRCVRBLECHG_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 5),
    _OramodCfgDfUNRCVRBLECHG_Type()
)
oramodCfgDfUNRCVRBLECHG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfUNRCVRBLECHG.setStatus("mandatory")


class _OramodCfgDfUNRCVRBLETIME_Type(Integer32):
    """Custom type oramodCfgDfUNRCVRBLETIME based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfUNRCVRBLETIME_Type.__name__ = "Integer32"
_OramodCfgDfUNRCVRBLETIME_Object = MibTableColumn
oramodCfgDfUNRCVRBLETIME = _OramodCfgDfUNRCVRBLETIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 6),
    _OramodCfgDfUNRCVRBLETIME_Type()
)
oramodCfgDfUNRCVRBLETIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfUNRCVRBLETIME.setStatus("mandatory")


class _OramodCfgDfKBYTES_Type(Integer32):
    """Custom type oramodCfgDfKBYTES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfKBYTES_Type.__name__ = "Integer32"
_OramodCfgDfKBYTES_Object = MibTableColumn
oramodCfgDfKBYTES = _OramodCfgDfKBYTES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 7),
    _OramodCfgDfKBYTES_Type()
)
oramodCfgDfKBYTES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfKBYTES.setStatus("mandatory")


class _OramodCfgDfCRTKBYTES_Type(Integer32):
    """Custom type oramodCfgDfCRTKBYTES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfCRTKBYTES_Type.__name__ = "Integer32"
_OramodCfgDfCRTKBYTES_Object = MibTableColumn
oramodCfgDfCRTKBYTES = _OramodCfgDfCRTKBYTES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 8),
    _OramodCfgDfCRTKBYTES_Type()
)
oramodCfgDfCRTKBYTES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfCRTKBYTES.setStatus("mandatory")
_OramodCfgDfFNAME_Type = DisplayString
_OramodCfgDfFNAME_Object = MibTableColumn
oramodCfgDfFNAME = _OramodCfgDfFNAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 9),
    _OramodCfgDfFNAME_Type()
)
oramodCfgDfFNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfFNAME.setStatus("mandatory")
_OramodCfgDfCRTTIME_Type = DisplayString
_OramodCfgDfCRTTIME_Object = MibTableColumn
oramodCfgDfCRTTIME = _OramodCfgDfCRTTIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 10),
    _OramodCfgDfCRTTIME_Type()
)
oramodCfgDfCRTTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfCRTTIME.setStatus("mandatory")


class _OramodCfgDfTBLESPACENUM_Type(Integer32):
    """Custom type oramodCfgDfTBLESPACENUM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfTBLESPACENUM_Type.__name__ = "Integer32"
_OramodCfgDfTBLESPACENUM_Object = MibTableColumn
oramodCfgDfTBLESPACENUM = _OramodCfgDfTBLESPACENUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 11),
    _OramodCfgDfTBLESPACENUM_Type()
)
oramodCfgDfTBLESPACENUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfTBLESPACENUM.setStatus("mandatory")


class _OramodCfgDfTBLESPACERFILENUM_Type(Integer32):
    """Custom type oramodCfgDfTBLESPACERFILENUM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgDfTBLESPACERFILENUM_Type.__name__ = "Integer32"
_OramodCfgDfTBLESPACERFILENUM_Object = MibTableColumn
oramodCfgDfTBLESPACERFILENUM = _OramodCfgDfTBLESPACERFILENUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 12),
    _OramodCfgDfTBLESPACERFILENUM_Type()
)
oramodCfgDfTBLESPACERFILENUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfTBLESPACERFILENUM.setStatus("mandatory")


class _OramodCfgDfBLOCKS_Type(Integer32):
    """Custom type oramodCfgDfBLOCKS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OramodCfgDfBLOCKS_Type.__name__ = "Integer32"
_OramodCfgDfBLOCKS_Object = MibTableColumn
oramodCfgDfBLOCKS = _OramodCfgDfBLOCKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 13),
    _OramodCfgDfBLOCKS_Type()
)
oramodCfgDfBLOCKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfBLOCKS.setStatus("mandatory")


class _OramodCfgDfBLOCKSIZE_Type(Integer32):
    """Custom type oramodCfgDfBLOCKSIZE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OramodCfgDfBLOCKSIZE_Type.__name__ = "Integer32"
_OramodCfgDfBLOCKSIZE_Object = MibTableColumn
oramodCfgDfBLOCKSIZE = _OramodCfgDfBLOCKSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 14),
    _OramodCfgDfBLOCKSIZE_Type()
)
oramodCfgDfBLOCKSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfBLOCKSIZE.setStatus("mandatory")


class _OramodCfgDfERROR_Type(Integer32):
    """Custom type oramodCfgDfERROR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OramodCfgDfERROR_Type.__name__ = "Integer32"
_OramodCfgDfERROR_Object = MibTableColumn
oramodCfgDfERROR = _OramodCfgDfERROR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 15),
    _OramodCfgDfERROR_Type()
)
oramodCfgDfERROR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfERROR.setStatus("mandatory")
_OramodCfgDfRECOVER_Type = DisplayString
_OramodCfgDfRECOVER_Object = MibTableColumn
oramodCfgDfRECOVER = _OramodCfgDfRECOVER_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 16),
    _OramodCfgDfRECOVER_Type()
)
oramodCfgDfRECOVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfRECOVER.setStatus("mandatory")


class _OramodCfgDfRSTLOGSCHGNUM_Type(Integer32):
    """Custom type oramodCfgDfRSTLOGSCHGNUM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OramodCfgDfRSTLOGSCHGNUM_Type.__name__ = "Integer32"
_OramodCfgDfRSTLOGSCHGNUM_Object = MibTableColumn
oramodCfgDfRSTLOGSCHGNUM = _OramodCfgDfRSTLOGSCHGNUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 17),
    _OramodCfgDfRSTLOGSCHGNUM_Type()
)
oramodCfgDfRSTLOGSCHGNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfRSTLOGSCHGNUM.setStatus("mandatory")
_OramodCfgDfRSTLOGSTIME_Type = DisplayString
_OramodCfgDfRSTLOGSTIME_Object = MibTableColumn
oramodCfgDfRSTLOGSTIME = _OramodCfgDfRSTLOGSTIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 2, 1, 1, 18),
    _OramodCfgDfRSTLOGSTIME_Type()
)
oramodCfgDfRSTLOGSTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgDfRSTLOGSTIME.setStatus("mandatory")
_OramodCfgLf_ObjectIdentity = ObjectIdentity
oramodCfgLf = _OramodCfgLf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3)
)
_OramodCfgLfTable_Object = MibTable
oramodCfgLfTable = _OramodCfgLfTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1)
)
if mibBuilder.loadTexts:
    oramodCfgLfTable.setStatus("mandatory")
_OramodCfgLfEntry_Object = MibTableRow
oramodCfgLfEntry = _OramodCfgLfEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1)
)
oramodCfgLfEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodCfgLfSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodCfgLfMEMBERINDX"),
)
if mibBuilder.loadTexts:
    oramodCfgLfEntry.setStatus("mandatory")


class _OramodCfgLfSIDINDX_Type(Integer32):
    """Custom type oramodCfgLfSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgLfSIDINDX_Type.__name__ = "Integer32"
_OramodCfgLfSIDINDX_Object = MibTableColumn
oramodCfgLfSIDINDX = _OramodCfgLfSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1, 1),
    _OramodCfgLfSIDINDX_Type()
)
oramodCfgLfSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgLfSIDINDX.setStatus("mandatory")


class _OramodCfgLfMEMBERINDX_Type(Integer32):
    """Custom type oramodCfgLfMEMBERINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147482647),
    )


_OramodCfgLfMEMBERINDX_Type.__name__ = "Integer32"
_OramodCfgLfMEMBERINDX_Object = MibTableColumn
oramodCfgLfMEMBERINDX = _OramodCfgLfMEMBERINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1, 2),
    _OramodCfgLfMEMBERINDX_Type()
)
oramodCfgLfMEMBERINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgLfMEMBERINDX.setStatus("mandatory")


class _OramodCfgLfGROUPNUM_Type(Integer32):
    """Custom type oramodCfgLfGROUPNUM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147482647),
    )


_OramodCfgLfGROUPNUM_Type.__name__ = "Integer32"
_OramodCfgLfGROUPNUM_Object = MibTableColumn
oramodCfgLfGROUPNUM = _OramodCfgLfGROUPNUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1, 3),
    _OramodCfgLfGROUPNUM_Type()
)
oramodCfgLfGROUPNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgLfGROUPNUM.setStatus("mandatory")
_OramodCfgLfSTATUS_Type = DisplayString
_OramodCfgLfSTATUS_Object = MibTableColumn
oramodCfgLfSTATUS = _OramodCfgLfSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1, 4),
    _OramodCfgLfSTATUS_Type()
)
oramodCfgLfSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgLfSTATUS.setStatus("mandatory")
_OramodCfgLfMEMBER_Type = DisplayString
_OramodCfgLfMEMBER_Object = MibTableColumn
oramodCfgLfMEMBER = _OramodCfgLfMEMBER_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 3, 1, 1, 5),
    _OramodCfgLfMEMBER_Type()
)
oramodCfgLfMEMBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgLfMEMBER.setStatus("mandatory")
_OramodCfgSga_ObjectIdentity = ObjectIdentity
oramodCfgSga = _OramodCfgSga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4)
)
_OramodCfgSgaTable_Object = MibTable
oramodCfgSgaTable = _OramodCfgSgaTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1)
)
if mibBuilder.loadTexts:
    oramodCfgSgaTable.setStatus("mandatory")
_OramodCfgSgaEntry_Object = MibTableRow
oramodCfgSgaEntry = _OramodCfgSgaEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1)
)
oramodCfgSgaEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodCfgSgaSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodCfgSgaEntry.setStatus("mandatory")


class _OramodCfgSgaSIDINDX_Type(Integer32):
    """Custom type oramodCfgSgaSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgSgaSIDINDX_Type.__name__ = "Integer32"
_OramodCfgSgaSIDINDX_Object = MibTableColumn
oramodCfgSgaSIDINDX = _OramodCfgSgaSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 1),
    _OramodCfgSgaSIDINDX_Type()
)
oramodCfgSgaSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaSIDINDX.setStatus("mandatory")


class _OramodCfgSgaTOTALMEMALLOC_Type(Integer32):
    """Custom type oramodCfgSgaTOTALMEMALLOC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147482647),
    )


_OramodCfgSgaTOTALMEMALLOC_Type.__name__ = "Integer32"
_OramodCfgSgaTOTALMEMALLOC_Object = MibTableColumn
oramodCfgSgaTOTALMEMALLOC = _OramodCfgSgaTOTALMEMALLOC_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 2),
    _OramodCfgSgaTOTALMEMALLOC_Type()
)
oramodCfgSgaTOTALMEMALLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaTOTALMEMALLOC.setStatus("mandatory")


class _OramodCfgSgaFIXEDSGA_Type(Integer32):
    """Custom type oramodCfgSgaFIXEDSGA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgSgaFIXEDSGA_Type.__name__ = "Integer32"
_OramodCfgSgaFIXEDSGA_Object = MibTableColumn
oramodCfgSgaFIXEDSGA = _OramodCfgSgaFIXEDSGA_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 3),
    _OramodCfgSgaFIXEDSGA_Type()
)
oramodCfgSgaFIXEDSGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaFIXEDSGA.setStatus("mandatory")


class _OramodCfgSgaVARIABLE_Type(Integer32):
    """Custom type oramodCfgSgaVARIABLE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgSgaVARIABLE_Type.__name__ = "Integer32"
_OramodCfgSgaVARIABLE_Object = MibTableColumn
oramodCfgSgaVARIABLE = _OramodCfgSgaVARIABLE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 4),
    _OramodCfgSgaVARIABLE_Type()
)
oramodCfgSgaVARIABLE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaVARIABLE.setStatus("mandatory")


class _OramodCfgSgaDBBUFF_Type(Integer32):
    """Custom type oramodCfgSgaDBBUFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgSgaDBBUFF_Type.__name__ = "Integer32"
_OramodCfgSgaDBBUFF_Object = MibTableColumn
oramodCfgSgaDBBUFF = _OramodCfgSgaDBBUFF_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 5),
    _OramodCfgSgaDBBUFF_Type()
)
oramodCfgSgaDBBUFF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaDBBUFF.setStatus("mandatory")


class _OramodCfgSgaREDOBUFF_Type(Integer32):
    """Custom type oramodCfgSgaREDOBUFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodCfgSgaREDOBUFF_Type.__name__ = "Integer32"
_OramodCfgSgaREDOBUFF_Object = MibTableColumn
oramodCfgSgaREDOBUFF = _OramodCfgSgaREDOBUFF_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 10, 4, 1, 1, 6),
    _OramodCfgSgaREDOBUFF_Type()
)
oramodCfgSgaREDOBUFF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodCfgSgaREDOBUFF.setStatus("mandatory")
_OramodPerf_ObjectIdentity = ObjectIdentity
oramodPerf = _OramodPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11)
)
_OramodFootprint_ObjectIdentity = ObjectIdentity
oramodFootprint = _OramodFootprint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1)
)
_OramodFootprt_ObjectIdentity = ObjectIdentity
oramodFootprt = _OramodFootprt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1)
)
_OramodFootprtTable_Object = MibTable
oramodFootprtTable = _OramodFootprtTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oramodFootprtTable.setStatus("mandatory")
_OramodFootprtEntry_Object = MibTableRow
oramodFootprtEntry = _OramodFootprtEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1)
)
oramodFootprtEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodFootprtSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodFootprtEntry.setStatus("mandatory")


class _OramodFootprtSIDINDX_Type(Integer32):
    """Custom type oramodFootprtSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodFootprtSIDINDX_Type.__name__ = "Integer32"
_OramodFootprtSIDINDX_Object = MibTableColumn
oramodFootprtSIDINDX = _OramodFootprtSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 1),
    _OramodFootprtSIDINDX_Type()
)
oramodFootprtSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtSIDINDX.setStatus("mandatory")
_OramodFootprtCPUTIME_Type = Integer32
_OramodFootprtCPUTIME_Object = MibTableColumn
oramodFootprtCPUTIME = _OramodFootprtCPUTIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 2),
    _OramodFootprtCPUTIME_Type()
)
oramodFootprtCPUTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtCPUTIME.setStatus("mandatory")


class _OramodFootprtPERCENTCPU_Type(Integer32):
    """Custom type oramodFootprtPERCENTCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OramodFootprtPERCENTCPU_Type.__name__ = "Integer32"
_OramodFootprtPERCENTCPU_Object = MibTableColumn
oramodFootprtPERCENTCPU = _OramodFootprtPERCENTCPU_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 3),
    _OramodFootprtPERCENTCPU_Type()
)
oramodFootprtPERCENTCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtPERCENTCPU.setStatus("mandatory")
_OramodFootprtMEMSIZE_Type = Gauge32
_OramodFootprtMEMSIZE_Object = MibTableColumn
oramodFootprtMEMSIZE = _OramodFootprtMEMSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 4),
    _OramodFootprtMEMSIZE_Type()
)
oramodFootprtMEMSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtMEMSIZE.setStatus("mandatory")
_OramodFootprtRSS_Type = Gauge32
_OramodFootprtRSS_Object = MibTableColumn
oramodFootprtRSS = _OramodFootprtRSS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 5),
    _OramodFootprtRSS_Type()
)
oramodFootprtRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtRSS.setStatus("mandatory")


class _OramodFootprtPERCENTMEM_Type(Integer32):
    """Custom type oramodFootprtPERCENTMEM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OramodFootprtPERCENTMEM_Type.__name__ = "Integer32"
_OramodFootprtPERCENTMEM_Object = MibTableColumn
oramodFootprtPERCENTMEM = _OramodFootprtPERCENTMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 6),
    _OramodFootprtPERCENTMEM_Type()
)
oramodFootprtPERCENTMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtPERCENTMEM.setStatus("mandatory")
_OramodFootprtTHREADS_Type = Gauge32
_OramodFootprtTHREADS_Object = MibTableColumn
oramodFootprtTHREADS = _OramodFootprtTHREADS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 7),
    _OramodFootprtTHREADS_Type()
)
oramodFootprtTHREADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtTHREADS.setStatus("mandatory")
_OramodFootprtINBLKS_Type = Gauge32
_OramodFootprtINBLKS_Object = MibTableColumn
oramodFootprtINBLKS = _OramodFootprtINBLKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 8),
    _OramodFootprtINBLKS_Type()
)
oramodFootprtINBLKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtINBLKS.setStatus("mandatory")
_OramodFootprtOUTBLKS_Type = Gauge32
_OramodFootprtOUTBLKS_Object = MibTableColumn
oramodFootprtOUTBLKS = _OramodFootprtOUTBLKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 9),
    _OramodFootprtOUTBLKS_Type()
)
oramodFootprtOUTBLKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtOUTBLKS.setStatus("mandatory")
_OramodFootprtMSGSSENT_Type = Counter32
_OramodFootprtMSGSSENT_Object = MibTableColumn
oramodFootprtMSGSSENT = _OramodFootprtMSGSSENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 10),
    _OramodFootprtMSGSSENT_Type()
)
oramodFootprtMSGSSENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtMSGSSENT.setStatus("mandatory")
_OramodFootprtMSGSRCVD_Type = Counter32
_OramodFootprtMSGSRCVD_Object = MibTableColumn
oramodFootprtMSGSRCVD = _OramodFootprtMSGSRCVD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 11),
    _OramodFootprtMSGSRCVD_Type()
)
oramodFootprtMSGSRCVD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtMSGSRCVD.setStatus("mandatory")
_OramodFootprtSYSCALLS_Type = Counter32
_OramodFootprtSYSCALLS_Object = MibTableColumn
oramodFootprtSYSCALLS = _OramodFootprtSYSCALLS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 12),
    _OramodFootprtSYSCALLS_Type()
)
oramodFootprtSYSCALLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtSYSCALLS.setStatus("mandatory")
_OramodFootprtMINORPGFLTS_Type = Counter32
_OramodFootprtMINORPGFLTS_Object = MibTableColumn
oramodFootprtMINORPGFLTS = _OramodFootprtMINORPGFLTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 13),
    _OramodFootprtMINORPGFLTS_Type()
)
oramodFootprtMINORPGFLTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtMINORPGFLTS.setStatus("mandatory")
_OramodFootprtMAJORPGFLTS_Type = Counter32
_OramodFootprtMAJORPGFLTS_Object = MibTableColumn
oramodFootprtMAJORPGFLTS = _OramodFootprtMAJORPGFLTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 14),
    _OramodFootprtMAJORPGFLTS_Type()
)
oramodFootprtMAJORPGFLTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtMAJORPGFLTS.setStatus("mandatory")
_OramodFootprtNUMSWAPS_Type = Counter32
_OramodFootprtNUMSWAPS_Object = MibTableColumn
oramodFootprtNUMSWAPS = _OramodFootprtNUMSWAPS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 15),
    _OramodFootprtNUMSWAPS_Type()
)
oramodFootprtNUMSWAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtNUMSWAPS.setStatus("mandatory")
_OramodFootprtVOLCNTX_Type = Counter32
_OramodFootprtVOLCNTX_Object = MibTableColumn
oramodFootprtVOLCNTX = _OramodFootprtVOLCNTX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 16),
    _OramodFootprtVOLCNTX_Type()
)
oramodFootprtVOLCNTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtVOLCNTX.setStatus("mandatory")
_OramodFootprtINVOLCNTX_Type = Counter32
_OramodFootprtINVOLCNTX_Object = MibTableColumn
oramodFootprtINVOLCNTX = _OramodFootprtINVOLCNTX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 17),
    _OramodFootprtINVOLCNTX_Type()
)
oramodFootprtINVOLCNTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtINVOLCNTX.setStatus("mandatory")
_OramodFootprtHOMESIZE_Type = Gauge32
_OramodFootprtHOMESIZE_Object = MibTableColumn
oramodFootprtHOMESIZE = _OramodFootprtHOMESIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 18),
    _OramodFootprtHOMESIZE_Type()
)
oramodFootprtHOMESIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtHOMESIZE.setStatus("mandatory")
_OramodFootprtDBDISKSIZE_Type = Gauge32
_OramodFootprtDBDISKSIZE_Object = MibTableColumn
oramodFootprtDBDISKSIZE = _OramodFootprtDBDISKSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 19),
    _OramodFootprtDBDISKSIZE_Type()
)
oramodFootprtDBDISKSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtDBDISKSIZE.setStatus("mandatory")
_OramodFootprtLASTUPDATE_Type = TimeTicks
_OramodFootprtLASTUPDATE_Object = MibTableColumn
oramodFootprtLASTUPDATE = _OramodFootprtLASTUPDATE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 1, 1, 1, 20),
    _OramodFootprtLASTUPDATE_Type()
)
oramodFootprtLASTUPDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFootprtLASTUPDATE.setStatus("mandatory")
_OramodFFootprt_ObjectIdentity = ObjectIdentity
oramodFFootprt = _OramodFFootprt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2)
)
_OramodFFootprtTable_Object = MibTable
oramodFFootprtTable = _OramodFFootprtTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oramodFFootprtTable.setStatus("mandatory")
_OramodFFootprtEntry_Object = MibTableRow
oramodFFootprtEntry = _OramodFFootprtEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1)
)
oramodFFootprtEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodFFootprtSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodFFootprtFILEINDX"),
)
if mibBuilder.loadTexts:
    oramodFFootprtEntry.setStatus("mandatory")


class _OramodFFootprtSIDINDX_Type(Integer32):
    """Custom type oramodFFootprtSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodFFootprtSIDINDX_Type.__name__ = "Integer32"
_OramodFFootprtSIDINDX_Object = MibTableColumn
oramodFFootprtSIDINDX = _OramodFFootprtSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 1),
    _OramodFFootprtSIDINDX_Type()
)
oramodFFootprtSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtSIDINDX.setStatus("mandatory")


class _OramodFFootprtFILEINDX_Type(Integer32):
    """Custom type oramodFFootprtFILEINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodFFootprtFILEINDX_Type.__name__ = "Integer32"
_OramodFFootprtFILEINDX_Object = MibTableColumn
oramodFFootprtFILEINDX = _OramodFFootprtFILEINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 2),
    _OramodFFootprtFILEINDX_Type()
)
oramodFFootprtFILEINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtFILEINDX.setStatus("mandatory")
_OramodFFootprtFILETYPE_Type = DisplayString
_OramodFFootprtFILETYPE_Object = MibTableColumn
oramodFFootprtFILETYPE = _OramodFFootprtFILETYPE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 3),
    _OramodFFootprtFILETYPE_Type()
)
oramodFFootprtFILETYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtFILETYPE.setStatus("mandatory")
_OramodFFootprtFILENAME_Type = DisplayString
_OramodFFootprtFILENAME_Object = MibTableColumn
oramodFFootprtFILENAME = _OramodFFootprtFILENAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 4),
    _OramodFFootprtFILENAME_Type()
)
oramodFFootprtFILENAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtFILENAME.setStatus("mandatory")
_OramodFFootprtCRTTS_Type = DisplayString
_OramodFFootprtCRTTS_Object = MibTableColumn
oramodFFootprtCRTTS = _OramodFFootprtCRTTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 5),
    _OramodFFootprtCRTTS_Type()
)
oramodFFootprtCRTTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtCRTTS.setStatus("mandatory")
_OramodFFootprtCRTKBYTES_Type = Integer32
_OramodFFootprtCRTKBYTES_Object = MibTableColumn
oramodFFootprtCRTKBYTES = _OramodFFootprtCRTKBYTES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 6),
    _OramodFFootprtCRTKBYTES_Type()
)
oramodFFootprtCRTKBYTES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtCRTKBYTES.setStatus("mandatory")
_OramodFFootprtKBYTES_Type = Integer32
_OramodFFootprtKBYTES_Object = MibTableColumn
oramodFFootprtKBYTES = _OramodFFootprtKBYTES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 7),
    _OramodFFootprtKBYTES_Type()
)
oramodFFootprtKBYTES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtKBYTES.setStatus("mandatory")
_OramodFFootprtBLOCKS_Type = Integer32
_OramodFFootprtBLOCKS_Object = MibTableColumn
oramodFFootprtBLOCKS = _OramodFFootprtBLOCKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 8),
    _OramodFFootprtBLOCKS_Type()
)
oramodFFootprtBLOCKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtBLOCKS.setStatus("mandatory")
_OramodFFootprtSTATUS_Type = DisplayString
_OramodFFootprtSTATUS_Object = MibTableColumn
oramodFFootprtSTATUS = _OramodFFootprtSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 9),
    _OramodFFootprtSTATUS_Type()
)
oramodFFootprtSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtSTATUS.setStatus("mandatory")
_OramodFFootprtRECOVER_Type = DisplayString
_OramodFFootprtRECOVER_Object = MibTableColumn
oramodFFootprtRECOVER = _OramodFFootprtRECOVER_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 10),
    _OramodFFootprtRECOVER_Type()
)
oramodFFootprtRECOVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtRECOVER.setStatus("mandatory")
_OramodFFootprtAVGIOTIM_Type = DisplayString
_OramodFFootprtAVGIOTIM_Object = MibTableColumn
oramodFFootprtAVGIOTIM = _OramodFFootprtAVGIOTIM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 1, 2, 1, 1, 11),
    _OramodFFootprtAVGIOTIM_Type()
)
oramodFFootprtAVGIOTIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodFFootprtAVGIOTIM.setStatus("mandatory")
_OramodMetrics_ObjectIdentity = ObjectIdentity
oramodMetrics = _OramodMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2)
)
_OramodMetricsTable_Object = MibTable
oramodMetricsTable = _OramodMetricsTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1)
)
if mibBuilder.loadTexts:
    oramodMetricsTable.setStatus("mandatory")
_OramodMetricsEntry_Object = MibTableRow
oramodMetricsEntry = _OramodMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1)
)
oramodMetricsEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodMetricsSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodMetricsEntry.setStatus("mandatory")


class _OramodMetricsSIDINDX_Type(Integer32):
    """Custom type oramodMetricsSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodMetricsSIDINDX_Type.__name__ = "Integer32"
_OramodMetricsSIDINDX_Object = MibTableColumn
oramodMetricsSIDINDX = _OramodMetricsSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 1),
    _OramodMetricsSIDINDX_Type()
)
oramodMetricsSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSIDINDX.setStatus("mandatory")
_OramodMetricsBCPT_Type = Gauge32
_OramodMetricsBCPT_Object = MibTableColumn
oramodMetricsBCPT = _OramodMetricsBCPT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 2),
    _OramodMetricsBCPT_Type()
)
oramodMetricsBCPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsBCPT.setStatus("mandatory")
_OramodMetricsBGR_Type = Gauge32
_OramodMetricsBGR_Object = MibTableColumn
oramodMetricsBGR = _OramodMetricsBGR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 3),
    _OramodMetricsBGR_Type()
)
oramodMetricsBGR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsBGR.setStatus("mandatory")
_OramodMetricsBVPT_Type = Gauge32
_OramodMetricsBVPT_Object = MibTableColumn
oramodMetricsBVPT = _OramodMetricsBVPT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 4),
    _OramodMetricsBVPT_Type()
)
oramodMetricsBVPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsBVPT.setStatus("mandatory")
_OramodMetricsCHR_Type = Gauge32
_OramodMetricsCHR_Object = MibTableColumn
oramodMetricsCHR = _OramodMetricsCHR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 5),
    _OramodMetricsCHR_Type()
)
oramodMetricsCHR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCHR.setStatus("mandatory")
_OramodMetricsCR_Type = Gauge32
_OramodMetricsCR_Object = MibTableColumn
oramodMetricsCR = _OramodMetricsCR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 6),
    _OramodMetricsCR_Type()
)
oramodMetricsCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCR.setStatus("mandatory")
_OramodMetricsCPT_Type = Gauge32
_OramodMetricsCPT_Object = MibTableColumn
oramodMetricsCPT = _OramodMetricsCPT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 7),
    _OramodMetricsCPT_Type()
)
oramodMetricsCPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCPT.setStatus("mandatory")
_OramodMetricsCBR_Type = Gauge32
_OramodMetricsCBR_Object = MibTableColumn
oramodMetricsCBR = _OramodMetricsCBR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 8),
    _OramodMetricsCBR_Type()
)
oramodMetricsCBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCBR.setStatus("mandatory")
_OramodMetricsCCR_Type = Gauge32
_OramodMetricsCCR_Object = MibTableColumn
oramodMetricsCCR = _OramodMetricsCCR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 9),
    _OramodMetricsCCR_Type()
)
oramodMetricsCCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCCR.setStatus("mandatory")
_OramodMetricsCRR_Type = Gauge32
_OramodMetricsCRR_Object = MibTableColumn
oramodMetricsCRR = _OramodMetricsCRR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 10),
    _OramodMetricsCRR_Type()
)
oramodMetricsCRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCRR.setStatus("mandatory")
_OramodMetricsLCM_Type = Gauge32
_OramodMetricsLCM_Object = MibTableColumn
oramodMetricsLCM = _OramodMetricsLCM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 11),
    _OramodMetricsLCM_Type()
)
oramodMetricsLCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsLCM.setStatus("mandatory")
_OramodMetricsRTUC_Type = Gauge32
_OramodMetricsRTUC_Object = MibTableColumn
oramodMetricsRTUC = _OramodMetricsRTUC_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 12),
    _OramodMetricsRTUC_Type()
)
oramodMetricsRTUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsRTUC.setStatus("mandatory")
_OramodMetricsRLSW_Type = Gauge32
_OramodMetricsRLSW_Object = MibTableColumn
oramodMetricsRLSW = _OramodMetricsRLSW_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 13),
    _OramodMetricsRLSW_Type()
)
oramodMetricsRLSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsRLSW.setStatus("mandatory")
_OramodMetricsRSR_Type = Gauge32
_OramodMetricsRSR_Object = MibTableColumn
oramodMetricsRSR = _OramodMetricsRSR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 14),
    _OramodMetricsRSR_Type()
)
oramodMetricsRSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsRSR.setStatus("mandatory")
_OramodMetricsSOR_Type = Gauge32
_OramodMetricsSOR_Object = MibTableColumn
oramodMetricsSOR = _OramodMetricsSOR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 15),
    _OramodMetricsSOR_Type()
)
oramodMetricsSOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSOR.setStatus("mandatory")
_OramodMetricsTRR_Type = Gauge32
_OramodMetricsTRR_Object = MibTableColumn
oramodMetricsTRR = _OramodMetricsTRR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 16),
    _OramodMetricsTRR_Type()
)
oramodMetricsTRR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsTRR.setStatus("mandatory")
_OramodMetricsUCR_Type = Gauge32
_OramodMetricsUCR_Object = MibTableColumn
oramodMetricsUCR = _OramodMetricsUCR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 17),
    _OramodMetricsUCR_Type()
)
oramodMetricsUCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsUCR.setStatus("mandatory")
_OramodMetricsUCPP_Type = Gauge32
_OramodMetricsUCPP_Object = MibTableColumn
oramodMetricsUCPP = _OramodMetricsUCPP_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 18),
    _OramodMetricsUCPP_Type()
)
oramodMetricsUCPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsUCPP.setStatus("mandatory")
_OramodMetricsURR_Type = Gauge32
_OramodMetricsURR_Object = MibTableColumn
oramodMetricsURR = _OramodMetricsURR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 19),
    _OramodMetricsURR_Type()
)
oramodMetricsURR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsURR.setStatus("mandatory")
_OramodMetricsSGALCE_Type = Gauge32
_OramodMetricsSGALCE_Object = MibTableColumn
oramodMetricsSGALCE = _OramodMetricsSGALCE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 20),
    _OramodMetricsSGALCE_Type()
)
oramodMetricsSGALCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSGALCE.setStatus("mandatory")
_OramodMetricsSGADDCE_Type = Gauge32
_OramodMetricsSGADDCE_Object = MibTableColumn
oramodMetricsSGADDCE = _OramodMetricsSGADDCE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 21),
    _OramodMetricsSGADDCE_Type()
)
oramodMetricsSGADDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSGADDCE.setStatus("mandatory")
_OramodMetricsDBTOTALRW_Type = Counter32
_OramodMetricsDBTOTALRW_Object = MibTableColumn
oramodMetricsDBTOTALRW = _OramodMetricsDBTOTALRW_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 22),
    _OramodMetricsDBTOTALRW_Type()
)
oramodMetricsDBTOTALRW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBTOTALRW.setStatus("mandatory")
_OramodMetricsDBBLKCHG_Type = Counter32
_OramodMetricsDBBLKCHG_Object = MibTableColumn
oramodMetricsDBBLKCHG = _OramodMetricsDBBLKCHG_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 23),
    _OramodMetricsDBBLKCHG_Type()
)
oramodMetricsDBBLKCHG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBBLKCHG.setStatus("mandatory")
_OramodMetricsDBBLKGET_Type = Counter32
_OramodMetricsDBBLKGET_Object = MibTableColumn
oramodMetricsDBBLKGET = _OramodMetricsDBBLKGET_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 24),
    _OramodMetricsDBBLKGET_Type()
)
oramodMetricsDBBLKGET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBBLKGET.setStatus("mandatory")
_OramodMetricsDBCNSTGET_Type = Counter32
_OramodMetricsDBCNSTGET_Object = MibTableColumn
oramodMetricsDBCNSTGET = _OramodMetricsDBCNSTGET_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 25),
    _OramodMetricsDBCNSTGET_Type()
)
oramodMetricsDBCNSTGET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBCNSTGET.setStatus("mandatory")
_OramodMetricsDBPHYSREAD_Type = Counter32
_OramodMetricsDBPHYSREAD_Object = MibTableColumn
oramodMetricsDBPHYSREAD = _OramodMetricsDBPHYSREAD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 26),
    _OramodMetricsDBPHYSREAD_Type()
)
oramodMetricsDBPHYSREAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBPHYSREAD.setStatus("mandatory")
_OramodMetricsDBSORTDISK_Type = Counter32
_OramodMetricsDBSORTDISK_Object = MibTableColumn
oramodMetricsDBSORTDISK = _OramodMetricsDBSORTDISK_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 27),
    _OramodMetricsDBSORTDISK_Type()
)
oramodMetricsDBSORTDISK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBSORTDISK.setStatus("mandatory")
_OramodMetricsDBSORTMEM_Type = Counter32
_OramodMetricsDBSORTMEM_Object = MibTableColumn
oramodMetricsDBSORTMEM = _OramodMetricsDBSORTMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 28),
    _OramodMetricsDBSORTMEM_Type()
)
oramodMetricsDBSORTMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBSORTMEM.setStatus("mandatory")
_OramodMetricsBLKFREEWAIT_Type = Gauge32
_OramodMetricsBLKFREEWAIT_Object = MibTableColumn
oramodMetricsBLKFREEWAIT = _OramodMetricsBLKFREEWAIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 29),
    _OramodMetricsBLKFREEWAIT_Type()
)
oramodMetricsBLKFREEWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsBLKFREEWAIT.setStatus("mandatory")
_OramodMetricsMTHRDQUEUEWAIT_Type = Gauge32
_OramodMetricsMTHRDQUEUEWAIT_Object = MibTableColumn
oramodMetricsMTHRDQUEUEWAIT = _OramodMetricsMTHRDQUEUEWAIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 30),
    _OramodMetricsMTHRDQUEUEWAIT_Type()
)
oramodMetricsMTHRDQUEUEWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsMTHRDQUEUEWAIT.setStatus("mandatory")
_OramodMetricsSESSHIWTRMEM_Type = Counter32
_OramodMetricsSESSHIWTRMEM_Object = MibTableColumn
oramodMetricsSESSHIWTRMEM = _OramodMetricsSESSHIWTRMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 31),
    _OramodMetricsSESSHIWTRMEM_Type()
)
oramodMetricsSESSHIWTRMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSESSHIWTRMEM.setStatus("mandatory")
_OramodMetricsSESSCURRMEM_Type = Counter32
_OramodMetricsSESSCURRMEM_Object = MibTableColumn
oramodMetricsSESSCURRMEM = _OramodMetricsSESSCURRMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 32),
    _OramodMetricsSESSCURRMEM_Type()
)
oramodMetricsSESSCURRMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSESSCURRMEM.setStatus("mandatory")
_OramodMetricsSESSHIWTR_Type = Counter32
_OramodMetricsSESSHIWTR_Object = MibTableColumn
oramodMetricsSESSHIWTR = _OramodMetricsSESSHIWTR_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 33),
    _OramodMetricsSESSHIWTR_Type()
)
oramodMetricsSESSHIWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSESSHIWTR.setStatus("mandatory")
_OramodMetricsSESSCURRENT_Type = Gauge32
_OramodMetricsSESSCURRENT_Object = MibTableColumn
oramodMetricsSESSCURRENT = _OramodMetricsSESSCURRENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 34),
    _OramodMetricsSESSCURRENT_Type()
)
oramodMetricsSESSCURRENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSESSCURRENT.setStatus("mandatory")
_OramodMetricsUSERCOMMITS_Type = Counter32
_OramodMetricsUSERCOMMITS_Object = MibTableColumn
oramodMetricsUSERCOMMITS = _OramodMetricsUSERCOMMITS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 35),
    _OramodMetricsUSERCOMMITS_Type()
)
oramodMetricsUSERCOMMITS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsUSERCOMMITS.setStatus("mandatory")
_OramodMetricsUSERROLLBACK_Type = Counter32
_OramodMetricsUSERROLLBACK_Object = MibTableColumn
oramodMetricsUSERROLLBACK = _OramodMetricsUSERROLLBACK_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 36),
    _OramodMetricsUSERROLLBACK_Type()
)
oramodMetricsUSERROLLBACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsUSERROLLBACK.setStatus("mandatory")
_OramodMetricsUSERCALLS_Type = Counter32
_OramodMetricsUSERCALLS_Object = MibTableColumn
oramodMetricsUSERCALLS = _OramodMetricsUSERCALLS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 37),
    _OramodMetricsUSERCALLS_Type()
)
oramodMetricsUSERCALLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsUSERCALLS.setStatus("mandatory")
_OramodMetricsDBPHYSWRTS_Type = Counter32
_OramodMetricsDBPHYSWRTS_Object = MibTableColumn
oramodMetricsDBPHYSWRTS = _OramodMetricsDBPHYSWRTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 38),
    _OramodMetricsDBPHYSWRTS_Type()
)
oramodMetricsDBPHYSWRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDBPHYSWRTS.setStatus("mandatory")
_OramodMetricsTBLSCANROWS_Type = Counter32
_OramodMetricsTBLSCANROWS_Object = MibTableColumn
oramodMetricsTBLSCANROWS = _OramodMetricsTBLSCANROWS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 39),
    _OramodMetricsTBLSCANROWS_Type()
)
oramodMetricsTBLSCANROWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsTBLSCANROWS.setStatus("mandatory")
_OramodMetricsTBLFTCHROWID_Type = Counter32
_OramodMetricsTBLFTCHROWID_Object = MibTableColumn
oramodMetricsTBLFTCHROWID = _OramodMetricsTBLFTCHROWID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 40),
    _OramodMetricsTBLFTCHROWID_Type()
)
oramodMetricsTBLFTCHROWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsTBLFTCHROWID.setStatus("mandatory")
_OramodMetricsTBLFTCHCROW_Type = Counter32
_OramodMetricsTBLFTCHCROW_Object = MibTableColumn
oramodMetricsTBLFTCHCROW = _OramodMetricsTBLFTCHCROW_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 41),
    _OramodMetricsTBLFTCHCROW_Type()
)
oramodMetricsTBLFTCHCROW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsTBLFTCHCROW.setStatus("mandatory")
_OramodMetricsRECRSVCALLS_Type = Counter32
_OramodMetricsRECRSVCALLS_Object = MibTableColumn
oramodMetricsRECRSVCALLS = _OramodMetricsRECRSVCALLS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 42),
    _OramodMetricsRECRSVCALLS_Type()
)
oramodMetricsRECRSVCALLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsRECRSVCALLS.setStatus("mandatory")
_OramodMetricsCNSTCHGS_Type = Counter32
_OramodMetricsCNSTCHGS_Object = MibTableColumn
oramodMetricsCNSTCHGS = _OramodMetricsCNSTCHGS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 43),
    _OramodMetricsCNSTCHGS_Type()
)
oramodMetricsCNSTCHGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCNSTCHGS.setStatus("mandatory")
_OramodMetricsPARSECNT_Type = Counter32
_OramodMetricsPARSECNT_Object = MibTableColumn
oramodMetricsPARSECNT = _OramodMetricsPARSECNT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 44),
    _OramodMetricsPARSECNT_Type()
)
oramodMetricsPARSECNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsPARSECNT.setStatus("mandatory")
_OramodMetricsCPUTM_Type = Integer32
_OramodMetricsCPUTM_Object = MibTableColumn
oramodMetricsCPUTM = _OramodMetricsCPUTM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 45),
    _OramodMetricsCPUTM_Type()
)
oramodMetricsCPUTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsCPUTM.setStatus("mandatory")
_OramodMetricsLOGFILESWTCH_Type = Integer32
_OramodMetricsLOGFILESWTCH_Object = MibTableColumn
oramodMetricsLOGFILESWTCH = _OramodMetricsLOGFILESWTCH_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 46),
    _OramodMetricsLOGFILESWTCH_Type()
)
oramodMetricsLOGFILESWTCH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsLOGFILESWTCH.setStatus("mandatory")
_OramodMetricsARCHIVER_Type = DisplayString
_OramodMetricsARCHIVER_Object = MibTableColumn
oramodMetricsARCHIVER = _OramodMetricsARCHIVER_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 47),
    _OramodMetricsARCHIVER_Type()
)
oramodMetricsARCHIVER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsARCHIVER.setStatus("mandatory")
_OramodMetricsDATABASESTATUS_Type = DisplayString
_OramodMetricsDATABASESTATUS_Object = MibTableColumn
oramodMetricsDATABASESTATUS = _OramodMetricsDATABASESTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 48),
    _OramodMetricsDATABASESTATUS_Type()
)
oramodMetricsDATABASESTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsDATABASESTATUS.setStatus("mandatory")
_OramodMetricsSHUTDOWNPENDING_Type = DisplayString
_OramodMetricsSHUTDOWNPENDING_Object = MibTableColumn
oramodMetricsSHUTDOWNPENDING = _OramodMetricsSHUTDOWNPENDING_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 49),
    _OramodMetricsSHUTDOWNPENDING_Type()
)
oramodMetricsSHUTDOWNPENDING.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsSHUTDOWNPENDING.setStatus("mandatory")
_OramodMetricsLASTUPDATE_Type = TimeTicks
_OramodMetricsLASTUPDATE_Object = MibTableColumn
oramodMetricsLASTUPDATE = _OramodMetricsLASTUPDATE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 2, 1, 1, 50),
    _OramodMetricsLASTUPDATE_Type()
)
oramodMetricsLASTUPDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodMetricsLASTUPDATE.setStatus("mandatory")
_OramodSGA_ObjectIdentity = ObjectIdentity
oramodSGA = _OramodSGA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3)
)
_OramodSgaDddAgg_ObjectIdentity = ObjectIdentity
oramodSgaDddAgg = _OramodSgaDddAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1)
)
_OramodSgaDddAggTable_Object = MibTable
oramodSgaDddAggTable = _OramodSgaDddAggTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    oramodSgaDddAggTable.setStatus("mandatory")
_OramodSgaDddAggEntry_Object = MibTableRow
oramodSgaDddAggEntry = _OramodSgaDddAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1)
)
oramodSgaDddAggEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodSGAAGGSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodSgaDddAggEntry.setStatus("mandatory")


class _OramodSGAAGGSIDINDX_Type(Integer32):
    """Custom type oramodSGAAGGSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodSGAAGGSIDINDX_Type.__name__ = "Integer32"
_OramodSGAAGGSIDINDX_Object = MibTableColumn
oramodSGAAGGSIDINDX = _OramodSGAAGGSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 1),
    _OramodSGAAGGSIDINDX_Type()
)
oramodSGAAGGSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGSIDINDX.setStatus("mandatory")
_OramodSGAAGGCNT_Type = Counter32
_OramodSGAAGGCNT_Object = MibTableColumn
oramodSGAAGGCNT = _OramodSGAAGGCNT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 2),
    _OramodSGAAGGCNT_Type()
)
oramodSGAAGGCNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGCNT.setStatus("mandatory")
_OramodSGAAGGUSGE_Type = Counter32
_OramodSGAAGGUSGE_Object = MibTableColumn
oramodSGAAGGUSGE = _OramodSGAAGGUSGE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 3),
    _OramodSGAAGGUSGE_Type()
)
oramodSGAAGGUSGE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGUSGE.setStatus("mandatory")
_OramodSGAAGGFIX_Type = Counter32
_OramodSGAAGGFIX_Object = MibTableColumn
oramodSGAAGGFIX = _OramodSGAAGGFIX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 4),
    _OramodSGAAGGFIX_Type()
)
oramodSGAAGGFIX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGFIX.setStatus("mandatory")
_OramodSGAAGGGET_Type = Counter32
_OramodSGAAGGGET_Object = MibTableColumn
oramodSGAAGGGET = _OramodSGAAGGGET_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 5),
    _OramodSGAAGGGET_Type()
)
oramodSGAAGGGET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGGET.setStatus("mandatory")
_OramodSGAAGGGETMISS_Type = Counter32
_OramodSGAAGGGETMISS_Object = MibTableColumn
oramodSGAAGGGETMISS = _OramodSGAAGGGETMISS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 6),
    _OramodSGAAGGGETMISS_Type()
)
oramodSGAAGGGETMISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGGETMISS.setStatus("mandatory")
_OramodSGAAGGSCAN_Type = Counter32
_OramodSGAAGGSCAN_Object = MibTableColumn
oramodSGAAGGSCAN = _OramodSGAAGGSCAN_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 7),
    _OramodSGAAGGSCAN_Type()
)
oramodSGAAGGSCAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGSCAN.setStatus("mandatory")
_OramodSGAAGGSCANMISS_Type = Counter32
_OramodSGAAGGSCANMISS_Object = MibTableColumn
oramodSGAAGGSCANMISS = _OramodSGAAGGSCANMISS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 8),
    _OramodSGAAGGSCANMISS_Type()
)
oramodSGAAGGSCANMISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGSCANMISS.setStatus("mandatory")
_OramodSGAAGGSCANCPLT_Type = Counter32
_OramodSGAAGGSCANCPLT_Object = MibTableColumn
oramodSGAAGGSCANCPLT = _OramodSGAAGGSCANCPLT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 9),
    _OramodSGAAGGSCANCPLT_Type()
)
oramodSGAAGGSCANCPLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGSCANCPLT.setStatus("mandatory")
_OramodSGAAGGMODS_Type = Counter32
_OramodSGAAGGMODS_Object = MibTableColumn
oramodSGAAGGMODS = _OramodSGAAGGMODS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 10),
    _OramodSGAAGGMODS_Type()
)
oramodSGAAGGMODS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGMODS.setStatus("mandatory")
_OramodSGAAGGFLUSH_Type = Counter32
_OramodSGAAGGFLUSH_Object = MibTableColumn
oramodSGAAGGFLUSH = _OramodSGAAGGFLUSH_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 1, 1, 1, 11),
    _OramodSGAAGGFLUSH_Type()
)
oramodSGAAGGFLUSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGAAGGFLUSH.setStatus("mandatory")
_OramodSgaDlci_ObjectIdentity = ObjectIdentity
oramodSgaDlci = _OramodSgaDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2)
)
_OramodSgaDlciTable_Object = MibTable
oramodSgaDlciTable = _OramodSgaDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oramodSgaDlciTable.setStatus("mandatory")
_OramodSgaDlciEntry_Object = MibTableRow
oramodSgaDlciEntry = _OramodSgaDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1)
)
oramodSgaDlciEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodSGADLCISIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodSGADLCIINDX"),
)
if mibBuilder.loadTexts:
    oramodSgaDlciEntry.setStatus("mandatory")


class _OramodSGADLCISIDINDX_Type(Integer32):
    """Custom type oramodSGADLCISIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodSGADLCISIDINDX_Type.__name__ = "Integer32"
_OramodSGADLCISIDINDX_Object = MibTableColumn
oramodSGADLCISIDINDX = _OramodSGADLCISIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 1),
    _OramodSGADLCISIDINDX_Type()
)
oramodSGADLCISIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCISIDINDX.setStatus("mandatory")


class _OramodSGADLCIINDX_Type(Integer32):
    """Custom type oramodSGADLCIINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodSGADLCIINDX_Type.__name__ = "Integer32"
_OramodSGADLCIINDX_Object = MibTableColumn
oramodSGADLCIINDX = _OramodSGADLCIINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 2),
    _OramodSGADLCIINDX_Type()
)
oramodSGADLCIINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIINDX.setStatus("mandatory")
_OramodSGADLCINAME_Type = DisplayString
_OramodSGADLCINAME_Object = MibTableColumn
oramodSGADLCINAME = _OramodSGADLCINAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 3),
    _OramodSGADLCINAME_Type()
)
oramodSGADLCINAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCINAME.setStatus("mandatory")
_OramodSGADLCIGET_Type = Counter32
_OramodSGADLCIGET_Object = MibTableColumn
oramodSGADLCIGET = _OramodSGADLCIGET_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 4),
    _OramodSGADLCIGET_Type()
)
oramodSGADLCIGET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIGET.setStatus("mandatory")
_OramodSGADLCIGETHIT_Type = Counter32
_OramodSGADLCIGETHIT_Object = MibTableColumn
oramodSGADLCIGETHIT = _OramodSGADLCIGETHIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 5),
    _OramodSGADLCIGETHIT_Type()
)
oramodSGADLCIGETHIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIGETHIT.setStatus("mandatory")
_OramodSGADLCIGETHITRT_Type = Gauge32
_OramodSGADLCIGETHITRT_Object = MibTableColumn
oramodSGADLCIGETHITRT = _OramodSGADLCIGETHITRT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 6),
    _OramodSGADLCIGETHITRT_Type()
)
oramodSGADLCIGETHITRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIGETHITRT.setStatus("mandatory")
_OramodSGADLCIPIN_Type = Counter32
_OramodSGADLCIPIN_Object = MibTableColumn
oramodSGADLCIPIN = _OramodSGADLCIPIN_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 7),
    _OramodSGADLCIPIN_Type()
)
oramodSGADLCIPIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIPIN.setStatus("mandatory")
_OramodSGADLCIPINHIT_Type = Counter32
_OramodSGADLCIPINHIT_Object = MibTableColumn
oramodSGADLCIPINHIT = _OramodSGADLCIPINHIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 8),
    _OramodSGADLCIPINHIT_Type()
)
oramodSGADLCIPINHIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIPINHIT.setStatus("mandatory")
_OramodSGADLCIPINHITRT_Type = Gauge32
_OramodSGADLCIPINHITRT_Object = MibTableColumn
oramodSGADLCIPINHITRT = _OramodSGADLCIPINHITRT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 9),
    _OramodSGADLCIPINHITRT_Type()
)
oramodSGADLCIPINHITRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIPINHITRT.setStatus("mandatory")
_OramodSGADLCIRELOAD_Type = Counter32
_OramodSGADLCIRELOAD_Object = MibTableColumn
oramodSGADLCIRELOAD = _OramodSGADLCIRELOAD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 10),
    _OramodSGADLCIRELOAD_Type()
)
oramodSGADLCIRELOAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIRELOAD.setStatus("mandatory")
_OramodSGADLCIINVALID_Type = Counter32
_OramodSGADLCIINVALID_Object = MibTableColumn
oramodSGADLCIINVALID = _OramodSGADLCIINVALID_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 3, 2, 1, 1, 11),
    _OramodSGADLCIINVALID_Type()
)
oramodSGADLCIINVALID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodSGADLCIINVALID.setStatus("mandatory")
_OramodRedoLogBuf_ObjectIdentity = ObjectIdentity
oramodRedoLogBuf = _OramodRedoLogBuf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4)
)
_OramodRedoLogBufTable_Object = MibTable
oramodRedoLogBufTable = _OramodRedoLogBufTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1)
)
if mibBuilder.loadTexts:
    oramodRedoLogBufTable.setStatus("mandatory")
_OramodRedoLogBufEntry_Object = MibTableRow
oramodRedoLogBufEntry = _OramodRedoLogBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1)
)
oramodRedoLogBufEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodREDOSIDINDX"),
)
if mibBuilder.loadTexts:
    oramodRedoLogBufEntry.setStatus("mandatory")


class _OramodREDOSIDINDX_Type(Integer32):
    """Custom type oramodREDOSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodREDOSIDINDX_Type.__name__ = "Integer32"
_OramodREDOSIDINDX_Object = MibTableColumn
oramodREDOSIDINDX = _OramodREDOSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 1),
    _OramodREDOSIDINDX_Type()
)
oramodREDOSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSIDINDX.setStatus("mandatory")
_OramodREDOBLKWRT_Type = Counter32
_OramodREDOBLKWRT_Object = MibTableColumn
oramodREDOBLKWRT = _OramodREDOBLKWRT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 2),
    _OramodREDOBLKWRT_Type()
)
oramodREDOBLKWRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOBLKWRT.setStatus("mandatory")
_OramodREDOENTRIES_Type = Counter32
_OramodREDOENTRIES_Object = MibTableColumn
oramodREDOENTRIES = _OramodREDOENTRIES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 3),
    _OramodREDOENTRIES_Type()
)
oramodREDOENTRIES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOENTRIES.setStatus("mandatory")
_OramodREDOSIZE_Type = Integer32
_OramodREDOSIZE_Object = MibTableColumn
oramodREDOSIZE = _OramodREDOSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 4),
    _OramodREDOSIZE_Type()
)
oramodREDOSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSIZE.setStatus("mandatory")
_OramodREDOSPACERQST_Type = Counter32
_OramodREDOSPACERQST_Object = MibTableColumn
oramodREDOSPACERQST = _OramodREDOSPACERQST_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 5),
    _OramodREDOSPACERQST_Type()
)
oramodREDOSPACERQST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSPACERQST.setStatus("mandatory")
_OramodREDOSPACEWAIT_Type = Counter32
_OramodREDOSPACEWAIT_Object = MibTableColumn
oramodREDOSPACEWAIT = _OramodREDOSPACEWAIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 6),
    _OramodREDOSPACEWAIT_Type()
)
oramodREDOSPACEWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSPACEWAIT.setStatus("mandatory")
_OramodREDOSYNCHWRT_Type = Counter32
_OramodREDOSYNCHWRT_Object = MibTableColumn
oramodREDOSYNCHWRT = _OramodREDOSYNCHWRT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 7),
    _OramodREDOSYNCHWRT_Type()
)
oramodREDOSYNCHWRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSYNCHWRT.setStatus("mandatory")
_OramodREDOSYNCHTM_Type = Integer32
_OramodREDOSYNCHTM_Object = MibTableColumn
oramodREDOSYNCHTM = _OramodREDOSYNCHTM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 8),
    _OramodREDOSYNCHTM_Type()
)
oramodREDOSYNCHTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOSYNCHTM.setStatus("mandatory")
_OramodREDOWASTAGE_Type = Counter32
_OramodREDOWASTAGE_Object = MibTableColumn
oramodREDOWASTAGE = _OramodREDOWASTAGE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 9),
    _OramodREDOWASTAGE_Type()
)
oramodREDOWASTAGE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOWASTAGE.setStatus("mandatory")
_OramodREDORETRIES_Type = Counter32
_OramodREDORETRIES_Object = MibTableColumn
oramodREDORETRIES = _OramodREDORETRIES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 10),
    _OramodREDORETRIES_Type()
)
oramodREDORETRIES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDORETRIES.setStatus("mandatory")
_OramodREDOLASTUPDATE_Type = TimeTicks
_OramodREDOLASTUPDATE_Object = MibTableColumn
oramodREDOLASTUPDATE = _OramodREDOLASTUPDATE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 4, 1, 1, 11),
    _OramodREDOLASTUPDATE_Type()
)
oramodREDOLASTUPDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodREDOLASTUPDATE.setStatus("mandatory")
_OramodRollBack_ObjectIdentity = ObjectIdentity
oramodRollBack = _OramodRollBack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5)
)
_OramodRollBackTable_Object = MibTable
oramodRollBackTable = _OramodRollBackTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1)
)
if mibBuilder.loadTexts:
    oramodRollBackTable.setStatus("mandatory")
_OramodRollBackEntry_Object = MibTableRow
oramodRollBackEntry = _OramodRollBackEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1)
)
oramodRollBackEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodRollBackSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodRollBackSEGINDX"),
)
if mibBuilder.loadTexts:
    oramodRollBackEntry.setStatus("mandatory")


class _OramodRollBackSIDINDX_Type(Integer32):
    """Custom type oramodRollBackSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodRollBackSIDINDX_Type.__name__ = "Integer32"
_OramodRollBackSIDINDX_Object = MibTableColumn
oramodRollBackSIDINDX = _OramodRollBackSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 1),
    _OramodRollBackSIDINDX_Type()
)
oramodRollBackSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackSIDINDX.setStatus("mandatory")
_OramodRollBackSEGINDX_Type = Integer32
_OramodRollBackSEGINDX_Object = MibTableColumn
oramodRollBackSEGINDX = _OramodRollBackSEGINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 2),
    _OramodRollBackSEGINDX_Type()
)
oramodRollBackSEGINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackSEGINDX.setStatus("mandatory")
_OramodRollBackSEGNAME_Type = DisplayString
_OramodRollBackSEGNAME_Object = MibTableColumn
oramodRollBackSEGNAME = _OramodRollBackSEGNAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 3),
    _OramodRollBackSEGNAME_Type()
)
oramodRollBackSEGNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackSEGNAME.setStatus("mandatory")
_OramodRollBackEXTENTS_Type = Counter32
_OramodRollBackEXTENTS_Object = MibTableColumn
oramodRollBackEXTENTS = _OramodRollBackEXTENTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 4),
    _OramodRollBackEXTENTS_Type()
)
oramodRollBackEXTENTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackEXTENTS.setStatus("mandatory")
_OramodRollBackRSSIZE_Type = Counter32
_OramodRollBackRSSIZE_Object = MibTableColumn
oramodRollBackRSSIZE = _OramodRollBackRSSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 5),
    _OramodRollBackRSSIZE_Type()
)
oramodRollBackRSSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackRSSIZE.setStatus("mandatory")
_OramodRollBackWRITES_Type = Counter32
_OramodRollBackWRITES_Object = MibTableColumn
oramodRollBackWRITES = _OramodRollBackWRITES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 6),
    _OramodRollBackWRITES_Type()
)
oramodRollBackWRITES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackWRITES.setStatus("mandatory")
_OramodRollBackGETS_Type = Counter32
_OramodRollBackGETS_Object = MibTableColumn
oramodRollBackGETS = _OramodRollBackGETS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 7),
    _OramodRollBackGETS_Type()
)
oramodRollBackGETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackGETS.setStatus("mandatory")
_OramodRollBackWAITS_Type = Counter32
_OramodRollBackWAITS_Object = MibTableColumn
oramodRollBackWAITS = _OramodRollBackWAITS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 8),
    _OramodRollBackWAITS_Type()
)
oramodRollBackWAITS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackWAITS.setStatus("mandatory")
_OramodRollBackOPTSIZE_Type = Integer32
_OramodRollBackOPTSIZE_Object = MibTableColumn
oramodRollBackOPTSIZE = _OramodRollBackOPTSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 9),
    _OramodRollBackOPTSIZE_Type()
)
oramodRollBackOPTSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackOPTSIZE.setStatus("mandatory")
_OramodRollBackSHRINKS_Type = Counter32
_OramodRollBackSHRINKS_Object = MibTableColumn
oramodRollBackSHRINKS = _OramodRollBackSHRINKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 10),
    _OramodRollBackSHRINKS_Type()
)
oramodRollBackSHRINKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackSHRINKS.setStatus("mandatory")
_OramodRollBackWRAPS_Type = Counter32
_OramodRollBackWRAPS_Object = MibTableColumn
oramodRollBackWRAPS = _OramodRollBackWRAPS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 11),
    _OramodRollBackWRAPS_Type()
)
oramodRollBackWRAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackWRAPS.setStatus("mandatory")
_OramodRollBackEXTENDS_Type = Counter32
_OramodRollBackEXTENDS_Object = MibTableColumn
oramodRollBackEXTENDS = _OramodRollBackEXTENDS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 12),
    _OramodRollBackEXTENDS_Type()
)
oramodRollBackEXTENDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackEXTENDS.setStatus("mandatory")
_OramodRollBackAVESHRINK_Type = Integer32
_OramodRollBackAVESHRINK_Object = MibTableColumn
oramodRollBackAVESHRINK = _OramodRollBackAVESHRINK_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 13),
    _OramodRollBackAVESHRINK_Type()
)
oramodRollBackAVESHRINK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackAVESHRINK.setStatus("mandatory")
_OramodRollBackAVEACTIVE_Type = Counter32
_OramodRollBackAVEACTIVE_Object = MibTableColumn
oramodRollBackAVEACTIVE = _OramodRollBackAVEACTIVE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 14),
    _OramodRollBackAVEACTIVE_Type()
)
oramodRollBackAVEACTIVE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackAVEACTIVE.setStatus("mandatory")
_OramodRollBackSTATUS_Type = Integer32
_OramodRollBackSTATUS_Object = MibTableColumn
oramodRollBackSTATUS = _OramodRollBackSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 5, 1, 1, 15),
    _OramodRollBackSTATUS_Type()
)
oramodRollBackSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodRollBackSTATUS.setStatus("mandatory")
_OramodWaits_ObjectIdentity = ObjectIdentity
oramodWaits = _OramodWaits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6)
)
_OramodWaitsTable_Object = MibTable
oramodWaitsTable = _OramodWaitsTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1)
)
if mibBuilder.loadTexts:
    oramodWaitsTable.setStatus("mandatory")
_OramodWaitsEntry_Object = MibTableRow
oramodWaitsEntry = _OramodWaitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1)
)
oramodWaitsEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodWaitsSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodWaitsEVENTINDX"),
)
if mibBuilder.loadTexts:
    oramodWaitsEntry.setStatus("mandatory")


class _OramodWaitsSIDINDX_Type(Integer32):
    """Custom type oramodWaitsSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodWaitsSIDINDX_Type.__name__ = "Integer32"
_OramodWaitsSIDINDX_Object = MibTableColumn
oramodWaitsSIDINDX = _OramodWaitsSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 1),
    _OramodWaitsSIDINDX_Type()
)
oramodWaitsSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsSIDINDX.setStatus("mandatory")


class _OramodWaitsEVENTINDX_Type(Integer32):
    """Custom type oramodWaitsEVENTINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodWaitsEVENTINDX_Type.__name__ = "Integer32"
_OramodWaitsEVENTINDX_Object = MibTableColumn
oramodWaitsEVENTINDX = _OramodWaitsEVENTINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 2),
    _OramodWaitsEVENTINDX_Type()
)
oramodWaitsEVENTINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsEVENTINDX.setStatus("mandatory")
_OramodWaitsEVENT_Type = DisplayString
_OramodWaitsEVENT_Object = MibTableColumn
oramodWaitsEVENT = _OramodWaitsEVENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 3),
    _OramodWaitsEVENT_Type()
)
oramodWaitsEVENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsEVENT.setStatus("mandatory")
_OramodWaitsTOTALWAITS_Type = Counter32
_OramodWaitsTOTALWAITS_Object = MibTableColumn
oramodWaitsTOTALWAITS = _OramodWaitsTOTALWAITS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 4),
    _OramodWaitsTOTALWAITS_Type()
)
oramodWaitsTOTALWAITS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsTOTALWAITS.setStatus("mandatory")
_OramodWaitsTOTALTIMOUT_Type = Counter32
_OramodWaitsTOTALTIMOUT_Object = MibTableColumn
oramodWaitsTOTALTIMOUT = _OramodWaitsTOTALTIMOUT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 5),
    _OramodWaitsTOTALTIMOUT_Type()
)
oramodWaitsTOTALTIMOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsTOTALTIMOUT.setStatus("mandatory")
_OramodWaitsTIMEWAITED_Type = Counter32
_OramodWaitsTIMEWAITED_Object = MibTableColumn
oramodWaitsTIMEWAITED = _OramodWaitsTIMEWAITED_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 6),
    _OramodWaitsTIMEWAITED_Type()
)
oramodWaitsTIMEWAITED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsTIMEWAITED.setStatus("mandatory")
_OramodWaitsAVGWAIT_Type = Counter32
_OramodWaitsAVGWAIT_Object = MibTableColumn
oramodWaitsAVGWAIT = _OramodWaitsAVGWAIT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 6, 1, 1, 7),
    _OramodWaitsAVGWAIT_Type()
)
oramodWaitsAVGWAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodWaitsAVGWAIT.setStatus("mandatory")
_OramodExpSql_ObjectIdentity = ObjectIdentity
oramodExpSql = _OramodExpSql_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7)
)
_OramodExpSqlTable_Object = MibTable
oramodExpSqlTable = _OramodExpSqlTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1)
)
if mibBuilder.loadTexts:
    oramodExpSqlTable.setStatus("mandatory")
_OramodExpSqlEntry_Object = MibTableRow
oramodExpSqlEntry = _OramodExpSqlEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1)
)
oramodExpSqlEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodExpSqlSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodExpSqlSQLINDX"),
)
if mibBuilder.loadTexts:
    oramodExpSqlEntry.setStatus("mandatory")


class _OramodExpSqlSIDINDX_Type(Integer32):
    """Custom type oramodExpSqlSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodExpSqlSIDINDX_Type.__name__ = "Integer32"
_OramodExpSqlSIDINDX_Object = MibTableColumn
oramodExpSqlSIDINDX = _OramodExpSqlSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 1),
    _OramodExpSqlSIDINDX_Type()
)
oramodExpSqlSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlSIDINDX.setStatus("mandatory")


class _OramodExpSqlSQLINDX_Type(Integer32):
    """Custom type oramodExpSqlSQLINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodExpSqlSQLINDX_Type.__name__ = "Integer32"
_OramodExpSqlSQLINDX_Object = MibTableColumn
oramodExpSqlSQLINDX = _OramodExpSqlSQLINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 2),
    _OramodExpSqlSQLINDX_Type()
)
oramodExpSqlSQLINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlSQLINDX.setStatus("mandatory")
_OramodExpSqlEXECUTION_Type = Gauge32
_OramodExpSqlEXECUTION_Object = MibTableColumn
oramodExpSqlEXECUTION = _OramodExpSqlEXECUTION_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 3),
    _OramodExpSqlEXECUTION_Type()
)
oramodExpSqlEXECUTION.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlEXECUTION.setStatus("mandatory")
_OramodExpSqlDISKREAD_Type = Gauge32
_OramodExpSqlDISKREAD_Object = MibTableColumn
oramodExpSqlDISKREAD = _OramodExpSqlDISKREAD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 4),
    _OramodExpSqlDISKREAD_Type()
)
oramodExpSqlDISKREAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlDISKREAD.setStatus("mandatory")
_OramodExpSqlPARSECNT_Type = Gauge32
_OramodExpSqlPARSECNT_Object = MibTableColumn
oramodExpSqlPARSECNT = _OramodExpSqlPARSECNT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 5),
    _OramodExpSqlPARSECNT_Type()
)
oramodExpSqlPARSECNT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlPARSECNT.setStatus("mandatory")
_OramodExpSqlBUFFGETS_Type = Gauge32
_OramodExpSqlBUFFGETS_Object = MibTableColumn
oramodExpSqlBUFFGETS = _OramodExpSqlBUFFGETS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 6),
    _OramodExpSqlBUFFGETS_Type()
)
oramodExpSqlBUFFGETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlBUFFGETS.setStatus("mandatory")
_OramodExpSqlSORTS_Type = Gauge32
_OramodExpSqlSORTS_Object = MibTableColumn
oramodExpSqlSORTS = _OramodExpSqlSORTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 7),
    _OramodExpSqlSORTS_Type()
)
oramodExpSqlSORTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlSORTS.setStatus("mandatory")
_OramodExpSqlSQL_Type = DisplayString
_OramodExpSqlSQL_Object = MibTableColumn
oramodExpSqlSQL = _OramodExpSqlSQL_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 7, 1, 1, 8),
    _OramodExpSqlSQL_Type()
)
oramodExpSqlSQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodExpSqlSQL.setStatus("mandatory")
_OramodTblsp_ObjectIdentity = ObjectIdentity
oramodTblsp = _OramodTblsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8)
)
_OramodTblspTable_Object = MibTable
oramodTblspTable = _OramodTblspTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1)
)
if mibBuilder.loadTexts:
    oramodTblspTable.setStatus("mandatory")
_OramodTblspEntry_Object = MibTableRow
oramodTblspEntry = _OramodTblspEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1)
)
oramodTblspEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodTblspSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodTblspTBLSPINDX"),
)
if mibBuilder.loadTexts:
    oramodTblspEntry.setStatus("mandatory")


class _OramodTblspSIDINDX_Type(Integer32):
    """Custom type oramodTblspSIDINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodTblspSIDINDX_Type.__name__ = "Integer32"
_OramodTblspSIDINDX_Object = MibTableColumn
oramodTblspSIDINDX = _OramodTblspSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 1),
    _OramodTblspSIDINDX_Type()
)
oramodTblspSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspSIDINDX.setStatus("mandatory")


class _OramodTblspTBLSPINDX_Type(Integer32):
    """Custom type oramodTblspTBLSPINDX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OramodTblspTBLSPINDX_Type.__name__ = "Integer32"
_OramodTblspTBLSPINDX_Object = MibTableColumn
oramodTblspTBLSPINDX = _OramodTblspTBLSPINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 2),
    _OramodTblspTBLSPINDX_Type()
)
oramodTblspTBLSPINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspTBLSPINDX.setStatus("mandatory")
_OramodTblspTBLSPNAME_Type = DisplayString
_OramodTblspTBLSPNAME_Object = MibTableColumn
oramodTblspTBLSPNAME = _OramodTblspTBLSPNAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 3),
    _OramodTblspTBLSPNAME_Type()
)
oramodTblspTBLSPNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspTBLSPNAME.setStatus("mandatory")
_OramodTblspFILENAME_Type = DisplayString
_OramodTblspFILENAME_Object = MibTableColumn
oramodTblspFILENAME = _OramodTblspFILENAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 4),
    _OramodTblspFILENAME_Type()
)
oramodTblspFILENAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspFILENAME.setStatus("mandatory")
_OramodTblspEXTENTS_Type = Gauge32
_OramodTblspEXTENTS_Object = MibTableColumn
oramodTblspEXTENTS = _OramodTblspEXTENTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 5),
    _OramodTblspEXTENTS_Type()
)
oramodTblspEXTENTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspEXTENTS.setStatus("mandatory")
_OramodTblspLRGEXTENT_Type = Gauge32
_OramodTblspLRGEXTENT_Object = MibTableColumn
oramodTblspLRGEXTENT = _OramodTblspLRGEXTENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 6),
    _OramodTblspLRGEXTENT_Type()
)
oramodTblspLRGEXTENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspLRGEXTENT.setStatus("mandatory")
_OramodTblspSMEXTENT_Type = Gauge32
_OramodTblspSMEXTENT_Object = MibTableColumn
oramodTblspSMEXTENT = _OramodTblspSMEXTENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 7),
    _OramodTblspSMEXTENT_Type()
)
oramodTblspSMEXTENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspSMEXTENT.setStatus("mandatory")
_OramodTblspINCREMENTBY_Type = Integer32
_OramodTblspINCREMENTBY_Object = MibTableColumn
oramodTblspINCREMENTBY = _OramodTblspINCREMENTBY_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 8),
    _OramodTblspINCREMENTBY_Type()
)
oramodTblspINCREMENTBY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspINCREMENTBY.setStatus("mandatory")
_OramodTblspBYTESCOALSD_Type = Gauge32
_OramodTblspBYTESCOALSD_Object = MibTableColumn
oramodTblspBYTESCOALSD = _OramodTblspBYTESCOALSD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 9),
    _OramodTblspBYTESCOALSD_Type()
)
oramodTblspBYTESCOALSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspBYTESCOALSD.setStatus("mandatory")
_OramodTblspBYTESFREE_Type = Gauge32
_OramodTblspBYTESFREE_Object = MibTableColumn
oramodTblspBYTESFREE = _OramodTblspBYTESFREE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 8, 1, 1, 10),
    _OramodTblspBYTESFREE_Type()
)
oramodTblspBYTESFREE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTblspBYTESFREE.setStatus("mandatory")
_OramodLocks_ObjectIdentity = ObjectIdentity
oramodLocks = _OramodLocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9)
)
_OramodLock_ObjectIdentity = ObjectIdentity
oramodLock = _OramodLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1)
)
_OramodLockTable_Object = MibTable
oramodLockTable = _OramodLockTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1)
)
if mibBuilder.loadTexts:
    oramodLockTable.setStatus("mandatory")
_OramodLockEntry_Object = MibTableRow
oramodLockEntry = _OramodLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1)
)
oramodLockEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodLockSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodLockUSERINDX"),
)
if mibBuilder.loadTexts:
    oramodLockEntry.setStatus("mandatory")
_OramodLockSIDINDX_Type = Integer32
_OramodLockSIDINDX_Object = MibTableColumn
oramodLockSIDINDX = _OramodLockSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 1),
    _OramodLockSIDINDX_Type()
)
oramodLockSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockSIDINDX.setStatus("mandatory")
_OramodLockUSERINDX_Type = Integer32
_OramodLockUSERINDX_Object = MibTableColumn
oramodLockUSERINDX = _OramodLockUSERINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 2),
    _OramodLockUSERINDX_Type()
)
oramodLockUSERINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockUSERINDX.setStatus("mandatory")
_OramodLockUSERNAME_Type = DisplayString
_OramodLockUSERNAME_Object = MibTableColumn
oramodLockUSERNAME = _OramodLockUSERNAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 3),
    _OramodLockUSERNAME_Type()
)
oramodLockUSERNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockUSERNAME.setStatus("mandatory")
_OramodLockOBJECT_Type = DisplayString
_OramodLockOBJECT_Object = MibTableColumn
oramodLockOBJECT = _OramodLockOBJECT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 4),
    _OramodLockOBJECT_Type()
)
oramodLockOBJECT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockOBJECT.setStatus("mandatory")
_OramodLockTYPE_Type = DisplayString
_OramodLockTYPE_Object = MibTableColumn
oramodLockTYPE = _OramodLockTYPE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 5),
    _OramodLockTYPE_Type()
)
oramodLockTYPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockTYPE.setStatus("mandatory")
_OramodLockMODE_Type = Integer32
_OramodLockMODE_Object = MibTableColumn
oramodLockMODE = _OramodLockMODE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 6),
    _OramodLockMODE_Type()
)
oramodLockMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockMODE.setStatus("mandatory")
_OramodLockCTIME_Type = Integer32
_OramodLockCTIME_Object = MibTableColumn
oramodLockCTIME = _OramodLockCTIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 7),
    _OramodLockCTIME_Type()
)
oramodLockCTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockCTIME.setStatus("mandatory")
_OramodLockBLOCK_Type = Integer32
_OramodLockBLOCK_Object = MibTableColumn
oramodLockBLOCK = _OramodLockBLOCK_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 1, 1, 1, 8),
    _OramodLockBLOCK_Type()
)
oramodLockBLOCK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLockBLOCK.setStatus("mandatory")
_OramodLatch_ObjectIdentity = ObjectIdentity
oramodLatch = _OramodLatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2)
)
_OramodLatchTable_Object = MibTable
oramodLatchTable = _OramodLatchTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1)
)
if mibBuilder.loadTexts:
    oramodLatchTable.setStatus("mandatory")
_OramodLatchEntry_Object = MibTableRow
oramodLatchEntry = _OramodLatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1)
)
oramodLatchEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodLatchSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodLatchLATCHINDX"),
)
if mibBuilder.loadTexts:
    oramodLatchEntry.setStatus("mandatory")
_OramodLatchSIDINDX_Type = Integer32
_OramodLatchSIDINDX_Object = MibTableColumn
oramodLatchSIDINDX = _OramodLatchSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 1),
    _OramodLatchSIDINDX_Type()
)
oramodLatchSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchSIDINDX.setStatus("mandatory")
_OramodLatchLATCHINDX_Type = Integer32
_OramodLatchLATCHINDX_Object = MibTableColumn
oramodLatchLATCHINDX = _OramodLatchLATCHINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 2),
    _OramodLatchLATCHINDX_Type()
)
oramodLatchLATCHINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchLATCHINDX.setStatus("mandatory")
_OramodLatchLATCHNUM_Type = Integer32
_OramodLatchLATCHNUM_Object = MibTableColumn
oramodLatchLATCHNUM = _OramodLatchLATCHNUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 3),
    _OramodLatchLATCHNUM_Type()
)
oramodLatchLATCHNUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchLATCHNUM.setStatus("mandatory")
_OramodLatchLATCHNAME_Type = DisplayString
_OramodLatchLATCHNAME_Object = MibTableColumn
oramodLatchLATCHNAME = _OramodLatchLATCHNAME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 4),
    _OramodLatchLATCHNAME_Type()
)
oramodLatchLATCHNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchLATCHNAME.setStatus("mandatory")
_OramodLatchGETS_Type = Counter32
_OramodLatchGETS_Object = MibTableColumn
oramodLatchGETS = _OramodLatchGETS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 5),
    _OramodLatchGETS_Type()
)
oramodLatchGETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchGETS.setStatus("mandatory")
_OramodLatchMISSES_Type = Counter32
_OramodLatchMISSES_Object = MibTableColumn
oramodLatchMISSES = _OramodLatchMISSES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 6),
    _OramodLatchMISSES_Type()
)
oramodLatchMISSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchMISSES.setStatus("mandatory")
_OramodLatchSLEEPS_Type = Counter32
_OramodLatchSLEEPS_Object = MibTableColumn
oramodLatchSLEEPS = _OramodLatchSLEEPS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 7),
    _OramodLatchSLEEPS_Type()
)
oramodLatchSLEEPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchSLEEPS.setStatus("mandatory")
_OramodLatchIMDGETS_Type = Counter32
_OramodLatchIMDGETS_Object = MibTableColumn
oramodLatchIMDGETS = _OramodLatchIMDGETS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 8),
    _OramodLatchIMDGETS_Type()
)
oramodLatchIMDGETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchIMDGETS.setStatus("mandatory")
_OramodLatchIMDMISSES_Type = Counter32
_OramodLatchIMDMISSES_Object = MibTableColumn
oramodLatchIMDMISSES = _OramodLatchIMDMISSES_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 9),
    _OramodLatchIMDMISSES_Type()
)
oramodLatchIMDMISSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchIMDMISSES.setStatus("mandatory")
_OramodLatchWAITSHOLDING_Type = Counter32
_OramodLatchWAITSHOLDING_Object = MibTableColumn
oramodLatchWAITSHOLDING = _OramodLatchWAITSHOLDING_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 10),
    _OramodLatchWAITSHOLDING_Type()
)
oramodLatchWAITSHOLDING.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchWAITSHOLDING.setStatus("mandatory")
_OramodLatchSPINGETS_Type = Counter32
_OramodLatchSPINGETS_Object = MibTableColumn
oramodLatchSPINGETS = _OramodLatchSPINGETS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 9, 2, 1, 1, 11),
    _OramodLatchSPINGETS_Type()
)
oramodLatchSPINGETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodLatchSPINGETS.setStatus("mandatory")
_OramodBackups_ObjectIdentity = ObjectIdentity
oramodBackups = _OramodBackups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10)
)
_OramodBackup_ObjectIdentity = ObjectIdentity
oramodBackup = _OramodBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1)
)
_OramodBackupTable_Object = MibTable
oramodBackupTable = _OramodBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1)
)
if mibBuilder.loadTexts:
    oramodBackupTable.setStatus("mandatory")
_OramodBackupEntry_Object = MibTableRow
oramodBackupEntry = _OramodBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1)
)
oramodBackupEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodBackupSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodBackupFILENUM"),
)
if mibBuilder.loadTexts:
    oramodBackupEntry.setStatus("mandatory")
_OramodBackupSIDINDX_Type = Integer32
_OramodBackupSIDINDX_Object = MibTableColumn
oramodBackupSIDINDX = _OramodBackupSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1, 1),
    _OramodBackupSIDINDX_Type()
)
oramodBackupSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodBackupSIDINDX.setStatus("mandatory")
_OramodBackupFILENUM_Type = Integer32
_OramodBackupFILENUM_Object = MibTableColumn
oramodBackupFILENUM = _OramodBackupFILENUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1, 2),
    _OramodBackupFILENUM_Type()
)
oramodBackupFILENUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodBackupFILENUM.setStatus("mandatory")
_OramodBackupSTATUS_Type = DisplayString
_OramodBackupSTATUS_Object = MibTableColumn
oramodBackupSTATUS = _OramodBackupSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1, 3),
    _OramodBackupSTATUS_Type()
)
oramodBackupSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodBackupSTATUS.setStatus("mandatory")
_OramodBackupCHANGENUM_Type = Integer32
_OramodBackupCHANGENUM_Object = MibTableColumn
oramodBackupCHANGENUM = _OramodBackupCHANGENUM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1, 4),
    _OramodBackupCHANGENUM_Type()
)
oramodBackupCHANGENUM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodBackupCHANGENUM.setStatus("mandatory")
_OramodBackupDATE_Type = DisplayString
_OramodBackupDATE_Object = MibTableColumn
oramodBackupDATE = _OramodBackupDATE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 10, 1, 1, 1, 5),
    _OramodBackupDATE_Type()
)
oramodBackupDATE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodBackupDATE.setStatus("mandatory")
_OramodArchive_ObjectIdentity = ObjectIdentity
oramodArchive = _OramodArchive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11)
)
_OramodArcDest_ObjectIdentity = ObjectIdentity
oramodArcDest = _OramodArcDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1)
)
_OramodArcDestTable_Object = MibTable
oramodArcDestTable = _OramodArcDestTable_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1)
)
if mibBuilder.loadTexts:
    oramodArcDestTable.setStatus("mandatory")
_OramodArcDestEntry_Object = MibTableRow
oramodArcDestEntry = _OramodArcDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1)
)
oramodArcDestEntry.setIndexNames(
    (0, "EMPIRE-ORAMOD", "oramodArcDestSIDINDX"),
    (0, "EMPIRE-ORAMOD", "oramodArcDestARCINDX"),
)
if mibBuilder.loadTexts:
    oramodArcDestEntry.setStatus("mandatory")
_OramodArcDestSIDINDX_Type = Integer32
_OramodArcDestSIDINDX_Object = MibTableColumn
oramodArcDestSIDINDX = _OramodArcDestSIDINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1, 1),
    _OramodArcDestSIDINDX_Type()
)
oramodArcDestSIDINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodArcDestSIDINDX.setStatus("mandatory")
_OramodArcDestARCINDX_Type = Integer32
_OramodArcDestARCINDX_Object = MibTableColumn
oramodArcDestARCINDX = _OramodArcDestARCINDX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1, 2),
    _OramodArcDestARCINDX_Type()
)
oramodArcDestARCINDX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodArcDestARCINDX.setStatus("mandatory")
_OramodArcDestARCMODE_Type = DisplayString
_OramodArcDestARCMODE_Object = MibTableColumn
oramodArcDestARCMODE = _OramodArcDestARCMODE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1, 3),
    _OramodArcDestARCMODE_Type()
)
oramodArcDestARCMODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodArcDestARCMODE.setStatus("mandatory")
_OramodArcDestSTATUS_Type = DisplayString
_OramodArcDestSTATUS_Object = MibTableColumn
oramodArcDestSTATUS = _OramodArcDestSTATUS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1, 4),
    _OramodArcDestSTATUS_Type()
)
oramodArcDestSTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodArcDestSTATUS.setStatus("mandatory")
_OramodArcDestDEST_Type = DisplayString
_OramodArcDestDEST_Object = MibTableColumn
oramodArcDestDEST = _OramodArcDestDEST_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 11, 11, 1, 1, 1, 5),
    _OramodArcDestDEST_Type()
)
oramodArcDestDEST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodArcDestDEST.setStatus("mandatory")
_OramodTtlFootprt_ObjectIdentity = ObjectIdentity
oramodTtlFootprt = _OramodTtlFootprt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12)
)
_OramodTtlCPUTIME_Type = Integer32
_OramodTtlCPUTIME_Object = MibScalar
oramodTtlCPUTIME = _OramodTtlCPUTIME_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 1),
    _OramodTtlCPUTIME_Type()
)
oramodTtlCPUTIME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlCPUTIME.setStatus("mandatory")


class _OramodTtlPERCENTCPU_Type(Integer32):
    """Custom type oramodTtlPERCENTCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OramodTtlPERCENTCPU_Type.__name__ = "Integer32"
_OramodTtlPERCENTCPU_Object = MibScalar
oramodTtlPERCENTCPU = _OramodTtlPERCENTCPU_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 2),
    _OramodTtlPERCENTCPU_Type()
)
oramodTtlPERCENTCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlPERCENTCPU.setStatus("mandatory")
_OramodTtlMEMSIZE_Type = Gauge32
_OramodTtlMEMSIZE_Object = MibScalar
oramodTtlMEMSIZE = _OramodTtlMEMSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 3),
    _OramodTtlMEMSIZE_Type()
)
oramodTtlMEMSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlMEMSIZE.setStatus("mandatory")
_OramodTtlRSS_Type = Gauge32
_OramodTtlRSS_Object = MibScalar
oramodTtlRSS = _OramodTtlRSS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 4),
    _OramodTtlRSS_Type()
)
oramodTtlRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlRSS.setStatus("mandatory")


class _OramodTtlPERCENTMEM_Type(Integer32):
    """Custom type oramodTtlPERCENTMEM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OramodTtlPERCENTMEM_Type.__name__ = "Integer32"
_OramodTtlPERCENTMEM_Object = MibScalar
oramodTtlPERCENTMEM = _OramodTtlPERCENTMEM_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 5),
    _OramodTtlPERCENTMEM_Type()
)
oramodTtlPERCENTMEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlPERCENTMEM.setStatus("mandatory")
_OramodTtlTHREADS_Type = Gauge32
_OramodTtlTHREADS_Object = MibScalar
oramodTtlTHREADS = _OramodTtlTHREADS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 6),
    _OramodTtlTHREADS_Type()
)
oramodTtlTHREADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlTHREADS.setStatus("mandatory")
_OramodTtlINBLKS_Type = Gauge32
_OramodTtlINBLKS_Object = MibScalar
oramodTtlINBLKS = _OramodTtlINBLKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 7),
    _OramodTtlINBLKS_Type()
)
oramodTtlINBLKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlINBLKS.setStatus("mandatory")
_OramodTtlOUTBLKS_Type = Gauge32
_OramodTtlOUTBLKS_Object = MibScalar
oramodTtlOUTBLKS = _OramodTtlOUTBLKS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 8),
    _OramodTtlOUTBLKS_Type()
)
oramodTtlOUTBLKS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlOUTBLKS.setStatus("mandatory")
_OramodTtlMSGSSENT_Type = Counter32
_OramodTtlMSGSSENT_Object = MibScalar
oramodTtlMSGSSENT = _OramodTtlMSGSSENT_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 9),
    _OramodTtlMSGSSENT_Type()
)
oramodTtlMSGSSENT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlMSGSSENT.setStatus("mandatory")
_OramodTtlMSGSRCVD_Type = Counter32
_OramodTtlMSGSRCVD_Object = MibScalar
oramodTtlMSGSRCVD = _OramodTtlMSGSRCVD_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 10),
    _OramodTtlMSGSRCVD_Type()
)
oramodTtlMSGSRCVD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlMSGSRCVD.setStatus("mandatory")
_OramodTtlSYSCALLS_Type = Counter32
_OramodTtlSYSCALLS_Object = MibScalar
oramodTtlSYSCALLS = _OramodTtlSYSCALLS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 11),
    _OramodTtlSYSCALLS_Type()
)
oramodTtlSYSCALLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlSYSCALLS.setStatus("mandatory")
_OramodTtlMINORPGFLTS_Type = Counter32
_OramodTtlMINORPGFLTS_Object = MibScalar
oramodTtlMINORPGFLTS = _OramodTtlMINORPGFLTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 12),
    _OramodTtlMINORPGFLTS_Type()
)
oramodTtlMINORPGFLTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlMINORPGFLTS.setStatus("mandatory")
_OramodTtlMAJORPGFLTS_Type = Counter32
_OramodTtlMAJORPGFLTS_Object = MibScalar
oramodTtlMAJORPGFLTS = _OramodTtlMAJORPGFLTS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 13),
    _OramodTtlMAJORPGFLTS_Type()
)
oramodTtlMAJORPGFLTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlMAJORPGFLTS.setStatus("mandatory")
_OramodTtlNUMSWAPS_Type = Counter32
_OramodTtlNUMSWAPS_Object = MibScalar
oramodTtlNUMSWAPS = _OramodTtlNUMSWAPS_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 14),
    _OramodTtlNUMSWAPS_Type()
)
oramodTtlNUMSWAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlNUMSWAPS.setStatus("mandatory")
_OramodTtlVOLCNTX_Type = Counter32
_OramodTtlVOLCNTX_Object = MibScalar
oramodTtlVOLCNTX = _OramodTtlVOLCNTX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 15),
    _OramodTtlVOLCNTX_Type()
)
oramodTtlVOLCNTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlVOLCNTX.setStatus("mandatory")
_OramodTtlINVOLCNTX_Type = Counter32
_OramodTtlINVOLCNTX_Object = MibScalar
oramodTtlINVOLCNTX = _OramodTtlINVOLCNTX_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 16),
    _OramodTtlINVOLCNTX_Type()
)
oramodTtlINVOLCNTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlINVOLCNTX.setStatus("mandatory")
_OramodTtlDISKSIZE_Type = Integer32
_OramodTtlDISKSIZE_Object = MibScalar
oramodTtlDISKSIZE = _OramodTtlDISKSIZE_Object(
    (1, 3, 6, 1, 4, 1, 546, 16, 4, 12, 17),
    _OramodTtlDISKSIZE_Type()
)
oramodTtlDISKSIZE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oramodTtlDISKSIZE.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMPIRE-ORAMOD",
    **{"empire": empire,
       "applications": applications,
       "oracledb": oracledb,
       "oraModVersion": oraModVersion,
       "oraModMode": oraModMode,
       "oraFlag": oraFlag,
       "oramodCfg": oramodCfg,
       "oramodDbCfg": oramodDbCfg,
       "oramodDbCfgTable": oramodDbCfgTable,
       "oramodDbCfgEntry": oramodDbCfgEntry,
       "oramodDbCfgSIDINDX": oramodDbCfgSIDINDX,
       "oramodDbCfgSID": oramodDbCfgSID,
       "oramodDbCfgVERSION": oramodDbCfgVERSION,
       "oramodDbCfgHOME": oramodDbCfgHOME,
       "oramodDbCfgBASE": oramodDbCfgBASE,
       "oramodDbCfgID": oramodDbCfgID,
       "oramodDbCfgCRTDT": oramodDbCfgCRTDT,
       "oramodDbCfgLOGMODE": oramodDbCfgLOGMODE,
       "oramodDbCfgCTRLFILETYPE": oramodDbCfgCTRLFILETYPE,
       "oramodDbCfgOPENMODE": oramodDbCfgOPENMODE,
       "oramodDbCfgMAXPROCESS": oramodDbCfgMAXPROCESS,
       "oramodDbCfgMAXSESSION": oramodDbCfgMAXSESSION,
       "oramodDbCfgTIMEDSTATISTICS": oramodDbCfgTIMEDSTATISTICS,
       "oramodDbCfgCPUCNT": oramodDbCfgCPUCNT,
       "oramodDbCfgSHAREDPOOLSIZE": oramodDbCfgSHAREDPOOLSIZE,
       "oramodDbCfgSHAREDPOOLRSSIZE": oramodDbCfgSHAREDPOOLRSSIZE,
       "oramodDbCfgLARGEPOOLSIZE": oramodDbCfgLARGEPOOLSIZE,
       "oramodDbCfgJAVAPOOLSIZE": oramodDbCfgJAVAPOOLSIZE,
       "oramodDbCfgCNTRLFILES": oramodDbCfgCNTRLFILES,
       "oramodDbCfgDBBLKBUFF": oramodDbCfgDBBLKBUFF,
       "oramodDbCfgDBBLKSIZE": oramodDbCfgDBBLKSIZE,
       "oramodDbCfgCKPTINTRVL": oramodDbCfgCKPTINTRVL,
       "oramodDbCfgDBFILES": oramodDbCfgDBFILES,
       "oramodDbCfgSORTAREASIZE": oramodDbCfgSORTAREASIZE,
       "oramodDbCfgOPENCURSORS": oramodDbCfgOPENCURSORS,
       "oramodDbCfgTRNSACTNS": oramodDbCfgTRNSACTNS,
       "oramodDbCfgTRNSACTNSPERSEG": oramodDbCfgTRNSACTNSPERSEG,
       "oramodDbCfgMAXROLLSEG": oramodDbCfgMAXROLLSEG,
       "oramodCfgDf": oramodCfgDf,
       "oramodCfgDfTable": oramodCfgDfTable,
       "oramodCfgDfEntry": oramodCfgDfEntry,
       "oramodCfgDfSIDINDX": oramodCfgDfSIDINDX,
       "oramodCfgDfFILENUM": oramodCfgDfFILENUM,
       "oramodCfgDfSTATUS": oramodCfgDfSTATUS,
       "oramodCfgDfENABLED": oramodCfgDfENABLED,
       "oramodCfgDfUNRCVRBLECHG": oramodCfgDfUNRCVRBLECHG,
       "oramodCfgDfUNRCVRBLETIME": oramodCfgDfUNRCVRBLETIME,
       "oramodCfgDfKBYTES": oramodCfgDfKBYTES,
       "oramodCfgDfCRTKBYTES": oramodCfgDfCRTKBYTES,
       "oramodCfgDfFNAME": oramodCfgDfFNAME,
       "oramodCfgDfCRTTIME": oramodCfgDfCRTTIME,
       "oramodCfgDfTBLESPACENUM": oramodCfgDfTBLESPACENUM,
       "oramodCfgDfTBLESPACERFILENUM": oramodCfgDfTBLESPACERFILENUM,
       "oramodCfgDfBLOCKS": oramodCfgDfBLOCKS,
       "oramodCfgDfBLOCKSIZE": oramodCfgDfBLOCKSIZE,
       "oramodCfgDfERROR": oramodCfgDfERROR,
       "oramodCfgDfRECOVER": oramodCfgDfRECOVER,
       "oramodCfgDfRSTLOGSCHGNUM": oramodCfgDfRSTLOGSCHGNUM,
       "oramodCfgDfRSTLOGSTIME": oramodCfgDfRSTLOGSTIME,
       "oramodCfgLf": oramodCfgLf,
       "oramodCfgLfTable": oramodCfgLfTable,
       "oramodCfgLfEntry": oramodCfgLfEntry,
       "oramodCfgLfSIDINDX": oramodCfgLfSIDINDX,
       "oramodCfgLfMEMBERINDX": oramodCfgLfMEMBERINDX,
       "oramodCfgLfGROUPNUM": oramodCfgLfGROUPNUM,
       "oramodCfgLfSTATUS": oramodCfgLfSTATUS,
       "oramodCfgLfMEMBER": oramodCfgLfMEMBER,
       "oramodCfgSga": oramodCfgSga,
       "oramodCfgSgaTable": oramodCfgSgaTable,
       "oramodCfgSgaEntry": oramodCfgSgaEntry,
       "oramodCfgSgaSIDINDX": oramodCfgSgaSIDINDX,
       "oramodCfgSgaTOTALMEMALLOC": oramodCfgSgaTOTALMEMALLOC,
       "oramodCfgSgaFIXEDSGA": oramodCfgSgaFIXEDSGA,
       "oramodCfgSgaVARIABLE": oramodCfgSgaVARIABLE,
       "oramodCfgSgaDBBUFF": oramodCfgSgaDBBUFF,
       "oramodCfgSgaREDOBUFF": oramodCfgSgaREDOBUFF,
       "oramodPerf": oramodPerf,
       "oramodFootprint": oramodFootprint,
       "oramodFootprt": oramodFootprt,
       "oramodFootprtTable": oramodFootprtTable,
       "oramodFootprtEntry": oramodFootprtEntry,
       "oramodFootprtSIDINDX": oramodFootprtSIDINDX,
       "oramodFootprtCPUTIME": oramodFootprtCPUTIME,
       "oramodFootprtPERCENTCPU": oramodFootprtPERCENTCPU,
       "oramodFootprtMEMSIZE": oramodFootprtMEMSIZE,
       "oramodFootprtRSS": oramodFootprtRSS,
       "oramodFootprtPERCENTMEM": oramodFootprtPERCENTMEM,
       "oramodFootprtTHREADS": oramodFootprtTHREADS,
       "oramodFootprtINBLKS": oramodFootprtINBLKS,
       "oramodFootprtOUTBLKS": oramodFootprtOUTBLKS,
       "oramodFootprtMSGSSENT": oramodFootprtMSGSSENT,
       "oramodFootprtMSGSRCVD": oramodFootprtMSGSRCVD,
       "oramodFootprtSYSCALLS": oramodFootprtSYSCALLS,
       "oramodFootprtMINORPGFLTS": oramodFootprtMINORPGFLTS,
       "oramodFootprtMAJORPGFLTS": oramodFootprtMAJORPGFLTS,
       "oramodFootprtNUMSWAPS": oramodFootprtNUMSWAPS,
       "oramodFootprtVOLCNTX": oramodFootprtVOLCNTX,
       "oramodFootprtINVOLCNTX": oramodFootprtINVOLCNTX,
       "oramodFootprtHOMESIZE": oramodFootprtHOMESIZE,
       "oramodFootprtDBDISKSIZE": oramodFootprtDBDISKSIZE,
       "oramodFootprtLASTUPDATE": oramodFootprtLASTUPDATE,
       "oramodFFootprt": oramodFFootprt,
       "oramodFFootprtTable": oramodFFootprtTable,
       "oramodFFootprtEntry": oramodFFootprtEntry,
       "oramodFFootprtSIDINDX": oramodFFootprtSIDINDX,
       "oramodFFootprtFILEINDX": oramodFFootprtFILEINDX,
       "oramodFFootprtFILETYPE": oramodFFootprtFILETYPE,
       "oramodFFootprtFILENAME": oramodFFootprtFILENAME,
       "oramodFFootprtCRTTS": oramodFFootprtCRTTS,
       "oramodFFootprtCRTKBYTES": oramodFFootprtCRTKBYTES,
       "oramodFFootprtKBYTES": oramodFFootprtKBYTES,
       "oramodFFootprtBLOCKS": oramodFFootprtBLOCKS,
       "oramodFFootprtSTATUS": oramodFFootprtSTATUS,
       "oramodFFootprtRECOVER": oramodFFootprtRECOVER,
       "oramodFFootprtAVGIOTIM": oramodFFootprtAVGIOTIM,
       "oramodMetrics": oramodMetrics,
       "oramodMetricsTable": oramodMetricsTable,
       "oramodMetricsEntry": oramodMetricsEntry,
       "oramodMetricsSIDINDX": oramodMetricsSIDINDX,
       "oramodMetricsBCPT": oramodMetricsBCPT,
       "oramodMetricsBGR": oramodMetricsBGR,
       "oramodMetricsBVPT": oramodMetricsBVPT,
       "oramodMetricsCHR": oramodMetricsCHR,
       "oramodMetricsCR": oramodMetricsCR,
       "oramodMetricsCPT": oramodMetricsCPT,
       "oramodMetricsCBR": oramodMetricsCBR,
       "oramodMetricsCCR": oramodMetricsCCR,
       "oramodMetricsCRR": oramodMetricsCRR,
       "oramodMetricsLCM": oramodMetricsLCM,
       "oramodMetricsRTUC": oramodMetricsRTUC,
       "oramodMetricsRLSW": oramodMetricsRLSW,
       "oramodMetricsRSR": oramodMetricsRSR,
       "oramodMetricsSOR": oramodMetricsSOR,
       "oramodMetricsTRR": oramodMetricsTRR,
       "oramodMetricsUCR": oramodMetricsUCR,
       "oramodMetricsUCPP": oramodMetricsUCPP,
       "oramodMetricsURR": oramodMetricsURR,
       "oramodMetricsSGALCE": oramodMetricsSGALCE,
       "oramodMetricsSGADDCE": oramodMetricsSGADDCE,
       "oramodMetricsDBTOTALRW": oramodMetricsDBTOTALRW,
       "oramodMetricsDBBLKCHG": oramodMetricsDBBLKCHG,
       "oramodMetricsDBBLKGET": oramodMetricsDBBLKGET,
       "oramodMetricsDBCNSTGET": oramodMetricsDBCNSTGET,
       "oramodMetricsDBPHYSREAD": oramodMetricsDBPHYSREAD,
       "oramodMetricsDBSORTDISK": oramodMetricsDBSORTDISK,
       "oramodMetricsDBSORTMEM": oramodMetricsDBSORTMEM,
       "oramodMetricsBLKFREEWAIT": oramodMetricsBLKFREEWAIT,
       "oramodMetricsMTHRDQUEUEWAIT": oramodMetricsMTHRDQUEUEWAIT,
       "oramodMetricsSESSHIWTRMEM": oramodMetricsSESSHIWTRMEM,
       "oramodMetricsSESSCURRMEM": oramodMetricsSESSCURRMEM,
       "oramodMetricsSESSHIWTR": oramodMetricsSESSHIWTR,
       "oramodMetricsSESSCURRENT": oramodMetricsSESSCURRENT,
       "oramodMetricsUSERCOMMITS": oramodMetricsUSERCOMMITS,
       "oramodMetricsUSERROLLBACK": oramodMetricsUSERROLLBACK,
       "oramodMetricsUSERCALLS": oramodMetricsUSERCALLS,
       "oramodMetricsDBPHYSWRTS": oramodMetricsDBPHYSWRTS,
       "oramodMetricsTBLSCANROWS": oramodMetricsTBLSCANROWS,
       "oramodMetricsTBLFTCHROWID": oramodMetricsTBLFTCHROWID,
       "oramodMetricsTBLFTCHCROW": oramodMetricsTBLFTCHCROW,
       "oramodMetricsRECRSVCALLS": oramodMetricsRECRSVCALLS,
       "oramodMetricsCNSTCHGS": oramodMetricsCNSTCHGS,
       "oramodMetricsPARSECNT": oramodMetricsPARSECNT,
       "oramodMetricsCPUTM": oramodMetricsCPUTM,
       "oramodMetricsLOGFILESWTCH": oramodMetricsLOGFILESWTCH,
       "oramodMetricsARCHIVER": oramodMetricsARCHIVER,
       "oramodMetricsDATABASESTATUS": oramodMetricsDATABASESTATUS,
       "oramodMetricsSHUTDOWNPENDING": oramodMetricsSHUTDOWNPENDING,
       "oramodMetricsLASTUPDATE": oramodMetricsLASTUPDATE,
       "oramodSGA": oramodSGA,
       "oramodSgaDddAgg": oramodSgaDddAgg,
       "oramodSgaDddAggTable": oramodSgaDddAggTable,
       "oramodSgaDddAggEntry": oramodSgaDddAggEntry,
       "oramodSGAAGGSIDINDX": oramodSGAAGGSIDINDX,
       "oramodSGAAGGCNT": oramodSGAAGGCNT,
       "oramodSGAAGGUSGE": oramodSGAAGGUSGE,
       "oramodSGAAGGFIX": oramodSGAAGGFIX,
       "oramodSGAAGGGET": oramodSGAAGGGET,
       "oramodSGAAGGGETMISS": oramodSGAAGGGETMISS,
       "oramodSGAAGGSCAN": oramodSGAAGGSCAN,
       "oramodSGAAGGSCANMISS": oramodSGAAGGSCANMISS,
       "oramodSGAAGGSCANCPLT": oramodSGAAGGSCANCPLT,
       "oramodSGAAGGMODS": oramodSGAAGGMODS,
       "oramodSGAAGGFLUSH": oramodSGAAGGFLUSH,
       "oramodSgaDlci": oramodSgaDlci,
       "oramodSgaDlciTable": oramodSgaDlciTable,
       "oramodSgaDlciEntry": oramodSgaDlciEntry,
       "oramodSGADLCISIDINDX": oramodSGADLCISIDINDX,
       "oramodSGADLCIINDX": oramodSGADLCIINDX,
       "oramodSGADLCINAME": oramodSGADLCINAME,
       "oramodSGADLCIGET": oramodSGADLCIGET,
       "oramodSGADLCIGETHIT": oramodSGADLCIGETHIT,
       "oramodSGADLCIGETHITRT": oramodSGADLCIGETHITRT,
       "oramodSGADLCIPIN": oramodSGADLCIPIN,
       "oramodSGADLCIPINHIT": oramodSGADLCIPINHIT,
       "oramodSGADLCIPINHITRT": oramodSGADLCIPINHITRT,
       "oramodSGADLCIRELOAD": oramodSGADLCIRELOAD,
       "oramodSGADLCIINVALID": oramodSGADLCIINVALID,
       "oramodRedoLogBuf": oramodRedoLogBuf,
       "oramodRedoLogBufTable": oramodRedoLogBufTable,
       "oramodRedoLogBufEntry": oramodRedoLogBufEntry,
       "oramodREDOSIDINDX": oramodREDOSIDINDX,
       "oramodREDOBLKWRT": oramodREDOBLKWRT,
       "oramodREDOENTRIES": oramodREDOENTRIES,
       "oramodREDOSIZE": oramodREDOSIZE,
       "oramodREDOSPACERQST": oramodREDOSPACERQST,
       "oramodREDOSPACEWAIT": oramodREDOSPACEWAIT,
       "oramodREDOSYNCHWRT": oramodREDOSYNCHWRT,
       "oramodREDOSYNCHTM": oramodREDOSYNCHTM,
       "oramodREDOWASTAGE": oramodREDOWASTAGE,
       "oramodREDORETRIES": oramodREDORETRIES,
       "oramodREDOLASTUPDATE": oramodREDOLASTUPDATE,
       "oramodRollBack": oramodRollBack,
       "oramodRollBackTable": oramodRollBackTable,
       "oramodRollBackEntry": oramodRollBackEntry,
       "oramodRollBackSIDINDX": oramodRollBackSIDINDX,
       "oramodRollBackSEGINDX": oramodRollBackSEGINDX,
       "oramodRollBackSEGNAME": oramodRollBackSEGNAME,
       "oramodRollBackEXTENTS": oramodRollBackEXTENTS,
       "oramodRollBackRSSIZE": oramodRollBackRSSIZE,
       "oramodRollBackWRITES": oramodRollBackWRITES,
       "oramodRollBackGETS": oramodRollBackGETS,
       "oramodRollBackWAITS": oramodRollBackWAITS,
       "oramodRollBackOPTSIZE": oramodRollBackOPTSIZE,
       "oramodRollBackSHRINKS": oramodRollBackSHRINKS,
       "oramodRollBackWRAPS": oramodRollBackWRAPS,
       "oramodRollBackEXTENDS": oramodRollBackEXTENDS,
       "oramodRollBackAVESHRINK": oramodRollBackAVESHRINK,
       "oramodRollBackAVEACTIVE": oramodRollBackAVEACTIVE,
       "oramodRollBackSTATUS": oramodRollBackSTATUS,
       "oramodWaits": oramodWaits,
       "oramodWaitsTable": oramodWaitsTable,
       "oramodWaitsEntry": oramodWaitsEntry,
       "oramodWaitsSIDINDX": oramodWaitsSIDINDX,
       "oramodWaitsEVENTINDX": oramodWaitsEVENTINDX,
       "oramodWaitsEVENT": oramodWaitsEVENT,
       "oramodWaitsTOTALWAITS": oramodWaitsTOTALWAITS,
       "oramodWaitsTOTALTIMOUT": oramodWaitsTOTALTIMOUT,
       "oramodWaitsTIMEWAITED": oramodWaitsTIMEWAITED,
       "oramodWaitsAVGWAIT": oramodWaitsAVGWAIT,
       "oramodExpSql": oramodExpSql,
       "oramodExpSqlTable": oramodExpSqlTable,
       "oramodExpSqlEntry": oramodExpSqlEntry,
       "oramodExpSqlSIDINDX": oramodExpSqlSIDINDX,
       "oramodExpSqlSQLINDX": oramodExpSqlSQLINDX,
       "oramodExpSqlEXECUTION": oramodExpSqlEXECUTION,
       "oramodExpSqlDISKREAD": oramodExpSqlDISKREAD,
       "oramodExpSqlPARSECNT": oramodExpSqlPARSECNT,
       "oramodExpSqlBUFFGETS": oramodExpSqlBUFFGETS,
       "oramodExpSqlSORTS": oramodExpSqlSORTS,
       "oramodExpSqlSQL": oramodExpSqlSQL,
       "oramodTblsp": oramodTblsp,
       "oramodTblspTable": oramodTblspTable,
       "oramodTblspEntry": oramodTblspEntry,
       "oramodTblspSIDINDX": oramodTblspSIDINDX,
       "oramodTblspTBLSPINDX": oramodTblspTBLSPINDX,
       "oramodTblspTBLSPNAME": oramodTblspTBLSPNAME,
       "oramodTblspFILENAME": oramodTblspFILENAME,
       "oramodTblspEXTENTS": oramodTblspEXTENTS,
       "oramodTblspLRGEXTENT": oramodTblspLRGEXTENT,
       "oramodTblspSMEXTENT": oramodTblspSMEXTENT,
       "oramodTblspINCREMENTBY": oramodTblspINCREMENTBY,
       "oramodTblspBYTESCOALSD": oramodTblspBYTESCOALSD,
       "oramodTblspBYTESFREE": oramodTblspBYTESFREE,
       "oramodLocks": oramodLocks,
       "oramodLock": oramodLock,
       "oramodLockTable": oramodLockTable,
       "oramodLockEntry": oramodLockEntry,
       "oramodLockSIDINDX": oramodLockSIDINDX,
       "oramodLockUSERINDX": oramodLockUSERINDX,
       "oramodLockUSERNAME": oramodLockUSERNAME,
       "oramodLockOBJECT": oramodLockOBJECT,
       "oramodLockTYPE": oramodLockTYPE,
       "oramodLockMODE": oramodLockMODE,
       "oramodLockCTIME": oramodLockCTIME,
       "oramodLockBLOCK": oramodLockBLOCK,
       "oramodLatch": oramodLatch,
       "oramodLatchTable": oramodLatchTable,
       "oramodLatchEntry": oramodLatchEntry,
       "oramodLatchSIDINDX": oramodLatchSIDINDX,
       "oramodLatchLATCHINDX": oramodLatchLATCHINDX,
       "oramodLatchLATCHNUM": oramodLatchLATCHNUM,
       "oramodLatchLATCHNAME": oramodLatchLATCHNAME,
       "oramodLatchGETS": oramodLatchGETS,
       "oramodLatchMISSES": oramodLatchMISSES,
       "oramodLatchSLEEPS": oramodLatchSLEEPS,
       "oramodLatchIMDGETS": oramodLatchIMDGETS,
       "oramodLatchIMDMISSES": oramodLatchIMDMISSES,
       "oramodLatchWAITSHOLDING": oramodLatchWAITSHOLDING,
       "oramodLatchSPINGETS": oramodLatchSPINGETS,
       "oramodBackups": oramodBackups,
       "oramodBackup": oramodBackup,
       "oramodBackupTable": oramodBackupTable,
       "oramodBackupEntry": oramodBackupEntry,
       "oramodBackupSIDINDX": oramodBackupSIDINDX,
       "oramodBackupFILENUM": oramodBackupFILENUM,
       "oramodBackupSTATUS": oramodBackupSTATUS,
       "oramodBackupCHANGENUM": oramodBackupCHANGENUM,
       "oramodBackupDATE": oramodBackupDATE,
       "oramodArchive": oramodArchive,
       "oramodArcDest": oramodArcDest,
       "oramodArcDestTable": oramodArcDestTable,
       "oramodArcDestEntry": oramodArcDestEntry,
       "oramodArcDestSIDINDX": oramodArcDestSIDINDX,
       "oramodArcDestARCINDX": oramodArcDestARCINDX,
       "oramodArcDestARCMODE": oramodArcDestARCMODE,
       "oramodArcDestSTATUS": oramodArcDestSTATUS,
       "oramodArcDestDEST": oramodArcDestDEST,
       "oramodTtlFootprt": oramodTtlFootprt,
       "oramodTtlCPUTIME": oramodTtlCPUTIME,
       "oramodTtlPERCENTCPU": oramodTtlPERCENTCPU,
       "oramodTtlMEMSIZE": oramodTtlMEMSIZE,
       "oramodTtlRSS": oramodTtlRSS,
       "oramodTtlPERCENTMEM": oramodTtlPERCENTMEM,
       "oramodTtlTHREADS": oramodTtlTHREADS,
       "oramodTtlINBLKS": oramodTtlINBLKS,
       "oramodTtlOUTBLKS": oramodTtlOUTBLKS,
       "oramodTtlMSGSSENT": oramodTtlMSGSSENT,
       "oramodTtlMSGSRCVD": oramodTtlMSGSRCVD,
       "oramodTtlSYSCALLS": oramodTtlSYSCALLS,
       "oramodTtlMINORPGFLTS": oramodTtlMINORPGFLTS,
       "oramodTtlMAJORPGFLTS": oramodTtlMAJORPGFLTS,
       "oramodTtlNUMSWAPS": oramodTtlNUMSWAPS,
       "oramodTtlVOLCNTX": oramodTtlVOLCNTX,
       "oramodTtlINVOLCNTX": oramodTtlINVOLCNTX,
       "oramodTtlDISKSIZE": oramodTtlDISKSIZE}
)
