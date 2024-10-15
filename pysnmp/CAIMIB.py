# SNMP MIB module (CAIMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAIMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:18 2024
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

_Cai_ObjectIdentity = ObjectIdentity
cai = _Cai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791)
)
_CaiSysMgt_ObjectIdentity = ObjectIdentity
caiSysMgt = _CaiSysMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2)
)
_CaiUnicenter_ObjectIdentity = ObjectIdentity
caiUnicenter = _CaiUnicenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 2)
)


class _CaiUniGenlvl_Type(DisplayString):
    """Custom type caiUniGenlvl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CaiUniGenlvl_Type.__name__ = "DisplayString"
_CaiUniGenlvl_Object = MibScalar
caiUniGenlvl = _CaiUniGenlvl_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 2),
    _CaiUniGenlvl_Type()
)
caiUniGenlvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniGenlvl.setStatus("mandatory")


class _CaiUniConfig_Type(DisplayString):
    """Custom type caiUniConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CaiUniConfig_Type.__name__ = "DisplayString"
_CaiUniConfig_Object = MibScalar
caiUniConfig = _CaiUniConfig_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 3),
    _CaiUniConfig_Type()
)
caiUniConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniConfig.setStatus("mandatory")


class _CaiUniLicExp_Type(DisplayString):
    """Custom type caiUniLicExp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CaiUniLicExp_Type.__name__ = "DisplayString"
_CaiUniLicExp_Object = MibScalar
caiUniLicExp = _CaiUniLicExp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 4),
    _CaiUniLicExp_Type()
)
caiUniLicExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniLicExp.setStatus("mandatory")


class _CaiUniLstMsg_Type(DisplayString):
    """Custom type caiUniLstMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CaiUniLstMsg_Type.__name__ = "DisplayString"
_CaiUniLstMsg_Object = MibScalar
caiUniLstMsg = _CaiUniLstMsg_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 5),
    _CaiUniLstMsg_Type()
)
caiUniLstMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniLstMsg.setStatus("mandatory")


class _CaiUniCltSrv_Type(Integer32):
    """Custom type caiUniCltSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2),
          ("standalone", 3))
    )


_CaiUniCltSrv_Type.__name__ = "Integer32"
_CaiUniCltSrv_Object = MibScalar
caiUniCltSrv = _CaiUniCltSrv_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 6),
    _CaiUniCltSrv_Type()
)
caiUniCltSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniCltSrv.setStatus("mandatory")
_CaiUniStatTable_Object = MibTable
caiUniStatTable = _CaiUniStatTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 7)
)
if mibBuilder.loadTexts:
    caiUniStatTable.setStatus("mandatory")
_CaiUniStatEntry_Object = MibTableRow
caiUniStatEntry = _CaiUniStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2)
)
caiUniStatEntry.setIndexNames(
    (0, "CAIMIB", "caiUniStatEntIdx"),
)
if mibBuilder.loadTexts:
    caiUniStatEntry.setStatus("mandatory")
_CaiUniStatEntIdx_Type = Integer32
_CaiUniStatEntIdx_Object = MibTableColumn
caiUniStatEntIdx = _CaiUniStatEntIdx_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2, 2),
    _CaiUniStatEntIdx_Type()
)
caiUniStatEntIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniStatEntIdx.setStatus("mandatory")


class _CaiUniStatComp_Type(DisplayString):
    """Custom type caiUniStatComp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CaiUniStatComp_Type.__name__ = "DisplayString"
_CaiUniStatComp_Object = MibTableColumn
caiUniStatComp = _CaiUniStatComp_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 2, 7, 2, 3),
    _CaiUniStatComp_Type()
)
caiUniStatComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caiUniStatComp.setStatus("mandatory")
_CaiDbMgt_ObjectIdentity = ObjectIdentity
caiDbMgt = _CaiDbMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 3)
)
_CaiAppSft_ObjectIdentity = ObjectIdentity
caiAppSft = _CaiAppSft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 4)
)

# Managed Objects groups


# Notification objects

caiUniSecuT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 1)
)
caiUniSecuT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT1.setStatus(
        ""
    )

caiUniSecuT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 2)
)
caiUniSecuT2.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT2.setStatus(
        ""
    )

caiUniSecuT3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 3)
)
caiUniSecuT3.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT3.setStatus(
        ""
    )

caiUniSecuT4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 4)
)
caiUniSecuT4.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT4.setStatus(
        ""
    )

caiUniSecuT5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 5)
)
caiUniSecuT5.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT5.setStatus(
        ""
    )

caiUniSecuT6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 6)
)
caiUniSecuT6.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT6.setStatus(
        ""
    )

caiUniSecuT7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 7)
)
caiUniSecuT7.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT7.setStatus(
        ""
    )

caiUniSecuT8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 8)
)
caiUniSecuT8.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniSecuT8.setStatus(
        ""
    )

caiUniScheT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 100)
)
caiUniScheT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT1.setStatus(
        ""
    )

caiUniScheT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 101)
)
caiUniScheT2.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT2.setStatus(
        ""
    )

caiUniScheT3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 102)
)
caiUniScheT3.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT3.setStatus(
        ""
    )

caiUniScheT4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 103)
)
caiUniScheT4.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT4.setStatus(
        ""
    )

caiUniScheT5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 104)
)
caiUniScheT5.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT5.setStatus(
        ""
    )

caiUniScheT6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 105)
)
caiUniScheT6.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT6.setStatus(
        ""
    )

caiUniScheT7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 106)
)
caiUniScheT7.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT7.setStatus(
        ""
    )

caiUniScheT8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 107)
)
caiUniScheT8.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniScheT8.setStatus(
        ""
    )

caiUniGuiT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 200)
)
caiUniGuiT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniGuiT1.setStatus(
        ""
    )

caiUniTapeT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 300)
)
caiUniTapeT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT1.setStatus(
        ""
    )

caiUniTapeT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 301)
)
caiUniTapeT2.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT2.setStatus(
        ""
    )

caiUniTapeT3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 302)
)
caiUniTapeT3.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT3.setStatus(
        ""
    )

caiUniTapeT4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 303)
)
caiUniTapeT4.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT4.setStatus(
        ""
    )

caiUniTapeT5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 304)
)
caiUniTapeT5.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT5.setStatus(
        ""
    )

caiUniTapeT6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 305)
)
caiUniTapeT6.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT6.setStatus(
        ""
    )

caiUniTapeT7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 306)
)
caiUniTapeT7.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT7.setStatus(
        ""
    )

caiUniTapeT8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 307)
)
caiUniTapeT8.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT8.setStatus(
        ""
    )

caiUniTapeT9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 308)
)
caiUniTapeT9.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniTapeT9.setStatus(
        ""
    )

caiUniAsmT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 400)
)
caiUniAsmT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniAsmT1.setStatus(
        ""
    )

caiUniAsmT2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 401)
)
caiUniAsmT2.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniAsmT2.setStatus(
        ""
    )

caiUniCciT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 500)
)
caiUniCciT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniCciT1.setStatus(
        ""
    )

caiUniEnfT1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 0, 501)
)
caiUniEnfT1.setObjects(
    ("CAIMIB", "caiUniLstMsg")
)
if mibBuilder.loadTexts:
    caiUniEnfT1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAIMIB",
    **{"cai": cai,
       "caiUniSecuT1": caiUniSecuT1,
       "caiUniSecuT2": caiUniSecuT2,
       "caiUniSecuT3": caiUniSecuT3,
       "caiUniSecuT4": caiUniSecuT4,
       "caiUniSecuT5": caiUniSecuT5,
       "caiUniSecuT6": caiUniSecuT6,
       "caiUniSecuT7": caiUniSecuT7,
       "caiUniSecuT8": caiUniSecuT8,
       "caiUniScheT1": caiUniScheT1,
       "caiUniScheT2": caiUniScheT2,
       "caiUniScheT3": caiUniScheT3,
       "caiUniScheT4": caiUniScheT4,
       "caiUniScheT5": caiUniScheT5,
       "caiUniScheT6": caiUniScheT6,
       "caiUniScheT7": caiUniScheT7,
       "caiUniScheT8": caiUniScheT8,
       "caiUniGuiT1": caiUniGuiT1,
       "caiUniTapeT1": caiUniTapeT1,
       "caiUniTapeT2": caiUniTapeT2,
       "caiUniTapeT3": caiUniTapeT3,
       "caiUniTapeT4": caiUniTapeT4,
       "caiUniTapeT5": caiUniTapeT5,
       "caiUniTapeT6": caiUniTapeT6,
       "caiUniTapeT7": caiUniTapeT7,
       "caiUniTapeT8": caiUniTapeT8,
       "caiUniTapeT9": caiUniTapeT9,
       "caiUniAsmT1": caiUniAsmT1,
       "caiUniAsmT2": caiUniAsmT2,
       "caiUniCciT1": caiUniCciT1,
       "caiUniEnfT1": caiUniEnfT1,
       "caiSysMgt": caiSysMgt,
       "caiUnicenter": caiUnicenter,
       "caiUniGenlvl": caiUniGenlvl,
       "caiUniConfig": caiUniConfig,
       "caiUniLicExp": caiUniLicExp,
       "caiUniLstMsg": caiUniLstMsg,
       "caiUniCltSrv": caiUniCltSrv,
       "caiUniStatTable": caiUniStatTable,
       "caiUniStatEntry": caiUniStatEntry,
       "caiUniStatEntIdx": caiUniStatEntIdx,
       "caiUniStatComp": caiUniStatComp,
       "caiDbMgt": caiDbMgt,
       "caiAppSft": caiAppSft}
)
